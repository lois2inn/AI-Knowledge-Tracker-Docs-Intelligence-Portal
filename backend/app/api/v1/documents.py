from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.models.document import Document
from app.models.document_job import DocumentJob
from app.models.document_chunk import DocumentChunk
from app.models.enums import JobStage, JobStatus
from app.schemas.document import DocumentCreate, DocumentRead, DocumentCreateResponse
from app.schemas.document_chunk import DocumentChunkRead
from app.services.pipeline_service import process_document_job

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("", response_model=list[DocumentRead])
def list_documents(db: Session = Depends(get_db)) -> list[Document]:
    return db.query(Document).order_by(Document.created_at.desc()).all()

@router.post("", response_model=DocumentCreateResponse)
def create_document(
    payload: DocumentCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
):
    document = Document(
        title=payload.title,
        source_type=payload.source_type,
        raw_text=payload.raw_text,
        status=JobStatus.PENDING.value,
    )
    db.add(document)
    db.flush()

    job = DocumentJob(
        document_id=document.id,
        stage=JobStage.RECEIVED.value,
        status=JobStatus.PENDING.value,
    )
    db.add(job)

    db.commit()
    db.refresh(document)
    db.refresh(job)

    background_tasks.add_task(process_document_job, document.id, job.id)

    return {
        "document": document,
        "job": job,
    }

@router.get("/{document_id}", response_model=DocumentRead)
def get_document(document_id: int, db: Session = Depends(get_db)) -> Document:
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.get("/{document_id}/chunks", response_model=list[DocumentChunkRead])
def get_document_chunks(document_id: int, db: Session = Depends(get_db)) -> list[DocumentChunk]:
    document = db.query(Document).filter(Document.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    return (
        db.query(DocumentChunk)
        .filter(DocumentChunk.document_id == document_id)
        .order_by(DocumentChunk.chunk_index.asc())
        .all()
    )