from fastapi import FastAPI

from app.api.ingestion import router as ingestion_router
from app.api.chat import router as chat_router

from app.db.database import engine
from app.db.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Custom RAG Backend"
)

app.include_router(ingestion_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {
        "message": "RAG Backend Running"
    }