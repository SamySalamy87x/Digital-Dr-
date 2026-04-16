from digital_dr import db
from digital_dr.cli import main


def test_greet_command_output(capsys, tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "records.db")

    main(["greet"])

    output = capsys.readouterr().out
    assert "Welcome to Digital Dr. (prototype)" in output


def test_record_saves_to_db(capsys, tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "records.db")

    main(["record", "Alice", "fever,cough"])

    output = capsys.readouterr().out
    assert "Saved note for Alice" in output

    rows = db.get_notes_by_name("Alice")
    assert len(rows) == 1
    assert rows[0]["symptoms"] == "fever,cough"


def test_list_returns_records(capsys, tmp_path, monkeypatch):
    monkeypatch.setattr(db, "DB_PATH", tmp_path / "records.db")
    db.init_db()
    db.save_note("Bob", "headache")

    main(["list"])

    output = capsys.readouterr().out
    assert "Bob" in output
    assert "headache" in output
