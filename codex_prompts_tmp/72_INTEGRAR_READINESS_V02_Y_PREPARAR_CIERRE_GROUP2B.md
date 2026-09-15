# PROMPT 72 — INTEGRAR READINESS v0.2 Y PREPARAR CIERRE DE GRUPO 2B

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente:

1. integrar mediante fast-forward exacto el readiness de Grupo 2B v0.2 ya auditado externamente;
2. materializar un **candidato versionado de cierre de Grupo 2B** que preserve las limitaciones no bloqueantes y los elementos históricos identificados;
3. crear un candidato separado de actualización del Plan Maestro que cierre Grupo 2B y deje Grupo 3 como siguiente bloque elegible;
4. publicar ambos candidatos para auditoría externa.

Este bloque **NO ejecuta** experimentos, pipelines, tests científicos, retrieval, BM25, Top-k, MRR, planning, candidate generation, inferencia, regeneración de datasets, manifests, resultados, logs o case-level. No reabre EXP12 y no inicia Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt71 concluye:

```text
PROMPT71_EXTERNAL_AUDIT = PASS / APPROVED

G2B-RD-F001 = RESOLVED
G2B-RD-F002 = RESOLVED

GROUP2B_READINESS_V01 = REJECTED_FOR_INTEGRATION / SUPERSEDED_BY_V02
GROUP2B_READINESS_V02 = APPROVED_FOR_INTEGRATION

GROUP2B_BLOCKING_GAP_COUNT = 0
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_HISTORICAL_ONLY_COUNT = 5
ENVIRONMENT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
CLEAN_CHECKOUT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION

SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
GROUP2B_CLOSED = false
GROUP3_STARTED = false
```

Candidato readiness v0.2 aprobado:

```text
branch = codex/group2b-reproducibility-readiness-v02
commit = fbd321d817d22fef78417064e0d5bc8df37165ca
parent = 5787503329afd5ddd5e94d04cdbbdeb000260cda
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
changed_paths =
  docs/group2b_reproducibility_traceability_readiness_v0.2.md
  outputs/audits/group2b_reproducibility_readiness_v0.2.json
```

Estado canónico previo:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 2. Decisión externa de cierre propuesta

IA Experimental determina que el readiness v0.2 no contiene gaps bloqueantes para Grupo 2B. Las limitaciones históricas y local-only ya delimitadas permanecen visibles y no deben reinterpretarse como resueltas.

La disposición que debe materializarse como **candidata pendiente de auditoría de implementación** es:

```text
GROUP2B_DISPOSITION = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP2B_BLOCKING_GAP_COUNT = 0
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_HISTORICAL_ONLY_COUNT = 5
ENVIRONMENT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
CLEAN_CHECKOUT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
GROUP2B_SCIENTIFIC_REEXECUTION_REQUIRED = false
GROUP2B_RESULTS_RECOMPUTATION_REQUIRED = false
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
```

Este cierre **no** significa reproducibilidad perfecta ni recuperación de activos declarados no recuperables/local-only. Significa que, según la evidencia versionada auditada, no queda una brecha de reproducibilidad/trazabilidad clasificada como bloqueante para continuar al análisis cuantitativo.

---

## 3. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/codex/group2b-reproducibility-readiness-v02 = fbd321d817d22fef78417064e0d5bc8df37165ca
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para readiness v0.2 exige:

```text
parent = 5787503329afd5ddd5e94d04cdbbdeb000260cda
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 4. Fase A — integrar readiness v0.2 a main

Integra exclusivamente mediante fast-forward exacto:

```text
5787503329afd5ddd5e94d04cdbbdeb000260cda
→
fbd321d817d22fef78417064e0d5bc8df37165ca
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = fbd321d817d22fef78417064e0d5bc8df37165ca
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 5. Fase B — candidato de cierre versionado de Grupo 2B

Desde exactamente:

```text
fbd321d817d22fef78417064e0d5bc8df37165ca
```

crea la rama:

```text
codex/group2b-reproducibility-closure-v01
```

Un solo commit que añada exclusivamente:

```text
outputs/audits/group2b_reproducibility_closure_v0.1.json
```

El JSON debe contener como mínimo:

```text
artifact = GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE
version = v0.1
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
readiness_version = v0.2
readiness_commit = fbd321d817d22fef78417064e0d5bc8df37165ca
scientific_main_commit = fbd321d817d22fef78417064e0d5bc8df37165ca
canonical_plan_commit_before_closure = 0c77e86359bcd17ddd446429f21b62174c426f37
article_commit = 254b1e6df736fa9938ac86a515d65b36f4d361c5

group2b_disposition = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
blocking_gap_count = 0
nonblocking_limitation_count = 11
historical_only_count = 5
environment_reproducibility = COMPLETE_WITH_DECLARED_LIMITATION
clean_checkout_reproducibility = COMPLETE_WITH_DECLARED_LIMITATION
scientific_reexecution_required = false
results_recomputation_required = false
exp12_reopened = false
group3_started = false
next_eligible_block = GROUP3_METRICS_AND_INFERENCE
```

Debe referenciar, sin duplicar ni reinterpretar, las 11 limitaciones no bloqueantes y 5 historical-only items del readiness v0.2.

No declares que assets local-only hayan sido versionados ni que hallazgos `DECLARED_NOT_RECOVERABLE` se hayan recuperado.

---

## 6. Fase C — candidato de reconciliación del Plan Maestro

Desde exactamente:

```text
0c77e86359bcd17ddd446429f21b62174c426f37
```

crea la rama:

```text
codex/plan-maestro-group2b-closure-v01
```

Modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Un solo commit.

### 6.1 Estado obligatorio

Actualiza el Plan para reflejar coherentemente:

```text
main = origin/main = fbd321d817d22fef78417064e0d5bc8df37165ca
GROUP2B_READINESS_V02 = AUDITED / APPROVED / INTEGRATED
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP2B_BLOCKING_GAP_COUNT = 0
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_HISTORICAL_ONLY_COUNT = 5
ENVIRONMENT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
CLEAN_CHECKOUT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
GROUP2B_SCIENTIFIC_REEXECUTION_REQUIRED = false
GROUP2B_RESULTS_RECOMPUTATION_REQUIRED = false
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
```

La fila global `2. Reproducibilidad y trazabilidad` debe dejar de estar `EN CURSO` y pasar a un estado equivalente a:

```text
CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
```

Preserva explícitamente las limitaciones históricas ya aceptadas y la disposición final de EXP12. No simplifiques el historial de forma que parezca reproducibilidad perfecta.

### 6.2 Orden maestro

El tramo final debe quedar conceptualmente:

```text
EXP12 Original Frozen Design ✅ CLOSED_WITHOUT_RETRIEVAL
  ↓
Grupo 2B — Reproducibilidad y trazabilidad ✅ CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
  ↓
Grupo 3 — Métricas e inferencia ⏳ NEXT
  ↓
Grupos 4–8
```

No marques Grupo 3 como iniciado.

### 6.3 Historia y fecha

Mantén `Fecha de actualización = 2026-09-14` salvo que la ejecución ocurra después de esa fecha UTC/local; en ese caso usa la fecha real de ejecución.

Añade una entrada cronológica de cierre de Grupo 2B que indique:

- readiness v0.1 rechazado solo por F001/F002 documentales;
- readiness v0.2 corrigió ambos hallazgos;
- 47 artefactos inventariados;
- 35 identity checks: 31 pass-equivalent y 4 `HASH_BOUND_LOCAL_ONLY`/no mismatch;
- 11 cadenas end-to-end: 1 `COMPLETE`, 10 `COMPLETE_WITH_DECLARED_LIMITATION`;
- 0 gaps bloqueantes;
- 11 limitaciones no bloqueantes;
- 5 historical-only;
- no reejecución científica ni recomputación requerida.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = fbd321d817d22fef78417064e0d5bc8df37165ca
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

La rama canónica del Plan NO se mueve todavía.

Para cierre Group2B exige:

```text
parent = fbd321d817d22fef78417064e0d5bc8df37165ca
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/group2b_reproducibility_closure_v0.1.json
```

Para candidato Plan exige:

```text
parent = 0c77e86359bcd17ddd446429f21b62174c426f37
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Confirma:

```text
SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
EXP12_REOPENED = false
GROUP3_STARTED = false
```

---

## 8. Prohibiciones absolutas

Durante Prompt72 NO:

- ejecutes experimentos/pipelines/tests científicos;
- ejecutes retrieval/BM25/Top-k/MRR;
- regeneres resultados, datasets, manifests, logs o case-level;
- reconstruyas assets local-only;
- cambies hashes o clasificaciones del readiness v0.2;
- declares recuperados los elementos `DECLARED_NOT_RECOVERABLE`;
- reabras EXP12;
- modifiques Article;
- integres aún el candidato de cierre Group2B a main;
- integres aún el candidato del Plan;
- inicies Grupo 3.

---

## 9. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/72_RESPUESTA_INTEGRAR_READINESS_V02_Y_PREPARAR_CIERRE_GROUP2B.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 10. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT72 = COMPLETED | STOP

main_initial
main_final
plan_final
article_final
READINESS_V02_INTEGRATED

GROUP2B_CLOSURE_BRANCH
GROUP2B_CLOSURE_COMMIT
GROUP2B_CLOSURE_PARENT
GROUP2B_CLOSURE_CHANGED_PATH_COUNT
GROUP2B_CLOSURE_PUBLISHED

PLAN_CANDIDATE_BRANCH
PLAN_CANDIDATE_COMMIT
PLAN_CANDIDATE_PARENT
PLAN_CANDIDATE_CHANGED_PATH_COUNT
PLAN_CANDIDATE_PUBLISHED

GROUP2B_DISPOSITION
BLOCKING_GAP_COUNT
NONBLOCKING_LIMITATION_COUNT
HISTORICAL_ONLY_COUNT
ENVIRONMENT_REPRODUCIBILITY
CLEAN_CHECKOUT_REPRODUCIBILITY
SCIENTIFIC_REEXECUTION_REQUIRED
RESULTS_RECOMPUTATION_REQUIRED
NEXT_ELIGIBLE_BLOCK

SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
EXP12_REOPENED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT72 = COMPLETED
GROUP2B_CLOSURE = CANDIDATE_PENDING_EXTERNAL_AUDIT
PLAN_GROUP2B_CLOSURE = CANDIDATE_PENDING_EXTERNAL_AUDIT
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
SCIENTIFIC_EXECUTION_PERFORMED = false
GROUP3_STARTED = false
```
