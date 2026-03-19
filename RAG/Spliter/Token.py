from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders import TextLoader

data=TextLoader("RAG/Data/me.txt")

docs=data.load()

splitter=TokenTextSplitter(
    chunk_size=10,
    chunk_overlap=2
)

text=splitter.split_documents(docs)
for i in text:
    print(i.page_content)