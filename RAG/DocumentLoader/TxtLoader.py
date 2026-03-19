from langchain_community.document_loaders import TextLoader

data=TextLoader("RAG/Data/me.txt")

docs=data.load()

print(docs)
print()
print(docs[0].page_content)
print()
for doc in docs:
    print(doc.page_content)