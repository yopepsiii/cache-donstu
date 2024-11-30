from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
import httpx

from enum import Enum


class RequestMethods(Enum):
    POST = 'POST'
    GET = 'GET'


class BaseApiClientAbstract(ABC):
    __base_url = None

    def __init__(self, access_token: Optional[str] = None):
        """Инициализация клиента API и создание асинхронного HTTP клиента"""

        self.async_client: Optional[httpx.AsyncClient] = None
        self._create_session(access_token)

    def _set_base_url(self, base_url: str):
        self.__base_url = base_url

    def _get_base_url(self) -> str:
        return self.__base_url

    def _create_session(self, access_token: str):
        """Создание асинхронного клиента"""
        if not self.async_client:
            headers = None
            if access_token:
                headers = {"Authorization": f"Bearer {access_token}"}

            self.async_client = httpx.AsyncClient(headers=headers, timeout=30)

    async def make_request(self,
                           method: RequestMethods,
                           url: str,
                           headers: Optional[Dict[str, str]] = None,
                           params: Optional[Dict[str, Any]] = None,
                           json: Optional[Dict[str, Any]] = None) -> httpx.Response:
        """Выполнение асинхронного HTTP запроса"""
        if headers is None:
            headers = {}

        try:
            url = f'{self.__base_url}{url}'
            response = await self.async_client.request(method.value,
                                                       url=url,
                                                       headers=headers,
                                                       params=params,
                                                       json=json)
            response.raise_for_status()  # Возбудит исключение для ошибок HTTP (4xx, 5xx)
            return response
        except httpx.HTTPStatusError as e:
            # Логирование ошибок статуса
            raise ValueError(f"HTTP Error: {e.response.status_code} - {e.response.text}") from e
        except httpx.RequestError as e:
            # Логирование сетевых ошибок
            raise ConnectionError(f"Error во время коннектиона: {str(e)}") from e

    @abstractmethod
    async def check_token(self) -> bool:
        """Проверка валидности токена"""
        pass

    async def close(self):
        """Закрытие сессии HTTP клиента"""
        if self.async_client:
            await self.async_client.aclose()
