from anyio import Path
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tutor.llm import llm
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader

## Combine User question, retrieved context and LLM generation.

loader = PyPDFLoader("data/curriculum/dsa_intro.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.from_documents(chunks, embeddings)


#vectorstore = FAISS.load_local(
#    db,
#    embeddings,
#    allow_dangerous_deserialization=True
#)

retriever = db.as_retriever(search_kwargs={"k": 4})

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)
