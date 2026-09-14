# PROMPT 61 — INTEGRAR AUTORIZACIÓN Y EJECUTAR ONE-SHOT PLANNING EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto la autorización one-shot de **EXP12 PLANNING** ya auditada externamente;
2. ejecutar un preflight final sobre un checkout limpio y aislado;
3. consumir la autorización inmediatamente antes de la ejecución oficial;
4. ejecutar **exactamente una vez** el planeamiento EXP12 congelado: 10,000 candidatos por cada uno de los 10 seeds;
5. versionar, en una rama separada, los resultados o la evidencia de fallo para auditoría externa.

Este bloque **NO ejecuta retrieval**, BM25, Top-k, MRR ni evaluación EXP12. No abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt60 concluye:

```text
PROMPT60_EXTERNAL_AUDIT = PASS / APPROVED
PLAN_RECONCILIATION_EXP12_PREPLANNING = INTEGRATED / VERIFIED
EXP12_PLANNING_AUTHORIZATION_V01 = APPROVED_FOR_INTEGRATION_AND_ONE_SHOT_PLANNING
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato de autorización aprobado:

```text
branch = codex/exp12-planning-authorization-v01
commit = 9428cb3dd205069f02c23ce16c7a9bbc874a0df1
parent = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.3/exp12_planning_execution_authorization_v0.1.json
```

Identidad de autorización:

```text
authorization_id = EXP12_PLANNING_AUTH_001
attempt_id = EXP12_PLANNING_ATTEMPT_001
status = AUTHORIZED_ONE_SHOT
scope = EXP12_PLANNING_ONLY_10000_CANDIDATES_X_10_SEEDS_NO_RETRIEVAL
single_use = true
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false
```

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
origin/codex/exp12-planning-authorization-v01 = 9428cb3dd205069f02c23ce16c7a9bbc874a0df1
origin/docs/plan-maestro-temporal-2026-08-31 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para la autorización exige:

```text
parent = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.3/exp12_planning_execution_authorization_v0.1.json
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta de la autorización

Integra exclusivamente:

```text
6437a05325bdb01f3cd4964e1b0fae7d3641cc11
→
9428cb3dd205069f02c23ce16c7a9bbc874a0df1
```

mediante fast-forward exacto de `main`.

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = 9428cb3dd205069f02c23ce16c7a9bbc874a0df1
origin/docs/plan-maestro-temporal-2026-08-31 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

La integración de la autorización no cambia código, config, datos ni parámetros científicos.

---

## 4. Fase B — checkout aislado y preflight final

Realiza la ejecución desde un **checkout/worktree nuevo, aislado y limpio** del commit exacto:

```text
9428cb3dd205069f02c23ce16c7a9bbc874a0df1
```

No uses un working tree que contenga modificaciones locales del workbook u otros archivos del usuario.

Antes de consumir la autorización exige:

```text
TRACKED_WORKING_TREE_CLEAN = true
```

Verifica otra vez la autorización integrada y los bindings exactos:

```text
config = src/configs/exp12_historical_diversity_control_v0.5.json
config_sha256 = 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264

runner = src/experiments/plan_exp12_historical_diversity_v01.py
runner_sha256 = cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac

sampling_universe = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457

H100 = data/processed/data_aduanas_historico_clase87_v0.2.csv
H100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff

EVAL = data/processed/data_aduanas_evalset_clase87_v0.2.csv
EVAL_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

Para texto con CRLF de checkout, acepta únicamente la misma regla ya auditada: identidad canónica Git/LF exacta y worktree diferente solo por CRLF. No aceptes ninguna diferencia de contenido.

Ejecuta únicamente las comprobaciones no científicas siguientes:

1. parse JSON v0.5;
2. `validate_exp12_v05_contract(config)` = PASS;
3. confirma `execution_authorized=false` en config, porque la autorización operacional es el JSON one-shot integrado, no una mutación del contrato;
4. invoca el CLI **sin** `--execute-planning` y exige retorno fail-closed `2 / NOT_EXECUTED`;
5. no leas NANDINA, descripción ni performance de EVAL; el runner oficial solo puede usar `DECLARACION` para overlap.

### 4.1 Ausencia de ejecución previa

Exige inmediatamente antes del consumo:

```text
OUTPUT_DIR = outputs/experiments/exp12_planning_v0.1/attempt_001
OUTPUT_DIR_EXISTS = false
OUTPUT_DIR_TRACKED = false
OUTPUT_DIR_UNTRACKED = false

CONSUMPTION_MARKER = outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_consumption_marker.json
CONSUMPTION_MARKER_EXISTS = false
CONSUMPTION_MARKER_TRACKED = false
CONSUMPTION_MARKER_UNTRACKED = false
```

Si cualquiera existe:

```text
STOP / AUTHORIZATION_NOT_PRISTINE
```

No borres, renombres ni sobrescribas nada para hacer pasar este gate.

---

## 5. Fase C — consumo one-shot

Solo si todas las comprobaciones anteriores pasan, crea **inmediatamente antes de la invocación oficial**:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_consumption_marker.json
```

El marcador debe incluir como mínimo:

```text
artifact = EXP12_PLANNING_CONSUMPTION_MARKER
version = v0.1
authorization_id = EXP12_PLANNING_AUTH_001
attempt_id = EXP12_PLANNING_ATTEMPT_001
status = CONSUMED_EXECUTION_STARTED
authorization_commit = 9428cb3dd205069f02c23ce16c7a9bbc874a0df1
scientific_base_commit = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
consumed_at_utc = <UTC timestamp>
logical_command = <exact command below>
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false
```

Una vez creado el marcador, la autorización queda consumida aunque la ejecución falle.

---

## 6. Fase D — única ejecución oficial de planning

Ejecuta **exactamente una vez** la siguiente invocación lógica, usando el Python disponible del entorno sin cambiar argumentos ni semántica:

```text
python src/experiments/plan_exp12_historical_diversity_v01.py \
  --config src/configs/exp12_historical_diversity_control_v0.5.json \
  --sampling-universe data/interim/new_historical_gate_v0.2/new_historical_eligible.csv \
  --h100 data/processed/data_aduanas_historico_clase87_v0.2.csv \
  --eval data/processed/data_aduanas_evalset_clase87_v0.2.csv \
  --output-dir outputs/experiments/exp12_planning_v0.1/attempt_001 \
  --execute-planning
```

Registra:

```text
EXECUTION_START_UTC
EXECUTION_END_UTC
RUNTIME_PYTHON_PATH
RUNTIME_PYTHON_VERSION
EXIT_CODE
STDOUT
STDERR
```

No ejecutes ninguna segunda invocación bajo ninguna circunstancia.

Si hay error, excepción, timeout, interrupción o salida no cero:

```text
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
```

No reintentes, no reanudes, no completes parcialmente y no reconstruyas resultados.

Si la ejecución termina con código 0:

```text
EXP12_PLANNING_ATTEMPT_001 = COMPLETED_ONE_SHOT / PENDING_EXTERNAL_AUDIT
```

---

## 7. Fase E — verificación post-ejecución sin recomputación

**No vuelvas a ejecutar candidate generation.** Inspecciona únicamente los outputs producidos por la invocación oficial.

En caso de éxito exige:

```text
outputs/experiments/exp12_planning_v0.1/attempt_001/exp12_planning_summary_v0.1.json
```

Verifica estáticamente, sin recomputar candidatos:

- `artifact = EXP12_PLANNING_ONLY`;
- exactamente 10 runs;
- seeds exactamente `20262001..20262010`, una vez cada uno;
- `candidate_count_attempted = 10000` en cada run;
- `unique_feasible_candidate_count >= 30` en cada run;
- exactamente `D-HIGH`, `D-MID`, `D-LOW` por run;
- tres DAM sets distintos por run;
- para cada candidato seleccionado: filas `[2802,3098]`, coverage `1.0`, TVD `<=0.05`;
- `HHI_DLOW > HHI_DMID > HHI_DHIGH` en cada run;
- existen los 8 descriptores de manipulación congelados por run;
- `duplicate_triplet_structure` queda reportado tal como resulte, sin reemplazo automático;
- `retrieval_executed=false`, `bm25_executed=false`, `top_k_computed=false`, `mrr_computed=false`.

No uses el resultado para cambiar thresholds, seeds, quantiles, TVD, volumen ni candidate_count.

En caso de fallo, conserva exactamente el estado parcial que exista y no lo conviertas en éxito.

---

## 8. Evidencia de ejecución y versionado

Crea, después de terminar la única invocación, un reporte:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_execution_report_v0.1.json
```

Debe contener como mínimo:

- identidad de autorización/attempt;
- autorización commit y scientific base commit;
- timestamps y runtime Python;
- comando lógico exacto;
- exit code;
- estado `COMPLETED_ONE_SHOT_PENDING_EXTERNAL_AUDIT` o `FAILED_ONE_SHOT_AUTHORIZATION_CONSUMED`;
- hashes SHA-256 del marcador, stdout, stderr y de cada output que exista;
- resumen de las verificaciones post-ejecución;
- flags explícitos de que no hubo retry/resume/overwrite/partial recomputation;
- `retrieval_executed=false`, `bm25_executed=false`, `top_k_computed=false`, `mrr_computed=false`;
- `eval_labels_read=false`, `eval_descriptions_read=false`, `eval_performance_read=false`.

Guarda stdout y stderr exactamente en:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stdout.log
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stderr.log
```

Desde exactamente el commit integrado de autorización:

```text
9428cb3dd205069f02c23ce16c7a9bbc874a0df1
```

crea la rama:

```text
codex/exp12-planning-attempt001-evidence-v01
```

Un solo commit de evidencia. Puede añadir exclusivamente:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_consumption_marker.json
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_execution_report_v0.1.json
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stdout.log
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_stderr.log
outputs/experiments/exp12_planning_v0.1/attempt_001/**
```

No modifiques código, config, tests, data, Plan ni Article. Publica la rama para auditoría externa. **No la integres a main.**

Si la ejecución falla antes de producir el summary, versiona de todos modos marcador, logs, reporte y cualquier output parcial existente dentro de los paths permitidos.

---

## 9. Prohibiciones absolutas

Durante Prompt61 NO:

- ejecutes una segunda invocación oficial;
- reintentes o reanudes tras fallo;
- sobrescribas output_dir;
- realices candidate generation adicional para verificar resultados;
- modifiques v0.5, runner, tests o datasets;
- cambies thresholds, seeds, quantiles, volumen o candidate_count;
- ejecutes retrieval/BM25/Top-k/MRR;
- leas labels/descripciones/performance EVAL;
- autorices retrieval EXP12;
- modifiques Plan o Article;
- avances a Grupo 2B o Grupo 3.

---

## 10. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/61_RESPUESTA_INTEGRAR_AUTORIZACION_Y_EJECUTAR_ONE_SHOT_PLANNING_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 11. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT61 = COMPLETED | FAILED_ONE_SHOT | STOP

main_initial
main_final
plan_final
article_final

AUTHORIZATION_INTEGRATED
AUTHORIZATION_ID
ATTEMPT_ID
AUTHORIZATION_CONSUMED
CONSUMPTION_MARKER_PATH
CONSUMPTION_MARKER_SHA256

EXECUTION_START_UTC
EXECUTION_END_UTC
RUNTIME_PYTHON_PATH
RUNTIME_PYTHON_VERSION
OFFICIAL_INVOCATION_COUNT
EXIT_CODE
RETRY_EXECUTED
RESUME_EXECUTED
OVERWRITE_EXECUTED
PARTIAL_RECOMPUTATION_EXECUTED

EVIDENCE_BRANCH
EVIDENCE_COMMIT
EVIDENCE_PARENT
EVIDENCE_CHANGED_PATHS
EXECUTION_REPORT_PATH
PLANNING_SUMMARY_PATH

SEED_RUN_COUNT
SEEDS_OBSERVED
CANDIDATE_COUNT_ATTEMPTED_PER_SEED
UNIQUE_FEASIBLE_COUNTS
STRICT_HHI_ORDER_ALL_RUNS
SELECTED_CONSTRAINTS_ALL_RUNS
DUPLICATE_TRIPLET_STRUCTURE

EXP12_PLANNING_ATTEMPT_001
EXP12_RETRIEVAL_EXECUTED = false
BM25_EXECUTED = false
TOP_K_COMPUTED = false
MRR_COMPUTED = false
EXP12_RETRIEVAL_AUTHORIZED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Terminal de éxito:

```text
PROMPT61 = COMPLETED
EXP12_PLANNING_ATTEMPT_001 = COMPLETED_ONE_SHOT / PENDING_EXTERNAL_AUDIT
AUTHORIZATION_CONSUMED = true
OFFICIAL_INVOCATION_COUNT = 1
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Terminal de fallo después de consumir autorización:

```text
PROMPT61 = FAILED_ONE_SHOT
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
AUTHORIZATION_CONSUMED = true
OFFICIAL_INVOCATION_COUNT = 1
NO_RETRY = true
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
