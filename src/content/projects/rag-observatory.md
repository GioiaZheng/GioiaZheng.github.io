---
title: rag-observatory
summary: Research prototype for trace-based RAG observability and failure analysis.
order: 2
featured: true
academic: true
status: active
last_updated: "2026-07-27"
repo: https://github.com/GioiaZheng/rag-observatory
demo: https://huggingface.co/spaces/GioiaZheng/rag-observatory
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
  <dd>Research prototype &mdash; core reporting loop implemented and exercised on 40 public BEIR SciFact traces</dd>
</dl>

## Problem

A single aggregate score rarely explains why a RAG system failed. The source may be retrieval, reranking, evidence use, unsupported generation, or the evaluation setup itself. Without a shared trace contract, these failures are difficult to inspect across runs and easy to hide behind averages.

## What I built

A local-first research prototype that turns RAG execution traces into inspectable artifacts. It validates trace structure, applies manual or heuristic failure labels, compares runs, and produces reports that preserve the evidence and provenance behind each conclusion.

The project is deliberately not another RAG pipeline or chatbot framework. Its role is the diagnostic layer around experiments: capture what happened, make failures reviewable, and keep comparisons reproducible.

## Evidence map

<dl class="summary-grid">
  <dt>Research question</dt>
  <dd>Which RAG failure mode becomes visible when retrieval depth, context selection, or trace observability changes?</dd>
  <dt>Key result</dt>
  <dd>On 20 fixed BEIR SciFact test queries, increasing BM25 retrieval depth from <code>top_k=1</code> to <code>top_k=5</code> produced 40 public traces and raised retrieval hits from 13/20 to 14/20. The same run also exposed a heuristic limitation: <code>retrieval_noise</code> fired on every <code>top_k=5</code> trace because any irrelevant retrieved document triggered the label.</dd>
  <dt>What I did</dt>
  <dd>Built trace validation, stage-aware reports, failure labels, run comparison, OpenTelemetry/OpenInference JSON ingestion, and configuration-sensitive diagnostics.</dd>
  <dt>Evidence</dt>
  <dd><a href="https://github.com/GioiaZheng/rag-observatory">GitHub repo</a> · <a href="https://github.com/GioiaZheng/rag-observatory/blob/main/docs/reports/2026-07-25-scifact-retrieval-depth.md">SciFact retrieval-depth report</a> · <a href="https://huggingface.co/spaces/GioiaZheng/rag-observatory">Hugging Face Space</a> · <a href="https://huggingface.co/datasets/GioiaZheng/rag-observatory-toy-traces">Toy trace dataset</a></dd>
</dl>

## Technical components

<dl class="kv">
  <dt>Trace contract</dt><dd>Versioned JSON schema for queries, retrieved passages, generated answers, metrics, labels, and run provenance</dd>
  <dt>Failure analysis</dt><dd>Manual and heuristic categories spanning retrieval, evidence use, and generation errors</dd>
  <dt>Evidence inspection</dt><dd>Claim-level support views and attribution-oriented diagnostics</dd>
  <dt>Run comparison</dt><dd>Trace-to-trace comparisons, benchmark summaries, and conversation-level reports</dd>
  <dt>Reports</dt><dd>Portable Markdown and HTML outputs with SVG previews for local inspection</dd>
  <dt>Evaluation</dt><dd>Utilities for checking failure labels and quality dimensions rather than relying only on aggregate metrics</dd>
  <dt>Interoperability</dt><dd>Offline OTLP/HTTP JSON ingestion for OpenInference retriever, reranker, and LLM spans</dd>
  <dt>Quality gates</dt><dd>107 automated tests plus Ruff, mypy, pre-commit, and container checks</dd>
</dl>

## Reproduce a small run

```sh
make reproduce-small
```

The workflow produces normalized traces, human-readable reports, run comparisons, and a manifest suitable for review. Checked-in synthetic examples make the output format inspectable without requiring a full dataset-scale experiment.

## Controlled SciFact retrieval-depth run

I also ran an actual retrieval-stage comparison over 20 fixed BEIR SciFact test queries. Deterministic BM25, the top-1 context policy, extractive generator, and qrels evaluator stayed fixed while `retrieval_top_k` changed from 1 to 5, producing 40 public traces.

| Configuration | Retrieval hit | Failure-labelled traces | Retrieval-stage failures |
| --- | ---: | ---: | ---: |
| `top_k=1` | 13/20 | 7/20 | 7/20 |
| `top_k=5` | 14/20 | 20/20 | 20/20 |

The extra retrieval depth recovered one additional relevant result, while the current `retrieval_noise` heuristic fired on every `top_k=5` trace because any irrelevant retrieved document triggers the label. The useful result is therefore not a clean victory metric: it exposes both a retrieval-depth trade-off and a limitation in the diagnostic heuristic.

<aside class="callout">
  <div class="callout-label">Current evidence boundary</div>
  <ul>
    <li>The SciFact run uses real public retrieval data, but 20 sorted queries remain an inspectable smoke experiment, not a dataset-wide claim.</li>
    <li>The generator is deterministic and extractive, so this is not a full generative RAG benchmark.</li>
    <li>Heuristic labels support inspection and iteration, but they are not a learned failure classifier.</li>
    <li>The project is a research prototype, not yet a production telemetry backend or hosted dashboard.</li>
  </ul>
</aside>

## Current status

Research prototype. Public trace conversion, OpenTelemetry/OpenInference JSON ingestion, stage-aware reports, configuration comparison, and a real SciFact smoke run are in place. The next study will examine chunk-boundary sensitivity under fixed evidence and evaluation settings.

## Public artifacts

- [Source repository](https://github.com/GioiaZheng/rag-observatory)
- [Interactive Space](https://huggingface.co/spaces/GioiaZheng/rag-observatory)
- [Toy trace dataset](https://huggingface.co/datasets/GioiaZheng/rag-observatory-toy-traces)
