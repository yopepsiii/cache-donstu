import grpc
from loguru import logger

from modules.api_clients.donstu_client import DonstuAPIClient
from proto.gen.schedule import schedule_pb2_grpc
from proto.gen.schedule.schedule_pb2 import GetScheduleRequest, GetScheduleResponse, Lesson


class ScheduleService(schedule_pb2_grpc.ScheduleServicer):
    @logger.catch
    async def GetSchedule(self, request: GetScheduleRequest, context: grpc.aio.ServicerContext) -> GetScheduleResponse:
       logger.info(f"{request}")
        
       client = DonstuAPIClient(access_token=request.access_token)

       request_params = {
           'educationSpaceId': request.educationSpaceID,
           'month': request.month,
           'studentId': request.studentId,
           'teacherId': request.teacherId,
           'showAll': request.showAll,
           'showJournalFilled': request.showJournalFilled,
           'years': request.years
       }

       lessons = await client.get_schedule(request_params)
       await client.close()

       return GetScheduleResponse(lessons=lessons)
       
