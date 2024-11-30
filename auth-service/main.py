import asyncio

from loguru import logger

import grpc
from proto.gen.schedule import schedule_pb2_grpc
from service import ScheduleService


async def serve():
    server = grpc.aio.server()
    schedule_pb2_grpc.add_ScheduleServicer_to_server(ScheduleService(), server)  # Запуск сервера на порту 50051
    server.add_insecure_port('0.0.0.0:50051')
    await server.start()
    logger.info('🌀 ScheduleService is active --- schedule_service:50051')
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
