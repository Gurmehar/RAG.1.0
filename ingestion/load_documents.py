from __future__ import annotations

from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document

from config import settings

def _chapter_number_as_category(path:Path)->str:
    try:
        parts=path.relative_to(settings.KNOWLEDGE_BASE_PATH).parts[0].split("-",2)
        chapter_number="-".join(parts[:2])
        #print(f"chapter: {chapter_number}")
        return chapter_number
    except Exception as e:
        print(f"Error extracting chapter number from path {path}: {e}")
        return "Unknown"

def load_documents()->list[Document]:
    if not settings.KNOWLEDGE_BASE_PATH.exists():
        raise FileNotFoundError(f"Knowledge base path does not exist: {settings.KNOWLEDGE_BASE_PATH}")
    print(f"Loading Markdown documents from {settings.KNOWLEDGE_BASE_PATH}...")
    loader = DirectoryLoader(
        str(settings.KNOWLEDGE_BASE_PATH),
        glob="*.md",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
        show_progress=True,
    )    
    documents = loader.load()
    if not documents:
        print(f"Warning: No documents found in {settings.KNOWLEDGE_BASE_PATH}")

    enriched: list[Document] = []
    for doc in documents:
        source_path=Path(doc.metadata.get("source", "")).resolve()
        relative_path=source_path.relative_to(settings.KNOWLEDGE_BASE_PATH)

        metadata = {
            **doc.metadata,
            "source": relative_path.as_posix(),
            "category": _chapter_number_as_category(source_path),
            "filename": source_path.name,
            "document_path":relative_path.as_posix(),
        }
        enriched.append(Document(page_content=doc.page_content, metadata=metadata))
    print(f"Loaded {enriched[0]} and base docs is {documents[0]}")    
    return enriched    

# enriched = load_documents()
# print(f"Loaded {len(enriched)} documents")

# for doc in enriched[:5]:
#     print("-" * 80)
#     print("Content preview:")
#     print(doc.page_content[:30])
#     print()
#     print("Metadata:")
#     print(doc.metadata)