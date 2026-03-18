from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatMessagePromptTemplate

from dotenv import load_dotenv
load_dotenv()

model=ChatMistralAI(
    model_name="mistral-small-latest",
)

