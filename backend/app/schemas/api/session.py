from datetime import datetime

from pydantic import BaseModel,Field


class CreateSessionRequest(BaseModel):
    title: str
    
    

class UpdateSessionRequest(BaseModel):
    title: str = Field(min_length=1, max_length=100) 


class SessionResponse(BaseModel):
    id: str
    user_id: str
    title: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }