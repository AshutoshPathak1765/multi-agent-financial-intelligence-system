from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from app.graph.state import AgentState
from app.tools.registry import TOOLS
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import json

load_dotenv()

MAX_STEPS = 4


def decision_node(state):
    llm = init_chat_model("gpt-5.4-mini")

    llm_with_tools = llm.bind_tools(TOOLS)

    system_prompt = f"""
    You are a financial research executor agent.

    Your job is to execute the following plan:

    {state["plan"]}

    Use the available tools whenever necessary.

    Continue reasoning step-by-step until the task is complete.
    """

    messages = [{"role": "system", "content": system_prompt}, *state["messages"]]

    response = llm_with_tools.invoke(messages)

    return {"messages": [response], "steps": state.get("steps", 0) + 1}


def router(state):
    if state.get("steps", 0) >= MAX_STEPS:
        return END

    return tools_condition(state)


tool_node = ToolNode(TOOLS)
graph = StateGraph(AgentState)

graph.add_node("decision", decision_node)
graph.add_node("tools", tool_node)

graph.set_entry_point("decision")

graph.add_conditional_edges("decision", router, {"tools": "tools",END: END})
graph.add_edge("tools", "decision")

executor_graph = graph.compile()
