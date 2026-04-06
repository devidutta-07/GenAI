# If want the value genrrated at a point use in result

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

llm=ChatOllama(model="mistral:latest")

parser=StrOutputParser()

code_prompt=ChatPromptTemplate.from_template(
    "Write a program on {topic}"
)

explain_prompt=ChatPromptTemplate.from_template(
    "Explain this {code}"
)
chains=code_prompt|llm|parser|{"code":RunnablePassthrough()}|explain_prompt|llm|parser
response=chains.invoke({"topic":"addition of 3 numbers in python"})
print(response)

# Now its just giving code explanation . To get code we need to use ParallelRunnables and create a separate branch to store code