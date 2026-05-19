from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
from typing import List, Optional

from .errors import NotFoundError
from .models import Task


class JsonTaskStore:
    def __init__(self, path: Path):
        self.path = path

    def _ensure_parent(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> List[Task]:
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(data, list):
            raise ValueError("Invalid JSON database format: expected list")
        return [Task.from_dict(item) for item in data]

    def save(self, tasks: List[Task]) -> None:
        self._ensure_parent()
        payload = [t.to_dict() for t in tasks]
        self.path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    def next_id(self, tasks: List[Task]) -> int:
        return (max((t.id for t in tasks), default=0) + 1)

    def add(self, task: Task) -> Task:
        tasks = self.load()
        tasks.append(task)
        self.save(tasks)
        return task

    def list(self) -> List[Task]:
        return self.load()

    def get(self, task_id: int) -> Task:
        tasks = self.load()
        for task in tasks:
            if task.id == task_id:
                return task
        raise NotFoundError(f"No existe tarea con id={task_id}")

    def mark_done(self, task_id: int) -> Task:
        tasks = self.load()
        updated: Optional[Task] = None
        for idx, task in enumerate(tasks):
            if task.id == task_id:
                updated = replace(task, done=True)
                tasks[idx] = updated
                break
        if updated is None:
            raise NotFoundError(f"No existe tarea con id={task_id}")
        self.save(tasks)
        return updated

    def delete(self, task_id: int) -> None:
        tasks = self.load()
        new_tasks = [t for t in tasks if t.id != task_id]
        if len(new_tasks) == len(tasks):
            raise NotFoundError(f"No existe tarea con id={task_id}")
        self.save(new_tasks)

    def update_title(self, task_id: int, new_title: str) -> Task:
        tasks = self.load()
        updated: Optional[Task] = None
        for idx, task in enumerate(tasks):
            if task.id == task_id:
                updated = replace(task, title=new_title)
                tasks[idx] = updated
                break
        if updated is None:
            raise NotFoundError(f"No existe tarea con id={task_id}")
        self.save(tasks)
        return updated
