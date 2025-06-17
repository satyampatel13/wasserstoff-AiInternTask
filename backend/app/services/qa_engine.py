import os
from dotenv import load_dotenv
from groq import Groq
from app.services.vector_store import load_vector_db

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def search_chunks(query: str, top_k=5):
    db = load_vector_db()
    results = db.similarity_search_with_score(query, k=top_k)

    docs = []
    for doc, score in results:
        docs.append({
            "content": doc.page_content,
            "metadata": doc.metadata if doc.metadata else {},
            "score": score
        })
    return docs

def format_prompt(query: str, docs: list):
    context = "\n\n".join([f"- {doc['content']}" for doc in docs])
    prompt = f"""You are a legal assistant AI.

Answer the following question using only the context below. Provide document-wise answers with explanation and citation.

Question: {query}

Context:
{context}

Format your response like:

DOC001: Answer (Page x, Para y)
DOC002: Answer (Page a, Para b)

Then identify key themes and give summarized insight.

Begin Answer:
"""
    return prompt

def get_answer(query: str):
    docs = search_chunks(query)
    prompt = format_prompt(query, docs)

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1024
    )

    return {
        "answer": completion.choices[0].message.content,
        "docs_used": [d["content"][:100] + "..." for d in docs]  # short preview
    }
