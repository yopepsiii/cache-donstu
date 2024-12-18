from fastapi import FastAPI
from fastapi_cache import FastAPICache
from loguru import logger
from starlette.middleware.cors import CORSMiddleware
from routers import schedule, auth

from contextlib import asynccontextmanager
from typing import AsyncIterator
from redis import asyncio as aioredis
from fastapi_cache.backends.redis import RedisBackend
from utils import api_key_builder


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    logger.add('logs/api.log', 
		   format="{time:YYYY-MM-DD HH:mm:ss.SSS} {level} {message}",
		   level="DEBUG",
		   rotation='10 MB',
		   compression='zip'
		  )

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://redis")
    FastAPICache.init(RedisBackend(redis),
                      prefix="cache-edu",
                      key_builder=api_key_builder)
    yield

app = FastAPI(root_path='/api', lifespan=lifespan)

app.add_middleware(CORSMiddleware,
                   allow_origins=['http://localhost:5173',
                                  'http://192.168.31.122:5173'],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

app.include_router(schedule.router)
app.include_router(auth.router)

@app.get("/")
async def index():
    return {"welcome": "To my API"}