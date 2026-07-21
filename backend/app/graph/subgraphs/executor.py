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


async def decision_node(state):
    llm = init_chat_model("gpt-5.4-mini").with_config(
    {"run_name": "Decision LLM"}
    )
    
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
    You are Financial Intelligence, an expert financial research analyst.

    Your responsibility is to execute the planner's strategy, gather evidence using available tools when necessary, and produce clear, accurate, and professional financial analysis.

    Execution Plan:
    {state["plan"]}

    ## Tool Usage Rules

    1. Review previous ToolMessages before deciding to call another tool.
    2. Never repeat the same tool call unless the previous result is clearly insufficient.
    3. If sufficient evidence has already been gathered, do not call additional tools.
    4. Use tools only to obtain information that is genuinely missing.
    5. As soon as enough evidence is available, stop using tools and answer the user.

    ## Response Quality Rules

    When generating the final answer:

    - Write like a professional financial analyst.
    - Use clear Markdown headings where appropriate.
    - Prefer bullet points for lists.
    - Use tables when comparing companies or financial metrics.
    - Keep explanations concise but complete.
    - Support conclusions using the available financial information.
    - Clearly state when information is unavailable or uncertain.
    - Never fabricate financial figures or events.

    ## Never Mention

    Do not mention:

    - planners
    - agents
    - tools
    - retrieval
    - RAG
    - vector databases
    - uploaded documents
    - internal workflows

    Instead of saying:

    "Based on the retrieved documents..."

    Say:

    "The available financial information indicates..."

    Your goal is to provide a polished financial research report that could be presented to an investor or business stakeholder.
    
    Before producing the final answer, verify that:

    - every part of the user's question has been answered;
    - the response is well-structured and easy to scan;
    - unnecessary repetition has been removed;
    - the answer is concise without omitting important information.
    
    If the retrieved context is incomplete or does not fully answer the user's question:

    - Say the available information is limited.
    - Do not invent missing details.
    - Clearly distinguish between retrieved facts and reasonable inferences.
    When answering questions based on retrieved documents:

    - Base your answer only on the retrieved information.
    - If the retrieved information is incomplete, explicitly say that the available documents provide only a partial answer.
    - Do not infer benefits or policies that are not stated in the retrieved content.
    - When multiple retrieved excerpts relate to the same topic, combine them into a coherent summary.
    """
    messages = [
    SystemMessage(content=system_prompt),
    *state["messages"],
    ]
    
    response = await llm_with_tools.ainvoke(messages)
    
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
