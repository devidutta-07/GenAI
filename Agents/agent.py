from langchain_mistralai import ChatMistralAI
from langchain_community.tools import tool
from dotenv import load_dotenv
from rich import print
from langchain.agents import create_agent

load_dotenv()

llm = ChatMistralAI(model_name="mistral-small-2506")

@tool
def greeting(name: str) -> str:
    """Use this tool to greet a person when the user asks for greeting."""
    return f"Welcome {name} to our Website ..."

@tool
def str_length(text: str) -> int:
    """Use this tool when the user asks for the length of any word or sentence."""
    return len(text)

system_prompt = """
You are an AI assistant with access to tools.

RULES:
- If user asks to greet → use greeting tool
- If user asks length → use str_length tool
- Always use tools when applicable
- Do not answer manually
"""

agent = create_agent(
    llm,
    tools=[greeting, str_length],
    system_prompt=system_prompt,
)

while True:
    user_input = input("You : ")
    if user_input.lower() == "exit":
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
    )

    print(response["messages"][-1].content)