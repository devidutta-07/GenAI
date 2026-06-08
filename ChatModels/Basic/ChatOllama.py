from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from rich import print
load_dotenv()
llm=ChatOllama(model="qwen2.5-coder:3b")
print(llm.invoke("What is JavaScript").content)