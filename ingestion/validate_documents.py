from __future__ import annotations

from langchain_core.documents import Document

REQUIRED_METADATA_SET = {"source", "category", "filename", "document_path"}

def validate_documents(documents: list[Document]) -> None:
    if not documents:
        raise RuntimeError("The list of documents is empty.")
    
    failures: list[str]=[]
    for index, doc in enumerate(documents):
        missing_metadata=REQUIRED_METADATA_SET - set(doc.metadata)
        if missing_metadata:
            failures.append(f"Document at index {index} is missing required metadata fields: {', '.join(missing_metadata)}")
        if not doc.page_content.strip():
            failures.append(f"Document at index {index} has empty page content.{doc.metadata.get('source', 'unknown')}")

    if failures:
        joined_failures="\n".join(failures)        
        raise RuntimeError(f"Document validation failed with the following issues:\n{joined_failures}")
