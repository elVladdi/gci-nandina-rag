# EXP-04 and Group 1 Consolidated Closure v0.2

## Decision

EXP-04 (full rerun with corrected split) and Group 1 experimental design are CLOSED and APPROVED for review before any merge to `main`. This closure is a deterministic inventory of frozen evidence; it did not execute retrieval, call a model, change the split, or reopen hypotheses.

## Principal Evidence

Historical retrieval is the principal candidate-ranking result: Top-1 538/1056 (0.509470), Top-3 709/1056 (0.671402), Top-5 806/1056 (0.763258), Top-10 941/1056 (0.891098), Top-50 1047/1056 (0.991477), and MRR 0.629707. Normative BM25 flat and hierarchical results are preserved as documentary evidence and not as replacements for the main historical ranking. Dense D1a is preserved as early retrieval evidence.

HE4 used a fixed top-3 context for 50 sampled cases and is a local explanation audit only. The diagnostic reranker is not a benchmark claim. The pilot remains internally scoped to Clase 87 and must not be generalized beyond the frozen internal evaluation conditions.

## Integrity

The v0.2 split records zero DAM overlap, no evaluation drift, and no evaluation tuning. Exact and near-duplicate audits, concentration limitations, all listed phase gates, and the EXP-08 corrective sensitivity close are retained in the provenance registry. HE2, HE3, HE4, and HE5 statuses are preserved; no formal OE1/HE1 assessment is invented.

## Scope Boundary

This consolidation does not merge to `main` and does not authorize Group 2. The full list of residual limitations is intentionally preserved in `exp04_consolidated_limitations_v0.2.csv`.
