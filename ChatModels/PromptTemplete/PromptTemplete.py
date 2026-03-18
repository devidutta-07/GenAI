from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(
    model_name="mistral-small-latest"
)

prompt = PromptTemplate.from_template("""
You are a movie information assistant.

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

Movie name: {movie_name}
""")

movie = input("Enter Movie Name: ")

# Chain
chain = prompt | model

result = chain.invoke({"movie_name": movie})

print(result.content)