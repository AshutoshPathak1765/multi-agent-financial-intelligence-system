from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.dependencies import get_db
from app.schemas.api.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService
from app.services.session_service import SessionService
from app.auth.models import CurrentUser
from app.auth.dependencies import get_current_user
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/chat",tags=["Chat"])

@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    
    await SessionService.validate_session_owner(
    db=db,
    session_id=request.session_id,
    user_id=current_user.id,
    )
    
    result = await ChatService.chat(
        db=db,
        session_id=request.session_id,
        message=request.message,
    )

    return ChatResponse(response=result.response)

@router.post("/stream")
async def stream_chat(
    request: ChatRequest,
    current_user: CurrentUser = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    
    await SessionService.validate_session_owner(
    db=db,
    session_id=request.session_id,
    user_id=current_user.id,
    )
    
    generator = ChatService.stream(
    db=db,
    session_id=request.session_id,
    message=request.message,
    )
    
    return StreamingResponse(
    generator,
    media_type="text/plain; charset=utf-8",
    )