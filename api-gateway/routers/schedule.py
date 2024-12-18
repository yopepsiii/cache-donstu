import json
from typing import Optional

import grpc
from fastapi import APIRouter, Depends, HTTPException
from google.protobuf.json_format import MessageToJson
from loguru import logger

from proto.gen.schedule import schedule_pb2_grpc
from proto.gen.schedule.schedule_pb2 import GetScheduleRequest

from schemas.auth import Token
from oauth2 import get_current_user

from fastapi_cache.decorator import cache
router = APIRouter(prefix='/schedule', tags=['Расписание'])

# TODO: сделать валидацию Pydantic для API_Gateway'я

@router.get('', summary='Получить расписание')
@cache(namespace="schedule")
async def get_schedule(education_space_id: int,
                       month: int,
                       year: str,
                       module_id: Optional[int] = None,
                       type_id: Optional[int] = None,
                       aud: Optional[str] = None,
                       theme_id: Optional[int] = None,
                       kaf_id: Optional[int] = None,
                       groups_ids: Optional[str] = None,
                       students_ids: Optional[str] = None,
                       teachers_ids: Optional[str] = None,
                       show_all: Optional[bool] = False,
                       show_journal_filled: Optional[bool] = False,
                       current_user_data: Token = Depends(get_current_user)
                       ):
    async with grpc.aio.insecure_channel('schedule-service:50051') as channel:
        stub = schedule_pb2_grpc.ScheduleStub(channel)

        normal_groups_ids = list(map(int, groups_ids.split(", ") if groups_ids else []))
        normal_students_ids = list(map(int, students_ids.split(", ") if students_ids else []))
        normal_teachers_ids = list(map(int, teachers_ids.split(", ") if teachers_ids else []))

        get_schedule_request = GetScheduleRequest(educationSpaceID=education_space_id,
                                                             month=month,
                                                             year=year,
                                                             moduleID=module_id,
                                                             typeID=type_id,
                                                             aud=aud,
                                                             themeID=theme_id,
                                                             kafID=kaf_id,
                                                             groupsIDs=normal_groups_ids,
                                                             studentsIDs=normal_students_ids,
                                                             teachersIDs=normal_teachers_ids,
                                                             showJournalFilled=show_journal_filled,
                                                             showAll=show_all,
                                                             access_token=current_user_data.access_token)
        logger.info(f"Query params: {get_schedule_request}")
        try:
            response = await stub.GetSchedule(get_schedule_request)
            return json.loads(MessageToJson(response).encode('utf-8')).get('lessons')
        except Exception as e:
            logger.error(str(e))
            raise HTTPException(status_code=500, detail="Сервис расписания в данный момент недоступен, повторите попытку позже.")
        
