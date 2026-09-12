# RESPUESTA PROMPT 44 — PAQUETE DE EJECUCION EXP11B RETRIEVAL H150/H200

```makefile
PROMPT44 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## 1. Refs iniciales y finales

```makefile
origin/main_initial = 09ff184854659110f7711b3eee65fc18927649da
origin/main_final = 09ff184854659110f7711b3eee65fc18927649da
origin/docs/plan-maestro-temporal-2026-08-31_initial = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/docs/plan-maestro-temporal-2026-08-31_final = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript_initial = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/article/main-manuscript_final = 254b1e6df736fa9938ac86a515d65b36f4d361c5
portability_replay_proof_blob = ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead
portability_closure_blob = bfbeedff9025ae928a85ab8b65a261ff475422cb
prompt40_rejected_candidate_is_ancestor = false
preconditions = PASS
```

El candidato rechazado `799156b3c98858fbe081de73f381030426174ce1` no es ancestro de `main` ni del candidato Prompt44.

## 2. Diagnostico de arquitectura

El diagnostico obligatorio fue confirmado sin drift:

- `evaluate_historical_retrieval_data_aduanas_v02.py` contiene los helpers BM25 canonicos reutilizables.
- Su `evaluate()`/CLI esta ligado al H100 congelado por SHA-256 y por `EXPECTED_HISTORICAL_ROWS=2950`; por ello no se invoca directamente como CLI sobre H150/H200.
- `run_exp11a_historical_size_sensitivity_v03.py` demuestra el patron correcto para bancos variables: llama directamente `_build_bm25_index`, `_bm25_scores`, `_dedup_candidates`, `_rank_of` y `mrr_from_rank`.
- El nuevo runner importa esos helpers; no copia ni redefine la formula BM25.

La semantica preservada es: normalizacion NFKD en minusculas sin marcas combinantes, tokenizer `regex_[a-z0-9]+`, `k1=1.5`, `b=0.75`, candidate depth 100, `k=[1,3,5,10,50]`, desempate por score descendente e ID historico ascendente, deduplicacion por primera fila rankeada de NANDINA y MRR canonico.

## 3. Identidad local de los 20 bancos

Clasificacion epistemologica:

`CODEX_LOCAL_BANK_PREFLIGHT / NOT_INDEPENDENT_GITHUB_RUNTIME_OBSERVATION`

Se validaron los 14 campos gobernados contra inventory, manifest y ledger. Resultado global: `20/20 PASS_EXACT`, `10 H150`, `10 H200`, `bank_identity_mismatch_count=0`.

| bank_id | seed | rows | new_rows | SHA-256 | size_bytes | estado |
|---|---:|---:|---:|---|---:|---|
| EXP11B_R01_H150 | 20261005 | 4416 | 1466 | a95ccaa947994e9e01392c1f519f7a19ef015b560a2c3aa77f6bf3ee7a5961db | 5337882 | PASS_EXACT |
| EXP11B_R01_H200 | 20261005 | 5954 | 3004 | 20c987e52f0d6a221ffaa756527b1b4b571117a57c839909908cd7e7441abe49 | 7265669 | PASS_EXACT |
| EXP11B_R02_H150 | 20261006 | 4535 | 1585 | 331762d93446c575abaf59c76c38eb55e106431c811dda48c99d489cff279000 | 5415360 | PASS_EXACT |
| EXP11B_R02_H200 | 20261006 | 5897 | 2947 | 0b6772d0ead99f352ffde4170bceb6e443da0b84a3b652bee845f05c765cb468 | 7121941 | PASS_EXACT |
| EXP11B_R03_H150 | 20261007 | 4357 | 1407 | 1001a3821aec92b1f7c785ba620100bb68acee0a2e4312bb041f75578eb13fb2 | 5235342 | PASS_EXACT |
| EXP11B_R03_H200 | 20261007 | 5832 | 2882 | d27fcc4a9711cbc4d9126fc337518d09430a988fae554ee12246b1fec4205b77 | 7113741 | PASS_EXACT |
| EXP11B_R04_H150 | 20261010 | 4422 | 1472 | 2f21215da09a2e9bdb0fe72b9dae56a88f03109cbab901a0b236633aa7410850 | 5364067 | PASS_EXACT |
| EXP11B_R04_H200 | 20261010 | 5890 | 2940 | b2488c0b0a0525f0d6a98dd54071fd715afefbab719d526e4779283d9bf67887 | 7189470 | PASS_EXACT |
| EXP11B_R05_H150 | 20261011 | 4512 | 1562 | 74524582ec2158d2e87ac46d06a2259b7d03a674212678d39713345517d08f11 | 5417826 | PASS_EXACT |
| EXP11B_R05_H200 | 20261011 | 5977 | 3027 | 80ac01f63c184237c8ff36a5ecd1fef38d18562114bd60842cb2bdc8f9ee5cae | 7258140 | PASS_EXACT |
| EXP11B_R06_H150 | 20261013 | 4467 | 1517 | 66259a5fa9058b1f3c58601541aee4637f758878f18d8757e4c1bfc21de397a8 | 5408676 | PASS_EXACT |
| EXP11B_R06_H200 | 20261013 | 6039 | 3089 | 548159b34b19be379d7e1e54f170985466189c77796883fa4c8a2429c0d926fd | 7370152 | PASS_EXACT |
| EXP11B_R07_H150 | 20261017 | 4409 | 1459 | f00e9625b0684200e2a2fe91b3bcec1abeb05e3d444244177371ff7489b51345 | 5323182 | PASS_EXACT |
| EXP11B_R07_H200 | 20261017 | 5942 | 2992 | 221030d48308566f7e79f1ee7a37b1f9c9d6f7d4aadaba709a691fd417e1aa57 | 7240818 | PASS_EXACT |
| EXP11B_R08_H150 | 20261021 | 4448 | 1498 | d7bf195592c749333820cb1c1bc8c3202a446a1d5a6ebc2ef051593f52356bb8 | 5366465 | PASS_EXACT |
| EXP11B_R08_H200 | 20261021 | 5841 | 2891 | 7005a43687d80bd4454389fb34f96577911b75558618ab4b63104341ae85875a | 7142238 | PASS_EXACT |
| EXP11B_R09_H150 | 20261023 | 4439 | 1489 | 6353eb3081c31e829f978958ab0ab5d000633e1c678ef7aaf691444b33245f9d | 5294727 | PASS_EXACT |
| EXP11B_R09_H200 | 20261023 | 5859 | 2909 | 2c72fb62deb0cecfe90b49b991bf6918ab4177a35aebb8e88bf74b08058fd841 | 7075401 | PASS_EXACT |
| EXP11B_R10_H150 | 20261024 | 4483 | 1533 | 163f5b9f6284a40b21da405b958cccb571df7b4932381ecb832a2c771ca850b9 | 5393797 | PASS_EXACT |
| EXP11B_R10_H200 | 20261024 | 5868 | 2918 | ed570fccf8913fbd3416157013f152697dc1ed6358313e379e6b9e93af11cdf2 | 7149970 | PASS_EXACT |

La identidad completa de 14 campos de cada banco, incluido `composition_sha256` y los tres hashes de orden, queda versionada en el readiness artifact.

## 4. Paths y bindings del paquete

```text
src/experiments/run_exp11b_historical_retrieval_h150_h200_v01.py
  git_blob = 81e1ead26bd1c4635befdfbe6886439c4c4a0238
  sha256 = ef863f3c62c3008756d8b5d55cc0e97e993491ccf97efa4885b6a9d0611c1dd4

src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.1.json
  git_blob = b8be6af3cfa0f224db15838acb08a483889f5ae5
  sha256 = 691c8747f248ec112c34140928860567715248812b5978a79ca7d799c966f893

outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.1.json
  git_blob = 4af44e84efeb124da1feb9fbeb6d8df4a011f29d
  sha256 = b9a41e2967edcf1658fadeeac1fe14db522bd93f4bc04c6b669d69b675b14797
```

Los 14 source bindings versionados resolvieron exactamente, incluido EVAL, H100, gate config/manifest/inventory, manifest/ledger de bancos, replay proof, closure record, evaluador EXP-04, runner EXP11A, materializador, metric helper, hash helper y path helper.

## 5. Entorno y validacion estatica

```makefile
python_implementation = CPython
python_version = 3.12.14
platform = Windows-11-10.0.26200-SP0
machine = AMD64
numpy = 2.3.5
pandas = 3.0.1
config_json = PASS
py_compile = PASS
import = PASS
cli_help = PASS
working_tree_controlled = PASS
```

La CLI expone exclusivamente los modos mutuamente excluyentes `--preflight`, `--self-test-h100` y `--execute-official`.

## 6. Preflight unico

`--preflight` fue invocado exactamente una vez.

```makefile
status = PASS
mode = PREFLIGHT_ONLY
invocation_count = 1
bank_count = 20
h150_count = 10
h200_count = 10
bank_identity_mismatch_count = 0
eval_sha_match = true
h100_sha_match = true
canonical_source_binding_mismatch_count = 0
official_output_root_exists = false
authorization_artifact_exists = false
retrieval_executed = false
metrics_computed = false
official_bank_write_count = 0
official_bank_content_mutated = false
```

## 7. Self-test H100 unico

`--self-test-h100` fue invocado exactamente una vez y no abrio bancos H150/H200.

```makefile
status = PASS
mode = H100_SELF_TEST_ONLY
invocation_count = 1
Top1_numerator = 538
Top3_numerator = 709
Top5_numerator = 806
Top10_numerator = 941
Top50_numerator = 1047
all_top_numerator_deltas = 0
MRR_observed = 0.6297077493524843
MRR_expected = 0.6297077493524843
MRR_abs_delta = 0.0
MRR_abs_tolerance = 1e-12
h150_h200_bank_open_count = 0
temporary_self_test_cleanup = PASS
official_output_root_exists = false
```

## 8. Guard negativo sin autorizacion

`--execute-official` fue invocado una vez sin authorization artifact y termino fail-closed antes de preflight, scoring o creacion de outputs.

```makefile
guard_status = PASS
classification = OFFICIAL_EXECUTION_BLOCKED_NO_AUTHORIZATION
exit_code = 2
blocked_before_preflight = true
blocked_before_scoring = true
blocked_before_output_creation = true
authorization_consumed = false
```

## 9. No contaminacion

```makefile
official_output_root_exists = false
future_authorization_artifact_exists = false
h150_h200_retrieval_invocation_count = 0
h150_h200_metrics_observed = false
h150_h200_case_rankings_observed = false
official_bank_write_count = 0
official_bank_content_mutated = false
temporary_self_test_cleanup = PASS
EXP12_authorized = false
EXP12_executed = false
```

No se ejecuto retrieval H150/H200, no se calcularon ni observaron metricas o rankings H150/H200, y no se creo el output root oficial.

## 10. Identidad Git del candidato

```makefile
branch = codex/exp11b-retrieval-execution-package-v01
candidate_commit = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1
parent = 09ff184854659110f7711b3eee65fc18927649da
tree = 4fcc4959db2d2673ee8f19a9c6cb248c3cb312cb
ahead_of_origin_main = 1
behind_origin_main = 0
remote_candidate = 26b9e2bcf6dad74231f208f9137ffb0e39caf2e1
candidate_published = true
```

Changed paths exactos:

```text
A outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.1.json
A src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.1.json
A src/experiments/run_exp11b_historical_retrieval_h150_h200_v01.py
```

```makefile
existing_historical_files_modified = false
plan_maestro_modified = false
article_modified = false
EXP12_modified = false
prompt40_candidate_incorporated = false
temporary_results_committed = false
authorization_committed = false
scientific_working_tree_clean = true
```

## 11. Persistencia administrativa

```makefile
administrative_branch = codex/prompts-temporary
administrative_parent = 629bbb4fcdb327cccf6a7de0bcbd3c95346cdcd8
administrative_path = codex_prompts_tmp/44_RESPUESTA_PREPARAR_PAQUETE_EJECUCION_EXP11B_RETRIEVAL_H150_H200.md
administrative_commit = SELF / origin/codex/prompts-temporary HEAD containing this response
administrative_content_scope = RESPONSE_ONLY
```

## 12. Estado terminal

```makefile
PROMPT44 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
BLOCKERS = NONE_FOR_EXTERNAL_AUDIT
```
