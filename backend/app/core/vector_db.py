from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir, "chroma_langchain_db")


def insert_into_vector_db(documents):
    db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=persistent_directory,
        collection_name="movies_collection",
    )
return db