from app.database.database import engine
from app.database.models.prior_auth import Base
from app.database.models.audit_log import Base as AuditBase

Base.metadata.create_all(bind=engine)
AuditBase.metadata.create_all(bind=engine)

print("Tables created successfully")