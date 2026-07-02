from sqlalchemy.ext.asyncio import AsyncSession

from app.services.langgraph_service import LangGraphService
from app.services.message_service import MessageService


class ChatService:

    @staticmethod
    async def chat(
        db: AsyncSession,
        session_id: str,
        message: str,
    ):
        # Save the user's message
        await MessageService.create_message(
            db=db,
            session_id=session_id,
            role="user",
            content=message,
        )

        # Run LangGraph
        result = await LangGraphService.invoke(
            message=message,
            session_id=session_id,
        )

        response = result["response"]
        # Save AI response
        await MessageService.create_message(
            db=db,
            session_id=session_id,
            role="assistant",
            content=response,
        )

        return response