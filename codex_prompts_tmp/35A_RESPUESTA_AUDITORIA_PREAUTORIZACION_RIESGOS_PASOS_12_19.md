# RESPUESTA PROMPT 35A — AUDITORÍA PREAUTORIZACIÓN DE RIESGOS PASOS 12–19

## Clasificación y estado

```makefile
classification = CODEX_LOCAL_PREAUTHORIZATION_RISK_AUDIT / NOT_INDEPENDENT_GITHUB_CI
status = PREAUTH_RISK_AUDIT_COMPLETED / V05_NOT_BUILT / ATTEMPT06_NOT_AUTHORIZED
ready_for_attempt06 = false
Prompt35_executed = false
V05_built = false
Attempt05_reexecuted = false
Attempt05_retry = false
Attempt05_resume = false
Attempt06_authorized = false
Attempt06_executed = false
dependencies_installed_or_modified = false
scientific_execution_performed = false
```

## Estado de entrada

```makefile
main = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
origin/main = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
attempt05_audit_branch = codex/0b05c-attempt05-failclosed-evidence-env-diagnosis
attempt05_audit_commit = 5144bbdfc3b36e6172ecdd604a3e71d256ab248b
attempt05_audit_parent = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
attempt05_local_raw_commit = 525261c0d25d8286e25b1f618655115719540c8b
attempt05_local_raw_commit_available = true
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
main_modified = false
plan_modified = false
article_modified = false
```

Los outputs parciales de Attempt05 se leyeron exclusivamente como evidencia:

`DIAGNOSTIC_ONLY / NOT_SCIENTIFIC_RESULT / NEVER_REUSED_FOR_ATTEMPT06`.

No se publicaron corpus, índices, rankings ni métricas runtime parciales.

## Paso 12 — D1a

### Dependencias del path real

La inspección estática confirmó:

- El builder y el evaluator importan directamente `numpy` y `sentence_transformers`.
- `run_d1a_corrective_0b05c_v04.py` lanza ambos mediante `subprocess` con `sys.executable`.
- El índice usa vectores normalizados y búsqueda exacta brute-force por producto punto.
- El spec declara `hnsw=false`; `hnswlib` no es importado ni usado en el path D1a actual y no se clasificó como blocker.

### Intérpretes descubiertos

No se encontraron `python` en `PATH`, instalaciones registradas por `py -0p` ni Conda visible. Se inspeccionaron los tres intérpretes preexistentes razonablemente vinculados al proyecto/usuario.

| ID público | Ruta administrativa local | Python | SHA-256 ejecutable | Resultado D1a |
|---|---|---|---|---|
| `PROJECT_VENV_PY310` | `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA\.venv\Scripts\python.exe` | 3.10.11 | `b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961` | USABLE |
| `SYSTEM_PYTHON310` | `C:\Users\Vladimir\AppData\Local\Programs\Python\Python310\python.exe` | 3.10.11 | `3cce33d75d6fdae4e004d0bdf149320b3147482a9caf370079dcb9c191a1b260` | NOT_USABLE |
| `CODEX_PRIMARY_RUNTIME_PY312` | `C:\Users\Vladimir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe` | 3.12.14 | `372c2eae555b344520bf147be0096e009069aeca4e7f78d6aecea6d53158056a` | NOT_USABLE |

Matriz de imports:

| Intérprete | numpy | sentence_transformers | torch | tqdm | hnswlib | Builder D1a | Evaluator D1a |
|---|---|---|---|---|---|---|---|
| `PROJECT_VENV_PY310` | PASS 2.2.6 | PASS 5.5.1 | PASS 2.12.0+cpu | PASS 4.68.2 | FAIL, no requerido | PASS | PASS |
| `SYSTEM_PYTHON310` | FAIL | FAIL | FAIL | FAIL | FAIL, no requerido | FAIL en `numpy` | FAIL en `numpy` |
| `CODEX_PRIMARY_RUNTIME_PY312` | PASS 2.3.5 | FAIL | FAIL | FAIL | FAIL, no requerido | FAIL en `sentence_transformers` | FAIL en `sentence_transformers` |

Existe por tanto un intérprete preexistente que resuelve el bloqueo ambiental sin instalar nada. El defecto pendiente es que v0.4 no liga ni verifica qué intérprete debe utilizarse antes de integrar una autorización.

### Directorio completo del modelo

Referencia:

`data/processed/indexes/text2trade_mnrl_nandina8_v0.2/text2trade_mnrl_nandina8_v02_run_metadata.json`

Se verificó el directorio completo disponible en el checkout local canónico del proyecto:

| Path gobernado | Bytes | SHA-256 | Estado |
|---|---:|---|---|
| `models/text2trade_mnrl_v0.2/1_Pooling/config.json` | 94 | `bb80272f7adad76ce93073c25e18113ee66be1e91f60bcdd72aa41d05b28247e` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/config.json` | 777 | `867cac582ca8ac9a39e1fd577d793a60089cf2786d86c547ad44c0a12be73b80` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/config_sentence_transformers.json` | 295 | `44cd1329eec2dd1658d9fe7af6d266460a762a11e7dc5c71b16f9237d161eca7` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/model.safetensors` | 470637416 | `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/modules.json` | 290 | `318d49f1092cad125a35af58d9795bcddce84bf7e7240bd8d95b9b6858f9476b` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/README.md` | 4043 | `90bc9c8da4ec9fad492fd04218f7f3eabaa4173c9e8eec9dc59b519a01751cbb` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/sentence_bert_config.json` | 250 | `5fee3fcdc4a727fad422f0fed0c867b0921eefa9051de221521956ed42eb4c19` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/tokenizer.json` | 6973173 | `15e67157ec6fa47df5b142c36fbb0f3ea8e303a96de2e9bbb59b755c7cc46e49` | PASS_EXACT |
| `models/text2trade_mnrl_v0.2/tokenizer_config.json` | 649 | `ec1137c53aaa844aab218f337912175bbc7cd0e64ed0896a45d7f982af5c1c71` | PASS_EXACT |

```makefile
model_governed_files = 9
model_pass_exact = 9
model_missing = 0
model_mismatch = 0
model_extra = 0
complete_model_directory = PASS_EXACT
```

El worktree aislado de Prompt33 solo exponía `model.safetensors`; el directorio completo sí existe en el checkout local canónico. Una futura ejecución debe bloquearse salvo que el checkout seleccionado exponga los nueve archivos exactos.

### Smoke test offline

Se usó `PROJECT_VENV_PY310`, `HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`, CPU, `max_seq_length=128`, 32 strings triviales sintéticos, `batch_size=32`, `convert_to_numpy=True` y `normalize_embeddings=True`.

```makefile
offline_model_load = PASS
network_used = false
scientific_inputs_used = false
shape = [32, 384]
dtype = float32
all_values_finite = true
norm_min = 0.9999998807907104
norm_max = 1.0000001192092896
float32_epsilon = 1.1920928955078125e-07
tolerance = 8 * float32_epsilon = 9.5367431640625e-07
all_norms_within_tolerance = true
```

### Inputs, patch y config

Todo se derivó en memoria; no se construyeron embeddings del corpus real.

```makefile
original_corpus_sha256 = 83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0
original_corpus_sha_exact = true
corpus_total_rows = 7748
patched_total_rows = 7748
nandina8_document_count = 7644
nandina8_codes_unique = true
nandina8_order_preserved = true
changed_document_count = 2
changed_codes = 87044110, 87045110
unpatched_documents_identical = true
eval_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
eval_sha_exact = true
eval_rows = 1056
eval_case_ids_nonempty = true
eval_case_ids_unique = true
runtime_config_changed_fields = 4
runtime_config_allowed_diff_exact = true
```

Los cuatro campos cambiados fueron exactamente:

```text
frozen_inputs.normative_corpus
frozen_inputs.normative_corpus_sha256
index.output_dir
outputs.evaluation_dir
```

### Recursos del host

```makefile
checkout_volume_free_bytes = 463415988224
host_total_visible_memory_bytes = 34070192128
host_free_physical_memory_bytes_at_probe = 17817530368
attempt05_partial_output_bytes = 237929403
historical_d1a_index_bytes = 15055856
historical_d1a_evaluation_bytes = 2769761
complete_model_directory_bytes = 477616987
reference_footprint_bytes = 733372007
conservative_two_copy_disk_margin_bytes = 1466744014
```

El margen de disco de dos copias se derivó del footprint observado combinado para permitir coexistencia de fuente y outputs nuevos, no de un umbral arbitrario. El espacio libre supera ampliamente ese margen. La RAM disponible también supera el peso del modelo y matrices observadas, y el smoke de carga/encode pasó. No hay blocker de capacidad actual, aunque el pico de una ejecución completa continúa siendo riesgo runtime y debe reprobarse inmediatamente antes de autorizar.

## Paso 13 — Integrity validation

Se ejecutó exclusivamente el closure `integrity()` sobre los partial roots de Prompt33 y se verificaron de forma independiente todos los hashes disponibles en el execution record.

```makefile
integrity_status = PASS
current_integrity_scope = EXISTENCE_OF_14_EV03_EV04_FILES_ONLY
inventory_files_checked = 26
inventory_hashes_pass_exact = 26
inventory_mismatch_count = 0
```

Conclusión: los partials observados son exactos frente al inventario, pero el paso 13 actual solo exige existencia de 14 archivos EV03/EV04. No comprueba por sí mismo hashes, schema ni cardinalidad. Riesgo reducido, no eliminado.

## Paso 14 — Case-level comparisons

```makefile
EV03_case_summary_count = 1056
EV03_original_candidate_case_count = 1046
EV03_corrected_candidate_case_count = 1046
EV03_comparison = FAIL_CLOSED
EV03_full_rows_constructed = false
EV04_case_count = 1056
EV04_comparison = PASS
EV04_case_ids_unique = true
EV04_nandina_ref_stable = true
EV04_schema_order_exact = true
```

El comparator actual exige al menos una fila candidate ranking para cada `case_id`. EV03 contiene 10 casos con case summary pero sin candidate rows, tanto en control como en corrected. Por ello el paso 14 fallaría determinísticamente aun con los outputs ya producidos correctamente. Este es un blocker real que debe cerrarse antes de v0.5, definiendo una representación contractual de ranking vacío compatible con `rank=0`, sin cambiar retrieval.

Controles negativos sintéticos:

```makefile
missing_or_extra_case_id = FAIL_CLOSED_PASS
duplicate_case_id = FAIL_CLOSED_PASS
rank_gap = FAIL_CLOSED_PASS
duplicate_EV04_code = FAIL_CLOSED_PASS
changed_nandina_ref = FAIL_CLOSED_PASS
```

## Paso 15 — Aggregate comparisons

El camino positivo efectivo del runner, que conserva el objeto EV04 en memoria, pasó:

```makefile
EV03_metric_table_count = 17
EV03_aggregate_count = 17
EV04_metric_object_key_count = 92
EV04_metric_table_count = 27
EV04_aggregate_count = 28
EV04_order_exact = true
mrr_101_200_contribution_third = true
observed_numeric_values_finite = true
live_runtime_in_memory_path = PASS
```

Controles negativos:

```makefile
missing_metric = FAIL_CLOSED_PASS
extra_metric = FAIL_CLOSED_PASS
reordered_metric = FAIL_CLOSED_PASS
denominator_mismatch = FAIL_CLOSED_PASS
nan_noncontribution_metric = NOT_REJECTED
inf_noncontribution_metric = NOT_REJECTED
```

El validador legado comprueba tipo numérico, pero no finitud para todos los campos. Aceptar `NaN` o `Infinity` fuera de la contribution row es blocker antes de v0.5.

Hallazgo adicional: recargar el JSON EV04 persistido produce orden de keys de fila `denominator, metric, numerator, value`, mientras el validador exige `metric, numerator, denominator, value`. La recarga falla cerrada. El live runner usa el objeto in-memory y pasa, por lo que no bloquea esa invocación, pero v0.5 debe congelar un contrato serialización/recarga. Esto no concede permiso de resume.

## Paso 16 — Unified sensitivity summary

```makefile
positive_with_synthetic_structural_d1a = PASS
missing_d1a = FAIL_CLOSED_PASS
malformed_d1a_wrong_type = FAIL_CLOSED_PASS
empty_d1a_mapping = NOT_REJECTED
malformed_EV03_EV04 = NOT_REJECTED
```

La función actual solo exige `D1a.status=PASS` y que `aggregate_comparison` sea algún `Mapping`. Acepta un mapping vacío y no valida los payloads EV03/EV04. Este es blocker antes de v0.5. La disponibilidad de D1a real sigue siendo además riesgo runtime intrínseco.

## Paso 17 — Execution manifest

Prueba íntegramente en tempdir con objetos sintéticos v0.5:

```makefile
json_serialization = PASS
authorization_provenance_present = true
execution_order_count = 19
execution_order_exact = true
v04_partial_root_reference_present = false
preexisting_manifest_path = FAIL_CLOSED_PASS
```

La lógica/schema queda verificada preventivamente. Permanece riesgo residual de serialización de los objetos reales futuros; v0.5 debe validar el payload completo en memoria justo antes de escribir.

## Paso 18 — Exact hash ledger

Se derivaron por separado el set contractual y el set de productores de pasos 1–17:

```makefile
EXPECTED_SET_count = 47
PRODUCER_SET_count = 47
missing_in_producer = []
unexpected_producer_outputs = []
path_collisions = 0
failure_only_execution_failed_json_in_success_set = false
exact_placeholder_set = PASS
remove_one_placeholder = FAIL_CLOSED_PASS
add_one_unexpected_placeholder = FAIL_CLOSED_PASS
```

La cardinalidad y los nombres quedan cerrados para v0.4. Los hashes de bytes futuros son, por definición, riesgo runtime y no pueden demostrarse antes de producirlos.

## Paso 19 — Final completion state

`run_authorized_pipeline()` se ejecutó solo con operaciones 100% sintéticas:

```makefile
valid_19_step_pipeline = PASS
valid_step_count = 19
prior_step_FAIL = FAIL_CLOSED_PASS
missing_operation = FAIL_CLOSED_PASS
reordered_operation = FAIL_CLOSED_PASS
final_before_18_states = FAIL_CLOSED_PASS
```

La lógica de orden/completitud queda anulada como riesgo de diseño. Una excepción real del host o productor después de side effects sigue siendo riesgo runtime inevitable; se mitiga con roots aislados, una invocación, prohibición de resume y preservación de evidencia.

## Matriz de riesgos

| Paso | Riesgo inicial | Evidencia/probe | Resultado | Categoría | Mitigación obligatoria | Gate v0.5 |
|---:|---|---|---|---|---|---|
| 12 | HIGH | Tres intérpretes y imports reales | Existe un venv utilizable, pero el intérprete no está ligado | `BLOCKING_RISK_REQUIRES_REMEDIATION_BEFORE_V05` | Gate de intérprete/imports antes de autorización | true |
| 12 | HIGH | Manifest completo de nueve archivos | Directorio exacto existe, pero no en todo worktree | `BLOCKING_RISK_REQUIRES_REMEDIATION_BEFORE_V05` | Gate de directorio completo en checkout ejecutor | true |
| 12 | MEDIUM | Smoke offline sintético | PASS | `REDUCED_BY_PREAUTH_VERIFICATION` | Repetir antes de autorización | true |
| 12 | HIGH | Inputs/patch/config in-memory | PASS exacto | `ELIMINATED_BY_PREAUTH_VERIFICATION` | Preservar bindings | true |
| 12 | MEDIUM | Disco/RAM/footprints | Sin blocker actual | `RESIDUAL_RUNTIME_RISK_CANNOT_BE_ELIMINATED_PREAUTH` | Reprobe inmediatamente antes de autorizar | true |
| 13 | MEDIUM | Integrity + 26 hashes | Partials exactos; integrity es existence-only | `REDUCED_BY_PREAUTH_VERIFICATION` | Hash/schema/cardinality en step 13 | true |
| 14 | HIGH | Comparación completa de partials | EV03 falla por 10 rankings vacíos | `BLOCKING_RISK_REQUIRES_REMEDIATION_BEFORE_V05` | Contrato explícito de ranking vacío/rank 0 | true |
| 14 | MEDIUM | Cinco negativos sintéticos | Todos fail-closed | `ELIMINATED_BY_PREAUTH_VERIFICATION` | Preservar tests | true |
| 15 | HIGH | Positive y cuatro negativos estructurales | PASS | `ELIMINATED_BY_PREAUTH_VERIFICATION` | Preservar contrato | true |
| 15 | HIGH | NaN/Inf sintéticos | No rechazados | `BLOCKING_RISK_REQUIRES_REMEDIATION_BEFORE_V05` | `math.isfinite` para todo numérico | true |
| 15 | MEDIUM | Reload JSON persistido | Falla por orden de keys; live in-memory pasa | `REDUCED_BY_PREAUTH_VERIFICATION` | Contrato serialización/reload | true |
| 16 | HIGH | D1a/arms malformed | Mapping vacío y arms inválidos aceptados | `BLOCKING_RISK_REQUIRES_REMEDIATION_BEFORE_V05` | Schema completo de tres arms | true |
| 16 | HIGH | D1a sintético válido | Positive PASS | `RESIDUAL_RUNTIME_RISK_CANNOT_BE_ELIMINATED_PREAUTH` | Validar D1a completo antes de summary | true |
| 17 | MEDIUM | Manifest sintético tempdir | PASS | `REDUCED_BY_PREAUTH_VERIFICATION` | Validación pre-write del payload real | true |
| 18 | HIGH | Sets independientes + negatives | 47/47 exacto | `ELIMINATED_BY_PREAUTH_VERIFICATION` | Repetir para v0.5 | true |
| 18 | MEDIUM | Placeholder ledger | Schema PASS, hashes futuros desconocidos | `RESIDUAL_RUNTIME_RISK_CANNOT_BE_ELIMINATED_PREAUTH` | Hash post-productores | true |
| 19 | MEDIUM | Pipeline 100% sintético | Todos los controles PASS | `ELIMINATED_BY_PREAUTH_VERIFICATION` | Preservar harness | true |
| 19 | MEDIUM | Fallo sintético previo | Propagación fail-closed PASS | `RESIDUAL_RUNTIME_RISK_CANNOT_BE_ELIMINATED_PREAUTH` | Roots aislados y no resume | true |

## Blockers antes de v0.5/autorización

```text
R12-02_INTERPRETER_READINESS_NOT_GATED
R12-03_COMPLETE_MODEL_DIRECTORY_NOT_GATED
R14-01_EV03_EMPTY_RANKING_CASES_BREAK_COMPARISON
R15-02_NONFINITE_NONCONTRIBUTION_METRICS_NOT_REJECTED
R16-01_UNIFIED_SUMMARY_SCHEMA_UNDERVALIDATED
```

Estos findings no impiden construir una futura remediación v0.5, pero bloquean cualquier futura autorización hasta quedar corregidos y auditados.

## Respuestas obligatorias

1. **Riesgos anulados antes de ejecución real:** identidad de inputs/patch/config D1a; guards de case/rank/code; estructura canónica y denominadores aggregate; cardinalidad/nombres del ledger; orden/completitud de 19 pasos.
2. **Riesgos solo reducidos:** selección/importabilidad del intérprete, disponibilidad completa del modelo en el checkout ejecutor, integrity de archivos futuros, serialización del manifest y capacidad del host.
3. **Riesgos intrínsecamente runtime:** ejecución completa del modelo/corpus, bytes y hashes futuros, disponibilidad D1a real para summary, y fallos del host/productores posteriores a side effects.
4. **Blocker actual:** sí, cinco blockers contractuales. No bloquean construir correcciones; sí bloquean autorizar Attempt06.
5. **Intérprete preexistente que resuelve ambiente sin instalación:** sí, `PROJECT_VENV_PY310`; pasa imports directos y smoke offline.
6. **Controles obligatorios v0.5:** binding exacto del intérprete; imports y smoke antes de autorización; nueve archivos del modelo; ranking vacío EV03; finitud numérica completa; validación estricta de los tres arms; integrity con hash/schema/cardinalidad; serialización/reload estable; set ledger 47/47 rederivado; roots aislados y no retry/resume.

## Candidato audit-only

```makefile
branch = codex/0b05c-preauthorization-risk-audit-12-19
candidate_commit = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
candidate_parent = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
candidate_tree = 11f7c59d66c858022c1d75282a8c77b93606c8aa
candidate_remote = c873ff1bd10f4e86c6f80f7f34a4dad1126965f1
changed_path_count = 1
artifact_path = outputs/audits/0b05c_preauthorization_risk_audit_v0.4/preauthorization_risk_audit_steps12_19_v0.4.json
artifact_git_blob = 4bbb25940f5a14f88c4ed51daaa8475116facd29
artifact_size_bytes = 26355
artifact_sha256 = 6e16e3f149fe3b9fb8d726523eb7af9d65adbc2dc4b30dd4a4c6b853198a0cb7
public_artifact_absolute_paths_present = false
sensitive_partial_outputs_published = false
working_tree_clean = true
```

El candidato contiene exactamente el único JSON sanitizado permitido y no fue integrado a `main`.

## Estado final

```makefile
ATTEMPT05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
V05 = NOT_BUILT
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
BLOCKERS = 5_REMEDIATIONS_REQUIRED_BEFORE_V05_AUTHORIZATION
```
