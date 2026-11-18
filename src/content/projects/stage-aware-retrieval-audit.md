---
title: Stage-Aware Retrieval Audit
summary: "Versioned audit of candidate availability in two-stage retrieval using frozen ranked runs and independent metric checks."
order: 5
featured: false
academic: true
status: maintained
last_updated: "2026-11-18"
repo: https://github.com/GioiaZheng/stage-aware-retrieval-audit-release
tags: ["retrieval", "evaluation", "reproducibility"]
---

## Released resource

The [v0.2.2 release](https://github.com/GioiaZheng/stage-aware-retrieval-audit-release/releases/tag/v0.2.2) checks where the first judged-relevant document appears in frozen BM25 runs, and whether it is available to a reranker restricted to the top 100 candidates.

The evidence covers BEIR NFCorpus and SciFact test sets and judged TREC Deep Learning 2019/2020 topics. Separate code-path-independent recomputation scripts and SHA-256 checks make the results inspectable.

## Evidence and scope

- [Source, release documentation and quick start](https://github.com/GioiaZheng/stage-aware-retrieval-audit-release)
- [Release v0.2.2](https://github.com/GioiaZheng/stage-aware-retrieval-audit-release/releases/tag/v0.2.2)
- [Provenance](https://github.com/GioiaZheng/stage-aware-retrieval-audit-release/blob/main/docs/PROVENANCE.md)

These are operational candidate-set outcomes, not semantic explanations of query difficulty or causal explanations of generated-answer failures. Publication of the resource does not establish acceptance of an associated paper.
