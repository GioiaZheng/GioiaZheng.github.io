---
title: msmarco-genqa
summary: Reproducible retrieve → rerank → generate pipeline on MS MARCO with paired-bootstrap evaluation and a manifest-enforced reproducibility contract.
order: 1
featured: true
status: active
last_updated: "2026-05-28"
repo: https://github.com/GioiaZheng/msmarco-genqa
tags: ["retrieval", "rag", "evaluation", "reproducibility"]
---

Independent open-source research project on small-scale, CPU-tractable retrieval-augmented generation. Single staged pipeline — sparse retrieval, dense retrieval, cross-encoder reranking, grounded generation, evaluation — with a strict reproducibility contract on every experimental run.

## Problem

Surface generation metrics (Token-F1, ROUGE-L) on retrieve → rerank → generate pipelines do not, by themselves, tell you whether the generator's output is actually supported by the retrieved evidence. Reranking the retrieval stage can simultaneously raise surface metrics and reduce grounding on the same fixed generator. Quantifying this requires a pipeline where every component is exchangeable, every run is reproducible to a bit-level manifest, and statistical comparisons are paired and confidence-bounded.

## What I built

Four entry-point scripts under [`experiments/`](https://github.com/GioiaZheng/msmarco-genqa/tree/main/experiments) — one per pipeline stage — sharing a single source-of-truth config and writing a schema-versioned `manifest.json` next to every `metrics.json`. The contract is enforced at write time: a run that fails to capture the six required reproducibility fields cannot land an artifact.

## Technical components

<dl class="kv">
  <dt>Sparse retrieval</dt><dd>BM25 over MS MARCO passage (8.8 M docs), k₁ = 1.5, b = 0.75, top-k = 1000</dd>
  <dt>Dense retrieval</dt><dd>sentence-transformers/all-MiniLM-L6-v2 + FAISS flat IP, qrels-anchored 50 000-passage sample</dd>
  <dt>Reranking</dt><dd>cross-encoder/ms-marco-MiniLM-L-6-v2 over dense top-100</dd>
  <dt>Generation</dt><dd>t5-small, frozen, max_new_tokens = 64</dd>
  <dt>Retrieval metrics</dt><dd>MRR@k, Recall@k, nDCG@k</dd>
  <dt>Generation metrics</dt><dd>Token-F1, Exact-Match, ROUGE-L, BLEU (best-of-N references)</dd>
  <dt>Grounding</dt><dd>Lexical content-token, 3-gram, NLI entailment via cross-encoder/nli-deberta-v3-small</dd>
  <dt>Statistical core</dt><dd>Paired bootstrap, N = 10 000 resamples, seed 42</dd>
  <dt>Reproducibility manifest</dt><dd>Required fields enforced at write time: <code>git.commit</code>, <code>git.dirty</code>, <code>extra.seed</code>, <code>extra.resolved_config_hash</code>, <code>extra.data_fingerprint</code>, <code>extra.env_fingerprint</code></dd>
  <dt>CI</dt><dd>GitHub Actions, Python 3.10, CPU-only torch: <code>pytest -q</code> + <code>ruff check</code> on every push</dd>
</dl>

## Evidence / outputs

Headline result on the full MS MARCO dev/small (6 980 queries, paired):

<dl class="kv">
  <dt>Token-F1</dt><dd>BM25 → Reranked&nbsp; <strong>0.197 → 0.368</strong>, Δ +0.171 (95 % CI [+0.163, +0.178])</dd>
  <dt>ROUGE-L</dt><dd>0.193 → 0.368, Δ +0.174 (95 % CI [+0.166, +0.181])</dd>
  <dt>BLEU</dt><dd>Δ +0.2206 (CI strictly &gt; 0)</dd>
  <dt>Exact-Match</dt><dd>Δ +0.0471 (CI strictly &gt; 0)</dd>
</dl>

Retrieval-only, BM25 over the full 8.8 M-passage corpus: MRR@10 = 0.1703, Recall@100 = 0.6212, Recall@1000 = 0.8154 (6 980 queries).

Test suite: 173 functions under [`tests/`](https://github.com/GioiaZheng/msmarco-genqa/tree/main/tests). CI passes pytest + ruff on every push.

Reproduce from clean clone (CPU-only laptop):

```sh
make install
make reproduce-baseline
```

`make reproduce-baseline` runs the BM25 stage in a clean-tree checkpoint and then `python scripts/verify_reproduction.py outputs/week02_bm25` against the committed manifest fingerprints.

## Current status

Active. Schema-v2 manifest contract closed in [v2.0-reproducibility-protocol](https://github.com/GioiaZheng/msmarco-genqa/releases). Next round (`research/metric-robustness`) extends the contract with NLI-specific fields and runs the full factorial — multiple NLI backbones × score formulas × thresholds × seeds — with paired bootstrap confidence intervals and a length covariate. A failure taxonomy is being built as a versioned data product.

## Limitations

- Dense + reranker numbers are computed on a **50 000-passage qrels-anchored sample**, not the full 8.8 M corpus. The sample is anchored on relevant documents, which inflates recall-based metrics. The repo flags this as a `(sampled)` caveat block on every `metrics.json` to prevent the numbers from being read as deep-judgment results.
- CPU-only single-machine constraint by design (the project targets the laptop-reproducibility budget, not GPU throughput).
- Deep-judgment external validity (TREC-DL 2019 / 2020) is the next experimental milestone, not a completed claim.

## Repo

[github.com/GioiaZheng/msmarco-genqa](https://github.com/GioiaZheng/msmarco-genqa)
