uv init rag.1.0  
uv venv .venv
source .venv/bin/activate

add value in .gitignore
create .env 

create knowledge_base using https://deeppdf.ai/pdf-to-markdown

uv run python -m ingestion.load_documents 

uv run python -m  rag_app.app



Absolutely — here’s a polished LinkedIn post you can use. I kept it honest, beginner-friendly, and experience-focused.

🚀 My First RAG Project: RAG.1.0

I recently built my first Retrieval-Augmented Generation application, and I wanted to share the experience with my network.

The idea was simple:

Can I build an AI assistant that answers questions based on a specific knowledge base instead of relying only on the LLM’s general knowledge?

For this first version, I used **Head First Design Patterns, 2nd Edition** as the knowledge base. The assistant can answer questions related to design patterns explained in the book.

Tech stack used:

✅ OpenAI `gpt-4o-mini` as the chat model
✅ OpenAI `text-embedding-3-large` as the embedding model
✅ ChromaDB as the vector database
✅ LangChain for building the RAG pipeline
✅ Python for implementation

The current version works as expected. It retrieves relevant content from the knowledge base and generates answers based on that context.

This is still **RAG.1.0**, so there are improvements I want to add next, such as:

➡️ Chat history support
➡️ Better source citation
➡️ Improved evaluation of responses
➡️ Cleaner UI/UX
➡️ More robust document ingestion

What I learned from this project is that RAG is not just about connecting an LLM to documents. The real learning starts when you work with chunking, embeddings, retrieval quality, vector databases, prompts, and response generation together.

This project gave me a much better understanding of how AI applications can be grounded in custom knowledge.

Code: [https://github.com/Gurmehar/RAG.1.0](https://github.com/Gurmehar/RAG.1.0)

This is my first attempt, and I’m excited to keep improving it.

#RAG #GenerativeAI #LangChain #OpenAI #ChromaDB #Python #AIEngineering #LearningInPublic #DesignPatterns
