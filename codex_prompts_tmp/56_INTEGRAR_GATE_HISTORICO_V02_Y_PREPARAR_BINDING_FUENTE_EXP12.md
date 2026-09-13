# PROMPT 56 — INTEGRAR GATE HISTÓRICO v0.2 Y PREPARAR BINDING DE FUENTE EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente dos operaciones, en este orden:

1. integrar mediante fast-forward exacto el candidato histórico v0.2 aprobado externamente;
2. crear un **candidato separado de binding de fuente EXP12 v0.4**, sin ejecutar planeamiento, candidate generation, retrieval, BM25, Top-k ni MRR.

Este bloque **NO autoriza EXP12**, NO ejecuta EXP12, NO modifica H100/DEV/EVAL, NO modifica Article y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt55 concluye:

```text
PROMPT55_EXTERNAL_AUDIT = PASS / APPROVED_FOR_INTEGRATION
NEW_HISTORICAL_GATE_EXTENSION_V02 = APPROVED_FOR_INTEGRATION
EXP12_EXTENSION_COVERAGE_STATUS = PASS_66_OF_66_CANDIDATE
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

El usuario confirmó además, como declaración metodológica de procedencia:

```text
NUEVA_02_DAM_COMPLETENESS = COMPLETE_DAMS_WITH_ALL_ORIGINAL_SERIES
NUEVA_02_ACQUISITION_METHOD = SAME_SEARCH_EXTRACTION_COPY_METHOD_AS_INITIAL_DATA_AND_NUEVA_01
NUEVA_02_SOURCE_SELECTION_PURPOSE = COVER_PREDECLARED_H100_REFERENCE_LABEL_GAP
NUEVA_02_MODEL_OR_EVAL_PERFORMANCE_SELECTION = NOT_USED
PROVENANCE_EVIDENCE_CLASS = USER_ATTESTED_COMPLETE_DAM_ACQUISITION / NOT_INDEPENDENTLY_REPLAYED_AT_ACQUISITION
```

No reinterpretes esta declaración como evidencia independiente. Debe conservarse explícitamente como **user-attested provenance**.

Candidato aprobado:

```text
branch = codex/exp12-new-historical-gate-extension-v02
commit = 55847ed375202533f20fd09d72af41ced153a818
parent = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
tree = 4fc757c88a05576722605b214fa5fb1ee8572226
changed_path_count = 10
```

Pool aprobado candidato:

```text
path = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
rows = 7190
unique_dam = 101
unique_nandina_total = 84
H100_reference_codes_present = 66
H100_reference_codes_missing = 0
H100_reference_coverage_fraction = 1.0
rows_excluded_fixed_dev_eval_dam = 0
rows_with_frozen_id_overlap = 0
```

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/codex/exp12-new-historical-gate-extension-v02 = 55847ed375202533f20fd09d72af41ced153a818
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato histórico exige:

```text
parent = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
commits_ahead = 1
commits_behind = 0
changed_path_count = 10
```

Los 10 paths deben ser exactamente los reportados por Prompt55 bajo:

```text
data/interim/new_historical_gate_v0.2/
outputs/audits/new_historical_gate_v0.2/
```

Si existe cualquier drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integración exacta del gate histórico v0.2

Integra exclusivamente:

```text
2b9571eee76ecffcaef1abc7fd4a12051f76f906
→
55847ed375202533f20fd09d72af41ced153a818
```

mediante fast-forward exacto de `main`.

Prohibidos:

- merge commit;
- squash;
- cherry-pick;
- rebase;
- amend;
- reconstrucción manual de los artefactos.

Después del push exige:

```text
origin/main = 55847ed375202533f20fd09d72af41ced153a818
```

No muevas Plan ni Article en esta fase.

---

## 4. Fase B — preparar binding de fuente EXP12 v0.4

### 4.1 Baseline de contrato

Lee íntegramente:

```text
src/configs/exp12_historical_diversity_control_v0.3.json
outputs/audits/new_historical_gate_v0.2/exp12_source_coverage_audit_v0.2.json
outputs/audits/new_historical_gate_v0.2/new_historical_ingestion_manifest.json
outputs/audits/new_historical_gate_v0.2/source_extension_freeze_v0.2.json
outputs/audits/exp12_source_activation_v0.1/exp12_f007_source_activation_audit_v0.2.json
```

El contrato v0.3 permanece evidencia histórica inmutable. **No lo edites.**

Crea un nuevo archivo:

```text
src/configs/exp12_historical_diversity_control_v0.4.json
```

partiendo semánticamente de v0.3.

### 4.2 Cambios permitidos en v0.4

Solo se permiten cambios necesarios para enlazar la fuente ya aprobada y actualizar estados de gate. Como mínimo:

```text
experiment_id = exp12_historical_diversity_control_v0.4
version = v0.4
contract_status = SOURCE_BOUND_FROZEN_PENDING_PLANNING_AUDIT
method_contract = FROZEN_METHOD_SOURCE_BOUND_PENDING_PLANNING_AUDIT
execution_authorized = false
```

En `sampling_universe`:

```text
source = NEW_HISTORICAL_GATE_EXTENSION_V02_APPROVED
path = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
rows = 7190
dam_count = 101
nandina_count = 84
fail_closed = true
must_not_fallback_to_h100 = true
```

En `future_manipulation_check.execution_gate`, sustituye únicamente el estado pendiente por una formulación equivalente a:

```text
SOURCE_BOUND_PENDING_PLANNING_AUDIT
```

No cambies fórmulas, thresholds ni criterios.

Puedes actualizar exclusivamente campos de estado que literalmente indiquen `PENDING_NEW_HISTORICAL_GATE` cuando ya no sean verdaderos, siempre que el nuevo valor indique **pending planning/external audit**, nunca autorización ni ejecución.

### 4.3 Parámetros congelados que deben permanecer idénticos

Entre v0.3 y v0.4 deben permanecer semánticamente idénticos, entre otros:

```text
fixed_eval.path / sha256 / rows / immutable / selection_usage
reference_h100.path / sha256 / rows / label_source / role
volume_control.target_rows = 2950
volume_control.max_abs_row_deviation = 148
volume_control.minimum_rows = 2802
volume_control.maximum_rows = 3098
volume_control.preserve_complete_dams = true
replicate_policy.number_of_replicates_per_condition = 10
replicate_policy.seed_schedule = [20262001..20262010]
conditions.D-HIGH.quantile = 0.1
conditions.D-MID.quantile = 0.5
conditions.D-LOW.quantile = 0.9
primary_diversity_variable = unchanged
label_control.required_label_coverage_fraction = 1.0
label_control.maximum_tvd = 0.05
selection.algorithm = deterministic_complete_dam_quantile_by_hhi
selection.no_weighted_multiobjective = true
selection.uses_eval_performance = false
selection.uses_eval_labels_for_selection = false
candidate_generation.candidate_count = 10000
candidate_generation.order_key = unchanged
candidate_generation.selection = unchanged
candidate_generation.prefix_tie_breaking = unchanged
candidate_generation.deduplicate_by = sorted DAM tuple
feasibility_filter.minimum_unique_feasible_candidates = 30
feasibility_filter.requires_volume_range = [2802,3098]
feasibility_filter.requires_label_coverage_fraction = 1.0
feasibility_filter.requires_tvd_at_most = 0.05
feasibility_filter.requires_zero_eval_dam_overlap = true
feasibility_filter.requires_complete_dams = true
condition_selection = unchanged except no status drift unrelated to source binding
future_manipulation_check formulas/reports/new_threshold_introduced = unchanged
primary_diversity_measures = unchanged
secondary_diversity_measures = unchanged
duplicate_measurement = unchanged
controls = unchanged
evaluation_contract = unchanged
output_contract = unchanged
```

No introduzcas ningún parámetro nuevo para facilitar factibilidad.

---

## 5. Artefacto obligatorio de auditoría de binding

Crea:

```text
outputs/audits/exp12_source_activation_v0.2/exp12_sampling_universe_binding_v0.4.json
```

Debe incluir como mínimo:

```text
artifact = EXP12_SAMPLING_UNIVERSE_BINDING_AUDIT
version = v0.4
baseline_contract_path = src/configs/exp12_historical_diversity_control_v0.3.json
candidate_contract_path = src/configs/exp12_historical_diversity_control_v0.4.json
source_gate_commit = 55847ed375202533f20fd09d72af41ced153a818
sampling_universe_path = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
sampling_universe_rows = 7190
sampling_universe_dam_count = 101
sampling_universe_nandina_count = 84
H100_reference_codes_present = 66
H100_reference_code_count = 66
H100_reference_coverage_fraction = 1.0
rows_excluded_fixed_dev_eval_dam = 0
rows_with_frozen_id_overlap = 0
```

Incluye además:

```text
source_provenance:
  acquisition_unit = COMPLETE_DAM_WITH_ALL_ORIGINAL_SERIES
  acquisition_method = SAME_SEARCH_EXTRACTION_COPY_METHOD_AS_INITIAL_DATA_AND_NUEVA_01
  acquisition_selection_basis = PREDECLARED_H100_LABEL_COVERAGE_GAP
  model_or_eval_performance_used = false
  evidence_class = USER_ATTESTED_COMPLETE_DAM_ACQUISITION / NOT_INDEPENDENTLY_REPLAYED_AT_ACQUISITION
```

Y un control de deriva entre v0.3 y v0.4:

```text
allowed_changed_json_paths = [...]
observed_changed_json_paths = [...]
unexpected_changed_json_paths = []
all_frozen_parameters_preserved = true
```

Registra también:

```text
candidate_generation_executed = false
planning_10000_candidates_per_seed_executed = false
retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
eval_labels_read = false
eval_descriptions_read = false
eval_performance_read = false
exp12_authorized = false
exp12_executed = false
group2b_started = false
group3_started = false
```

---

## 6. Verificaciones permitidas y prohibidas

Puedes ejecutar únicamente verificaciones estáticas/read-only necesarias para comprobar:

- JSON válido;
- SHA-256 exacto del pool;
- existencia y row count del pool;
- DAM count y NANDINA count como comprobación descriptiva del binding;
- igualdad semántica de parámetros congelados entre v0.3 y v0.4;
- ausencia de overlap DAM con EVAL usando únicamente identificadores DAM, si deseas corroborarlo.

NO ejecutes:

- `generate_exp12_candidates`;
- 10,000 candidatos por seed;
- selección D-LOW/D-MID/D-HIGH;
- HHI/TVD de candidatos;
- retrieval;
- BM25;
- Top-k;
- MRR;
- lectura de labels/descripciones/performance EVAL;
- autorización EXP12.

---

## 7. Versionado del candidato de source binding

Después de integrar Fase A, crea desde exactamente:

```text
55847ed375202533f20fd09d72af41ced153a818
```

la rama:

```text
codex/exp12-source-binding-v04
```

Crea **un solo commit** que añada exclusivamente:

```text
src/configs/exp12_historical_diversity_control_v0.4.json
outputs/audits/exp12_source_activation_v0.2/exp12_sampling_universe_binding_v0.4.json
```

No modifiques ningún otro path.

El candidato debe quedar publicado y pendiente de auditoría externa. **No lo integres a main en Prompt56.**

No modifiques el Plan en Prompt56; se reconciliará después de la auditoría externa del source binding.

---

## 8. Verificaciones finales obligatorias

Exige al final:

```text
origin/main = 55847ed375202533f20fd09d72af41ced153a818
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato v0.4:

```text
parent = 55847ed375202533f20fd09d72af41ced153a818
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
```

Y:

```text
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_BM25_EXECUTED = false
EXP12_TOP_K_COMPUTED = false
EXP12_MRR_COMPUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 9. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/56_RESPUESTA_INTEGRAR_GATE_HISTORICO_V02_Y_PREPARAR_BINDING_FUENTE_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 10. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT56 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

NEW_HISTORICAL_GATE_EXTENSION_V02_INTEGRATED = true/false
INTEGRATION_MODE

SOURCE_BINDING_BRANCH
SOURCE_BINDING_COMMIT
SOURCE_BINDING_PARENT
SOURCE_BINDING_CHANGED_PATH_COUNT
SOURCE_BINDING_CHANGED_PATHS

EXP12_CONFIG_V04_PATH
EXP12_CONFIG_V04_SHA256
SOURCE_BINDING_AUDIT_PATH
SOURCE_BINDING_AUDIT_SHA256

SAMPLING_UNIVERSE_PATH
SAMPLING_UNIVERSE_SHA256
SAMPLING_UNIVERSE_ROWS
SAMPLING_UNIVERSE_DAM_COUNT
SAMPLING_UNIVERSE_NANDINA_COUNT
H100_REFERENCE_COVERAGE = 66/66

PROVENANCE_EVIDENCE_CLASS = USER_ATTESTED_COMPLETE_DAM_ACQUISITION / NOT_INDEPENDENTLY_REPLAYED_AT_ACQUISITION
ALL_FROZEN_PARAMETERS_PRESERVED = true/false
UNEXPECTED_CHANGED_JSON_PATHS

EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12_BM25_EXECUTED = false
EXP12_TOP_K_COMPUTED = false
EXP12_MRR_COMPUTED = false
EXP12_AUTHORIZATION_CREATED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT56 = COMPLETED
NEW_HISTORICAL_GATE_EXTENSION_V02 = INTEGRATED
EXP12_SOURCE_BINDING_V04 = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
