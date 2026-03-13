import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)
documents = []

def store_chunks(chunks, embeddings):
    global documents
    index.reset()           # clears old vectors
    documents.clear()       # clears old text

    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)
    documents.extend(chunks)

def search(query_embedding):
    query = np.array([query_embedding]).astype("float32")
    D, I = index.search(query, 1)
    return [documents[i] for i in I[0]]