# PROMPT101 — INTEGRAR Y CERRAR G5-F03 Y GRUPO 5 TRAS AUDITORÍA EXTERNA

## 0. Naturaleza, dictamen gobernante y alcance

Ejecuta **exclusivamente** la integración y cierre administrativo de **G5-F03 — Anexos, suplementos y cierre de Grupo 5**, después de la auditoría externa independiente satisfactoria del candidato generado por Prompt100.

Dictamen gobernante emitido por la IA Experimental/Auditora:

```text
PROMPT100_EXTERNAL_AUDIT = PASS
G5_F03_CANDIDATE_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
G5_F03 = APPROVABLE_FOR_INTEGRATION_AND_CLOSURE
GROUP5 = IN_PROGRESS
G6_F01_AUTHORIZED = false
```

Esta ejecución autoriza únicamente:

1. verificar nuevamente la identidad exacta del candidato G5-F03 auditado;
2. integrarlo en `main` mediante **fast-forward puro**;
3. cerrar operacionalmente G5-F03;
4. cerrar operacionalmente Grupo 5 como `CLOSED / APPROVED`;
5. reconciliar el Plan Maestro con ese cierre;
6. dejar G6-F01 únicamente `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.

No autoriza:

- editar o regenerar los dos artefactos candidatos auditados;
- crear nuevas tablas científicas;
- modificar las nueve tablas canónicas de G5-F02;
- recalcular métricas, intervalos, bootstrap, p-values o inferencia;
- ejecutar experimentos o retrieval;
- redecidir HE2 o HE5;
- reabrir EXP12;
- modificar el artículo o la tesis;
- realizar búsqueda bibliográfica;
- activar o ejecutar G6-F01;
- ejecutar G6-F02, G6-F03 ni fichas posteriores;
- convertir diagnósticos, auditorías o limitaciones en resultados científicos;
- sustituir fuentes congeladas por versiones superseded.

La invocación explícita de este Prompt101 constituye autorización únicamente para el alcance anterior.

---

## 1. Workspace local canónico obligatorio

Trabaja exclusivamente dentro del repositorio local canónico del usuario:

```text
C:/Users/Vladimir/OneDrive/Documentos/Maestría UNMSM/LLM_RGA_NANDINA
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

Debe cumplirse:

```text
WORKSPACE_ROOT_MATCH_EXPECTED = true
WORKSPACE_ORIGIN_REPOSITORY = elVladdi/gci-nandina-rag
USER_CANONICAL_LOCAL_PATH_FROZEN = true
```

Prohibido:

- usar otro clon como workspace principal;
- crear un clon alternativo;
- crear un worktree nuevo para esta ejecución;
- borrar, limpiar, resetear, sobrescribir o hacer stash de cambios locales preexistentes ajenos a Prompt101.

Si un cambio local intersecta un path gobernado por Prompt101 y no puede preservarse sin riesgo:

```text
STOP / G5_F03_CLOSURE_LOCAL_WORKSPACE_CONFLICT
```

Warnings por metadata histórica de worktrees son no bloqueantes si no impiden leer/escribir los paths gobernados.

---

## 2. Refs congelados y preflight

Ejecuta `git fetch --all --prune` cuando sea posible y verifica las refs remotas.

Refs experimentales congelados para esta integración:

```text
MAIN_BASE = e471d4336ab965cd55b7f0e2ca7926445b1f0391
PLAN_BASE = 996bd57efc92528863bc8b6401d3708a17e0b3b7
FICHAS_BASE = a85f79d7c91197624551b6e3d350aa8e5565154d
G5_F03_CANDIDATE = ca065618d5df0019f76ef5a971e858d91c263e1f
PROMPT100_SOURCE = 53890e3257c29a570cc63e5fd30659893ccbc52e
PROMPT100_RESPONSE = cc7266935bc9f7b41e9952cd705310f51235c40d
ARTICLE_OBSERVED_AT_DESIGN = 6b4807987f3c8144e791a2024ca4b432f5ede323
```

Debe cumplirse al preflight:

```text
origin/main == MAIN_BASE
origin/docs/plan-maestro-temporal-2026-08-31 == PLAN_BASE
origin/docs/fichas-grupos-3-8 == FICHAS_BASE
origin/codex/group5-f03-appendix-closure-v01 == G5_F03_CANDIDATE
```

Si `main`, Plan, fichas o candidato presentan drift inesperado:

```text
STOP / G5_F03_CLOSURE_REF_DRIFT
```

La rama `article/main-manuscript` es concurrente y **solo observacional**. Registra su HEAD al inicio y al final. Si avanzó respecto de `ARTICLE_OBSERVED_AT_DESIGN`, registra un warning informativo; no bloquees por ese hecho mientras Prompt101 no la modifique.

Verifica además el estado operacional de entrada:

```text
G5_F01 = CLOSED / APPROVED
G5_F02 = CLOSED / APPROVED
G5_F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
G6_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

---

## 3. Identidad exacta del candidato auditado

Rama candidata:

```text
codex/group5-f03-appendix-closure-v01
```

Debe verificarse exactamente:

```text
CANDIDATE_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
CANDIDATE_PARENT = e471d4336ab965cd55b7f0e2ca7926445b1f0391
CANDIDATE_COMMITS_AHEAD = 1
CANDIDATE_COMMITS_BEHIND = 0
CANDIDATE_CHANGED_PATH_COUNT = 2
```

Los dos únicos paths añadidos deben ser:

```text
docs/results/group5/g5_appendix_registry_v0.1.md
outputs/audits/group5_closure_v0.1.json
```

Blobs auditados que deben preservarse byte a byte:

```text
APPENDIX_REGISTRY_BLOB = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a
GROUP5_CLOSURE_CANDIDATE_BLOB = 1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf
```

No regeneres, edites, normalices ni reformatees esos archivos.

El estado interno `CANDIDATE_PENDING_EXTERNAL_AUDIT` de esos artefactos es un **estado histórico de generación**. Después de integrar y cerrar administrativamente G5-F03, no modifiques esos archivos solo para cambiar esa etiqueta. La verdad operacional posterior reside en el Plan Maestro y el registro de fichas.

Si falla cualquier identidad anterior:

```text
STOP / G5_F03_CANDIDATE_IDENTITY_FAILED
```

---

## 4. Contrato científico que debe permanecer inmutable

No alteres:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE

UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION

EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Semántica exacta de 0B-05C Attempt06:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
OVERALL = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

Prohibido concluir globalmente “sin impacto numérico”.

HE5 permanece `INCONCLUSIVE`:

```text
Descripción ambigua/incompleta = NOT_ESTIMABLE
Proximidad jerárquica = DESCRIPTIVE_ONLY
Precedentes históricos = DESCRIPTIVE_ONLY
Validez interna = DOCUMENTED_LIMITATION
```

EXP12 no tiene fila de rendimiento, no tiene resultado de retrieval y no apoya ni refuta HE5.

---

## 5. Cierres G5 ya aprobados que no se pueden alterar

### G5-F01

Preserva:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245
```

### G5-F02

Preserva la versión corregida integrada:

```text
scripts/results/group5/materialize_g5_tables_v0_1.py
blob = a2dc9f87d87f5ef144c1279828b85704ad6c206b

docs/results/group5/g5_canonical_tables_v0.1.md
blob = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d

outputs/results/group5/g5_numeric_crosscheck_v0.1.json
blob = a28af8df10f6d6bb4fdb02458288b41e34e1dc78

outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
blob = 727076a0d09735a87f45f6522d2a0ecead2cee17
```

Las nueve tablas canónicas deben permanecer idénticas. No materialices una décima tabla científica.

En `G5-SECONDARY-02`, preserva:

```text
SAME_CHAPTER -> denominator="" ; error_count=147
SAME_HS4     -> denominator="" ; error_count=284
SAME_HS6     -> denominator="" ; error_count=87
```

No inventes denominadores.

---

## 6. Auditoría externa de Prompt100 que gobierna este cierre

Antes de escribir, documenta que la auditoría externa independiente confirmó:

```text
PROMPT100_EXTERNAL_AUDIT = PASS

CANDIDATE_TOPOLOGY = PASS
CANDIDATE_TWO_PATH_SCOPE = PASS
APPENDIX_REGISTRY_BLOB_IDENTITY = PASS
GROUP5_CLOSURE_JSON_BLOB_IDENTITY = PASS

CANONICAL_TABLE_PRESENTATION_COVERAGE = 9/9
APPENDIX_TABLE_PRESENTATION_COVERAGE = 5/5
G3_EVIDENCE_FAMILY_TRACEABILITY = 16/16
G4_CONTROLLED_CLAIM_TRACEABILITY = 18/18
GROUP2B_NONBLOCKING_LIMITATION_TRACEABILITY = 11/11

EXISTING_CANONICAL_TABLE_MODIFICATION_COUNT = 0
NEW_SCIENTIFIC_TABLE_CREATED_COUNT = 0
NEW_SCIENTIFIC_METRIC_VALUE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0

HE5_DESCRIPTION_NOT_ESTIMABLE_VISIBLE = true
HE5_HIERARCHY_DESCRIPTIVE_ONLY_VISIBLE = true
HE5_PRECEDENT_SUPPORT_DESCRIPTIVE_ONLY_VISIBLE = true
HE5_INTERNAL_VALIDITY_LIMITATION_VISIBLE = true
EXP11A_NONCAUSAL_QUALIFICATION_VISIBLE = true
EXP11B_NO_SUPERPOPULATION_QUALIFICATION_VISIBLE = true
ATTEMPT06_CURRENT_SEMANTICS_VISIBLE = true
EXP12_CLOSED_WITHOUT_RETRIEVAL_VISIBLE = true
RESULTS_AND_AUDITS_SEPARATED = true
```

No repitas una nueva auditoría científica discrecional ni cambies el dictamen. Sí verifica identidades, topología y ausencia de drift antes de integrar.

---

## 7. RPRE obligatorio de cierre

Antes de cualquier escritura, todas estas verificaciones deben resultar `PASS`:

```text
RPRE_G5_F03_CLOSURE_SOURCE_CONTRACT
RPRE_G5_F03_CLOSURE_EXTERNAL_AUDIT_PASS
RPRE_G5_F03_CLOSURE_MAIN_BASE
RPRE_G5_F03_CLOSURE_PLAN_BASE
RPRE_G5_F03_CLOSURE_FICHAS_BASE
RPRE_G5_F03_CLOSURE_CANDIDATE_IDENTITY
RPRE_G5_F03_CLOSURE_TWO_PATH_SCOPE
RPRE_G5_F03_CLOSURE_BLOB_IDENTITY
RPRE_G5_F03_CLOSURE_FAST_FORWARD_POSSIBLE
RPRE_G5_F03_CLOSURE_G5_F01_PRESERVED
RPRE_G5_F03_CLOSURE_G5_F02_PRESERVED
RPRE_G5_F03_CLOSURE_NO_NEW_SCIENCE
RPRE_G5_F03_CLOSURE_NO_RECOMPUTATION
RPRE_G5_F03_CLOSURE_NO_NEW_INFERENCE
RPRE_G5_F03_CLOSURE_HE2_HE5_PRESERVATION
RPRE_G5_F03_CLOSURE_EXP12_FAIL_CLOSED
RPRE_G5_F03_CLOSURE_GROUP2B_LIMITATIONS_PRESERVED
RPRE_G5_F03_CLOSURE_ARTICLE_READONLY
RPRE_G5_F03_CLOSURE_G6_NOT_AUTHORIZED
```

Si cualquiera falla:

```text
STOP / G5_F03_CLOSURE_RPRE_FAILED
```

No integres ni cambies estados en ese caso.

---

## 8. Integración exacta a main

Integra el candidato auditado en `main` mediante **fast-forward puro**.

Debe cumplirse:

```text
MAIN_BEFORE_INTEGRATION = e471d4336ab965cd55b7f0e2ca7926445b1f0391
INTEGRATION_METHOD = FAST_FORWARD_ONLY
MAIN_AFTER_INTEGRATION = ca065618d5df0019f76ef5a971e858d91c263e1f
MAIN_PARENT_COUNT = 1
```

Prohibido:

- cherry-pick;
- squash;
- merge commit;
- rebase;
- regeneración;
- edición de los dos artefactos candidatos.

Después del push:

```text
origin/main == ca065618d5df0019f76ef5a971e858d91c263e1f
```

Y los blobs en `main` deben seguir siendo:

```text
APPENDIX_REGISTRY_BLOB = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a
GROUP5_CLOSURE_CANDIDATE_BLOB = 1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf
```

Verifica además que los blobs críticos G5-F01/G5-F02 de la sección 5 permanezcan idénticos.

Si no puede lograrse fast-forward exacto:

```text
STOP / G5_F03_FAST_FORWARD_IDENTITY_FAILED
```

---

## 9. Cierre administrativo de G5-F03 y habilitación prospectiva de G6-F01

Solo después de confirmar la integración exacta, trabaja sobre:

```text
branch = docs/fichas-grupos-3-8
base = a85f79d7c91197624551b6e3d350aa8e5565154d
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo.

Deja los estados operacionales:

```text
G5-F01 = CLOSED / APPROVED
G5-F02 = CLOSED / APPROVED
G5-F03 = CLOSED / APPROVED
GROUP5 = CLOSED / APPROVED

G6-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
```

Añade un bloque de cierre con al menos:

```text
FICHA = G5-F03
PROMPT100_SOURCE = 53890e3257c29a570cc63e5fd30659893ccbc52e
PROMPT100_RESPONSE = cc7266935bc9f7b41e9952cd705310f51235c40d
PROMPT100_EXTERNAL_AUDIT = PASS
APPROVED_CANDIDATE = ca065618d5df0019f76ef5a971e858d91c263e1f
CANDIDATE_PARENT = e471d4336ab965cd55b7f0e2ca7926445b1f0391
APPENDIX_REGISTRY_BLOB = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a
GROUP5_CLOSURE_BLOB = 1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf
INTEGRATION_METHOD = FAST_FORWARD_ONLY
INTEGRATION_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
FINAL_G5_F03_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
```

El cambio de `G6-F01` desde `PROSPECTIVE` a `ELIGIBLE` **no constituye activación**. No añadas bloque de activación de G6-F01 y no ejecutes su ficha.

Haz un único commit administrativo y push normal.

---

## 10. Reconciliación del Plan Maestro y cierre de Grupo 5

Después del cierre de fichas, trabaja sobre:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = 996bd57efc92528863bc8b6401d3708a17e0b3b7
file = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Modifica exclusivamente ese archivo.

Debe quedar inequívocamente:

```text
GROUP5 = CLOSED / APPROVED
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03_INTEGRATION_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
G5_F03_EXTERNAL_AUDIT = PASS

NEXT_ELIGIBLE_FICHA = G6-F01
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
GROUP6 = NOT_STARTED
```

Registra también, sin redecidir ni reinterpretar:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
```

Conserva explícitamente los guardrails:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

No declares G6-F01 `ACTIVE`, `AUTHORIZED` ni `EXECUTION_PENDING`.

Haz un único commit documental y push normal.

---

## 11. Verificación postintegración obligatoria

Después de los pushes, verifica las refs remotas finales.

Debe cumplirse:

```text
FINAL_ORIGIN_MAIN = ca065618d5df0019f76ef5a971e858d91c263e1f
FINAL_ORIGIN_FICHAS = <commit administrativo nuevo de cierre G5-F03>
FINAL_ORIGIN_PLAN = <commit documental nuevo de cierre Grupo 5>
```

Comprueba en `main`:

```text
docs/results/group5/g5_appendix_registry_v0.1.md
blob = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a

outputs/audits/group5_closure_v0.1.json
blob = 1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf
```

Comprueba que no se modificaron los artefactos científicos G5-F01/G5-F02 y que no apareció ningún path de Grupo 6 en `main` como consecuencia de Prompt101.

La rama candidata puede permanecer como referencia histórica. No la reescribas.

---

## 12. Prohibiciones científicas y editoriales durante Prompt101

Todos deben permanecer:

```text
NEW_SCIENTIFIC_STATEMENT_COUNT = 0
NEW_SCIENTIFIC_TABLE_CREATED_COUNT = 0
NEW_SCIENTIFIC_METRIC_VALUE_COUNT = 0
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
HE2_REDECIDED = false
HE5_REDECIDED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
```

La actualización administrativa de fichas y Plan no cuenta como nueva afirmación científica.

---

## 13. Persistencia del reporte de ejecución

Al finalizar, crea en:

```text
branch = codex/prompts-temporary
file = codex_prompts_tmp/101_RESPUESTA_INTEGRAR_CERRAR_G5_F03_Y_GRUPO5.md
```

El commit del reporte debe añadir **solo** ese archivo respecto del commit de Prompt101 invocado por el usuario.

No edites Prompt101 durante la ejecución.

---

## 14. Reporte terminal obligatorio

Devuelve únicamente un bloque terminal que incluya, como mínimo:

```text
PROMPT101 = COMPLETED | STOPPED

WORKSPACE_ROOT_OBSERVED = ...
WORKSPACE_ORIGIN_URL = ...
WORKSPACE_INITIAL_BRANCH = ...
WORKSPACE_INITIAL_HEAD = ...
WORKSPACE_INITIAL_DIRTY_COUNT = ...

PREFLIGHT_MAIN = ...
PREFLIGHT_PLAN = ...
PREFLIGHT_FICHAS = ...
PREFLIGHT_G5_F03_CANDIDATE = ...
ARTICLE_HEAD_PREFLIGHT = ...
PROMPT101_SOURCE = ...

PROMPT100_RESPONSE = cc7266935bc9f7b41e9952cd705310f51235c40d
PROMPT100_EXTERNAL_AUDIT = PASS

RPRE_G5_F03_CLOSURE_SOURCE_CONTRACT = PASS|FAIL
RPRE_G5_F03_CLOSURE_EXTERNAL_AUDIT_PASS = PASS|FAIL
RPRE_G5_F03_CLOSURE_MAIN_BASE = PASS|FAIL
RPRE_G5_F03_CLOSURE_PLAN_BASE = PASS|FAIL
RPRE_G5_F03_CLOSURE_FICHAS_BASE = PASS|FAIL
RPRE_G5_F03_CLOSURE_CANDIDATE_IDENTITY = PASS|FAIL
RPRE_G5_F03_CLOSURE_TWO_PATH_SCOPE = PASS|FAIL
RPRE_G5_F03_CLOSURE_BLOB_IDENTITY = PASS|FAIL
RPRE_G5_F03_CLOSURE_FAST_FORWARD_POSSIBLE = PASS|FAIL
RPRE_G5_F03_CLOSURE_G5_F01_PRESERVED = PASS|FAIL
RPRE_G5_F03_CLOSURE_G5_F02_PRESERVED = PASS|FAIL
RPRE_G5_F03_CLOSURE_NO_NEW_SCIENCE = PASS|FAIL
RPRE_G5_F03_CLOSURE_NO_RECOMPUTATION = PASS|FAIL
RPRE_G5_F03_CLOSURE_NO_NEW_INFERENCE = PASS|FAIL
RPRE_G5_F03_CLOSURE_HE2_HE5_PRESERVATION = PASS|FAIL
RPRE_G5_F03_CLOSURE_EXP12_FAIL_CLOSED = PASS|FAIL
RPRE_G5_F03_CLOSURE_GROUP2B_LIMITATIONS_PRESERVED = PASS|FAIL
RPRE_G5_F03_CLOSURE_ARTICLE_READONLY = PASS|FAIL
RPRE_G5_F03_CLOSURE_G6_NOT_AUTHORIZED = PASS|FAIL

CANDIDATE_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
CANDIDATE_PARENT = e471d4336ab965cd55b7f0e2ca7926445b1f0391
CANDIDATE_COMMITS_AHEAD = ...
CANDIDATE_COMMITS_BEHIND = ...
CANDIDATE_CHANGED_PATH_COUNT = ...
APPENDIX_REGISTRY_BLOB = ...
GROUP5_CLOSURE_BLOB = ...

MAIN_BEFORE_INTEGRATION = ...
INTEGRATION_METHOD = ...
MAIN_AFTER_INTEGRATION = ...
MAIN_PARENT_COUNT = ...

POSTCLOSURE_FICHAS_COMMIT = ...
POSTCLOSURE_PLAN_COMMIT = ...

G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = CLOSED / APPROVED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
GROUP6 = NOT_STARTED

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false

NEW_SCIENTIFIC_STATEMENT_COUNT = 0
NEW_SCIENTIFIC_TABLE_CREATED_COUNT = 0
NEW_SCIENTIFIC_METRIC_VALUE_COUNT = 0
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false

FINAL_ORIGIN_MAIN = ...
FINAL_ORIGIN_FICHAS = ...
FINAL_ORIGIN_PLAN = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...

BLOCKERS = NONE | ...
WARNINGS = NONE | ...
```

No declares G6-F01 autorizado o iniciado. No avances a Grupo 6 dentro de Prompt101.