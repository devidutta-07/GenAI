from langchain_community.document_loaders import PyPDFLoader

data=PyPDFLoader("RAG/Data/data.pdf")
docs=data.load()

for doc in docs:
    print(doc.page_content)
    print("\n\n")

