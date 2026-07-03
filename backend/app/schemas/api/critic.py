from pydantic import BaseModel, Field

from app.core.constants import CriticDecision


class CriticResponse(BaseModel):
    decision: CriticDecision = Field(
        description=(
            "Whether the generated financial analysis is approved or should be retried."
        )
    )

    feedback: str = Field(
        description=(
            "Short, actionable feedback explaining the evaluation."
        )
    )