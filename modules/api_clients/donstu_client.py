from typing import Any, Optional, Type

from fastapi import HTTPException
from loguru import logger
from starlette import status

from typing import Optional

from modules.api_clients.base_client import BaseApiClientAbstract, RequestMethods


class DonstuAPIClient(BaseApiClientAbstract):

    __base_url = "https://edu.donstu.ru/api"

    def __init__(self, access_token: Optional[str] = ''):
        super().__init__(access_token)
        self._set_base_url(self.__base_url)

    async def check_token(self) -> str:
        res = await self.make_request(method=RequestMethods.GET,
                                      url="/tokenauth")

        logger.info(res)

        if res.status_code == 200:
            username = res.json().get("data").get('userName')
            if username:
                return username

        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Ваш токен устарел, авторизуйтесь снова.')

    async def get_schedule(self, params: dict):
        res = await self.make_request(method=RequestMethods.GET,
                                      url="/RaspManager",
                                      params=params
                                      )
        
        logger.info(res)

        raspList = res.json().get("data").get('raspList')

        if len(raspList) == 0:
            return []

        return raspList
            
        

        



