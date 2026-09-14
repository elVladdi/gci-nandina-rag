# PROMPT 68 — INTEGRAR EVIDENCIA FORENSE Y RECONCILIAR ESTADO EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto la evidencia auditada del diagnóstico forense one-shot `EXP12_FORENSIC_ATTEMPT_001`;
2. verificar estáticamente los agregados persistidos, sin recomputación;
3. crear un candidato separado de actualización del Plan Maestro que incorpore el resultado forense y delimite estrictamente qué demuestra y qué no demuestra;
4. publicar ese candidato para nueva auditoría externa.

Este bloque **NO ejecuta ningún diagnóstico**, NO reintenta planning, NO ejecuta candidate generation, NO prueba otros seeds ni thresholds, NO modifica contrato/config/runner/datos, NO selecciona condiciones, NO ejecuta retrieval/BM25/Top-k/MRR y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt67 concluye:

```text
PROMPT67_EXTERNAL_AUDIT = PASS / APPROVED

EXP12_FORENSIC_AUTH_002 = INTEGRATED / CONSUMED
EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT / AUDITED
OFFICIAL_FORENSIC_INVOCATION_COUNT = 1
NO_RETRY = true
FORENSIC_RESULT = NON_GOVERNING_FORENSIC_RESULT

FORENSIC_EVIDENCE = APPROVED_FOR_INTEGRATION
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Evidencia aprobada:

```text
branch = codex/exp12-feasibility-forensic-attempt001-evidence-v01
commit = 5787503329afd5ddd5e94d04cdbbdeb000260cda
parent = d9431e71c363d9d6d372e8476d4f2c071dc905b7
commits_ahead = 1
commits_behind = 0
changed_path_count = 5
```

Paths exactos:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_consumption_marker.json
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_execution_report_v0.1.json
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stderr.log
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stdout.log
```

Resultado persistido auditado:

```text
candidate_indices_attempted = 10000
duplicate_dam_set_rejections = 0
eval_overlap_rejections = 0
unique_nonoverlap_candidates = 10000

volume_below_min_count = 1617
volume_within_range_count = 6821
volume_above_max_count = 1562

coverage_pass_count_among_volume_pass = 1
coverage_fail_count_among_volume_pass = 6820

tvd_pass_count_among_volume_pass = 0
tvd_fail_count_among_volume_pass = 6821

coverage_and_tvd_pass_count = 0
coverage_pass_tvd_fail_count = 1
coverage_fail_tvd_pass_count = 0
coverage_and_tvd_fail_count = 6820

final_unique_feasible_count = 0
minimum_required_unique_feasible = 30
historical_failure_condition_reproduced = true
```

La auditoría externa verificó aritméticamente los invariantes sobre esos valores persistidos. No constituye una nueva ejecución ni una recomputación independiente.

### Delimitación interpretativa obligatoria

Los agregados permiten afirmar, exclusivamente para el seed `20262001`, los 10,000 índices congelados y las reglas v0.5:

```text
- deduplicación no eliminó candidatos: 0 / 10000;
- overlap EVAL no eliminó candidatos: 0 / 10000;
- 6821 candidatos únicos quedaron dentro del rango de volumen;
- solo 1 / 6821 pasó cobertura H100=1.0;
- 0 / 6821 pasó TVD<=0.05;
- por tanto, 0 candidatos fueron factibles y el mínimo de 30 no pudo cumplirse;
- el fallo histórico `<30` queda reproducido exactamente como `0<30`.
```

Caracterización permitida:

```text
TVD<=0.05 = UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
COVERAGE_1.0 = NEAR_UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
VOLUME = NOT_SUFFICIENT_EXPLANATION_BY_ITSELF
DEDUPLICATION = NOT_OBSERVED_AS_BOTTLENECK
EVAL_OVERLAP = NOT_OBSERVED_AS_BOTTLENECK
```

No declares que esto pruebe:

- inviabilidad matemática global sobre todos los subconjuntos DAM posibles;
- comportamiento de otros seeds;
- que un threshold alternativo sea científicamente correcto;
- que deba relajarse TVD o cobertura;
- que el resultado forense reemplace el Attempt001 oficial;
- que exista autorización para un nuevo planning o retrieval.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = d9431e71c363d9d6d372e8476d4f2c071dc905b7
origin/codex/exp12-feasibility-forensic-attempt001-evidence-v01 = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para la evidencia exige:

```text
parent = d9431e71c363d9d6d372e8476d4f2c071dc905b7
commits_ahead = 1
commits_behind = 0
changed_path_count = 5
```

y exactamente los cinco paths de §1.

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta de la evidencia forense

Integra exclusivamente:

```text
d9431e71c363d9d6d372e8476d4f2c071dc905b7
→
5787503329afd5ddd5e94d04cdbbdeb000260cda
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 4. Fase B — verificación READ-ONLY sin recomputación

Desde el `main` integrado lee íntegramente únicamente:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_consumption_marker.json
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_execution_report_v0.1.json
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stdout.log
outputs/audits/exp12_planning_gate_v0.4/exp12_feasibility_forensic_attempt_001_stderr.log
```

No ejecutes módulo, runner, tests ni datasets.

Verifica estáticamente:

```text
authorization_id = EXP12_FORENSIC_AUTH_002
diagnostic_attempt_id = EXP12_FORENSIC_ATTEMPT_001
marker_status = CONSUMED_EXECUTION_STARTED
official_forensic_invocation_count = 1
exit_code = 0
terminal_status = COMPLETED_ONE_SHOT / PENDING_EXTERNAL_AUDIT
forensic_non_governing = true
condition_selection_performed = false
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
```

Revalida únicamente por aritmética de los valores persistidos:

```text
10000 = 0 + 0 + 10000
10000 = 1617 + 6821 + 1562
6821 = 0 + 1 + 0 + 6820
6821 = 1 + 6820
6821 = 0 + 6821
0 = coverage_and_tvd_pass_count
0 < 30
```

No calcules candidatos ni leas datos fuente.

---

## 5. Fase C — candidato de reconciliación del Plan Maestro

Crea desde exactamente:

```text
5a3df4c2665ac5d1b57f7ef19b800d39758e6920
```

la rama nueva:

```text
codex/plan-maestro-exp12-forensic-result-v01
```

Modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Un solo commit.

### 5.1 Estado vigente obligatorio

Actualiza el estado vigente y el orden maestro para reflejar:

```text
main = origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda

EXP12_FORENSIC_AUTH_001 = REJECTED_PREEXECUTION / NOT_INTEGRATED
EXP12_FORENSIC_AUTH_002 = INTEGRATED / CONSUMED
EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_FORENSIC_RESULT = NON_GOVERNING_FORENSIC_RESULT
OFFICIAL_FORENSIC_INVOCATION_COUNT = 1

EXP12_FORENSIC_CANDIDATE_INDICES_ATTEMPTED = 10000
EXP12_FORENSIC_DUPLICATE_REJECTIONS = 0
EXP12_FORENSIC_EVAL_OVERLAP_REJECTIONS = 0
EXP12_FORENSIC_UNIQUE_NONOVERLAP = 10000
EXP12_FORENSIC_VOLUME_BELOW = 1617
EXP12_FORENSIC_VOLUME_WITHIN = 6821
EXP12_FORENSIC_VOLUME_ABOVE = 1562
EXP12_FORENSIC_COVERAGE_PASS = 1
EXP12_FORENSIC_COVERAGE_FAIL = 6820
EXP12_FORENSIC_TVD_PASS = 0
EXP12_FORENSIC_TVD_FAIL = 6821
EXP12_FORENSIC_FINAL_UNIQUE_FEASIBLE = 0
EXP12_FORENSIC_MINIMUM_REQUIRED = 30
EXP12_FORENSIC_HISTORICAL_FAILURE_REPRODUCED = true
```

Registra la caracterización limitada:

```text
EXP12_FORENSIC_TVD_CHARACTERIZATION = UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
EXP12_FORENSIC_COVERAGE_CHARACTERIZATION = NEAR_UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
EXP12_FORENSIC_GLOBAL_INFEASIBILITY_PROVEN = false
EXP12_FORENSIC_OTHER_SEEDS_CHARACTERIZED = false
```

Preserva:

```text
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_PLANNING_RETRY = PROHIBITED_UNDER_AUTH_001
EXP12_PLANNING_OFFICIAL_CONDITIONS = NOT_SELECTED
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B = NOT_STARTED
GROUP3 = NOT_STARTED
```

El siguiente bloque debe quedar como:

```text
NEXT_ELIGIBLE_BLOCK = EXP12_POST_FAILURE_METHODOLOGICAL_DISPOSITION
```

No definas aún una nueva versión del experimento, no cambies thresholds y no declares cerrado EXP12 en este bloque.

### 5.2 Historia y fecha

Conserva íntegramente la historia previa, incluyendo Prompt61–Prompt67, la autorización forense v0.1 rechazada, la corrección v0.2 y el carácter no gobernante del diagnóstico.

Mantén:

```text
Fecha de actualización = 2026-09-14
```

Añade una entrada cronológica de `2026-09-14` para el diagnóstico forense de Prompt67.

---

## 6. Prohibiciones absolutas

Durante Prompt68 NO:

- ejecutes diagnóstico forense;
- ejecutes `generate_exp12_candidates`;
- ejecutes planning oficial;
- pruebes otros seeds;
- pruebes thresholds alternativos;
- calcules escenarios what-if;
- cambies TVD, cobertura, volumen, candidate_count, minimum feasible, seeds o quantiles;
- selecciones D-HIGH/D-MID/D-LOW;
- modifiques módulo/protocolo/config/tests/datasets;
- ejecutes retrieval/BM25/Top-k/MRR;
- autorices retrieval EXP12;
- cierres EXP12 definitivamente;
- abras una nueva autorización de planning;
- avances a Grupo 2B o Grupo 3;
- modifiques Article.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

La rama canónica del Plan NO se mueve todavía.

Para el candidato del Plan exige:

```text
parent = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Confirma:

```text
FORENSIC_DIAGNOSTIC_REEXECUTED = false
EXP12_PLANNING_REEXECUTED = false
OTHER_SEEDS_TESTED = false
ALTERNATIVE_THRESHOLDS_TESTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_RETRIEVAL_AUTHORIZED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 8. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/68_RESPUESTA_INTEGRAR_EVIDENCIA_FORENSE_Y_RECONCILIAR_ESTADO_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT68 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_final

FORENSIC_EVIDENCE_INTEGRATED
INTEGRATION_MODE

AUTHORIZATION_ID
DIAGNOSTIC_ATTEMPT_ID
MARKER_STATUS
OFFICIAL_FORENSIC_INVOCATION_COUNT
EXIT_CODE
TERMINAL_STATUS

CANDIDATE_INDICES_ATTEMPTED
DUPLICATE_DAM_SET_REJECTIONS
EVAL_OVERLAP_REJECTIONS
UNIQUE_NONOVERLAP_CANDIDATES
VOLUME_BELOW_MIN_COUNT
VOLUME_WITHIN_RANGE_COUNT
VOLUME_ABOVE_MAX_COUNT
COVERAGE_PASS_COUNT_AMONG_VOLUME_PASS
COVERAGE_FAIL_COUNT_AMONG_VOLUME_PASS
TVD_PASS_COUNT_AMONG_VOLUME_PASS
TVD_FAIL_COUNT_AMONG_VOLUME_PASS
FINAL_UNIQUE_FEASIBLE_COUNT
MINIMUM_REQUIRED_UNIQUE_FEASIBLE
HISTORICAL_FAILURE_CONDITION_REPRODUCED

FORENSIC_TVD_CHARACTERIZATION
FORENSIC_COVERAGE_CHARACTERIZATION
GLOBAL_INFEASIBILITY_PROVEN = false
OTHER_SEEDS_CHARACTERIZED = false

PLAN_CANDIDATE_BRANCH
PLAN_CANDIDATE_COMMIT
PLAN_CANDIDATE_PARENT
PLAN_CANDIDATE_CHANGED_PATH_COUNT
PLAN_CANDIDATE_PUBLISHED

NEXT_ELIGIBLE_BLOCK = EXP12_POST_FAILURE_METHODOLOGICAL_DISPOSITION
FORENSIC_DIAGNOSTIC_REEXECUTED = false
EXP12_PLANNING_REEXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT68 = COMPLETED
EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_FORENSIC_FINAL_UNIQUE_FEASIBLE = 0
NEXT_ELIGIBLE_BLOCK = EXP12_POST_FAILURE_METHODOLOGICAL_DISPOSITION
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```
