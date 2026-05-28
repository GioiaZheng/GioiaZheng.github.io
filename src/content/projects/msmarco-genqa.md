---
title: msmarco-genqa
summary: Reproducible retrieve → rerank → generate pipeline over MS MARCO, with grounding-aware evaluation.
order: 1
featured: true
status: active
repo: https://github.com/GioiaZheng/msmarco-genqa
tags: ["retrieval", "rag", "evaluation", "reproducibility"]
---

Independent open-source research project on small-scale, CPU-tractable retrieval-augmented generation. The codebase is structured around a single staged pipeline — sparse retrieval, dense retrieval, cross-encoder reranking, grounded generation, evaluation — with a strict reproducibility contract on every experimental run.

## Problem

Surface generation metrics (Token-F1, ROUGE-L) on retrieve → rerank → generate pipelines do not, by themselves, tell you whether the generator's output is actually supported by the retrieved evidence. Reranking the retrieval stage can simultaneously raise surface metrics and reduce grounding on the same fixed generator. Quantifying this requires a pipeline where every component is exchangeable, every run is reproducible to bit-level manifests, and statistical comparisons are paired and confidence-bounded.

## What I built

A staged, exchangeable pipeline over MS MARCO passage with four entry points (`experiments/run_*.py` for BM25 / dense / reranker / generation), a single source-of-truth YAML config, and a schema-versioned manifest written next to every `metrics.json`. The contract is enforced at write time, not as an afterthought: a run that fails to capture the six required reproducibility fields cannot land an artifact.

## Technical components

<dl class="kv">
  <dt>Sparse retrieval</dt><dd>Pyserini BM25 over MS MARCO passage</dd>
  <dt>Dense retrieval</dt><dd>Sentence-Transformers encoder + FAISS flat IP index</dd>
  <dt>Reranking</dt><dd>Cross-encoder reranker on top-k candidates</dd>
  <dt>Generation</dt><dd>Seq2seq generator (T5 family) with fixed decoding</dd>
  <dt>Evaluation</dt><dd>Token-F1, ROUGE-L, BERTScore; NLI-based grounding score</dd>
  <dt>Statistical core</dt><dd>Paired bootstrap (N = 10 000) with stratified resampling</dd>
  <dt>Reproducibility</dt><dd>Schema-v2 manifest: resolved config + hash, data fingerprint, env fingerprint, sampled-eval caveat, pinned model revisions</dd>
  <dt>CI</dt><dd>GitHub Actions: pytest + ruff on every push</dd>
</dl>

## Evidence / outputs

- Frozen v1.0 baseline report PDF, tagged as the initial release; subsequent rounds preserve the v1.0 numbers as the immutable reference point.
- Schema-v2 reproducibility contract: `make reproduce-baseline` plus `scripts/verify_reproduction.py` is the canonical reproduce-then-verify entry point.
- Three `provenance.backfill.json` files (BM25, dense, reranker stages) anchor downstream artifacts to the v1.0 commit.
- 349 tests passing, ruff clean on `main`.

## Current status

Active. Next experimental round (`research/metric-robustness`) extends the manifest contract with NLI-specific fields and runs the full factorial — multiple NLI backbones × score formulas × thresholds × seeds — with paired bootstrap confidence intervals and a length covariate. Failure taxonomy is being built as a versioned data product.

## Limitations

CPU-only single-machine constraint by design (the project targets the laptop-reproducibility budget, not GPU throughput). Evaluation has so far been anchored to a 50 000-passage MS MARCO sample plus a sampled query set; deep-judgment external validity (TREC-DL 2019 / 2020) is the next experimental milestone, not a completed claim.

## Repo

<a href="https://github.com/GioiaZheng/msmarco-genqa">github.com/GioiaZheng/msmarco-genqa</a>
