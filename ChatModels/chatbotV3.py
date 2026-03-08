from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

model=ChatMistralAI(
    model_name="mistral-small-latest",
    max_tokens=50,
    temperature=0.2
)

messages=[]

print("------------WELCOME TO MY AI V3----------")
print("Enter 0 to stop AI ")

while(True):
    prompt=input("User : ")

    if prompt=='0':
        break

    messages.append({"role":"user","content":prompt})
    response=model.invoke(messages)
    print("Bot : ",response.content)
    messages.append({"role":"bot","content":response.content})

print(messages)

# Disadvantages 
'''
1. Entire message pass as prompt which lead to hit max token limit
'''