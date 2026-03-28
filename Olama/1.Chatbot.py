from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm =ChatOllama(
    model="mistral:latest"
)

# response=llm.invoke("What is the capital of France?")
# print(response.content)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a funny assistant. 
    Answer the question in a humorous way.
    Dont add anything Just the joke. 
    . Give Indian vibe"""),
    ("human", " give me joke about {topic} "),
])

print("====== What a Joke ('exit' to quit)=====")
while True:
    topic = input("Enter a topic for a joke : ")
    if topic.lower()=="exit" :
        break

    final_prompt=prompt.invoke({"topic":topic})
    response=llm.invoke(final_prompt)
    print(response.content)

