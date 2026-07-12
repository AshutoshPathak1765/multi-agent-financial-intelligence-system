from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from app.db.base import Base
from datetime import datetime,UTC
from sqlalchemy import DateTime

class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4())
    )

    user_id: Mapped[str] = mapped_column(
        String(255),
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255)
    )

    messages = relationship(
        "Message",
        back_populates="session",
        cascade="all, delete-orphan"
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )