from fastapi import APIRouter

from sqlalchemy import func

from app.database.database import SessionLocal

from app.models.agentic_triage import AgenticTriage

router = APIRouter(
    prefix="/agentic",
    tags=["Agentic Dashboard"]
)

@router.get("/dashboard")

def get_dashboard_metrics():

    db = SessionLocal()

    approved = db.query(AgenticTriage).filter(
        AgenticTriage.recommendation == "APPROVED"
    ).count()

    denied = db.query(AgenticTriage).filter(
        AgenticTriage.recommendation == "DENIED"
    ).count()

    request_info = db.query(AgenticTriage).filter(
        AgenticTriage.recommendation == "REQUEST_INFO"
    ).count()

    avg_score = db.query(
        func.avg(AgenticTriage.compliance_score)
    ).scalar()

    db.close()

    return {

        "approved": approved,

        "denied": denied,

        "request_info": request_info,

        "average_compliance_score": round(avg_score or 0, 2)
    }