from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .db import get_notes_by_name, init_db, list_notes, save_note

DISCLAIMER = "Not medical advice. Educational use only."

app = FastAPI(title="Digital Dr API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.middleware("http")
async def add_disclaimer_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Disclaimer"] = DISCLAIMER
    return response


class PatientNoteCreate(BaseModel):
    name: str
    symptoms: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": "0.1.0"}


@app.post("/patients")
def create_patient_note(payload: PatientNoteCreate) -> dict:
    return save_note(payload.name, payload.symptoms)


@app.get("/patients")
def get_all_patient_notes() -> list[dict]:
    return list_notes()


@app.get("/patients/{name}")
def get_patient_notes(name: str) -> list[dict]:
    return get_notes_by_name(name)
