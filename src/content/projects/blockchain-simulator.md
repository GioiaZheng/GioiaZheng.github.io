---
title: Blockchain Simulator (Java P2P)
summary: Java multithreaded peer-to-peer blockchain simulator with proof-of-work validation; coursework systems project.
order: 10
featured: false
status: archived
last_updated: "2023-06-30"
tags: ["java", "distributed-systems", "blockchain", "concurrency"]
---

A coursework distributed-systems project — Java multithreaded peer-to-peer network with proof-of-work consensus — built as the Programming 2 final at Sapienza.

## Problem

Most "build a blockchain" tutorials stay single-process. The brief here was the harder version: multiple agents running concurrently in the same JVM, communicating over an internal P2P channel, with proof-of-work validation and observable behavior under varying difficulty.

## What I built

A self-contained Java simulator: each peer is a thread, blocks propagate over a simulated network layer, and proof-of-work difficulty is a tunable parameter. The simulator collects per-run metrics (block time, fork rate, network convergence) so different consensus parameters can be compared on the same scenario.

## Technical components

<dl class="kv">
  <dt>Language</dt><dd>Java</dd>
  <dt>Concurrency</dt><dd>Per-peer thread model with shared message channels</dd>
  <dt>Consensus</dt><dd>Proof-of-work with tunable difficulty</dd>
  <dt>Networking</dt><dd>Simulated P2P message bus (in-process, not real sockets)</dd>
  <dt>Instrumentation</dt><dd>Per-run logging of block time, fork count, network convergence</dd>
</dl>

## Evidence / outputs

- Working multithreaded simulator that runs end-to-end, with parameter sweeps over difficulty and peer count.
- Per-run analysis: how block-production time and fork rate behave under varying consensus parameters.
- Written project report (Programming 2 final).

## Current status

Archived. Coursework deliverable, not extended.

## Limitations

- In-process P2P, not real network sockets — latency and partition behavior are simulated, not real.
- No transaction layer; the consensus story is the whole project.
- No public GitHub repo (coursework artifact lives as a project report only).
