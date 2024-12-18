import json
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.datastructures import FormData
from fastapi.security import OAuth2PasswordRequestForm
from proto.gen.auth import auth_pb2_grpc
from proto.gen.auth.auth_pb2 import LoginRequest
from schemas.auth import TokenOut

from loguru import logger

from google.protobuf.json_format import MessageToJson
import grpc

router = APIRouter(tags=['Авторизация'])

@router.post('/login_dstu', response_model=TokenOut, summary='Войти в Edu Donstu API')
async def login_via_dstu(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    async with grpc.aio.insecure_channel('auth-service:50052') as channel:
        stub = auth_pb2_grpc.AuthStub(channel)

        logger.info(f"Тело запроса: {form_data}")
        
        try:
            response = await stub.Login(LoginRequest(email=form_data.username,
                                                 password=form_data.password,
                                                 app_id=0))
            return {'access_token': response.token,
                    'type': 'bearer'}
        except Exception as e:
            logger.error(str(e))
            raise HTTPException(status_code=401, detail="Неверно введены логин или пароль.")