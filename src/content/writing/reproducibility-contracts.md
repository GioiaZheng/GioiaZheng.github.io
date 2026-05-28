---
title: "Reproducibility contracts for small-scale AI experiments"
summary: A schema-versioned manifest enforced at write time turns "I ran an experiment" into "anyone with the repo can run this experiment".
status: planned
order: 4
---

Planned.

A walk-through of what a reproducibility contract actually looks like at the field level: resolved config + content hash, data fingerprint, environment fingerprint, pinned model revisions, sampled-evaluation caveat. The interesting design choice is enforcing the contract at write time — a run that fails to capture any required field cannot land an artifact — rather than auditing after the fact.

TODO: write.
