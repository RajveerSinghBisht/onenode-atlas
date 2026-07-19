# OneNode Atlas Backend

This directory contains the FastAPI foundation for OneNode Atlas. It provides the initial HTTP service boundary that later sprints will extend for repository analysis, knowledge graph generation, AI orchestration, world generation, and Git integration.

## Structure

```text
backend/
├── app/
│   ├── api/routes/     # HTTP route modules
│   ├── analyzers/      # Future repository analyzers
│   ├── core/           # Future core application modules
│   ├── models/         # Pydantic request and response models
│   ├── services/       # Future application services
│   ├── utils/          # Shared utilities
│   └── main.py         # FastAPI application entry point
├── tests/              # Future automated tests
└── requirements.txt    # Runtime dependencies
```

## Install dependencies

From the `backend` directory, create and activate a virtual environment, then install the requirements:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

## Run the server

```bash
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- OpenAPI schema: `http://127.0.0.1:8000/openapi.json`
