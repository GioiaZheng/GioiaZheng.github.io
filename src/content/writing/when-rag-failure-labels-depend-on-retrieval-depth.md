---
title: "When RAG Failure Labels Depend on Retrieval Depth"
summary: "A small SciFact retrieval-depth check where retrieval hit rose from 13/20 to 14/20 while a binary retrieval_noise label rose from 7/20 to 20/20."
date: "2026-09-04"
status: published
order: 0
---

## The question

When retrieval depth changes, do our RAG failure labels still describe the same phenomenon?

That question came up while looking at a small controlled run in [rag-observatory](/projects/rag-observatory/). I was not trying to prove that one retrieval setting is better than another. The narrower goal was to check whether a diagnostic label remains interpretable when the retrieval configuration changes underneath it.

This matters because failure labels can feel more concrete than aggregate scores. A label like `retrieval_noise` sounds like an error category. But in an evaluation pipeline, a label is still a measurement produced by a configuration, an annotation rule, and a piece of code. If any of those changes, the meaning of the label can move too.

## Controlled setup

The run used BEIR SciFact test data, with the first 20 sorted test queries in the diagnostic sample. It compared two retrieval-depth settings: `retrieval_top_k=1` and `retrieval_top_k=5`.

The important control is that retrieval depth was the only main changed variable. The same query set, BM25 retriever implementation, top-1 context policy, deterministic extractive answer rule, and qrels-based evaluator were held fixed. In other words, the run asked a simple question: if the candidate pool gets deeper, what happens to the measured labels?

The generator in this run was deliberately boring: it selected text from the first retrieved document. That makes the experiment less like a full production RAG benchmark, but more useful as a diagnostic check. The point was to isolate how retrieval depth affects trace-level measurements before adding more moving parts.

## What changed

The retrieval hit metric improved slightly when the run moved from `top_k=1` to `top_k=5`. A trace counted as a retrieval hit if at least one qrels-relevant SciFact document appeared in the retrieved candidate set.

| Configuration | Retrieval hit | `retrieval_noise` | Failure-labelled traces |
| --- | ---: | ---: | ---: |
| `retrieval_top_k=1` | 13/20 (0.650) | 7/20 | 7/20 |
| `retrieval_top_k=5` | 14/20 (0.700) | 20/20 | 20/20 |

The surprising part is not the hit-rate change. Going deeper can surface one more relevant document. The surprising part is the binary `retrieval_noise` label: it moved from 7 out of 20 traces to 20 out of 20 traces.

At first glance, that could be misread as "the `top_k=5` configuration is much noisier, therefore worse." That is too quick.

## Why the label became unstable

In this experiment, `retrieval_noise` is a heuristic label. It fires when at least one retrieved document is annotated as not relevant. That rule is useful as an inspection signal, but it is not an objective truth about whether the whole answer failed.

With `top_k=1`, the candidate set contains one document. The label fires only if that one document is irrelevant. With `top_k=5`, the candidate set contains five documents, so the chance of including at least one irrelevant document is much higher. The label can saturate even when the deeper retrieval set also includes useful evidence.

This is the measurement issue: a binary "any irrelevant document" rule changes its behavior when the number of retrieved documents changes. The trace may be more complete, and the hit rate may be slightly better, while the noise label becomes less comparable across configurations.

The result does not mean `retrieval_top_k=5` is worse. It means that this particular label is sensitive to the retrieval depth and the decision rule used to create it.

## What this means for RAG evaluation

For RAG evaluation, a failure label should travel with its configuration. Reporting "`retrieval_noise` increased" without also reporting `retrieval_top_k`, the definition of noise, and the context-selection rule can be misleading.

A more stable diagnostic design would make the measurement less binary. For example, instead of only asking whether any irrelevant document appears, the report could include a graded noise measure: how many retrieved documents were irrelevant, where they appeared in the ranking, and whether a relevant document was also present. It could also report stability across several `k` values, not only one comparison.

The broader lesson is that failure analysis should be versioned like the rest of an evaluation pipeline. The dataset slice, retrieval configuration, labelling heuristic, scorer, and report format all shape the final diagnosis. If those choices are not recorded, the label becomes hard to compare across runs.

## Limitations

This is a small diagnostic run, not a general benchmark result. The sample contains 20 SciFact test queries, and the experiment does not claim statistical significance.

The result should not be automatically generalized to every dataset, retriever, reranker, generator, or RAG pipeline. It also does not show that a higher retrieval hit rate always improves generation quality. In this setup, generation was intentionally deterministic and extractive, because the focus was measurement sensitivity rather than end-to-end answer quality.

The safest reading is narrow: on this controlled SciFact run, a binary `retrieval_noise` heuristic changed sharply when retrieval depth changed from 1 to 5. That is enough to justify treating the label as configuration-dependent evidence, not as a standalone ground-truth category.

## Next experiment

The next useful step is to make the diagnostic less brittle. I would compare several retrieval depths, keep both binary and graded noise measures, and track whether the same query receives the same failure interpretation across `k`.

I would also separate candidate-pool noise from context noise. A retrieved irrelevant document is different from an irrelevant document that is actually passed to the generator. Those should not be collapsed into one label if the goal is to explain where the pipeline failed.

## Evidence

The verified SciFact evidence for this note is the committed report and runner. The Hugging Face link below is the public toy trace dataset that accompanies the project, not the raw SciFact trace output.

- [rag-observatory repository](https://github.com/GioiaZheng/rag-observatory)
- [SciFact retrieval-depth report](https://github.com/GioiaZheng/rag-observatory/blob/main/docs/reports/2026-07-25-scifact-retrieval-depth.md)
- [SciFact config-sensitivity runner](https://github.com/GioiaZheng/rag-observatory/blob/main/scripts/run_scifact_config_sensitivity.py)
- [Failure taxonomy note](https://github.com/GioiaZheng/rag-observatory/blob/main/docs/failure_taxonomy.md)
- [Public toy trace dataset on Hugging Face](https://huggingface.co/datasets/GioiaZheng/rag-observatory-toy-traces)
