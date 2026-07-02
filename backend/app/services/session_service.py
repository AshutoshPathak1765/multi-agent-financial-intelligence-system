from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.session_repository import SessionRepository

class SessionService:

    @staticmethod
    async def create_session(
        db: AsyncSession,
        user_id: str,
        title: str,
    ):
        return await SessionRepository.create_session(
            db=db,
            user_id=user_id,
            title=title,
        )

    @staticmethod
    async def get_sessions(
        db: AsyncSession,
        user_id: str,
    ):
        return await SessionRepository.get_sessions(
            db=db,
            user_id=user_id,
        )