# AI Knowledge Tracker / Docs Intelligence Portal

A full-stack AI-powered document intelligence system that ingests, processes, and enables semantic search over documents using modern backend architecture and vector embeddings.

---

## Problem Overview

Managing and retrieving knowledge from unstructured documents is inefficient with traditional keyword search.

This project solves that by:

* Ingesting documents via API
* Cleaning and processing text asynchronously
* Generating embeddings
* Enabling semantic (meaning-based) search using vector similarity

---

## Architecture

**Backend Stack:**

* FastAPI (API layer)
* SQLAlchemy ORM (data layer)
* Alembic (database migrations)
* PostgreSQL + pgvector (vector storage)
* Background Tasks (document processing pipeline)

**Design Patterns:**

* Service Layer Pattern
* Repository Pattern
* Dependency Injection

**High-Level Flow:**

1. User submits document → `/documents`
2. Document stored with `PENDING` status
3. Background job processes document:

   * Clean text
   * Chunk content (overlap-aware)
   * Generate embeddings
4. Store embeddings in PostgreSQL (pgvector)
5. Semantic search endpoint retrieves similar content

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* Alembic
* PostgreSQL 17
* pgvector
* Docker
* NumPy

---

## Project Structure

```
ai-knowledge-tracker/
├── docker-compose.yml
├── requirements.txt
├── .env
├── alembic/
├── app/
│   ├── main.py
│   ├── models/
│   ├── services/
│   ├── repositories/
│   └── api/
```
Environment variables are managed via .env and not committed to version control.

---

## Running Locally

### 1. Clone repo

```
git clone <your-repo-url>
cd ai-knowledge-tracker
```

---

### 2. Setup environment

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3. Start PostgreSQL (Docker)

```
docker compose up -d
```

---

### 4. Enable pgvector

```
docker exec -it ai_tracker_postgres psql -U ai_user -d ai_tracker
```

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

---

### 5. Run migrations

```
alembic upgrade head
```

---

### 6. Start API

```
uvicorn app.main:app --reload
```

API available at:

```
http://127.0.0.1:8000/docs
```

---

## Example Workflow

* POST `/documents` → upload document
* Background task processes text
* Embeddings stored in vector column
* Query endpoint performs semantic similarity search

---

## Key Features

* Asynchronous document processing pipeline
* Overlap-aware text chunking
* Vector embeddings stored in PostgreSQL
* Semantic search using cosine similarity
* Clean, scalable backend architecture

---

## Future Enhancements

* LLM-powered Q&A over documents (RAG pipeline)
* Streaming responses
* Frontend dashboard (React)
* Authentication & user-specific knowledge bases
* Microservice-based ingestion pipeline

---

## Why This Project

This project demonstrates:

* Full-stack backend engineering
* Data pipeline design for AI systems
* Real-world use of vector databases
* Production-ready architecture patterns

---

## Author

GitHub: https://github.com/lois2inn
