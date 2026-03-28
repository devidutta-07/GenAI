from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatMistralAI(
    model_name="mistral-small-latest",
)
class format (BaseModel):
    titel:str
    genre:List[str]
    director:Optional[str]
    rating:Optional[float]  

parser=PydanticOutputParser(pydantic_object=format)

prompt=ChatPromptTemplate.from_messages([
    ("system","You are a Movie Details Extractor . Extract movie deatils like this {format}"),
    ("human","Extract Movie Details : {movie_name}")
]
)
movie=input("Enter Movie Name :")

final_prompt=prompt.invoke({
    "movie_name":movie,
    "format": parser.get_format_instructions()
})

response=model.invoke(final_prompt)

print(final_prompt)
print(response.content)


""" 
There are two others ways to have structured output 
1. TypeDict 
2. Dataclass
Difference 
| Method        | Validation        | Performance     | Best Use                    |
| ------------- | ----------------- | --------------- | --------------------------- |
| **Pydantic**  | Strong validation | Slightly slower | Production APIs             |
| **TypedDict** | No validation     | Fast            | Simple JSON structure       |
| **Dataclass** | Medium            | Fast            | Pythonic structured objects |
"""