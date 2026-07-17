---
title: rag-observatory
summary: Local-first, trace-based observability and failure analysis for inspectable and reproducible RAG runs.
order: 2
featured: true
academic: true
status: active
last_updated: "2026-07-17"
repo: https://github.com/GioiaZheng/rag-observatory
tags: ["rag", "observability", "failure-analysis", "reproducibility"]
---

<dl class="summary-grid">
  <dt>Focus</dt>
  <dd>Trace-based observability and failure-level diagnosis for retrieval-augmented generation</dd>
  <dt>Inputs</dt>
  <dd>Versioned JSON traces containing queries, retrieved evidence, answers, metrics, and provenance</dd>
  <dt>Outputs</dt>
  <dd>Validated traces, failure labels, comparisons, benchmark summaries, and inspectable Markdown / HTML reports</dd>
  <dt>Status</dt>
  <dd>Active &mdash; core schema and reporting loop implemented; interfaces remain early</dd>
</dl>

## Problem

A single aggregate score rarely explains why a RAG system failed. The source may be retrieval, reranking, evidence use, unsupported generation, or the evaluation setup itself. Without a shared trace contract, these failures are difficult to inspect across runs and easy to hide behind averages.

## What I built

A local-first research-engineering toolkit that turns RAG execution traces into inspectable artifacts. It validates trace structure, applies manual or heuristic failure labels, compares runs, and produces reports that preserve the evidence and provenance behind each conclusion.

The project is deliberately not another RAG pipeline or chatbot framework. Its role is the diagnostic layer around experiments: capture what happened, make failures reviewable, and keep comparisons reproducible.

## Technical components

<dl class="kv">
  <dt>Trace contract</dt><dd>Versioned JSON schema for queries, retrieved passages, generated answers, metrics, labels, and run provenance</dd>
  <dt>Failure analysis</dt><dd>Manual and heuristic categories spanning retrieval, evidence use, and generation errors</dd>
  <dt>Evidence inspection</dt><dd>Claim-level support views and attribution-oriented diagnostics</dd>
  <dt>Run comparison</dt><dd>Trace-to-trace comparisons, benchmark summaries, and conversation-level reports</dd>
  <dt>Reports</dt><dd>Portable Markdown and HTML outputs with SVG previews for local inspection</dd>
  <dt>Evaluation</dt><dd>Utilities for checking failure labels and quality dimensions rather than relying only on aggregate metrics</dd>
  <dt>Interoperability</dt><dd>OpenTelemetry-aligned fields and adapters for <code>msmarco-genqa</code> exports</dd>
  <dt>Quality gates</dt><dd>Tests, Ruff, mypy, pre-commit, and a reproducible small workflow</dd>
</dl>

## Reproduce a small run

```sh
make reproduce-small
```

The workflow produces normalized traces, human-readable reports, run comparisons, and a manifest suitable for review. Checked-in synthetic examples make the output format inspectable without requiring a full dataset-scale experiment.

<aside class="callout">
  <div class="callout-label">Current evidence boundary</div>
  <ul>
    <li>The checked-in workflow is intentionally small and synthetic; it demonstrates the trace and reporting contract, not a dataset-scale benchmark claim.</li>
    <li>Heuristic labels support inspection and iteration, but they are not a learned failure classifier.</li>
    <li>The project is a research toolkit, not yet a production telemetry backend or hosted dashboard.</li>
  </ul>
</aside>

## Current status

Active. The core trace-validation, reporting, comparison, and evaluator-protocol loop is in place. The next milestone is broader reviewed trace coverage from real experiments, followed by stronger agreement and robustness analysis for the failure taxonomy.

## Repo

[github.com/GioiaZheng/rag-observatory](https://github.com/GioiaZheng/rag-observatory)
