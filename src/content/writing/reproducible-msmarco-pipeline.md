---
title: "Building a Reproducible MS MARCO Pipeline"
summary: "How I keep retrieval runs inspectable: separate stages, resolved configs, manifests, fingerprints, and explicit sampling caveats."
date: "2026-06-23"
status: published
order: 3
---

The main engineering goal of [msmarco-genqa](/projects/msmarco-genqa/) is not only to run a retrieval experiment. It is to make the result explainable after the run finishes.

For me, a useful experiment artifact should answer four questions:

1. What code produced this number?
2. What configuration was actually used?
3. What data and environment did the run depend on?
4. Which numbers are full-corpus results, and which ones are sampled?

## Pipeline shape

The system is split into four stages:

- BM25 retrieval over the MS MARCO passage corpus;
- dense retrieval on a controlled sub-corpus;
- cross-encoder reranking over retrieved candidates;
- generation and evaluation from the selected passages.

Keeping those stages separate makes the pipeline a little less convenient, but much easier to debug. When a metric moves, I can inspect the stage that changed instead of treating the whole run as one opaque script.

## Run artifacts

Each run writes the metrics next to a manifest and a resolved config.

The manifest records the git commit, dirty-tree flag, command, dependency files, output digests, Python/runtime details, seed, data fingerprint, environment fingerprint, and resolved-config hash.

The resolved config matters because the config file alone is not enough. A run can use the same `configs/baseline.yaml` file and still differ through CLI overrides. I want the final configuration object, after overrides, to be visible and hashable.

## Sampling caveats

The full BM25 baseline runs over the 8.8M-passage corpus. Some dense and reranking experiments use a qrels-anchored 50,000-passage sample so that iteration stays laptop-friendly.

Those sampled numbers are useful for development. They are not full-corpus claims.

That caveat is written into `metrics.json` rather than left as a memory or a README note. If a number is sampled, the artifact should say so where the number lives.

## What I keep

The reproducibility layer is intentionally small:

- one command for the baseline;
- one resolved config per run;
- one manifest per run;
- stable seeds and fingerprints;
- output hashes checked by a verifier.

That is enough to turn a metric file from "a number I got once" into a run I can inspect, compare, and reproduce.
