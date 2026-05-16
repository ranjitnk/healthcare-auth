from fastapi import APIRouter, UploadFile, File
from app.services.pipeline import process_pipeline
import shutil
import os

router = APIRouter(prefix="/intake", tags=["Intake"])

@router.post("/document")
async def intake_document(file: UploadFile = File(...)):

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:

        result = process_pipeline(temp_path)

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)

    return result