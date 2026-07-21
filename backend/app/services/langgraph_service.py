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

        async for event in graph.astream_events(
            {
                "messages": messages,
                "steps": 0,
            },
            config=config,
            version="v2",
        ):
            print("=" * 80)
            print(event["event"])
            print(event.get("metadata"))

            event_name = event.get("event")
            node = event.get("metadata", {}).get("langgraph_node")

            # Normal financial-response streaming
            if (
                event_name == "on_chat_model_stream"
            ):
                chunk = event["data"]["chunk"].content
                print("=" * 80)
                print(f"NODE: {node}")
                print(f"EVENT: {event_name}")
                print(f"CHUNK: {repr(chunk)}")

                if chunk:
                    streamed_llm = True
                    yield chunk

            # Planner-only response (Hi, Hello, Thanks...)
            elif (
                event_name == "on_chain_end"
            ):
                print("=" * 80)
                print(f"CHAIN END NODE: {node}")
                print(event["data"])
                output = event["data"].get("output")

                if (
                    not streamed_llm
                    and isinstance(output, dict)
                    and output.get("final_output")
                ):
                    yield output["final_output"]