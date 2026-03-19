from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

data=TextLoader("RAG/Data/me.txt")

docs=data.load()

spliter=CharacterTextSplitter(
    separator=(""), #default use \n\n : SO it split if have 2 newline
    chunk_size=10,
    chunk_overlap=2
)
text=spliter.split_documents(docs)
for i in text:
    print(i.page_content)

