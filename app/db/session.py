from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://admin:password@localhost:5432/healthauth"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)