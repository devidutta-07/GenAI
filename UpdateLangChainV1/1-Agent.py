from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

@tool
def city_temp(city: str) -> str:
    """Get the current temperature for a given city. Always use this tool when asked about temperature."""
    return f"The current temperature in {city} is 25 degrees Celsius."

agent = create_agent(
    model="mistral-small-latest",
    tools=[city_temp],
    system_prompt="""
You are a helpful assistant.

RULES:
- If the user asks about temperature, you MUST call the city_temp tool.
- Extract the city name from the question.
- Do NOT ask follow-up questions.
- Do NOT answer yourself.
"""
)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is the current temperature in New York?"}
    ]
})

print(response)

print(response["messages"][-1].content)