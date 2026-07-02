from fastapi import APIRouter,Depends
from pydantic import BaseModel
from app.services.agent_service import run_agent
from app.schemas.chat import CreateSessionRequest
from app.repositories.session_repository import SessionRepository
from app.db.dependencies import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import *

router = APIRouter()

class RequestModel(BaseModel):
    input: str

@router.post("/run")
def run(request: RequestModel):
    return run_agent(request.input)

@router.get("/health")
async def health(
    db: AsyncSession = Depends(get_db)
):
    return {"status": "ok"}

@router.post("/sessions")
async def create_session(
    payload: CreateSessionRequest,
    db: AsyncSession = Depends(get_db),
):
    session = await SessionRepository.create_session(
        db=db,
        user_id="test-user",
        title=payload.title,
    )

    return session

@router.get("/sessions")
async def get_sessions(
    db: AsyncSession = Depends(get_db),
):
    sessions = await SessionRepository.get_sessions(
        db=db,
        user_id="test-user",
    )

    return sessions

# @router.post("/sessions")
# async def create_session(
#     payload: CreateSessionRequest,
#     db: AsyncSession = Depends(get_db),
# ):
#     result = await db.execute(text("SELECT 1"))
#     print(result.scalar())

#     session = await SessionRepository.create_session(
#         db=db,
#         user_id="test-user",
#         title=payload.title,
#     )

#     return session
