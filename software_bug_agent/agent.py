from google.adk.agents import Agent

from .tools import get_current_date, langchain_tool, search_tool

# --- Agent Definition (model, instructions, tools) ---
root_agent = Agent(
    model="gemini-2.5-flash",
    name="software_assistant",
    instruction="""
    You are a skilled expert in triaging and debugging software issues for a
    coffee machine company, QuantumRoast.
    """,
    tools=[get_current_date, search_tool, langchain_tool],
)