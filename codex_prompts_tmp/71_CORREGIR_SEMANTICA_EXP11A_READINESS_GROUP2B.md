# PROMPT 71 — CORREGIR SEMÁNTICA EXP11A EN READINESS DE GRUPO 2B

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque corrige exclusivamente dos inexactitudes documentales detectadas por auditoría externa en el candidato de readiness de Grupo 2B generado por Prompt70. No cambia el estado científico, no modifica el cierre de EXP12 y no ejecuta ningún experimento, pipeline, test científico, retrieval, BM25, Top-k, MRR, planning, candidate generation ni regeneración de artefactos.

El candidato v0.1 de readiness **no debe integrarse**. Debe preservarse como evidencia histórica de la revisión y ser sustituido por un candidato v0.2 construido desde el `main` científico canónico.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt70 concluye:

```text
PROMPT70_EXTERNAL_AUDIT = PASS_WITH_MINOR_DOCUMENTARY_CORRECTION_REQUIRED

PLAN_EXP12_CLOSURE_INTEGRATED = true
GROUP2B_READINESS_V01 = REJECTED_FOR_INTEGRATION / SUPERSEDED_PENDING_V02
SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
GROUP2B_CLOSED = false
GROUP3_STARTED = false
```

El paquete v0.1 publicado es:

```text
branch = codex/group2b-reproducibility-readiness-v01
commit = 26b64db898b96ef1225d6f238bedc44ffaa87823
parent = 5787503329afd5ddd5e94d04cdbbdeb000260cda
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
```

Paths v0.1:

```text
docs/group2b_reproducibility_traceability_readiness_v0.1.md
outputs/audits/group2b_reproducibility_readiness_v0.1.json
```

La auditoría externa verificó que el paquete es sustantivamente consistente en su inventario, ausencia propuesta de gaps bloqueantes y carácter READ-ONLY, pero contiene dos errores semánticos sobre EXP11A que deben corregirse antes de cualquier decisión de cierre de Grupo 2B.

---

## 2. Hallazgos documentales obligatorios

### G2B-RD-F001 — diseño EXP11A mal descrito

En `end_to_end_matrix` v0.1 aparece:

```text
EXP11A.config_contract = nested complete-DAM design
```

Eso es incorrecto para el diseño final ejecutado.

La fuente versionada `docs/g2a_contract_exp11_exp12_v0.1.md` establece que H25, H50 y H75 usan **subconjuntos completos de DAM independientes** y que el nesting quedó `NOT_REQUIRED_STRUCTURALLY_INFEASIBLE`. H50 usa el diseño corregido estratificado D1/D2.

La descripción correcta debe reflejar, sin introducir nomenclatura nueva:

```text
independent complete-DAM conditions; H50 paired D1/D2 stratification; nesting not required / structurally infeasible
```

No describas EXP11A como diseño nested ejecutado.

### G2B-RD-F002 — seeds EXP11A descritos con alcance excesivo

En v0.1 se afirma de forma general que H25/H50/H75/H100 preservan seeds `20261001..20261010`.

El run manifest versionado:

```text
outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_run_manifest.json
```

establece exactamente:

```text
H25 = 10 runs, seeds 20261001..20261010
H50 = 10 runs formados por 5 paired seeds 20261001..20261005,
      cada paired seed produce una corrida D1 y una D2
H75 = 10 runs, seeds 20261001..20261010
H100 = frozen reference / seed not applicable
```

Corrige tanto el Markdown como `seed_and_parameter_status.EXP11A` en el JSON para reflejar exactamente esa distribución.

---

## 3. Precondiciones Git exactas

Ejecuta `git fetch` y exige:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/group2b-reproducibility-readiness-v01 = 26b64db898b96ef1225d6f238bedc44ffaa87823
```

Para v0.1 exige:

```text
parent = 5787503329afd5ddd5e94d04cdbbdeb000260cda
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
changed_paths =
  docs/group2b_reproducibility_traceability_readiness_v0.1.md
  outputs/audits/group2b_reproducibility_readiness_v0.1.json
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 4. Verificación READ-ONLY de las dos correcciones

Lee únicamente, sin ejecutar scripts/tests/pipelines:

```text
docs/g2a_contract_exp11_exp12_v0.1.md
outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_run_manifest.json
docs/group2b_reproducibility_traceability_readiness_v0.1.md
outputs/audits/group2b_reproducibility_readiness_v0.1.json
```

Verifica estáticamente F001 y F002.

No recalcules métricas, hashes científicos, composiciones ni resultados.

---

## 5. Crear readiness v0.2 desde main canónico

Desde exactamente:

```text
5787503329afd5ddd5e94d04cdbbdeb000260cda
```

crea la rama:

```text
codex/group2b-reproducibility-readiness-v02
```

Un solo commit que añada exclusivamente:

```text
docs/group2b_reproducibility_traceability_readiness_v0.2.md
outputs/audits/group2b_reproducibility_readiness_v0.2.json
```

No integres v0.1 a `main`.
No modifiques archivos existentes.

### 5.1 Regla de contenido

Usa v0.1 únicamente como base documental y conserva todas las partes que continúen siendo válidas. Aplica exclusivamente las correcciones F001 y F002, además de los cambios mínimos de identidad de versión necesarios:

```text
version = v0.2
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
supersedes_candidate_commit = 26b64db898b96ef1225d6f238bedc44ffaa87823
supersession_reason = EXP11A_DOCUMENTARY_SEMANTIC_CORRECTION
```

Si estos campos no encajan en el Markdown, regístralos en una breve nota de supersesión; en el JSON sí deben quedar explícitos.

No alteres, salvo consecuencia puramente textual de F001/F002:

- `artifact_inventory`;
- los 35 `identity_checks`;
- sus expected/observed hashes;
- las 11 filas de la matriz;
- `blocking_gaps=[]`;
- las 11 limitaciones no bloqueantes;
- los 5 historical-only items;
- environment/clean-checkout classifications;
- summary counts;
- proposed next block.

Los conteos esperados permanecen:

```text
artifact_inventory_count = 47
identity_check_count = 35
identity_check_pass_count = 31
identity_check_nonpass_count = 4
end_to_end_matrix_row_count = 11
complete_row_count = 1
complete_with_declared_limitation_row_count = 10
partial_nonblocking_row_count = 0
blocking_gap_row_count = 0
not_applicable_row_count = 0
blocking_gap_count = 0
nonblocking_limitation_count = 11
historical_only_count = 5
```

### 5.2 Texto EXP11A requerido

La fila EXP11A de `end_to_end_matrix` debe describir el contrato final de forma equivalente a:

```text
independent complete-DAM conditions; H50 paired D1/D2 stratification; nesting not required / structurally infeasible
```

El estado de seeds/params EXP11A debe ser equivalente a:

```text
H25: 10 runs, seeds 20261001..20261010
H50: 10 runs from paired seeds 20261001..20261005, 5 D1 + 5 D2
H75: 10 runs, seeds 20261001..20261010
H100: frozen reference, seed not applicable
```

El Markdown debe expresar lo mismo sin ambigüedad.

---

## 6. Verificaciones finales

Exige:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para v0.2 exige:

```text
parent = 5787503329afd5ddd5e94d04cdbbdeb000260cda
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
changed_paths =
  docs/group2b_reproducibility_traceability_readiness_v0.2.md
  outputs/audits/group2b_reproducibility_readiness_v0.2.json
```

Confirma:

```text
G2B-RD-F001 = RESOLVED
G2B-RD-F002 = RESOLVED
GROUP2B_READINESS_V01 = REJECTED_FOR_INTEGRATION / SUPERSEDED_BY_V02_CANDIDATE
GROUP2B_READINESS_V02 = CANDIDATE_PENDING_EXTERNAL_AUDIT
SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
GROUP2B_CLOSED = false
EXP12_REOPENED = false
GROUP3_STARTED = false
```

---

## 7. Prohibiciones absolutas

Durante Prompt71 NO:

- integres v0.1 a main;
- modifiques main, Plan o Article;
- ejecutes experimentos, pipelines o tests científicos;
- recalcules resultados, métricas, candidate rankings, hashes científicos o composiciones;
- regeneres datasets, manifests, logs, case-level o resultados;
- reconstruyas assets local-only;
- cambies la clasificación de gaps/limitaciones salvo que F001/F002 obliguen lógicamente a ello (no deberían);
- reabras EXP12;
- cierres Grupo 2B;
- avances a Grupo 3.

---

## 8. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/71_RESPUESTA_CORREGIR_SEMANTICA_EXP11A_READINESS_GROUP2B.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT71 = COMPLETED | STOP

main_final
plan_final
article_final

G2B_RD_F001
G2B_RD_F002

GROUP2B_V01_COMMIT
GROUP2B_V01_INTEGRATED_TO_MAIN
GROUP2B_V01_STATUS

GROUP2B_V02_BRANCH
GROUP2B_V02_COMMIT
GROUP2B_V02_PARENT
GROUP2B_V02_COMMITS_AHEAD
GROUP2B_V02_COMMITS_BEHIND
GROUP2B_V02_CHANGED_PATH_COUNT
GROUP2B_V02_CHANGED_PATHS
GROUP2B_V02_PUBLISHED

ARTIFACT_INVENTORY_COUNT
IDENTITY_CHECK_COUNT
IDENTITY_CHECK_PASS_COUNT
IDENTITY_CHECK_NONPASS_COUNT
END_TO_END_MATRIX_ROW_COUNT
BLOCKING_GAP_COUNT
NONBLOCKING_LIMITATION_COUNT
HISTORICAL_ONLY_COUNT

SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
GROUP2B_CLOSED = false
EXP12_REOPENED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT71 = COMPLETED
G2B-RD-F001 = RESOLVED
G2B-RD-F002 = RESOLVED
GROUP2B_READINESS_V01 = REJECTED_FOR_INTEGRATION / SUPERSEDED_BY_V02_CANDIDATE
GROUP2B_READINESS_V02 = CANDIDATE_PENDING_EXTERNAL_AUDIT
SCIENTIFIC_EXECUTION_PERFORMED = false
GROUP2B_CLOSED = false
GROUP3_STARTED = false
```
