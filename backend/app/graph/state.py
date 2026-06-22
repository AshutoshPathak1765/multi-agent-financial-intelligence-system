from typing import Annotated, TypedDict, List
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]
    plan: str
    steps: int
    critic_feedback: str
    out_of_scope: bool
    critic_attempts: int
    final_output: str
