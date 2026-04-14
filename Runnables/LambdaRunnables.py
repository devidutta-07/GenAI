# What is we want to pass different topics . Then 

from langchain_mistralai import ChatMistralAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel,RunnableLambda

llm=ChatMistralAI(model="mistral-small-latest")

parser=StrOutputParser()

small_prompt=ChatPromptTemplate.from_template(
    "Explain this {topic} in one small paragraph"
)

big_prompt=ChatPromptTemplate.from_template(
    "Explain this {topic} point wise 2-3 "
)

chains=RunnableParallel({
    "small":RunnableLambda(lambda x:x['small'])|small_prompt|llm|parser,
    "big":RunnableLambda(lambda x:x['big'])|big_prompt|llm|parser
})
response=chains.invoke({
    "small":{"topic":"Machine Learning"},
    "big":{"topic":"Deep Learning"}
})
print(response['small'])
print(response["big"])