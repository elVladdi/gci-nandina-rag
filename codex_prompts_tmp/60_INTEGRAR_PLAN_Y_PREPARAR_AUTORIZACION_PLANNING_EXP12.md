# PROMPT 60 — INTEGRAR PLAN Y PREPARAR AUTORIZACIÓN ONE-SHOT DE PLANNING EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el candidato del Plan Maestro EXP12 pre-planning ya auditado externamente;
2. realizar las comprobaciones técnicas finales necesarias para un futuro planeamiento oficial EXP12, **sin ejecutar candidate generation**;
3. crear y publicar en una rama separada un **candidato de autorización one-shot exclusivamente para EXP12 PLANNING**, pendiente de auditoría externa.

Este bloque **NO ejecuta** `plan_exp12_historical_diversity_v01.py --execute-planning`, NO ejecuta los 10,000 candidatos por seed, NO selecciona D-HIGH/D-MID/D-LOW, NO materializa bancos EXP12, NO ejecuta retrieval/BM25/Top-k/MRR y NO autoriza la fase de retrieval/evaluación EXP12.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt59 concluye:

```text
PROMPT59_EXTERNAL_AUDIT = PASS / APPROVED
EXP12_PREPLANNING_CORRECTION_V01 = INTEGRATED / VERIFIED
PLAN_RECONCILIATION_EXP12_PREPLANNING = APPROVED_FOR_INTEGRATION
EXP12_PLANNING = NOT_YET_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato del Plan aprobado:

```text
branch = codex/plan-maestro-exp12-preplanning-v01
commit = 532f7ad93b01881817a6c8cec9f6eb486e37b684
parent = 00adb8f6fc668609500be913203be50a5d402554
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Estado científico/técnico que debe permanecer congelado:

```text
main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
config = src/configs/exp12_historical_diversity_control_v0.5.json
config_sha256 = 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264
runner = src/experiments/plan_exp12_historical_diversity_v01.py
runner_sha256 = cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac
sampling_universe = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
H100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
EVAL_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
TVD_support = FULL_REFERENCE_SUPPORT_PLUS_OTHER
maximum_tvd = 0.05
coverage = 1.0
target_rows = 2950
volume_range = [2802,3098]
candidate_count = 10000
minimum_unique_feasible = 30
seeds = [20262001..20262010]
quantiles = D-HIGH 0.1 / D-MID 0.5 / D-LOW 0.9
```

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/codex/plan-maestro-exp12-preplanning-v01 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato del Plan exige:

```text
parent = 00adb8f6fc668609500be913203be50a5d402554
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Si existe cualquier drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta del Plan

Integra exclusivamente:

```text
00adb8f6fc668609500be913203be50a5d402554
→
532f7ad93b01881817a6c8cec9f6eb486e37b684
```

mediante fast-forward exacto de:

```text
docs/plan-maestro-temporal-2026-08-31
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 4. Fase B — comprobaciones finales sin planeamiento

Trabaja sobre un checkout limpio del `main` exacto:

```text
6437a05325bdb01f3cd4964e1b0fae7d3641cc11
```

No ejecutes `--execute-planning`.

### 4.1 Identidad exacta de artefactos

Verifica SHA-256 de:

```text
src/configs/exp12_historical_diversity_control_v0.5.json
= 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264

src/experiments/plan_exp12_historical_diversity_v01.py
= cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac

data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
= f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457

data/processed/data_aduanas_historico_clase87_v0.2.csv
= 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff

data/processed/data_aduanas_evalset_clase87_v0.2.csv
= 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

Para archivos de texto sujetos exclusivamente a CRLF de checkout puedes registrar SHA de blob/canonical LF y SHA de worktree por separado, pero la identidad canónica debe coincidir exactamente con la congelada.

### 4.2 Validación estática de contrato

Sin generar candidatos:

- parsea JSON v0.5;
- ejecuta únicamente `validate_exp12_v05_contract(config)`;
- confirma que `execution_authorized=false` sigue siendo obligatorio;
- confirma que el CLI sin `--execute-planning` permanece fail-closed;
- no leas labels/descripciones/performance EVAL.

### 4.3 Estado de salida oficial

Reserva prospectivamente como salida oficial de planning:

```text
outputs/experiments/exp12_planning_v0.1/attempt_001
```

Exige antes de crear la autorización:

```text
OFFICIAL_OUTPUT_DIR_EXISTS = false
OFFICIAL_OUTPUT_DIR_TRACKED = false
OFFICIAL_OUTPUT_DIR_UNTRACKED = false
```

No crees todavía ese directorio.

Reserva prospectivamente el marcador de consumo:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_consumption_marker.json
```

Exige que no exista actualmente en tracked ni untracked. No lo crees todavía.

### 4.4 Comando exacto futuro

Congela exactamente la futura invocación lógica:

```text
python src/experiments/plan_exp12_historical_diversity_v01.py \
  --config src/configs/exp12_historical_diversity_control_v0.5.json \
  --sampling-universe data/interim/new_historical_gate_v0.2/new_historical_eligible.csv \
  --h100 data/processed/data_aduanas_historico_clase87_v0.2.csv \
  --eval data/processed/data_aduanas_evalset_clase87_v0.2.csv \
  --output-dir outputs/experiments/exp12_planning_v0.1/attempt_001 \
  --execute-planning
```

La ruta Python concreta del entorno puede registrarse como runtime detail en la ejecución futura; la semántica y argumentos anteriores no pueden cambiar.

---

## 5. Fase C — candidato de autorización one-shot de PLANNING

Desde exactamente:

```text
6437a05325bdb01f3cd4964e1b0fae7d3641cc11
```

crea la rama:

```text
codex/exp12-planning-authorization-v01
```

Crea un solo commit que añada exclusivamente:

```text
outputs/audits/exp12_planning_gate_v0.3/exp12_planning_execution_authorization_v0.1.json
```

No modifiques código, config, tests, datos, Plan ni Article.

### 5.1 Contenido mínimo obligatorio

El JSON debe incluir como mínimo:

```text
artifact = EXP12_PLANNING_EXECUTION_AUTHORIZATION
version = v0.1
authorization_id = EXP12_PLANNING_AUTH_001
attempt_id = EXP12_PLANNING_ATTEMPT_001
status = AUTHORIZED_ONE_SHOT
scope = EXP12_PLANNING_ONLY_10000_CANDIDATES_X_10_SEEDS_NO_RETRIEVAL

effective_only_if_external_audit_passes = true
effective_only_if_integrated_to_main = true
single_use = true
retry_allowed = false
resume_allowed = false
overwrite_allowed = false
partial_recomputation_allowed = false

execution_base_commit = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
config_path = src/configs/exp12_historical_diversity_control_v0.5.json
config_sha256 = 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264
runner_path = src/experiments/plan_exp12_historical_diversity_v01.py
runner_sha256 = cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac
sampling_universe_path = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
h100_path = data/processed/data_aduanas_historico_clase87_v0.2.csv
h100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
eval_path = data/processed/data_aduanas_evalset_clase87_v0.2.csv
eval_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
eval_usage = DECLARACION_OVERLAP_ONLY

candidate_count_per_seed = 10000
seed_schedule = [20262001,20262002,20262003,20262004,20262005,20262006,20262007,20262008,20262009,20262010]
target_rows = 2950
volume_range = [2802,3098]
required_label_coverage_fraction = 1.0
maximum_tvd = 0.05
tvd_support = FULL_REFERENCE_SUPPORT_PLUS_OTHER
minimum_unique_feasible_candidates = 30
quantiles = {D-HIGH:0.1,D-MID:0.5,D-LOW:0.9}
strict_hhi_order = HHI_DLOW > HHI_DMID > HHI_DHIGH

output_dir = outputs/experiments/exp12_planning_v0.1/attempt_001
consumption_marker_path = outputs/audits/exp12_planning_gate_v0.3/exp12_planning_attempt_001_consumption_marker.json

planning_only = true
retrieval_authorized = false
bm25_authorized = false
top_k_authorized = false
mrr_authorized = false
exp12_retrieval_authorized = false
group2b_authorized = false
group3_authorized = false
```

Incluye el comando lógico exacto congelado en 4.4.

Registra también resultados de las verificaciones de 4.1–4.3 y:

```text
candidate_generation_executed = false
planning_executed = false
condition_selection_executed = false
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
eval_labels_read = false
eval_descriptions_read = false
eval_performance_read = false
```

### 5.2 Semántica one-shot prospectiva

El futuro ejecutor, solo después de integración y nueva aprobación externa, deberá:

1. comprobar nuevamente refs, SHAs, clean state y ausencia del output dir/marker;
2. crear **primero** el marcador de consumo con estado `CONSUMED_EXECUTION_STARTED` inmediatamente antes de la invocación oficial;
3. ejecutar exactamente una invocación;
4. no reintentar, reanudar, sobrescribir ni completar parcialmente si falla;
5. conservar y versionar el marcador aun si la ejecución falla;
6. someter resultados o fallo a auditoría externa antes de cualquier siguiente bloque.

No crees el marcador en Prompt60.

---

## 6. Prohibiciones absolutas

Durante Prompt60 NO:

- ejecutes `--execute-planning`;
- ejecutes `generate_exp12_candidates` sobre el pool oficial;
- ejecutes los 10,000 candidatos por seed;
- selecciones condiciones oficiales;
- calcules HHI/TVD oficiales por seed;
- materialices bancos EXP12;
- leas labels/descripciones/performance EVAL;
- ejecutes retrieval/BM25/Top-k/MRR;
- modifiques v0.5, runner, tests o datasets;
- cambies thresholds, seeds, quantiles, volumen o candidate_count;
- autorices retrieval EXP12;
- avances a Grupo 2B o Grupo 3.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
origin/docs/plan-maestro-temporal-2026-08-31 = 532f7ad93b01881817a6c8cec9f6eb486e37b684
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato de autorización:

```text
parent = 6437a05325bdb01f3cd4964e1b0fae7d3641cc11
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/exp12_planning_gate_v0.3/exp12_planning_execution_authorization_v0.1.json
```

Y:

```text
EXP12_PLANNING_EXECUTED = false
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
codex_prompts_tmp/60_RESPUESTA_INTEGRAR_PLAN_Y_PREPARAR_AUTORIZACION_PLANNING_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT60 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

PLAN_RECONCILIATION_INTEGRATED = true/false
PLAN_INTEGRATION_MODE

AUTHORIZATION_BRANCH
AUTHORIZATION_COMMIT
AUTHORIZATION_PARENT
AUTHORIZATION_CHANGED_PATH_COUNT
AUTHORIZATION_CHANGED_PATHS
AUTHORIZATION_PUBLISHED

AUTHORIZATION_ID
ATTEMPT_ID
AUTHORIZATION_STATUS
AUTHORIZATION_SCOPE
OUTPUT_DIR
OUTPUT_DIR_EXISTS
CONSUMPTION_MARKER_PATH
CONSUMPTION_MARKER_EXISTS

CONFIG_SHA_VALIDATION
RUNNER_SHA_VALIDATION
POOL_SHA_VALIDATION
H100_SHA_VALIDATION
EVAL_SHA_VALIDATION
V05_VALIDATOR_RETURN
CLI_WITHOUT_EXECUTE_PLANNING_RETURN

EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_RETRIEVAL_AUTHORIZED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT60 = COMPLETED
PLAN_RECONCILIATION_EXP12_PREPLANNING = INTEGRATED
EXP12_PLANNING_AUTHORIZATION_V01 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP12_PLANNING_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
