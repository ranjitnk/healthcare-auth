from fastapi import APIRouter
from app.core.security.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login():
    token = create_access_token({"user":"admin"})
    return {"token": token}