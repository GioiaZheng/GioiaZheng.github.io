---
title: handwritten-ocr-system
summary: End-to-end handwritten OCR with CNN + BiLSTM + CTC, evaluated with CER / WER.
order: 3
featured: true
status: maintained
repo: https://github.com/GioiaZheng/handwritten-ocr-system
tags: ["computer-vision", "sequence-modeling", "pytorch"]
---

A from-scratch implementation of the CNN-RNN-CTC handwriting recognition stack, with the training loop, evaluation harness, and ablations all wired together in a single PyTorch project.

## Problem

OCR is usually treated as a closed API call. This project takes it apart: image preprocessing → convolutional feature extractor → recurrent sequence model → connectionist temporal classification → decoded string, with no high-level OCR library in the path.

## What I built

A PyTorch training pipeline on the IAM handwriting dataset with the full CNN + BiLSTM + CTC stack, plus a held-out evaluation harness that reports Character Error Rate and Word Error Rate per split.

## Technical components

<dl class="kv">
  <dt>Framework</dt><dd>PyTorch</dd>
  <dt>Architecture</dt><dd>CNN feature extractor → BiLSTM → CTC head</dd>
  <dt>Data</dt><dd>IAM handwriting database, line-level</dd>
  <dt>Metrics</dt><dd>Character Error Rate, Word Error Rate on held-out splits</dd>
  <dt>Training</dt><dd>Curriculum-free baseline; greedy + beam CTC decoding</dd>
</dl>

## Evidence / outputs

- Trained model with reported CER / WER on the official IAM test split.
- Reproducible training script and split definitions in-repo.

## Current status

Maintained. The core training loop and evaluation harness are stable; not actively chasing SOTA numbers.

## Limitations

Line-level recognition only — no full-page layout analysis. No language model fusion; decoded outputs are raw model predictions plus simple beam search.

## Repo

<a href="https://github.com/GioiaZheng/handwritten-ocr-system">github.com/GioiaZheng/handwritten-ocr-system</a>
