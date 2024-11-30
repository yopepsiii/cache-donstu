import grpc
from fastapi import HTTPException
from loguru import logger

from modules.api_clients.base_client import RequestMethods
from modules.api_clients.donstu_client import DonstuAPIClient
from proto.gen.auth import auth_pb2_grpc
from proto.gen.auth.auth_pb2 import LoginRequest, LoginResponse


class AuthService(auth_pb2_grpc.AuthServicer):
    @logger.catch
    async def Login(self, request: LoginRequest, context: grpc.aio.ServicerContext) -> LoginResponse:

        client = DonstuAPIClient()

        data = {
            'userName': request.email,
            'password': request.password
        }

        res = await client.make_request(method=RequestMethods.POST,
                                        json=data,
                                        url='/tokenauth')
        res_data = res.json().get('data')
        if res_data == 'uNull':
            raise HTTPException(status_code=401, detail='Данные для входа не верные.')

        access_token = res_data.get('accessToken')

        if not access_token:
            raise HTTPException(status_code=401, detail='Данные для входа не верные.')

        await client.close()

        return LoginResponse(token=access_token)
