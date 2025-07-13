from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from datetime import date
from app.schemas import Wheel
from app.db_connection import get_db
from app.operations import create_wheel, get_wheels

router = APIRouter(prefix="/api/forms/wheel-specifications", tags=["Wheel Specs"])

@router.post("", status_code=status.HTTP_201_CREATED)
def create_wheel_form(form: Wheel, db: Session = Depends(get_db)):
    create_wheel(db, form)
    return {
        "success": True,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": form.formNumber,
            "submittedBy": form.submittedBy,
            "submittedDate": str(form.submittedDate),
            "status": "Saved"
        }
    }

@router.get("", status_code=status.HTTP_200_OK)
def filter_wheel_forms(
    formNumber: str = None,
    submittedBy: str = None,
    submittedDate: date = None,
    db: Session = Depends(get_db)
):
    result = get_wheels(db, formNumber, submittedBy, submittedDate)

    if not result:
        return {
            "success": True,
            "message": "No records found"
        }

    item = result[0]
    formatted_data = {
        "formNumber": item.formNumber,
        "submittedBy": item.submittedBy,
        "submittedDate": str(item.submittedDate),
        "fields": {
            "treadDiameterNew": item.fields.get("treadDiameterNew"),
            "lastShopIssueSize": item.fields.get("lastShopIssueSize"),
            "condemningDia": item.fields.get("condemningDia"),
            "wheelGauge": item.fields.get("wheelGauge")
        }
    }

    return {
        "success": True,
        "message": "Wheel specification form fetched successfully.",
        "data": formatted_data
    }
