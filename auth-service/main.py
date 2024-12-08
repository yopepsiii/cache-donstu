import asyncio

from loguru import logger

import grpc
from proto.gen.auth import auth_pb2_grpc
from service import AuthService


async def serve():
    server = grpc.aio.server()
    auth_pb2_grpc.add_AuthServicer_to_server(AuthService(), server)
    server.add_insecure_port('0.0.0.0:50052')
    await server.start()
    logger.info('💫  AuthService is active --- auth-service:50052')
    await server.wait_for_termination()


if __name__ == '__main__':
    logger.add('auth_service_debug.log', 
		   format="{time:YYYY-MM-DD HH:mm:ss.SSS} {level} {message}",
		   level="DEBUG",
		   rotation='10 MB',
		   compression='zip' 
		  )
    asyncio.run(serve())
