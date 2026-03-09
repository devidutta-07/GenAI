from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from collections import deque

load_dotenv()

model=ChatMistralAI(
    model_name="mistral-small-latest",
    max_tokens=50,
    temperature=0.2
)
messages = deque(maxlen=3) #Last 3 messages from top 


print("------------WELCOME TO MY AI V3----------")
print("Enter 0 to stop AI ")

while(True):
    prompt=input("User : ")

    if prompt=='0':
        break

    messages.append({"role":"user","content":prompt})
    response=model.invoke(list(messages))
    print("Bot : ",response.content)
    messages.append({"role":"bot","content":response.content})

print(messages)

# Disadvantages 
'''
1. This bot is generic . We want the bot to beheve in a specific way (SystemMessage)
2. In Langchain their is better ways to handel messages
'''