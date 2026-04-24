from datetime import datetime

from pydantic import BaseModel

from app.schemas.document_job import DocumentJobRead


class DocumentCreate(BaseModel):
    title: str
    source_type: str = "note"
    raw_text: str | None = None


class DocumentRead(BaseModel):
    id: int
    title: str
    source_type: str
    raw_text: str | None
    cleaned_text: str | None
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}


class DocumentCreateResponse(BaseModel):
    document: DocumentRead
    job: DocumentJobRead