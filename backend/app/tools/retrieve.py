from app.rag.retriever import retrieve_docs
from langchain_core.tools import tool

MAX_CONTEXT_CHUNKS = 5

@tool
def retrieve_tool(query: str):
    """
    Retrieve relevant excerpts from the indexed financial knowledge base.

    Use this tool whenever the answer depends on uploaded financial documents,
    benefits guides, annual reports, internal reports, or company filings stored
    in the vector database.

    Do not use this tool for current events or information outside the indexed documents.
"""
    docs = retrieve_docs(query)
    context = []

    for i, doc in enumerate(docs, start=1):
        context.append(
            f"""
    Source {i}
    File: {doc.metadata.get("filename")}
    Page: {doc.metadata.get("page_number")}

    Content:
    {doc.page_content}
    """
        )

    return "\n\n".join(context)
