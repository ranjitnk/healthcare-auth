from fastapi import APIRouter
from app.services.dashboard.dashboard_service import get_dashboard_metrics

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/metrics")
def get_metrics():

    return get_dashboard_metrics()