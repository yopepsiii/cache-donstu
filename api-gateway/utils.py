import hashlib
from typing import Callable, Optional
from loguru import logger
from starlette.requests import Request
from starlette.responses import Response

def api_key_builder(
        func: Callable,
        namespace: Optional[str] = "",
        request: Optional[Request] = None,
        response: Optional[Response] = None,
        args: Optional[tuple] = None,
        kwargs: Optional[dict] = None,
) -> str:
    # SOLUTION: https://github.com/long2ice/fastapi-cache/issues/26
    # print("kwargs.items():", kwargs.items())
    arguments = {}
    keys_for_multiply_users_cache_mod = ('module_id', 'type_id', 'aud', 'theme_id', 'kaf_id', 'groups_ids', 'students_ids', 'teachers_ids', 'show_all')

    user_data = kwargs.get('current_user_data')
    if user_data:
        kwargs['current_user_email'] = user_data.email
        kwargs.pop('current_user_data', None)
        del user_data

    for key, value in kwargs.items():
        if key == 'db' or value is None:
            continue

        arguments[key] = value
            
    for key in arguments.keys():
        if key in keys_for_multiply_users_cache_mod and arguments.get('show_all') == True:
            if arguments.get('current_user_email'):
                arguments.pop('current_user_email', None)
                break
            else:
                pass

    # print("request:", request, "request.base_url:", request.base_url, "request.url:", request.url)
    arguments['url'] = request.url

    prefix = f"{namespace}:"
    cache_key = (
            prefix
            + hashlib.md5(  # nosec:B303
        f"{func.__module__}:{func.__name__}:{args}:{arguments}".encode()
    ).hexdigest()
    )

    return cache_key
