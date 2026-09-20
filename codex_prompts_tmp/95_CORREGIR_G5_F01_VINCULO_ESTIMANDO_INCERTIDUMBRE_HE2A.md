# PROMPT 95 — CORREGIR G5-F01: VÍNCULO ESTIMANDO–INCERTIDUMBRE EN HE2_A

## 0. Naturaleza y alcance

Esta ejecución corrige exclusivamente un defecto documental de G5-F01 detectado en auditoría externa de Prompt94.

Dictamen gobernante:

```text
PROMPT94_EXTERNAL_AUDIT = PASS_WITH_CORRECTION_REQUIRED
G5_F01_SCIENTIFIC_CONTENT = SUBSTANTIVELY_PASS
G5_F01_TRACEABILITY_AND_UNCERTAINTY_BINDING = FAIL_LOCALIZED
SCIENTIFIC_RECOMPUTATION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
CORRECTION_SCOPE = HE2A_ESTIMAND_CI_BINDING_ONLY
G5_F01 = NOT_APPROVABLE_FOR_INTEGRATION_YET
GROUP5 = IN_PROGRESS
G5_F02_AUTHORIZED = false
```

La corrección no cambia resultados, métricas, hipótesis, jerarquía de presentación ni conteos de cobertura. Corrige únicamente la arquitectura de `G5-MAIN-01` para que el intervalo de confianza congelado de G3-F03 quede ligado inequívocamente al **contraste pareado histórico − comparador**, y no pueda interpretarse como un CI del rendimiento absoluto de cada brazo.

No autoriza G5-F02, integración a `main`, actualización del Plan, nueva ciencia, nueva inferencia, recalcular métricas, modificar artículo/tesis ni alterar otras fichas.

---

## 1. Refs congelados

Verifica exactamente:

```text
origin/main = 38e22c19a0eb0d344e7675761a88d7968091eead
origin/docs/plan-maestro-temporal-2026-08-31 = 3ba3557eb10e741b8f49c420850940dee1df08ef
origin/docs/fichas-grupos-3-8 = 0542f1b527e14d116e5587e8d5282e4e7799d933
origin/codex/group5-f01-results-presentation-architecture-v01 = 779c07c7865b115e668f8d8f409c0080638f9134
origin/article/main-manuscript = 88a3570fbc8c91af5f06798dcd82e2157121f394
```

Gobernanza:

```text
PROMPT94_SOURCE = 37edbc97610395ef655379628d63f0d8847d117c
PROMPT94_RESPONSE = 9442027fc0d96ee28fe9acd39f5ab473078742a4
PROMPT94_ACTIVATION = b3f861dd04e5778634e585d4c2cebb925fb2c88d
PROMPT94_POSTEXEC_FICHAS = 0542f1b527e14d116e5587e8d5282e4e7799d933
PROMPT94_CANDIDATE_V01 = 779c07c7865b115e668f8d8f409c0080638f9134
V01_PRESENTATION_PLAN_BLOB = 543ad1d71103747bb98ce323873ce14f4377e3e2
V01_TABLE_REGISTRY_BLOB = 6f1d77e584bf4f45cc82f539419c7c6c87e7826a
```

Ficha rectora:

```text
docs/fichas/grupos_3_8/grupo_5/G5_F01_ARQUITECTURA_PRESENTACION_RESULTADOS.md
blob = f55ee2a65c145ef7377c983cef9276f4a77d109e
```

Fuentes que gobiernan la corrección:

```text
outputs/analysis/group3/g3_inferential_results_v0.1.csv
blob = cf3d8d85e099a300330da0214836e70af7a02253

outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
blob = da0351cb523fc7f3b45a83e072765a07f809b7fe
```

Si `main`, Plan, fichas o candidato v01 presentan drift no explicado:

```text
STOP / G5_F01_CORRECTION_REF_DRIFT
```

El artículo es solo lectura. Drift editorial concurrente es advertencia no bloqueante si esta ejecución no lo modifica.

---

## 2. Defecto exacto

En G3-F03, los resultados `G3F03-0001:G3F03-0015` tienen como estimando el **contraste pareado histórico menos comparador**. Sus `point_estimate`, `ci_lower` y `ci_upper` pertenecen a esa diferencia, no al rendimiento absoluto de un brazo.

G4-F01 conserva esta semántica en `G3C-001:G3C-003` como `NONCAUSAL_PAIRED_CONTRAST`.

El candidato G5-F01 v01 define en `G5-MAIN-01`:

```text
required_columns_or_content = ["arm", "metric", "observed estimate", "frozen CI", ...]
```

y el plan humano habla de H100 y tres brazos con “estimación observada y CI”. Esa formulación permite asociar erróneamente el CI de la diferencia a una estimación absoluta por brazo.

La corrección debe eliminar esa ambigüedad antes de materializar cifras en G5-F02.

---

## 3. Contrato correcto para G5-MAIN-01

Mantén su destino, rol, claims y familias:

```text
presentation_id = G5-MAIN-01
presentation_destination = MAIN_TABLE
scientific_role = PRIMARY_INFERENTIAL
claim_ids = G3C-001; G3C-002; G3C-003
evidence_family_ids =
  HE2_A_HISTORICAL_VS_NORMATIVE_FLAT_ATTEMPT06
  HE2_A_HISTORICAL_VS_NORMATIVE_HIERARCHICAL_ATTEMPT06
  HE2_A_HISTORICAL_VS_D1A_ATTEMPT06
```

La estructura futura debe distinguir expresamente:

```text
comparison
metric
historical_observed_value
comparator_observed_value
paired_difference_historical_minus_comparator
frozen_99pct_ci_lower_for_paired_difference
frozen_99pct_ci_upper_for_paired_difference
EVAL_N
DAM_N
source_version
```

Reglas:

1. Los valores absolutos de brazos pueden copiarse únicamente desde fuentes congeladas aprobadas.
2. El `point_estimate` de G3-F03 debe etiquetarse como **diferencia pareada histórico − comparador**.
3. `ci_lower` y `ci_upper` de G3-F03 deben etiquetarse como CI del **mismo contraste pareado**.
4. No presentar esos CI como incertidumbre de `historical_observed_value` ni `comparator_observed_value`.
5. No calcular CI por brazo ni nueva incertidumbre.
6. Mantener 99% para los cinco contrastes primarios HE2_A según G3-F03.
7. Mantener Top-50 separado en `G5-APPENDIX-01` con su semántica suplementaria ya correcta.

El título puede ajustarse de forma puramente documental para hacer explícito el estimando, por ejemplo:

```text
Contrastes primarios HE2_A de ranking temprano
```

No es obligatorio usar literalmente ese título si otra formulación equivalente es más clara.

---

## 4. Correcciones permitidas en los dos artefactos

Usa el v01 como base semántica y modifica únicamente lo necesario para el defecto anterior.

### 4.1 Plan humano

En:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
```

corrige la sección de `G5-MAIN-01` y, si es necesario, reglas generales de incertidumbre para dejar explícito que:

- los valores absolutos por brazo y los contrastes son columnas/conceptos distintos;
- los CI de G3-F03 pertenecen al contraste pareado;
- no existen CI por brazo autorizados por esta ficha si no están materializados en una fuente aprobada.

No cambies los destinos de presentación ni la jerarquía de las demás familias.

### 4.2 Registro JSON

En:

```text
outputs/results/group5/g5_table_registry_v0.1.json
```

corrige exclusivamente `G5-MAIN-01` y los campos globales de validación/trazabilidad necesarios.

Conserva:

```text
PRESENTATION_REGISTRY_COUNT = 16
G5_F02_DEFERRED_MATERIALIZATION_STRUCTURE_COUNT = 9
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
FINAL_NUMERIC_TABLE_MATERIALIZED_COUNT = 0
NEW_METRIC_VALUE_DERIVED_COUNT = 0
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Añade validaciones:

```text
HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0
```

---

## 5. Rama correctiva v02

No modifiques la rama v01.

Crea desde `origin/main`:

```text
branch = codex/group5-f01-results-presentation-architecture-v02
base = 38e22c19a0eb0d344e7675761a88d7968091eead
```

Debe contener exactamente un commit y solo estos dos paths:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
outputs/results/group5/g5_table_registry_v0.1.json
```

Al final:

```text
COMMITS_AHEAD = 1
COMMITS_BEHIND = 0
CHANGED_PATH_COUNT = 2
```

Los artefactos siguen siendo `CANDIDATE_PENDING_EXTERNAL_AUDIT`; no cierres G5-F01 ni Grupo 5.

---

## 6. Guardrails científicos invariables

Debe permanecer exactamente:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Y:

```text
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
G5_F02_STARTED = false
```

No introduzcas números nuevos, no recalcules, no cambies claims ni jerarquía.

---

## 7. Actualización administrativa postcorrección

Después de publicar el candidato v02, actualiza exclusivamente:

```text
branch = docs/fichas-grupos-3-8
base = 0542f1b527e14d116e5587e8d5282e4e7799d933
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Mantén el estado operativo:

```text
G5-F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
G5-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque correctivo con:

```text
FICHA = G5-F01
CORRECTIVE_PROMPT = PROMPT95
CORRECTION_SCOPE = HE2A_ESTIMAND_CI_BINDING_ONLY
SUPERSEDED_CANDIDATE = 779c07c7865b115e668f8d8f409c0080638f9134
CURRENT_CANDIDATE = <v02>
SCIENTIFIC_RECOMPUTATION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP5 = IN_PROGRESS
G5_F02_AUTHORIZED = false
G5_F02_STARTED = false
PENDING_EXTERNAL_AUDIT = true
```

No actualices el Plan Maestro.

---

## 8. Verificación final

Exige:

```text
origin/main = 38e22c19a0eb0d344e7675761a88d7968091eead
origin/docs/plan-maestro-temporal-2026-08-31 = 3ba3557eb10e741b8f49c420850940dee1df08ef

V02_COMMITS_AHEAD = 1
V02_COMMITS_BEHIND = 0
V02_CHANGED_PATH_COUNT = 2

PRESENTATION_REGISTRY_COUNT = 16
G5_F02_DEFERRED_MATERIALIZATION_STRUCTURE_COUNT = 9
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0
FINAL_NUMERIC_TABLE_MATERIALIZED_COUNT = 0
NEW_METRIC_VALUE_DERIVED_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED = false
GROUP5 = IN_PROGRESS
G5_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

---

## 9. Persistencia de respuesta

Crea exclusivamente:

```text
codex_prompts_tmp/95_RESPUESTA_CORREGIR_G5_F01_VINCULO_ESTIMANDO_INCERTIDUMBRE_HE2A.md
```

en `codex/prompts-temporary`.

El commit de respuesta debe añadir únicamente ese archivo.

Reporte terminal mínimo:

```text
PROMPT95 = COMPLETED
PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
V01_CANDIDATE = 779c07c7865b115e668f8d8f409c0080638f9134
V02_BRANCH = codex/group5-f01-results-presentation-architecture-v02
V02_CANDIDATE = ...
V02_PARENT = 38e22c19a0eb0d344e7675761a88d7968091eead
V02_COMMITS_AHEAD = 1
V02_COMMITS_BEHIND = 0
V02_CHANGED_PATH_COUNT = 2
V02_PRESENTATION_PLAN_BLOB = ...
V02_TABLE_REGISTRY_BLOB = ...
HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
POSTCORRECTION_FICHAS_COMMIT = ...
G5_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
G5_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
ARTICLE_HEAD_FINAL_OBSERVED = ...
BLOCKERS = NONE
WARNINGS = ...
```
