"""Batch processing allows you to submit multiple requests to the API at once, which can improve 
performance and reduce latency."""


from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatMistralAI(model_name="mistral-small-latest", streaming=True)
responses=llm.batch([
    "What is the capital of France?",
    "What is the capital of Germany?",
    "What is the capital of Italy?"
])
for response in responses:
    print(response.content)