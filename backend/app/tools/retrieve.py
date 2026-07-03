from app.rag.retriever import retrieve_docs
from langchain_core.tools import tool


@tool
def retrieve_tool(query: str):
    """Retrieve relevant financial report excerpts and company filing data for a given query."""

    docs = retrieve_docs(query)
    return "\n\n".join(
        doc.page_content
        for doc in docs[:3]
    )
