from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm=ChatOllama(model="mistral:latest")

parser=StrOutputParser()

prompt=ChatPromptTemplate.from_template(
    "Explain this {topic} in 2-3 lines"
)

chain=prompt | llm|parser

response=chain.invoke({"topic":"AI"})
print(response)