from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.get("/detections/", response_model=List[schemas.Detection])
def read_detections(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    detections = crud.get_detections(db, skip=skip, limit=limit)
    return detections

@app.post("/detections/", response_model=schemas.Detection)
def create_detection(detection: schemas.DetectionCreate, db: Session = Depends(database.get_db)):
    return crud.create_detection(db=db, detection=detection)
