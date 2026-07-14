# AI Software Engineer Agent

A public portfolio reconstruction of an AI-assisted developer tool for analyzing GitHub issues, retrieving relevant repository context, generating structured implementation plans, running automated checks, and preparing developer-facing summaries.

> **Original project year:** 2026  
> **Public repository reconstruction:** July 2026  
> **Status:** Active portfolio reconstruction using verified, original work only

## Current Public Implementation

This repository currently includes:

- A FastAPI backend
- Structured GitHub issue analysis
- Local repository file discovery
- Keyword-based context retrieval
- Implementation-plan generation
- Pull-request summary generation
- Pytest coverage
- Docker support
- GitHub Actions continuous integration

The résumé-listed project also references LangChain, OpenAI API, GitHub API, React, Docker-based test execution, and automated error-repair loops. Those integrations should only be added publicly when the original implementation is recovered or they are rebuilt and verified.

## Architecture

```text
GitHub issue text
      ↓
Issue analyzer
      ↓
Repository context retriever
      ↓
Implementation planner
      ↓
Developer-facing summary
```

## API Endpoints

### Health check

```http
GET /health
```

### Analyze an issue

```http
POST /analyze
Content-Type: application/json
```

Example request:

```json
{
  "title": "Add CSV export",
  "body": "Users need to export filtered reports as CSV.",
  "repository_path": "."
}
```

Example response:

```json
{
  "issue": {
    "title": "Add CSV export",
    "keywords": ["add", "csv", "export", "filtered", "reports"]
  },
  "context_files": [],
  "implementation_plan": [],
  "pull_request_summary": ""
}
```

## Run Locally

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the API

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Run Tests

```bash
pytest
```

## Run with Docker

```bash
docker build -t ai-software-engineer-agent .
docker run -p 8000:8000 ai-software-engineer-agent
```

## Development Timeline

- **2026:** Original project work
- **July 2026:** Public portfolio reconstruction and documentation

Exact original months are not stated on the résumé, so this repository does not claim a more specific timeline.

## Accuracy Note

This repository distinguishes between:

1. Features implemented in the current public reconstruction
2. Features listed on the résumé but not yet publicly verified

No employer code, private client material, credentials, or proprietary data should be committed.
