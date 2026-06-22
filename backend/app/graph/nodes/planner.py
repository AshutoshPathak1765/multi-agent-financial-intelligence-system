from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()


def planner_node(state):
    llm = init_chat_model("gpt-5.4-mini")

    query = state["messages"][-1].content

    prompt = f"""
    You are a specialized Financial Research Planner.

Your responsibility is to create an execution plan ONLY for queries related to company financial analysis.

The agent has access to:

* financial document retrieval
* financial news search
* financial analysis tools

Query:
{query}

First determine whether the query is related to:

* Company financial performance
* Revenue, profit, earnings, cash flow
* Balance sheets and financial statements
* SEC filings, annual reports, quarterly reports
* Investor presentations
* Financial ratios and key metrics
* Business segments and growth trends
* Industry and competitive analysis
* Corporate risks and opportunities
* Financial forecasting and investment research

If the query is related to company financial analysis:

* Create a concise, step-by-step execution plan.
* Use only the tools necessary to answer the query.
* Return only the plan.

If the query is in scope, return:

PLAN:
<execution plan>

If the query is out of scope, return:

OUT_OF_SCOPE:
<polite message>
    """

    response = llm.invoke(prompt)
    
    plan=response.content.strip()
    
    user_message=(
            "I'm a specialized Financial Intelligence Assistant focused on "
            "company financial analysis.\n\n"
            "I can help with earnings reports, financial statements, revenue "
            "and profit trends, SEC filings, business performance, risks, "
            "competitive analysis, and market research.\n\n"
            "Please ask a question related to a company's financial or "
            "business performance."
        )
    
    if plan.startswith("OUT_OF_SCOPE"):
        return {
            "plan": "",
            "out_of_scope": True,
            "final_output": user_message
        }

    return {
        "plan": plan,
        "out_of_scope": False
    }
