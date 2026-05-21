## 🏁 Getting Started
## 📦 Prerequisites

Install the following before setup:

- Python 3.10+
- Docker Desktop
- PostgreSQL (optional if using Docker)
- VS Code
- Git

Optional tools:

- pgAdmin
- UiPath Studio
- Postman
- DBeaver

---

## 📥 Clone Repository

```bash
git clone https://github.com/your-repo/healthauthai-enterprise.git

cd healthauthai-enterprise
```

---

# 3. Create Virtual Environment

## Windows

```bash
python -m venv venv

venv\Scripts\activate
source venv/bin/activate
```

---

# 4. Install Dependencies

## 📚 Install Dependencies

```bash
pip install -r requirements.txt


---

# ⚙️ Configure Environment Variables

Create a `.env` file in the project root.


## ⚙️ Configure Environment Variables

Create a `.env` file in project root:

```env
ENV=DEV

JWT_SECRET=changeme

DB_HOST=postgres
DB_PORT=5432
DB_NAME=healthauth
DB_USER=admin
DB_PASSWORD=password

OPENAI_API_KEY=


---

# 6. Start Docker Services


## 🐳 Start Infrastructure Services

Run PostgreSQL and Redis:

```bash
docker-compose up -d


---

# 7. Create Database Tables

Run:

```bash
python create_tables.py


---

# 8. Start FastAPI


## 🚀 Run FastAPI Application

```bash
uvicorn main:app --reload


---

# 9. Open Swagger


## 📄 Swagger API Documentation

Open:

http://127.0.0.1:8000/docs

## 🧪 Test Prior Authorization Flow

1. Open Swagger UI
2. Use:

POST /intake/document

3. Upload sample file:

```txt
Patient Name: Alice Johnson
Insurance ID: INS7777
Procedure: CT Scan


---

# 11. Verify Dashboard


## 📊 Dashboard Metrics API

Use:

GET /dashboard/metrics

## 🗄️ Verify Database Persistence

Connect to PostgreSQL:

```bash
docker exec -it <container_name> psql -U admin -d healthauth

```sql
SELECT * FROM prior_authorizations;

SELECT * FROM audit_logs;


---

# 13. Supported APIs

VERY enterprise-looking.


## 🔌 Available APIs

| Endpoint | Description |
|---|---|
| GET /health | Health check |
| POST /intake/document | Upload prior auth document |
| GET /dashboard/metrics | Dashboard metrics |
| GET /prior-auth/history | Prior auth history |

## 🏗️ Enterprise Workflow Architecture

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


---

# 15. HIPAA Compliance Features

VERY important for healthcare credibility.


## 🔒 HIPAA-Oriented Security Features

- JWT Authentication
- Audit Logging
- PHI-aware architecture
- Request Traceability
- Role-Based Access Control (RBAC)
- Kubernetes Secrets Management
- Secure Environment Variables

## 🤖 UiPath Integration Architecture

UiPath Dispatcher:
- Reads healthcare intake emails
- Downloads attachments
- Creates Orchestrator queue items

UiPath Performer:
- Calls FastAPI APIs
- Processes prior authorization workflows
- Handles retries and exception routing

## 🚧 Planned Enhancements

- Azure OCR
- OpenAI Structured Extraction
- LangGraph Agents
- Epic/FHIR Integration
- Celery Async Workers
- AKS Deployment
- Streamlit Dashboard