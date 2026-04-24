from fastapi import FastAPI

from app.api.v1.documents import router as documents_router
from app.api.v1.jobs import router as jobs_router


app = FastAPI(title="AI Knowledge Tracker API")

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

app.include_router(documents_router)
app.include_router(jobs_router)