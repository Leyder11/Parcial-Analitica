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
