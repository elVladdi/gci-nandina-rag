# 0B-05C corrective numerical recovery gate v0.3

## Scope

This candidate is a prospective, non-authorized recovery gate. It closes the EV04 metric-producer contract mismatch observed by Attempt03 without changing retrieval, ranking, corpora, patches, EVAL, BM25 parameters, D1a weights, or historical artifacts.

## Root cause

The historical hierarchical producer emits a legacy `mrr` row. The frozen EXP-04 Gate C artifact was later enriched with `mrr_at_100`, `mrr_at_200`, their numerators and denominators, the 101-200 contribution, and a fixed metric-table order. Attempt03 reproduced ranking and case rows exactly but failed the strict metrics comparison.

The v0.3 evaluator derives the enriched MRR payload from the reproduced case rows. It never copies expected control metrics into observed output. Control acceptance remains fail-closed and requires exact ranking, exact case summary, and exact enriched metrics.

## Isolation

All sixteen prospective roots use the v0.3 namespace and are disjoint from v0.2. Local v0.2 partial roots may remain as historical evidence, but v0.3 neither rejects nor reads them as execution inputs. The v0.2 gate, Attempt03 failure record, historical runner, Plan Maestro, article, EXP11B, EXP12, and every v0.1 artifact remain unchanged.

## Scientific invariants

- EV03 keeps recovered `DROP_SINGLE_CHARACTER_TOKENS`, BM25 `k1=1.5`, `b=0.75`, depth 100, Decision885 control, EVAL N=1056, and the two-code Decision906 patch.
- EV04 keeps the frozen hierarchical corpus, BM25 `k1=1.5`, `b=0.75`, effective depth 200, unique NANDINA-8 first-score duplicate collapse, EVAL N=1056, and the same two-code patch.
- D1a keeps the 470637416-byte model with SHA-256 `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`, full corrective index rebuild, EVAL N=1056, and the 17-metric contract.

## Candidate state

`gate_status=CANDIDATE_PENDING_EXTERNAL_AUDIT` and `authorization_readiness=NOT_AUTHORIZATION_READY`. All four numerical executions are `NOT_AUTHORIZED`; no authorization record or runtime record exists. Attempt04 is `NOT_AUTHORIZED / NOT_EXECUTED`.
