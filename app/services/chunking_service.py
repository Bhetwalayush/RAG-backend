from typing import List


def fixed_chunking(
    text: str,
    chunk_size: int = 500
) -> List[str]:

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def overlap_chunking(
    text: str,
    chunk_size: int = 500,
    overlap: int = 100
) -> List[str]:

    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks