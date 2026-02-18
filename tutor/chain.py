from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain

from tutor.llm import llm
from tutor.rag import retriever
from tutor.memory import memory

## Enables model to behave like a patient tutor.
def build_chain():
    prompt = PromptTemplate(
    template="""
    You are a patient AI tutor.

    Rules:
    - Explain concepts step-by-step
    - Use examples before definitions
    - Ask a follow-up question if the student may be confused
    - Keep answers concise unless asked to elaborate

    Context:
    {context}

    Chat history:
    {chat_history}

    Question:
    {question}

    Answer:
    """,
        input_variables=["context", "chat_history", "question"]
    )

    tutor_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

    return tutor_chain

"""
while True:
    q = input("Student: ")
    if q.lower() == "exit":
        break

    result = tutor_chain.invoke({"question": q})
    print("Tutor:", result["answer"])
"""