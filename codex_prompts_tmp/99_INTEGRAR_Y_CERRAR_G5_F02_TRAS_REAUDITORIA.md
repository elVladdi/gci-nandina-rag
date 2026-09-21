# PROMPT 99 — INTEGRAR Y CERRAR G5-F02 TRAS REAUDITORÍA EXTERNA

## 0. Naturaleza y autorización

Ejecuta **exclusivamente** la integración y cierre administrativo de **G5-F02 — Tablas canónicas y control numérico** después de la reauditoría externa satisfactoria del candidato corregido v02.

Dictamen gobernante:

```text
PROMPT98_EXTERNAL_AUDIT = PASS
G5_F02_CORRECTED_CANDIDATE_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
G5_F02 = APPROVABLE_FOR_INTEGRATION_AND_CLOSURE
GROUP5 = IN_PROGRESS
G5_F03_AUTHORIZED = false
```

Esta ejecución autoriza únicamente:

1. integrar por fast-forward puro el candidato G5-F02 v02 auditado a `main`;
2. cerrar G5-F02 en el registro de fichas;
3. reconciliar el Plan Maestro con ese cierre;
4. dejar G5-F03 únicamente `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.

No autoriza:

- regenerar o editar los artefactos G5-F02 auditados;
- recalcular métricas, inferencia, bootstrap, intervalos o p-values;
- redecidir HE2 o HE5;
- modificar resultados G3/G4/G5-F01;
- reabrir EXP12;
- modificar artículo o tesis;
- activar o ejecutar G5-F03;
- cerrar Grupo 5;
- iniciar Grupo 6.

---

## 1. Workspace local canónico obligatorio

Trabaja exclusivamente dentro del repositorio local canónico del usuario:

```text
WORKSPACE_LOCAL_CANONICO = C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier operación registra y verifica:

```text
git rev-parse --show-toplevel
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git status --porcelain
git worktree list --porcelain
```

En Windows se acepta la representación normalizada equivalente con `/` en lugar de `\`, pero **no otra carpeta**.

Debe cumplirse:

```text
WORKSPACE_ROOT_MATCH_EXPECTED = true
WORKSPACE_ORIGIN_REPOSITORY = elVladdi/gci-nandina-rag
USER_CANONICAL_LOCAL_PATH_FROZEN = true
```

Prohibido, salvo autorización expresa del usuario:

- usar otro clon como workspace principal;
- crear un clon alternativo;
- usar un workspace temporal como repositorio principal;
- crear un worktree fuera del repositorio canónico para ejecutar esta ficha;
- borrar, resetear, limpiar, sobrescribir o hacer stash de cambios locales preexistentes del usuario.

Si existen cambios locales preexistentes, registra sus paths. No son por sí solos un bloqueo si son ajenos a los paths gobernados y no impiden la operación. Si alguno entra en conflicto con `main`, Plan, fichas o la persistencia del reporte:

```text
STOP / G5_F02_CLOSURE_LOCAL_WORKSPACE_CONFLICT
```

No operes en worktrees observados fuera del workspace canónico. No crees worktrees nuevos para esta ejecución.

---

## 2. Refs congelados y preflight

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = d5729887f47c36d8cf42d87090c40f9668e5ae84
origin/docs/plan-maestro-temporal-2026-08-31 = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
origin/docs/fichas-grupos-3-8 = 511fcf6346ba03d98247320ca252f25d7143f4eb
origin/codex/group5-f02-canonical-tables-v02 = e471d4336ab965cd55b7f0e2ca7926445b1f0391
```

Gobernanza inmediata:

```text
PROMPT97_SOURCE = 5b5de5acc62cbf5dfd08f044870f815369ee6c96
PROMPT97_RESPONSE = 8596fe65e5aa50f6b245f13450fc4a64ae5397a8
PROMPT98_SOURCE = 3ee292c718d5d673642faceb2a1ae28ae00cbc9c
PROMPT98_RESPONSE = 28f04e3c79991666b2dae52de5705883e28b190b
PROMPT98_POSTCORRECTION_FICHAS = 511fcf6346ba03d98247320ca252f25d7143f4eb
G5_F02_V01_SUPERSEDED = 9a8ca23ef607b5975b46a4336e033fc44ebe9453
G5_F02_V02_APPROVED = e471d4336ab965cd55b7f0e2ca7926445b1f0391
```

La rama editorial es solo observacional. Registra su HEAD al inicio y al final. Su avance concurrente no es bloqueo mientras este prompt no la modifique.

Si `main`, Plan, fichas o candidato v02 presentan drift no explicado:

```text
STOP / G5_F02_CLOSURE_REF_DRIFT
```

---

## 3. Identidad exacta del candidato auditado

Verifica que:

```text
candidate = e471d4336ab965cd55b7f0e2ca7926445b1f0391
candidate_parent = d5729887f47c36d8cf42d87090c40f9668e5ae84
commits_ahead = 1
commits_behind = 0
changed_path_count_from_main = 12
```

Los 12 paths deben ser exactamente:

```text
scripts/results/group5/materialize_g5_tables_v0_1.py
docs/results/group5/g5_canonical_tables_v0.1.md
outputs/results/group5/g5_numeric_crosscheck_v0.1.json
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv
outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv
outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv
```

Blobs críticos auditados que deben preservarse exactamente:

```text
SCRIPT_BLOB = a2dc9f87d87f5ef144c1279828b85704ad6c206b
CANONICAL_TABLES_MD_BLOB = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d
NUMERIC_CROSSCHECK_BLOB = a28af8df10f6d6bb4fdb02458288b41e34e1dc78
G5_SECONDARY_02_BLOB = 727076a0d09735a87f45f6522d2a0ecead2cee17
```

No regeneres ni edites ningún path del candidato.

Preserva las conclusiones auditadas:

```text
EXPECTED_CANONICAL_TABLE_COUNT = 9
MATERIALIZED_CANONICAL_TABLE_COUNT = 9
UNTRACED_SCIENTIFIC_VALUE_COUNT = 0
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
DENOMINATOR_MISMATCH_COUNT = 0
UNIT_MISMATCH_COUNT = 0
CI_LEVEL_MISMATCH_COUNT = 0
HE5_HIERARCHY_FABRICATED_DENOMINATOR_COUNT = 0
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0
SCIENTIFIC_METRIC_VALUE_DELTA_COUNT = 0
```

---

## 4. Integración a main — fast-forward puro

Integra **exactamente** el candidato v02 en `main` mediante fast-forward puro.

Debe cumplirse:

```text
MAIN_BEFORE_INTEGRATION = d5729887f47c36d8cf42d87090c40f9668e5ae84
INTEGRATION_METHOD = FAST_FORWARD_ONLY
MAIN_AFTER_INTEGRATION = e471d4336ab965cd55b7f0e2ca7926445b1f0391
MAIN_PARENT_COUNT = 1
```

No cherry-pick, no squash, no merge commit, no rebase y no regeneración.

Después del push, `origin/main` debe ser exactamente:

```text
e471d4336ab965cd55b7f0e2ca7926445b1f0391
```

Verifica que los cuatro blobs críticos en `main` sean idénticos a los anteriores.

Si la integración no puede ser fast-forward exacta:

```text
STOP / G5_F02_FAST_FORWARD_IDENTITY_FAILED
```

---

## 5. Cierre administrativo de G5-F02

Después de confirmar la integración exacta, trabaja sobre:

```text
branch = docs/fichas-grupos-3-8
base = 511fcf6346ba03d98247320ca252f25d7143f4eb
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo.

Deja los estados:

```text
G5-F01 = CLOSED / APPROVED
G5-F02 = CLOSED / APPROVED
G5-F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP5 = IN_PROGRESS
```

Añade un bloque de cierre que incluya como mínimo:

```text
FICHA = G5-F02
PROMPT97_SOURCE = 5b5de5acc62cbf5dfd08f044870f815369ee6c96
PROMPT97_RESPONSE = 8596fe65e5aa50f6b245f13450fc4a64ae5397a8
PROMPT98_SOURCE = 3ee292c718d5d673642faceb2a1ae28ae00cbc9c
PROMPT98_RESPONSE = 28f04e3c79991666b2dae52de5705883e28b190b
SUPERSEDED_CANDIDATE_V01 = 9a8ca23ef607b5975b46a4336e033fc44ebe9453
APPROVED_CANDIDATE_V02 = e471d4336ab965cd55b7f0e2ca7926445b1f0391
EXTERNAL_REAUDIT = PASS
INTEGRATION_COMMIT = e471d4336ab965cd55b7f0e2ca7926445b1f0391
FINAL_G5_F02_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = IN_PROGRESS
G5_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Haz un único commit administrativo y push normal.

---

## 6. Reconciliación del Plan Maestro

Después del cierre de fichas, trabaja sobre:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
file = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Modifica exclusivamente ese archivo para reflejar:

```text
GROUP5 = IN_PROGRESS
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02_INTEGRATION_COMMIT = e471d4336ab965cd55b7f0e2ca7926445b1f0391
G5_F02_EXTERNAL_REAUDIT = PASS
NEXT_ELIGIBLE_FICHA = G5-F03
G5_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false
```

Registra también, sin redecidir:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
```

Y conserva explícitamente:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

No declares `GROUP5=CLOSED`.

Haz un único commit documental y push normal.

---

## 7. Prohibiciones científicas y editoriales

Durante Prompt99 debe cumplirse:

```text
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED_BY_PROMPT99 = false
THESIS_MODIFIED_BY_PROMPT99 = false
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false
GROUP5_CLOSED = false
```

No modifiques ninguna de las 12 salidas auditadas durante esta ejecución.

---

## 8. Verificación final obligatoria

Ejecuta `git fetch origin` y verifica:

```text
origin/main = e471d4336ab965cd55b7f0e2ca7926445b1f0391
origin/docs/fichas-grupos-3-8 = <commit de cierre Prompt99>
origin/docs/plan-maestro-temporal-2026-08-31 = <commit de reconciliación Prompt99>

G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = IN_PROGRESS
G5_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Vuelve a registrar:

```text
WORKSPACE_ROOT
WORKSPACE_ROOT_MATCH_EXPECTED
WORKSPACE_ORIGIN_URL
WORKSPACE_FINAL_BRANCH
WORKSPACE_FINAL_HEAD
WORKSPACE_FINAL_DIRTY_COUNT
USER_CANONICAL_LOCAL_PATH_FROZEN = true
LOCAL_PERSISTENCE_IN_USER_FOLDER_ASSERTED = true
```

`LOCAL_PERSISTENCE_IN_USER_FOLDER_ASSERTED=true` solo puede reportarse si la ejecución realmente se realizó en el workspace canónico verificado. No afirmes que el workspace está limpio si conserva cambios preexistentes.

---

## 9. Persistencia de la respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/99_RESPUESTA_INTEGRAR_Y_CERRAR_G5_F02_TRAS_REAUDITORIA.md
```

El commit de respuesta debe añadir únicamente ese archivo.

Reporte terminal mínimo:

```text
PROMPT99 = COMPLETED

WORKSPACE_ROOT = ...
WORKSPACE_ROOT_MATCH_EXPECTED = true
WORKSPACE_ORIGIN_URL = ...
WORKSPACE_INITIAL_BRANCH = ...
WORKSPACE_INITIAL_HEAD = ...
WORKSPACE_INITIAL_DIRTY_COUNT = ...
USER_CANONICAL_LOCAL_PATH_FROZEN = true

PREFLIGHT_MAIN = d5729887f47c36d8cf42d87090c40f9668e5ae84
PREFLIGHT_PLAN = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
PREFLIGHT_FICHAS = 511fcf6346ba03d98247320ca252f25d7143f4eb
PREFLIGHT_CANDIDATE_V02 = e471d4336ab965cd55b7f0e2ca7926445b1f0391
ARTICLE_HEAD_PREFLIGHT = ...
PROMPT99_COMMIT = <commit fuente invocado>

INTEGRATION_METHOD = FAST_FORWARD_ONLY
MAIN_BEFORE_INTEGRATION = d5729887f47c36d8cf42d87090c40f9668e5ae84
MAIN_AFTER_INTEGRATION = e471d4336ab965cd55b7f0e2ca7926445b1f0391
CANDIDATE_TREE_IDENTITY_WITH_MAIN = true
AUDITED_ARTIFACTS_REGENERATED = false
AUDITED_ARTIFACTS_MODIFIED_DURING_INTEGRATION = false
SCRIPT_BLOB = a2dc9f87d87f5ef144c1279828b85704ad6c206b
CANONICAL_TABLES_MD_BLOB = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d
NUMERIC_CROSSCHECK_BLOB = a28af8df10f6d6bb4fdb02458288b41e34e1dc78
G5_SECONDARY_02_BLOB = 727076a0d09735a87f45f6522d2a0ecead2cee17

FICHAS_CLOSURE_COMMIT = ...
PLAN_RECONCILIATION_COMMIT = ...

G5_F02_EXTERNAL_REAUDIT = PASS
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = IN_PROGRESS
G5_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED_BY_PROMPT99 = false
GROUP5_CLOSED = false

WORKSPACE_FINAL_BRANCH = ...
WORKSPACE_FINAL_HEAD = ...
WORKSPACE_FINAL_DIRTY_COUNT = ...
LOCAL_PERSISTENCE_IN_USER_FOLDER_ASSERTED = true
ARTICLE_HEAD_FINAL_OBSERVED = ...

BLOCKERS = NONE
WARNINGS = <NONE o advertencias no bloqueantes reales>
```

Si aparece un bloqueo, no simules `COMPLETED`; reporta el `STOP` correspondiente y conserva la frontera de autorización.