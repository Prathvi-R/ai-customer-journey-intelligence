# AI Customer Journey Intelligence
### AI_CONTEXT.md
Version: 1.0
Last Updated: June 2026

---

# Purpose

This document is the canonical context for every AI assistant working on this repository.

Before suggesting architecture, writing code, or reviewing implementations, always read this file first.

This document overrides assumptions.

---

# Project Vision

This project is NOT a website crawler.

This project is an enterprise-grade Company Intelligence Platform powered by Agentic AI.

The long-term objective is to autonomously analyze a company's complete digital presence and generate executive-level business recommendations.

The website is only the first data source.

Eventually the system should understand an entire business.

---

# End Goal

The final product should be capable of ingesting

- Company Website
- Google Reviews
- Instagram
- LinkedIn
- Facebook
- YouTube
- PDFs
- Brochures
- Floor Plans
- Price Lists
- News Articles
- Other digital assets

↓

convert them into structured company knowledge

↓

allow multiple AI agents to reason over that knowledge

↓

generate business recommendations

↓

produce executive reports.

---

# Guiding Principle

Everything in this repository exists to support intelligent reasoning.

Collectors never perform reasoning.

Agents never crawl websites.

Responsibilities are always separated.

---

# High-Level Architecture

Company Assets

↓

Collectors

↓

Structured Data

↓

Knowledge Layer

↓

Knowledge Graph (future)

↓

LangGraph Agent System

↓

Executive Reports

↓

Dashboard

---

# Current Development Phase

Phase 1

Website Intelligence Engine

Current objective:

Build a production-quality crawler capable of extracting structured website information.

No AI.

No embeddings.

No reasoning.

Only deterministic structured extraction.

---

# Technology Stack

Language

Python 3.14

Libraries

Playwright

BeautifulSoup

Pydantic

LangChain

LangGraph

OpenAI

FastAPI

Streamlit

ChromaDB

Git

GitHub

---

# Current Repository Structure

app/

    agents/

    collectors/

    models/

    pipelines/

    prompts/

    services/

    utils/

    config.py

    settings.py

    main.py

Other folders

dashboard/

data/

docs/

reports/

tests/

vectorstore/

---

# Folder Responsibilities

agents/

Contains AI reasoning.

Never performs crawling.

Never performs storage.

Never contains scraping logic.

---

collectors/

Responsible for data acquisition only.

No AI.

No embeddings.

No business logic.

Only collection.

---

models/

Pure Pydantic models.

No methods besides validation.

These are the contracts of the system.

---

services/

Business logic.

Extraction.

Persistence.

Browser utilities.

Storage.

No orchestration.

---

pipelines/

Coordinates workflows.

Uses collectors.

Uses services.

Returns final outputs.

---

prompts/

Prompt templates.

No Python logic.

---

utils/

Shared utilities.

Logging.

Helper functions.

Constants.

---

# Architectural Principles

1.

Single Responsibility Principle

Every module should perform one responsibility.

---

2.

Strong Typing

Everything should use

- type hints
- Pydantic models

---

3.

Async First

Network operations should always be asynchronous.

---

4.

Deterministic Collection

Collectors should produce identical outputs for identical inputs.

---

5.

Reproducibility

Every crawl should be reproducible.

---

6.

No Hidden AI

Collectors never call LLMs.

Services never call LLMs.

Only agents use AI.

---

# Data Flow

Website

↓

WebsiteCollector

↓

PageData

↓

WebsiteData

↓

JSON

↓

Knowledge Base

↓

Agent Graph

↓

Reports

---

# Current Models

Existing

PageData

Planned

WebsiteData

CrawlConfig

CrawlResult

CrawlError

PageArtifact

DiscoveredLink

CompanyData (future)

---

# Planned Collectors

Website

Google Reviews

Instagram

LinkedIn

Facebook

YouTube

PDF

News

---

# Planned Agents

Journey Agent

UX Agent

Persona Agent

Strategy Agent

Report Agent

Eventually

Market Agent

Competitor Agent

Sales Agent

Growth Agent

Vision Agent

---

# Knowledge Layer

Phase 2

ChromaDB

Embeddings

Semantic Retrieval

Future

Knowledge Graph

The long-term objective is not simply vector search.

The project should understand relationships between

Projects

Amenities

Pricing

Navigation

Forms

Testimonials

Reviews

Locations

CTAs

etc.

This will eventually allow graph-based reasoning.

---

# Website Intelligence Engine

Responsibilities

Discover pages

Normalize URLs

Ignore external domains

Respect crawl limits

Extract structured content

Capture screenshots

Generate deterministic JSON

Never call AI

---

# Coding Standards

Production quality only.

No tutorial code.

No shortcuts.

Prefer readability over cleverness.

Prefer maintainability over premature optimization.

Everything should contain

- type hints
- logging
- docstrings

Avoid print().

---

# Git Philosophy

Every commit should represent a working milestone.

Preferred commit examples

Implement website crawler

Add extraction service

Implement screenshot capture

Add WebsiteData model

Integrate ChromaDB

Implement Journey Agent

Avoid

"updates"

"changes"

"fix"

unless absolutely necessary.

---

# Documentation Philosophy

Whenever architecture changes,

update

ARCHITECTURE.md

ROADMAP.md

DECISIONS.md

AI_CONTEXT.md

Documentation is part of the codebase.

---

# Decision Log

Current important decisions

✔ Collectors never call AI

✔ Services contain business logic

✔ Pipelines orchestrate

✔ Agents reason

✔ Pydantic models define contracts

✔ Async Playwright

✔ BFS website traversal

✔ Versioned JSON outputs

✔ Screenshot capture

✔ Strong separation of concerns

---

# Future Vision

The project should eventually become something closer to

Company Intelligence Platform

than

Website Audit Tool.

The crawler is only one subsystem.

The final product should allow a CEO, product manager, or consultant to ask

"Analyze this company."

and automatically receive

Customer Journey

UX Issues

Conversion Bottlenecks

Competitive Positioning

Brand Consistency

Growth Opportunities

Executive Recommendations

generated from every available company asset.

---

# AI Assistant Instructions

Whenever contributing:

Read this document first.

Preserve architectural boundaries.

Do not introduce unnecessary abstractions.

Recommend production-quality solutions.

Think like a senior engineer performing a pull request review.

Challenge architectural decisions if there is a significantly better alternative.

When uncertain,

favor scalability,

maintainability,

clarity,

and modularity.

The objective is not merely to make the project work.

The objective is to build a repository that demonstrates enterprise software engineering, agentic AI architecture, and product thinking at a level that stands out to recruiters and hiring managers.