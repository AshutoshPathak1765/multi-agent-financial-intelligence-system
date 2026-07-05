from sqlalchemy.ext.asyncio import AsyncSession
from app.services.langgraph_service import LangGraphService
from app.services.message_service import MessageService
from app.services.history_service import HistoryService
from langchain_core.messages import HumanMessage
from app.core.constants import MessageRole

class ChatService:

    @staticmethod
    async def chat(
        db: AsyncSession,
        session_id: str,
        message: str,
    ):
        async with db.begin():    
            # Save the user's message
            await MessageService.create_message(
                db=db,
                session_id=session_id,
                role=MessageRole.USER.value,
                content=message,
            )
            
            # Load conversation history
            history = await HistoryService.get_history(
                db=db,
                session_id=session_id,
            )

            # Run LangGraph
            result = await LangGraphService.invoke(messages=history)

            # Save assistant response
            await MessageService.create_message(
                db=db,
                session_id=session_id,
                role=MessageRole.ASSISTANT.value,
                content=result.response,
            )

            return result