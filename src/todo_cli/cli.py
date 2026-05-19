from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from typing import Iterable, List, Optional

from .errors import TodoCliError
from .models import Task
from .storage import JsonTaskStore
from .utils import parse_due_date, validate_priority, validate_title


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo", description="CLI de gestión de tareas")
    parser.add_argument(
        "--db",
        default=str(Path("data") / "tasks.json"),
        help="Ruta al archivo JSON (default: data/tasks.json)",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    add_p = sub.add_parser("add", help="Agregar tarea")
    add_p.add_argument("title")
    add_p.add_argument("--priority", type=int, default=2, help="1..3 (default: 2)")
    add_p.add_argument("--due", type=str, default=None, help="YYYY-MM-DD")

    list_p = sub.add_parser("list", help="Listar tareas")
    group = list_p.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="Todas (default)")
    group.add_argument("--pending", action="store_true", help="Solo pendientes")
    group.add_argument("--done", action="store_true", help="Solo completadas")

    done_p = sub.add_parser("done", help="Marcar como completada")
    done_p.add_argument("id", type=int)

    edit_p = sub.add_parser("edit", help="Editar título")
    edit_p.add_argument("id", type=int)
    edit_p.add_argument("title", nargs="+", help="Nuevo título")

    del_p = sub.add_parser("delete", help="Eliminar tarea")
    del_p.add_argument("id", type=int)

    exp_p = sub.add_parser("export", help="Exportar a CSV")
    exp_p.add_argument("csv_path", type=str)

    return parser


def _format_task(task: Task) -> str:
    due = task.due.isoformat() if task.due else "-"
    status = "DONE" if task.done else "PENDING"
    return f"{task.id:>4} | p{task.priority} | {status:<7} | {due} | {task.title}"


def list_filtered(tasks: Iterable[Task], *, pending: bool, done: bool) -> List[Task]:
    if pending:
        return [t for t in tasks if not t.done]
    if done:
        return [t for t in tasks if t.done]
    return list(tasks)


def run(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    store = JsonTaskStore(Path(args.db))

    try:
        if args.command == "add":
            title = validate_title(args.title)
            priority = validate_priority(args.priority)
            due = parse_due_date(args.due)
            tasks = store.list()
            task = Task(id=store.next_id(tasks), title=title, priority=priority, due=due)
            store.add(task)
            print(f"OK: creada tarea id={task.id}")
            return 0

        if args.command == "list":
            tasks = store.list()
            pending = bool(args.pending)
            done = bool(args.done)
            items = list_filtered(tasks, pending=pending, done=done)
            items.sort(key=lambda t: (t.done, t.priority, t.id))
            if not items:
                print("(sin tareas)")
                return 0
            print(" id  | pr | status  | due        | title")
            print("-----+----+---------+------------+----------------")
            for task in items:
                print(_format_task(task))
            return 0

        if args.command == "done":
            updated = store.mark_done(args.id)
            print(f"OK: tarea id={updated.id} completada")
            return 0

        if args.command == "edit":
            new_title = validate_title(" ".join(args.title))
            updated = store.update_title(args.id, new_title)
            print(f"OK: tarea id={updated.id} actualizada")
            return 0

        if args.command == "delete":
            store.delete(args.id)
            print(f"OK: tarea id={args.id} eliminada")
            return 0

        if args.command == "export":
            tasks = store.list()
            out_path = Path(args.csv_path)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with out_path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=["id", "title", "priority", "due", "done"])
                writer.writeheader()
                for t in tasks:
                    writer.writerow(t.to_dict())
            print(f"OK: exportado a {out_path}")
            return 0

        parser.error("Comando inválido")
        return 2

    except TodoCliError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


def main() -> None:
    raise SystemExit(run())
