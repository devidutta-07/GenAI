from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

data=PyPDFLoader("RAG/Data/data.pdf")

docs=data.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=5,
)
text= splitter.split_documents(docs)
for i in text:
    print(i.page_content)
    print("\n\n\n")
embedding_model=MistralAIEmbeddings(
    model="mistral-embed-2312"

)

vector=embedding_model.embed_documents([docs[0].page_content])
print(vector)

'''
Genrally it is best to use the embedding_model directly intializing VectoreStore
'''