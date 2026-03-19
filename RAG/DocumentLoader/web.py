from langchain_community.document_loaders import WebBaseLoader

url="https://learn.microsoft.com/en-us/minecraft/creator/?view=minecraft-bedrock-stable"

data=WebBaseLoader(url)
docs=data.load()

for doc in docs:
    print(doc.page_content)