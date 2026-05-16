from app.services.ocr.ocr_service import run_ocr
from app.services.llm.patient_extractor import extract_patient_data
from app.services.validation.insurance_validation import validate_insurance

def process_document(file_path: str):

    text = run_ocr(file_path)

    patient_data = extract_patient_data(text)

    validation = validate_insurance(patient_data)

    return {
        "ocr_text": text,
        "patient_data": patient_data,
        "validation": validation
    }