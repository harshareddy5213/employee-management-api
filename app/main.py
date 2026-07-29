from fastapi import FastAPI

from .database import Base, engine
from .routers import auth, employees


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Employee Management API",
    description="RESTful API for managing employees",
    version="1.0.0"
)


app.include_router(
    auth.router
)

app.include_router(
    employees.router
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
