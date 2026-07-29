from fastapi import FastAPI

from .database import Base, engine
from .models import Employee


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    description="RESTful API for managing employees",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Employee Management API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
