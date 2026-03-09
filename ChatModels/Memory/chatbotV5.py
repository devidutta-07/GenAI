from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
from collections import deque
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage

load_dotenv()

model=ChatMistralAI(
    model_name="mistral-small-latest",
    max_tokens=50,
    temperature=0.2
)

messages=deque(maxlen=5)
messages.append(SystemMessage(content="You are a Funny ChatBot"))

print("------------WELCOME TO MY AI V3----------")
print("Enter 0 to stop AI ")

while(True):
    prompt=input("User : ")

    if prompt=='0':
        break

    messages.append(HumanMessage(content=prompt))
    response=model.invoke(list(messages))
    print("Bot : ",response.content)
    messages.append(AIMessage(content=response.content))


print(messages)

# Disadvantages 
'''
1. After 5th Iteration System Message Removed .(We can store StstemMessage in a variable and pass with each prompt)
2. Gving entire message with response_metadata ..etc which increase API cost 
3. Summarize old chat
'''