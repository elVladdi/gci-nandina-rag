# Respuesta Prompt30A - Correccion de decision metodologica MRR v0.4 / contrato MRR@200

## 1. Baseline y referencias

```text
repository = elVladdi/gci-nandina-rag
baseline_main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
origin_main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
tracked_working_tree_before_change = CLEAN
preflight = PASS
```

Candidato Prompt30 rechazado, preservado sin cambios:

```text
rejected_branch = codex/0b05c-ev04-mrr100-methodological-decision-v04
rejected_local_head = 0298a6a51181ba992e981063be87a9742ba266ef
rejected_remote_head = 0298a6a51181ba992e981063be87a9742ba266ef
rejected_artifact_blob = 60a146e101c77f9c9ffaa679cec5b6eeca94c36c
rejected_candidate_modified = false
```

Las once fuentes obligatorias fueron leidas integramente por objetos Git, sin retrieval ni evaluacion real.

## 2. Verificacion del hallazgo MRR@200

La evidencia congelada registra:

```text
legacy_mrr_numerator = 45.76874185264425
legacy_mrr = 0.04334161160288281
mrr_at_200_numerator = 45.76874185264425
mrr_at_200 = 0.04334161160288281
mrr_at_200_equals_legacy_mrr = true
mrr_definition = legacy mrr field is MRR@200 because EXP-04 Fase C retrieval_depth=200
```

El runner historico versionado en `ce239059d748a4baf8a2113df5398f50c0e14a58` usa:

```python
numerator = sum(float(row["reciprocal_rank"]) for row in case_rows)
value = float(numerator / denominator)
```

El candidato Prompt30 aplicaba una regla racional a todo cutoff y registraba para MRR@200 `0.043341611602882815`. Esa salida difiere 1 ULP del contrato legacy y contradice la equivalencia requerida entre `mrr` y `mrr_at_200`.

```text
external_audit_finding = MRR200_CONTRACT_COLLATERAL_DRIFT
finding_verified = true
finding_corrected_in_new_candidate = true
```

## 3. Calculos read-only

```text
calculation_class = CODEX_LOCAL_PURE_READ_ONLY_COMPUTATION
github_ci_evidence = NONE_USED
input_case_summary_blob = 5421bf1bf2082e2ba66ce045f804f1d02b77fd58
N = 1056
retrieval_or_evaluator_invoked = false
read_only_checks = PASS
```

MRR@100 prospectivo racional:

```text
numerator_binary64 = 44.33224687474575
numerator_hex = 0x1.62a8710ca9d98p+5
mrr_at_100_binary64 = 0.04198129438896378
mrr_at_100_hex = 0x1.57e927ce3818cp-5
```

MRR@200 legacy estable:

```text
legacy_numerator = 45.76874185264425
legacy_numerator_hex = 0x1.6e266220e1635p+5
legacy_mrr_at_200 = 0.04334161160288281
legacy_mrr_at_200_hex = 0x1.630df28c7d779p-5
```

Control negativo racional MRR@200:

```text
exact_rational_mrr_at_200 = 0.043341611602882815
exact_rational_mrr_at_200_hex = 0x1.630df28c7d77ap-5
ulp_distance_from_legacy = 1
selected_as_mrr_at_200_output = false
```

Contribucion 101-200 prospectiva racional:

```text
C101_200_rational = 4221638972662797829869925972156161758832328316869 / 2938847011382373982458217544917517734717582104000
contribution_numerator_binary64 = 1.4364949778985006
contribution_numerator_hex = 0x1.6fbe2286f13acp+0
contribution_rational = 4221638972662797829869925972156161758832328316869 / 3103422444019786925475877727432898727861766701824000
contribution_binary64 = 0.0013603172139190346
contribution_hex = 0x1.649957c8abdbep-10
computed_by_subtracting_rounded_floats = false
```

## 4. Decision metodologica corregida

```text
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
MRR200_ROLE = STABLE_LEGACY_CONTRACT / ENRICHED_ALIAS_OF_LEGACY_MRR
HISTORICAL_101_200_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
```

MRR@100 usa suma racional exacta desde `rank_ref`, N exacto y una sola conversion final del numerador y de la razon. No se reclama provenance historica para `.78`.

MRR@200 preserva el productor legacy en orden del case summary. `mrr_at_200_numerator`, `mrr_at_200_denominator` y `mrr_at_200` son aliases exactos de los campos legacy correspondientes. La razon racional S200/N no puede sustituir esa salida.

La contribucion 101-200 se deriva prospectivamente como `S200-S100` racional y se convierte una sola vez, tanto para numerador como para valor normalizado. No se obtiene restando floats redondeados.

```text
mrr_at_200_equals_legacy_mrr_required = true
mrr_at_200_rational_ratio_redefinition_forbidden = true
mrr_at_100_uses_prospective_exact_rational_rule = true
contribution_101_200_uses_prospective_exact_rational_rule = true
generic_exact_rational_cutoff_rule_applies_to_mrr_at_200_output = false
mrr200_contract_collateral_drift_removed = true
PASS_EXACT = REQUIRED / NOT_WEAKENED
```

## 5. Candidato corregido y compare

```text
branch = codex/0b05c-ev04-mrr-methodological-decision-v04-corrected
candidate_commit = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
candidate_parent = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
candidate_tree = ef6145872ac02da8b750c219b0708e679a9a5b7e
merge_base = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
candidate_behind_baseline = 0
candidate_ahead_baseline = 1
candidate_commit_count = 1
candidate_changed_path_count = 1
candidate_remote_head = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
candidate_integrated_to_main = false
```

```text
artifact_path = outputs/audits/0b05c_ev04_mrr_methodological_decision_v0.4/mrr_methodological_decision_v0.4.json
artifact_blob_sha1 = 26b4310979e042bc7bb4fa0594d1ef450bf0032e
artifact_id = 0b05c_ev04_mrr_methodological_decision_v0.4
schema_version = 1
decision_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
```

El compare baseline a candidato contiene exactamente un commit y un path nuevo. La rama fue creada directamente desde `main`; no hereda el commit Prompt30 rechazado.

## 6. Source bindings reales

| Fuente | Ref | Git blob SHA-1 |
|---|---|---|
| Diagnosis Attempt04 | `main` | `fca5712c615960b41cb2741c2164f19fc00df9dd` |
| Arithmetic provenance Prompt28 | `main` | `c3667f85b4f8ec51f026e2e3b706062da586a7f1` |
| Frozen case summary | `main` | `5421bf1bf2082e2ba66ce045f804f1d02b77fd58` |
| Frozen metrics artifact | `main` | `bc3b34cae7d8832426e6b2b56cb3d2d1541cdd57` |
| Frozen run metadata | `main` | `3cbbabd9d9446958e5a0b386f13bd32aec817fa1` |
| Gate C microaudit | `main` | `098bc50f382a54c9dca7025d0e2d4364ac27ad3b` |
| Limitation stratified metrics | `main` | `3e13cd52e8fac58bf4452c1c83a1fb11e233508b` |
| Historical Gate C test | `ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97` | `1d3e45c19b29ce7f1a38a4721f01b7e70d270e3c` |
| Historical hierarchical runner | `ce239059d748a4baf8a2113df5398f50c0e14a58` | `aadbec6bdc5c152def0a7e925d2cf30f16aa4c7d` |
| Current v0.3 producer | `main` | `3fb1346dcee357d7b1d2d430e3ca98c0bba1d1a0` |
| Rejected Prompt30 candidate | `0298a6a51181ba992e981063be87a9742ba266ef` | `60a146e101c77f9c9ffaa679cec5b6eeca94c36c` |

```text
source_bindings_verified_from_git = true
```

## 7. Prohibiciones y aislamiento

```text
main_modified = false
candidate_integrated = false
rejected_prompt30_candidate_modified = false
historical_artifacts_modified = false
historical_tests_modified = false
v03_artifacts_modified = false
v03_producer_modified = false
v04_code_built = false
v04_gate_or_specs_built = false
v04_authorization_created = false
attempt05_authorized = false
attempt05_executed = false
retrieval_executed = false
ev03_executed = false
ev04_real_executed = false
d1a_executed = false
eval_real_executed = false
model_inference_executed = false
canonical_plan_modified = false
article_modified = false
exp11b_or_exp12_touched = false
tolerance_round_nextafter_or_code_hardcoding_introduced = false
main_working_tree_clean = true
candidate_working_tree_clean = true
```

## 8. Persistencia administrativa

```text
administrative_branch = codex/prompts-temporary
administrative_path = codex_prompts_tmp/30A_RESPUESTA_CORREGIR_DECISION_METODOLOGICA_MRR_V04_CONTRATO_MRR200.md
administrative_scope = RESPONSE_ONLY
administrative_commit = THIS_COMMIT / HEAD QUE AGREGA EXCLUSIVAMENTE ESTE ARCHIVO
scientific_and_administrative_history_mixed = false
```

## 9. Estado cientifico final

```text
GROUP_2 = EN_CURSO
PROMPT30_CANDIDATE = REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED
PROMPT30_BLOCKING_FINDING = MRR200_CONTRACT_COLLATERAL_DRIFT
CORRECTED_METHODOLOGICAL_DECISION_CANDIDATE = BUILT / PENDING_EXTERNAL_AUDIT
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
MRR200_ROLE = STABLE_LEGACY_CONTRACT / ENRICHED_ALIAS_OF_LEGACY_MRR
V04_BUILD = NOT_AUTHORIZED / NOT_BUILT
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```
