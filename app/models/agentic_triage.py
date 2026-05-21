from sqlalchemy import Column, Integer, String, Text

from app.database.models.prior_auth import Base

class AgenticTriage(Base):

    __tablename__ = "agentic_triage"

    id = Column(Integer, primary_key=True)

    patient_name = Column(String)

    insurance_id = Column(String)

    procedure = Column(String)

    diagnosis = Column(String)

    recommendation = Column(String)

    compliance_score = Column(Integer)

    reasoning_logs = Column(Text)