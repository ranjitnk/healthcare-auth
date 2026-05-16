def validate_insurance(data):

    missing = []

    insurance_id = data.get("insurance_id")
    procedure = data.get("procedure")

    # Missing Insurance
    if not insurance_id or insurance_id == "Not Found":
        missing.append("insurance_id")

    # Missing Procedure
    if not procedure or procedure == "Not Found":
        missing.append("procedure")

    # Manual Review Scenario
    if len(missing) == 1:
        return {
            "approved": False,
            "status": "MANUAL_REVIEW",
            "missing_documents": missing
        }

    # Fully Rejected Scenario
    if len(missing) >= 2:
        return {
            "approved": False,
            "status": "REJECTED",
            "missing_documents": missing
        }

    # Approved Scenario
    return {
        "approved": True,
        "status": "APPROVED",
        "missing_documents": []
    }