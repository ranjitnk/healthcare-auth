from app.services.ocr.ocr_engine import extract_text
from app.services.llm.patient_extractor import extract_patient_data
from app.services.validation.insurance_validation import validate_insurance

def process_document(filename: str):

    text = extract_text(filename)

    patient_data = extract_patient_data(text)

    validation = validate_insurance(patient_data)

    return {
        "patient": patient_data,
        "validation": validation
    }