# Parcial — SDD (Requirements → IA → Código → Pruebas)

Tema elegido: **CLI de Gestión de Tareas (ToDo)** con persistencia en JSON y exportación a CSV.

## Entregables
- [SPEC.md](SPEC.md): lista de requerimientos (lo que el sistema *debe* hacer).
- [PROMPTS.md](PROMPTS.md): prompts utilizados y la IA usada (**GPT-5.2**).
- [ANALISIS.md](ANALISIS.md): resultado + análisis (verificación de cumplimiento y qué haría para solventar fallas).
- Código en `src/` y pruebas en `tests/`.

## Cómo ejecutar
Requisitos: Python 3.10+ (recomendado 3.11+).

En Windows puede que el comando sea `py -3` en vez de `python`.

### 1) (Opcional) Crear entorno virtual
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Instalar dependencias de desarrollo (pytest)
```powershell
.
venv\Scripts\python -m pip install -r requirements-dev.txt
```

### 2.1) Instalar el paquete (para que `python -m todo_cli` funcione)
```powershell
.
venv\Scripts\python -m pip install -e .
```

### 3) Ejecutar pruebas
```powershell
.
venv\Scripts\python -m pytest -q
```

### 4) Usar la CLI
```powershell
py -3 -m todo_cli --help
py -3 -m todo_cli add "Comprar leche" --priority 2 --due 2026-05-20
py -3 -m todo_cli list --pending
py -3 -m todo_cli done 1
py -3 -m todo_cli export tasks.csv
```

## Estructura
- `src/todo_cli/`: implementación.
- `tests/`: pruebas automatizadas.
- `data/`: base de datos local por defecto (JSON). Se crea sola al usar la CLI.

## Flujo SDD (como lo describe el parcial)
1) Requerimientos en [SPEC.md](SPEC.md) (y este [README.md](README.md)).
2) IA (GPT-5.2) lee requisitos y genera código + pruebas (ver [PROMPTS.md](PROMPTS.md)).
3) La IA/ingeniería valida ejecutando `pytest` (evidencia en [ANALISIS.md](ANALISIS.md)).
4) Con CI/CD: este repo incluye un pipeline de ejemplo en GitHub Actions (ver `.github/workflows/ci.yml`) que corre `pytest` en cada push/PR.

## Troubleshooting
- Si `pip install` muestra `ERROR: Operation cancelled by user`, normalmente es porque el proceso recibió un **cancel/interrupt** (Ctrl+C / botón Stop del terminal) o el directorio está bajo control/sincronización (p. ej. OneDrive/Documentos con políticas).
	- Recomendación: clonar el repo en una ruta simple como `C:\dev\Parcial-Analitica` y reintentar.
	- Alternativa: reintentar el install y esperar a que termine: `.
venv\Scripts\python -m pip install -r requirements-dev.txt --progress-bar off`.
