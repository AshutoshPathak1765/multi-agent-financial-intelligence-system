from langgraph.graph import StateGraph, END
from app.graph.state import AgentState
from app.graph.nodes.basic import basic_node


def get_graph():
    graph = StateGraph(AgentState)

    graph.add_node("basic", basic_node)

    graph.set_entry_point("basic")
    graph.add_edge("basic", END)

    return graph.compile()
