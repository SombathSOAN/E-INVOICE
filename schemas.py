from pydantic import BaseModel
from typing import List, Dict, Any

class DatasetCreate(BaseModel):
    name: str

class DatasetResponse(BaseModel):
    id: int
    name: str
    data: List[Dict[str, Any]]

    class Config:
        from_attributes = True
