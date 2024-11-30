from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import schedule, auth

app = FastAPI(root_path='/api')

app.include_router(schedule.router)
app.include_router(auth.router)

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])
