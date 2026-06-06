from langgraph.graph import StateGraph, END
from app.graph.state import AgentState
from app.graph.nodes.planner import planner_node
from app.graph.nodes.critic import critic_node
from app.graph.subgraphs.executor import executor_graph

MAX_CRITIC_RETRIES = 2


def critic_router(state):
    feedback = state["critic_feedback"]

    if state.get("critic_attempts", 0) >= MAX_CRITIC_RETRIES:
        return END

    if "RETRY" in feedback:
        return "executor"

    return END


def get_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("executor", executor_graph)
    graph.add_node("critic", critic_node)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "executor")
    graph.add_edge("executor", "critic")
    graph.add_conditional_edges("critic", critic_router, {"executor": "executor"})

    return graph.compile()
