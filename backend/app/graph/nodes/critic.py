from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from app.schemas.api.critic import CriticResponse

load_dotenv()


def critic_node(state):
    llm = init_chat_model("gpt-5.4-mini")

    structured_llm = llm.with_structured_output(CriticResponse)

    messages = state["messages"]

    final_response = messages[-1].content

    prompt = f"""
    You are a senior financial analysis critic agent responsible for validating 
    the quality of an AI-generated financial report.

    Review the response carefully for:

    1. Factual accuracy
    2. Completeness of analysis
    3. Financial reasoning quality
    4. Clarity and coherence
    5. Whether the response fully answers the user's query

    User Query:
    {messages[0].content}

    Generated Response:
    {final_response}

    Instructions:

    - Return "approved" if the response is complete, accurate, and well-reasoned.
    - Return "retry" if:
        * important information is missing
        * reasoning is weak
        * the response is vague
        * the analysis lacks supporting evidence
        * the response does not fully answer the query

    Keep feedback concise and actionable.
    """

    response = structured_llm.invoke(prompt)

    return {
        "critic_feedback": response.feedback,
        "critic_decision": response.decision,
        "critic_attempts": state.get("critic_attempts", 0) + 1,
        "final_output": final_response,
    }
