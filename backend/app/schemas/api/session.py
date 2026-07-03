from datetime import datetime

from pydantic import BaseModel


class CreateSessionRequest(BaseModel):
    title: str


class SessionResponse(BaseModel):
    id: str
    user_id: str
    title: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }