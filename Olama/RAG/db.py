from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

embedding=OllamaEmbeddings(model="qwen3-embedding:0.6b")
data=PyPDFLoader("Olama/RAG/resume2.pdf")
docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=50
)
texts =splitter.split_documents(documents=docs)

vectorDB=Chroma.from_documents(
    embedding=embedding,
    documents=texts,
    persist_directory="Resume"
)