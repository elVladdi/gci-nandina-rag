# FIG006 — Respuesta oficial: corregir scope, integrar y cerrar G6-F01

## 0. Resultado

```text
FIG006_EXECUTION = COMPLETE
SOURCE_CONTRACT = PASS
EXTERNAL_AUDIT = PASS_WITH_ADMINISTRATIVE_CORRECTION_COMPLETED
```

Se ejecutó exclusivamente `figure_prompts_tmp/FIG006_CORREGIR_SCOPE_INTEGRAR_Y_CERRAR_G6_F01.md@e44506cc45f527a324005f44f4e2db35103cf369`.

La única corrección previa a la integración fue administrativa: se eliminó exclusivamente la línea accidental `FICHA = G4-F02` situada inmediatamente después de `## Candidato G4-F02 pendiente de auditoria externa` en el registro operacional de fichas. No se modificó ningún contenido científico ni el resto del bloque histórico G4-F02.

## 1. Corrección administrativa de scope

```text
FICHAS_BEFORE = f5686cc7aa7ffd11ab45dc52cf258b256523abc9
SCOPE_CORRECTION_COMMIT = 7342b05ddf9b3ac1861b037fb444f04104c4897d
SCOPE_CORRECTION_CHANGED_PATH_COUNT = 1
SCOPE_CORRECTION_CHANGED_PATH = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
SCOPE_CORRECTION_DELETIONS = 1
SCIENTIFIC_CORRECTION_REQUIRED = false
```

## 2. Integración de G6-F01

Antes de integrar se revalidó que `main` permanecía en la base congelada y que el candidato era su descendiente directo, exactamente un commit delante y cero detrás, con un solo path añadido.

```text
MAIN_BEFORE = ca065618d5df0019f76ef5a971e858d91c263e1f
CANDIDATE_BRANCH = figures/g6-f01-spec-registry-v01
CANDIDATE_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
CANDIDATE_PARENT = ca065618d5df0019f76ef5a971e858d91c263e1f
COMMITS_AHEAD_BEFORE_INTEGRATION = 1
COMMITS_BEHIND_BEFORE_INTEGRATION = 0
CANDIDATE_CHANGED_PATH_COUNT = 1
CANDIDATE_CHANGED_PATH = outputs/figures/group6/g6_figure_spec_registry_v0.1.json
INTEGRATION_METHOD = PURE_FAST_FORWARD
INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
MAIN_AFTER = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
REGISTRY_BLOB_AFTER = 44cc30fc3c38639c6aa4370cb6f317458041f1b1
FIGURE_SPEC_COUNT = 3
NON_FIGURE_DISPOSITION_COUNT = 6
```

La integración se realizó moviendo `main` por fast-forward sin merge commit, squash, rebase ni cherry-pick. El commit integrado conserva como padre directo `ca065618d5df0019f76ef5a971e858d91c263e1f`.

## 3. Cierre operacional y reconciliación del Plan Maestro

```text
FICHAS_CLOSURE_COMMIT = 98b5c1edeb6bb1b78a06a08b549b4e068e14e62b
PLAN_BEFORE = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
PLAN_RECONCILIATION_COMMIT = b74b96d0163807007e4579d86450dd235125b30f
G6_F01_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_FINAL_STATE = IN_PROGRESS
G6_F02_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F03_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7_FINAL_STATE = PENDING / NOT_AUTHORIZED
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
```

El registro de fichas quedó cerrado para G6-F01 y mantiene G6-F02 solo como elegible. El Plan Maestro fue reconciliado de forma mínima: Grupo 6 queda `IN_PROGRESS`, G6-F01 cerrado e integrado con su commit, G6-F02 elegible pero no autorizado/no ejecutado y Grupo 7 pendiente/no autorizado.

## 4. Controles de no-ejecución científica

```text
FIGURE_BINARY_COUNT = 0
FIGURE_SCRIPT_COUNT = 0
NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
EXP12_REOPENED = false
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
```

No se generaron figuras, scripts, PNG, SVG, PDF, EPS ni mockups; no se recalcularon métricas, intervalos, inferencia o p-values; no se modificaron artículo o tesis; no se reabrió EXP12 y no se ejecutó G6-F02.

## 5. Disposición terminal

```text
FIG006_EXECUTION = COMPLETE
SOURCE_CONTRACT = PASS
EXTERNAL_AUDIT = PASS_WITH_ADMINISTRATIVE_CORRECTION_COMPLETED
G6_F01_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_FINAL_STATE = IN_PROGRESS
G6_F02_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
```
