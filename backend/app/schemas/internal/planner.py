from pydantic import BaseModel, Field
from app.core.constants import ToolStrategy


class PlannerResponse(BaseModel):
    plan: str = Field(
        description=(
            "Execution plan for financial requests only. "
            "Leave empty for casual conversation or out-of-scope requests."
        )
    )

    out_of_scope: bool = Field(
        description=(
            "True only when the user's request is unrelated to financial analysis "
            "and is not part of a normal friendly conversation."
        )
    )

    tool_strategy: ToolStrategy = Field(
        description=(
            "Information source required for financial requests. "
            "Use 'none' for casual conversation or out-of-scope requests."
        )
    )

    final_output: str | None = Field(
        default=None,
        description=(
            "Final user-facing response for casual conversation or out-of-scope "
            "requests. Leave null for financial requests."
        )
    )