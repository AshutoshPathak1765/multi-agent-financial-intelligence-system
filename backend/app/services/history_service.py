from langchain_core.messages import HumanMessage, AIMessage
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.constants import MessageRole
from app.repositories.message_repository import MessageRepository


class HistoryService:

    @staticmethod
    async def get_history(
        db: AsyncSession,
        session_id: str,
    ):
        messages = await MessageRepository.get_messages(
            db=db,
            session_id=session_id,
        )

        history = []

        for message in messages:

            if message.role == MessageRole.USER.value:
                history.append(
                    HumanMessage(
                        content=message.content
                    )
                )

            elif message.role == MessageRole.ASSISTANT.value:
                history.append(
                    AIMessage(
                        content=message.content
                    )
                )
                
        return history