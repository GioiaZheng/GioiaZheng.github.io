---
title: CiboCompass
summary: React Native + Go mobile app with REST API and offline-first sync.
order: 4
status: paused
repo: https://github.com/GioiaZheng/CiboCompass
tags: ["mobile", "react-native", "go", "offline-sync"]
---

Cross-platform mobile app exploring offline-first synchronisation patterns against a Go REST backend.

## Problem

Most mobile menu-reading tools assume always-online and a single language. This project explored what changes — at the storage layer, the sync protocol, and the UI — when neither assumption holds.

## What I built

A React Native client and a Go REST backend with a local SQLite cache on-device, sync-on-reconnect semantics, and culturally-aware translation of menu content for international students.

## Technical components

<dl class="kv">
  <dt>Client</dt><dd>React Native</dd>
  <dt>Backend</dt><dd>Go REST API</dd>
  <dt>Storage</dt><dd>SQLite on-device + server-side persistence</dd>
  <dt>Sync</dt><dd>Offline-first with reconcile-on-reconnect</dd>
</dl>

## Evidence / outputs

- Working iOS / Android build with on-device cache populated from the API.
- Sync exercised under simulated connectivity drops.

## Current status

Paused. The offline-sync patterns were the goal; once those landed, active development stopped.

## Limitations

Translation quality is dependent on the upstream service; no in-house model. Single-region content coverage.

## Repo

<a href="https://github.com/GioiaZheng/CiboCompass">github.com/GioiaZheng/CiboCompass</a>
