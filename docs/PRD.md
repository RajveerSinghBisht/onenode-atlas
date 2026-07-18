# OneNode Atlas — Product Requirements Document

## 1. Problem

Large or unfamiliar repositories are hard to understand. File trees reveal storage structure, not architectural importance. Developers must manually reconstruct relationships, entry points, and history from many disconnected sources.

## 2. Solution

Atlas accepts a public GitHub repository URL, analyzes its structure and Git history, and produces:

- A holographic, interactive world representing the repository.
- A repository summary with key structural facts.
- Context panels for selected modules and files.
- An AI guide for grounded repository questions.
- A guided onboarding tour.
- A simplified historical view with three repository snapshots.

## 3. Primary user journey

1. A user pastes a public GitHub repository URL.
2. Atlas analyzes the repository and shows a construction sequence instead of a conventional loading spinner.
3. The world appears: major districts, meaningful connections, landmarks, and an overview.
4. Atlas offers **Start Tour** or **Explore Yourself**.
5. The user explores, selects a district or building, reads its context, and asks Atlas a question.
6. The user can switch among initial, middle, and current snapshots to see architectural evolution.

## 4. Functional requirements

### Repository import and analysis

- Accept a public GitHub URL.
- Clone or fetch the repository server-side.
- Exclude generated and irrelevant directories such as `.git`, `node_modules`, `dist`, `build`, `target`, and caches.
- Detect languages, framework signals, top-level modules, likely entry points, imports/dependencies, and basic Git metadata.
- Return a validated, structured repository model.

### Atlas World

- Render a stylized holographic world using a floating core/platform, neon geometry, roads, labels, particles, and bloom.
- Support hover, selection, orbit, pan, zoom, and camera focus transitions.
- Generate the world from repository data, not a hand-authored scene.
- Render only the appropriate detail for the current level of exploration.

### Context and summary

- Show repository name, detected languages/framework, architecture summary, major modules, likely entry points, and repository size.
- Show selected-node details: name, path, type, direct relationships, available history metadata, and a short explanation.
- Surface at most two or three high-confidence observations; do not overclaim.

### Atlas AI Guide

- Answer questions using the repository model and retrieved source/history context.
- Explain selected areas and recommend where a newcomer should start.
- Return optional visual instructions: nodes to highlight and an intended camera target.
- Avoid unsupported claims; indicate uncertainty when evidence is incomplete.

### Guided tour

- Offer a 45–60 second tour after analysis.
- Visit 3–5 significant modules.
- Highlight relevant districts/roads while presenting concise narration.
- Allow the user to skip, pause, or exit to free exploration.

### Timeline

- Provide three representative snapshots: initial, middle, and current.
- Animate additions, removals, and major connection changes between snapshots.
- This is not a full commit-by-commit playback in V1.

## 5. Non-functional requirements

- Keep interaction responsive by using progressive disclosure and efficient rendering.
- Treat large repositories as a hierarchy: overview → districts → neighborhoods → files.
- Use deterministic heuristics for core graph data; AI enriches understanding but must not be the sole source of structural facts.
- Keep the application usable without a paid service when a local model is configured.

## 6. V1 exclusions

Atlas V1 explicitly excludes:

- Proactive AI alerts and autonomous recommendations.
- Runtime debugging or guided investigations.
- Security analysis, code review, refactoring advice, or performance audits.
- Authentication, accounts, collaboration, sharing, plugins, or cloud sync.
- GitLab/Bitbucket/local repository connectors.
- Full commit-by-commit time travel.
- Voice interaction as a dependency for the core demo.

## 7. Success criteria

- A first-time user can identify the major areas of a repository and where to begin.
- A user can select a module, understand its role and connections, and receive a grounded explanation.
- The guided tour makes the product’s value clear within one minute.
- The demo remains visually polished while presenting real repository-derived information.
