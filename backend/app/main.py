from fastapi import FastAPI
from app.api.router import router
from app.models import *

app = FastAPI()

app.include_router(router, prefix="/api")
