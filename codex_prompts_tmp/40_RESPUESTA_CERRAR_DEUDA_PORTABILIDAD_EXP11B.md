# RESPUESTA PROMPT 40 - CERRAR DEUDA DE PORTABILIDAD EXP11B

## Estado terminal

```makefile
PROMPT40 = COMPLETED
EXP11B_PORTABILITY_DEBT = CANDIDATE_CLOSED_PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## Referencias iniciales

```makefile
origin/main = 6846537602539506c8e90426daad05252cc982b9
origin/docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
0B05C_CLOSURE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
EXP11B_BANK_MATERIALIZATION = CLOSED / APPROVED / INTEGRATED
EXP11B_RETRIEVAL_EXECUTION_GATE = APPROVED / INTEGRATED
EXP11B_PORTABILITY_DEBT = OPEN
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
precondition_ref_drift = false
```

## Discrepancia de configuracion

```makefile
manifest_embedded_config_sha256 = a7fa158dcf13e4b293e3de51351f814305cf5208b08395d5de8994f2d69c710c
current_config_sha256 = 39c27e6791bcc5d574a2c132af59bbe99a4793ee0506d95724ad8f2d632a5e17
classification = PROVENANCE_CONFIG_HISTORY_MISMATCH_WITHOUT_BANK_CONTENT_MUTATION
subtype = CHECKOUT_EOL_REPRESENTATION_LF_VS_CRLF_SAME_GIT_BLOB
historical_config_state_recovered = true
historical_config_commit = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c
historical_config_git_blob = cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8
current_config_git_blob = cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8
same_git_blob = true
semantic_config_change = false
bank_content_mutation = false
```

La historia Git recupero el estado que corresponde a `a7fa...` en el commit
`95ffec4...`. Ese estado y `main` apuntan al mismo blob Git
`cda209dc...`. El contenido canonico LF del blob produce `a7fa...`; la
representacion del checkout Windows con `core.autocrlf=true` produce
`39c...`. La diferencia es de representacion EOL/procedencia y no una
mutacion semantica de la configuracion ni de los bancos.

## Identidad de los bancos

Se contrastaron los 20 registros del ledger, los 20 del manifest y los 20 del
inventario sobre los 14 campos congelados:

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
ledger_bank_count = 20
manifest_bank_count = 20
inventory_bank_count = 20
identity_fields_compared = 14
ledger_manifest_inventory_match_count = 20
bank_identity_mismatch_count = 0
bank_csv_present_count = 20
bank_csv_sha256_match_count = 20
bank_csv_sha256_mismatch_count = 0
bank_csv_size_match_count = 20
bank_csv_size_mismatch_count = 0
bank_csv_missing_count = 0
banks_versioned_in_git = false
banks_regenerable_from_versioned_inputs = true
```

Los 20 CSV materializados presentes en el path gobernado v0.1 coinciden en
SHA-256 y `size_bytes` con el ledger. Factualmente, el manifest declara
`banks_versioned_in_git=false`: los CSV no son blobs Git, mientras sus
identidades, manifest, ledger e inputs deterministas si estan versionados y el
manifest declara `banks_regenerable_from_versioned_inputs=true`. Esta condicion
se expone expresamente para la auditoria externa; no se rematerializo ningun
banco.

## H100 y EVAL

```makefile
H100_path = data/processed/data_aduanas_historico_clase87_v0.2.csv
H100_expected_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
H100_observed_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
H100_hash_status = PASS
EVAL_path = data/processed/data_aduanas_evalset_clase87_v0.2.csv
EVAL_expected_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
EVAL_observed_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
EVAL_hash_status = PASS
```

## Semantica BM25

El contrato semantico del gate y el inventario coincide campo por campo, con
cero mismatches. Los seis bindings de codigo/configuracion congelados tambien
coinciden con sus SHA-256:

```makefile
canonical_implementation_sha256 = 251b8f60d6591bbdfadaf3aa1d69103d55fbc1bfe63169df42f4150c3113e836
direct_exp11a_reuse_sha256 = e9f9ee27d869692d73e6414542a9d61c426f9e1a3613812db2915dd83462089f
rank_and_mrr_helpers_sha256 = 69889887d511ee1fdda760f490c703fefd3ea15d6c392b5863c6fffea94d13e4
sha256_input_helper_sha256 = 31562c7a1e6b1e0fd7b01ef0fb556ecb3e33a33072c51421fa15915d8117e2f5
project_path_resolution_sha256 = 2bf513a29e93b8f5582240ea0dcff050428011f2bda9bcb3fd1bfa13b92d11cb
exp11a_frozen_execution_contract_sha256 = 51faf2d21967017ace40cddc62c01f58c8ee31e41fe394a24a0667168336491e
code_binding_mismatch_count = 0
normalization = unicode_NFKD_lowercase_remove_combining_marks
tokenizer = regex_[a-z0-9]+
k1 = 1.5
b = 0.75
candidate_depth = 100
k_values = 1,3,5,10,50
ranking_order = descending_score_then_ascending_historical_case_id
bm25_semantics_preserved = true
```

## Criterio de cierre

```makefile
banks_match_frozen_ledger_and_manifest = true
bank_identity_mismatch_count = 0
H100_and_EVAL_hashes_match = true
bm25_semantics_preserved = true
config_difference_is_provenance_only = true
bank_rematerialization_required = false
closure_criteria_pass = true
external_audit_required = true
```

No se requiere rematerializar H150/H200 para preservar la validez
experimental: los CSV actuales coinciden 20/20 con las identidades congeladas,
la configuracion canonica Git es la misma, H100/EVAL permanecen exactos y la
semantica BM25 no cambio.

## Candidato publicado

```makefile
branch = codex/exp11b-portability-debt-closure-v01
candidate_commit = 799156b3c98858fbe081de73f381030426174ce1
candidate_parent = 6846537602539506c8e90426daad05252cc982b9
candidate_tree = 7c0d83108729a9adb18422bf8c3e6f641d581ead
commits_ahead_of_main = 1
changed_path_count = 1
changed_path = outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_closure_v0.1.json
candidate_published = true
local_remote_candidate_identity = true
tracked_working_tree_clean = true
```

El artefacto registra
`status=CANDIDATE_CLOSED_PENDING_EXTERNAL_AUDIT`; no declara cierre externo
definitivo, no modifica el gate/config existente y mantiene
`exp11b_retrieval_authorized=false`.

## Referencias finales y preservaciones

```makefile
main = 6846537602539506c8e90426daad05252cc982b9
origin/main = 6846537602539506c8e90426daad05252cc982b9
origin/codex/exp11b-portability-debt-closure-v01 = 799156b3c98858fbe081de73f381030426174ce1
origin/docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
official_H150_H200_output_root_exists = false
retrieval_executed = false
evaluation_metrics_computed = false
bank_rematerialization_executed = false
exp11b_retrieval_authorized = false
main_modified = false
plan_master_modified = false
article_modified = false
exp12_modified = false
additional_hardening_opened = false
scientific_tests_executed = false
```
