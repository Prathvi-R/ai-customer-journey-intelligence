# Architecture

## Overview

AI Customer Journey Intelligence follows a layered architecture where each layer has a single responsibility.

```
Company Assets
        │
        ▼
+-------------------------+
|       Collectors        |
+-------------------------+
        │
        ▼
+-------------------------+
|   Structured Data       |
|  (Pydantic Models)      |
+-------------------------+
        │
        ▼
+-------------------------+
|   Knowledge Layer       |
| ChromaDB / JSON / Graph |
+-------------------------+
        │
        ▼
+-------------------------+
|    LangGraph Agents     |
+-------------------------+
        │
        ▼
+-------------------------+
| Reports & Dashboard     |
+-------------------------+
```

---

## Layers

### Collectors

Responsible only for collecting raw information.

Examples:

- Website
- PDFs
- Reviews
- Social Media

Collectors never call LLMs.

---

### Models

System contracts represented as Pydantic models.

Examples:

- PageData
- WebsiteData
- CrawlResult
- CrawlConfig

---

### Services

Reusable business logic.

Examples:

- HTML extraction
- Screenshot storage
- JSON persistence
- Browser management

---

### Pipelines

Coordinate collectors and services.

Pipelines orchestrate workflows but do not contain business logic.

---

### Agents

Reason over structured knowledge.

Examples:

- Journey Agent
- UX Agent
- Persona Agent
- Strategy Agent
- Report Agent

---

## Design Principles

- Single Responsibility
- Async-first
- Strong typing
- Production quality
- Deterministic collection
- Modular architecture