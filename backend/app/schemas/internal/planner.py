from pydantic import BaseModel, Field
from app.core.constants import ToolStrategy


class PlannerResponse(BaseModel):
    plan: str = Field(description="Execution plan for answering the query.")
    out_of_scope: bool = Field(description="Whether the query is outside the scope of company financial analysis.")
    tool_strategy: ToolStrategy = Field(description="Which information source(s) should be used.")
    final_output: str | None = Field(
        default=None,
        description="Polite message returned to the user if the query is out of scope."
    )