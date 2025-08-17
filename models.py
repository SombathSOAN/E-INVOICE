from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Dataset(Base):
    __tablename__ = "datasets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    data = Column(JSON)   # store rows as JSON for flexibility
