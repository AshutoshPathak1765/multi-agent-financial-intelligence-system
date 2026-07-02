from pydantic import BaseModel

class CreateSessionRequest(BaseModel):
    title: str


class ChatMessageRequest(BaseModel):
    session_id: str
    message: str


class SessionResponse(BaseModel):
    id: str
    title: str

    model_config = {
        "from_attributes": True
    }