import grpc
from loguru import logger

from proto.gen.schedule import schedule_pb2_grpc
from proto.gen.schedule.schedule_pb2 import GetScheduleRequest, GetScheduleResponse, Lesson


class ScheduleService(schedule_pb2_grpc.ScheduleServicer):
    @logger.catch
    async def GetSchedule(self, request: GetScheduleRequest, context: grpc.aio.ServicerContext) -> GetScheduleResponse:
        logger.info(f"{request}")
        lessons = [Lesson(name='Бебеб',
                          start_time='2024-01',
                          end_time='2024-02'),
                   Lesson(name='Бебеб',
                          start_time='2024-01',
                          end_time='2024-02')
                   ]
        return GetScheduleResponse(lessons=lessons)
