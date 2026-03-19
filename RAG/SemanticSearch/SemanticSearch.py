from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

embedding_model = MistralAIEmbeddings(
    model="mistral-embed"
)

vectorstore = Chroma(
    embedding_function=embedding_model,
    persist_directory="Chroma"   
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5, "fetch_k": 20}
)

model = ChatMistralAI(model_name="mistral-small-latest")

prompt = ChatPromptTemplate.from_messages([
    ("system", """
You are a helpful AI assistant.

Answer ONLY using the provided context.
If the answer is not in the context, say:
"I could not find the answer in the document."
"""),
    ("human", """
Context:
{context}

Question:
{question}

Answer:
""")
])

print("============== AI ===============")
print("Press 0 to exit")

while True:
    query = input("Enter your question: ")

    if query == "0":
        break

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs]).strip()

    final_prompt = prompt.invoke({
        "question": query,
        "context": context
    })

    response = model.invoke(final_prompt)

    print("\nAI:", response.content)