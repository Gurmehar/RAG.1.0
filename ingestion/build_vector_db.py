from __future__ import annotations

import chromadb
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from config import settings


def build_vector_db(chunks: list[Document]) -> None:
    settings.get_open_api_key()

    if not chunks:
        RuntimeError("No chunks to add to the vector database.")

    client = chromadb.HttpClient(host=settings.CHROMA_HOST, port=settings.CHROMA_PORT)
    try:
        client.delete_collection(name=settings.CHROMA_COLLECTION)
    except Exception:
        print(f"No existing collection to delete: {settings.CHROMA_COLLECTION}")

    embeddings = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)      
    vector_store=Chroma(
        client=client,
        collection_name=settings.CHROMA_COLLECTION,
        embedding_function=embeddings,
    )
    #store chunks in Batches in , as Maximum allowed batch size = 5461
    BATCH_SIZE = 1000
    for start in range(0, len(chunks), BATCH_SIZE):
        end = start + BATCH_SIZE
        batch = chunks[start:end]
        vector_store.add_documents(batch)


