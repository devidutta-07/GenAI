from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.chat import ChatMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model_name="mistral-small-latest"
)

# Create message templates
system_message = ChatMessagePromptTemplate.from_template(
    role="system",
    template="""You are a movie information assistant.

The user will provide a movie name. Your task is to extract and return detailed information about the movie in strictly valid JSON format.

Include the following fields:
- title
- genre (as a list)
- release_year
- director
- cast (as a list of main actors)
- language
- country
- plot_summary (short, 2-3 lines)
- imdb_rating (if available)

Rules:
- Return ONLY JSON. No explanation, no extra text.
- If any information is not available, use null.
- Ensure the JSON is properly formatted and valid.
"""
)

human_message = ChatMessagePromptTemplate.from_template(
    role="human",
    template="Movie name: {movie_name}"
)

# Combine into chat prompt
prompt = ChatPromptTemplate.from_messages([
    system_message,
    human_message
])

movie = input("Enter Movie Name: ")

chain = prompt | model
result = chain.invoke({"movie_name": movie})

print(result.content)