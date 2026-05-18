from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "chroma_langchain_db")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


def insert_into_vector_db(docs):
    db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persistent_directory,
        collection_name="financial_docs",
    )
    return db


def get_vector_db():

    db = Chroma(
        persist_directory=persistent_directory,
        embedding_function=embeddings,
        collection_name="financial_docs",
    )

    return db
