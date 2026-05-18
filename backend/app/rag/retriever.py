from app.core.vector_db import get_vector_db

db = get_vector_db()

retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5},
)


def retrieve_docs(query: str):
    response = retriever.invoke(query)
    return response
