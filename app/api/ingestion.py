import os

from fastapi import APIRouter, UploadFile, File

from app.utils.pdf_loader import load_pdf_text
from app.utils.text_loader import load_text_file

from app.services.chunking_service import (
    fixed_chunking,
    overlap_chunking
)

from app.services.embedding_service import (
    generate_embedding
)

from app.services.qdrant_service import (
    create_collection,
    store_embeddings
)

router = APIRouter()


@router.post("/ingest")
async def ingest_document(
    file: UploadFile = File(...),
    strategy: str = "fixed"
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    if file.filename.endswith(".pdf"):
        text = load_pdf_text(file_path)

    else:
        text = load_text_file(file_path)

    if strategy == "overlap":
        chunks = overlap_chunking(text)

    else:
        chunks = fixed_chunking(text)

    embeddings = [
        generate_embedding(chunk)
        for chunk in chunks
    ]

    create_collection()

    store_embeddings(chunks, embeddings)

    return {
        "message": "Document ingested successfully",
        "chunks": len(chunks)
    }