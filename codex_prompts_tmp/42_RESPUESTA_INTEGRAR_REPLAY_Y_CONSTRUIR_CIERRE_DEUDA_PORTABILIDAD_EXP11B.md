# RESPUESTA PROMPT 42 — INTEGRAR REPLAY Y CONSTRUIR CIERRE DE DEUDA DE PORTABILIDAD EXP11B

## 1. Estado final

```text
PROMPT42 = COMPLETED
PROMPT41_REPLAY_PROOF = APPROVED / INTEGRATED_IN_MAIN
PORTABILITY_CLOSURE_RECORD = CANDIDATE / PENDING_EXTERNAL_GIT_AUDIT
EXP11B_PORTABILITY_DEBT = CLOSED_BY_EXTERNAL_DECISION / PENDING_CLOSURE_RECORD_INTEGRATION
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Prompt42 completó exclusivamente sus dos fases autorizadas: integración fast-forward bit a bit del proof Prompt41 y construcción de un registro formal de cierre en una rama candidata separada. El registro de cierre no fue integrado a `main`.

## 2. Referencias iniciales

```makefile
origin/main = 6846537602539506c8e90426daad05252cc982b9
origin/codex/exp11b-portability-replay-proof-v01 = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
replay_candidate_parent = 6846537602539506c8e90426daad05252cc982b9
replay_candidate_tree = 5ead782eeb0d25a9ef1965f43de7036eedf0a0eb
replay_proof_blob = ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead
origin/docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
prompt41_response_commit = 2e2172a57a0db6560e6910477a97751eba52e269
```

```ini
precondition_drift = false
candidate_ahead_of_main = 1
candidate_behind_main = 0
candidate_changed_path_count = 1
```

Único path del candidato Prompt41:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_replay_proof_v0.1.json
```

El candidato rechazado de Prompt40, `799156b3c98858fbe081de73f381030426174ce1`, no fue integrado ni reutilizado.

## 3. Verificación read-only del proof Prompt41

```makefile
artifact_id = exp11b_portability_replay_proof_v0.1
status = CANDIDATE_PORTABILITY_REPLAY_VERIFIED_PENDING_EXTERNAL_AUDIT
main_baseline_commit = 6846537602539506c8e90426daad05252cc982b9
external_audit_origin = PROMPT40_REJECTED

H100_hash_match = true
EVAL_hash_match = true
input_mismatch_count = 0
materializer_git_blob = ba64a85b4bb8bfa9f163a4f1115440486b7d8d2c
config_git_blob = cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8
config_provenance = SAME_GIT_BLOB_EQUIVALENT_JSON_LF_VS_CRLF_CHECKOUT_REPRESENTATION

H150_banks_produced = 10
H200_banks_produced = 10
process_return_code = 2
governed_14_field_identity_status = PASS_EXACT
csv_byte_identity_status = PASS_EXACT

frozen_official = 20/20 PASS / 0 mismatches
frozen_replay = 20/20 PASS / 0 mismatches
official_replay = 20/20 PASS / 0 mismatches

official_bank_write_count = 0
official_bank_content_mutated = false
temporary_replay_cleanup = PASS
retrieval_executed = false
evaluation_metrics_computed = false
exp11b_retrieval_authorized = false
exp12_authorized = false
```

Seeds congeladas preservadas:

```text
20261005
20261006
20261007
20261010
20261011
20261013
20261017
20261021
20261023
20261024
```

## 4. Contrato gobernado de identidad bancaria

Los 14 campos contractuales verificados por Prompt41 y vinculados por el closure record son:

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
triple_comparison_status = PASS_EXACT_20_OF_20
frozen_official_match_count = 20
frozen_official_mismatch_count = 0
frozen_replay_match_count = 20
frozen_replay_mismatch_count = 0
official_replay_match_count = 20
official_replay_mismatch_count = 0
bank_identity_mismatch_count = 0
```

## 5. Clasificación del código de retorno 2

```makefile
observed_return_code = 2
blocking_for_governed_bank_identity = false
failure_field = total_bank_descriptor
failure_field_is_part_of_required_14_identity_contract = false
max_absolute_delta = 5.329070518200751e-15
historical_descriptor_tolerance = 1e-12
within_historical_descriptor_tolerance = true
bank_csv_content_affected = false
```

La clasificación no bloqueante se preserva sin ocultar el evento: el materializador produjo los 20 CSV antes de la comparación exacta adicional del manifest; las tres comparaciones de los 14 campos gobernados fueron 20/20; `bank_csv_sha256` y `size_bytes` están dentro del contrato; el fallo terminal correspondió a `total_bank_descriptor`, fuera de esos 14 campos. El delta máximo quedó dentro de la tolerancia histórica `1e-12`, mientras la comparación posterior del manifest aplicó igualdad Python exacta.

## 6. Clasificación epistemológica

```text
RUNTIME_REPLAY_AND_OFFICIAL_OBSERVATION = CODEX_LOCAL_RUNTIME_EVIDENCE / NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR
```

La auditoría externa aprobó la evidencia versionada para integración, pero no se afirma que el auditor externo haya reejecutado el replay, observado directamente los bancos locales o promovido estos eventos runtime a GitHub CI.

## 7. Fase A — Integración exacta

```makefile
integration_method = git merge --ff-only origin/codex/exp11b-portability-replay-proof-v01
pre_integration_main = 6846537602539506c8e90426daad05252cc982b9
post_integration_main = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
post_integration_origin_main = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
integrated_tree = 5ead782eeb0d25a9ef1965f43de7036eedf0a0eb
approved_candidate_tree = 5ead782eeb0d25a9ef1965f43de7036eedf0a0eb
tree_identity = true
candidate_vs_origin_main_diff = empty
merge_commit_created = false
additional_commit_created_in_phase_a = false
```

La integración fue un fast-forward exacto de `6846537...` a `7d7267f...`, seguido de push exclusivo de `main`.

## 8. Fase B — Registro formal de cierre

```makefile
branch = codex/exp11b-portability-debt-external-closure-v01
candidate_commit = 09ff184854659110f7711b3eee65fc18927649da
parent = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
tree = b39f169e898492c0cbb1b4944ee579c7fc5eea71
commit_count = 1
ahead_of_main = 1
behind_main = 0
published = true
integrated_to_main = false
```

Único path añadido:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_external_closure_v0.1.json
```

```makefile
closure_record_blob = bfbeedff9025ae928a85ab8b65a261ff475422cb
changed_path_count = 1
existing_paths_modified = 0
```

Estado interno del registro:

```text
artifact_id = exp11b_portability_debt_external_closure_v0.1
schema_version = 1
baseline_commit = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
status = CANDIDATE_CLOSURE_RECORD / EXTERNAL_DECISION_ALREADY_PASS / PENDING_GIT_AUDIT_AND_INTEGRATION
external_audit_verdict = PASS / APPROVED_FOR_PORTABILITY_DEBT_CLOSURE
prompt40_candidate_status = REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED
prompt41_replay_proof_status = APPROVED_BY_EXTERNAL_AUDIT / INTEGRATED
EXP11B_PORTABILITY_DEBT = CLOSED_BY_EXTERNAL_AUDIT / NOT_YET_INTEGRATED_AS_CLOSURE_RECORD
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## 9. Bindings del closure record

| Binding | Path | Git blob / SHA-256 |
|---|---|---|
| Proof Prompt41 | `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_replay_proof_v0.1.json` | `ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead` |
| Materializador | `src/experiments/materialize_exp11b_banks_v01.py` | `ba64a85b4bb8bfa9f163a4f1115440486b7d8d2c` |
| Config de materialización | `src/configs/exp11b_bank_materialization_v0.1.json` | `cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8` |
| Ledger congelado | `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_hashes_v0.1.csv` | `a375c02e8364bc131a358646ba1c4401acef94d1` |
| Manifest de materialización | `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_materialization_manifest_v0.1.json` | `f06227780137a7977521a01226e0775ac4187b86` |
| Config retrieval gate | `src/configs/exp11b_retrieval_execution_gate_v0.1.json` | `905645027df16d80fb99c3ba090c185f6c730c80` |
| Manifest retrieval gate | `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_gate_manifest_v0.1.json` | `6ea8ad94e7188180f35aa845d18b3476a22f5ab8` |
| Inventory retrieval | `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_input_inventory_v0.1.json` | `95416679b939f7f719d5e18508bd628d9c4ef08d` |
| H100 | `data/processed/data_aduanas_historico_clase87_v0.2.csv` | SHA-256 `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff` |
| EVAL | `data/processed/data_aduanas_evalset_clase87_v0.2.csv` | SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941` |

## 10. Resolución de procedencia de configuración

```makefile
canonical_lf_sha256 = a7fa158dcf13e4b293e3de51351f814305cf5208b08395d5de8994f2d69c710c
windows_crlf_sha256 = 39c27e6791bcc5d574a2c132af59bbe99a4793ee0506d95724ad8f2d632a5e17
git_blob = cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8
semantic_json_equal = true
classification = SAME_GIT_BLOB_EQUIVALENT_JSON_LF_VS_CRLF_CHECKOUT_REPRESENTATION
semantic_config_drift = false
```

## 11. Notice histórico y alcance prospectivo

El notice histórico:

```text
retrieval_authorization_blocked_pending_external_audit = true
```

permanece inmutable en el artefacto histórico. El closure record registra prospectivamente:

```makefile
blocking_condition_status = SUPERSEDED_FOR_PORTABILITY_DEBT_BY_PROMPT41_EXTERNAL_AUDIT
retrieval_authorization_requires_separate_future_block = true
historical_notice_mutated = false
```

Esta resolución no autoriza retrieval.

## 12. Inmutabilidad y prohibiciones verificadas

```makefile
historical_gate_artifacts_mutated = false
retrieval_gate_config_modified = false
retrieval_gate_manifest_modified = false
retrieval_input_inventory_modified = false
materialization_manifest_modified = false
materialization_ledger_modified = false
prompt41_proof_modified = false

official_h150_h200_results_root_exists = false
retrieval_executed = false
evaluation_metrics_computed = false
h150_h200_results_created = false
exp11b_retrieval_authorized = false
exp12_authorized = false

canonical_plan_modified = false
article_modified = false
attempt06_modified = false
group2b_opened = false
group3_opened = false
```

No se reejecutó Prompt41, no se rematerializaron bancos oficiales, no se ejecutó BM25/retrieval, no se calcularon métricas y no se modificaron H100, DEV, EVAL, EXP12, Plan Maestro ni Article.

## 13. Referencias finales

```makefile
main = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
origin/main = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
origin/codex/exp11b-portability-replay-proof-v01 = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
origin/codex/exp11b-portability-debt-external-closure-v01 = 09ff184854659110f7711b3eee65fc18927649da
origin/docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
candidate_working_tree_tracked_clean = true
```

```text
PROMPT42 = COMPLETED
PROMPT41_REPLAY_PROOF = APPROVED / INTEGRATED_IN_MAIN
PORTABILITY_CLOSURE_RECORD = CANDIDATE / PENDING_EXTERNAL_GIT_AUDIT
EXP11B_PORTABILITY_DEBT = CLOSED_BY_EXTERNAL_DECISION / PENDING_CLOSURE_RECORD_INTEGRATION
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
