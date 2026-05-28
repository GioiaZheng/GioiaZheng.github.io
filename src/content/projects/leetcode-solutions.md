---
title: Leetcode-Solutions
summary: Structured algorithm-practice repo with per-problem READMEs, a generated catalog, and a pytest harness.
order: 9
featured: false
status: maintained
last_updated: "2026-05-28"
repo: https://github.com/GioiaZheng/Leetcode-Solutions
tags: ["algorithms", "python", "study-notes"]
---

A personal practice repo deliberately structured as a small software project rather than a dump of one-off files.

## Problem

Most algorithm-practice repos are append-only directories with no shared scaffolding, no tests, and no traceable mapping from problem to pattern. That makes them useless for revisiting, refactoring, or measuring coverage against curated study paths.

## What I built

A Python repo with one directory per problem, a generated catalog driven by a single `metadata.json` source-of-truth, written pattern notes, and overlays that mark coverage against curated paths (Blind 75, NeetCode 150).

## Technical components

<dl class="kv">
  <dt>Language</dt><dd>Python</dd>
  <dt>Tests</dt><dd>pytest harness exercising public LeetCode signatures</dd>
  <dt>Structure</dt><dd>Per-problem directory, per-pattern notes under <code>0000-notes/</code>, curated paths under <code>paths/</code></dd>
  <dt>Generation</dt><dd><code>scripts/update_indexes.py</code> regenerates <code>CATALOG.md</code> + <code>TOPICS.md</code> + featured tables from <code>metadata.json</code></dd>
  <dt>CI</dt><dd>GitHub Actions "quality" workflow on every push</dd>
</dl>

## Evidence / outputs

- 99 problem directories, 99 reference solutions, Easy 28 / Medium 52 / Hard 19.
- 13 problems with reviewed AI-card showcases across Blind 75 (10 tagged) and NeetCode 150 paths.
- Generated, derived-from-source-of-truth catalog and topic index in-repo.

## Current status

Maintained. Expanded incrementally rather than in bursts.

## Limitations

- Not a complete coverage of either curated list yet.
- Complexity analysis is prose only — no formal proofs.

## Repo

[github.com/GioiaZheng/Leetcode-Solutions](https://github.com/GioiaZheng/Leetcode-Solutions)
