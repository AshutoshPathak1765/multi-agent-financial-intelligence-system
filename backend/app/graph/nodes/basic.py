from app.rag.retriever import retrieve_docs


def basic_node(state):
    query = state["input"]
    docs = retrieve_docs(query=query)
    # Dummy logic (replace later with LLM)
    return {"output": f"Relevant data: {docs}"}
