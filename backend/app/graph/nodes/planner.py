from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


def planner_node(state):
    llm = init_chat_model("gpt-5.4-mini")

    query = state["messages"][-1].content

    prompt = f"""
    You are a financial research planner.

    Create a concise execution plan for the following query:

    Query:
    {query}

    The agent has access to:
    - financial document retrieval
    - financial news search
    - financial analysis tools

    Return only the plan.
    """

    response = llm.invoke(prompt)

    return {
        "plan": response.content,
    }
