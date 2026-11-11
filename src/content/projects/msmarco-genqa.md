---
title: msmarco-genqa
summary: Reproducible retrieve → rerank → generate pipeline on MS MARCO with paired-bootstrap evaluation and a manifest-enforced reproducibility contract.
order: 1
featured: true
academic: true
status: maintained
last_updated: "2026-10-17"
repo: https://github.com/GioiaZheng/msmarco-genqa
tags: ["retrieval", "rag", "evaluation", "reproducibility"]
---

<dl class="summary-grid">
  <dt>Comparison</dt>
  <dd>Full-corpus BM25 top-3 versus cross-encoder-reranked dense top-3 from a 50 000-passage pool seeded with the queries' judged-relevant passages (qrels-anchored); T5-small and all 6 980 <code>dev/small</code> queries are fixed</dd>
  <dt>Dataset</dt>
  <dd>MS MARCO passage: 8.8 M passages in the BM25 arm; a qrels-anchored 50 000-passage pool in the reranked-dense arm</dd>
  <dt>Main result</dt>
  <dd>Under these different first-stage conditions, Token-F1 is 0.197 versus 0.368 (Δ&nbsp;+0.171, 95 % CI [+0.163, +0.179], paired bootstrap). This does not isolate the reranker's causal effect.</dd>
  <dt>External retrieval</dt>
  <dd>TREC-DL 2019/2020 full-corpus BM25 + cross-encoder benchmark, independently cross-checked</dd>
  <dt>Reproducibility</dt>
  <dd>Schema-v2 manifest contract; <code>make reproduce-baseline</code> from clean clone</dd>
  <dt>Status</dt>
  <dd>Maintained &mdash; research baseline frozen through thesis completion and graduation; security and reproducibility maintenance only</dd>
</dl>

## Problem

Surface generation metrics (Token-F1, ROUGE-L) on retrieve → rerank → generate pipelines do not, by themselves, tell you whether the generator's output is actually supported by the retrieved evidence. In the evaluated paired comparison, surface metrics improve under the reranked-dense arm while the grounding checks disagree: lexical and 3-gram overlap remain near ceiling, but the sentence-level NLI proxy falls. This divergence is an evaluator-sensitivity finding, not proof that grounding itself worsened. Studying it requires exchangeable components, paired confidence-bounded comparisons, and explicit provenance: new runs are checked against a versioned manifest contract, while legacy canonical runs carry separate provenance backfills with unrecoverable fields marked <code>unknown</code>.

## What I built

Four entry-point scripts under [`experiments/`](https://github.com/GioiaZheng/msmarco-genqa/tree/main/experiments) — one per pipeline stage — sharing a single source-of-truth config and writing a schema-versioned `manifest.json` next to every `metrics.json`. The contract is enforced at write time: a run that fails to capture the six required reproducibility fields cannot land an artifact.

## Evidence map

<dl class="summary-grid">
  <dt>Research question</dt>
  <dd>When do retrieval and reranking improvements transfer into better generated answers, and when are they bounded by missing first-stage candidates?</dd>
  <dt>Key result</dt>
  <dd>On MS MARCO <code>dev/small</code>, the reranked-dense arm (50 000-passage qrels-anchored pool) reaches T5-small Token-F1 0.3677 versus 0.1966 for the full-corpus BM25 arm across 6 980 paired queries (Δ +0.1711, 95% CI [+0.1632, +0.1789]). This is not a like-for-like full-corpus retrieval comparison. On BEIR NFCorpus and SciFact, cross-encoder reranking improves early ranking while Recall@100 stays fixed because the reranker only sees the BM25 top-100 candidate set.</dd>
  <dt>What I did</dt>
  <dd>Built retrieval, reranking, generation, paired-bootstrap evaluation, external retrieval benchmarks, first-stage failure analysis, and versioned reproducibility artifacts.</dd>
  <dt>Evidence</dt>
  <dd><a href="https://github.com/GioiaZheng/msmarco-genqa">GitHub repo</a> · <a href="https://github.com/GioiaZheng/msmarco-genqa/blob/main/RESULTS.md">MS MARCO results</a> · <a href="https://github.com/GioiaZheng/msmarco-genqa/blob/main/docs/cross_dataset_error_analysis.md">NFCorpus/SciFact error analysis</a> · <a href="https://huggingface.co/datasets/GioiaZheng/msmarco-genqa-benchmark-runs">Hugging Face benchmark runs</a></dd>
</dl>

## Headline result

All 6 980 MS MARCO <code>dev/small</code> queries; fixed T5-small generator; full-corpus BM25 top-3 versus reranked dense top-3 from the 50 000-passage qrels-anchored pool; paired bootstrap (N = 10 000). The comparison changes the first-stage retrieval condition as well as the use of reranking.

<div class="metric-grid">
  <div class="metric">
    <div class="metric-label">Token-F1</div>
    <div class="metric-value">+0.171</div>
    <div class="metric-delta">paired per-query Δ</div>
    <div class="metric-ci">CI [+0.163, +0.179]</div>
  </div>
  <div class="metric">
    <div class="metric-label">ROUGE-L</div>
    <div class="metric-value">+0.174</div>
    <div class="metric-delta">paired per-query Δ</div>
    <div class="metric-ci">CI [+0.166, +0.182]</div>
  </div>
  <div class="metric">
    <div class="metric-label">Sentence BLEU</div>
    <div class="metric-value">+0.133</div>
    <div class="metric-delta">paired per-query Δ</div>
    <div class="metric-ci">CI [+0.127, +0.140]</div>
  </div>
  <div class="metric">
    <div class="metric-label">Exact Match</div>
    <div class="metric-value">+0.047</div>
    <div class="metric-delta">paired per-query Δ</div>
    <div class="metric-ci">CI [+0.042, +0.053]</div>
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
  <dt>Validated result</dt><dd>On MS MARCO <code>dev/small</code>, the evaluated reranked-dense arm yields higher T5-small surface metrics than the full-corpus BM25 arm on 6 980 paired queries. The dense and reranking stages use a documented 50 000-passage qrels-anchored pool, not a full-corpus dense first stage, so the result does not isolate reranking.</dd>
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

Maintained. The paired MS MARCO generation comparison and the TREC-DL 2019/2020 BM25-plus-reranker benchmark are completed, versioned evidence. The research baseline is frozen through thesis completion and graduation; security and reproducibility maintenance may continue, but no new experimental result is claimed until a complete versioned artifact exists.

## Repo

[github.com/GioiaZheng/msmarco-genqa](https://github.com/GioiaZheng/msmarco-genqa)
