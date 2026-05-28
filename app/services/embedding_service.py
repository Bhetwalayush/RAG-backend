from sentence_transformers import SentenceTransformer

from app.core.constants import EMBEDDING_MODEL

model = SentenceTransformer(EMBEDDING_MODEL)


def generate_embedding(text: str):
    return model.encode(text).tolist()