from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
index = None


def create_index(text):
    global documents, index

    chunks = []

    chunk_size = 1000

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    print("Chunks created:", len(chunks))

    documents = chunks

    embeddings = model.encode(chunks)

    print("Embeddings generated")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(embeddings, dtype=np.float32))

    print("FAISS index ready")


def search(query, k=5):
    global documents, index

    if index is None:
        return ""

    query_embedding = model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding, dtype=np.float32),
        k
    )

    results = []

    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return "\n\n".join(results)