from app.graph.graph import graph


def export_graph():
    png = graph.get_graph(xray=True).draw_mermaid_png()

    with open("langgraph_flow.png", "wb") as f:
        f.write(png)


if __name__ == "__main__":
    export_graph()