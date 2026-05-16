from app.database.database import SessionLocal
from app.database.models.prior_auth import PriorAuthorization

def save_prior_auth(data, validation):

    db = SessionLocal()

    try:

        auth = PriorAuthorization(
            patient_name=data.get("patient_name"),
            insurance_id=data.get("insurance_id"),
            procedure=data.get("procedure"),
            status=validation["status"]
        )

        db.add(auth)
        db.commit()

    finally:
        db.close()

def get_all_prior_auths():

    db = SessionLocal()

    try:

        return db.query(PriorAuthorization).all()

    finally:
        db.close()