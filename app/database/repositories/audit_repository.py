from app.database.database import SessionLocal
from app.database.models.audit_log import AuditLog

def create_audit_log(action, patient_name, status):

    db = SessionLocal()

    try:

        log = AuditLog(
            action=action,
            patient_name=patient_name,
            status=status
        )

        db.add(log)
        db.commit()

    finally:
        db.close()