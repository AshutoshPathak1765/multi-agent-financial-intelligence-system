from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from app.schemas.api.critic import CriticResponse

load_dotenv()


async def critic_node(state):
    llm = init_chat_model("gpt-5.4-mini").with_config(
    {"run_name": "Critic LLM"}
    )

    structured_llm = llm.with_structured_output(CriticResponse)

    messages = state["messages"]

    final_response = messages[-1].content

    prompt = f"""
    You are the Senior Review Analyst for Financial Intelligence.

    Your responsibility is to perform the final quality review of every response before it is delivered to the user.

    Review the response as though it were a professional financial report prepared for an investor, executive, or business stakeholder.

    User Query:
    {messages[0].content}

    Generated Response:
    {final_response}

    Evaluate the response using ALL of the following criteria.

    --------------------------------------------------
    1. Accuracy
    --------------------------------------------------

    - Financial statements are factually correct.
    - No unsupported or fabricated claims.
    - Any uncertainty is clearly stated.

    --------------------------------------------------
    2. Completeness
    --------------------------------------------------

    - Every part of the user's request has been addressed.
    - No important information has been omitted.

    --------------------------------------------------
    3. Financial Reasoning
    --------------------------------------------------

    - Conclusions are supported by evidence.
    - Financial metrics are explained where appropriate.
    - The analysis provides useful insights rather than simply listing facts.

    --------------------------------------------------
    4. Professional Writing
    --------------------------------------------------

    The response should:

    - read like a professional financial research report
    - use appropriate Markdown headings where useful
    - use bullet points for lists
    - use comparison tables when appropriate
    - remain clear, concise, and easy to scan

    --------------------------------------------------
    5. Readability
    --------------------------------------------------

    The response should:

    - avoid repetition
    - avoid unnecessary verbosity
    - use logical flow between sections

    --------------------------------------------------
    6. Implementation Leakage
    --------------------------------------------------

    Reject responses that expose internal implementation details such as:

    - retrieved documents
    - uploaded documents
    - RAG
    - retrievers
    - vector databases
    - planners
    - agents
    - internal workflows

    The user should never see references to how the system works internally.

    --------------------------------------------------
    7. Overall Quality
    --------------------------------------------------

    Ask yourself:

    "If I were reviewing this report before sending it to a paying client, would I confidently approve it?"

    Instructions:

    Return "approved" ONLY if the response:

    - is factually accurate
    - fully answers the user's question
    - demonstrates sound financial reasoning
    - is professionally written
    - is well-structured
    - avoids implementation leakage
    - contains no unsupported claims

    Otherwise return "retry".

    Feedback should:

    - be concise
    - identify the most important issue
    - explain what should be improved
    """

    response = await structured_llm.ainvoke(prompt)

    return {
        "critic_feedback": response.feedback,
        "critic_decision": response.decision,
        "critic_attempts": state.get("critic_attempts", 0) + 1,
        "final_output": final_response,
    }
