# Cómo probar el proyecto (y qué creó la IA)

## 0) Idea clave (para no enredarse)
- **La IA no crea un “programa aparte”**: la IA ayudó a generar/editar **el código del proyecto** (los archivos `.py` y los tests).
- **`.venv/` NO es el proyecto**: es un **entorno virtual de Python** (una copia aislada de Python + pip + pytest) para que todo funcione sin ensuciar tu Windows.

En este repo:
- **Lo que es “el programa” (código)** está en `src/todo_cli/`.
- **Las pruebas** están en `tests/`.
- **La evidencia de prompts** está en `PROMPTS.md`.


## 1) ¿Quién creó `.venv`?
`.venv` se crea cuando ejecutas algo como:
- `python -m venv .venv`  (o `py -m venv .venv` en Windows)

Eso lo creaste tú (o nosotros cuando configuramos el proyecto). Por eso ves archivos como:
- `.venv\Scripts\python.exe`
- `.venv\Scripts\pip.exe`
- `.venv\Scripts\pytest.exe`

**Normalmente `.venv` no se sube a GitHub** (se ignora con `.gitignore`).


## 2) ¿Qué creó la IA exactamente?
La IA ayudó a crear/editar:
- `src/todo_cli/cli.py` (la CLI: comandos add/list/done/delete/export/edit)
- `src/todo_cli/storage.py` (persistencia JSON)
- `tests/test_todo_cli.py` (pruebas automáticas)

Y también documentos de evidencia:
- `SPEC.md` (requerimientos)
- `PROMPTS.md` (prompts usados)
- `ANALISIS.md` (resultado + evidencia)


## 3) Cómo ejecutar el programa (manual)
### Opción A (recomendada): ejecutar sin “activar” nada
Desde la carpeta del proyecto (donde está `SPEC.md`), usa:

```powershell
.\.venv\Scripts\python.exe -m todo_cli --help
```

Ejemplo completo (sin ensuciar tu BD real):

```powershell
# 1) Crear una BD demo
.\.venv\Scripts\python.exe -m todo_cli --db .\data\demo.json add "Comprar pan" --priority 2 --due 2026-05-20

# 2) Ver el “panel/tabla” en consola
.\.venv\Scripts\python.exe -m todo_cli --db .\data\demo.json list --all

# 3) Editar (RF-08)
.\.venv\Scripts\python.exe -m todo_cli --db .\data\demo.json edit 1 "Pan y leche"

# 4) Marcar como completada
.\.venv\Scripts\python.exe -m todo_cli --db .\data\demo.json done 1

# 5) Exportar CSV
.\.venv\Scripts\python.exe -m todo_cli --db .\data\demo.json export .\data\out.csv
```

### Opción B: activar el entorno virtual y luego ejecutar
```powershell
.\.venv\Scripts\Activate.ps1
python -m todo_cli --db .\data\demo.json list --all
```


## 4) Cómo probar (evidencia fuerte): correr tests
Esto es lo que más le gusta al profe porque demuestra cumplimiento del SPEC.

```powershell
.\.venv\Scripts\python.exe -m pytest -q
```

Si ves algo como `9 passed`, ya está validado.


## 5) Si sale un error típico
### “python no se reconoce”
Usa siempre la ruta del venv:
- `.\.venv\Scripts\python.exe ...`

### Estabas dentro de `.venv\Scripts` y corriste `.python.exe ...`
Eso no es recomendable. Vuelve a la raíz del proyecto:

```powershell
cd ..\..
```

Y ejecuta con:
- `.\.venv\Scripts\python.exe -m todo_cli ...`


## 6) Evidencia para entregar
- Captura de:
  - `PROMPTS.md` (prompts usados)
  - `SPEC.md` (requerimientos)
  - `ANALISIS.md` (resultado)
  - Output de `python -m pytest -q` (tests pasando)

Listo: con eso puedes explicar qué hizo la IA y cómo se prueba.
