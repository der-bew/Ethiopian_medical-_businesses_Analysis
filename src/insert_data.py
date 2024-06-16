from sqlalchemy import create_engine, Column, Integer, Float, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

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

Base.metadata.create_all(bind=engine)

def insert_detection_data(df):
    session = SessionLocal()
    for _, row in df.iterrows():
        detection = Detection(
            image=row['image'],
            xmin=row['xmin'],
            ymin=row['ymin'],
            xmax=row['xmax'],
            ymax=row['ymax'],
            confidence=row['confidence'],
            class_=row['class'],
            name=row['name']
        )
        session.add(detection)
    session.commit()
    session.close()

# Read data from CSV and insert into database
df = pd.read_csv('detection_results.csv')
insert_detection_data(df)
