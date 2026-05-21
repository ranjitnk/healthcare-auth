# HealthAuthAI Enterprise Framework
## Installation & Execution Guide

> Enterprise setup and execution guide for the Healthcare Agentic AI Prior Authorization Platform powered by FastAPI, LangGraph, ChromaDB, PostgreSQL, GPT-4o, and UiPath integration architecture.

---

# 1. Prerequisites

Install the following software before starting setup.

| Component | Version |
|---|---|
| Python | 3.10+ |
| Docker Desktop | Latest |
| PostgreSQL | Optional if using Docker |
| VS Code | Latest |
| Git | Latest |

Optional tools:

- pgAdmin
- UiPath Studio
- Postman
- DBeaver

---

# 2. Clone Repository

```bash
git clone https://github.com/your-repo/healthauthai-enterprise.git
cd healthauthai-enterprise
```

---

# 3. Create Python Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Additional enterprise AI packages:

```bash
pip install langgraph chromadb pypdf openai python-dotenv
```

---

# 5. Configure Environment Variables

Create a `.env` file in the project root.

```env
ENV=DEV

JWT_SECRET=changeme

DB_HOST=postgres
DB_PORT=5432
DB_NAME=healthauth
DB_USER=admin
DB_PASSWORD=password

GITHUB_TOKEN=your_github_models_token
```

---

# 6. GitHub Models GPT-4o Integration

The platform uses GitHub Models GPT-4o integration for enterprise AI reasoning.

The AI client uses:

```python
base_url="https://models.inference.ai.azure.com"
```

Configure:

```env
GITHUB_TOKEN=your_token_here
```

---

# 7. Start Docker Infrastructure

Run PostgreSQL and Redis services.

```bash
docker-compose up -d
```

Verify containers:

```bash
docker ps
```

Expected containers:

- postgres
- redis
- api

---

# 8. Initialize Database Tables

```bash
python create_tables.py
```

This creates:

- prior authorization tables
- audit logging tables
- agentic triage persistence tables

---

# 9. Start FastAPI Application

```bash
uvicorn main:app --reload
```

---

# 10. Open Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger provides:

- API testing
- request validation
- endpoint documentation
- workflow execution testing

---

# 11. Test Agentic Prior Authorization Workflow

## Endpoint

```text
POST /agentic/prior-auth
```

## Example Payload

```json
{
  "claim_text": "Patient Name: John Doe\nInsurance ID: INS9000\nProcedure: Knee Replacement\nDiagnosis: Severe Knee Osteoarthritis"
}
```

## Example Response

```json
{
  "request_id": "86f0bb7f-4dbf-4058-b820-49d14fc1df15",
  "patient_name": "John Doe",
  "recommendation": "APPROVED",
  "compliance_score": 95,
  "missing_items": [],
  "reasoning_summary": [
    "Insurance validated successfully",
    "Diagnosis documentation provided",
    "Policy requirements satisfied"
  ]
}
```

---

# 12. Dynamic Policy Ingestion

Policy files are dynamically loaded from:

```text
data/policies/
```

Supported formats:

- TXT
- PDF

Current specialties:

- orthopedic
- cardiology

Example files:

```text
orthopedic_policy.txt
cardiology_policy.txt
```

---

# 13. ChromaDB Vector Persistence

The enterprise RAG pipeline uses ChromaDB for:

- semantic retrieval
- metadata-aware filtering
- vector indexing
- specialty-based routing

If policy files change:

Delete:

```text
chroma_db/
```

Then restart the application.

---

# 14. Metadata-Aware Retrieval

The platform supports specialty-aware retrieval routing.

| Procedure | Specialty Retrieval |
|---|---|
| Knee Replacement | Orthopedic |
| Cardiac Catheterization | Cardiology |

Benefits:

- retrieval precision
- hallucination reduction
- improved clinical relevance

---

# 15. Verify Dashboard Analytics

## Endpoint

```text
GET /agentic/dashboard
```

Dashboard metrics include:

- approval counts
- compliance scores
- authorization trends
- workflow metrics

---

# 16. Verify PostgreSQL Persistence

Connect to PostgreSQL:

```bash
docker exec -it <container_name> psql -U admin -d healthauth
```

Example queries:

```sql
SELECT * FROM prior_authorizations;
SELECT * FROM audit_logs;
SELECT * FROM agentic_triage;
```

---

# 17. Available API Endpoints

| Endpoint | Description |
|---|---|
| GET /health | Health probe endpoint |
| POST /agentic/prior-auth | Executes complete Agentic AI workflow |
| GET /agentic/dashboard | Dashboard analytics |
| POST /intake/document | Upload healthcare intake document |
| POST /auth/login | Authentication endpoint |

---

# 18. Enterprise Architecture Workflow

```text
Healthcare Intake
        ↓
UiPath Automation
        ↓
FastAPI Gateway
        ↓
LangGraph Orchestration
        ↓
Entity Extraction Agent
        ↓
Metadata-Aware RAG Retrieval
        ↓
GPT Validation Agent
        ↓
Decision Agent
        ↓
PostgreSQL Persistence
        ↓
Dashboard Analytics
        ↓
Legacy System Writeback
```

---

# 19. LangGraph Multi-Agent Workflow

| Agent | Responsibility |
|---|---|
| Extraction Agent | Extracts healthcare entities |
| Policy Agent | Retrieves relevant policies |
| Validation Agent | Executes GPT-powered reasoning |
| Decision Agent | Generates authorization recommendation |

---

# 20. UiPath Integration Architecture

## Dispatcher Workflow

UiPath Dispatcher can:

- monitor healthcare inboxes
- download attachments
- capture intake requests
- create queue items

## Performer Workflow

UiPath Performer can:

- invoke FastAPI endpoints
- receive AI decisions
- update SAP/EHR systems
- send notifications
- perform retry handling

---

# 21. Docker & Kubernetes Support

Current support:

- Docker Compose
- Containerized PostgreSQL
- Redis infrastructure
- Health probe endpoints

Planned enterprise enhancements:

- AKS deployment
- Kubernetes autoscaling
- secrets management
- production ingress routing

---

# 22. HIPAA-Oriented Security Features

Implemented and planned security capabilities:

- JWT authentication
- audit logging
- PHI-aware workflow design
- request traceability
- metadata persistence
- environment variable protection
- containerized infrastructure

Planned enhancements:

- RBAC expansion
- enterprise IAM integration
- OAuth2 support
- encryption enhancements

---

# 23. Common Troubleshooting

## Chroma Retrieval Empty

Delete:

```text
chroma_db/
```

Restart the server.

## PostgreSQL Connection Refused

Verify containers are running:

```bash
docker ps
```

Verify `.env` values:

```env
DB_HOST=postgres
```

## GitHub GPT Authentication Error

Ensure:

```env
GITHUB_TOKEN=your_valid_token
```

Verify AI client configuration:

```python
base_url="https://models.inference.ai.azure.com"
```

## Module Import Errors

Run from project root:

```bash
python -m tests.test_langgraph
```

NOT:

```bash
python tests/test_langgraph.py
```

---

# 24. Planned Enterprise Enhancements

Future roadmap items include:

- OCR pipelines
- real-time graph visualization
- Epic/FHIR integration
- SMTP notification engine
- distributed observability
- Streamlit/React dashboard UI
- advanced RAG chunking
- parent-child retrieval
- Celery async workers
- enterprise deployment automation

---

# 25. Disclaimer

This repository currently represents a validated enterprise prototype architecture and healthcare AI demonstration platform.

Some described components remain architectural roadmap enhancements and may not yet represent fully production-deployed implementations.

