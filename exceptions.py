from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()

    for error in errors:
        loc = error.get("loc", [])
        err_type = error.get("type", "")
        detail = error.get("msg")

        # Targeting the "submittedDate" field
        if "submittedDate" in loc and err_type.startswith("date_"):

            # If the format is not "YYYY-MM-DD"
            if "invalid date format" in detail.lower() or "does not match format" in detail.lower():
                return JSONResponse(
                    status_code=422,
                    content={
                        "success": False,
                        "message": "Invalid date format. Expected format: YYYY-MM-DD",
                        "details": detail
                    },
                )
            else:
                # If the format is valid but the value is invalid (like day/month out of range)
                return JSONResponse(
                    status_code=422,
                    content={
                        "success": False,
                        "details": detail
                    },
                )

    # Fallback for all other validation errors
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation error",
            "details": errors,
        },
    )
