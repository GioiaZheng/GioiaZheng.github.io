---
title: "Failure analysis in retrieval-augmented generation"
summary: A single aggregate score is the wrong unit for evaluating a RAG pipeline. Reporting per-category failure rates makes regressions visible that aggregates hide.
date: "2026-05-28"
status: published
order: 1
---

A retrieve &rarr; rerank &rarr; generate pipeline can fail at four roughly disjoint points. Most evaluations roll them up into one score. That makes pipeline-level regressions almost invisible: an improvement at one stage that worsens another can wash out completely in the average, or &mdash; worse &mdash; appear as a net win while the actual error mix shifts in a damaging direction.

This note argues for treating failure analysis as a first-class output of evaluation, not as a follow-up exercise. It is methodological &mdash; not a results write-up &mdash; and is shaped by the design choices that went into building [msmarco-genqa](/projects/msmarco-genqa/).

## Four failure modes, named

For a system that takes a query, retrieves passages, reranks them, and generates an answer, the failure space partitions reasonably well into:

1. **Retrieval gap.** No relevant passage appears in the candidate pool. The reranker has nothing to promote; the generator is asked to answer from negative evidence. The right action is at the retrieval stage &mdash; expand the candidate pool, swap the encoder &mdash; not at the generator.

2. **Rank inversion.** A relevant passage is in the candidate pool but the reranker promotes a confidently-wrong distractor above it. This is the failure mode Cuconasu et al. (SIGIR 2024) characterise as the "hard distractor" pattern: lexically or semantically similar to the query but factually unrelated, and exactly the kind of passage a stronger reranker selects.

3. **Evidence under-use.** The relevant passage is in the top-k handed to the generator, but the generator outputs something either generic ("I cannot answer") or grounded in its parametric prior rather than the supplied passage. The retrieval and ranking did their job; the generation step did not condition.

4. **Fabrication.** The output is fluent, plausibly relevant, and not supported by anything in the retrieved passages. From outside the pipeline this looks identical to a correct answer except on a faithfulness check.

Categories (1) and (2) are owned by the retrieval / ranking stack; (3) and (4) are owned by the generator and by the grounding metric. Conflating them under one number means a regression in (4) can be hidden by an improvement in (1), and the pipeline is silently shifting in the wrong direction.

## Why aggregates hide the shift

Token-F1, ROUGE-L, BLEU and BERTScore all reward token-level overlap with the reference. A fabrication that happens to use the same vocabulary as the reference scores well. An honest "I cannot answer" scores zero even when (1) is the correct diagnosis and the system should not have been required to answer at all.

A concrete pattern from msmarco-genqa: turning on a cross-encoder reranker between dense retrieval and the generator raises Token-F1 on the dev/small split (BM25 0.197 &rarr; reranked 0.368, &Delta; +0.171 with 95% CI [+0.163, +0.178], paired bootstrap, N = 6 980). The aggregate says "reranking helps." The aggregate does not say whether the &Delta; comes from fixing category (1) errors (genuine improvement) or from category (4) shifts (the reranker promoted hard distractors that share vocabulary with the reference, so the fabricated answer scored higher).

This is the precise gap an NLI-based grounding score is built to detect: it asks, per output, whether the produced text is entailed by the retrieved passage, independent of how much vocabulary it shares with the reference. If the &Delta; in Token-F1 is genuine, grounding rises with it. If the &Delta; comes from hard distractors, grounding falls while Token-F1 climbs.

## What "per-category" looks like in practice

The unit of evaluation becomes a triple per query:

- a retrieval-stage label &mdash; did the relevant passage reach the top-k handed to the generator? (binary)
- a ranking-stage label &mdash; if it reached top-k, was it ranked at or above the highest-scored irrelevant passage? (binary, conditional)
- a generation-stage label &mdash; given the top-k actually shown to the generator, is the output entailed by any of them? (NLI-based, ternary: entailed / neutral / contradicted)

The output of evaluation is then a 2 &times; 2 &times; 3 = 12-cell contingency. Most cells will be empty or rare. The two cells that matter for pipeline regressions are:

- _"reached top-k, properly ranked, NOT entailed"_ &mdash; the generator failed to condition. Increasing this rate is a regression even if the aggregate score improves.
- _"reached top-k, hard distractor ranked above, entailed by distractor"_ &mdash; the reranker actively misled the generator. This is the cell that Cuconasu-style mechanism analysis lives in, and it is invisible if you only look at aggregates.

Reporting these per-category rates alongside the aggregate, with paired bootstrap confidence intervals on the difference between system A and system B for each cell, lets a reader see exactly _which_ failure mode is moving when an intervention is applied. The aggregate alone cannot.

## Two design implications

**Grounding is not a tiebreaker; it is the second axis.** A surface metric and a grounding metric measure different things; reporting only their sum (or worse, only the surface metric) collapses a 2D quantity to 1D, and the collapsed coordinate is exactly where the interesting regressions hide. The right unit is the pair `(surface, grounding)`, reported with paired CIs.

**Failure categories deserve to be a versioned data product.** Once you commit to per-category reporting, the category definitions and the labeller (NLI model, threshold, score formula) become load-bearing for cross-experiment comparison. Pinning them &mdash; in a manifest, alongside the model revisions &mdash; is what turns "this run had 12% category-4 errors" into a comparable claim across experiments.

## What this note is not

This is a methodological argument, not a results paper. The concrete msmarco-genqa numbers above are a single intervention on one dataset with one generator; whether the surface-up / grounding-down direction reverses on T5-base, on a different NLI backbone, or under a different decision threshold is exactly what the next experimental round is set up to test. The point here is narrower: when you set up that test, the unit of evaluation should be per-category &mdash; not a single number with a confidence interval glued on.

---

_Status: draft. References will be added when the next experimental round closes; the Cuconasu et al. (SIGIR 2024) and the SummaC / MENLI line on NLI-as-faithfulness are the obvious anchors._
