from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.session_repository import SessionRepository

class SessionService:

    @staticmethod
    async def create_session(
        db: AsyncSession,
        user_id: str,
        title: str,
    ):
        session = await SessionRepository.create_session(
            db=db,
            user_id=user_id,
            title=title,
        )
        await db.commit()
        return session

    @staticmethod
    async def get_sessions(
        db: AsyncSession,
        user_id: str,
    ):
        return await SessionRepository.get_sessions(
            db=db,
            user_id=user_id,
        )
        
    @staticmethod
    async def validate_session_owner(
    db: AsyncSession,
    session_id: str,
    user_id: str,
):
        session = await SessionRepository.get_session_by_id(
            db=db,
            session_id=session_id,
        )

        if session is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Session not found.",
            )

        if session.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You are not authorized to access this session.",
            )

        return session
    
    @staticmethod
    async def update_title(
        db: AsyncSession,
        session_id: str,
        title: str,
    ):
        
        title = " ".join(title.split())
        session = await SessionRepository.update_title(
            db=db,
            session_id=session_id,
            title=title,
        )

        await db.commit()

        return session
    
    @staticmethod
    async def delete_session(
        db: AsyncSession,
        session_id: str,
        user_id: str,
    ):
        session = await SessionService.validate_session_owner(
            db=db,
            session_id=session_id,
            user_id=user_id,
        )

        await SessionRepository.delete_session(
            db=db,
            session=session,
        )

        await db.commit()