from fastapi.testclient import TestClient

from digital_dr import db
from digital_dr.api import app


def test_health_returns_200(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "records.db")

    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "version": "0.1.0"}
    assert response.headers["x-disclaimer"] == "Not medical advice. Educational use only."


def test_post_patients_creates_record(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "records.db")

    with TestClient(app) as client:
        response = client.post("/patients", json={"name": "Carla", "symptoms": "nausea"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["name"] == "Carla"
    assert payload["symptoms"] == "nausea"
    assert payload["timestamp"]


def test_get_patients_returns_list(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "records.db")

    with TestClient(app) as client:
        client.post("/patients", json={"name": "Diego", "symptoms": "fatigue"})
        response = client.get("/patients")

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) == 1
    assert payload[0]["name"] == "Diego"
