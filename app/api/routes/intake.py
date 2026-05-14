from fastapi import APIRouter, UploadFile
from app.services.intake.document_processor import process_document

router = APIRouter(prefix="/intake", tags=["Intake"])

@router.post("/document")
async def upload_document(file: UploadFile):
    result = process_document(file.filename)

    return {
        "status": "processed",
        "data": result
    }