
from langchain_mistralai import ChatMistralAI
from langchain_community.tools import tool
from dotenv import load_dotenv
from rich import print

load_dotenv()

llm=ChatMistralAI(model_name="mistral-small-latest")

# TOOL CREATE
@tool
def greeting (name:str)-> str:
    """This tool is use to greet users"""
    return f"Welcome {name} to our Website ..."
@tool
def str_length (text:str)-> int:
    """This tool return the length of the  given string"""
    return len(text)

#tools Dictionary
tool={
    "greeting":greeting,
    "str_length":str_length
}

# TOOL BINDING
model=llm.bind_tools([greeting,str_length])
# print(model)

# TOOL CALLING
response=model.invoke("new user Devidutta")
# print(response)
# print(response.content) : Nothing print becasuse content is empty . AI is suggesting tool call . WE have to write code to exicute


# TOOL EXICUTION

if response.tool_calls :
    tool_name=response.tool_calls[0]["name"]
    result=tool[tool_name].invoke(response.tool_calls[0])  # TypeError / KeyError / not subscriptable : Create tool dictionary
    print(result.content)