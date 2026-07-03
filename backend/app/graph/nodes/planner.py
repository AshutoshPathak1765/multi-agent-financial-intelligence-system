from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from app.schemas.internal.planner import PlannerResponse

load_dotenv()


def planner_node(state):
    llm = init_chat_model("gpt-5.4-mini")

    query = state["messages"][-1].content

    prompt = f"""
You are a specialized Financial Research Planner.

Your responsibility is to create an execution plan ONLY for company financial analysis queries.

Available information sources:

• rag
  - Use ONLY for questions about the uploaded Sun Life documents.

• search
  - Use for public companies such as Apple, Microsoft, Tesla, NVIDIA, Amazon, Google, etc.

• both
  - Use when the answer requires both the uploaded Sun Life documents and recent public financial information.

• none
  - Use when the question is NOT related to company financial analysis.

User Query:
{query}

Instructions:

1. Determine whether the query is related to company financial analysis.
2. If it is related:
   - Set out_of_scope to false.
   - Generate a concise execution plan.
   - Select the appropriate tool_strategy ("rag", "search", or "both").
   - Leave final_output as null.

3. If it is NOT related:
   - Set out_of_scope to true.
   - Set tool_strategy to "none".
   - Set plan to an empty string.
   - Set final_output to a short, polite message explaining that you only assist with company financial analysis and related financial topics.
"""
    
    structured_llm = llm.with_structured_output(PlannerResponse)
    
    response = structured_llm.invoke(prompt)
    print(response.model_dump())
    return response.model_dump()
