from langchain_core.messages import HumanMessage

from app.graph.graph import graph


class LangGraphService:

    @staticmethod
    async def invoke(
        message: str,
        session_id: str | None = None,
    ):
        state = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=message)
                ],
                "steps": 0,
            }
        )

        return {
                "response": state["messages"][-1].content,
                "steps": state["steps"],
                "state": state,  # optional, useful for debugging
        }