from sqlalchemy.ext.asyncio import AsyncSession
from app.services.langgraph_service import LangGraphService
from app.services.message_service import MessageService
from app.services.history_service import HistoryService
from app.services.session_service import SessionService
from app.services.title_service import TitleService
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
            # Title generation
            if len(history) == 1:
                generated_title = await TitleService.generate(
                    user_message=message,
                    assistant_response=result.response,
                )

                await SessionService.update_title(
                    db=db,
                    session_id=session_id,
                    title=generated_title,
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
            # Title generation
            if len(history) == 1:
                generated_title = await TitleService.generate(
                    user_message=message,
                    assistant_response=assistant_response,
                )

                await SessionService.update_title(
                    db=db,
                    session_id=session_id,
                    title=generated_title,
                )
            await db.commit()
        except Exception:
            await db.rollback()
            raise