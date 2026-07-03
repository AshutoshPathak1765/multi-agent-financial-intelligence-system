from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from app.graph.state import AgentState
from app.tools.retrieve import retrieve_tool
from app.tools.search import search_tool
from app.core.constants import ToolStrategy
from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv
import json

load_dotenv()

MAX_STEPS = 4


def decision_node(state):
    llm = init_chat_model("gpt-5.4-mini")
    
    strategy = state["tool_strategy"]
    
    if strategy == ToolStrategy.RAG:
        tools = [retrieve_tool]

    elif strategy == ToolStrategy.SEARCH:
        tools = [search_tool]

    elif strategy == ToolStrategy.BOTH:
        tools = [retrieve_tool, search_tool]

    else:
        tools = []

    llm_with_tools = llm.bind_tools(tools)

    system_prompt = f"""
    You are a Financial Research Execution Agent.

    Your task is to execute the plan created by the planner.

    Execution Plan:
    {state["plan"]}

    Rules:

1. Review all previous ToolMessages before deciding whether another tool call is needed.

2. Do NOT repeat the same tool call unless the previous tool output is clearly insufficient.

3. If retrieve_tool has already returned relevant information, use it to answer the question instead of retrieving again.

4. Only make another tool call when you require information that has not already been retrieved.

5. Once enough evidence has been collected, immediately generate the final answer.
    """
    messages = [
    SystemMessage(content=system_prompt),
    *state["messages"],
    ]
    
    response = llm_with_tools.invoke(messages)
    
    return {"messages": [response], "steps": state.get("steps", 0) + 1}


def router(state):
    if state.get("steps", 0) >= MAX_STEPS:
        return END

    return tools_condition(state)


tool_node = ToolNode([retrieve_tool, search_tool])
graph = StateGraph(AgentState)

graph.add_node("decision", decision_node)
graph.add_node("tools", tool_node)

graph.set_entry_point("decision")

graph.add_conditional_edges("decision", router, {"tools": "tools",END: END})
graph.add_edge("tools", "decision")

executor_graph = graph.compile()
