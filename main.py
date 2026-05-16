from fastapi import FastAPI
from app.api.routes.intake import router as intake_router
from app.api.routes.auth import router as auth_router
from app.core.middleware.audit import AuditMiddleware
from app.api.routes.prior_auth import router as prior_auth_router
from app.api.routes.dashboard import router as dashboard_router

app = FastAPI(title="HealthAuthAI Enterprise")

app.add_middleware(AuditMiddleware)

app.include_router(auth_router)
app.include_router(intake_router)
app.include_router(dashboard_router)
app.include_router(prior_auth_router)

@app.get("/health")
def health():
    return {"status": "healthy"}