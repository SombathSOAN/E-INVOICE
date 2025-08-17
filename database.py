from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL database URL for Railway deployment
# DATABASE_URL = "postgresql://postgres:hCukXsTnUaLQmoVVsICaDhRSBWyXfVIZ@postgres-glu6.railway.internal:5432/railway"

# For local development, use SQLite (Railway internal hostnames don't work locally)
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
