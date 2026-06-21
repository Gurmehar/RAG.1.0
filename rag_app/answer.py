from __future__ import annotations

from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from config import settings
from rag_app.prompts import RAG_SYSTEM_PROMPT, RAG_USER_TEMPLATE
from rag_app.retriever import fetch_context

def format_context(doc:list[Document]) -> str:
    blocks=[]
    for index, doc in enumerate(doc,start=1):
        source=doc.metadata.get("source",doc.metadata.get("filename","unknown"))
        category=doc.metadata.get("category","unknown")
        blocks.append(f"[{index}] source {source} category {category}:\n{doc.page_content}")
    return "\n\n".join(blocks)

def answer_question(question:str,history:list[dict]|None=None,k:int|None=None) -> tuple[str,list[Document]]:
    del history
    documents=fetch_context(question,k=k)
    if not documents:
          return "The approved documents do not contain enough information to answer that question.\n\nSources: none", []
    
    model= ChatOpenAI(model=settings.CHAT_MODEL,temperature=0.0)
    response= model.invoke(
         [
              {"role":"system","content":RAG_SYSTEM_PROMPT},
              {"role":"user","content":RAG_USER_TEMPLATE.format(question=question,context=format_context(documents))},
         ]
    )
    return str(response.content), documents
    