from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
UNSTRUCTURED_API_KEY = os.getenv("UNSTRUCTURED_API_KEY")
CLERK_SECRET_KEY=os.getenv("CLERK_SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")


# Psycopg connection string for LangGraph
CHECKPOINTER_DATABASE_URL = DATABASE_URL.replace(
    "postgresql+asyncpg://",
    "postgresql://",
)