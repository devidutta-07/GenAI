from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

llm=ChatMistralAI(model_name="mistral-small-latest")

tool=TavilySearchResults(max_reasult=5,topic='news')

parser=StrOutputParser()

prompt=ChatPromptTemplate.from_template("""
You are a News Summerizer AI who convert the {news} to small bullet points
""")
news=tool.run("Find the news about finance in 2026 in India")
chains=prompt|llm|parser

response=chains.invoke({"news":news})
print(response)