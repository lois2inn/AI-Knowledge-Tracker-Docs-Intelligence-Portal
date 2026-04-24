from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.document_job import DocumentJob
from app.schemas.document_job import DocumentJobRead

router = APIRouter(prefix="/api/v1/jobs", tags=["jobs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=list[DocumentJobRead])
def list_jobs(db: Session = Depends(get_db)) -> list[DocumentJob]:
    return db.query(DocumentJob).order_by(DocumentJob.created_at.desc()).all()


@router.get("/{job_id}", response_model=DocumentJobRead)
def get_job(job_id: int, db: Session = Depends(get_db)) -> DocumentJob:
    job = db.query(DocumentJob).filter(DocumentJob.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job 