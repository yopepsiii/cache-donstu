import json
from typing import Optional

import grpc
from fastapi import APIRouter, Depends
from google.protobuf.json_format import MessageToJson
from loguru import logger

from proto.gen.schedule import schedule_pb2_grpc
from proto.gen.schedule.schedule_pb2 import GetScheduleRequest

from schemas.auth import Token
from oauth2 import get_current_user

router = APIRouter(prefix='/schedule', tags=['Расписание'])


@router.get('/', summary='Получить расписание')
async def get_schedule(education_space_id: int,
                       month: int,
                       years: str,
                       student_id: Optional[int] = None,
                       teacher_id: Optional[int] = None,
                       show_all: Optional[bool] = False,
                       show_journal_filled: Optional[bool] = False,
                       current_user_data: Token = Depends(get_current_user)
                       ):
    async with grpc.aio.insecure_channel('schedule-service:50051') as channel:
        stub = schedule_pb2_grpc.ScheduleStub(channel)
        response = await stub.GetSchedule(GetScheduleRequest(educationSpaceID=education_space_id,
                                                             month=month,
                                                             studentId=student_id,
                                                             teacherId=teacher_id,
                                                             showJournalFilled=show_journal_filled,
                                                             years=years,
                                                             showAll=show_all,
                                                             access_token=current_user_data.access_token))
        logger.info(response)
        return json.loads(MessageToJson(response).encode('utf-8'))
