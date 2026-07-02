from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.session import ChatSession


class SessionRepository:

    @staticmethod
    async def create_session(
        db: AsyncSession,
        user_id: str,
        title: str,
    ):
        session = ChatSession(
            user_id=user_id,
            title=title,
        )

        db.add(session)
        await db.commit()
        await db.refresh(session)

        return session

    @staticmethod
    async def get_sessions(
        db: AsyncSession,
        user_id: str,
    ):
        result = await db.execute(
            select(ChatSession)
            .where(ChatSession.user_id == user_id)
            .order_by(ChatSession.created_at.desc())
        )

        return result.scalars().all()