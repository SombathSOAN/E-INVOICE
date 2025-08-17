import pandas as pd
from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import shutil, os

from database import Base, engine, SessionLocal
from models import Dataset
from schemas import DatasetResponse

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# create db
Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 1. Upload Excel/CSV
@app.post("/upload", response_model=DatasetResponse)
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Save temporarily
    filepath = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read with pandas
    if file.filename.endswith(".csv"):
        df = pd.read_csv(filepath)
    else:
        df = pd.read_excel(filepath)

    # Store in DB as JSON
    dataset = Dataset(name=file.filename, data=df.to_dict(orient="records"))
    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return dataset


# 2. List all datasets
@app.get("/datasets", response_model=list[DatasetResponse])
def list_datasets(db: Session = Depends(get_db)):
    return db.query(Dataset).all()


# 3. Get single dataset
@app.get("/datasets/{dataset_id}", response_model=DatasetResponse)
def get_dataset(dataset_id: int, db: Session = Depends(get_db)):
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset


# 4. Update dataset row(s)
@app.put("/datasets/{dataset_id}", response_model=DatasetResponse)
def update_dataset(dataset_id: int, new_data: list[dict], db: Session = Depends(get_db)):
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")

    dataset.data = new_data
    db.commit()
    db.refresh(dataset)
    return dataset
