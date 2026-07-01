# AI Customer Journey Intelligence

An AI-powered platform that crawls websites, extracts structured data, analyzes customer journeys, and builds a rich knowledge base for downstream AI applications.

---

## Overview

AI Customer Journey Intelligence automatically discovers and analyzes websites to understand:

- Customer journeys
- Website structure
- Navigation patterns
- Contact information
- SEO quality
- Business information
- Trust signals
- Content organization

The long-term vision is to power AI agents capable of answering business questions, recommending UX improvements, generating customer personas, and building intelligent knowledge graphs.

---

# Current Features

## Website Crawling

- Breadth-First Search crawler
- Playwright-powered rendering
- JavaScript support
- Internal link discovery
- Crawl queue management
- Configurable crawl depth
- Duplicate URL detection
- URL normalization

---

## Structured Extraction

Each crawled page extracts:

### Metadata

- Title
- Meta Description
- Language
- Canonical URL
- Robots
- Keywords
- Favicon

### Open Graph

- OG Title
- OG Description
- OG Image
- OG URL

### Twitter Cards

- Twitter Card
- Twitter Title
- Twitter Description
- Twitter Image

### Content

- Headings
- Paragraphs
- Buttons
- Forms
- Images
- Lists
- Tables

### Links

- Internal links
- External links
- Mail links
- Telephone links
- Download links
- Anchor links

### Structured Data

- JSON-LD
- Schema Types

---

## Page Classification

Pages are automatically classified into:

- Home
- About
- Service
- Project
- Product
- Blog
- Contact
- Career
- Other

---

## Website Analysis

### Contact Analyzer

Automatically extracts:

- Emails
- Phone numbers
- Social media profiles

### Customer Journey Analyzer

Builds an initial customer journey including:

- Entry pages
- Awareness pages
- Consideration pages
- Trust pages
- Conversion pages
- Support pages

---

## Storage

Every crawl produces:

```
data/
└── website/
    └── YYYY-MM-DD_HH-MM-SS/
        ├── crawl.json
        ├── website.json
        └── pages/
            ├── page_1.json
            ├── page_2.json
            └── ...
```

---

# Project Structure

```
app/
│
├── analyzers/
│   ├── contact.py
│   ├── journey.py
│   └── website.py
│
├── collectors/
│   ├── crawl_state.py
│   └── website.py
│
├── models/
│
├── pipelines/
│
├── services/
│   ├── extraction/
│   │   ├── content.py
│   │   ├── extractor.py
│   │   ├── links.py
│   │   ├── schema.py
│   │   └── seo.py
│   │
│   ├── browser.py
│   ├── classification.py
│   ├── storage.py
│   └── url.py
│
└── utils/
```

---

# Technologies

- Python 3.14
- Playwright
- BeautifulSoup
- Pydantic
- Loguru

---

# Example Pipeline

```
Website
      │
      ▼
Website Collector
      │
      ▼
Extraction Service
      │
      ▼
Page Classification
      │
      ▼
Website Analyzer
      │
      ├── Contact Analyzer
      └── Journey Analyzer
      │
      ▼
Storage
```

---

# Roadmap

## Phase 1 — Crawling

- [x] BFS crawler
- [x] JavaScript rendering
- [x] URL normalization
- [x] Crawl state

---

## Phase 2 — Extraction

- [x] Metadata
- [x] SEO
- [x] OpenGraph
- [x] Twitter Cards
- [x] Content
- [x] Images
- [x] Forms
- [x] Links
- [x] JSON-LD

---

## Phase 3 — Analysis

- [x] Page classification
- [x] Contact extraction
- [x] Customer journey analysis

---

## Phase 4 — Navigation Intelligence

- [ ] Navigation graph
- [ ] Site hierarchy
- [ ] Page relationships
- [ ] Funnel detection

---

## Phase 5 — Business Intelligence

- [ ] Trust analyzer
- [ ] Project analyzer
- [ ] Product analyzer
- [ ] Team analyzer
- [ ] FAQ analyzer
- [ ] Blog analyzer

---

## Phase 6 — AI Layer

- [ ] Embeddings
- [ ] Vector database
- [ ] Knowledge graph
- [ ] Semantic search

---

## Phase 7 — Customer Journey Intelligence

- [ ] Persona detection
- [ ] User intent
- [ ] Journey optimization
- [ ] UX bottleneck detection
- [ ] Conversion opportunity detection

---

## Phase 8 — AI Agents

- [ ] Website Q&A
- [ ] UX recommendation agent
- [ ] Marketing strategy agent
- [ ] Competitor comparison
- [ ] Sales intelligence

---

# Current Progress

```
██████████████░░░░░░░░░░░░░░░░░░ 35%

✓ Website Crawling
✓ Structured Extraction
✓ Page Classification
✓ Contact Analysis
✓ Customer Journey
□ Navigation Graph
□ Knowledge Graph
□ AI Intelligence
```

---

# Running

Install dependencies

```bash
pip install -r requirements.txt
```

Run the pipeline

```bash
python run.py
```

Run tests

```bash
python -m tests.test_extractor

python -m tests.test_collector
```

---

# Vision

The goal is to evolve this project into a complete AI-powered Customer Journey Intelligence platform capable of understanding any business website, modeling user journeys, building semantic knowledge graphs, and enabling intelligent AI agents for marketing, product management, and UX optimization.
