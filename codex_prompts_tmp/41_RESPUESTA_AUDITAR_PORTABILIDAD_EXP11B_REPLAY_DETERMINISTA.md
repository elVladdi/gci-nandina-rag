# RESPUESTA PROMPT 41 — AUDITORÍA DE PORTABILIDAD EXP11B MEDIANTE REPLAY DETERMINISTA

## 1. Resultado terminal

```text
PROMPT41 = COMPLETED
EXP11B_PORTABILITY_REPLAY = CANDIDATE_VERIFIED_PENDING_EXTERNAL_AUDIT
EXP11B_PORTABILITY_DEBT = OPEN_PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

La evidencia exigida por Prompt41 fue producida. Los 20 bancos replay coincidieron exactamente con las 14 identidades gobernadas congeladas y con los 20 bancos oficiales observados en modo read-only. El candidato queda sujeto a auditoría externa; este bloque no cierra definitivamente la deuda.

## 2. Referencias iniciales y finales

| Referencia | Inicial | Final | Resultado |
|---|---|---|---|
| `origin/main` | `6846537602539506c8e90426daad05252cc982b9` | `6846537602539506c8e90426daad05252cc982b9` | PASS / sin modificación |
| `origin/docs/plan-maestro-temporal-2026-08-31` | `b814a8c2f976185209153e97e0d6ece0510526fb` | `b814a8c2f976185209153e97e0d6ece0510526fb` | PASS / sin modificación |
| `origin/article/main-manuscript` | `254b1e6df736fa9938ac86a515d65b36f4d361c5` | `254b1e6df736fa9938ac86a515d65b36f4d361c5` | PASS / sin modificación |
| `origin/codex/exp11b-portability-replay-proof-v01` | inexistente | `7d7267f8224e56ea5e945625a7e3955ddc15eadb` | publicado |

El candidato rechazado de Prompt40, `799156b3c98858fbe081de73f381030426174ce1`, no fue integrado ni reutilizado. La nueva rama fue creada directamente desde `main = 6846537602539506c8e90426daad05252cc982b9`.

## 3. Precondiciones canónicas

```ini
0B05C_CLOSURE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
EXP11B_BANK_MATERIALIZATION = CLOSED / APPROVED / INTEGRATED
EXP11B_RETRIEVAL_EXECUTION_GATE = APPROVED / INTEGRATED
EXP11B_PORTABILITY_DEBT = OPEN
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
PRECONDITION_DRIFT = false
```

## 4. Materializador y helpers

```makefile
materializer = src/experiments/materialize_exp11b_banks_v01.py
materializer_git_blob = ba64a85b4bb8bfa9f163a4f1115440486b7d8d2c
materializer_checkout_sha256 = 1b0a27fd077d2daba8d73ea395c80dfca1d207ad8370acb4c4565099516cdcee
dependencies = PYTHON_STANDARD_LIBRARY_ONLY
third_party_dependencies = NONE
new_materializer_implemented = false
historical_audit_helper_used = audit_bank / read-only identity derivation after replay
```

La construcción utilizó el materializador histórico versionado. Los bancos oficiales no fueron copiados, leídos ni usados como input de construcción; solo se observaron después del replay para la comparación triple.

## 5. Inputs congelados

| Input | SHA-256 esperado | SHA-256 observado | Estado |
|---|---|---|---|
| H100 `data/processed/data_aduanas_historico_clase87_v0.2.csv` | `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff` | `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff` | PASS |
| NEW_ELIGIBLE `data/interim/new_historical_gate_v0.1/new_historical_eligible.csv` | `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4` | `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4` | PASS |
| DEV `data/processed/data_aduanas_devset_clase87_v0.2.csv` | `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00` | `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00` | PASS |
| EVAL `data/processed/data_aduanas_evalset_clase87_v0.2.csv` | `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941` | `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941` | PASS |
| Feasibility `outputs/audits/new_historical_gate_v0.1/exp11b_h150_h200_feasibility_v0.1.json` | `fa9eaf906feac264bca9e496557bbc1f17fe1462af412752c2b81a85af78fdf0` | `fa9eaf906feac264bca9e496557bbc1f17fe1462af412752c2b81a85af78fdf0` | PASS |

```ini
input_mismatch_count = 0
H100_hash_match = true
EVAL_hash_match = true
REPLAY_INPUT_NOT_PORTABLE = false
```

## 6. Configuración y procedencia EOL

```makefile
config_path = src/configs/exp11b_bank_materialization_v0.1.json
config_git_blob = cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8
canonical_git_content_sha256 = a7fa158dcf13e4b293e3de51351f814305cf5208b08395d5de8994f2d69c710c
windows_working_tree_sha256 = 39c27e6791bcc5d574a2c132af59bbe99a4793ee0506d95724ad8f2d632a5e17
canonical_git_bytes = 2476
windows_working_tree_bytes = 2552
canonical_git_crlf_count = 0
canonical_git_lf_count = 76
windows_working_tree_crlf_count = 76
windows_working_tree_lf_count = 76
semantic_json_equal = true
classification = SAME_GIT_BLOB_EQUIVALENT_JSON_LF_VS_CRLF_CHECKOUT_REPRESENTATION
CONFIG_PROVENANCE_NOT_DEMONSTRATED = false
```

La diferencia `a7fa158d...` frente a `39c27e67...` quedó reproduciblemente explicada por representación LF canónica del blob Git frente a CRLF del checkout Windows. No se reescribió la configuración.

## 7. Diseño congelado

```makefile
conditions = H150,H200
expected_banks = 20
expected_replicates = 10
seeds = 20261005,20261006,20261007,20261010,20261011,20261013,20261017,20261021,20261023,20261024
row_order_policy = H100_ORIGINAL_ORDER_THEN_NEW_ELIGIBLE_ORIGINAL_ORDER_FILTERED_BY_SELECTED_DAMS
encoding = utf-8
lineterminator = LF
quoting = csv.QUOTE_MINIMAL
header = H100_EXACT_COLUMN_ORDER
```

No se alteraron seeds, composición, H100, DEV ni EVAL.

## 8. Replay aislado

```makefile
worktree_mode = TEMPORARY_DETACHED
worktree_commit = 6846537602539506c8e90426daad05252cc982b9
worktree_clean_before = true
python_version = 3.10.11
python_implementation = CPython
python_architecture = 64bit
platform = Windows-10-10.0.26200-SP0
machine = AMD64
python_executable_sha256 = b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961
internet_required = false
external_scientific_files_required = false
dependency_installation_performed = false
```

Comando ejecutado exactamente una vez:

```powershell
& '<existing_project_venv>\Scripts\python.exe' -B -m src.experiments.materialize_exp11b_banks_v01 --materialize --output-dir replay_tmp/banks --audit-dir replay_tmp/audit --expected-manifest outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_materialization_manifest_v0.1.json
```

```ini
invocation_count = 1
retry_performed = false
resume_performed = false
official_banks_used_as_construction_input = false
replay_outputs_temporary = true
banks_produced = 20
H150_banks_produced = 10
H200_banks_produced = 10
```

El proceso terminó con código `2` al aplicar una comparación exacta adicional de `total_bank_descriptor` no incluida en las 14 identidades gobernadas exigidas por Prompt41:

```text
ERROR: Frozen manifest mismatch for EXP11B_R01_H150: total_bank_descriptor
```

Diagnóstico estático posterior, sin reintentar ni reanudar la construcción:

```ini
classification = FLOAT_REPRESENTATION_DIFFERENCE_OUTSIDE_REQUIRED_14_IDENTITY_FIELDS
exact_float_descriptor_difference_count = 52
affected_bank_count = 18
maximum_absolute_delta = 5.329070518200751e-15
historical_validator_tolerance = 1e-12
within_historical_validator_tolerance = true
bank_csv_content_affected = false
governed_14_field_identity_status = PASS_EXACT
csv_byte_identity_status = PASS_EXACT
```

El evento se conserva expresamente como procedencia. No debilitó el criterio solicitado: los 20 CSV fueron producidos y las 14 identidades gobernadas, incluidos contenido, tamaño, composición y hashes de orden, coinciden exactamente en las tres comparaciones.

## 9. Comparación triple

Campos comparados para cada banco:

```text
bank_id
filename
seed
condition
row_count
new_row_count
total_dam_count
new_dam_count
bank_csv_sha256
size_bytes
composition_sha256
H100_core_id_order_sha256
increment_id_order_sha256
total_bank_id_order_sha256
```

```makefile
frozen_bank_count = 20
official_observed_bank_count = 20
replay_bank_count = 20

frozen_official_match_count = 20
frozen_official_mismatch_count = 0

frozen_replay_match_count = 20
frozen_replay_mismatch_count = 0

official_replay_match_count = 20
official_replay_mismatch_count = 0
```

## 10. Detalle por banco

Cada fila `14/14` significa igualdad exacta de todos los campos gobernados entre FROZEN, OFFICIAL_OBSERVED y REPLAY.

| Banco | SHA-256 FROZEN = OFFICIAL = REPLAY | F-O | F-R | O-R |
|---|---|---:|---:|---:|
| `EXP11B_R01_H150` | `a95ccaa947994e9e01392c1f519f7a19ef015b560a2c3aa77f6bf3ee7a5961db` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R01_H200` | `20c987e52f0d6a221ffaa756527b1b4b571117a57c839909908cd7e7441abe49` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R02_H150` | `331762d93446c575abaf59c76c38eb55e106431c811dda48c99d489cff279000` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R02_H200` | `0b6772d0ead99f352ffde4170bceb6e443da0b84a3b652bee845f05c765cb468` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R03_H150` | `1001a3821aec92b1f7c785ba620100bb68acee0a2e4312bb041f75578eb13fb2` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R03_H200` | `d27fcc4a9711cbc4d9126fc337518d09430a988fae554ee12246b1fec4205b77` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R04_H150` | `2f21215da09a2e9bdb0fe72b9dae56a88f03109cbab901a0b236633aa7410850` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R04_H200` | `b2488c0b0a0525f0d6a98dd54071fd715afefbab719d526e4779283d9bf67887` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R05_H150` | `74524582ec2158d2e87ac46d06a2259b7d03a674212678d39713345517d08f11` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R05_H200` | `80ac01f63c184237c8ff36a5ecd1fef38d18562114bd60842cb2bdc8f9ee5cae` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R06_H150` | `66259a5fa9058b1f3c58601541aee4637f758878f18d8757e4c1bfc21de397a8` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R06_H200` | `548159b34b19be379d7e1e54f170985466189c77796883fa4c8a2429c0d926fd` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R07_H150` | `f00e9625b0684200e2a2fe91b3bcec1abeb05e3d444244177371ff7489b51345` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R07_H200` | `221030d48308566f7e79f1ee7a37b1f9c9d6f7d4aadaba709a691fd417e1aa57` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R08_H150` | `d7bf195592c749333820cb1c1bc8c3202a446a1d5a6ebc2ef051593f52356bb8` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R08_H200` | `7005a43687d80bd4454389fb34f96577911b75558618ab4b63104341ae85875a` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R09_H150` | `6353eb3081c31e829f978958ab0ab5d000633e1c678ef7aaf691444b33245f9d` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R09_H200` | `2c72fb62deb0cecfe90b49b991bf6918ab4177a35aebb8e88bf74b08058fd841` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R10_H150` | `163f5b9f6284a40b21da405b958cccb571df7b4932381ecb832a2c771ca850b9` | 14/14 | 14/14 | 14/14 |
| `EXP11B_R10_H200` | `ed570fccf8913fbd3416157013f152697dc1ed6358313e379e6b9e93af11cdf2` | 14/14 | 14/14 | 14/14 |

## 11. BM25 estático

```makefile
normalization = unicode_NFKD_lowercase_remove_combining_marks
tokenizer = regex_[a-z0-9]+
k1 = 1.5
b = 0.75
candidate_depth = 100
k_values = 1,3,5,10,50
ranking = descending_score_then_ascending_historical_case_id
bm25_semantics_preserved = true
retrieval_executed = false
evaluation_metrics_computed = false
```

La verificación fue exclusivamente estática. No se ejecutó BM25, retrieval H150/H200 ni cálculo de métricas.

## 12. Inmutabilidad de bancos oficiales

```makefile
official_bank_count_before = 20
official_bank_count_after = 20
official_snapshot_sha256_before = 66cdea3ad6d25c0d8c4e37e5ec4c1757039658057d316d5a97e12c0d0fe2829a
official_snapshot_sha256_after = 66cdea3ad6d25c0d8c4e37e5ec4c1757039658057d316d5a97e12c0d0fe2829a
official_bank_write_count = 0
official_bank_content_mutated = false
official_artifacts_preserved = true
OFFICIAL_BANK_MUTATION_RISK = false
```

## 13. Limpieza

```makefile
replay_outputs_temporary = true
replay_outputs_removed_after_audit = true
temporary_replay_cleanup = PASS
temporary_worktree_present_after_cleanup = false
```

El worktree detached y todos los outputs replay temporales fueron eliminados después de capturar la evidencia. Los artefactos oficiales permanecen intactos.

## 14. Candidato

```makefile
branch = codex/exp11b-portability-replay-proof-v01
candidate_commit = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
parent = 6846537602539506c8e90426daad05252cc982b9
tree = 5ead782eeb0d25a9ef1965f43de7036eedf0a0eb
ahead_of_main = 1
behind_main = 0
published = true
```

Changed paths exactos:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_replay_proof_v0.1.json
```

```ini
changed_path_count = 1
scientific_inputs_modified = false
official_banks_versioned = false
replay_banks_committed = false
main_modified = false
plan_maestro_modified = false
article_modified = false
exp12_modified = false
attempt06_modified = false
group2b_opened = false
external_audit_required = true
```

## 15. Confirmaciones finales

```makefile
main = 6846537602539506c8e90426daad05252cc982b9
origin/main = 6846537602539506c8e90426daad05252cc982b9
origin/docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
candidate_remote = 7d7267f8224e56ea5e945625a7e3955ddc15eadb

retrieval_executed = false
evaluation_metrics_computed = false
exp11b_retrieval_authorized = false
exp12_authorized = false
plan_maestro_modified = false
article_modified = false
EXP11B_PORTABILITY_DEBT = OPEN_PENDING_EXTERNAL_AUDIT
```

```text
PROMPT41 = COMPLETED
EXP11B_PORTABILITY_REPLAY = CANDIDATE_VERIFIED_PENDING_EXTERNAL_AUDIT
EXP11B_PORTABILITY_DEBT = OPEN_PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
