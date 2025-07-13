from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from db_connection import engine
from models import Base
from routers import wheel_routes
from exceptions import validation_exception_handler

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include route file
app.include_router(wheel_routes.router)

# Add custom exception
app.add_exception_handler(RequestValidationError, validation_exception_handler)
