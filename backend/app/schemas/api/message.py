from pydantic import BaseModel
from datetime import datetime

class CreateMessageRequest(BaseModel):
    session_id: str
    role: str
    content: str
    
class MessageResponse(BaseModel):
    id: str
    session_id: str
    role: str
    content: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }