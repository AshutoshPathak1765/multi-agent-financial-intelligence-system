from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.message_repository import MessageRepository


class MessageService:

    @staticmethod
    async def create_message(
        db: AsyncSession,
        session_id: str,
        role: str,
        content: str,
    ):
        return await MessageRepository.create_message(
            db=db,
            session_id=session_id,
            role=role,
            content=content,
        )

    @staticmethod
    async def get_messages(
        db: AsyncSession,
        session_id: str,
    ):
        return await MessageRepository.get_messages(
            db=db,
            session_id=session_id,
        )