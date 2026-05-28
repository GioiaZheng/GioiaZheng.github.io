---
title: go-chat-system
summary: Concurrent Go chat backend with persistent storage, REST API, and an embedded Vue frontend.
order: 2
featured: true
status: maintained
repo: https://github.com/GioiaZheng/go-chat-system
tags: ["backend", "go", "rest", "sqlite"]
---

Self-contained full-stack chat service used as a practice ground for Go service design, REST contract discipline, and end-to-end testing without a heavy framework.

## Problem

Most "build a chat app" tutorials skip the parts that actually matter for a small production-shaped service: concurrent message fan-out under load, deterministic persistence semantics, an API contract that survives client refactors, and a frontend that the backend can serve without a separate deploy pipeline.

## What I built

A Go HTTP service exposing authenticated REST endpoints for users, rooms, and messages, backed by SQLite for durable storage. The Vue frontend is built and embedded into the binary so the service ships as a single artifact.

## Technical components

<dl class="kv">
  <dt>Language</dt><dd>Go</dd>
  <dt>Storage</dt><dd>SQLite via database/sql</dd>
  <dt>API</dt><dd>REST, documented under an OpenAPI spec</dd>
  <dt>Auth</dt><dd>Token-based session authentication</dd>
  <dt>Frontend</dt><dd>Vue, built and embedded into the Go binary</dd>
  <dt>Tests</dt><dd>Go test suite covering the HTTP layer + storage round-trips</dd>
</dl>

## Evidence / outputs

- Working binary that boots, serves the embedded UI, and exercises every API endpoint end-to-end.
- OpenAPI document checked into the repo as the contract source-of-truth.

## Current status

Maintained, not actively expanded. Used as a reference for clean Go service layout when I need one.

## Limitations

Single-node by design; no horizontal scaling story. WebSocket / streaming is intentionally out of scope — the goal was getting REST + persistence right before adding real-time transport.

## Repo

<a href="https://github.com/GioiaZheng/go-chat-system">github.com/GioiaZheng/go-chat-system</a>
