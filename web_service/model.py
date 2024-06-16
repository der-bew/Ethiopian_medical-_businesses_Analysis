from sqlalchemy import Column, Integer, Float, String
from .database import Base

class Detection(Base):
    __tablename__ = "detections"
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String, index=True)
    xmin = Column(Float)
    ymin = Column(Float)
    xmax = Column(Float)
    ymax = Column(Float)
    confidence = Column(Float)
    class_ = Column(Integer)
    name = Column(String)

