import asyncio
from concurrent import futures

import grpc
from loguru import logger

from proto.gen.schedule import schedule_pb2_grpc, schedule_pb2
from proto.gen.schedule.schedule_pb2 import GetScheduleRequest, GetScheduleResponse, Lesson


class ScheduleService(schedule_pb2_grpc.ScheduleServicer):
    @logger.catch
    async def GetSchedule(self, request: GetScheduleRequest, context: grpc.aio.ServicerContext) -> GetScheduleResponse:
        logger.info(f"{request}")

        return GetScheduleResponse(lessons=lessons)


async def serve():
    server = grpc.aio.server()
    schedule_pb2_grpc.add_ScheduleServicer_to_server(ScheduleService(), server)  # Запуск сервера на порту 50051
    server.add_insecure_port('[::]:50051')
    await server.start()
    logger.info('🌀 localhost:50051')
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
