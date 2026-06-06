from app.tools.registry import TOOLS


def basic_node(state):
    query = state["input"]
    docs = TOOLS["retrieve"](query)
    analysis = TOOLS["analyze"](str(docs))
    return {"output": analysis}
