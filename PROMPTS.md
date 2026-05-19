# PROMPTS utilizados (IA: GPT-5.2)

> Nota: Este documento registra los prompts usados para simular el flujo SDD: requisitos → IA genera código → IA valida con pruebas.

## Prompt 1 — Convertir requisitos a diseño
**IA:** GPT-5.2

"""
Tengo este SPEC para una CLI ToDo con persistencia JSON y export CSV.
Quiero una propuesta de arquitectura mínima en Python con módulos, funciones y responsabilidades.
Debe ser fácil de probar con pytest y evitar dependencias externas.
"""

## Prompt 2 — Generar implementación
**IA:** GPT-5.2

"""
Implementa el proyecto según SPEC.md:
- CLI con argparse: add/list/done/delete/export
- Persistencia en JSON con creación automática
- Validaciones: title no vacío, priority 1..3, due YYYY-MM-DD
- Errores claros por id inexistente
Entrega código en src/todo_cli y un entrypoint python -m todo_cli
"""

## Prompt 3 — Generar pruebas
**IA:** GPT-5.2

"""
Genera pruebas pytest para validar RF-01..RF-07.
Usa tmp_path para evitar tocar archivos reales.
Cubre add/list filtros/done/delete/export.
"""

## Prompt 4 — Depuración (si falla)
**IA:** GPT-5.2

"""
Estas son las fallas de pytest (pego el output). Propón el fix mínimo en el módulo correcto sin romper otros tests.
"""

## Prompt 5 — Nuevo requerimiento (RF-08: edit)
**IA:** GPT-5.2

"""
Contexto: ya existe una CLI ToDo en Python con `argparse` y storage JSON.

Necesito implementar el requerimiento RF-08 en SPEC.md:
- Comando: edit <id> <nuevo_titulo>
- Validación: nuevo_titulo no puede ser vacío
- Error: si el id no existe, mostrar error claro

Restricciones:
- Cambios mínimos.
- Mantener compatibilidad con comandos existentes: add/list/done/delete/export.
- Actualizar solo los archivos necesarios.

Entrega:
1) Cambios propuestos por archivo (cli.py, storage.py, tests).
2) Código completo de las funciones/bloques modificados.
"""

## Prompt 6 — Pruebas para RF-08
**IA:** GPT-5.2

"""
Genera pruebas pytest para RF-08 (edit):
- Caso feliz: add -> edit 1 "Nuevo título" -> list --all muestra el título nuevo.
- Caso error: edit con id inexistente retorna exit code 2 y mensaje contiene "no existe".

Usa tmp_path y llama a `run([...])` igual que en tests existentes.
"""

## Prompt 7 — Verificación y reporte
**IA:** GPT-5.2

"""
Te pego el output de `pytest -q` (y/o el error si falla).

1) Si falla: indica el fix mínimo y en qué archivo aplicarlo.
2) Si pasa: resume qué cambió y cómo demuestra cumplimiento de RF-08.
"""
