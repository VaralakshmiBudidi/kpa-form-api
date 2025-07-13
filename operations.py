from sqlalchemy.orm import Session
from schemas import Wheel
from models import WheelSpecifications
from sqlalchemy import func
from fastapi import HTTPException

def create_wheel(db: Session, wheel: Wheel):
    # Check if formNumber already exists
    existing = db.query(WheelSpecifications).filter_by(formNumber=wheel.formNumber).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail=f"Form number {wheel.formNumber} already exists."
        )

    # Proceed to insert if not exists
    db_item = WheelSpecifications(
        formNumber=wheel.formNumber,
        submittedBy=wheel.submittedBy,
        submittedDate=wheel.submittedDate,
        fields=wheel.fields.dict()
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_wheels(db: Session, formNumber=None, submittedBy=None, submittedDate=None):
    query = db.query(WheelSpecifications)

    if formNumber:
        query = query.filter(WheelSpecifications.formNumber == formNumber)
    if submittedBy:
        query = query.filter(func.lower(WheelSpecifications.submittedBy) == submittedBy.lower())
    if submittedDate:
        query = query.filter(WheelSpecifications.submittedDate == submittedDate)

    return query.all()

