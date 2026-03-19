from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
load_dotenv()

embedding_model=MistralAIEmbeddings(
    model="mistral-embed"
)

data=PyPDFLoader("RAG/Data/data.pdf")

docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
)
text= splitter.split_documents(docs)


vectorstore=Chroma.from_documents(
    documents=text,  # if use docs then entire pdf is going to store at once.
    embedding=embedding_model,
    persist_directory="Chroma"
)
