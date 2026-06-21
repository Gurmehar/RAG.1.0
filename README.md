uv init rag.1.0  
uv venv .venv
source .venv/bin/activate

add value in .gitignore
create .env 

create knowledge_base using https://deeppdf.ai/pdf-to-markdown

uv run python -m ingestion.load_documents 

uv run python -m  rag_app.app


🚀 My First RAG Project: RAG.1.0


The idea was simple:

For this first version, I used **Head First Design Patterns, 2nd Edition** as the knowledge base. The assistant can answer questions related to design patterns explained in the book.

Tech stack used:

✅ OpenAI `gpt-4o-mini` as the chat model
✅ OpenAI `text-embedding-3-large` as the embedding model
✅ ChromaDB as the vector database
✅ LangChain for building the RAG pipeline
✅ Python for implementation




