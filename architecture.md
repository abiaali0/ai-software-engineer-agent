# Architecture

## Components

### Issue Analyzer

Extracts concise keywords and a short summary from an issue title and body.

### Context Retriever

Searches a local repository for filenames related to the issue keywords. The current public implementation is intentionally deterministic and does not send private source code to an external model.

### Implementation Planner

Creates a structured engineering plan covering acceptance criteria, affected modules, implementation, tests, and validation.

### Pull-Request Summary Generator

Formats the issue analysis and plan into a developer-facing pull-request summary.

## Future Verified Enhancements

The following should only be added after implementation and testing:

- GitHub API issue ingestion
- Semantic code retrieval
- LLM provider integration
- Docker-isolated test execution
- Automated failure analysis and repair
- React user interface
