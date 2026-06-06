from pydantic import BaseModel
from typing import Literal


class CriticResponse(BaseModel):
    decision: Literal["approved", "retry"]
    feedback: str
