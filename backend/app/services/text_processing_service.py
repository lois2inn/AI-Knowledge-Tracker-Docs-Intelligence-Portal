import re

def clean_document_text(raw_text: str | None) -> str:
    if not raw_text:
        return ""

    text = raw_text.strip()

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Collapse repeated whitespace except newlines first
    text = re.sub(r"[ \t]+", " ", text)

    # Collapse too many blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Final trim
    text = text.strip()

    return text
