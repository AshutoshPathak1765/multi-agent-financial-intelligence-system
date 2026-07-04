from fastapi import APIRouter,Depends
from app.schemas.api.message import CreateMessageRequest, MessageResponse
from app.services.message_service import MessageService
from app.db.dependencies import get_db
from app.auth.models import CurrentUser
from app.auth.dependencies import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter(prefix="/messages",tags=["Messages"],)

@router.post("",response_model=MessageResponse)
async def create_message(payload:CreateMessageRequest,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)):
    message = await MessageService.create_message(
        db=db,
        session_id=payload.session_id,
        role=payload.role,
        content=payload.content
    )
    return message

@router.get("/{session_id}",response_model=list[MessageResponse])
async def get_messages(session_id:str,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)):
    messages = await MessageService.get_messages(
        db=db,
        session_id=session_id
    )
    return messages
