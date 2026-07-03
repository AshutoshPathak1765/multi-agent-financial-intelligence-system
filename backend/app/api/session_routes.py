from fastapi import APIRouter,Depends
from app.schemas.api.session import CreateSessionRequest
from app.services.session_service import SessionService
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_db
from app.auth.models import CurrentUser
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/sessions",tags=["Sessions"])

@router.post("/")
async def create_session(
    payload: CreateSessionRequest,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    session = await SessionService.create_session(
        db=db,
        user_id=current_user.id,
        title=payload.title,
    )

    return session

@router.get("/")
async def get_sessions(
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    sessions = await SessionService.get_sessions(
        db=db,
        user_id=current_user.id,
    )

    return sessions
