from langchain_ollama import ChatOllama ,OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma  import Chroma
llm =ChatOllama(
    model="mistral:latest"
)
embedding=OllamaEmbeddings(model="qwen3-embedding:0.6b")
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful AI assistant.\n"
     "Use the provided context (a resume) to answer the user's question.\n"
     "Be concise and accurate.\n"
     "If the answer is not in the context, say 'I don't know based on the resume.'"),
    
    ("human",
     "Resume Context:\n{context}\n\n"
     "User Question:\n{question}")
])

vectorDB=Chroma(
    embedding_function=embedding,
    persist_directory="Resume"
)
retriver=vectorDB.as_retriever(
    search_type="mmr",
    search_kwargs={"k":4,"fetch_k":10}

)
while True:
    query=input("\nAsk Question from document :")
    if query.lower== "exit":
        break
    docs=retriver.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs]).strip()

    final_prompt=prompt.invoke({"context":context,"question":query})
    chunks=llm.stream(final_prompt)
    for chunk in chunks:
        print(chunk.content,end="",flush=True)