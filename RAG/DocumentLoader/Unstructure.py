from langchain_community.document_loaders import UnstructuredPDFLoader
# remove space and other 
loader = UnstructuredPDFLoader("RAG/Data/data.pdf")
docs = loader.load()

for doc in docs:
    print(doc.page_content)