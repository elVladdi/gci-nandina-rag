# Prompt76 terminal report

PROMPT76 = COMPLETED | STOP

## Frozen refs

```text
main_final = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
plan_final = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
article_final = 254b1e6df736fa9938ac86a515d65b36f4d361c5
fichas_snapshot_final = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

The four refs were verified locally before the attempted remote update. A
fresh `git fetch origin` was blocked by the session usage limit; no ref was
modified.

```text
PROMPT75_STATUS = SUPERSEDED / DO_NOT_EXECUTE
SRC01_ORIGINAL = Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf
SRC01_ACCESS_MODE = AUTHOR_APPROVED_FROZEN_TRANSCRIPTION_IN_GITHUB
SRC01_DIRECT_PDF_BYTES_READ_BY_CODEX = false
SRC01_TRANSCRIPTION_STATUS = APPROVED / FROZEN / INDEPENDENTLY_VERIFIED_BY_IA_EXPERIMENTAL
HE2_TEXT_EXACT_MATCH = true
HE5_TEXT_EXACT_MATCH = true
```

## G3-F01 candidate

```text
G3_F01_BRANCH = codex/group3-f01-analytical-contract-v01
G3_F01_COMMIT = c727da94f5d38f530a839631c3ac9e427a1eb27e
G3_F01_PARENT = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
G3_F01_TREE = 8ba1692a4e236ee0d3ae8a0388793b52206ec0ec
G3_F01_COMMITS_AHEAD = 1
G3_F01_COMMITS_BEHIND = 0
G3_F01_CHANGED_PATH_COUNT = 2
G3_F01_CHANGED_PATHS =
  docs/analysis/group3/g3_analytical_contract_v0.1.md
  outputs/analysis/group3/g3_analytical_contract_v0.1.json
G3_F01_PUBLISHED = false
```

The candidate contains exactly one scientific commit and exactly the two
authorized paths. The candidate push was attempted with the requested branch
and was blocked by network access to `github.com:443`; it was not merged into
main. No additional publication or workaround was attempted.

## Evidence matrix

```text
EVIDENCE_FAMILY_COUNT = 13
ELIGIBLE_COUNT = 6
DESCRIPTIVE_ONLY_COUNT = 6
NOT_ESTIMABLE_COUNT = 1
NOT_APPLICABLE_COUNT = 0
```

The matrix separates HE2_A early ranking from HE2_B deeper coverage. It keeps
EXP11A as sensitivity-only with no isolated causal bank-size effect, binds
EXP11B to ten paired H150/H200 seeds, and uses only corrected Attempt06 for
0B-05C. HE5 is split into descriptive ambiguity, hierarchical proximity,
historical support, internal scope, and explanation/evidence limits. EXP12 is
`NOT_ESTIMABLE`; no D-HIGH, D-MID, or D-LOW selection is introduced.

```text
EXP11A_INFERENCE_SCOPE = SENSITIVITY_ONLY
EXP11A_ISOLATED_CAUSAL_BANK_SIZE_EFFECT = NOT_AUTHORIZED
EXP11A_DESIGN = independent complete-DAM conditions
EXP11A_H50 = paired D1/D2 stratification
ATTEMPT06_ONLY = true
EXP12_ANALYTICAL_CLASSIFICATION = NOT_ESTIMABLE
```

The contract freezes procedures prospectively and does not run them. No
calculation, retrieval, metric recomputation, ranking regeneration, or
statistical test was performed by Prompt76.

```text
INFERENTIAL_CALCULATION_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
SCIENTIFIC_EXPERIMENT_REEXECUTED = false
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
EXTERNAL_AUDIT_REQUIRED = true
```

## Administrative persistence

```text
response_path = codex_prompts_tmp/76_RESPUESTA_EJECUTAR_G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
response_branch = codex/prompts-temporary
response_commit = PENDING_LOCAL_COMMIT
```

This response file is the only path intended for the administrative commit.
