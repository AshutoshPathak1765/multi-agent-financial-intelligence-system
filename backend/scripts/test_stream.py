import asyncio

from langchain_core.messages import HumanMessage
from app.services.langgraph_service import LangGraphService


async def main():
    async for token in LangGraphService.stream(
        [HumanMessage(content="Hi")]
    ):
        print(token, end="", flush=True)


asyncio.run(main())