# Digital Dr Architecture

## Purpose

Digital Dr is an educational notes prototype. It provides a small Python command-line interface and a FastAPI service for local development and demonstration.

## Runtime structure

```text
CLI
  └─ digital_dr/cli.py

API
  ├─ digital_dr/run_api.py
  └─ digital_dr/api.py

Storage
  ├─ digital_dr/db.py
  └─ records.db

Tests
  ├─ tests/test_cli.py
  └─ tests/test_api.py
```

## Data flow

```text
CLI or HTTP request
  -> validation layer
  -> storage adapter
  -> SQLite database
  -> response payload
```

## Current scope

- Local prototype.
- Synthetic demonstration records.
- CLI commands for greeting, recording, and listing entries.
- REST API for health checks and record retrieval.

## Production hardening backlog

- Authentication.
- Authorization.
- Input validation.
- Audit logging.
- Backup and migration strategy.
- Deployment pipeline.
- Documentation for safe demo operation.
