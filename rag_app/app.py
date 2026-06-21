from __future__ import annotations

import gradio as gr

from config import settings
from rag_app.answer import answer_question


def _context_markdown(docs:list)->str:
    if not docs:
        return "No context found."
    lines =[]
    for index, doc in enumerate(docs,start=1):
       metadata=doc.metadata
       source=metadata.get("source","unknown")
       category=metadata.get("category","unknown")
       text= doc.page_content #document.page_content[:900]
       lines.append(f"[Chunk {index}]:  {source} \n\nCategory {category}:\n\n{text}")
    return "\n\n---\n\n".join(lines)

def reply(message:str,history:list,retrival_k:int,show_context:bool):
    answer, docs= answer_question(message,history=history,k=int(retrival_k))
    context =_context_markdown(docs) if show_context else "Context hidden."
    return answer,context

def build_app() -> gr.Blocks:
    with gr.Blocks(title="RAG 1.0") as demo:
        gr.Markdown("# Retrieval Augmented Generation (RAG) Demo For Java Design Patterns")
        gr.Markdown("This demo showcases a Retrieval Augmented Generation (RAG) system built using Langchain, ChromaDB, and OpenAI. \n It allows users to ask questions about Java design patterns and retrieves relevant information from a knowledge base to generate accurate answers.")
        with gr.Row():
            retrieval_k = gr.Slider(label="Number of Retrieved Chunks(k)", minimum=1, maximum=10, value=settings.RETRIEVAL_K, step=1)
            show_context =gr.Checkbox(value=True,label="Show Retrieved Context")
        chatbot =gr.ChatInterface(
            fn=reply,
            additional_inputs=[ retrieval_k, show_context],
            additional_outputs=[gr.Markdown(label="Retrieved Context")],
            title="Ask about Java Design Patterns",
        )
        del chatbot
    return demo

def main() -> None:
    build_app().launch(server_name=settings.APP_HOST, server_port=settings.RAG_APP_PORT)


if __name__ == "__main__":
    main()
            




