# OneNode Atlas — Roadmap

## Delivery strategy

Build a polished vertical slice first: a real repository produces a real world, a user can explore it, and Atlas can explain it. Add breadth only after that loop works.

## Milestone 1 — Foundation

**Goal:** A maintainable application skeleton.

- Initialize Next.js, TypeScript, Tailwind, and the React Three Fiber scene.
- Create FastAPI service, typed models, and health endpoint.
- Establish frontend/backend data contracts.
- Add project documentation and environment configuration.

**Done when:** The app launches locally and displays a blank, stable 3D canvas connected to the backend.

## Milestone 2 — First Breath of Atlas

**Goal:** Establish the product’s visual identity.

- Build the dark holographic landing experience.
- Add the Atlas Core, ambient particles, and Atlas orb.
- Add repository URL input and construction-state UI.
- Build a mock world with districts, buildings, roads, bloom, and basic camera controls.

**Done when:** A user can experience the landing and construction sequence without repository analysis.

## Milestone 3 — Repository analysis and knowledge graph

**Goal:** Replace mock data with evidence-backed repository information.

- Clone/filter a public repository.
- Extract structure, languages, imports, likely entry points, and bounded Git metadata.
- Build the knowledge graph and return a repository summary.
- Create a world generator that maps the graph to a stable world model.

**Done when:** A small public repository generates a recognizable, data-derived world.

## Milestone 4 — Explore and understand

**Goal:** Make the world useful rather than merely visual.

- Add node selection, labels, context panel, and relationship highlighting.
- Add progressive disclosure from districts to neighborhoods/files.
- Add summary panel with high-confidence repository facts.
- Implement focus-camera movement.

**Done when:** A user can identify major modules, inspect a selected item, and understand its direct connections.

## Milestone 5 — Atlas AI guide

**Goal:** Add grounded explanation and the signature guided tour.

- Add provider adapter and local-model configuration.
- Implement grounded question answering over graph/source/history context.
- Return UI directives for highlights and camera focus.
- Generate a short guided tour with 3–5 stops.

**Done when:** Atlas can explain a selected module and lead a complete 45–60 second tour.

## Milestone 6 — Simplified evolution

**Goal:** Show that software has history.

- Build initial, middle, and current snapshots from Git history.
- Animate growth, removal, and important relationship changes.
- Add compact timeline controls.

**Done when:** The user can compare three meaningful moments in the repository’s evolution.

## Milestone 7 — Polish and demo readiness

**Goal:** Make the core story reliable and memorable.

- Tune camera timings, bloom, labels, construction, and guided narration.
- Test a small demo repository and a larger repository overview.
- Add loading/error states, input validation, and graceful fallbacks.
- Prepare README, demo script, screenshots, and a short video.

**Done when:** The complete demo can run end-to-end reliably in under three minutes.

## Scope guard

When a new idea appears, ask: “Does it make the V1 loop—analyze, explore, understand—materially better?” If not, add it to Future Ideas and continue shipping the current milestone.
