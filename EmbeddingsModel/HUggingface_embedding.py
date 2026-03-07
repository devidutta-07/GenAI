from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
# Downloaded Locally
embeddings=HuggingFaceEmbeddings(
    model_name="ibm-granite/granite-embedding-small-english-r2"
)

vector=embeddings.embed_query("I am a Good Boy")
print(vector)