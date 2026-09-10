# RESPUESTA PROMPT 32 — BUNDLE v0.4 INTEGRADO Y AUTORIZACIÓN ATTEMPT05 CANDIDATA

## Fase A — Integración v0.4

```makefile
repository = elVladdi/gci-nandina-rag
integration_method = git merge --ff-only
old_main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
new_main = 588962100362174df6486a3c6446276d8749743c
origin_main = 588962100362174df6486a3c6446276d8749743c
candidate = 588962100362174df6486a3c6446276d8749743c
tree = cc58251fee6d9d0855037f6bb342c3c1259e09d2
parent = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
compare_old_to_new = 0 behind / 1 ahead
changed_paths = 14
candidate_main_identity = true
additional_scientific_commit = false
V04_CANDIDATE_AUDIT = PASS / APPROVED_FOR_INTEGRATION
V04_BUNDLE = INTEGRATED
```

Los 14 paths y blobs integrados son exactamente los del candidato auditado:

| Git blob SHA-1 | Path |
|---|---|
| `82032bbc7d8bc1997f734f0e7565892e795e398e` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` |
| `9186b0cb40cf3d3d9a4c8552181918037d9385e8` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_hash_ledger_v0.4.json` |
| `eb3fdc0e850f6ad22d9cbebe386bab1260d8af77` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_manifest_v0.4.json` |
| `805f0d60c16fcbead5af1d1929b6be963a692bd8` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` |
| `053533ff9ea78404848c69790a8c46839444c1f3` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` |
| `5c3d7d83c447b542049bf290819b4eb790780b43` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` |
| `61cb524538e11f5f45f67d3b106deea2de7188cd` | `outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json` |
| `8b8b93c1a075fce555eabd4dd301533df89e6a1a` | `src/experiments/evaluate_normative_bm25_corrective_0b05c_v04.py` |
| `54b150a4bdde5f105ce89e7335fd7eaf6db999ed` | `src/experiments/prepare_0b05c_corrective_numerical_gate_v04.py` |
| `c545d32cb6ea6d037e7ee88c9916bff072c3b257` | `src/experiments/run_0b05c_corrective_numerical_v04.py` |
| `a6fc65a27f5dace40cd4651b400e1d6a4ac52bfa` | `src/experiments/run_d1a_corrective_0b05c_v04.py` |
| `d153189592a5407cbdb54ddbd976e6f76d558141` | `tests/test_0b05c_corrective_numerical_gate_v04.py` |
| `257a46d7b01262dbe2e081b8724d101d56a89c20` | `tests/test_0b05c_ev04_mrr_contract_v04.py` |
| `10396f1e5456ea6354d299a3c266115060cd507f` | `tests/test_d1a_corrective_0b05c_runner_v04.py` |

En `main`, el authorization record v0.4 no existe y `attempt05` permanece `NOT_AUTHORIZED / NOT_EXECUTED`.

## Fase B — Candidato de autorización

```makefile
authorization_branch = codex/0b05c-v04-attempt05-authorization-candidate
authorization_commit = 812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea
authorization_parent = 588962100362174df6486a3c6446276d8749743c
authorization_tree = 90bea7fa9deb9ca5da56274180efef6c31ac29cf
changed_paths = 5
AUTHORIZATION_CANDIDATE = VERSIONED / PENDING_EXTERNAL_AUDIT
AUTHORIZATION_IN_MAIN = NOT_YET_INTEGRATED
```

Paths y blobs exactos del candidato de autorización:

| Estado | Git blob SHA-1 | Path |
|---|---|---|
| Modificado | `782bb487744aedbf7b2f6ec098c2ee2c2837e077` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` |
| Nuevo | `5115bcaeaeb8a0ccfa2dee57fd130a930d216f10` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_numerical_authorization_record_v0.4.json` |
| Modificado | `67cf8d906eec206d7166a351589e950fbe3f3ddf` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` |
| Modificado | `fa7664bdfe887824e3e53b9cfa993345f2264a4a` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` |
| Modificado | `8ccad4fbb70471080f4b8fdaa101112b173584cb` | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` |

No cambiaron código, tests, manifest, hash ledger, shadow audit ni artefactos históricos.

## Authorization Record

```makefile
authorization_record_blob = 5115bcaeaeb8a0ccfa2dee57fd130a930d216f10
artifact_id = 0b05c_numerical_authorization_record_v0.4
schema_version = 3
authorization_baseline_commit = 588962100362174df6486a3c6446276d8749743c
baseline_external_audit = PASS / APPROVED_FOR_INTEGRATION
authorization_record_schema = PASS
baseline_artifact_bindings = PASS / 4
```

Bindings baseline derivados directamente de Git en `588962100362174df6486a3c6446276d8749743c`:

| Artifact | Git blob SHA-1 | Canonical Git blob SHA-256 | Bytes | Path |
|---|---|---|---:|---|
| `unified_gate` | `82032bbc7d8bc1997f734f0e7565892e795e398e` | `a5dede786f625b7e3eda6473d808dc6538262540d1ec96d2702bb9167eca002a` | 29108 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json` |
| `ev03_spec` | `053533ff9ea78404848c69790a8c46839444c1f3` | `ac77bb6058b4a722a1c7fa860f70e413661f9987077143061354f58afc745bf5` | 21130 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json` |
| `ev04_spec` | `5c3d7d83c447b542049bf290819b4eb790780b43` | `8b80daf254d1b73f2182a85599db42317fcb3b2c59088d0f32dafe62eacbb58e` | 29149 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json` |
| `d1a_spec` | `805f0d60c16fcbead5af1d1929b6be963a692bd8` | `9e7d69f8ee353248da1601ea53efb4c1594cdb6322b78a1d15ee60310282bc71` | 17469 | `outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json` |

## Validación Positiva Read-Only

Clasificación probatoria: `CODEX_LOCAL_READ_ONLY_PREFLIGHT / NOT_INDEPENDENT_GITHUB_CI`.

```makefile
validate_authorization_record_schema = PASS
baseline_proper_ancestor = PASS
baseline_artifact_bindings = PASS
immutable_projection_status = PASS
immutable_projection_mode = BASELINE_TO_AUTHORIZED_IMMUTABLE_PROJECTION
immutable_projection_allowed_fields_only = true
baseline_projection_sha256 = 72e2f509cda217b88d2282b7fb4847a967f39bf8b12ca0b2b53951bf8bf98cba
authorized_projection_sha256 = 72e2f509cda217b88d2282b7fb4847a967f39bf8b12ca0b2b53951bf8bf98cba

authorized_preflight_status = PASS
authorized_preflight_mode = AUTHORIZED_PREFLIGHT_ONLY
proof_four_authorizations = PASS
d1a_authorization_proof = PASS
d1a_preflight_status = PASS
d1a_preflight_mode = PREEXECUTION_CLOSED_READONLY
future_roots_present = false
numerical_execution_occurred = false
```

El modelo congelado se materializó solo como archivo ignorado local para comprobar su identidad durante el preflight. No fue commiteado ni publicado. No se llamó `execute_authorized()` ni se ejecutó ninguna operación del pipeline de 19 pasos.

## Estado Final

```makefile
main = 588962100362174df6486a3c6446276d8749743c
origin_main = 588962100362174df6486a3c6446276d8749743c
V04_BUNDLE = INTEGRATED

AUTHORIZATION_CANDIDATE = VERSIONED / PENDING_EXTERNAL_AUDIT
AUTHORIZATION_IN_MAIN = NOT_YET_INTEGRATED
ATTEMPT05_CANONICAL_MAIN = NOT_AUTHORIZED / NOT_EXECUTED
ATTEMPT05_CANDIDATE = AUTHORIZED / NOT_EXECUTED
ATTEMPT05 = NOT_EXECUTED

canonical_plan_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
canonical_plan_modified = false
article_modified = false
exp11b_modified = false
exp12_opened = false

retrieval_executed = false
EV03_real_executed = false
EV04_real_executed = false
D1a_real_executed = false
EVAL_real_executed = false
model_inference_executed = false
numerical_execution_occurred = false

0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
main_working_tree_clean = true
authorization_working_tree_clean = true
BLOCKERS = NONE
```

**RESULTADO FINAL: BUNDLE v0.4 INTEGRADO EN MAIN; CANDIDATO FORMAL DE AUTORIZACIÓN ATTEMPT05 PUBLICADO PARA AUDITORÍA EXTERNA; ATTEMPT05 NO EJECUTADO.**
