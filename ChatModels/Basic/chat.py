from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
 
load_dotenv()

llm = ChatMistralAI(
    model_name="mistral-small-latest",
    temperature=0
)

response = llm.invoke("Explain what is machine learning")

print(response.content) 