---
title: "Why Better Retrieval Does Not Always Improve Grounding"
summary: "Better ranked evidence is useful, but it is not the same as a faithful answer. I treat retrieval quality and grounding as separate axes."
date: "2026-06-23"
status: published
order: 1
---

This is a short note from building [msmarco-genqa](/projects/msmarco-genqa/): retrieval quality and grounding should not be collapsed into one claim.

In a retrieve -> rerank -> generate pipeline, the retrieval stack decides what the generator can see. Grounding asks a different question: whether the answer is actually supported by what the generator saw.

Those two layers often move together, but not always.

## The observation

Reranking can improve surface QA metrics because the shown passages become more query-shaped. On the MS MARCO dev/small run, the reranked generation setting improves Token-F1 over the BM25-conditioned setting.

That is a useful result. It is not, by itself, a faithfulness result.

A reranker can also promote hard distractors: passages that are close to the query but wrong for the answer. If the generator follows that distractor, the output may sound specific and even share vocabulary with the reference while not being supported by the right evidence.

## What I check

For each intervention, I want to separate three questions:

1. Did relevant evidence enter the candidate set?
2. Did the ranking stage place it above plausible distractors?
3. Did the generator answer from the shown evidence?

The first two are retrieval and ranking questions. The third is a grounding question. Token-F1, ROUGE-L, BLEU, and exact match are still useful, but I do not want them to be the only view of the system.

## Why this matters

If Token-F1 rises and grounding rises, the intervention is probably helping the pipeline.

If Token-F1 rises and grounding falls, the system may only be getting better at producing answers that look right. That is a different result, and it needs a different next step.

The practical rule I use is simple: better retrieval is a necessary condition for good grounded generation, not a guarantee. Every retrieval improvement still needs a second-axis grounding check.
