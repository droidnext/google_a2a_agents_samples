from datetime import datetime

# ----- Example of a Function tool -----
def get_current_date() -> dict:
    """
    Get the current date in the format YYYY-MM-DD
    """
    return {"current_date": datetime.now().strftime("%Y-%m-%d")}

# ----- Built-in Tool Imports -----
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

# ----- Example of a Built-in Tool -----
search_agent = Agent(
    model="gemini-2.5-flash",
    name="search_agent",
    description="A specialist in Google Search.",
    instruction="""
    You're a specialist in Google Search.
    """,
    tools=[google_search],
)

search_tool = AgentTool(search_agent)    


# ----- Example of a Third-Party Tool -----
from google.adk.tools.langchain_tool import LangchainTool
from langchain_community.tools import StackExchangeTool
from langchain_community.utilities import StackExchangeAPIWrapper

stack_exchange_tool = StackExchangeTool(api_wrapper=StackExchangeAPIWrapper())
langchain_tool = LangchainTool(stack_exchange_tool)