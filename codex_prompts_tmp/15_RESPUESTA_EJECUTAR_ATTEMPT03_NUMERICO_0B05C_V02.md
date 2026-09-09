### A. Preflight Git y autorización

```makefile
execution_branch = codex/0b05c-numerical-attempt03-v02
execution_branch_initial_head = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
origin_main = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
authorized_tree = 4d0703327c2d9e05ecf19fd04f5a8c7d808bd0f6
authorized_parent = c44f447cb941c512cd70712cf7c3e4bc670ab05a
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
tracked_worktree_clean = true
gate_status = APPROVED / INTEGRATED
authorization_readiness = AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION
gate_four_authorizations = AUTHORIZED
authorization_record_present = true
authorization_record_validation = PASS
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
EV03_spec = AUTHORIZED / NOT_EXECUTED
EV04_spec = AUTHORIZED / NOT_EXECUTED
D1A_spec = AUTHORIZED / NOT_EXECUTED
runtime_authorization_record_present_before_attempt = false
unified_sensitivity_summary_present_before_attempt = false
future_roots_present_before_attempt = false
corrective_results_present_before_attempt = false
model_size_bytes = 470637416
model_sha256 = ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87
preflight_git_and_authorization = PASS
```

Se creó un worktree aislado desde el commit autorizado exacto, sin commits propios. La copia local del modelo congelado fue verificada antes de la ejecución y no fue staged ni versionada. No se limpió ni alteró evidencia local/ignored de Attempt01/Attempt02.

### B. Preflight autorizado

```makefile
authorized_preflight_invocations_before_attempt = 1
authorized_preflight_status = PASS
authorized_preflight_mode = AUTHORIZED_PREFLIGHT_ONLY
execution_authorization_commit = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
four_authorizations = AUTHORIZED
future_roots_present = false
numerical_execution_occurred = false
side_effects = 0
```

El preflight read-only pasó. La invocación interna posterior de preflight dentro de `--execute-authorized` formó parte de la única ejecución autorizada.

### C. Attempt03

```makefile
command = C:\Users\Vladimir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -B -m src.experiments.run_0b05c_corrective_numerical_v02 --execute-authorized
attempt03_invocations = 1
start_local = 2026-09-09T08:08:45.583-05:00
end_local = 2026-09-09T08:09:01.215-05:00
exit_code = 1
completed_steps = 6 / 19
last_completed_step = 06_EV03_corrected_evaluation
last_started_step = 07_EV04_Decision885_control_reproduction
last_started_step_completed = false
retry_performed = false
resume_performed = false
manual_component_execution_performed = false
```

Excepción exacta:

```text
src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact
```

El fallo ocurrió en `evaluate_normative_bm25_corrective_0b05c_v01.compare_control_reproduction()` durante `reproduce("EV04")`, antes de que el paso 07 pudiera registrarse como completado. No se reintentó, reanudó, corrigió ni ejecutó componente alguno por separado.

### D. Controles EV03/EV04

EV03 alcanzó y superó el paso 03 de verificación:

```makefile
EV03_Decision885_control = PASS_EXACT
EV03_LOGICAL_INDEX_IDENTITY = EXACT
EV03_ranking_schema_exact = true
EV03_case_summary_schema_exact = true
EV03_ranking_exact = true
EV03_case_summary_exact = true
EV03_metrics_exact = true
EV03_ranking_rows = 50327
EV03_cases = 1056
EV03_ranking_sha256 = d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
EV03_case_summary_sha256 = f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
```

EV04 generó el control, pero falló su comparación obligatoria antes de `PASS_EXACT`:

```makefile
EV04_Decision885_control = FAIL / NOT_PASS_EXACT
EV04_ranking_sha256_observed = fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662
EV04_ranking_sha256_frozen = fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662
EV04_case_summary_sha256_observed = 17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634
EV04_case_summary_sha256_frozen = 17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634
EV04_ranking_and_case_bytes_exact = true
EV04_metrics_exact = false
```

La inspección read-only de los JSON ya generados mostró que el control congelado incluye evidencia `mrr_at_100`, `mrr_at_200`, sus numerator/denominator, `mrr_101_200_contribution`, `mrr_101_200_contribution_numerator` y `mrr_definition`; además, su `metric_table` comienza con filas `mrr_at_100` y `mrr_at_200`. El output reproducido conserva solo la fila legacy `mrr` y no esos campos adicionales. No se recalculó ni reparó ningún artefacto.

### E. D1a

```makefile
D1A_step_started = false
D1A_step_completed = false
D1A_corrected_corpus_present = false
D1A_corrected_index_present = false
D1A_evaluation_present = false
D1A_ranking_top200_present = false
D1A_case_summary_present = false
D1A_case_level_comparison_present = false
D1A_aggregate_comparison_present = false
D1A_execution_manifest_present = false
D1A_hash_ledger_present = false
D1A_17_metrics_generated = false
```

D1a no fue ejecutado manualmente después del fallo.

### F. Runtime provenance / manifest / ledger

El paso 01 creó el runtime authorization record antes del fallo:

```makefile
runtime_authorization_record_present = true
runtime_authorization_record_status = PASS
runtime_authorization_record_mode = AUTHORIZED_PREFLIGHT_ONLY
runtime_authorization_record_sha256 = 5df72255bfffe3dca2fb9f4d256d18c65537c526b370941dd5b22e02c3f69fb6
runtime_authorization_record_size_bytes = 2441
execution_authorization_commit = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
authorization_baseline_commit = c44f447cb941c512cd70712cf7c3e4bc670ab05a
authorization_record_git_blob_sha1 = 5d963214a8ab0a614dc6917a71b0136397625fe9
authorization_record_canonical_sha256 = 06403316f34eafa70af63f07061aeb21d83611ba285f7cc4e4c1108abfaddfbe
authorization_record_size_bytes = 1638
authorized_gate_binding = f34977a96bf0d14271cacfc4f03f295ccf7f5aef / 274cac1fdcb031221d2213983081e6403a385c7f1387679d9c67ef18c3dc8356 / 26638
authorized_ev03_binding = f435dcc831f2882a8a5ea49e76f7b77325f53024 / ffd35532c6d9d5ce5aea4b7bc9336c063a81775073d91b8d4aa5cf4ae834eb83 / 20597
authorized_ev04_binding = fbcab8b9581c79cb876f78b8efa0b3e3551fa910 / f419ba9803279e3b3d8da22108ab62f9fb1980fd93803c3848c436e7561de203 / 26991
authorized_d1a_binding = 25e36c821cab1ee9c6b36a30a5ecb4110880103a / 1668620930730b2186184f1cf8817b701ee3ff48ac8e1dcf796fc71f9ec9b282 / 16936
execution_manifest_present = false
exact_runtime_ledger_present = false
unified_sensitivity_summary_present = false
ledger_mismatch_count = NOT_AVAILABLE / STEP_NOT_REACHED
ledger_missing_or_extra = NOT_EVALUATED / STEP_NOT_REACHED
```

Inventario read-only de los 17 archivos parciales preservados, expresado como `path | size_bytes | sha256`:

```text
data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.2.jsonl | 3614411 | 6ecb82fe594853ec8cdd4ffa1c25e198612c988e13b5bd5332afbdfff6a8e0f3
data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.2/index.pkl | 918320 | 8f729ab4d841f2c4e52078d4dab6a2dc49049de3a71491d0424595aeaad3ce75
data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.2/index_metadata.json | 1523 | 3f70fbd7f3479268eabf5430554e6890724160998ad12680a8fa0eda24091211
data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.2/index.pkl | 918504 | b1421f526994b7df001b3d55e4990f92bc4a4c8b8d367a6c37e444b025461557
data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.2/index_metadata.json | 1484 | 9cb3d82aab557424faf6aeb3312746b30f37cb4def30fb354dc89b77abb379f7
data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.2/index.pkl | 6019545 | f828736ea700471c95d2b985bdd969d751cd36c3ca01c407049209010bdbe60b
data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.2/index_metadata.json | 1719 | 09830d6d7015870f9e169811d2225413c1af82cdd011e47039ecb4b468d9231f
outputs/audits/0b05c_corrective_numerical_runtime_v0.2/runtime_authorization_record_v0.2.json | 2441 | 5df72255bfffe3dca2fb9f4d256d18c65537c526b370941dd5b22e02c3f69fb6
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.2/normative_flat_case_summary.csv | 497252 | 7c51c5fc56c5b969191fe2587625d979d5e1d954d5f45ffb76102c5062d29bff
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.2/normative_flat_metrics.json | 5277 | 2224a5be9ac91e6dcaba19031e5e09cc3432332aa0f092bd328611134badeea0
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.2/normative_flat_results.csv | 13135996 | 37577911c843ea97510f0696bdbeb3aa21a993d630772ce3c511dbb546264618
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.2/normative_flat_case_summary.csv | 497448 | f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.2/normative_flat_metrics.json | 5281 | af93c4cb260703986f9aad2c3cf474ef5921fc6d27ac68fa13add3ad3a91f96f
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.2/normative_flat_results.csv | 13145709 | d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015
outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.2/normative_hierarchical_case_summary.csv | 607072 | 17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634
outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.2/normative_hierarchical_metrics.json | 7451 | 04041811eba0c64dcd9e61a2d84621c26636484e70d0c8ff50f2e17b084d4844
outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.2/normative_hierarchical_results.csv | 85426164 | fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662
```

### G. Resultados numéricos

```makefile
result_extraction = NOT_APPLICABLE / ATTEMPT03_FAILED_BEFORE_COMPLETE_VALIDATION
EV03_aggregate_interpretation = NOT_PERFORMED
EV04_corrected_results = NOT_GENERATED
D1A_results = NOT_GENERATED
unified_results = NOT_GENERATED
metric_impact_decision = NOT_PERFORMED
```

No se interpretó impacto, no se decidió downstream y no se cerró 0B-05C.

### H. Aislamiento

```makefile
future_roots_existing = 8 / 16
future_roots_absent = 8 / 16
partial_files_preserved = 17
partial_outputs_deleted = false
partial_outputs_modified_after_failure = false
tracked_worktree_clean = true
model_staged = false
model_versioned = false
gate_specs_authorization_record_modified = false
code_modified = false
tests_modified = false
docs_modified = false
canonical_plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false
v01_artifacts_modified = false
attempt01_attempt02_evidence_modified = false
```

Roots existentes preservados: EV03 control index/output, EV03 corrected corpus/index/output, EV04 control index/output y runtime audit root. Los roots EV04 correctivos, D1a y unified evaluation permanecen ausentes. No se limpió ni completó nada después del fallo.

### I. Commit científico

```makefile
scientific_branch = codex/0b05c-numerical-attempt03-v02
scientific_branch_head = 41d3259ff09d8a63cc3a12a7f11a146a603ee3ef
NO_SCIENTIFIC_COMMIT = true
scientific_push = NOT_PERFORMED
partial_outputs_versioned = false
main_modified = false
```

### J. Persistencia administrativa

```makefile
response_branch = codex/prompts-temporary
response_path = codex_prompts_tmp/15_RESPUESTA_EJECUTAR_ATTEMPT03_NUMERICO_0B05C_V02.md
admin_commit = SELF / docs: persist prompt 15 attempt03 numerical report
admin_commit_changed_paths = 1 / response_path_only
RESPONSE_PERSISTENCE = PASS
```

### K. Estado científico final

GROUP_2 = EN_CURSO

0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED

0B05C_V02_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED

0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED

0B05C_METRIC_IMPACT = NOT_DETERMINED

DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED

0B05C_CLOSURE = NOT_AUTHORIZED
