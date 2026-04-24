from datetime import datetime

from pydantic import BaseModel


class DocumentChunkRead(BaseModel):
    id: int
    document_id: int
    chunk_index: int
    content: str
    char_count: int
    created_at: datetime

    model_config = {"from_attributes": True}