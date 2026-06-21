"""Central settings for ingestion, retrieval, evaluation, and apps."""
from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
PROJECT_ROOT=Path(__file__).resolve().parents[1]
KNOWLEDGE_BASE_PATH=PROJECT_ROOT/"knowledge_base"
EVALUATION_TESTS_PATH = PROJECT_ROOT/"evaluation"/"tests.jsonl"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

CHROMA_HOST = os.getenv("CHROMA_HOST", "localhost")
CHROMA_PORT = os.getenv("CHROMA_PORT", "8000")
CHROMA_COLLECTION = os.getenv("CHROMA_COLLECTION", "headfirstpatterns")

CHAT_MODEL = os.getenv("MY_CHAT_MODEL", "gpt-4.1-nano")
EMBEDDING_MODEL = os.getenv("OLD_EMBEDDING_MODEL", "text-embedding-3-large")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "350"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "100"))
RETRIEVAL_K = int(os.getenv("RETRIEVAL_K", "6"))

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
RAG_APP_PORT = int(os.getenv("RAG_APP_PORT", "7860"))
EVALUATOR_PORT = int(os.getenv("EVALUATOR_PORT", "7861"))

def get_open_api_key():
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is not set in environment variables, add values in .env file ")
    return OPENAI_API_KEY


def get_chroma_connection_string() -> str:
    return f"http://{CHROMA_HOST}:{CHROMA_PORT}"