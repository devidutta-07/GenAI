"""Streaming allow to get the response as it is generated, instead of waiting for the entire response 
to be generated before receiving it. This can be useful for applications that require real-time responses,
 such as chatbots or interactive applications."""

from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatMistralAI(model_name="mistral-small-latest", streaming=True)


for chunks in llm.stream("5 points on machine learning"):
    print(chunks.content, end="",flush=True)
