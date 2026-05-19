# PROMPTS utilizados (IA: GPT-5.2)

> Nota: Este documento registra los prompts usados para simular el flujo SDD: requisitos → IA genera código → IA valida con pruebas.

## Prompt 1 — Convertir requisitos a diseño
**IA:** GPT-5.2

"""
Lee primero `SPEC.md` y luego `README.md`.

Necesito una arquitectura mínima en Python (módulos/funciones/responsabilidades) para una CLI ToDo.

Restricciones:
- Sin dependencias externas (solo stdlib + pytest para pruebas).
- Fácil de probar con pytest.

Salida:
- Lista de archivos (ruta + propósito).
- Lista de funciones/clases clave por archivo.
"""

## Prompt 2 — Generar implementación
**IA:** GPT-5.2

"""
Lee primero `SPEC.md` y luego `README.md`.

Implementa el proyecto según `SPEC.md`.

Requisitos (mínimos):
- CLI con argparse: add/list/done/delete/export
- Persistencia JSON con creación automática
- Validaciones: título no vacío, prioridad 1..3, fecha YYYY-MM-DD
- Errores claros cuando el id no existe

Restricciones:
- Cambios mínimos y código simple.
- No inventes features fuera del SPEC.

Entrega:
- Código en `src/todo_cli/*`.
- Comando de ejecución: `python -m todo_cli`.
"""

## Prompt 3 — Generar pruebas
**IA:** GPT-5.2

"""
Genera pruebas `pytest` para validar RF-01..RF-07.

Reglas:
- Usa `tmp_path` (no tocar archivos reales).
- Llama a la CLI vía `run([...])` (como en los tests existentes).

Cubre:
- add + list (pending/done/all)
- done
- delete
- export CSV
- validaciones (título/prioridad/fecha)
- errores por id inexistente
"""

## Prompt 4 — Depuración (si falla)
**IA:** GPT-5.2

"""
Estas son las fallas de pytest (pego el output). Propón el fix mínimo en el módulo correcto sin romper otros tests.
"""

## Prompt 5 — RF-08 (edit) — implementación y pruebas (simple)
**IA:** GPT-5.2

"""
Orden de lectura:
1) Lee `SPEC.md`
2) Lee `README.md`
3) Revisa `src/todo_cli/cli.py`, `src/todo_cli/storage.py`, `src/todo_cli/utils.py`, `tests/test_todo_cli.py`

Tarea:
Implementa RF-08 (editar título): `edit <id> <nuevo_titulo>`.

Reglas:
- `nuevo_titulo` no puede ser vacío.
- Si el `id` no existe: mensaje claro (debe contener "no existe").
- No rompas comandos existentes: add/list/done/delete/export.
- Cambios mínimos.

Entrega exactamente:
1) Qué archivos vas a cambiar.
2) Parches/código para esos cambios.
3) Nuevos tests para RF-08.
"""

## Prompt 6 — Verificación (pytest) y resumen
**IA:** GPT-5.2

"""
Voy a pegar el output de `python -m pytest -q` (o el error si falla).

Si falla:
- Indica el fix mínimo y en qué archivo aplicarlo.

Si pasa:
- Resume qué cambió y cómo demuestra cumplimiento de RF-08.
"""

## Prompt 7 — (Opcional) Crear proyecto desde carpeta vacía
**IA:** GPT-5.2

"""
Tengo una carpeta vacía con solo `SPEC.md` y `README.md`.

Orden de lectura:
1) Lee `SPEC.md`
2) Lee `README.md`

Tarea:
Genera el proyecto completo en Python (estructura `src/`), implementando EXACTAMENTE el SPEC.

Reglas:
- No inventes features fuera del SPEC.
- Incluye `pytest` con tests de aceptación.

Entrega:
- Estructura de carpetas.
- Contenido de archivos principales.
- Comandos para instalar dependencias y correr tests.
"""
