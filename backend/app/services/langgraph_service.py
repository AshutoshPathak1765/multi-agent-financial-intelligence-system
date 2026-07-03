from langchain_core.messages import HumanMessage,BaseMessage
from app.services.history_service import HistoryService
from app.graph.graph import graph
from app.schemas.internal.langgraph import GraphResult
from typing import List

class LangGraphService:

    @staticmethod
    async def invoke(
        messages: List[BaseMessage],
    ):
        state = graph.invoke(
            {
                "messages": messages,
                "steps": 0,
            }
        )
        
        response=(state["final_output"] if state["out_of_scope"] else state["messages"][-1].content)
        
        return GraphResult(
            response=response,
            steps=state["steps"],
            state=state,
        )