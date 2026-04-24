
def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """
    Split text into overlapping character-based chunks.

    Example:
    chunk_size=300, overlap=50

    Chunk 1: chars 0-300
    Chunk 2: chars 250-550
    Chunk 3: chars 500-800

    Overlap helps preserve context across chunk boundaries.
    """
    if not text:
        return []

    text = text.strip()
    if not text:
        return []
    
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks: list[str] = []
    start = 0

    while start < len(text):
        end = start + chunk_size  
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap

    return chunks