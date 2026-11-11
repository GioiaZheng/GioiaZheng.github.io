---
title: "Why Better Retrieval Does Not Always Improve Grounding"
summary: "Better ranked evidence is useful, but it is not the same as a faithful answer. I treat retrieval quality and grounding as separate axes."
date: "2026-06-23"
status: published
order: 1
---

This is a short note from building [msmarco-genqa](/projects/msmarco-genqa/): retrieval quality and grounding should not be collapsed into one claim.

In a retrieve -> rerank -> generate pipeline, the retrieval stack shapes what the generator can see. Context grounding asks a different question: whether the answer is supported by what the generator saw. Neither question, on its own, establishes that the answer is correct.

Those two layers often move together, but not always.

## The observation

On the evaluated MS MARCO <code>dev/small</code> comparison, the reranked-dense arm reaches higher Token-F1 than the BM25-conditioned arm. The generator, prompt, top-k, and paired queries are fixed, but the retrieval boundaries differ: BM25 searches the full corpus, whereas the reranked-dense arm uses a 50,000-passage pool seeded with judged-relevant passages. The comparison therefore does not isolate the reranker's causal effect.

That is a useful result. It is not, by itself, a faithfulness result.

Ranking and context construction can also promote answer-missing passages. If the generator follows one, the output may be supported by that supplied passage while still being irrelevant to the question or factually wrong. Context support, passage relevance, and answer correctness must therefore be checked separately.

## What I check

For each comparison, I want to separate four questions:

1. Did judged-relevant evidence enter the candidate set?
2. What relevant and answer-missing passages were placed in the shown context?
3. Did the output answer the question correctly or agree with the reference?
4. Was the output supported by the shown context under a named, calibrated scorer?

These are related observations, not mutually exclusive causal labels. Token-F1, ROUGE-L, BLEU, and exact match remain useful reference-agreement measures, while NLI adds one context-support signal. None of them alone identifies which pipeline stage caused a change.

## Why this matters

If Token-F1 and an NLI grounding score both rise, the output has stronger reference agreement and stronger estimated context support under those scorers. Passage relevance and answer correctness still need to be checked.

If Token-F1 rises while the grounding score falls, the signals disagree. That is an audit trigger, not evidence of a specific failure mechanism: the next step is case review, per-passage support analysis, and a check of evaluator sensitivity.

The practical rule I use is simple: answer-bearing evidence must be available for context-grounded answering, but a higher aggregate retrieval score does not guarantee a better answer. Retrieval, answer quality, context relevance, and context support should remain separate reporting axes. The longer [failure-analysis note](/writing/rag-failure-analysis/) records the definitions and limitations used here.
