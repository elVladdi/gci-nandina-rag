# G3-F01 Analytical Contract v0.1

## Contract state

This is the Prompt79 corrective microclose of the prospective G3-F01
analytical contract. It freezes sources, evidence families, estimands, and
future procedures. It performs no inference and does not decide HE2 or HE5.

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G3-F01
revision = PROMPT79_CORRECTIVE_MICROCLOSE
scientific_main_commit = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
canonical_plan_commit = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
article_head_observed = f02aef2448b7b8c0db2df4895c02860b66786716
fichas_snapshot_commit = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

## Global bindings

```text
UNIT_OF_ANALYSIS = SERIE
PRIMARY_ANALYTICAL_UNIT = SERIE
DEPENDENCY_GROUP = DAM / DECLARACIÓN cuando exista dependencia
DEPENDENCE_HANDLING = DAM_CLUSTER_AWARE
EVAL_V02_N = 1056
EVAL_V02_DAM_N = 67
EVAL_V02_NANDINA_N = 42
EVAL_V02_SHA256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
H100_N = 2950
H100_DAM_N = 28
H100_NANDINA_N = 66
H100_SHA256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
SUPERSEDED_SPLIT_3000_1006 = EXCLUDED
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

The primary estimand is always series-weighted. A later DAM-cluster bootstrap
must sample DAM clusters, carry every series in each sampled DAM, use the same
sampled DAM/cases in paired strategies, and recompute the series-weighted
estimand. It must not replace that estimand with an unweighted mean of DAM
means.

## Source governance

The exact frozen hypotheses were verified by the external auditor against the
approved source. Codex did not directly read the PDF bytes and used the frozen,
author-approved transcription.

```text
SRC01_DIRECT_PDF_BYTES_READ_BY_CODEX = false
SRC01_FROZEN_TRANSCRIPTION_USED = true
SRC01_FROZEN_TRANSCRIPTION_BLOB = 52c45948bbc085a25faf4df850ae15e6ca682d17
SRC01_AUTHOR_APPROVAL_BLOB = db5cd447df1d85ee0f9d271e2a85af66e050aea1
SRC01_EXTERNAL_AUDITOR_DIRECT_SOURCE_VERIFICATION = true
SRC01_HYPOTHESIS_TEXT_MISMATCH = false
SOURCE_ACCESS_GOVERNANCE_DEVIATION = DOCUMENTED
SCIENTIFIC_RERUN_REQUIRED_FOR_SRC01 = false
```

HE2 remains exactly:

> La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.

HE5 remains exactly:

> Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.

## HE2 operationalization

HE2_A is early-ranking performance. Its approved primary metrics are Top-1,
Top-3, Top-5, Top-10, and MRR@100; Top-50 is supplementary only. The final
comparable normative inventory is flat BM25, hierarchical BM25, and D1a, all
from corrected Attempt06 Decision 906 outputs. Static checks found identical
sets of 1,056 `case_id` values, identical `id_unico` values, and identical
labels against historical retrieval. D1a obtains DAM and SERIE by an exact
`case_id`/`id_unico` join to the frozen EVAL/historical case summary.

For each of the three HE2_A families, the future estimand is the
series-weighted mean of the paired per-series contribution
`historical - normative`: binary hit differences for Top-1/3/5/10 and
reciprocal-rank difference truncated at rank 100 for MRR@100. Expected
direction is positive. A future analysis may use 10,000 paired DAM-cluster
bootstrap resamples with seed 20263001 and two-sided percentile intervals.
Within each five-metric strategy family, 99% marginal intervals implement a
Bonferroni familywise 95% rule. No p-values are planned.

HE2_B is deep coverage and is not interchangeable with ranking performance.
The corrected hierarchical family uses exact NANDINA Recall@100,
Recall@200/Pool@200; its single prospective contrast is the series-weighted
paired difference `hit_recall_200 - hit_recall_100`, expected positive. Its
future procedure is the same paired 10,000-resample DAM-cluster bootstrap,
seed 20263001, with one two-sided 95% percentile interval; multiplicity is not
applicable to that single contrast.

Candidate-pool evidence comes only from Phase E under
`outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/`.
The frozen-role variants `hierarchical_only`, `dual_only`,
`hierarchical_first_100`, and `hierarchical_80_dual_backfill_20` carry
`pre_specification=A_historical_defined` and remain descriptive coverage
inventories at Pool@50/100/200. `hierarchical_70_dual_backfill_30` remains
`B_historical_not_formally_frozen_for_v0_2`. The
`diagnostic_union_hierarchical_dual` remains `not_a_ranking=true` and is only a
descriptive coverage ceiling. EXP08 is not a primary source for HE2_B.

## Sensitivity families

EXP11A is `SENSITIVITY_ONLY`: 30 variable runs (10 H25, 10 H50, 10 H75),
plus one frozen H100 reference check. H50 D1/D2 uses five paired seeds
20261001--20261005. EVAL is 1,056 series/67 DAM; H100 is 2,950 rows/28 DAM.
Bank size and composition are coupled, so no isolated causal size effect is
authorized.

EXP11B contains ten H150 and ten H200 banks paired on the same ten seeds and
reuses the same 1,056-series EVAL in every run. The 10 x 1,056 rows are not
independent observations. No defensible superpopulation of seeds was frozen;
the family is therefore `DESCRIPTIVE_ONLY` sensitivity, not inferential.

Attempt06 sensitivity is descriptive only and binds to the corrected flat,
hierarchical, D1a, execution-record, and unified-summary outputs. Superseded
attempts and uncorrected 0B-05C outputs are excluded.

## HE5 operationalization

The integrated matrix has 1,056 series and explicit DAM/SERIE fields.
`description_quality_operationalized=0`, so ambiguous/incomplete-description
prevalence is not estimable. Hierarchy categories `SAME_CHAPTER`, `SAME_HS4`,
and `SAME_HS6` are preserved descriptively. Historical support buckets are
used literally as frozen: `1 DAM`, `2 DAM`, `3-4 DAM`, and `5+ DAM`; no bucket
is newly labeled "insufficient" and no post-hoc threshold is created. The
validity boundary remains the internal Chapter 87 benchmark. Explanation and
evidence auditability is a diagnostic limitation, not a fifth literal HE5
proposition. All HE5 families are `DESCRIPTIVE_ONLY`.

## Evidence-family inventory

The machine-readable JSON is authoritative and records every required field
for each family. The terminal inventory is:

| Evidence family | Component | Compared conditions | Exact eligible metrics | Classification |
|---|---|---|---|---|
| HE2_A_HISTORICAL_VS_NORMATIVE_FLAT_ATTEMPT06 | HE2_A | historical vs corrected flat | Top-1/3/5/10, MRR@100; Top-50 supplementary | ELIGIBLE |
| HE2_A_HISTORICAL_VS_NORMATIVE_HIERARCHICAL_ATTEMPT06 | HE2_A | historical vs corrected hierarchical | Top-1/3/5/10, MRR@100; Top-50 supplementary | ELIGIBLE |
| HE2_A_HISTORICAL_VS_D1A_ATTEMPT06 | HE2_A | historical vs corrected D1a | Top-1/3/5/10, MRR@100; Top-50 supplementary | ELIGIBLE |
| HE2_B_HIERARCHICAL_DEEP_COVERAGE_ATTEMPT06 | HE2_B | corrected hierarchical depth 100 vs 200 | Recall@100, Recall@200/Pool@200 | ELIGIBLE |
| HE2_B_PHASE_E_FROZEN_ROLE_POOLS | HE2_B | four A_historical_defined variants | Pool@50/100/200 | DESCRIPTIVE_ONLY |
| HE2_B_PHASE_E_70_30 | HE2_B | hierarchical_70_dual_backfill_30 | Pool@50/100/200 | DESCRIPTIVE_ONLY |
| HE2_B_PHASE_E_DIAGNOSTIC_UNION | HE2_B | diagnostic union ceiling | Pool@50/100/200 | DESCRIPTIVE_ONLY |
| EXP11A_HISTORICAL_BANK_SENSITIVITY | sensitivity | H25/H50/H75/H100 | frozen Top-1/3/5/10/50 and MRR | DESCRIPTIVE_ONLY |
| EXP11B_H150_H200_PAIRED_SENSITIVITY | sensitivity | paired H150 vs H200 seeds | frozen Top-1/3/5/10/50 and MRR | DESCRIPTIVE_ONLY |
| 0B05C_ATTEMPT06_CORRECTIVE_SENSITIVITY | sensitivity | corrected vs control arms | frozen comparison fields only | DESCRIPTIVE_ONLY |
| HE5_AMBIGUOUS_INCOMPLETE_DESCRIPTIONS | HE5 | no operationalized contrast | none | DESCRIPTIVE_ONLY |
| HE5_HIERARCHICAL_PROXIMITY | HE5 | frozen hierarchy categories | frozen counts only | DESCRIPTIVE_ONLY |
| HE5_INSUFFICIENT_HISTORICAL_PRECEDENTS | HE5 | four literal support buckets | frozen summaries only | DESCRIPTIVE_ONLY |
| HE5_INTERNAL_EVALUATION_SCOPE | HE5 | internal benchmark boundary | coverage inventory | DESCRIPTIVE_ONLY |
| HE5_EXPLANATION_EVIDENCE_LIMITS | HE5 diagnostic limitation | diagnostic samples/scopes | traceability inventory | DESCRIPTIVE_ONLY |
| EXP12_DIVERSITY | EXP12 | no selected conditions | none | NOT_ESTIMABLE |

## Frozen exclusions and administration

The split 3,000/1,006, superseded 0B-05C outputs, post-hoc support thresholds,
unselected EXP12 conditions, and any unlisted scientific rerun are excluded.
No result is selected because it is favorable.

```text
G3_F01_ACTIVATION_REGISTRY_RECONCILIATION = REQUIRED_BEFORE_CLOSURE
G3_F01_ACTIVATION_WAS_USER_AUTHORIZED = true
G3_F01_ACTIVATION_REGISTRY_WAS_NOT_MATERIALIZED_PREEXECUTION = true
```

## Audit state

```text
INFERENTIAL_CALCULATION_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
SCIENTIFIC_EXPERIMENT_REEXECUTED = false
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
G3_F01_EXTERNAL_AUDIT = PENDING_REAUDIT
G3_F02_AUTHORIZED = NO
```
