# IA conectada al Git (modo automático)

El profe pidió que el Git esté **conectado** a una IA de forma automática. En este repo se deja un ejemplo realista:

- Un workflow de GitHub Actions que puede ejecutarse manualmente (`workflow_dispatch`).
- El workflow lee `SPEC.md` (o cualquier archivo de requerimientos) y ejecuta un agente tipo **aider** (soporta GPT/Claude) para proponer cambios.
- El workflow crea un **Pull Request** automático con los cambios.

> Importante: por seguridad, el repo **no** incluye llaves. Las llaves se configuran como **GitHub Secrets**.

## 1) Qué instala / usa
- Herramienta: `aider-chat` (edita repos usando LLM y Git).
- Acción para PR: `peter-evans/create-pull-request`.

## 2) Configurar secretos (GitHub)
En tu repo → **Settings → Secrets and variables → Actions → New repository secret**.

Elige un proveedor:

### Opción A) OpenAI (ChatGPT)
- Secret: `OPENAI_API_KEY`

### Opción B) Anthropic (Claude)
- Secret: `ANTHROPIC_API_KEY`

## 3) Ejecutar el workflow
Repo → **Actions** → workflow **AI SDD (SPEC → PR)** → **Run workflow**.

Inputs:
- `requirements_file`: por defecto `SPEC.md`
- `instructions`: mensaje corto con lo que quieres implementar (ej: "Implementa RF-08: editar título de tarea")

## 4) Evidencia para el parcial
- Captura de pantalla de:
  - Secrets configurados (no muestres el valor)
  - Ejecución del workflow en Actions
  - PR creado automáticamente por la IA
  - CI en verde sobre ese PR

## 5) Nota de seguridad
- Nunca comitees llaves en el repo.
- Revisa el PR: la IA puede equivocarse.

## 6) Si falla con: "GitHub Actions is not permitted to create or approve pull requests"
Debes habilitar permisos de escritura para el token automático de Actions:

1) Repo → **Settings** → **Actions** → **General**
2) En **Workflow permissions** selecciona **Read and write permissions**
3) Activa **Allow GitHub Actions to create and approve pull requests**
4) Guarda y vuelve a ejecutar el workflow.
