from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

## Load PDF, split into chunks and prepare for embedding.
loader = PyPDFLoader("data/curriculum/dsa_intro.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(docs)

print(f"Created {len(chunks)} chunks")

## Prepare Embeddings, Convert text → vectors so we can search by meaning, not keywords.

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

## Enable similarity search for RAG

vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("vector_db")


