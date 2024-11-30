from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from starlette import status

from modules.api_clients.donstu_client import DonstuAPIClient
from schemas.auth import Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def verify_dstu_token(token: str, credentials_exception):
    try:
        client = DonstuAPIClient(access_token=token)
        email = await client.check_token()

        if email is None:
            raise credentials_exception

        token_data = Token(email=email, access_token=token)
        await client.close()
    except JWTError as e:
        raise credentials_exception from e

    return token_data


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не получилось подтвердить данные.",
        headers={"WWW-Authenticate": "Bearer"},
    )  # Создаем описание ошибки для неправильного токена
    return await verify_dstu_token(token, credentials_exception)
