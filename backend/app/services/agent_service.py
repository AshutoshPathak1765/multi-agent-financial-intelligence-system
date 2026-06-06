from app.graph.builder import get_graph
from langchain_core.messages import HumanMessage

graph = get_graph()

graph_png = graph.get_graph(xray=True).draw_mermaid_png()

with open("langgraph_flow.png", "wb") as f:
    f.write(graph_png)


def run_agent(user_input: str):
    result = graph.invoke(
        {
            "messages": [HumanMessage(content=user_input)],
            "steps": 0,
        }
    )

    return result
