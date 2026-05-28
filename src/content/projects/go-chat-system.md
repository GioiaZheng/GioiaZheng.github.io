---
title: go-chat-system
summary: Coursework full-stack chat baseline — Go REST backend, embedded Vue UI, OpenAPI contract.
order: 7
featured: false
status: archived
last_updated: "2026-05-27"
repo: https://github.com/GioiaZheng/go-chat-system
tags: ["backend", "go", "rest", "sqlite"]
---

Coursework chat application implemented end-to-end as a single-binary Go service. Scope is deliberately a homework baseline, not a production system.

## Problem

The course brief required a self-contained chat service with REST endpoints, persistent storage, an OpenAPI contract, and a UI good enough for grading and manual QA — shipped as one buildable artifact.

## What I built

A Go HTTP service exposing authenticated REST endpoints for users, rooms, and messages, backed by SQLite for durable storage. The Vue frontend is built and embedded into the binary so the service ships as a single executable.

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

- Working single-binary build that boots, serves the embedded UI, and exercises every API endpoint end-to-end.
- OpenAPI document under [`doc/`](https://github.com/GioiaZheng/go-chat-system/tree/main/doc) as the contract source-of-truth.

## Current status

Archived. The course grading goal was met; not actively expanded.

## Limitations

- Course-grade authentication; not hardened for production.
- Single-node, SQLite-backed; no horizontal-scaling story.
- WebSocket / streaming intentionally out of scope; REST polling is the transport.
- No comparative benchmark — this is an implementation exercise, not a research artifact.

## Repo

[github.com/GioiaZheng/go-chat-system](https://github.com/GioiaZheng/go-chat-system)
