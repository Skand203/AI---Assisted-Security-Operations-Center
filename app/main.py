
from fastapi import FastAPI

app = FastAPI(
    title="AI-Assisted SOC API",
    description="Backend API for a security operations center project.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
