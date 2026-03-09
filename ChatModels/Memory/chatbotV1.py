from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(
    model_name="mistral-small-latest",
    max_tokens=50,
    temperature=0.7
)
print("------------WELCOME TO MY AI V1---------")
while(True):
    prompt=input("User : ")
    response=model.invoke(prompt)
    print("Bot : ",response.content)

# DrawBack
""" 
1. No Context to previous conversations
"""
