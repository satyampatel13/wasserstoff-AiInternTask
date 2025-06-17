import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
import uuid

# Load .env
load_dotenv()

# Path where Chroma vector database will be saved
CHROMA_PATH = "backend/data/chroma"

def split_text(content: str, chunk_size=300, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(content)

def create_vector_db(documents: list):
    all_chunks = []
    ids = []

    for doc in documents:
        chunks = split_text(doc["content"])
        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            ids.append(f"{doc['id']}_{i}")

    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_texts(texts=all_chunks, embedding=embedder, persist_directory=CHROMA_PATH, ids=ids)
    db.persist()
    print("Vector DB created and saved.")

def load_vector_db():
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedder)
