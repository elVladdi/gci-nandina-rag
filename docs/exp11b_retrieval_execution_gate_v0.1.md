# EXP-11B Retrieval Execution Gate v0.1

## Status

`CANDIDATE_PENDING_EXTERNAL_AUDIT`.

This is a prospective execution contract. It does not execute historical BM25
for H150 or H200, compute metrics, create result rows, or authorize retrieval.

## Canonical BM25 semantics

The future runner must reuse `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`.
EXP-11A v0.3 imports that module and directly calls its index, score,
deduplication, rank, and MRR helpers. The frozen semantics are:

- NFKD lowercase text with combining marks removed.
- Tokens matched by `[a-z0-9]+`.
- BM25 `k1=1.5`, `b=0.75`, candidate depth 100.
- Descending score, then ascending historical `case_id` for ties.
- First ranked historical row per NANDINA retained as the unique candidate.
- Top-1/3/5/10/50 and MRR over all 1056 primary eval cases.

## Inputs and banks

The configuration freezes the integrated base, evalset, H100 reference,
historical audit inputs, source-file hashes, materialization manifest, F003
ledger, Gate 03 feasibility artifact, and common-clean mask. The generated
input inventory records all twenty bank identities from the ledger.

Common-clean is sensitivity-only. It never replaces the primary N=1056:

- exact: 36 affected, clean N=1020;
- near 0.90: 75 affected, clean N=981;
- near 0.95: 54 affected, clean N=1002;
- near 0.98: 46 affected, clean N=1010.

## Future execution policy

There is exactly one official execution per one of the 20 frozen banks. The
future runner must fail closed on any material failure. Retries, silent resume,
overwrite, partial recomputation as an official run, output replacement, and
configuration mutation after start are forbidden.

The defined future outputs are a run manifest, metrics by bank, case-level
results, candidate rankings, condition summary, output hash ledger, failure
ledger, and environment metadata. This gate only versions their schemas; it
does not create a future execution output directory.

## Provenance notice

The materialization manifest preserves its embedded historical configuration
fingerprint while the current tracked materialization configuration is frozen
separately by exact SHA-256. This is recorded for external audit and does not
alter the verified manifest or ledger identities of the twenty banks.
