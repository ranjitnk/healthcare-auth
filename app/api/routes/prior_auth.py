from fastapi import APIRouter
from app.database.repositories.prior_auth_repository import get_all_prior_auths

router = APIRouter(
    prefix="/prior-auth",
    tags=["Prior Authorization"]
)

@router.get("/history")
def get_history():

    records = get_all_prior_auths()

    result = []

    for r in records:

        result.append({
            "id": r.id,
            "patient_name": r.patient_name,
            "insurance_id": r.insurance_id,
            "procedure": r.procedure,
            "status": r.status
        })

    return result