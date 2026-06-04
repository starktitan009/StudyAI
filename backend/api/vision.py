from fastapi import APIRouter, UploadFile, File, Form
import shutil

from backend.vision.vision_service import analyze_image

router = APIRouter()

@router.post("/vision")
async def vision_chat(
    file: UploadFile = File(...),
    question: str = Form(...)
):

    save_path = "uploads/image.png"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    answer = analyze_image(
        save_path,
        question
    )

    return {
        "answer": answer
    }