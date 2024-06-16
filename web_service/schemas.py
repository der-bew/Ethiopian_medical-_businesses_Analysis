from pydantic import BaseModel

class DetectionBase(BaseModel):
    image: str
    xmin: float
    ymin: float
    xmax: float
    ymax: float
    confidence: float
    class_: int
    name: str

class DetectionCreate(DetectionBase):
    pass

class Detection(DetectionBase):
    id: int

    class Config:
        orm_mode = True
