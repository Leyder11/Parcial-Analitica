from __future__ import annotations

from datetime import date
from typing import Optional

from .errors import ValidationError


def validate_title(title: str) -> str:
    cleaned = (title or "").strip()
    if not cleaned:
        raise ValidationError("El título no puede estar vacío")
    return cleaned


def validate_priority(priority: int) -> int:
    if priority < 1 or priority > 3:
        raise ValidationError("La prioridad debe estar entre 1 y 3")
    return priority


def parse_due_date(due: Optional[str]) -> Optional[date]:
    if due is None:
        return None
    raw = due.strip()
    if not raw:
        return None
    try:
        return date.fromisoformat(raw)
    except ValueError as exc:
        raise ValidationError("Fecha inválida. Use YYYY-MM-DD") from exc
