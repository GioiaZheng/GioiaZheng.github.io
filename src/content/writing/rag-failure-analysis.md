---
title: "Failure Taxonomy for RAG Systems"
summary: "When a RAG score changes, I want to know which observable moved: evidence availability, context composition, answer quality, context support, or the metric itself."
date: "2026-05-28"
status: published
order: 2
---

A retrieve &rarr; rerank &rarr; generate pipeline can fail in several interacting ways. Aggregate scores can hide whether a change affects evidence coverage, ranking and context composition, answer quality, or support from the retrieved context. An improvement in one observable can wash out a regression in another, or appear as a net win while the error mix shifts.

This note argues for treating failure analysis as a first-class output of evaluation, not as a follow-up exercise. It is methodological &mdash; not a results write-up &mdash; and is shaped by the design choices that went into building [msmarco-genqa](/projects/msmarco-genqa/).

## Four review patterns

For a system that takes a query, retrieves passages, reranks them, and generates an answer, four useful review patterns are:

1. **Retrieval gap.** No judged-relevant passage appears in the candidate pool. The reranker therefore has no labelled positive to promote. This identifies a first-stage coverage problem, but it does not by itself explain how the generator will behave.

2. **Rank or context-composition failure.** A judged-relevant passage is available, but an answer-missing passage is ranked above it or consumes the context budget. Cuconasu et al. study highly scored, query-related passages that do not contain the answer and report that they can reduce answer accuracy under their experimental setup. Their result motivates this audit; it does not establish that every reranker-related regression has this cause.

3. **Evidence under-use.** Answer-bearing evidence is present in the supplied context, but the output omits it, gives an incomplete answer, or abstains. Unsupported content may come from parametric memory or another source, but its provenance cannot be inferred from the output alone.

4. **Unsupported generation.** The output contains a claim that is not supported by the retrieved context. Such a claim may still agree with the reference &mdash; or even be factually correct &mdash; so context faithfulness must be assessed separately from answer correctness.

These patterns are diagnostic labels, not mutually exclusive ownership assignments. A single query can exhibit more than one of them, and the cause may lie in retrieval, ranking, context construction, prompting, generation, annotation, or the evaluator itself. Causal attribution therefore requires controlled comparisons or case-level review.

## Why aggregates hide the shift

Token-F1, ROUGE-L, and BLEU are lexical reference-agreement metrics: they use token overlap, longest common subsequences, and n-gram overlap, respectively. BERTScore is different: it matches contextual token embeddings and can credit semantically similar wording without exact lexical overlap. All four compare an output with a reference; none by itself establishes that the output is supported by the retrieved context. An unsupported answer can therefore score well when it resembles the reference, while a faithful paraphrase or abstention may be penalised &mdash; most sharply by the lexical metrics.

In msmarco-genqa, the evaluated reranked-dense arm reaches higher Token-F1 than the BM25 arm on 6,980 paired <code>dev/small</code> queries (0.1966 &rarr; 0.3677, &Delta; +0.1711 with 95% CI [+0.1632, +0.1789]). The generator, prompt, top-k, and queries are fixed, but the retrieval boundaries are not: BM25 searches the full corpus, whereas the dense + reranker arm uses a 50,000-passage pool seeded with the queries' judged-relevant passages (qrels-anchored). The result establishes higher reference agreement under those two evaluated configurations; it does not isolate the reranker's causal effect or explain the mechanism.

An NLI-based score adds one context-support signal by estimating whether the retrieved context entails the generated output. Unlike exact lexical metrics, it targets entailment rather than surface overlap, but it does not determine whether the supporting context is relevant to the question or whether the answer is correct. If a model follows an irrelevant distractor, that distractor may entail the wrong answer and produce a high grounding score. A divergence between reference agreement and NLI grounding is therefore an audit trigger, not a diagnosis; attribution requires relevance and correctness checks, per-passage analysis, and case review.

## What per-query evidence looks like in practice

The unit of evaluation becomes a set of observations per query:

- **Evidence availability:** did a judged-relevant passage reach the context shown to the generator?
- **Context composition:** where were relevant and answer-missing passages ranked?
- **Answer quality:** how well did the output answer the question or agree with the reference?
- **Context support:** was the output supported by the supplied context, under a named and calibrated scorer?

These observations should be cross-tabulated rather than forced into a single causal label. In particular, joined-context NLI cannot identify which passage supports an output; a claim that the generator followed a distractor requires per-passage support checks together with passage relevance and answer correctness. Paired confidence intervals can quantify which observed rates changed, while controlled ablations or case review are still needed to explain why.

## Two design implications

**Grounding is a separate axis, not a diagnosis.** Reference agreement, answer relevance or correctness, context relevance, and context faithfulness measure different properties. They should be reported separately rather than summed into one score. Their joint pattern narrows the investigation, but it does not by itself identify the causal stage.

**Audit fields deserve to be a versioned data product.** Once you commit to per-query reporting, the field definitions and each labeller (NLI model, threshold, score formula) become load-bearing for cross-experiment comparison. Pinning them &mdash; in a manifest, alongside model revisions &mdash; is what turns a reported rate into a comparable claim across experiments.

## What this note is not

This is a methodological note, not a causal account of the reported result. The concrete msmarco-genqa figures describe one fixed paired comparison with different first-stage retrieval boundaries; they do not establish that hard distractors caused the observed change. Any disagreement among lexical reference agreement, semantic similarity, and grounding signals should be treated as a hypothesis to inspect rather than a completed diagnosis.

## References

- [Papineni et al. (2002), BLEU](https://aclanthology.org/P02-1040/)
- [Lin (2004), ROUGE](https://aclanthology.org/W04-1013/)
- [Zhang et al. (2020), BERTScore](https://arxiv.org/abs/1904.09675)
- [Laban et al. (2022), SummaC](https://aclanthology.org/2022.tacl-1.10/)
- [Chen and Eger (2023), MENLI](https://aclanthology.org/2023.tacl-1.47/)
- [Cuconasu et al. (2024), The Power of Noise](https://arxiv.org/abs/2401.14887)
- [Saad-Falcon et al. (2024), ARES](https://aclanthology.org/2024.naacl-long.20/)

---

_Status: methodological note. Metric definitions and limitations are anchored above; empirical mechanism claims remain conditional on case review or controlled ablation._
