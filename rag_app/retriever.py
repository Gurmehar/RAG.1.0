from __future__ import annotations

import chromadb
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

from config import settings

def get_vector_store() -> Chroma:
    settings.get_open_api_key()
    client = chromadb.HttpClient(host=settings.CHROMA_HOST, port=settings.CHROMA_PORT)
    embedding_function = OpenAIEmbeddings(model=settings.EMBEDDING_MODEL)
    return Chroma(
        collection_name=settings.CHROMA_COLLECTION, 
                  embedding_function=embedding_function, 
                  client=client)


def fetch_context(query:str,k:int|None=None) -> list[Document]:
    if not query.strip():
        return []
    vector_store = get_vector_store()
    return vector_store.similarity_search(query, k=k or settings.RETRIEVAL_K)


def fetch_context_with_score(query:str,k:int|None=None) -> list[tuple[Document,float]]:
    if not query.strip():
        return []
    vector_store = get_vector_store()
    return vector_store.similarity_search_with_score(query, k=k or settings.RETRIEVAL_K)