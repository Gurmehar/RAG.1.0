uv init harborlight-rag  
uv venv .venv
source .venv/bin/activate

add value in .gitignore
create .env 

create knowledge_base using https://deeppdf.ai/pdf-to-markdown

uv run python -m ingestion.load_documents 


