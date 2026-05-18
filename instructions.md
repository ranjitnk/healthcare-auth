# HealthAuthAI Enterprise - Installation & Execution Guide

---

# 📦 Prerequisites

Install the following tools before setup:

| Tool | Version |
|------|---------|
| Python | 3.10+ |
| Docker Desktop | Latest |
| Git | Latest |
| VS Code | Recommended |

Optional:
- pgAdmin
- UiPath Studio

---

# 📥 Clone Repository

```bash
git clone https://github.com/your-repo/healthauthai-enterprise.git

cd healthauthai-enterprise
```

---

# 🐍 Create Virtual Environment

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

# 📚 Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
ENV=DEV

JWT_SECRET=changeme

DB_HOST=localhost
DB_PORT=5432
DB_NAME=healthauth
DB_USER=admin
DB_PASSWORD=password

OPENAI_API_KEY=
```

---

# 🐳 Start Docker Infrastructure

Run PostgreSQL and Redis containers:

```bash
docker-compose up -d
```

Verify containers:

```bash
docker ps
```

Expected:
- postgres container running
- redis container running

---

# 🗄️ Create Database Tables

Run:

```bash
python create_tables.py
```

Expected Output:

```text
Tables created successfully
```

---

# 🚀 Run FastAPI Application

Start application server:

```bash
uvicorn main:app --reload
```

Expected:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# 📄 Swagger API Documentation

Open browser:

```text
http://127.0.0.1:8000/docs
```

---

# ❤️ Health Check API

Test:

```text
GET /health
```

Expected Response:

```json
{
  "status": "healthy"
}
```

---

# 🧪 Test Prior Authorization Flow

Use:

```text
POST /intake/document
```

Upload sample file.

Example content:

```txt
Patient Name: Alice Johnson
Insurance ID: INS7777
Procedure: CT Scan
```

Expected Response:

```json
{
  "request_id": "generated-uuid",
  "status": "processed",
  "validation": {
    "status": "APPROVED"
  }
}
```

---

# 📊 Dashboard Metrics API

Test:

```text
GET /dashboard/metrics
```

Expected Response:

```json
{
  "processed": 1,
  "approved": 1,
  "rejected": 0
}
```

---

# 📜 Prior Authorization History API

Test:

```text
GET /prior-auth/history
```

Expected Response:

```json
[
  {
    "id": 1,
    "patient_name": "Alice Johnson",
    "insurance_id": "INS7777",
    "procedure": "CT Scan",
    "status": "APPROVED"
  }
]
```

---

# 🗄️ Verify Database Records

Open PostgreSQL shell:

```bash
docker exec -it <postgres_container_name> psql -U admin -d healthauth
```

Run SQL:

```sql
SELECT * FROM prior_authorizations;

SELECT * FROM audit_logs;
```

Exit PostgreSQL:

```bash
\q
```

---

# 🧾 Audit Logging

The framework automatically stores:
- transaction history
- processing status
- audit trail entries

Audit logs are stored in:

```text
audit_logs
```

table.

---

# 🔒 Security & HIPAA Features

Implemented Features:
- JWT Authentication
- Audit Logging
- Request Traceability
- Secure Environment Variables
- Dockerized Infrastructure
- Kubernetes Secret Integration
- RBAC Architecture Ready

---

# 🤖 UiPath Integration Overview

## Dispatcher

Responsibilities:
- Read healthcare intake emails
- Download attachments
- Create Orchestrator queue items

## Performer

Responsibilities:
- Call FastAPI APIs
- Process prior authorization workflows
- Handle retries and exception routing

---

# 🏗️ Enterprise Workflow Architecture

```text
Upload File
    ↓
FastAPI API
    ↓
Pipeline Orchestration
    ↓
OCR Service
    ↓
AI Extraction
    ↓
Validation Engine
    ↓
Dashboard Metrics
    ↓
Audit Logging
    ↓
PostgreSQL Persistence
```

---

# ☸️ Kubernetes Deployment

Deployment manifests available under:

```text
infra/kubernetes/
```

Includes:
- deployment.yml
- service.yml
- secrets.yml

Supports:
- rolling deployments
- readiness probes
- liveness probes
- Kubernetes secrets

---

# 🚧 Planned Enhancements

- Azure OCR
- OpenAI Structured Extraction
- LangGraph Agents
- FHIR / Epic Integration
- Celery Async Workers
- AKS Deployment
- Streamlit Dashboard
- Human-in-the-loop workflows

---

# 🛠️ Troubleshooting

## PostgreSQL Connection Refused

Verify:
- Docker Desktop running
- PostgreSQL container running
- Port mapping exists:

```yaml
ports:
  - "5432:5432"
```

---

## Uvicorn Import Errors

Verify:
- virtual environment activated
- requirements installed
- correct command used:

```bash
uvicorn main:app --reload
```

---

## Database Table Missing

Run:

```bash
python create_tables.py
```

---

# 📌 Notes

This framework is designed as:
- enterprise healthcare automation architecture
- AI + RPA integration showcase
- HIPAA-oriented backend framework
- production-ready FastAPI reference architecture
