from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from backend.api.chat import router as chat_router
from backend.api.vision import router as vision_router
from backend.api.math import router as math_router

import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(vision_router)
app.include_router(math_router)

os.makedirs("uploads", exist_ok=True)

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    save_path = "uploads/test.pdf"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "PDF uploaded successfully"
    }