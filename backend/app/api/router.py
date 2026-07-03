from fastapi import APIRouter

from app.api.chat_routes import router as chat_router
from app.api.message_routes import router as message_router
from app.api.session_routes import router as session_router

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}

router.include_router(
    session_router,
    tags=["Sessions"],
)

router.include_router(
    message_router,
    tags=["Messages"],
)

router.include_router(
    chat_router,
    tags=["Chat"],
)