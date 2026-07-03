from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.message import Message


class MessageRepository:

    @staticmethod
    async def create_message(
        db: AsyncSession,
        session_id: str,
        role: str,
        content: str,
    ):
        message = Message(
            session_id=session_id,
            role=role,
            content=content,
        )

        db.add(message)
       # Send INSERT to PostgreSQL without committing
        await db.flush()
       # Populate generated values (UUID, timestamps, etc.)
        await db.refresh(message)
        
        return message

    @staticmethod
    async def get_messages(
        db: AsyncSession,
        session_id: str,
    ):
        result = await db.execute(
            select(Message)
            .where(Message.session_id == session_id)
            .order_by(Message.created_at.asc())
        )

        return result.scalars().all()