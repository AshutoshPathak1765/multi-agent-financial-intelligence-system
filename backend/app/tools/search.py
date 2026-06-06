import os
from tavily import TavilyClient
from app.core.config import TAVILY_API_KEY
from langchain_core.tools import tool

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def search_tool(query: str):
    """Search recent financial news, market trends, and company updates related to a query."""
    result = tavily_client.search(query=query, search_depth="advanced")
    return result["results"]
