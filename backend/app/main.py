from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import router
from app.models import *

from app.core.config import CHECKPOINTER_DATABASE_URL
from app.graph.builder import get_graph
from app.graph.runtime import set_graph
from app.graph.checkpointer import (
    initialize_checkpointer,
    close_checkpointer,
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    checkpointer = await initialize_checkpointer(
        CHECKPOINTER_DATABASE_URL
    )

    compiled_graph = get_graph(
        checkpointer=checkpointer,
    )

    set_graph(compiled_graph)

    try:
        yield
    finally:
        await close_checkpointer()

app = FastAPI(
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://multi-agent-financial-intelligence.vercel.app/"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")