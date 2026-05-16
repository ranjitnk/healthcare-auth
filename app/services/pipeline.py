import uuid
from app.services.ocr.ocr_service import run_ocr
from app.services.llm.llm_service import extract_entities
from app.services.validation.insurance_validation import validate_insurance
from app.services.dashboard.dashboard_service import update_dashboard_metrics
from app.database.repositories.prior_auth_repository import save_prior_auth
from app.database.repositories.audit_repository import create_audit_log


def process_pipeline(filename):
    request_id = str(uuid.uuid4())

    # OCR
    text = run_ocr(filename)

    # Extraction
    entities = extract_entities(text)

    # Validation
    validation = validate_insurance(entities)

    # Dashboard Metrics
    update_dashboard_metrics(validation)

    # Save Prior Auth
    save_prior_auth(entities, validation)

    # Audit Logging
    create_audit_log(
        action="PRIOR_AUTH_PROCESSED",
        patient_name=entities["patient_name"],
        status=validation["status"]
    )

    return {
        "request_id": request_id,
        "status": "processed",
        "ocr_text": text,
        "entities": entities,
        "validation": validation
    }