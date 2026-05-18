# SPEC — CLI de Gestión de Tareas (ToDo)

## 1) Alcance
Sistema de línea de comandos (CLI) para gestionar tareas personales, con almacenamiento local en JSON.

## 2) Requerimientos funcionales
RF-01. El sistema **debe** permitir **agregar** una tarea con:
- `title` (texto obligatorio, no vacío)
- `priority` (entero 1–3, por defecto 2)
- `due` (fecha opcional en formato `YYYY-MM-DD`)

RF-02. El sistema **debe** asignar un `id` entero incremental único a cada tarea.

RF-03. El sistema **debe** permitir **listar** tareas con filtros:
- `--all` (por defecto)
- `--pending` (solo no completadas)
- `--done` (solo completadas)

RF-04. El sistema **debe** permitir **marcar como completada** una tarea por `id`.

RF-05. El sistema **debe** permitir **eliminar** una tarea por `id`.

RF-06. El sistema **debe** permitir **exportar** todas las tareas a un archivo CSV.

RF-07. El sistema **debe** persistir los datos en un archivo JSON. Si no existe, **debe** crearlo automáticamente.

## 3) Requerimientos no funcionales
RNF-01. Debe incluir pruebas automatizadas (pytest) que validen RF-01..RF-07.

RNF-02. La CLI debe mostrar mensajes de error claros cuando:
- `id` no existe
- fecha inválida
- prioridad fuera de rango

RNF-03. El proyecto debe poder ejecutarse en Windows con PowerShell.

## 4) Criterios de aceptación (resumen)
CA-01. Ejecutar `pytest` debe pasar sin errores.

CA-02. Flujo mínimo:
1) `add` crea tarea con `id` 1
2) `list --pending` la muestra
3) `done 1` la marca completada
4) `list --done` la muestra
5) `delete 1` la elimina
6) `export out.csv` genera un CSV con encabezados
