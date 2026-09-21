# PROMPT 96 — INTEGRAR Y CERRAR G5-F01 TRAS REAUDITORÍA EXTERNA

## 0. Naturaleza y autorización

Esta ejecución corresponde exclusivamente a la integración y cierre administrativo de **G5-F01 — Arquitectura de presentación de resultados** después de la reauditoría externa satisfactoria del candidato corregido v02.

Dictamen externo gobernante:

```text
PROMPT95_EXTERNAL_AUDIT = PASS
G5_F01_CORRECTED_CANDIDATE_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
G5_F01 = APPROVABLE_FOR_INTEGRATION_AND_CLOSURE
GROUP5 = IN_PROGRESS
G5_F02_AUTHORIZED = false
```

Esta ejecución autoriza únicamente:

1. integrar por fast-forward puro el candidato G5-F01 v02 previamente auditado;
2. cerrar administrativamente G5-F01 como `CLOSED / APPROVED / INTEGRATED_TO_MAIN`;
3. reconciliar el Plan Maestro con ese cierre;
4. dejar G5-F02 como `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.

No autoriza:

- regenerar o modificar los dos artefactos científicos-documentales auditados de G5-F01;
- recalcular métricas, CI, inferencia o p-values;
- ejecutar experimentos o retrieval;
- materializar tablas numéricas finales;
- modificar HE2 o HE5;
- reabrir EXP12;
- modificar el artículo o la tesis;
- activar o ejecutar G5-F02;
- cerrar Grupo 5;
- iniciar Grupo 6.

---

## 1. Preflight obligatorio y refs congelados

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 38e22c19a0eb0d344e7675761a88d7968091eead
origin/docs/plan-maestro-temporal-2026-08-31 = 3ba3557eb10e741b8f49c420850940dee1df08ef
origin/docs/fichas-grupos-3-8 = 5c1a00acb87d3a6cd8122043e3d36650999bd005
origin/codex/group5-f01-results-presentation-architecture-v02 = d5729887f47c36d8cf42d87090c40f9668e5ae84
origin/article/main-manuscript = b2b338493f4045a772e6bbb40a606fc63cea9c79
```

Gobernanza inmediata:

```text
PROMPT94_SOURCE = 37edbc97610395ef655379628d63f0d8847d117c
PROMPT94_RESPONSE = 9442027fc0d96ee28fe9acd39f5ab473078742a4
PROMPT94_CANDIDATE_V01 = 779c07c7865b115e668f8d8f409c0080638f9134
PROMPT95_SOURCE = c36b0d18c4d3588c92d95c1c17596384e2697e2f
PROMPT95_RESPONSE = 9de82202002cfbb7520813a22305ad3e0b6415a0
PROMPT95_POSTCORRECTION_FICHAS = 5c1a00acb87d3a6cd8122043e3d36650999bd005
G5_F01_CORRECTED_CANDIDATE_V02 = d5729887f47c36d8cf42d87090c40f9668e5ae84
G5_F01_V02_PARENT = 38e22c19a0eb0d344e7675761a88d7968091eead
```

Blobs auditados que deben preservarse exactamente:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245
```

La rama editorial es solo lectura/observacional. Si avanza concurrentemente, registra el HEAD final como advertencia no bloqueante siempre que esta ejecución no la modifique.

Si `main`, Plan, fichas o candidato presentan drift no explicado:

```text
STOP / G5_F01_CLOSURE_REF_DRIFT
```

---

## 2. Verificación previa del candidato auditado

Antes de integrar confirma:

```text
candidate = d5729887f47c36d8cf42d87090c40f9668e5ae84
parent = 38e22c19a0eb0d344e7675761a88d7968091eead
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
```

Los únicos paths del candidato deben ser:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
outputs/results/group5/g5_table_registry_v0.1.json
```

Confirma además en el candidato:

```text
PRESENTATION_REGISTRY_COUNT = 16
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G3_EVIDENCE_FAMILY_UNMAPPED_COUNT = 0
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
G4_CONTROLLED_CLAIM_UNMAPPED_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0
FAVORABILITY_BASED_SELECTION_COUNT = 0
UNJUSTIFIED_OMISSION_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
FINAL_NUMERIC_TABLE_MATERIALIZED_COUNT = 0
NEW_METRIC_VALUE_DERIVED_COUNT = 0
HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
G5_F02_STARTED = false
```

Verifica específicamente que `G5-MAIN-01` mantenga separados:

```text
historical_observed_value
comparator_observed_value
paired_difference_historical_minus_comparator
frozen_99pct_ci_lower_for_paired_difference
frozen_99pct_ci_upper_for_paired_difference
```

y que el CI de G3-F03 esté ligado exclusivamente al contraste pareado histórico menos comparador, no a valores absolutos por brazo.

Si falla cualquier condición:

```text
STOP / G5_F01_AUDITED_CANDIDATE_MISMATCH
```

---

## 3. Integración exacta a `main`

Integra exclusivamente mediante fast-forward puro:

```text
38e22c19a0eb0d344e7675761a88d7968091eead
    -> d5729887f47c36d8cf42d87090c40f9668e5ae84
```

No cherry-pick, no squash, no merge commit, no regeneración.

Después del push debe cumplirse:

```text
origin/main = d5729887f47c36d8cf42d87090c40f9668e5ae84
```

Y los blobs en `main` deben seguir exactamente:

```text
PRESENTATION_PLAN_BLOB = 9eaf780f3a2f6c8579dc80867ed3a86e96683894
TABLE_REGISTRY_BLOB = 4fe9318d52fad093066ff9f42d524fc95e436245
```

Si cambia cualquier blob:

```text
STOP / G5_F01_INTEGRATION_BLOB_DRIFT
```

---

## 4. Cierre administrativo de G5-F01

Trabaja únicamente en:

```text
branch = docs/fichas-grupos-3-8
base = 5c1a00acb87d3a6cd8122043e3d36650999bd005
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo para dejar:

```text
G5-F01 = CLOSED / APPROVED
G5-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP5 = IN_PROGRESS
```

Añade un bloque de cierre que registre como mínimo:

```text
FICHA = G5-F01
PROMPT94_SOURCE = 37edbc97610395ef655379628d63f0d8847d117c
PROMPT94_RESPONSE = 9442027fc0d96ee28fe9acd39f5ab473078742a4
PROMPT95_SOURCE = c36b0d18c4d3588c92d95c1c17596384e2697e2f
PROMPT95_RESPONSE = 9de82202002cfbb7520813a22305ad3e0b6415a0
SUPERSEDED_CANDIDATE = 779c07c7865b115e668f8d8f409c0080638f9134
APPROVED_CANDIDATE = d5729887f47c36d8cf42d87090c40f9668e5ae84
G5_F01_EXTERNAL_REAUDIT = PASS
INTEGRATION_COMMIT = d5729887f47c36d8cf42d87090c40f9668e5ae84
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP5 = IN_PROGRESS
G5_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F02_AUTHORIZED = false
G5_F02_STARTED = false
```

Publica un único commit administrativo.

---

## 5. Reconciliación del Plan Maestro

Trabaja únicamente en:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = 3ba3557eb10e741b8f49c420850940dee1df08ef
file = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Actualiza exclusivamente ese archivo para reflejar el nuevo estado operacional:

```text
GROUP4 = CLOSED / APPROVED
GROUP5 = IN_PROGRESS
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F01_INTEGRATION_COMMIT = d5729887f47c36d8cf42d87090c40f9668e5ae84
G5_F01_EXTERNAL_REAUDIT = PASS
NEXT_ELIGIBLE_FICHA = G5-F02
G5_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F02_AUTHORIZED = false
G5_F02_STARTED = false
```

Registra también, sin reinterpretar:

```text
G5_F01_PRESENTATION_REGISTRY_COUNT = 16
G5_F01_G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G5_F01_G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
G5_F01_EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
G5_F01_HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
G5_F01_NEW_INFERENCE_PERFORMED = false
G5_F01_METRICS_RECOMPUTED = false
```

Preserva explícitamente los guardrails científicos existentes:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
```

No declares Grupo 5 cerrado.

---

## 6. Prohibiciones científicas y documentales

Durante Prompt96:

```text
SCIENTIFIC_ARTIFACT_REGENERATION = PROHIBITED
NEW_INFERENCE = PROHIBITED
NEW_CI = PROHIBITED
P_VALUES = PROHIBITED
METRIC_RECOMPUTATION = PROHIBITED
NEW_EXPERIMENT = PROHIBITED
RETRIEVAL = PROHIBITED
ARTICLE_EDIT = PROHIBITED
G5_F02_ACTIVATION = PROHIBITED
GROUP5_CLOSURE = PROHIBITED
```

No modifiques los artefactos integrados de G3/G4 ni cualquier output experimental previo.

---

## 7. Verificación final obligatoria

Tras todos los push ejecuta `git fetch origin` y verifica:

```text
origin/main = d5729887f47c36d8cf42d87090c40f9668e5ae84
origin/codex/group5-f01-results-presentation-architecture-v02 = d5729887f47c36d8cf42d87090c40f9668e5ae84
PRESENTATION_PLAN_BLOB = 9eaf780f3a2f6c8579dc80867ed3a86e96683894
TABLE_REGISTRY_BLOB = 4fe9318d52fad093066ff9f42d524fc95e436245

G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = IN_PROGRESS
G5_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F02_AUTHORIZED = false
G5_F02_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED_BY_PROMPT96 = false
```

Si la rama editorial avanzó concurrentemente, registra el nuevo HEAD como advertencia no bloqueante; no la modifiques.

---

## 8. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/96_RESPUESTA_INTEGRAR_Y_CERRAR_G5_F01_TRAS_REAUDITORIA.md
```

El commit de respuesta debe añadir únicamente ese archivo.

Reporte terminal mínimo:

```text
PROMPT96 = COMPLETED

PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
PREFLIGHT_CANDIDATE_V02 = ...
ARTICLE_HEAD_PREFLIGHT = ...

MAIN_AFTER_INTEGRATION = d5729887f47c36d8cf42d87090c40f9668e5ae84
PRESENTATION_PLAN_BLOB = 9eaf780f3a2f6c8579dc80867ed3a86e96683894
TABLE_REGISTRY_BLOB = 4fe9318d52fad093066ff9f42d524fc95e436245

FICHAS_CLOSURE_COMMIT = ...
PLAN_RECONCILIATION_COMMIT = ...

G5_F01_EXTERNAL_REAUDIT = PASS
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = IN_PROGRESS
G5_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F02_AUTHORIZED = false
G5_F02_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED_BY_PROMPT96 = false

ARTICLE_HEAD_FINAL_OBSERVED = ...
BLOCKERS = NONE
WARNINGS = ...
```
