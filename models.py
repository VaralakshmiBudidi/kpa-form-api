from sqlalchemy import Column, Integer, String, Date, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WheelSpecifications(Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True)
    submittedBy = Column(String)
    submittedDate = Column(Date)
    fields = Column(JSON)