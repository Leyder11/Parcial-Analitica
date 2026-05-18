from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    priority: int = 2
    due: Optional[date] = None
    done: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due": self.due.isoformat() if self.due else None,
            "done": self.done,
        }

    @staticmethod
    def from_dict(payload: Dict[str, Any]) -> "Task":
        due_raw = payload.get("due")
        due_value = date.fromisoformat(due_raw) if due_raw else None
        return Task(
            id=int(payload["id"]),
            title=str(payload["title"]),
            priority=int(payload.get("priority", 2)),
            due=due_value,
            done=bool(payload.get("done", False)),
        )
