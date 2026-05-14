from jose import jwt
import os
from datetime import datetime, timedelta

SECRET = os.getenv("JWT_SECRET","changeme")

def create_access_token(payload: dict):
    payload["exp"] = datetime.utcnow() + timedelta(hours=1)
    return jwt.encode(payload, SECRET, algorithm="HS256")