import redis

from app.core.config import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)


def save_chat(session_id: str, message: str):
    redis_client.rpush(session_id, message)


def get_chat_history(session_id: str):
    return redis_client.lrange(session_id, 0, -1)