from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class PriorAuthorization(Base):

    __tablename__ = "prior_authorizations"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    insurance_id = Column(String)
    procedure = Column(String)
    
    status = Column(String)