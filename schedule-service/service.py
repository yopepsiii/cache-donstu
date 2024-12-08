import grpc
from loguru import logger

from modules.api_clients.donstu_client import DonstuAPIClient
from proto.gen.schedule import schedule_pb2_grpc
from proto.gen.schedule.schedule_pb2 import GetScheduleRequest, GetScheduleResponse, Lesson
from util import convert_dict_to_lesson
from urllib.parse import urlencode


class ScheduleService(schedule_pb2_grpc.ScheduleServicer):
    @logger.catch
    async def GetSchedule(self, request: GetScheduleRequest, context: grpc.aio.ServicerContext) -> GetScheduleResponse:        
       client = DonstuAPIClient(access_token=request.access_token)

       request_params = {
           'educationSpaceID': request.educationSpaceID,
           'month': request.month,
           'groupIDs': request.groupsIDs,
           'studentsIDs': request.studentsIDs,
           'teacherIDs': request.teachersIDs,
           'showAll': request.showAll,
           'showJournalFilled': request.showJournalFilled,
           'aud': request.aud,
           'moduleID': request.moduleID,
           'typeID': request.typeID,
           'themeID': request.themeID,
           'kafID': request.kafID,
           'year': request.year
       }
       
       request_params = {key: value for key, value in request_params.items() if value not in (None, 0, [], '')}
       encoded_params = urlencode(request_params, doseq=True)

       logger.info(f"Request encoded_params: {encoded_params}")

       json_lessons = await client.get_schedule(encoded_params)

       await client.close()
       
       mapped_lessons = list(map(convert_dict_to_lesson, json_lessons))
       
       return GetScheduleResponse(lessons=mapped_lessons)
       
