# OneNode Atlas — World Rules

## Purpose

The Atlas world is a visual language for software. It is not a decorative city. Every element must communicate a fact, relationship, or state derived from the repository.

## Atlas language

| Software concept | Atlas representation | Meaning |
|---|---|---|
| Repository | Atlas Core / floating world | The bounded knowledge space being explored |
| Major top-level module | District | A major architectural area |
| Nested folder | Neighborhood | A local area within a district |
| Source file | Building | An explorable unit of implementation |
| Important entry/core file | Landmark | A highly visible starting point or system anchor |
| Import/dependency | Road | A direct relationship between components |
| Strong module relationship | Highway | High-volume or high-importance cross-module dependency |
| External service/library | Portal or bridge | A connection beyond the Atlas world |
| Documentation | Library | A discovery point for repository knowledge |
| Tests | Academy | Verification and learning infrastructure |
| Configuration | Control center | System-wide operational settings |
| Data store signal | Power station | A persistent/shared system resource |

Domain labels such as “power station” are presentation metaphors only. The analyzer must not assert a database or API role unless it has evidence.

## Geometry rules

- District size reflects the bounded aggregate importance of its visible contents.
- Building height reflects a normalized combination of importance, connectivity, and size/complexity proxy.
- Landmarks are reserved for likely entry points, highly central nodes, or explicitly recognized configuration roots.
- Buildings within a district use a regular, readable layout rather than a physically realistic skyline.
- Roads are created only for meaningful internal relationships; noisy or duplicate edges are aggregated.

## Visual state rules

- **Electric blue:** default repository knowledge and navigable structure.
- **Violet:** Atlas AI guidance, active narration, and guided path.
- **Emerald:** healthy/confirmed/selected success state when applicable.
- **Amber:** attention state or incomplete confidence; never used to imply a defect without evidence.
- **Crimson:** explicit errors only, not speculative “bad code.”
- **Glow intensity:** recent activity or current focus, based on available Git data.
- **Pulses on roads:** represented relationships/data flow; in V1 these are illustrative dependency pulses, not runtime telemetry.

## Interaction rules

- Hover raises emphasis, reveals a concise label, and never obscures nearby context.
- Selecting an entity highlights its direct roads and dims unrelated scene elements slightly.
- The camera moves smoothly to selected entities; it must never teleport.
- The context panel uses plain software terms alongside the Atlas metaphor so users are never confused.
- Atlas AI should highlight or focus the world whenever that is more informative than a text-only answer.

## Construction and time rules

- During construction, districts materialize before buildings; roads appear after their endpoints exist.
- New entities in a timeline snapshot assemble or rise.
- Removed entities fade/dissolve rather than simulate destruction.
- Changed relationships reroute as roads; Atlas does not claim causality unless Git evidence supports it.
- V1 timeline uses only initial, middle, and current snapshots.

## Accessibility and clarity

- Color is never the only signal; labels, shapes, and panels carry meaning.
- Motion can be reduced or skipped.
- Bloom, particles, and camera effects are restrained so labels and relationships remain readable.
- The product should explain its visual language in a short first-tour introduction and a compact legend.
