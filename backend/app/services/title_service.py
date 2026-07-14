from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage


class TitleService:

    llm = init_chat_model(
        "gpt-5.4-mini",
    ).with_config(
        {
            "run_name": "Generate Chat Title",
            "tags": ["title-generation"],
        }
    )

    @staticmethod
    async def generate(
        user_message: str,
        assistant_response: str,
    ) -> str:

        prompt = f"""
Generate a concise chat title for this conversation.

Rules:
- 3 to 6 words.
- Focus on the main topic.
- Avoid generic words like "analysis", "conversation", or "discussion".
- No quotation marks.
- No trailing punctuation.
- Maximum 50 characters.

If the conversation is a greeting or casual chat,
prefer natural titles such as:

- Greeting
- General Chat
- Introduction
- Getting Started

Avoid titles like:
- Simple Greeting Exchange
- Casual Conversation
- General Discussion

User:
{user_message}

Assistant:
{assistant_response}
"""

        response = await TitleService.llm.ainvoke(
            [HumanMessage(content=prompt)]
        )

        title = response.content.strip()

        if len(title) > 50:
            title = title[:47] + "..."

        return title