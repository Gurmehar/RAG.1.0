uv init rag.1.0  
uv venv .venv
source .venv/bin/activate

add value in .gitignore
create .env 

create knowledge_base using https://deeppdf.ai/pdf-to-markdown

uv run python -m ingestion.load_documents 

uv run python -m  rag_app.app

