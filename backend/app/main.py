from fastapi import FastAPI
from app.api.router import router
from fastapi.middleware.cors import CORSMiddleware
from app.models import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
