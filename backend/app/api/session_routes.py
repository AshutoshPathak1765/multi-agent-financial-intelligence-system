from fastapi import APIRouter,Depends
from app.schemas.session import CreateSessionRequest
from app.services.session_service import SessionService
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_db

router = APIRouter(prefix="/sessions",tags=["Sessions"])

@router.post("/")
async def create_session(
    payload: CreateSessionRequest,
    db: AsyncSession = Depends(get_db),
):
    session = await SessionService.create_session(
        db=db,
        user_id="test-user",
        title=payload.title,
    )

    return session

@router.get("/")
async def get_sessions(
    db: AsyncSession = Depends(get_db),
):
    sessions = await SessionService.get_sessions(
        db=db,
        user_id="test-user",
    )

    return sessions
