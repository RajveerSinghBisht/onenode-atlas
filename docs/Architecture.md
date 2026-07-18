# OneNode Atlas — Architecture

## Architecture principle

Atlas separates repository facts, world generation, and AI narration. The renderer never has to infer repository meaning, and the AI never becomes the source of truth for file structure.

```text
Public GitHub URL
        |
        v
FastAPI Repository Analyzer
        |
        v
Repository Knowledge Graph
   ┌────┴───────────┐
   v                v
World Generator    AI Guide / Retrieval
   |                |
   └───────┬────────┘
           v
Next.js + React Three Fiber client
```

## Frontend

- **Next.js + React + TypeScript:** application shell, routes, panels, and API integration.
- **Tailwind CSS + shadcn/ui:** interface primitives and holographic visual styling.
- **Three.js + React Three Fiber + Drei:** world rendering and scene composition.
- **camera-controls:** smooth user navigation and programmatic focus transitions.
- **GSAP:** cinematic construction, guided-tour, and camera animations.
- **React Postprocessing:** restrained bloom, vignette, and atmosphere.
- **Zustand:** scene/UI state such as selected node, active snapshot, tour state, and camera target.

The frontend receives a world model, not raw source code. It renders districts, buildings, roads, labels, and their interaction metadata.

## Backend

- **Python + FastAPI:** analysis and AI API surface.
- **GitPython:** cloning and Git metadata/history collection.
- **Tree-sitter:** consistent multi-language parsing where grammars are available.
- **NetworkX:** dependency and repository graph construction.
- **Pydantic:** request/response validation and explicit data contracts.

The backend must bound analysis by configurable file count, size, and history limits. It should filter generated/vendor content before parsing.

## Knowledge graph

The knowledge graph is the canonical internal model. Nodes can represent repository, directory, file, symbol, external dependency, or snapshot. Edges can represent containment, import/dependency, export/reference, and historical relationship.

Each node stores only evidence-backed metadata, for example:

- Path and node type.
- Language and line count where available.
- Import and dependent relationships.
- Commit count, last changed time, and contributors where available.
- Importance score derived from deterministic graph and repository metrics.

## World generator

The world generator converts the knowledge graph into a frontend-friendly world model:

- Cluster major directories into districts.
- Create neighborhood clusters for child folders.
- Represent files as buildings only when that level is open.
- Size/height uses bounded importance, complexity proxies, and connectivity—not random values.
- Create roads from internal dependencies and gateways/bridges for external dependencies.
- Mark likely entry points and architectural cores as landmarks.

The output includes stable identifiers so selection, history snapshots, AI highlights, and animations refer to the same entities.

## AI layer

The AI layer is provider-agnostic. An adapter may use a local Ollama model for free/local operation or a hosted provider when configured.

V1 calls are limited to:

1. Repository overview enrichment.
2. Guided-tour narration and stop selection.
3. Grounded question answering over selected/retrieved repository context.

AI output is structured where it controls the interface, e.g. `answer`, `highlightNodeIds`, and `focusNodeId`. It should never invent node IDs or override structural data.

## Progressive disclosure and scale

Atlas uses semantic levels of detail:

| Level | Visible information |
|---|---|
| Overview | Repository summary and major districts |
| District | Neighborhoods and high-value relationships |
| Neighborhood | Files/buildings and local roads |
| File | File metadata, imports, exports, explanation |

This prevents rendering every file in large projects. The client should use instancing for repeated building geometry, cap labels, and load detailed entities on demand.

## Core API contracts

- `POST /analyze` — accepts a public GitHub URL and returns/creates an analysis job.
- `GET /repositories/{id}` — returns repository summary and current world model.
- `GET /repositories/{id}/nodes/{nodeId}` — returns contextual node details.
- `GET /repositories/{id}/snapshots` — returns initial, middle, and current world snapshots.
- `POST /repositories/{id}/ask` — returns a grounded AI answer and visual directives.
- `POST /repositories/{id}/tour` — returns ordered tour stops and narration.

Exact transport may be synchronous for a small demo repository and job-based for larger ones; the model and API contract remain the same.
