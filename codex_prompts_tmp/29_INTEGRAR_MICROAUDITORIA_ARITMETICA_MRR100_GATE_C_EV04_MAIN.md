# PROMPT 29 — INTEGRAR MICROAUDITORÍA ARITMÉTICA MRR@100 GATE C / EV04 A `main`

## 0. Rol y alcance

Actúa exclusivamente como **ejecutor de integración Git controlada** del artefacto científico ya auditado externamente de la microauditoría aritmética MRR@100 de Gate C / EV04.

Este bloque es **solo integración**.

Queda expresamente prohibido:

- repetir la microauditoría aritmética;
- ejecutar retrieval;
- construir índices;
- ejecutar EV03;
- ejecutar EV04 real;
- ejecutar D1a;
- ejecutar EVAL real;
- ejecutar inferencia del modelo;
- construir v0.4;
- modificar el productor v0.3;
- debilitar `PASS_EXACT`;
- introducir tolerancias, redondeos o escalares hardcodeados;
- crear autorización v0.4;
- autorizar o ejecutar Attempt05;
- decidir todavía si `.77` o `.78` será la referencia prospectiva;
- modificar el Plan Maestro canónico;
- modificar la rama del artículo;
- tocar EXP11B o EXP12.

No avances a ningún bloque posterior.

---

## 1. Repositorio y referencias obligatorias

Repositorio:

`elVladdi/gci-nandina-rag`

### Baseline científico que debe existir antes de integrar

`origin/main = 6187ca29357c42c43675fb8e5ffdacbb4705ee83`

### Candidato científico aprobado externamente

Rama:

`codex/0b05c-ev04-mrr100-arithmetic-provenance-v03`

Commit exacto:

`ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`

Parent exacto:

`6187ca29357c42c43675fb8e5ffdacbb4705ee83`

Tree exacto:

`401ee00fa621e2f084278ef5bf5ee5b8d7771fd2`

Único path científico del candidato:

`outputs/audits/0b05c_ev04_gatec_mrr100_arithmetic_provenance_v0.3/ev04_gatec_mrr100_arithmetic_provenance_v0.3.json`

Git blob SHA-1 exacto del artefacto:

`c3667f85b4f8ec51f026e2e3b706062da586a7f1`

### Referencias que deben permanecer intactas

Plan Maestro:

`docs/plan-maestro-temporal-2026-08-31 = fe847f708d4d1ded92b5a50a38d4913bb69ed311`

Artículo:

`article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`

---

## 2. Preflight Git obligatorio y fail-closed

Antes de integrar:

1. `git fetch --all --prune`.
2. Verifica que `origin/main` sea exactamente `6187ca29357c42c43675fb8e5ffdacbb4705ee83`.
3. Verifica que la rama candidata remota apunte exactamente a `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`.
4. Verifica parent y tree exactos del candidato.
5. Verifica que el merge-base entre baseline y candidato sea exactamente el baseline.
6. Verifica que el candidato esté exactamente `1 ahead / 0 behind` respecto del baseline.
7. Verifica que exista exactamente **1 commit** entre baseline y candidato.
8. Verifica que exista exactamente **1 changed path**, y que sea únicamente el artefacto indicado arriba.
9. Verifica el Git blob SHA-1 exacto `c3667f85b4f8ec51f026e2e3b706062da586a7f1`.
10. Verifica que Plan Maestro y artículo continúen en sus SHAs exactos.

Si cualquier identidad difiere: **STOP / FAIL_CLOSED / NO INTEGRAR**.

---

## 3. Verificación read-only mínima del artefacto antes de integrar

Lee el JSON candidato sin modificarlo y confirma exactamente:

- `artifact_id = 0b05c_ev04_gatec_mrr100_arithmetic_provenance_v0.3`
- `baseline_commit = 6187ca29357c42c43675fb8e5ffdacbb4705ee83`
- `case_count = 1056`
- `causal_classification = HISTORICAL_ARITHMETIC_PATH_NOT_RECOVERED`
- `v04_recovery_readiness = NOT_READY_NEEDS_METHODOLOGICAL_DECISION`
- `attempt05_authorized = false`
- `metric_impact = NOT_DETERMINED`
- `closure = NOT_AUTHORIZED`
- `source_bindings_all_match_expected = true`
- `environment_exact_match = false`
- `mrr100_numeric_matching_routes = []`
- `historical_provenance_supported_routes = []`
- coexistencia versionada `.77/.78` con `coexistence_ulp_distance = 1`
- `pass_exact_weakened = false`
- `tolerance_or_rounding_introduced = false`
- `v0_4_built = false`
- `v0_4_authorization_created = false`

Confirma también que el propio artefacto diferencia explícitamente:

- hechos Git/versionados reproducibles;
- reproducción aritmética local de CODEX;
- ausencia de evidencia de GitHub CI usada para validar dicha reproducción local.

No conviertas los cálculos locales de CODEX en evidencia independiente de CI.

---

## 4. Integración permitida

Si y solo si todo el preflight pasa:

1. Sitúate sobre `main` sincronizado con `origin/main`.
2. Integra el candidato mediante **fast-forward only**.
3. El resultado de `main` debe ser exactamente el commit candidato:

`ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`

4. Haz push normal de `main`.

### Prohibiciones Git

No usar:

- merge commit;
- squash;
- cherry-pick;
- rebase;
- amend;
- force push;
- regeneración del artefacto;
- edición de archivos durante la integración;
- commit adicional sobre `main`.

La integración debe preservar exactamente el objeto científico ya auditado.

---

## 5. Validación post-integración obligatoria

Después del push verifica:

- `origin/main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`
- tree de `main = 401ee00fa621e2f084278ef5bf5ee5b8d7771fd2`
- rama candidata y `main` apuntan al mismo commit;
- diff candidato vs `origin/main` vacío;
- baseline antiguo → nuevo `main` = `1 ahead / 0 behind`;
- exactamente 1 commit integrado;
- exactamente 1 changed path integrado;
- path exacto del artefacto;
- blob exacto `c3667f85b4f8ec51f026e2e3b706062da586a7f1`;
- Plan Maestro permanece en `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- artículo permanece en `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Verifica además que **no** aparezcan en este bloque:

- cambios al failure record de Attempt04;
- cambios al gate/specs/authorization record v0.3;
- outputs runtime parciales de Attempt04;
- código v0.4;
- gate/specs v0.4;
- autorización v0.4;
- autorización o ejecución de Attempt05;
- decisión prospectiva `.77` vs `.78`;
- cambios al Plan/artículo/EXP11B/EXP12.

---

## 6. Estado científico que debe preservarse

Al terminar, reporta sin reinterpretar:

```text
GROUP_2 = EN_CURSO

0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED

0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04

EV04_ATTEMPT04_STATIC_DIAGNOSIS = VERSIONED / INTEGRATED

EV04_GATEC_MRR100_ARITHMETIC_PROVENANCE_AUDIT = VERSIONED / INTEGRATED

EV04_GATEC_MRR100_HISTORICAL_ARITHMETIC_PATH = NOT_RECOVERED

V04_RECOVERY_READINESS = NOT_READY_NEEDS_METHODOLOGICAL_DECISION

ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
```

No declares v0.4 lista. No decidas `.77` vs `.78`.

---

## 7. Persistencia administrativa obligatoria

Después de terminar el trabajo científico:

1. vuelve a obtener la rama remota `codex/prompts-temporary`;
2. no mezcles esta rama con `main`;
3. persiste exclusivamente el reporte final de este bloque en:

`codex_prompts_tmp/29_RESPUESTA_INTEGRAR_MICROAUDITORIA_ARITMETICA_MRR100_GATE_C_EV04_MAIN.md`

4. el commit administrativo debe modificar únicamente ese archivo de respuesta;
5. no modifiques Prompt29 ni respuestas anteriores;
6. no uses force push, rebase ni amend en la rama administrativa.

---

## 8. Formato mínimo del reporte final

Incluye como mínimo:

### A. Preflight Git
- baseline main;
- candidato;
- parent/tree;
- merge-base;
- ahead/behind;
- número de commits y paths;
- blob del artefacto;
- SHAs Plan/artículo.

### B. Verificación read-only del artefacto
- clasificación causal;
- readiness v0.4;
- Attempt05;
- source bindings;
- coexistencia `.77/.78`;
- prueba de que no se atribuyó provenance histórica no demostrada.

### C. Integración
- método exacto;
- from/to;
- confirmación de ausencia de merge/squash/cherry-pick/rebase/amend/force.

### D. Post-integración
- nuevo `origin/main`;
- tree;
- identidad con candidato;
- commit/path count;
- blob integrado;
- Plan/artículo intactos.

### E. Aislamiento
- nada ejecutado;
- v0.4 no construida;
- Attempt05 no autorizado/ejecutado;
- no decisión `.77/.78`.

### F. Persistencia administrativa
- rama;
- archivo de respuesta;
- scope `RESPONSE_ONLY`.

### G. Estado científico final
- bloque exacto de la sección 6.

Responde únicamente con el reporte final exigido.