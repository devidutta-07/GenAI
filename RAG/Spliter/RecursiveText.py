from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader("RAG/Data/data.pdf")
docs=data.load()

# for doc in docs:
#     print(doc.page_content)
#     print("\n\n")

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=5,
)
text= splitter.split_documents(docs)
for i in text:
    print(i.page_content)
    print("\n\n\n")