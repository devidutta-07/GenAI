from langchain_community.tools import tool

@tool
def greeting (name:str)-> str:
    """This tool is use to greet users"""
    return f"Welcome {name} to our Website ..."

print(greeting.invoke("Devidutta"))
print(greeting.name)
print(greeting.description)
print(greeting.args)