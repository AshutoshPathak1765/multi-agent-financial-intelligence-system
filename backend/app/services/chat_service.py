from sqlalchemy.ext.asyncio import AsyncSession
from app.services.langgraph_service import LangGraphService
from app.services.message_service import MessageService
from app.services.history_service import HistoryService
from app.services.session_service import SessionService
from langchain_core.messages import HumanMessage
from app.core.constants import MessageRole
from typing import AsyncGenerator

class ChatService:

    @staticmethod
    async def chat(
        db: AsyncSession,
        session_id: str,
        message: str,
    ):
        try:    
            # Load history BEFORE saving the new message
            history = await HistoryService.get_history(
                db=db,
                session_id=session_id,
            )
            
            if len(history) == 0:
                title = message.strip()

                if title:
                    if len(title) > 50:
                        title = title[:47] + "..."

                    await SessionService.update_title(
                        db=db,
                        session_id=session_id,
                        title=title,
                    )
            
            # Save the user's message
            await MessageService.create_message(
                db=db,
                session_id=session_id,
                role=MessageRole.USER.value,
                content=message,
            )
            
            # Load history AFTER saving the new message
            history = await HistoryService.get_history(
                db=db,
                session_id=session_id,
            )
            
            # Run LangGraph
            result = await LangGraphService.invoke(session_id=session_id,messages=history)

            # Save assistant response
            await MessageService.create_message(
                db=db,
                session_id=session_id,
                role=MessageRole.ASSISTANT.value,
                content=result.response,
            )
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        return result
    
    @staticmethod
    async def stream(
        db: AsyncSession,
        session_id: str,
        message: str,
    ) -> AsyncGenerator[str, None]:
        try:
            # Load history BEFORE saving the new message
            history = await HistoryService.get_history(
                db=db,
                session_id=session_id,
            )
            
            if len(history) == 0:
                title = message.strip()

                if title:
                    if len(title) > 50:
                        title = title[:47] + "..."

                    await SessionService.update_title(
                        db=db,
                        session_id=session_id,
                        title=title,
                    )
            
            # Save the user's message
            await MessageService.create_message(
                db=db,
                session_id=session_id,
                role=MessageRole.USER.value,
                content=message,
            )
            
            # Load history AFTER saving the new message
            history = await HistoryService.get_history(
                db=db,
                session_id=session_id,
            )
            
            # Stream the assistant's response
            assistant_response = ""

            async for token in LangGraphService.stream(
                session_id=session_id,
                messages=history,
            ):
                assistant_response += token
                yield token
                
            # Save assistant response
            await MessageService.create_message(
                db=db,
                session_id=session_id,
                role=MessageRole.ASSISTANT.value,
                content=assistant_response,
            )
            await db.commit()
        except Exception:
            await db.rollback()
            raise