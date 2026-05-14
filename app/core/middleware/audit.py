from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.getLogger("audit")

class AuditMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        logger.info(f"AUDIT {request.method} {request.url}")
        response = await call_next(request)
        return response