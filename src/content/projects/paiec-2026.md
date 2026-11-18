---
title: "PAIEC 2026: Fixed Shrinkage"
summary: "Accepted technical report on predicting model correctness with few observed labels."
order: 4
featured: false
academic: true
status: maintained
last_updated: "2026-11-18"
repo: https://github.com/GioiaZheng/paiec-2026
tags: ["model-evaluation", "uncertainty", "reproducibility"]
---

## Accepted technical report

Gioia Zheng. [*Fixed Shrinkage for Predictive AI Evaluation with Few Observed Labels*](https://openreview.net/forum?id=unVHJGkE8n). **Accepted at PAIEC 2026**, November 2026.

The submitted method uses fixed Beta(1,1) shrinkage, `(successes + 1) / (labels + 2)`, with random label acquisition. Local experiments examine small-budget gains and low-success bias. Weaker shrinkage, transferred priors and lexical weighting did not meet the criteria for replacing it.

## Reproducible evidence

- [Source, accepted-report details and reproduction commands](https://github.com/GioiaZheng/paiec-2026)
- [Results and limitations](https://github.com/GioiaZheng/paiec-2026/blob/main/RESULTS.md)
- [Evaluation protocol](https://github.com/GioiaZheng/paiec-2026/blob/main/docs/evaluation_protocol.md)
- [OpenReview report](https://openreview.net/forum?id=unVHJGkE8n)

Report acceptance is distinct from a competition award or ranking. No award or presentation-selection claim is made here.
