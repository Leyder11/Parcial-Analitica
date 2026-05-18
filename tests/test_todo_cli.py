from __future__ import annotations

import csv
from pathlib import Path

import pytest

from todo_cli.cli import run


def test_add_and_list_pending(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    db = tmp_path / "tasks.json"

    code = run(["--db", str(db), "add", "Comprar leche", "--priority", "2", "--due", "2026-05-20"])
    assert code == 0

    code = run(["--db", str(db), "list", "--pending"])
    assert code == 0
    out = capsys.readouterr().out
    assert "Comprar leche" in out
    assert "PENDING" in out


def test_done_filter_and_delete(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    db = tmp_path / "tasks.json"

    assert run(["--db", str(db), "add", "Tarea A"]) == 0
    assert run(["--db", str(db), "add", "Tarea B"]) == 0

    assert run(["--db", str(db), "done", "1"]) == 0

    assert run(["--db", str(db), "list", "--done"]) == 0
    out = capsys.readouterr().out
    assert "Tarea A" in out
    assert "DONE" in out

    assert run(["--db", str(db), "delete", "1"]) == 0
    assert run(["--db", str(db), "list", "--done"]) == 0
    out = capsys.readouterr().out
    assert "(sin tareas)" in out


def test_export_csv(tmp_path: Path) -> None:
    db = tmp_path / "tasks.json"
    out_csv = tmp_path / "out.csv"

    assert run(["--db", str(db), "add", "Exportable"]) == 0
    assert run(["--db", str(db), "export", str(out_csv)]) == 0

    rows = list(csv.DictReader(out_csv.read_text(encoding="utf-8").splitlines()))
    assert len(rows) == 1
    assert rows[0]["title"] == "Exportable"


@pytest.mark.parametrize(
    "argv, expected",
    [
        (["add", "   "], "título"),
        (["add", "X", "--priority", "5"], "prioridad"),
        (["add", "X", "--due", "20-05-2026"], "Fecha"),
    ],
)
def test_validation_errors(tmp_path: Path, capsys: pytest.CaptureFixture[str], argv: list[str], expected: str) -> None:
    db = tmp_path / "tasks.json"
    code = run(["--db", str(db), *argv])
    assert code == 2
    err = capsys.readouterr().err
    assert "ERROR:" in err
    assert expected.lower() in err.lower()


def test_not_found_errors(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    db = tmp_path / "tasks.json"

    code = run(["--db", str(db), "done", "999"])
    assert code == 2
    err = capsys.readouterr().err
    assert "no existe" in err.lower()

    code = run(["--db", str(db), "delete", "999"])
    assert code == 2
    err = capsys.readouterr().err
    assert "no existe" in err.lower()
