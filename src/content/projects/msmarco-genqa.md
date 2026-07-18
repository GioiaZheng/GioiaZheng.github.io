---
title: msmarco-genqa
summary: Reproducible retrieve → rerank → generate pipeline on MS MARCO with paired-bootstrap evaluation and a manifest-enforced reproducibility contract.
order: 1
featured: true
academic: true
status: active
last_updated: "2026-07-18"
repo: https://github.com/GioiaZheng/msmarco-genqa
tags: ["retrieval", "rag", "evaluation", "reproducibility"]
---

<dl class="summary-grid">
  <dt>System</dt>
  <dd>BM25 → dense (MiniLM L6) → cross-encoder rerank → T5-small generation</dd>
  <dt>Dataset</dt>
  <dd>MS MARCO passage, 8.8 M docs, 6 980 paired queries (dev/small)</dd>
  <dt>Main result</dt>
  <dd>Reranking lifts Token-F1 from 0.197 to 0.368 (Δ&nbsp;+0.171, 95 % CI [+0.163, +0.178], paired bootstrap)</dd>
  <dt>External retrieval</dt>
  <dd>TREC-DL 2019/2020 full-corpus BM25 + cross-encoder benchmark, independently cross-checked</dd>
  <dt>Reproducibility</dt>
  <dd>Schema-v2 manifest contract; <code>make reproduce-baseline</code> from clean clone</dd>
  <dt>Status</dt>
  <dd>Active &mdash; CPU-only, single-machine, CI-backed test suite</dd>
</dl>

## Problem

Surface generation metrics (Token-F1, ROUGE-L) on retrieve → rerank → generate pipelines do not, by themselves, tell you whether the generator's output is actually supported by the retrieved evidence. Reranking the retrieval stage can simultaneously raise surface metrics and reduce grounding on the same fixed generator. Quantifying this requires a pipeline where every component is exchangeable, every run is reproducible to a bit-level manifest, and statistical comparisons are paired and confidence-bounded.

## What I built

Four entry-point scripts under [`experiments/`](https://github.com/GioiaZheng/msmarco-genqa/tree/main/experiments) — one per pipeline stage — sharing a single source-of-truth config and writing a schema-versioned `manifest.json` next to every `metrics.json`. The contract is enforced at write time: a run that fails to capture the six required reproducibility fields cannot land an artifact.

## Headline result

Generation × retrieval source, full MS MARCO dev/small, 6 980 paired queries, paired bootstrap (N = 10 000).

<div class="metric-grid">
  <div class="metric">
    <div class="metric-label">Token-F1</div>
    <div class="metric-value">0.368</div>
    <div class="metric-delta">Δ +0.171 vs 0.197</div>
    <div class="metric-ci">CI [+0.163, +0.178]</div>
  </div>
  <div class="metric">
    <div class="metric-label">ROUGE-L</div>
    <div class="metric-value">0.368</div>
    <div class="metric-delta">Δ +0.174 vs 0.193</div>
    <div class="metric-ci">CI [+0.166, +0.181]</div>
  </div>
  <div class="metric">
    <div class="metric-label">BLEU</div>
    <div class="metric-value">+0.221</div>
    <div class="metric-delta">Δ vs BM25</div>
    <div class="metric-ci">CI strictly &gt; 0</div>
  </div>
  <div class="metric">
    <div class="metric-label">Exact Match</div>
    <div class="metric-value">+0.047</div>
    <div class="metric-delta">Δ vs BM25</div>
    <div class="metric-ci">CI strictly &gt; 0</div>
  </div>
</div>

Retrieval-only, BM25 on the full 8.8 M-passage corpus (6 980 queries):

<div class="metric-grid">
  <div class="metric">
    <div class="metric-label">MRR@10</div>
    <div class="metric-value">0.170</div>
    <div class="metric-delta">BM25, full corpus</div>
  </div>
  <div class="metric">
    <div class="metric-label">Recall@100</div>
    <div class="metric-value">0.621</div>
    <div class="metric-delta">BM25, full corpus</div>
  </div>
  <div class="metric">
    <div class="metric-label">Recall@1000</div>
    <div class="metric-value">0.815</div>
    <div class="metric-delta">BM25, full corpus</div>
  </div>
</div>

## Evidence status

<dl class="kv">
  <dt>Validated result</dt><dd>On MS MARCO <code>dev/small</code>, reranked dense top-3 improves T5-small surface metrics over BM25 top-3 on 6 980 paired queries. The dense and reranking stages use a documented 50 000-passage qrels-anchored pool, not a full-corpus dense first stage.</dd>
  <dt>Validated external retrieval</dt><dd>On all 43 TREC-DL 2019 and 54 TREC-DL 2020 judged topics, cross-encoder reranking improves MRR@10 and graded nDCG@10 over full-corpus BM25. The protocol and checked artifact are in the repository's <a href="https://github.com/GioiaZheng/msmarco-genqa/blob/main/docs/trec_dl_external_validity.md">TREC-DL report</a>.</dd>
  <dt>Implemented, pending evaluation</dt><dd>The T5-base generator-capacity sweep and configurable alternative-generator paths exist, but no T5-base or FLAN-T5 headline result is claimed without a complete versioned run.</dd>
  <dt>Not established</dt><dd>The current artifacts do not show that TREC-DL retrieval gains transfer to generation, that dense retrieval beats BM25 under a fair full-corpus condition, or that the findings generalize beyond MS MARCO passages.</dd>
</dl>

## Technical components

<dl class="kv">
  <dt>Sparse retrieval</dt><dd>BM25, k₁ = 1.5, b = 0.75, top-k = 1000</dd>
  <dt>Dense retrieval</dt><dd><code>sentence-transformers/all-MiniLM-L6-v2</code> + FAISS flat IP, qrels-anchored 50 000-passage sample</dd>
  <dt>Reranking</dt><dd><code>cross-encoder/ms-marco-MiniLM-L-6-v2</code> over dense top-100</dd>
  <dt>Generation</dt><dd><code>t5-small</code>, frozen, max_new_tokens = 64</dd>
  <dt>Retrieval metrics</dt><dd>MRR@k, Recall@k, nDCG@k</dd>
  <dt>Generation metrics</dt><dd>Token-F1, Exact-Match, ROUGE-L, BLEU (best-of-N references)</dd>
  <dt>Grounding</dt><dd>Lexical content-token, 3-gram, NLI entailment via <code>cross-encoder/nli-deberta-v3-small</code></dd>
  <dt>Statistical core</dt><dd>Paired bootstrap, N = 10 000 resamples, seed 42</dd>
  <dt>Manifest contract</dt><dd>Required at write time: <code>git.commit</code>, <code>git.dirty</code>, <code>extra.seed</code>, <code>extra.resolved_config_hash</code>, <code>extra.data_fingerprint</code>, <code>extra.env_fingerprint</code></dd>
  <dt>CI</dt><dd>GitHub Actions, Python 3.10, CPU-only torch &mdash; <code>pytest -q</code> + <code>ruff check</code> on every push</dd>
</dl>

## Reproduce

Clean clone, CPU-only laptop:

```sh
make install
make reproduce-baseline
```

`make reproduce-baseline` runs the BM25 stage under a clean-tree checkpoint and then validates the produced manifest against committed fingerprints via `scripts/verify_reproduction.py`.

<aside class="callout">
  <div class="callout-label">Limitations</div>
  <ul>
    <li>Dense + reranker numbers come from a 50 000-passage <strong>qrels-anchored sample</strong>, not the full corpus. The sample is anchored on relevant documents, which inflates recall-based metrics. Every <code>metrics.json</code> carries a <code>(sampled)</code> caveat block to prevent the numbers being read as deep-judgment results.</li>
    <li>CPU-only, single-machine by design &mdash; the target is laptop reproducibility, not GPU throughput.</li>
    <li>TREC-DL 2019 / 2020 now provides deep-judgment evidence for full-corpus BM25 plus cross-encoder retrieval only. It is not generation evidence and does not include a full-corpus dense first stage.</li>
  </ul>
</aside>

## Current status

Active. The paired MS MARCO generation comparison and the TREC-DL 2019/2020 BM25-plus-reranker benchmark are completed, versioned evidence. The T5-base capacity study and broader generator comparisons remain implemented or planned work; they are not reported as empirical findings until their artifacts land.

## Repo

[github.com/GioiaZheng/msmarco-genqa](https://github.com/GioiaZheng/msmarco-genqa)
