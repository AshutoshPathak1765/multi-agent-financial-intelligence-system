from langchain_core.messages import BaseMessage
from app.graph.runtime import get_graph
from app.schemas.internal.langgraph import GraphResult
from typing import List, AsyncGenerator


class LangGraphService:

    @staticmethod
    async def invoke(
        session_id: str,
        messages: List[BaseMessage],
    ):
        graph = get_graph()

        config = {
            "configurable": {
                "thread_id": session_id,
            },
            "metadata": {
                "session_id": session_id,
            },
            "run_name": "Financial Chat",
        }

        state = await graph.ainvoke(
            {
                "messages": messages,
                "steps": 0,
            },
            config=config,
        )

        response = (
            state["final_output"]
            if state.get("final_output")
            else state["messages"][-1].content
        )

        return GraphResult(
            response=response,
            steps=state["steps"],
            state=state,
        )

    @staticmethod
    async def stream(
        session_id: str,
        messages: List[BaseMessage],
    ) -> AsyncGenerator[str, None]:

        graph = get_graph()

        config = {
            "configurable": {
                "thread_id": session_id,
            },
            "metadata": {
                "session_id": session_id,
            },
            "run_name": "Financial Chat",
        }

        streamed_llm = False

        try:

            async for event in graph.astream_events(
                {
                    "messages": messages,
                    "steps": 0,
                },
                config=config,
                version="v2",
            ):

                try:

                    event_name = event.get("event")
                    node = event.get("metadata", {}).get("langgraph_node")

                    # -------------------------------------------------
                    # Stream Executor responses
                    # -------------------------------------------------
                    if (
                        event_name == "on_chat_model_stream"
                        and node == "decision"
                    ):

                        chunk = event.get("data", {}).get("chunk")

                        if chunk and chunk.content:
                            streamed_llm = True
                            yield chunk.content

                    # -------------------------------------------------
                    # Planner-only responses
                    # -------------------------------------------------
                    elif (
                        event_name == "on_chat_model_end"
                        and node == "planner"
                        and not streamed_llm
                    ):

                        ai_message = event.get("data", {}).get("output")

                        if ai_message is None:
                            continue

                        planner_response = (
                            ai_message.additional_kwargs.get("parsed")
                        )

                        if planner_response is None:
                            continue

                        final_output = getattr(
                            planner_response,
                            "final_output",
                            None,
                        )

                        if final_output:
                            yield final_output

                except Exception:
                    logger.exception(
                        "Error while processing LangGraph event."
                    )

        except Exception:
            logger.exception(
                "Streaming failed for session %s",
                session_id,
            )

            raise