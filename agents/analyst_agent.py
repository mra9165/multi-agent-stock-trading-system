from crewai import Agent
from crewai.llm import LLM

from tools.stock_research_tool import get_stock_price
# initialise the llm
llm= LLM(
    model = "groq/llama-3.3-70b-versatile",
    temperature=0.0
)
analyst_agent=Agent(
    role="Financial Market Analyst",
    goal=(
        "Perform in-depth evaluation of publicly traded stocks using "
        "real-time market data to support informed decision-making."
    ),
    backstory=(
        "You are a veteran financial analyst with deep expertise in interpreting "
        "stock market data, technical indicators, and fundamental metrics. "
        "You specialize in producing clear, structured insights based on "
        "live market information."),
    llm=llm,
    tools=[get_stock_price],
    verbose=True
)
