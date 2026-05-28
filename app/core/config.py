from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GEMINI_API_KEY: str

    QDRANT_HOST: str
    QDRANT_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()