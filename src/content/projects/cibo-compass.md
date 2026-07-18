---
title: CiboCompass
summary: React Native + Go mobile app with offline-resilient rating submission and local caching.
order: 8
featured: false
status: archived
last_updated: "2026-07-18"
repo: https://github.com/GioiaZheng/CiboCompass
tags: ["mobile", "react-native", "go", "offline-sync"]
---

Cross-platform mobile app with offline-resilient rating delivery against a Go REST backend. The project began as a design / HCI exercise and later added a persistent retry queue and idempotent submission.

## Problem

Most mobile menu-reading tools assume always-online and a single language. The brief was to explore what changes — at the storage layer, the sync protocol, and the UI — when neither assumption holds.

## What I built

A React Native (Expo) client and a Go REST backend with local caching, a persistent retry queue, idempotent feedback submission, and culturally-aware exploration of dishes for international students.

## Technical components

<dl class="kv">
  <dt>Client</dt><dd>React Native + Expo</dd>
  <dt>Backend</dt><dd>Go REST API</dd>
  <dt>Storage</dt><dd>Local client cache + server-side SQLite persistence</dd>
  <dt>Delivery</dt><dd>Offline-resilient rating submission with a persistent retry queue and idempotent backend handling</dd>
</dl>

## Evidence / outputs

- Working iOS / Android build with on-device cache populated from the API.
- Sync exercised under simulated connectivity drops.

## Current status

Archived. The retry and idempotency work landed; broader synchronisation guarantees were outside the project scope.

## Limitations

- No authentication.
- SQLite-only backend; no scaling story.
- Single-region content coverage.
- No stable actor identity or cross-device conflict resolution.
- No complete synchronisation protocol.

## Repo

[github.com/GioiaZheng/CiboCompass](https://github.com/GioiaZheng/CiboCompass)
