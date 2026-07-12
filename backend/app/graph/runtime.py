graph = None

def set_graph(compiled_graph):
    global graph
    graph = compiled_graph

def get_graph():
    if graph is None:
        raise RuntimeError("Graph has not been initialized.")
    return graph