---
title: handwritten-ocr-system
summary: End-to-end handwritten OCR with CNN + BiLSTM + CTC on the IAM dataset.
order: 6
featured: false
academic: true
status: experimental
last_updated: "2026-05-27"
repo: https://github.com/GioiaZheng/handwritten-ocr-system
tags: ["computer-vision", "sequence-modeling", "pytorch"]
---

A from-scratch implementation of the CNN-RNN-CTC handwriting recognition stack — written to understand the pipeline rather than to chase a leaderboard.

## Problem

OCR is usually treated as a closed API call. This project takes it apart: image preprocessing → convolutional feature extractor → recurrent sequence model → CTC alignment → decoded string, with no high-level OCR library in the path.

## What I built

A PyTorch training pipeline on the IAM handwriting dataset (line-level), evaluated with Character Error Rate and Word Error Rate. A small inference web UI under [`OCR_WebApp/`](https://github.com/GioiaZheng/handwritten-ocr-system/tree/main/OCR_WebApp) for visual inspection.

## Technical components

<dl class="kv">
  <dt>Framework</dt><dd>PyTorch</dd>
  <dt>Architecture</dt><dd>CNN feature extractor → BiLSTM → CTC head</dd>
  <dt>Data</dt><dd>IAM handwriting database, line-level</dd>
  <dt>Metrics</dt><dd>Character Error Rate, Word Error Rate (held-out splits)</dd>
  <dt>Decoding</dt><dd>Greedy + beam CTC decoding</dd>
  <dt>Inference UI</dt><dd>Web app under <code>OCR_WebApp/</code> for visual prediction inspection</dd>
</dl>

## Evidence / outputs

> TODO: publish concrete CER / WER numbers on the IAM test split, a comparison row against a CRNN baseline, model size, and average per-line inference latency. The current README ships the architecture and evaluation harness but not a results table — this page intentionally does not invent numbers.

## Current status

Experimental. The architecture and training loop are stable; results table on the repo is the open item.

## Limitations

- Line-level only — no full-page layout analysis.
- No language model fusion; decoded outputs are raw model predictions plus simple beam search.
- No published baseline comparison yet (see Evidence).

## Repo

[github.com/GioiaZheng/handwritten-ocr-system](https://github.com/GioiaZheng/handwritten-ocr-system)
