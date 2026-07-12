from fastapi import APIRouter,Depends,status
from app.schemas.api.session import CreateSessionRequest
from app.services.session_service import SessionService
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_db
from app.auth.models import CurrentUser
from app.auth.dependencies import get_current_user
from app.schemas.api.session import SessionResponse,UpdateSessionRequest

router = APIRouter(prefix="/sessions",tags=["Sessions"])

@router.post("", response_model=SessionResponse)
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

@router.get("", response_model=list[SessionResponse])
async def get_sessions(
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    sessions = await SessionService.get_sessions(
        db=db,
        user_id=current_user.id,
    )

    return sessions

@router.patch(
    "/{session_id}",
    response_model=SessionResponse,
)
async def update_session(
    session_id: str,
    payload: UpdateSessionRequest,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await SessionService.validate_session_owner(
        db=db,
        session_id=session_id,
        user_id=current_user.id,
    )

    session = await SessionService.update_title(
        db=db,
        session_id=session_id,
        title=payload.title,
    )

    return session

@router.delete(
    "/{session_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_session(
    session_id: str,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await SessionService.delete_session(
        db=db,
        session_id=session_id,
        user_id=current_user.id,
    )
