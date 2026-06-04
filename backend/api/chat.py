from backend.search.vector_store import create_index, search
from backend.router.model_router import get_model

from fastapi import APIRouter
from pydantic import BaseModel

import ollama

from backend.pdf.pdf_service import extract_text

router = APIRouter()

pdf_loaded = False


class ChatRequest(BaseModel):

    message: str
    mode: str = "fast"
    use_pdf: bool = False


@router.post("/chat")
def chat(req: ChatRequest):

    global pdf_loaded

    context = ""

    if req.use_pdf:

        try:

            if not pdf_loaded:

                print("Loading PDF...")

                pdf_text = extract_text(
                    "uploads/test.pdf"
                )

                print("PDF extracted")

                create_index(pdf_text)

                pdf_loaded = True

                print("PDF indexed")

            context = search(
                req.message
            )

            print("Search completed")

        except Exception as e:

            print(
                "PDF ERROR:",
                e
            )

    prompt = f"""
You are an AI Study Assistant.

Context:

{context}

Question:

{req.message}
"""

    selected_model = get_model(
        req.mode
    )

    print(
        "Using model:",
        selected_model
    )

    response = ollama.chat(
        model=selected_model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return {
        "answer":
        response["message"]["content"]
    }