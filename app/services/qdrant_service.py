from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import requests

from app.core.config import settings
from app.core.constants import COLLECTION_NAME

client = QdrantClient(
    host=settings.QDRANT_HOST,
    port=settings.QDRANT_PORT
)


def create_collection():
    collections = client.get_collections().collections

    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )


def store_embeddings(chunks, embeddings):
    points = []

    for index, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):
        points.append(
            PointStruct(
                id=index,
                vector=embedding,
                payload={"text": chunk}
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )


def search_embeddings(query_embedding):
    url = f"http://{settings.QDRANT_HOST}:{settings.QDRANT_PORT}/collections/{COLLECTION_NAME}/points/search"
    payload = {
        "vector": query_embedding,
        "limit": 3,
        "with_payload": True
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    data = response.json()
    
    # Convert response to match expected format
    class SearchResult:
        def __init__(self, id, score, payload):
            self.id = id
            self.score = score
            self.payload = payload
    
    results = []
    for result in data.get("result", []):
        results.append(SearchResult(
            id=result["id"],
            score=result.get("score", 0),
            payload=result.get("payload", {})
        ))
    return results