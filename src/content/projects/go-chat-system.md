---
title: go-chat-system
summary: WASA course project built from the Fantastic Coffee starter — Go chat API, Vue UI, and SQLite.
order: 7
featured: false
status: archived
last_updated: "2026-07-18"
repo: https://github.com/GioiaZheng/go-chat-system
tags: ["backend", "go", "rest", "sqlite"]
---

Coursework chat application built from the WASA *Fantastic Coffee (decaffeinated)* starter and delivered as a single-binary Go service. Scope is deliberately a course project, not a production system.

## Problem

The course brief required a self-contained chat service with REST endpoints, persistent storage, an OpenAPI contract, and a UI good enough for grading and manual QA — shipped as one buildable artifact.

## What I built

Starting from the course scaffold, I implemented and extended the chat-specific user, one-to-one and group conversation, message, reply, forward, and deletion workflows. The submitted application connects those flows to SQLite, an OpenAPI contract, and a Vue frontend that can be embedded into the Go binary.

## Attribution

The starter supplied the initial full-stack project scaffold and WASA build conventions. The public repository begins with a full project upload rather than an untouched starter snapshot, so it cannot support file-by-file authorship claims. Later repository history separately records API and authorization tests, CI, security scans and documentation, dependency maintenance, and SQLite connection hardening.

## Technical components

<dl class="kv">
  <dt>Backend</dt><dd>Go (modules + vendoring), <code>cmd/webapi</code> daemon, <code>service/api</code> handlers</dd>
  <dt>Storage</dt><dd>SQLite via database/sql</dd>
  <dt>API</dt><dd>REST, documented in <code>doc/</code> as an OpenAPI spec</dd>
  <dt>Auth</dt><dd>Simplified token-based session model (coursework-grade)</dd>
  <dt>Frontend</dt><dd>Vue + Vite + Bootstrap, built and embedded into the Go binary</dd>
  <dt>Tests</dt><dd>Go test suite covering HTTP layer + storage round-trips</dd>
</dl>

## Evidence / outputs

- Working single-binary build with repository tests covering key user, conversation, message, authorization, and storage paths.
- OpenAPI document under [`doc/`](https://github.com/GioiaZheng/go-chat-system/tree/main/doc) as the contract source-of-truth.
- Feature- and phase-level attribution in the repository [`README`](https://github.com/GioiaZheng/go-chat-system#course-context-and-attribution), including links to the later maintenance commits.

## Current status

The course feature scope is closed. Repository maintenance continues for tests, dependencies, security checks, and correctness, but the project is not being expanded into a production messaging service.

## Limitations

- Course-grade authentication; not hardened for production.
- Single-node, SQLite-backed; no horizontal-scaling story.
- WebSocket / streaming intentionally out of scope; REST polling is the transport.
- No comparative benchmark — this is an implementation exercise, not a research artifact.

## Repo

[github.com/GioiaZheng/go-chat-system](https://github.com/GioiaZheng/go-chat-system)
