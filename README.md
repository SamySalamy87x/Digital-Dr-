# Digital Dr.

Digital Dr. is an educational healthcare prototype with a Python CLI and a FastAPI backend for recording and retrieving patient notes.

## Quick Start

### 1) Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 2) CLI usage

```bash
python -m digital_dr greet
python -m digital_dr record "Alice" "fever,cough"
python -m digital_dr list
```

### 3) API usage

Run the API server:

```bash
python -m digital_dr.run_api
```

Example requests:

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/patients -H "Content-Type: application/json" -d '{"name":"Alice","symptoms":"fever,cough"}'
curl http://127.0.0.1:8000/patients
curl http://127.0.0.1:8000/patients/Alice
```

## Architecture

```text
+--------------------+         +-----------------------+
|   CLI (argparse)   |         |  FastAPI (REST API)   |
| digital_dr/cli.py  |         |  digital_dr/api.py    |
+---------+----------+         +-----------+-----------+
          |                                |
          +--------------+-----------------+
                         |
                 +-------v--------+
                 | SQLite Storage |
                 | records.db     |
                 | digital_dr/db.py|
                 +----------------+
```

## Testing

```bash
pytest --cov=digital_dr
```

## Roadmap

| Area | MVP (v0.1) | Phase 2 (v0.2) |
|---|---|---|
| Data storage | SQLite patient notes | Migration tooling + backups |
| API security | Open endpoints for local dev/education | JWT auth + role-based access |
| Validation | Basic schema validation | Stricter validation + audit logging |
| Delivery | CLI + REST API + CI checks | Deployment automation + staging environment |

## Disclaimer

Digital Dr. is for educational use only and does not provide medical advice.
Always consult a qualified healthcare professional for medical concerns.
