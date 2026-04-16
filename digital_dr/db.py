from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).resolve().parent / "data" / "records.db"


def _connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db() -> None:
    with _connect() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS patient_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                symptoms TEXT NOT NULL,
                timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def save_note(name: str, symptoms: str) -> dict[str, Any]:
    with _connect() as conn:
        cursor = conn.execute(
            "INSERT INTO patient_notes (name, symptoms) VALUES (?, ?)",
            (name, symptoms),
        )
        note_id = cursor.lastrowid
        row = conn.execute(
            "SELECT id, name, symptoms, timestamp FROM patient_notes WHERE id = ?",
            (note_id,),
        ).fetchone()
    return dict(row) if row else {}


def list_notes() -> list[dict[str, Any]]:
    with _connect() as conn:
        rows = conn.execute(
            "SELECT id, name, symptoms, timestamp FROM patient_notes ORDER BY id ASC"
        ).fetchall()
    return [dict(row) for row in rows]


def get_notes_by_name(name: str) -> list[dict[str, Any]]:
    with _connect() as conn:
        rows = conn.execute(
            """
            SELECT id, name, symptoms, timestamp
            FROM patient_notes
            WHERE name = ?
            ORDER BY id ASC
            """,
            (name,),
        ).fetchall()
    return [dict(row) for row in rows]
