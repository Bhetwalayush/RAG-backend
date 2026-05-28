from app.services.embedding_service import generate_embedding
from app.services.qdrant_service import search_embeddings


def retrieve_context(query: str) -> str:
    embedding = generate_embedding(query)

    results = search_embeddings(embedding)

    context = []

    for result in results:
        context.append(result.payload["text"])

    return "\n".join(context)