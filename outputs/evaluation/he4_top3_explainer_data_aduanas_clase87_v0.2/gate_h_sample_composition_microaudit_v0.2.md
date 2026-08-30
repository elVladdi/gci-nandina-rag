# Gate H Sample-Composition Microaudit v0.2

## Decision

APPROVED. This is read-only. No sample, Top-3, context, input, prompt, model, schema, or rubric changed. No LLM was called and Phase I was not started.

## Selector

- Script: src/experiments/prepare_he4_pre_explainer_data_aduanas_v02.py.
- Population: 1,056 frozen Phase A historical_case_summary rows.
- exact_rank is the expected NANDINA rank in the complete code-deduplicated Phase A candidate list; 0 means absent.
- support_count_dams is distinct historical DAM support for expected NANDINA.
- Buckets: rank_1 is 1; rank_2_3 is 2-3; rank_4_10 is 4-10; difficult_low_support is 0, above 10, or low support after the prior branches.
- The buckets are mutually exclusive and exhaustive. difficult_low_support is not an independent low-support stratum for ranks 1-10. Support controls ordering, and its ten selected cases have support 1-3.
- Ordering: support bucket 0, 1, 2-4, 5-9, 10+; support ascending; exact rank ascending with zero last; case_id ascending.
- Seed 2026 is metadata only; no random generator or shuffle exists.
- A used case_id set prevents reuse. Target priority is rank_1, rank_2_3, rank_4_10, difficult_low_support.
- Fallback would scan non-target rows after direct rows. It was unused.

## Quotas

| bucket | quota | eligible | direct | fallback | status |
| --- | ---: | ---: | ---: | ---: | --- |
| rank_1 | 15 | 538 | 15 | 0 | A. QUOTA SATISFIED DIRECTLY |
| rank_2_3 | 15 | 171 | 15 | 0 | A. QUOTA SATISFIED DIRECTLY |
| rank_4_10 | 10 | 232 | 10 | 0 | A. QUOTA SATISFIED DIRECTLY |
| difficult_low_support | 10 | 115 | 10 | 0 | A. QUOTA SATISFIED DIRECTLY |

15/15/10/10 means direct selections from the named buckets. This run coincides with full Phase A rank groups 1, 2-3, 4-10, and 11-50.

## Full Rank Composition

| full Phase A rank | cases |
| --- | ---: |
| rank 1 | 15 |
| rank 2-3 | 15 |
| rank 4-10 | 10 |
| rank 11-50 | 10 |
| rank >50/not recovered | 0 |

Top-1 is 15/50. Top-3 is 30/50. Top-10 is 40/50. Top-50 is 50/50.

| selection bucket | rank1 | rank2-3 | rank4-10 | rank11-50 | >50/not recovered |
| --- | ---: | ---: | ---: | ---: | ---: |
| rank_1 | 15 | 0 | 0 | 0 | 0 |
| rank_2_3 | 0 | 15 | 0 | 0 | 0 |
| rank_4_10 | 0 | 0 | 10 | 0 | 0 |
| difficult_low_support | 0 | 0 | 0 | 10 | 0 |

## Evaluation-Only

he4_sample_evaluation_only_v0.2.csv is CORRECT AS TOP3 PROJECTION. It records rank within exported Phase A Top-3 and zero when the reference is absent. It has 15 rank-1, 10 rank-2, 5 rank-3, and 20 zero rows. It is not the complete exact-rank table: the zeroes are ten full ranks 4-10 and ten full ranks 11-50.

The earlier Top-1=0/50 and Top-3=50/50 report read nonexistent field reference_rank instead of reference_rank_evaluation_only. This microaudit corrects that report only; no frozen HE4 artifact changed.

## Freeze Checks

- Top-3 Phase A equals Phase F by code, position, and score: 150/150 PASS.
- Contexts and generation inputs are byte-identical intentionally: the builder serializes the same closed Top-3 objects twice.
- Label used for sample design: true. Label exposed to future LLM payloads: false.
- Prompt, schema, rubric, sample, contexts, and inputs retain frozen hashes.
- llm_called is false; no HE4 responses exist; phases A-G remain intact.

## Gate

ready_for_phase_i remains true as the frozen technical readiness flag. Phase I remains unstarted pending human review.
