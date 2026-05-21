import json

from app.db.session import SessionLocal

from app.models.agentic_triage import AgenticTriage

def save_triage_result(result):

    db = SessionLocal()

    entities = result["extracted_entities"]

    decision = result["final_decision"]

    triage = AgenticTriage(

        patient_name=entities.get("patient_name"),

        insurance_id=entities.get("insurance_id"),

        procedure=entities.get("procedure"),

        diagnosis=entities.get("diagnosis"),

        recommendation=decision.get("status"),

        compliance_score=decision.get("compliance_score"),

        reasoning_logs=json.dumps(
            result["reasoning_logs"]
        )
    )

    db.add(triage)

    db.commit()

    db.close()