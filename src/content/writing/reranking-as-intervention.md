---
title: "Reranking as a controlled intervention in RAG pipelines"
summary: Treating the reranker as a knob — not a black box — lets you measure what it does to the generator downstream.
status: planned
order: 2
---

Planned.

A short methodological note: rerankers are usually evaluated on retrieval-level metrics (nDCG, MRR) in isolation. When you instead hold the retrieval set and the generator fixed and toggle only the reranker, you can observe its causal effect on downstream grounding — and that effect is not always positive.

TODO: write.
