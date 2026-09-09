# Respuesta Prompt30 - Decision metodologica prospectiva MRR@100 `.77` / `.78`

## 1. Baseline y preflight

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

Las diez fuentes exigidas fueron leidas integramente sin ejecutar retrieval, evaluacion ni modelo. Sus objetos Git se verificaron antes de construir el candidato.

## 2. Candidato cientifico

```text
branch = codex/0b05c-ev04-mrr100-methodological-decision-v04
candidate_commit = 0298a6a51181ba992e981063be87a9742ba266ef
candidate_parent = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
candidate_tree = 7870905328472fb0c93469cd40a859ae70bf7331
merge_base = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
candidate_behind_baseline = 0
candidate_ahead_baseline = 1
candidate_commit_count = 1
candidate_changed_path_count = 1
candidate_remote_head = 0298a6a51181ba992e981063be87a9742ba266ef
candidate_integrated_to_main = false
```

```text
artifact_path = outputs/audits/0b05c_ev04_mrr100_methodological_decision_v0.4/mrr100_methodological_decision_v0.4.json
artifact_blob_sha1 = 60a146e101c77f9c9ffaa679cec5b6eeca94c36c
artifact_id = 0b05c_ev04_mrr100_methodological_decision_v0.4
schema_version = 1
decision_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
```

El compare `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6..0298a6a51181ba992e981063be87a9742ba266ef` contiene exactamente un commit y agrega exclusivamente el JSON anterior.

## 3. Decision metodologica materializada

```text
methodological_decision = ADOPT_CASE_DERIVED_DOT78_AS_PROSPECTIVE_REFERENCE_PRESERVE_DOT77_AS_HISTORICAL_LITERAL
historical_arithmetic_path = NOT_RECOVERED
```

### `.77` historico

```text
mrr_at_100_numerator = 44.33224687474574
mrr_at_100_numerator_float_hex = 0x1.62a8710ca9d97p+5
mrr_at_100 = 0.04198129438896377
mrr_at_100_float_hex = 0x1.57e927ce3818bp-5
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
historical_provenance = NOT_RECOVERED
```

El literal `.77` queda inmutable como valor reportado historicamente por Gate C. No se normalizo ningun artefacto historico y no se usara como oracle computacional prospectivo.

### `.78` prospectivo

```text
numerator_binary64 = 44.33224687474575
numerator_binary64_float_hex = 0x1.62a8710ca9d98p+5
mrr_at_100_binary64 = 0.04198129438896378
mrr_at_100_binary64_float_hex = 0x1.57e927ce3818cp-5
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
historical_provenance_claimed_for_dot78 = false
```

La adopcion de `.78` define solo la referencia computacional prospectiva reproducible. No afirma que `.78` fuera el valor historico verdadero de Gate C.

### Contrato reductor canonico prospectivo

El artefacto registra integralmente estas trece reglas:

1. Fuente: `rank_ref` entero del case summary para cada cutoff `K`.
2. Contribucion: `1/rank_ref` cuando `1 <= rank_ref <= K`, y `0` en otro caso.
3. Acumulacion racional exacta, sin acumulacion float intermedia.
4. Invariancia matematica respecto del orden de filas.
5. Denominador igual al numero exacto de casos `N`.
6. Una sola conversion final del numerador racional a binary64.
7. Una sola conversion final de `numerator_rational/N` a binary64.
8. Contribucion 101-200 como `S_200-S_100` racional, nunca resta de floats redondeados.
9. Sin tolerancias.
10. Sin redondeo decimal de conveniencia.
11. Sin `nextafter`.
12. Sin escalares de salida hardcodeados en el productor.
13. Sin correccion manual para forzar `.77` o `.78`.

`PASS_EXACT` permanece obligatorio. Ranking y case summary historicos continuan como controles frozen exactos. Los enriched MRR expected y actual deberan derivarse independientemente desde sus respectivos case summaries bajo la misma regla racional y compararse por igualdad exacta. Ningun control fue debilitado para permitir Attempt05.

## 4. Comprobacion racional read-only

Clasificacion probatoria:

```text
computation_class = CODEX_LOCAL_PURE_READ_ONLY_COMPUTATION
github_ci_evidence = NONE_USED
input_case_summary_blob = 5421bf1bf2082e2ba66ce045f804f1d02b77fd58
N = 1056
retrieval_or_evaluator_invoked = false
rational_check = PASS
```

Resultado MRR@100:

```text
S100_rational = 1934200815516088018 / 43629659037605025
S100_binary64_repr = 44.33224687474575
S100_binary64_hex = 0x1.62a8710ca9d98p+5
MRR100_rational = 967100407758044009 / 23036459971855453200
MRR100_binary64_repr = 0.04198129438896378
MRR100_binary64_hex = 0x1.57e927ce3818cp-5
matches_declared_prospective_reference = true
```

Control MRR@200 y contribucion 101-200:

```text
S200_rational = 541930033409542605714417802343096476523631054751252721 / 11840614608859584775324158488472678953177138297016000
MRR200_rational = 541930033409542605714417802343096476523631054751252721 / 12503689026955721522742311363827148974555058041648896000
MRR200_binary64_repr = 0.043341611602882815
MRR200_binary64_hex = 0x1.630df28c7d77ap-5
contribution_101_200_rational = 4221638972662797829869925972156161758832328316869 / 2938847011382373982458217544917517734717582104000
contribution_101_200_binary64_repr = 1.4364949778985006
contribution_101_200_binary64_hex = 0x1.6fbe2286f13acp+0
computed_by_subtracting_rounded_floats = false
```

## 5. Source bindings reales

| Fuente | Ref | Git blob SHA-1 |
|---|---|---|
| Diagnosis Attempt04 | `main` | `fca5712c615960b41cb2741c2164f19fc00df9dd` |
| Arithmetic provenance Prompt28 | `main` | `c3667f85b4f8ec51f026e2e3b706062da586a7f1` |
| Frozen case summary | `main` | `5421bf1bf2082e2ba66ce045f804f1d02b77fd58` |
| Frozen run metadata | `main` | `3cbbabd9d9446958e5a0b386f13bd32aec817fa1` |
| Frozen metrics artifact | `main` | `bc3b34cae7d8832426e6b2b56cb3d2d1541cdd57` |
| Gate C microaudit | `main` | `098bc50f382a54c9dca7025d0e2d4364ac27ad3b` |
| Limitation stratified metrics | `main` | `3e13cd52e8fac58bf4452c1c83a1fb11e233508b` |
| Historical Gate C test | `ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97` | `1d3e45c19b29ce7f1a38a4721f01b7e70d270e3c` |
| Historical hierarchical runner | `ce239059d748a4baf8a2113df5398f50c0e14a58` | `aadbec6bdc5c152def0a7e925d2cf30f16aa4c7d` |
| Current v0.3 producer | `main` | `3fb1346dcee357d7b1d2d430e3ca98c0bba1d1a0` |

```text
source_bindings_verified_from_git = true
```

## 6. Prohibiciones y aislamiento

```text
main_modified = false
candidate_integrated = false
historical_artifacts_mutated = false
v03_artifacts_mutated = false
v03_producer_modified = false
existing_tests_modified = false
v04_code_built = false
v04_gate_built = false
v04_authorization_created = false
attempt05_authorized = false
attempt05_executed = false
retrieval_executed = false
indexes_built = false
ev03_executed = false
ev04_real_executed = false
d1a_executed = false
eval_real_executed = false
model_inference_executed = false
canonical_plan_modified = false
article_modified = false
exp11b_or_exp12_touched = false
tolerances_introduced = false
convenience_rounding_introduced = false
nextafter_introduced = false
producer_output_scalars_hardcoded = false
```

## 7. Persistencia administrativa

```text
administrative_branch = codex/prompts-temporary
administrative_path = codex_prompts_tmp/30_RESPUESTA_DECISION_METODOLOGICA_PROSPECTIVA_MRR100_DOT77_DOT78.md
administrative_scope = RESPONSE_ONLY
administrative_commit = THIS_COMMIT / HEAD QUE AGREGA EXCLUSIVAMENTE ESTE ARCHIVO
scientific_and_administrative_history_mixed = false
```

## 8. Estado cientifico final

```text
GROUP_2 = EN_CURSO
0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED
0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04
EV04_GATEC_MRR100_ARITHMETIC_PROVENANCE_AUDIT = VERSIONED / INTEGRATED
METHODOLOGICAL_DECISION_CANDIDATE = BUILT / PENDING_EXTERNAL_AUDIT
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
V04_BUILD = NOT_AUTHORIZED / NOT_BUILT
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```
