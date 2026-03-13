from fastapi import FastAPI
from pdf_loader import load_pdf_pages
from chunking import chunk_text_streaming
from embedding import embed
from vector_store import store_chunks
from rag_pipeline import ask

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Endee Semantic RAG Running"}

@app.post("/upload")
def upload(path: str):
    pages = load_pdf_pages(path)
    chunks = chunk_text_streaming(pages)

    embeddings = [embed(c) for c in chunks]
    store_chunks(chunks, embeddings)

    return {"status": "notes indexed"}

@app.get("/ask")
def question(q: str):
    return {"answer": ask(q)}