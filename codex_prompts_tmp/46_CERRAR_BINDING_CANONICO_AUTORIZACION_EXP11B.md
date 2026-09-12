# PROMPT 46 — CERRAR BINDING CANÓNICO DE AUTORIZACIÓN EXP11B

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Debes corregir exclusivamente el paquete prospectivo de ejecución de `EXP11B Retrieval H150/H200` producido por Prompt45. Este bloque sigue siendo **pre-ejecución**: NO autoriza ni ejecuta retrieval oficial H150/H200 y NO puede observar métricas ni rankings H150/H200.

El objetivo es cerrar un hallazgo bloqueante adicional detectado por la auditoría externa de IA Experimental: el runner v02 endurece correctamente el binding del paquete y el consumo one-shot, pero **no liga técnicamente el propio artefacto de autorización a la ruta canónica y a los bytes versionados en `HEAD`**. En su estado actual, `--authorization` puede apuntar a un JSON arbitrario/local y una modificación no versionada del `authorization_id`/`attempt_id` podría eludir el consumo one-shot.

Aprovecha este mismo bloque para colocar el punto de consumo exactamente en el límite contractual: después de todas las validaciones pre-scoring del primer banco y **justo antes del primer scoring EVAL**.

---

# 1. Dictamen externo que gobierna este bloque

```text
PROMPT45_EXTERNAL_AUDIT = REJECTED / CORRECTION_REQUIRED

EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V02 = NOT_APPROVED_FOR_INTEGRATION
candidate_f5dddac0d296e74e5f92af3f863cbb3c74e757b9 = DO_NOT_INTEGRATE

F003_STREAMING = CLOSED_BY_STATIC_EXTERNAL_AUDIT
F004_FAILURE_CONTEXT = CLOSED_BY_STATIC_EXTERNAL_AUDIT

F005 = AUTHORIZATION_ARTIFACT_NOT_CANONICALLY_VERSION_BOUND
F006 = CONSUMPTION_POINT_PRECEDES_FIRST_BANK_PRE_SCORING_WORK

EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

El candidato v02 rechazado permanece como evidencia histórica inmutable. No lo integres, no lo amend, no hagas rebase sobre él y no lo uses como parent del nuevo candidato.

La auditoría externa NO rechaza:

- la semántica BM25;
- la reutilización de helpers EXP-04/EXP11A;
- el streaming de case-level/candidates;
- el modelo explícito de failure context;
- el principio de `approved_package_commit` ancestro de `execution_head`.

---

# 2. Baseline y refs obligatorias

Antes de modificar nada ejecuta `git fetch` y verifica exactamente:

```text
origin/main = 09ff184854659110f7711b3eee65fc18927649da
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/exp11b-retrieval-execution-package-v01 = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1
origin/codex/exp11b-retrieval-execution-package-v02 = f5dddac0d296e74e5f92af3f863cbb3c74e757b9
```

Verifica también:

```text
v01 parent = 09ff184854659110f7711b3eee65fc18927649da
v02 parent = 09ff184854659110f7711b3eee65fc18927649da
v01 is NOT ancestor of origin/main
v02 is NOT ancestor of origin/main
EXP11B_PORTABILITY_DEBT = CLOSED / APPROVED / INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Si cualquier ref canónica cambió: `STOP / PRECONDITION_REF_DRIFT`.

---

# 3. Nuevo candidato limpio v03

Crea desde `origin/main = 09ff184...`:

`codex/exp11b-retrieval-execution-package-v03`

El único commit científico debe tener parent directo:

`09ff184854659110f7711b3eee65fc18927649da`

No cherry-pickees v01 ni v02. Puedes consultarlos como referencia, pero reconstruye limpiamente desde `main`.

El candidato v03 puede añadir exclusivamente:

```text
src/experiments/run_exp11b_historical_retrieval_h150_h200_v03.py
src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.3.json
```

No modifiques archivos científicos existentes.

---

# 4. Semántica científica congelada

No cambies el método científico. Conserva exactamente:

```text
query_column = DESCRIPCION DE MERCANCIAS CONCATENADA
label_column = NANDINA
normalization = unicode_NFKD_lowercase_remove_combining_marks
tokenizer = regex_[a-z0-9]+
k1 = 1.5
b = 0.75
history_depth = bank_row_count
candidate_depth = 100
k_values = [1,3,5,10,50]
ranking_order = descending_score_then_ascending_historical_case_id
candidate_deduplication = first_ranked_historical_row_per_NANDINA
reference_rank = one_based_rank_after_NANDINA_deduplication_or_zero_when_absent
reciprocal_rank = zero_when_rank_is_zero_else_1_over_rank
primary_eval_n = 1056
```

Reutiliza directamente los helpers canónicos versionados. No copies ni redefinas BM25.

---

# 5. F005 — binding canónico y versionado del artefacto de autorización

## 5.1 Ruta única

La ejecución oficial debe aceptar **únicamente** la autorización canónica definida por la config:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json`

No permitas que `--execute-official` use un JSON arbitrario externo.

Puedes:

- eliminar `--authorization`; o
- conservarlo solo si el runner exige que su `resolve()` sea exactamente igual a la ruta canónica resuelta.

Cualquier otra ruta debe terminar, antes de scoring y antes de consumo, con una clasificación equivalente a:

`OFFICIAL_EXECUTION_BLOCKED_NONCANONICAL_AUTHORIZATION_PATH`

## 5.2 El authorization JSON debe estar versionado en `execution_head`

Antes de aceptar la autorización, exige todo lo siguiente:

```text
canonical authorization path exists as regular file;
authorization path is tracked by Git;
HEAD:<canonical_authorization_path> exists;
working-tree blob of authorization == HEAD blob of authorization;
working-tree bytes/hash == bytes/hash stored in HEAD;
no local/uncommitted mutation of authorization is accepted.
```

Una autorización presente solo en working tree pero no versionada debe bloquear:

`OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_NOT_VERSIONED`

Una autorización versionada pero modificada localmente debe bloquear:

`OFFICIAL_EXECUTION_BLOCKED_AUTHORIZATION_WORKTREE_DRIFT`

Registra el blob Git observado de la autorización y su SHA-256 en la evidencia de ejecución futura o en el objeto validado que devuelva el runner.

## 5.3 Relación con `approved_package_commit`

Mantén el modelo correcto de Prompt45:

```text
approved_package_commit = commit científico exacto del paquete aprobado/integrado
execution_head = commit posterior que contiene la autorización versionada
approved_package_commit is ancestor of execution_head
runner/config package blob == execution_head blob == working-tree blob
runner/config package SHA256 == execution_head SHA256 == working-tree canonical SHA256
```

La autorización canónica futura seguirá conteniendo, como mínimo:

```text
authorization_id
attempt_id
authorization_status = AUTHORIZED_ONE_SHOT
approved_package_commit
runner_path
runner_git_blob
runner_sha256
config_path
config_git_blob
config_sha256
eval_sha256
bank_manifest_sha256
bank_ledger_sha256
portability_closure_blob
expected_banks = 20
official_output_root
```

No crees la autorización oficial en Prompt46.

## 5.4 Prueba adversarial obligatoria de one-shot

En un repositorio Git temporal, sin H150/H200:

1. crea package commit sintético;
2. crea commit descendiente con autorización canónica versionada;
3. demuestra `PASS_CONTRACT_MODEL` con authorization working tree byte-idéntica a HEAD;
4. modifica localmente solo `authorization_id` o `attempt_id` sin commit;
5. demuestra que el runner/validador bloquea **antes de scoring y antes de crear un nuevo marcador**;
6. restaura el working tree temporal;
7. demuestra que una ruta alternativa de autorización también bloquea;
8. cleanup temporal PASS.

Esto debe probar que un operador no puede reutilizar una autorización consumida simplemente editando/copiendo el JSON localmente.

---

# 6. F006 — punto exacto de consumo

Conserva `open(..., 'x')` o semántica equivalente exclusiva.

La secuencia oficial prospectiva debe ser exactamente:

```text
1. validar autorización canónica versionada + bindings;
2. ejecutar preflight completo sin consumo;
3. verificar ausencia de output oficial;
4. seleccionar primer banco;
5. validar SHA/rows del primer banco;
6. construir su índice BM25;
7. JUSTO ANTES de calcular scores para el primer caso EVAL, crear el marcador one-shot de forma exclusiva;
8. iniciar scoring;
9. no volver a crear ni reemplazar el marcador durante la corrida.
```

Si falla algo en 1–6, la autorización NO se consume porque el scoring no comenzó.

Si el marcador se crea en 7, queda consumida aunque falle/interrumpa posteriormente.

No debe existir ninguna llamada a `_bm25_scores` antes del consumo.

Implementa el hook de consumo en el límite real de scoring, no antes del loop de bancos.

Prueba local/sintética obligatoria:

```text
failure_before_first_scoring => marker_created = false
first_scoring_boundary => marker_created = true before bm25_scores_call_count becomes 1
second/repeated scoring => marker_creation_count remains 1
```

No uses H150/H200 para esta prueba.

---

# 7. F003/F004 — conservar sin regresión

Mantén:

```text
stream_case_level_output = true
stream_candidate_output = true
global_case_accumulator = false
global_candidate_accumulator = false
flush_frequency = PER_BANK
partial_outputs_are_official = false
```

Mantén también:

```text
current_run_id
current_bank_id
current_condition
current_stage
```

con stages auditables y failure ledger correcto.

No reintroduzcas acumulación global ni atribución del fallo al banco anterior.

---

# 8. H100 full-output shadow

Ejecuta exactamente una vez `--self-test-h100`, exclusivamente H100 y directorio temporal.

Debe volver a reproducir:

```text
Top1 numerator = 538
Top3 numerator = 709
Top5 numerator = 806
Top10 numerator = 941
Top50 numerator = 1047
MRR = 0.6297077493524843
MRR abs tolerance = 1e-12
```

Debe ejercitar la misma serialización/streaming futura y validar los 8 artefactos congelados:

```text
run_manifest_json
metrics_by_bank_csv
case_level_csv
candidate_ranking_csv
condition_summary_csv
output_hash_ledger_csv
failure_ledger_json
environment_json
```

Cleanup temporal PASS.

No abras ningún banco H150/H200 en el self-test.

---

# 9. Preflight y pruebas preventivas obligatorias

Sin scoring H150/H200, registra:

```text
A. py_compile/import/CLI help = PASS
B. config JSON/source bindings = PASS
C. --preflight exactamente una vez = PASS_EXACT_20_OF_20
D. --self-test-h100 exactamente una vez = PASS
E. --execute-official sin autorización canónica = BLOCKED_BEFORE_SCORING
F. authorization path alternativo = BLOCKED_NONCANONICAL_BEFORE_SCORING
G. authorization canónica no versionada = BLOCKED_NOT_VERSIONED_BEFORE_SCORING
H. authorization canónica versionada pero dirty = BLOCKED_WORKTREE_DRIFT_BEFORE_SCORING
I. approved_package_commit inválido = BLOCKED_BEFORE_SCORING
J. marcador ya consumido = BLOCKED_BEFORE_SCORING
K. descendant authorization model versionado limpio = PASS_CONTRACT_MODEL
L. failure-before-first-scoring = marker NOT created
M. scoring-boundary synthetic test = marker created exactly once before first score
N. failure-context test = PASS
O. streaming/bounded-memory inspection/test = PASS
```

Los tests E–O deben ser sintéticos/temporales, sin tocar rutas oficiales reales y sin scoring H150/H200.

---

# 10. Config v0.3

Crea:

`src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.3.json`

Debe conservar todas las invariantes válidas de v0.2 y añadir explícitamente:

```text
contract_status = CANDIDATE_EXECUTION_PACKAGE_V03_PENDING_EXTERNAL_AUDIT
canonical_authorization_path_required = true
authorization_must_be_versioned_in_execution_head = true
authorization_worktree_identity_required = true
noncanonical_authorization_override_allowed = false
one_shot_consumption_required = true
consumption_boundary = IMMEDIATELY_BEFORE_FIRST_BM25_SCORE
```

Ruta futura de autorización:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.3.json`

No la crees todavía.

---

# 11. Readiness v0.3

Crea:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.3.json`

Debe registrar al menos:

```text
baseline main;
v01 y v02 rechazados / DO_NOT_INTEGRATE;
F005 y F006;
conservación F003/F004;
runner/config v03 path + Git blob + SHA256;
source/input bindings;
20 bank identities read-only;
preflight;
H100 shadow;
canonical authorization path guard;
authorization tracked/HEAD/working blob checks;
noncanonical path test;
unversioned authorization test;
dirty authorization test;
invalid package test;
consumed marker test;
descendant clean authorization model;
exact scoring-boundary consumption test;
failure-context test;
streaming evidence;
absence de autorización oficial;
absence de marcador real;
absence de output oficial;
zero H150/H200 scoring;
zero H150/H200 metrics/rankings observed;
no bank mutation;
cleanup temporal;
runtime checks = CODEX_LOCAL_* / NOT_INDEPENDENT_GITHUB_RUNTIME_OBSERVATION.
```

Estado máximo:

```text
status = CANDIDATE_PREEXECUTION_READY_V03_PENDING_EXTERNAL_AUDIT
execution_package_ready = true
execution_authorized = false
retrieval_executed = false
h150_h200_results_observed = false
future_authorization_required = true
EXP12_authorized = false
```

---

# 12. Criterio de éxito

Solo `COMPLETED` si:

```text
F005 = CLOSED
F006 = CLOSED
F003_NO_REGRESSION = PASS
F004_NO_REGRESSION = PASS
H100_FULL_OUTPUT_SHADOW = PASS
BANK_PREFLIGHT = PASS_EXACT_20_OF_20
NO_AUTH_GUARD = PASS
NONCANONICAL_AUTH_GUARD = PASS
UNVERSIONED_AUTH_GUARD = PASS
DIRTY_AUTH_GUARD = PASS
INVALID_PACKAGE_BINDING_GUARD = PASS
CONSUMED_AUTH_GUARD = PASS
DESCENDANT_AUTHORIZATION_MODEL = PASS
SCORING_BOUNDARY_CONSUMPTION_TEST = PASS
FAILURE_CONTEXT_TEST = PASS
STREAMING_OUTPUT_MODEL = PASS
OFFICIAL_OUTPUT_ROOT_EXISTS = false
OFFICIAL_AUTHORIZATION_EXISTS = false
REAL_CONSUMPTION_MARKER_EXISTS = false
H150_H200_SCORING_COUNT = 0
H150_H200_RESULTS_OBSERVED = false
```

Si falla cualquier condición bloqueante: `STOP`; no hagas retries alterando parámetros.

---

# 13. Restricciones Git

El candidato v03 debe:

```text
parent = 09ff184854659110f7711b3eee65fc18927649da
commits_ahead_of_main = 1
commits_behind_main = 0
changed_path_count = 3
```

Solo los tres paths v03/v0.3 autorizados pueden aparecer en el diff.

No integres el candidato a `main`.

No modifiques Plan, Article, EXP12, H100, DEV, EVAL, bancos oficiales, retrieval gate histórico, manifest/ledger, Prompt41 replay proof, portability closure ni bloques posteriores.

---

# 14. Prohibiciones absolutas

NO:

- crear autorización oficial;
- consumir autorización oficial real;
- ejecutar retrieval H150/H200;
- calcular/observar métricas H150/H200;
- calcular/observar rankings EVAL contra H150/H200;
- crear output root oficial;
- integrar/reusar/amendar v01 o v02;
- rematerializar bancos;
- cambiar BM25;
- retry/resume/overwrite;
- avanzar a EXP12, Grupo 2B o Grupo 3.

---

# 15. Persistencia administrativa

Después del trabajo científico:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch`;
3. no rebase/amend/force;
4. crea únicamente:

`codex_prompts_tmp/46_RESPUESTA_CERRAR_BINDING_CANONICO_AUTORIZACION_EXP11B.md`

5. persiste la respuesta en un commit administrativo separado;
6. no mezcles archivos científicos en ese commit.

---

# 16. Reporte obligatorio

Incluye como mínimo:

1. `COMPLETED` o `STOP`;
2. refs iniciales/finales;
3. estado v01/v02 rechazados;
4. resolución F005/F006 y no regresión F003/F004;
5. runner/config/readiness v03 paths + blobs + SHA256;
6. compile/import/CLI;
7. preflight único;
8. H100 shadow único;
9. guards de autorización canónica/versionada/dirty;
10. consumed/invalid/descendant tests;
11. scoring-boundary consumption test;
12. failure-context/streaming tests;
13. cero scoring/métricas/rankings H150/H200;
14. output/auth/marker oficial ausentes;
15. candidate branch/commit/parent/tree/ahead-behind/changed paths;
16. no cambios Plan/Article/EXP12;
17. ruta + commit administrativo de respuesta.

Estado máximo terminal:

```text
PROMPT46 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V03 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
