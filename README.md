# AI-Assisted Security Operations Center (SOC)

**Event Ingestion, Rule-Based Threat Correlation, and AI-Augmented Triage Backend**

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20Framework-009688?style=flat-square&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Data%20Store-4169E1?style=flat-square&logo=postgresql)
![Status](https://img.shields.io/badge/Status-Foundational%20Development-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## Overview

Modern Security Operations Centers (SOCs) are inundated with high-volume telemetry across firewalls, host endpoints, authentication services, and network devices. Junior security analysts face overwhelming alert fatigue, manual alert correlation overhead, and repetitive contextual research.

This project implements an open-source, backend-focused **AI-Assisted SOC Platform** designed to:
1. Ingest structured security telemetry via high-throughput REST APIs.
2. Evaluate event streams against deterministic detection rules (Sigma/YARA-style matching).
3. Correlate related indicators into cohesive security alerts stored in PostgreSQL.
4. Augment analyst triage by generating automated threat summaries, MITRE ATT&CK mapping, and preliminary remediation playbooks using LLM reasoning.

> **Project Development Status:** Foundational Backend Phase. The core FastAPI service architecture, initial schema models, and endpoint routing are established. Event correlation pipelines and database migrations are under active implementation.

---

## Planned System Architecture

```text
 ┌─────────────────────────────────────────────────────────┐
 │ Telemetry Sources (Endpoint Beats, Syslog, Auth Events)  │
 └────────────────────────────┬────────────────────────────┘
                              │ HTTP POST (Structured JSON)
                              ▼
 ┌─────────────────────────────────────────────────────────┐
 │ FastAPI Ingestion Service (app/api/v1/telemetry)        │
 │  - Pydantic schema validation & timestamp normalization  │
 │  - API key authentication & rate limiting               │
 └────────────────────────────┬────────────────────────────┘
                              │
                              ▼
 ┌─────────────────────────────────────────────────────────┐
 │ Correlation & Detection Engine                          │
 │  - Deterministic Rule Engine (Pattern & Threshold)      │
 │  - Statistical Anomaly Filter                           │
 │  - Event deduplication & session aggregation            │
 └────────────────────────────┬────────────────────────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
 ┌───────────────────────────┐ ┌───────────────────────────┐
 │ Relational Storage (PgSQL)│ │ AI Triage Engine          │
 │ - Events & Audit Records  │ │ - MITRE ATT&CK Mapping    │
 │ - Alerts & Incident State │ │ - Threat Actor Context    │
 │ - Analyst Investigation   │ │ - Triage Recommendations  │
 └───────────────────────────┘ └───────────────────────────┘
```

---

## Key Modules & Capabilities

- **High-Throughput Telemetry Ingestion:** FastAPI endpoints utilizing asynchronous request handling and Pydantic validation to normalize heterogeneous event payloads (host, user, process, network, timestamp).
- **Rule-Based Threat Correlation:** Rule evaluation engine matching security events against defined IOC patterns (e.g., suspicious PowerShell invocations, brute force login sequences, unauthorized privilege escalation).
- **Relational Alert Data Store:** PostgreSQL schema designed to link raw event telemetry with escalated security incidents and investigation notes.
- **AI-Assisted Analyst Triage:** Integration with language models to produce synthesized incident briefs, reducing Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR).

---

## Database Schema (Planned Relational Model)

```text
 ┌─────────────────────────┐         ┌─────────────────────────┐
 │      SecurityEvent      │         │      SecurityAlert      │
 ├─────────────────────────┤         ├─────────────────────────┤
 │ id: UUID (PK)           │         │ id: UUID (PK)           │
 │ timestamp: TIMESTAMPTZ  │         │ created_at: TIMESTAMPTZ │
 │ host_id: VARCHAR(64)    │ 1     * │ severity: VARCHAR(16)   │
 │ event_type: VARCHAR(32) │────────►│ title: VARCHAR(128)     │
 │ source_ip: INET         │         │ status: VARCHAR(16)     │
 │ user_id: VARCHAR(64)    │         │ mitre_tactic: VARCHAR   │
 │ raw_payload: JSONB      │         │ summary: TEXT           │
 └─────────────────────────┘         └────────────┬────────────┘
                                                  │ 1
                                                  │ *
                                     ┌────────────▼────────────┐
                                     │     InvestigationNote   │
                                     ├─────────────────────────┤
                                     │ id: UUID (PK)           │
                                     │ alert_id: UUID (FK)     │
                                     │ analyst_id: VARCHAR(64) │
                                     │ note: TEXT              │
                                     │ created_at: TIMESTAMPTZ │
                                     └─────────────────────────┘
```

---

## Repository Structure

```text
AI---Assisted-Security-Operations-Center/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── health.py        # System health and liveness checks
│   │       │   ├── telemetry.py     # Log and telemetry ingestion endpoints
│   │       │   └── alerts.py        # Alert query and lifecycle endpoints
│   │       └── router.py            # API version router
│   ├── core/
│   │   ├── config.py                # Environment configuration & secrets
│   │   └── database.py              # Async SQLAlchemy engine & session maker
│   ├── models/
│   │   ├── event.py                 # Telemetry database models
│   │   └── alert.py                 # Incident and alert database models
│   ├── schemas/
│   │   ├── telemetry.py             # Ingestion validation schemas
│   │   └── alert.py                 # Alert serialization schemas
│   ├── services/
│   │   ├── detection.py             # Rule matching logic
│   │   └── ai_triage.py             # LLM incident synthesis client
│   └── main.py                      # FastAPI application entrypoint
├── tests/
│   ├── test_health.py               # Health-check endpoint tests
│   └── test_telemetry.py            # Ingestion pipeline unit tests
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Local Development Setup

### Prerequisites
- Python 3.11 or higher
- PostgreSQL (local instance or Docker container)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/Skand203/AI---Assisted-Security-Operations-Center.git
cd AI---Assisted-Security-Operations-Center
```

### 2. Switch to the Active Development Branch
```bash
git checkout feature/project-foundation
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
# On Linux/macOS
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Launch the FastAPI Development Server
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Access the interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Development Milestones

- [x] **Milestone 1:** Baseline FastAPI repository setup, environment config, health checks.
- [ ] **Milestone 2:** PostgreSQL integration with SQLAlchemy async engine and Alembic migrations.
- [ ] **Milestone 3:** Structured telemetry ingestion endpoints (`/api/v1/telemetry`) with Pydantic validation.
- [ ] **Milestone 4:** Deterministic rule engine for threshold-based and string-match threat triggers.
- [ ] **Milestone 5:** LLM incident context generator providing triage assistance and MITRE ATT&CK mapping.

---

## License

This project is licensed under the [MIT License](LICENSE).
