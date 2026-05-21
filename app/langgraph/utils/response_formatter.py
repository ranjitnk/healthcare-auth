import uuid

def build_triage_report(result):

    validation = result["validation_result"]

    decision = result["final_decision"]

    entities = result["extracted_entities"]

    reasoning_summary = []

    if entities.get("insurance_id") != "Not Found":
        reasoning_summary.append(
            "Insurance validated successfully"
        )

    if entities.get("diagnosis") != "Not Found":
        reasoning_summary.append(
            "Diagnosis documentation provided"
        )

    if decision["status"] == "APPROVED":
        reasoning_summary.append(
            "Policy requirements satisfied"
        )

    report = {

        "request_id": str(uuid.uuid4()),

        "patient_name": entities.get("patient_name"),

        "recommendation": decision["status"],

        "compliance_score": decision["compliance_score"],

        "missing_items": validation["missing_items"],

        "reasoning_summary": reasoning_summary
    }

    return report