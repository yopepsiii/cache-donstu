from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.datastructures import FormData
from fastapi.security import OAuth2PasswordRequestForm
from proto.gen.auth import auth_pb2_grpc
from schemas.auth import TokenOut
import grpc

router = APIRouter(tags=['Авторизация'])

@router.post('/dstu', response_model=TokenOut, summary='Войти в Edu Donstu API')
async def login_via_dstu(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    async with grpc.aio.insecure_channel('auth-service:50052') as channel:
        stub = auth_pb2_grpc.AuthStub(channel)

        response = await stub.Login()