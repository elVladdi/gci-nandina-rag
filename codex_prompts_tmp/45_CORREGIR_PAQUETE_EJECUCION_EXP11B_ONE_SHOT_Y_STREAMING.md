# PROMPT 45 — CORREGIR PAQUETE DE EJECUCIÓN EXP11B: ONE-SHOT, BINDING DE AUTORIZACIÓN Y STREAMING

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Debes corregir exclusivamente el paquete prospectivo de ejecución de `EXP11B Retrieval H150/H200` producido por Prompt44. Este bloque sigue siendo **pre-ejecución**: NO autoriza ni ejecuta retrieval oficial H150/H200 y NO puede observar métricas ni rankings H150/H200.

El objetivo es cerrar cuatro hallazgos bloqueantes/preventivos detectados por la auditoría externa de IA Experimental antes de integrar cualquier paquete y antes de emitir una autorización one-shot.

---

# 1. Dictamen externo que gobierna este bloque

El candidato Prompt44 queda rechazado como paquete oficial:

```text
PROMPT44_EXTERNAL_AUDIT = REJECTED / CORRECTION_REQUIRED

EXP11B_RETRIEVAL_EXECUTION_PACKAGE = NOT_APPROVED_FOR_INTEGRATION
candidate_26b9e2bcf6dad74231f208f9137ffb0e39caf2e1 = DO_NOT_INTEGRATE

F001 = ONE_SHOT_AUTHORIZATION_NOT_CONSUMED
F002 = PACKAGE_COMMIT_BINDING_INCOMPATIBLE_WITH_VERSIONED_AUTHORIZATION
F003 = HIGH_MEMORY_ACCUMULATION_PREVENTABLE_ONE_SHOT_RISK
F004 = FAILURE_LEDGER_CAN_MISIDENTIFY_FAILING_BANK

EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

La auditoría externa NO rechaza la semántica BM25 ni el principio de reutilización de helpers de Prompt44. El problema está en la capa de control de ejecución oficial y en riesgos técnicos previsibles.

El candidato rechazado es evidencia histórica inmutable. **No lo integres, no lo amend, no hagas rebase sobre él y no uses su commit como parent del nuevo candidato.**

---

# 2. Baseline y refs obligatorias

Antes de modificar nada, ejecuta `git fetch` y verifica exactamente:

```text
origin/main = 09ff184854659110f7711b3eee65fc18927649da
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/exp11b-retrieval-execution-package-v01 = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1
```

Verifica también:

```text
26b9e2bc... parent = 09ff184854659110f7711b3eee65fc18927649da
26b9e2bc... is NOT ancestor of origin/main
EXP11B_PORTABILITY_DEBT = CLOSED / APPROVED / INTEGRATED
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Si cualquier ref canónica cambió respecto de lo anterior: `STOP / PRECONDITION_REF_DRIFT`.

---

# 3. Nuevo candidato limpio

Crea desde `origin/main = 09ff184...` una rama nueva:

`codex/exp11b-retrieval-execution-package-v02`

El parent directo del único commit científico del candidato debe ser exactamente `09ff184854659110f7711b3eee65fc18927649da`.

No cherry-pickees el candidato v01 rechazado. Puedes consultar su contenido como referencia, pero el nuevo candidato debe reconstruirse limpiamente desde `main`.

El candidato v02 puede añadir exclusivamente estos tres paths nuevos:

```text
src/experiments/run_exp11b_historical_retrieval_h150_h200_v02.py
src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.2.json
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.2.json
```

No modifiques ningún archivo científico existente.

---

# 4. Semántica científica que debe permanecer idéntica

La corrección NO autoriza cambiar el método científico. El runner v02 debe seguir reutilizando directamente los helpers canónicos versionados de EXP-04/EXP11A y mantener exactamente:

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

No copies ni redefinas la fórmula BM25 si puedes reutilizar los helpers existentes. No cambies resultados H100 esperados ni tolerancias.

---

# 5. Corrección obligatoria F001 — consumo one-shot real

El runner v02 debe impedir técnicamente que una misma autorización oficial sea reutilizada después de que la ejecución haya comenzado, aunque la corrida falle, sea interrumpida o no llegue a instalar el output final.

La autorización futura deberá contener, como mínimo:

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

Define una ruta gobernada para marcadores de intento/consumo, por ejemplo:

`outputs/audits/exp11b_retrieval_execution_attempts/`

La implementación debe cumplir esta secuencia:

```text
1. validar autorización y bindings;
2. ejecutar todas las validaciones preflight que todavía no consumen la autorización;
3. verificar que output oficial no existe;
4. inmediatamente antes del primer scoring oficial, crear de forma ATÓMICA/EXCLUSIVA un marcador de consumo para authorization_id + attempt_id;
5. si el marcador ya existe: bloquear antes de scoring;
6. una vez creado, la autorización queda consumida aunque el proceso falle después;
7. un retry oficial solo puede existir con una autorización prospectiva nueva y otro authorization_id/attempt_id.
```

La creación del marcador debe usar semántica exclusiva (`open(..., 'x')`, `O_CREAT|O_EXCL` o equivalente) para que dos procesos concurrentes no puedan consumir la misma autorización.

El marcador debe registrar al menos:

```text
authorization_id
attempt_id
approved_package_commit
execution_head
started_at_utc
status = CONSUMED_EXECUTION_STARTED
```

Si después ocurre un fallo, el marcador NO se elimina ni se sobrescribe. Debe quedar como evidencia de que la autorización fue consumida.

No crees un marcador real oficial en Prompt45. Las pruebas de esta lógica deben usar únicamente un directorio temporal aislado.

---

# 6. Corrección obligatoria F002 — binding correcto de package commit

El v01 rechazado equiparaba el `package_commit` de autorización con `HEAD`, lo cual es incompatible con una autorización versionada creada después de integrar el paquete.

Corrige el contrato así:

```text
approved_package_commit = commit científico exacto del paquete v02 aprobado e integrado
execution_head = HEAD desde el que se ejecuta posteriormente
```

El runner futuro debe aceptar que `execution_head` sea un descendiente del `approved_package_commit`, por ejemplo porque contiene posteriormente el artefacto de autorización.

Antes de ejecutar debe verificar como mínimo:

```text
approved_package_commit existe;
approved_package_commit es ancestro de execution_head;
runner/config en approved_package_commit tienen exactamente los blobs/hashes autorizados;
runner/config del working tree/HEAD usado para ejecutar son byte-idénticos a esos bindings;
EVAL, manifest, ledger, closure record y demás bindings científicos coinciden;
```

No permitas que un commit posterior modifique runner/config manteniendo una autorización antigua.

Construye un test local no científico que simule una autorización situada en un descendiente versionado y demuestre que este modelo de binding es válido sin ejecutar H150/H200.

---

# 7. Corrección obligatoria F003 — escritura incremental y memoria acotada

No acumules en RAM todos los candidatos de los 20 bancos.

La ejecución oficial prospectiva debe escribir en **staging** de forma incremental, al menos:

```text
exp11b_retrieval_case_level_v0.1.csv
exp11b_retrieval_candidates_v0.1.csv
```

Usa writers abiertos sobre archivos temporales/staging y escribe/flush por banco o por lotes acotados.

Puedes mantener en memoria únicamente estructuras pequeñas necesarias para:

```text
métricas por banco;
summary por condición;
manifest/estado;
hashes/metadatos finales.
```

La semántica de ranking y métricas no cambia. La corrección es exclusivamente de robustez operacional.

En caso de fallo después de consumir autorización, preserva el staging/failure evidence según la política fail-closed. No conviertas resultados parciales en resultados oficiales.

---

# 8. Corrección obligatoria F004 — identificación inequívoca del fallo

Antes de iniciar cada banco, mantén variables explícitas:

```text
current_run_id
current_bank_id
current_condition
current_stage
```

Actualiza `current_stage` en pasos auditables, por ejemplo:

```text
BANK_VALIDATION
INDEX_BUILD
EVAL_SCORING
CASE_WRITE
METRIC_FINALIZATION
OUTPUT_FINALIZATION
```

Si hay excepción, el failure ledger debe registrar el banco/run/stage realmente activo, no el último banco completado.

Si el fallo ocurre antes de seleccionar banco, usa una clasificación explícita como `NOT_STARTED`.

---

# 9. Shadow test H100 del contrato completo de output

Sin abrir ningún banco H150/H200, ejecuta exactamente una vez un shadow/self-test H100 temporal que ejercite **la misma capa de serialización/escritura que usaría la ejecución oficial**.

Debe generar en un directorio temporal, validar y luego eliminar al menos equivalentes temporales de:

```text
run manifest
metrics by bank
case level
candidate ranking
condition summary o equivalente de self-test
output hash ledger
environment
failure representation/schema cuando aplique
```

Valida los headers/campos requeridos contra el `future_output_contract` congelado del retrieval gate.

El H100 debe reproducir:

```text
Top1 numerator = 538
Top3 numerator = 709
Top5 numerator = 806
Top10 numerator = 941
Top50 numerator = 1047
MRR = 0.6297077493524843
MRR abs tolerance = 1e-12
```

Debe finalizar con cleanup temporal PASS.

No abras ni leas ningún CSV H150/H200 durante este shadow test.

---

# 10. CLI y modos

Mantén separación inequívoca entre:

```text
--preflight
--self-test-h100
--execute-official
```

`--execute-official` continúa bloqueado porque el artefacto real de autorización todavía no existe.

No crees autorización oficial en Prompt45.

---

# 11. Pruebas preventivas obligatorias

Sin ejecutar H150/H200, ejecuta y registra:

```text
A. py_compile/import/CLI help = PASS
B. config JSON/bindings estáticos = PASS
C. --preflight exactamente una vez = PASS
D. --self-test-h100 exactamente una vez = PASS, usando serialización completa temporal
E. --execute-official sin autorización = BLOCKED_BEFORE_SCORING
F. autorización simulada con approved_package_commit inválido = BLOCKED_BEFORE_SCORING
G. simulación temporal de marcador ya consumido = BLOCKED_BEFORE_SCORING
H. simulación estática/local de autorización en commit descendiente con package binding válido = PASS_CONTRACT_MODEL, sin scoring oficial
I. test de failure-context sintético/local = identifica correctamente current_bank_id/current_run_id/current_stage
J. memoria/acumulación: demostrar por inspección/test que candidates/case-level no se acumulan globalmente para 20 bancos
```

Las autorizaciones y marcadores usados en F–I deben ser temporales/sintéticos, fuera de las rutas oficiales, y eliminarse al finalizar.

Ninguno de estos tests puede ejecutar scoring H150/H200.

---

# 12. Validación read-only de bancos

`--preflight` puede leer/validar los 20 bancos oficiales, pero no calcular rankings ni métricas.

Debe exigir nuevamente:

```text
bank_count = 20
H150_count = 10
H200_count = 10
bank_identity_mismatch_count = 0
eval_sha_match = true
canonical_source_binding_mismatch_count = 0
official_output_root_exists = false
official_bank_write_count = 0
official_bank_content_mutated = false
```

No rematerialices bancos.

---

# 13. Config v0.2

Crea:

`src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.2.json`

Debe conservar el diseño científico de v0.1 y añadir explícitamente:

```text
contract_status = CANDIDATE_EXECUTION_PACKAGE_V02_PENDING_EXTERNAL_AUDIT
execution_authorized = false
execution_executed = false
one_shot_consumption_required = true
reuse_same_authorization_after_start = false
new_authorization_required_after_failure = true
approved_package_commit_must_be_ancestor_of_execution_head = true
runner_config_byte_identity_required = true
stream_case_level_output = true
stream_candidate_output = true
partial_outputs_are_official = false
```

Debe definir las rutas y schemas prospectivos de autorización/consumo, pero no crear artefactos oficiales.

Bindear por path + hash/blob todos los inputs/código relevantes igual o más estrictamente que Prompt44.

---

# 14. Readiness v0.2

Crea:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.2.json`

Debe registrar de forma auditable:

```text
baseline main;
candidato rechazado v01 y su estado DO_NOT_INTEGRATE;
F001-F004 y su resolución;
runner/config v02 path + blob + SHA256;
source/input bindings;
20 bank identities read-only;
preflight;
H100 full-output shadow test;
negative authorization tests;
one-shot consumption test;
descendant authorization binding test;
failure-context test;
streaming/bounded-memory evidence;
absence of official authorization;
absence of real official consumption marker;
absence of official output root;
zero H150/H200 scoring;
zero H150/H200 metrics/rankings observed;
no bank mutation;
cleanup temporal;
classification of all runtime checks as CODEX_LOCAL_* / NOT_INDEPENDENT_GITHUB_RUNTIME_OBSERVATION.
```

Estado máximo permitido:

```text
status = CANDIDATE_PREEXECUTION_READY_V02_PENDING_EXTERNAL_AUDIT
execution_package_ready = true
execution_authorized = false
retrieval_executed = false
h150_h200_results_observed = false
future_authorization_required = true
EXP12_authorized = false
```

---

# 15. Criterio de éxito del Prompt45

Prompt45 solo puede declarar `COMPLETED` si:

```text
F001 = CLOSED
F002 = CLOSED
F003 = CLOSED
F004 = CLOSED
H100_FULL_OUTPUT_SHADOW = PASS
BANK_PREFLIGHT = PASS_EXACT_20_OF_20
NO_AUTH_GUARD = PASS
INVALID_PACKAGE_BINDING_GUARD = PASS
CONSUMED_AUTH_GUARD = PASS
DESCENDANT_AUTHORIZATION_MODEL = PASS
FAILURE_CONTEXT_TEST = PASS
STREAMING_OUTPUT_MODEL = PASS
OFFICIAL_OUTPUT_ROOT_EXISTS = false
OFFICIAL_AUTHORIZATION_EXISTS = false
REAL_CONSUMPTION_MARKER_EXISTS = false
H150_H200_SCORING_COUNT = 0
H150_H200_RESULTS_OBSERVED = false
```

Si cualquier condición bloqueante falla: `STOP`, registra evidencia y no abras un nuevo intento automático.

---

# 16. Restricciones Git

El candidato v02 debe:

```text
parent = 09ff184854659110f7711b3eee65fc18927649da
commits_ahead_of_main = 1
commits_behind_main = 0
changed_path_count = 3
```

Únicamente los tres paths v0.2/v02 autorizados pueden aparecer en el diff.

No integres el candidato a `main`.

No modifiques:

```text
Plan Maestro
Article
EXP12
H100
DEV
EVAL
20 bancos oficiales
retrieval gate histórico
materialization manifest/ledger
Prompt41 replay proof
portability closure record
Attempt06
Grupo 2B
Grupo 3
```

---

# 17. Prohibiciones absolutas

NO:

- crear la autorización oficial futura;
- consumir una autorización oficial real;
- ejecutar retrieval H150/H200;
- calcular/observar métricas H150/H200;
- calcular/observar rankings EVAL contra H150/H200;
- crear el output root oficial;
- reusar/integrar/amendar el candidato v01 rechazado;
- rematerializar bancos;
- modificar parámetros BM25 para lograr PASS;
- hacer retries silenciosos;
- hacer resume;
- promover resultados temporales como oficiales;
- avanzar a EXP12, Grupo 2B o Grupo 3.

---

# 18. Persistencia administrativa

Después del trabajo científico:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch`;
3. no rebase/amend/force;
4. crea únicamente:

`codex_prompts_tmp/45_RESPUESTA_CORREGIR_PAQUETE_EJECUCION_EXP11B_ONE_SHOT_Y_STREAMING.md`

5. persiste esa respuesta en un commit administrativo separado;
6. no mezcles archivos científicos en el commit administrativo.

---

# 19. Reporte obligatorio

El reporte debe incluir:

```text
estado terminal COMPLETED/STOP;
refs iniciales/finales;
confirmación de candidato v01 rechazado/no integrado;
resolución claim-by-claim F001-F004;
runner/config/readiness v02 blobs + SHA256;
resultado de preflight 20/20;
H100 full-output shadow test y schemas;
resultado guard sin autorización;
resultado invalid package binding;
resultado consumed-authorization guard;
resultado descendant authorization model;
resultado failure-context test;
evidencia de streaming/memoria acotada;
confirmación de cero H150/H200 scoring/metrics/rankings;
confirmación de output oficial ausente;
confirmación de autorización oficial real ausente;
confirmación de marcador real ausente;
branch/commit/parent/tree/ahead-behind/diff exacto;
Plan/Article/EXP12 sin cambios;
ruta y commit administrativo de la respuesta.
```

Estado máximo terminal permitido:

```text
PROMPT45 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE_V02 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
