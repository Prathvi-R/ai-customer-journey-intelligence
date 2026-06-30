# Architecture Decisions

## ADR-001

Collectors never call AI.

Reason:

Data collection should remain deterministic and reproducible.

---

## ADR-002

Only agents perform reasoning.

Reason:

Maintains separation of concerns and allows AI providers to be swapped without modifying the crawl layer.

---

## ADR-003

Pydantic models define all system contracts.

Reason:

Provides validation, serialization and maintainability.

---

## ADR-004

Async Playwright is the browser engine.

Reason:

Reliable rendering of modern JavaScript websites.

---

## ADR-005

Website traversal uses Breadth First Search.

Reason:

Predictable crawl order and easier depth control.

---

## ADR-006

All outputs are versioned.

Example

schema_version: "1.0"

Reason:

Allows future schema evolution without breaking compatibility.