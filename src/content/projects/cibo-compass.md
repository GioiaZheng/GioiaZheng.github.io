---
title: CiboCompass
summary: React Native + Go mobile app exploring offline-first sync for menu reading.
order: 8
featured: false
status: archived
last_updated: "2026-05-27"
repo: https://github.com/GioiaZheng/CiboCompass
tags: ["mobile", "react-native", "go", "offline-sync"]
---

Cross-platform mobile app exploring offline-first synchronisation patterns against a Go REST backend. Project was a design / HCI exercise more than a backend exercise.

## Problem

Most mobile menu-reading tools assume always-online and a single language. The brief was to explore what changes — at the storage layer, the sync protocol, and the UI — when neither assumption holds.

## What I built

A React Native (Expo) client and a Go REST backend with a local SQLite cache on-device, sync-on-reconnect semantics, and culturally-aware exploration of dishes for international students.

## Technical components

<dl class="kv">
  <dt>Client</dt><dd>React Native + Expo</dd>
  <dt>Backend</dt><dd>Go REST API</dd>
  <dt>Storage</dt><dd>SQLite on-device + server-side persistence</dd>
  <dt>Sync</dt><dd>Offline-first; reads from local cache, writes reconcile on reconnect</dd>
</dl>

## Evidence / outputs

- Working iOS / Android build with on-device cache populated from the API.
- Sync exercised under simulated connectivity drops.

## Current status

Archived. The offline-sync patterns were the goal; once those landed, active development stopped.

## Limitations

- No authentication.
- SQLite-only backend; no scaling story.
- Single-region content coverage.

## Repo

[github.com/GioiaZheng/CiboCompass](https://github.com/GioiaZheng/CiboCompass)
