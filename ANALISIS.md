# Resultado y análisis

## 1) Resultado realizado
Se implementó una CLI de gestión de tareas en Python con persistencia local (JSON), comandos CRUD básicos y exportación a CSV. Se incluyeron pruebas automatizadas (pytest) para validar el cumplimiento del SPEC.

## 2) Evidencia de verificación
Criterio CA-01: ejecutar `pytest` debe pasar.
- Evidencia: ejecutar `pytest -q` en el proyecto.
- Resultado observado (Windows, venv): `7 passed in 0.15s`.

Validación CI (opcional, alineado a CI/CD):
- GitHub Actions ejecutó el workflow `CI` en push/PR y terminó en **Success** (matriz Python 3.10/3.11/3.12).

Criterio CA-02: flujo mínimo add → list → done → list → delete → export.
- Evidencia: pruebas automatizadas + ejecución manual opcional.

## 3) Validación de cumplimiento vs requerimientos
- RF-01: `add` valida título, prioridad y fecha.
- RF-02: `id` incremental.
- RF-03: `list` soporta filtros `--all/--pending/--done`.
- RF-04: `done <id>`.
- RF-05: `delete <id>`.
- RF-06: `export <archivo.csv>`.
- RF-07: JSON se crea automáticamente.

## 4) ¿Qué haría si no cumple o falla?
En un marco SDD real, si el resultado no es satisfactorio, el rol de ingeniería sería:
1) **Reproducir**: convertir el fallo en un caso reproducible (idealmente un test nuevo).
2) **Aislar la causa raíz**: ubicar el módulo responsable (p. ej. parseo de fechas o storage).
3) **Corregir con el cambio mínimo**: evitar cambios amplios; mantener compatibilidad.
4) **Agregar cobertura**: si el bug no estaba cubierto, añadir test de regresión.
5) **Re-ejecutar pipeline**: `pytest` local y (si existe) CI.

Ejemplos de fallas típicas y mitigación:
- Fecha inválida aceptada: endurecer `parse_due_date` + test de fechas.
- IDs duplicados al borrar: recalcular `next_id` como `max(id)+1`.
- Corrupción JSON: manejo de errores y mensaje que sugiera borrar/recuperar archivo.

## 5) Limitaciones
- No hay CI/CD real configurado (se describe conceptualmente). Se ejecuta localmente.
- Persistencia es local (JSON), no multiusuario.
