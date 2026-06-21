from __future__ import annotations

from rich.console import Console
from config import settings
from ingestion.build_vector_db import build_vector_db
from ingestion.chunk_documents import split_documents
from ingestion.load_documents import load_documents
from ingestion.validate_documents import validate_documents

console = Console()

def main() -> None:
    console.rule("Rag 1.0 Ingestion Pipeline")
    console.print(f"Knowledge base: {settings.KNOWLEDGE_BASE_PATH}")
    console.print(f"ChromaDB: {settings.CHROMA_HOST}:{settings.CHROMA_PORT}")
    console.print(f"Collection: {settings.CHROMA_COLLECTION}")
    console.print(f"Embedding model: {settings.EMBEDDING_MODEL}")

    settings.get_open_api_key()
    documents = load_documents()
    validate_documents(documents)
    chunks = split_documents(documents)
    build_vector_db(chunks)

if __name__ == "__main__":
    main()

