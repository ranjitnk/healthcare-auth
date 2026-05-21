# HealthAuthAI Enterprise Framework (`healthcare-auth`)

> Production-Grade Healthcare Prior Authorization Platform powered by Agentic AI, Enterprise RAG, LangGraph Orchestration, and UiPath Automation Integration.

---

# Enterprise Solution Overview

HealthAuthAI Enterprise is a modern healthcare prior authorization automation platform designed to streamline payer validation workflows using:

- Agentic AI orchestration
- Retrieval-Augmented Generation (RAG)
- GPT-powered clinical reasoning
- ChromaDB semantic retrieval
- FastAPI enterprise APIs
- PostgreSQL persistence
- UiPath RPA integration architecture

The platform combines enterprise AI workflow automation with explainable healthcare authorization reasoning to modernize legacy authorization operations.

---

# Core Enterprise Capabilities

## Agentic AI Orchestration

Stateful multi-agent workflow orchestration powered by LangGraph.

Implemented AI agents include:

- Entity Extraction Agent
- Policy Retrieval Agent
- GPT Validation Agent
- Decision Agent

---

## Enterprise RAG Architecture

The platform supports:

- Dynamic TXT/PDF policy ingestion
- Multi-document semantic retrieval
- ChromaDB vector indexing
- Metadata-aware filtering
- Specialty-aware policy routing

Supported specialties currently include:

- Orthopedic workflows
- Cardiology workflows

---

## GPT-Powered Healthcare Validation

Integrated with GitHub Models GPT-4o for:

- clinical reasoning
- policy validation
- compliance scoring
- missing documentation detection
- authorization recommendations

---

## Healthcare Authorization Workflow

Supported authorization outcomes:

- APPROVED
- REQUEST_INFO
- DENIED

The system generates:

- compliance scores
- AI reasoning summaries
- audit-ready workflow logs
- request tracking identifiers

---

## PostgreSQL Persistence Layer

Workflow execution data is persisted into PostgreSQL including:

- patient references
- authorization outcomes
- compliance scores
- reasoning summaries
- audit logs
- workflow execution state

---

## Dashboard Analytics

Operational dashboard APIs provide:

- approval trend analytics
- workflow throughput metrics
- compliance score distribution
- operational visibility
- audit monitoring

---

## UiPath Enterprise Integration

The architecture supports enterprise RPA integration workflows where UiPath bots can:

- monitor intake channels
- upload authorization requests
- trigger FastAPI endpoints
- receive AI decisions
- update legacy systems
- send notifications

Target integration systems:

- SAP Healthcare ERP
- Epic EHR
- Cerner Millennium
- payer authorization portals

---

# Enterprise Architecture Workflow

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

# Technology Stack

| Layer | Technology |
|---|---|
| Backend API | FastAPI |
| AI Orchestration | LangGraph |
| LLM Engine | GitHub Models GPT-4o |
| Vector Database | ChromaDB |
| Database | PostgreSQL |
| Containerization | Docker |
| Orchestration | Kubernetes (Planned) |
| Automation | UiPath |
| Documentation | Swagger / OpenAPI |

---

# Current Implementation Status

| Capability | Status |
|---|---|
| FastAPI Backend | IMPLEMENTED |
| LangGraph Workflow | IMPLEMENTED |
| GPT Validation | VALIDATED |
| ChromaDB RAG | IMPLEMENTED |
| Multi-Policy Retrieval | IMPLEMENTED |
| Metadata Filtering | IMPLEMENTED |
| PostgreSQL Persistence | IMPLEMENTED |
| Dashboard APIs | IMPLEMENTED |
| UiPath Integration Design | ARCHITECTURALLY DESIGNED |
| Kubernetes Deployment | PLANNED ENHANCEMENT |
| Front-End Visualization | PLANNED ENHANCEMENT |

---

# Core API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/agentic/prior-auth` | Executes complete Agentic AI authorization workflow |
| GET | `/agentic/dashboard` | Retrieves operational analytics metrics |
| POST | `/intake/document` | Uploads healthcare intake documents |
| GET | `/health` | Health probe endpoint for Docker/Kubernetes |
| POST | `/auth/login` | Authentication gateway |

---

# Sample API Response

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

# Project Structure

```text
HealthAuthAI_Enterprise_v2/
│
├── app/
│   ├── api/
│   ├── langgraph/
│   │   ├── agents/
│   │   ├── rag/
│   │   ├── state/
│   │   ├── workflows/
│   │   └── utils/
│   ├── database/
│   ├── services/
│   └── core/
│
├── data/
│   └── policies/
│
├── tests/
├── chroma_db/
├── docs/
├── docker-compose.yml
└── README.md
```

---

# Getting Started

Detailed installation and execution instructions are available in:

```text
instructions.md
```

Quick Start:

```bash
# Build and start containers
Docker Compose Up --build
```

OR local execution:

```bash
# Activate virtual environment
venv\Scripts\activate

# Start FastAPI server
uvicorn main:app
```

---

# Swagger API Documentation

After startup:

```text
http://127.0.0.1:8000/docs
```

---

# Example Test Claim

```json
{
  "claim_text": "Patient Name: John Doe\nInsurance ID: INS9000\nProcedure: Knee Replacement\nDiagnosis: Severe Knee Osteoarthritis"
}
```

---

# Enterprise RAG Features

Implemented retrieval features include:

- multi-document semantic search
- metadata-aware retrieval
- specialty-based filtering
- dynamic TXT/PDF ingestion
- ChromaDB persistence
- policy indexing pipeline

---

# Planned Enterprise Enhancements

Future roadmap items include:

- Live graph execution visualization
- OCR extraction pipelines
- Kubernetes production deployment
- Enterprise IAM/OAuth2 integration
- Real-time observability
- SMTP notification services
- SAP/Epic production connectors
- Streamlit/React dashboard UI

---

# Enterprise Architecture Positioning

The platform demonstrates a modern enterprise AI architecture combining:

- Agentic AI orchestration
- Enterprise RAG engineering
- GPT-powered healthcare reasoning
- Explainable AI workflows
- Healthcare automation
- RPA integration compatibility
- Audit-ready persistence
- Metadata-aware semantic retrieval

The solution architecture aligns strongly with:

- healthcare automation modernization
- payer authorization transformation
- intelligent document processing
- AI-assisted clinical operations
- enterprise workflow orchestration initiatives

---

# Disclaimer

This repository currently represents a validated enterprise prototype architecture and technical demonstration platform for healthcare prior authorization automation workflows.

Some components described in this repository are roadmap-oriented architectural enhancements and may not yet represent fully production-deployed implementations.

---

# License

Internal Enterprise Prototype / Solution Architecture Demonstration

