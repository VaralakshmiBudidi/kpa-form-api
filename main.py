from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.db_connection import engine
from app.models import Base
from app.routers import wheel_routes
from app.exceptions import validation_exception_handler

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include route file
app.include_router(wheel_routes.router)

# Add custom exception
app.add_exception_handler(RequestValidationError, validation_exception_handler)
