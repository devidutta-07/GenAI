from langchain_mistralai import ChatMistralAI
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

llm=ChatMistralAI(model="mistral-small-latest")
parser=StrOutputParser()

code_prompt=ChatPromptTemplate.from_template(
    "Generate a code on {topic} "
)
explain_prompt=ChatPromptTemplate.from_template(
    "explain the {code}"
)

seq1=code_prompt|llm|parser
# Not used the only response of code is given but no code ... (RunnablePassthrough)
seq2=RunnableParallel({
    "code":RunnablePassthrough(),
    "explanation": explain_prompt|llm|parser
})

chains=seq1 | seq2

response=chains.invoke({"topic":"palindrome"})

print(response['code'])
print(response['explanation'])