from fastapi import FastAPI

app = FastAPI(
    title="Employee Management API",
    description="REST API for managing employees",
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
