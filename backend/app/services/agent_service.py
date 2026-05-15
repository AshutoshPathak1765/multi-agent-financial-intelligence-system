from app.graph.builder import get_graph

graph = get_graph()


def run_agent(user_input: str):
    result = graph.invoke({"input": user_input})

    return result
