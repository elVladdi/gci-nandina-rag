# PROMPT 52 — INTEGRAR CORRECCIÓN F007 Y RECONCILIAR PLAN EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente dos operaciones, en este orden:

1. integrar en `main`, mediante fast-forward exacto, el candidato correctivo F007 v0.2 ya auditado externamente;
2. construir un **candidato separado de reconciliación del Plan Maestro** que registre el estado metodológico vigente de EXP12.

Este bloque **NO ejecuta EXP12**, NO ejecuta retrieval/BM25/Top-k/MRR, NO ejecuta el planeamiento de 10,000 candidatos por seed, NO ingiere nuevas hojas, NO busca ni asume `NUEVA_02`, NO modifica el contrato EXP12 v0.3 y NO abre Grupo 2B ni Grupo 3.

---

# 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt51 concluyó:

```text
PROMPT51_EXTERNAL_AUDIT = PASS / APPROVED_FOR_INTEGRATION

EXP12_F007_CORRECTION_V02 = APPROVED_FOR_INTEGRATION
EXP12_SOURCE_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
EXP12_SOURCE_SCOPE_STATUS = PROSPECTIVELY_CLARIFIED_BY_EXTERNAL_METHODOLOGICAL_DECISION

EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
EXP12_F007 = SOURCE_SCOPE_CLARIFIED_CURRENT_GATE_INSUFFICIENT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED

NEXT_REQUIRED_ACTION = EXP12_NEW_HISTORICAL_GATE_EXTENSION
```

Candidato aprobado:

```text
branch = codex/exp12-f007-source-activation-audit-v02
commit = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
parent = dfd04f0db26383624d54e52bf4fd72f06bbb869c
artifact = outputs/audits/exp12_source_activation_v0.1/exp12_f007_source_activation_audit_v0.2.json
artifact_blob = a585cec8764d2c7648d266d00036a2bcd869cdfb
```

El candidato anterior de Prompt50 permanece rechazado e histórico:

```text
rejected_candidate = ccd10565427a2eb0b938428a68f2b78e538ab144
status = DO_NOT_INTEGRATE
```

No reconstruyas ni reinterpretes el dictamen externo.

---

# 2. Precondiciones Git exactas

Ejecuta `git fetch` y verifica exactamente:

```text
origin/main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
origin/codex/exp12-f007-source-activation-audit-v02 = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/exp12-f007-source-activation-audit-v01 = ccd10565427a2eb0b938428a68f2b78e538ab144
```

Para v0.2 exige:

```text
parent = dfd04f0db26383624d54e52bf4fd72f06bbb869c
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_source_activation_v0.1/exp12_f007_source_activation_audit_v0.2.json
artifact_blob = a585cec8764d2c7648d266d00036a2bcd869cdfb
```

Verifica además:

```text
ccd10565427a2eb0b938428a68f2b78e538ab144 is NOT ancestor of origin/main
ccd10565427a2eb0b938428a68f2b78e538ab144 is NOT ancestor of 2b9571eee76ecffcaef1abc7fd4a12051f76f906
```

Si existe cualquier drift, commit adicional, path adicional o ancestry indebido:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

# 3. Fase A — integración exacta del correctivo F007 v0.2

Trabaja sobre `main` limpio y ejecuta exclusivamente:

```text
dfd04f0db26383624d54e52bf4fd72f06bbb869c
→
2b9571eee76ecffcaef1abc7fd4a12051f76f906
```

mediante `git merge --ff-only` o mecanismo equivalente de fast-forward exacto.

NO uses:

- merge commit;
- squash;
- cherry-pick;
- rebase;
- amend;
- reconstrucción manual del JSON.

Después del push exige:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
```

La integración debe añadir exclusivamente el artefacto v0.2 aprobado. El candidato v0.1 rechazado debe seguir fuera de `main`.

Estado científico después de Fase A:

```text
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_F007_CORRECTION_V02 = INTEGRATED
EXP12_SOURCE_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No ejecutes ninguna comprobación que vuelva a generar ciencia o planeamiento EXP12.

---

# 4. Hechos metodológicos que debe preservar el Plan

El candidato de Plan debe registrar sin reinterpretación los siguientes hechos:

## 4.1 Historial de Prompt50

```text
PROMPT50_PHASE_A_PLAN_INTEGRATION = PASS / APPROVED
PROMPT50_PHASE_B_F007_AUDIT = REJECTED
rejected_candidate = ccd10565427a2eb0b938428a68f2b78e538ab144
rejected_candidate_integrated = false
PROMPT50_DOCUMENTARY_BINDING_RESULT = AMBIGUOUS_UNDER_STRICT_UNIQUE_RULE
PROMPT50_INTERPRETATION_B_PLANNING_GOVERNING = false
PROMPT50_INTERPRETATION_B_PLANNING_CLASSIFICATION = LOCAL_NONRETRIEVAL_NON_GOVERNING_EVIDENCE_FROM_REJECTED_SOURCE_BINDING
```

No borres del registro histórico que Prompt50 realizó ese planeamiento local; clasifícalo correctamente como no gobernante.

## 4.2 Decisión metodológica prospectiva vigente para EXP12

```text
EXP12_SAMPLING_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
H100_ROLE_IN_EXP12 = REFERENCE_LABEL_SET_AND_DISTRIBUTION_ONLY
H100_ROWS_ALLOWED_AS_EXP12_CANDIDATE_SAMPLING_ROWS = false
```

La decisión es prospectiva y específica de EXP12. No modifica ni invalida la construcción H100+incremento ya cerrada de EXP11B.

## 4.3 Fuente actual y bloqueo estructural

Registra:

```text
current_source_path = data/interim/new_historical_gate_v0.1/new_historical_eligible.csv
current_source_sha256 = a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4
current_source_rows = 6029
current_source_dams = 43
current_source_nandina = 56
H100_reference_codes_present = 45
H100_reference_code_count = 66
H100_reference_coverage_upper_bound = 0.6818181818181818
eval_dam_overlap_count = 0
```

El requisito congelado sigue siendo:

```text
required_label_coverage_fraction = 1.0
```

Por tanto:

```text
EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
EXP12_F007 = SOURCE_SCOPE_CLARIFIED_CURRENT_GATE_INSUFFICIENT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Aclara epistemológicamente que los conteos de composición/cobertura fueron recalculados por Codex sobre los artefactos versionados y conservados en el artefacto F007 v0.2; la auditoría externa verificó Git, bindings, consistencia metodológica y estado, pero no reivindica haber reejecutado localmente esa recomputación.

## 4.4 Parámetros que permanecen congelados

No modifiques ni propongas relajar:

```text
target_rows = 2950
max_abs_row_deviation = 148
minimum_rows = 2802
maximum_rows = 3098
preserve_complete_dams = true
seed_schedule = 20262001..20262010
primary_diversity_variable = DAM_CONCENTRATION_HHI
required_label_coverage_fraction = 1.0
maximum_tvd = 0.05
candidate_count_per_seed = 10000
minimum_unique_feasible_candidates = 30
quantiles = 0.10 / 0.50 / 0.90
requires_distinct_dam_sets = true
strict_HHI_order = HHI_DLOW > HHI_DMID > HHI_DHIGH
no_eval_performance_selection = true
```

No declares EXP12 inviable en términos absolutos. La conclusión es únicamente que **la fuente histórica nueva elegible actualmente congelada es insuficiente** para el contrato vigente.

## 4.5 Próxima transición permitida

Registra exactamente:

```text
NEXT_ELIGIBLE_BLOCK = EXP12_NEW_HISTORICAL_GATE_EXTENSION
```

El protocolo histórico contempla prospectivamente `NEW_SHEET_SET_2 = [NUEVA_01, NUEVA_02]`, pero el Plan NO debe afirmar que `NUEVA_02` existe, está disponible, es válida o resolverá la cobertura.

La próxima fase deberá auditar/establecer una ampliación histórica nueva elegible antes de cualquier nuevo planeamiento EXP12.

---

# 5. Fase B — construir candidato de reconciliación del Plan

Parte exactamente de:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
```

Crea una rama nueva:

```text
codex/plan-maestro-exp12-f007-v01
```

Crea **un solo commit** que modifique exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

No integres ese candidato a la rama canónica del Plan durante Prompt52. Debe quedar pendiente de auditoría externa.

El candidato debe:

1. preservar todo el historial existente;
2. añadir la transición Prompt50 → Prompt51 con los estados correctos;
3. registrar que F007 v0.2 está integrado en `main`;
4. registrar el bloqueo estructural 45/66 frente a 66/66 requerido;
5. mantener EXP12 como no autorizado/no ejecutado;
6. fijar `EXP12_NEW_HISTORICAL_GATE_EXTENSION` como próximo bloque elegible;
7. mantener Grupo 2B y Grupo 3 sin iniciar;
8. no introducir resultados, inferencia o interpretación causal nuevos;
9. no convertir la evidencia local de Codex en reejecución independiente de IA Experimental.

---

# 6. Prohibiciones

Durante Prompt52 NO:

- integres el candidato rechazado `ccd105...`;
- modifiques `src/configs/exp12_historical_diversity_control_v0.3.json`;
- crees config v0.4;
- crees autorización EXP12;
- ejecutes EXP12;
- ejecutes `generate_exp12_candidates`;
- ejecutes 10,000 candidatos por seed;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas labels/descripciones EVAL;
- ingieras o busques `NUEVA_02`;
- modifiques Excel;
- rematerialices `new_historical_eligible.csv`;
- modifiques H100, DEV o EVAL;
- modifiques Article;
- abras Grupo 2B o Grupo 3;
- vuelvas a ejecutar EXP11B.

---

# 7. Verificaciones finales obligatorias

Antes de reportar, verifica:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
```

Para el candidato de Plan:

```text
parent = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Verifica además:

```text
EXP12 authorization artifact absent
EXP12 execution outputs absent
EXP12 retrieval invocation count in Prompt52 = 0
EXP12 planning invocation count in Prompt52 = 0
EXP11B reexecution count = 0
NUEVA_02 ingestion count = 0
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

# 8. Persistencia administrativa

Al finalizar, vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/52_RESPUESTA_INTEGRAR_CORRECCION_F007_Y_RECONCILIAR_PLAN_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

# 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT52 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

F007_V02_INTEGRATED = true/false
F007_V02_COMMIT
REJECTED_F007_V01_INTEGRATED = false

PLAN_CANDIDATE_BRANCH
PLAN_CANDIDATE_COMMIT
PLAN_CANDIDATE_PARENT
PLAN_CANDIDATE_CHANGED_PATH_COUNT
PLAN_CANDIDATE_CHANGED_PATH

EXP12_SOURCE_SCOPE
H100_ROLE_IN_EXP12
current_source_rows
current_source_dams
current_source_nandina
H100_reference_codes_present
H100_reference_code_count
H100_reference_coverage_upper_bound

EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY
EXP12_F007
EXP12
NEXT_ELIGIBLE_BLOCK

EXP12_RETRIEVAL_EXECUTED = false
EXP12_PLANNING_EXECUTED = false
EXP12_BM25_EXECUTED = false
EXP12_TOP_K_COMPUTED = false
EXP12_MRR_COMPUTED = false
NUEVA_02_INGESTED = false
EXP11B_REEXECUTED = false
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT52 = COMPLETED
EXP12_F007_CORRECTION_V02 = INTEGRATED
EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
PLAN_RECONCILIATION = CANDIDATE / PENDING_EXTERNAL_AUDIT
NEXT_ELIGIBLE_BLOCK = EXP12_NEW_HISTORICAL_GATE_EXTENSION
```
