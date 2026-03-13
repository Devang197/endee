import ollama
from embedding import embed
from vector_store import search

def ask(query):
    query_emb = embed(query)
    results = search(query_emb)
    print("Retrieved chunks:", results)

    context = " ".join(results)

    prompt = f"""
    Answer the question using ONLY the given context.

    Rules:
    - Answer in maximum 3 lines.
    - Do not include examples unless asked.
    - Do not add extra explanation.
    - If formula exists, include it.
    - If answer not found, say "Not found in notes".


    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    response = ollama.chat(
        model="phi",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]