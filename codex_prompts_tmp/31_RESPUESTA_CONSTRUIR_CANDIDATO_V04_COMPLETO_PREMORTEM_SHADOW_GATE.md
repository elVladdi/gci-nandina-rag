# RESPUESTA PROMPT31 - CANDIDATO 0B-05C v0.4

## 1. Baseline y referencias protegidas

```makefile
scientific_baseline = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
origin/main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
rejected_prompt30_candidate = 0298a6a51181ba992e981063be87a9742ba266ef
methodological_decision_blob = 26b4310979e042bc7bb4fa0594d1ef450bf0032e
protected_refs_modified = false
```

La decision metodologica vinculada es
`outputs/audits/0b05c_ev04_mrr_methodological_decision_v0.4/mrr_methodological_decision_v0.4.json`.
Los 26 inputs obligatorios fueron leidos integramente antes de codificar. El gate
congela 41 bindings de codigo, datos y outputs historicos en su ledger; el modelo
local mantiene SHA-256 `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`
y longitud `470637416`, sin lectura de inferencia ni modificacion.

## 2. Pre-mortem de 20 invariantes

Resultado: `20/20 PASS`; no se encontro `NEW_BLOCKING_INVARIANT`.

1. `MRR100_PROSPECTIVE_RATIONAL = PASS`
2. `MRR200_LEGACY = PASS`
3. `CONTRIBUTION_101_200_RATIONAL = PASS`
4. `CANONICAL_METRIC_DICT = PASS`
5. `NO_LEGACY_DRIFT = PASS`
6. `RANKING_AND_CASE_SUMMARY_EXACT = PASS`
7. `INDEPENDENT_EXACT_COMPARATOR = PASS`
8. `EV03_UNCHANGED = PASS`
9. `D1A_UNCHANGED = PASS`
10. `NINETEEN_STEP_ORCHESTRATION = PASS`
11. `AUTHORIZATION_BOUNDARY = PASS`
12. `SIDE_EFFECT_BOUNDARY = PASS`
13. `FUTURE_ROOT_ISOLATION = PASS`
14. `HISTORICAL_IMMUTABILITY = PASS`
15. `NO_ORACLE_LEAKAGE = PASS`
16. `NO_TOLERANCE = PASS`
17. `CROSS_FIELD_ALIASES = PASS`
18. `ROW_ORDER_SEMANTICS = PASS`
19. `SCHEMA_BLAST_RADIUS = PASS`
20. `GOVERNANCE_BLAST_RADIUS = PASS`

La matriz, evidencia y blast radius quedaron persistidos en
`outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json`.

## 3. Identidad Git del candidato

```makefile
branch = codex/0b05c-v04-complete-preexecution-candidate
candidate_commit = 69a05710295556e365086c52f93933c5b3a2ad1c
candidate_tree = 67afbbe4be85d1c4844fb06de7bbed3e5bf33263
parent = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
merge_base = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9
commits_ahead = 1
commits_behind = 0
origin_candidate = 69a05710295556e365086c52f93933c5b3a2ad1c
single_scientific_commit = true
working_tree_clean = true
```

La correccion nominal final `v02_partial_roots` -> `v03_partial_roots` estaba
staged junto con tres bindings regenerados. Como el commit inicial aun no habia
sido publicado, se consolido mediante amend local en el unico commit cientifico
final. No se reescribio historia remota ni protegida.

## 4. Changed paths y Git blob SHA-1

Los 12 paths son nuevos; no se modifico ningun archivo historico ni v0.3.

```text
21e13dd1cefe6cf428413b2ba056b822f28c9807  outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_execution_gate_v0.4.json
8a44890b2c2ee46977b4d11e9b1e3af7d92a3ea1  outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_hash_ledger_v0.4.json
6096f95a1269a4867b8dc8d2dad10bbdfd00cba0  outputs/audits/0b05c_corrective_numerical_gate_v0.4/0b05c_corrective_numerical_gate_manifest_v0.4.json
43d34d2880b9a21bbc96496ac3f5fd2d107f138e  outputs/audits/0b05c_corrective_numerical_gate_v0.4/d1a_numerical_execution_spec_v0.4.json
4a677985767e261b621b8c7b2f29edc176320fca  outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev03_numerical_execution_spec_v0.4.json
b19f479c1be4326c198708434c3bee8fbe86e787  outputs/audits/0b05c_corrective_numerical_gate_v0.4/ev04_numerical_execution_spec_v0.4.json
8c1586b06a90f4931d546c268552b4dbc84629b4  outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json
57b88a3da6b0b61918e4a20398d20ab7a26cb06e  src/experiments/evaluate_normative_bm25_corrective_0b05c_v04.py
d157f87fe65a914545e9ce1a9e2441bf486aad7c  src/experiments/prepare_0b05c_corrective_numerical_gate_v04.py
a4bfa108e70f8d8f00d0c044d57617ea4de4c18c  src/experiments/run_0b05c_corrective_numerical_v04.py
c7792907014bd1fefa7ac069a2e35eee387fe718  tests/test_0b05c_corrective_numerical_gate_v04.py
88cea0f3ad4b0624d788f5290f9ec4c432157a20  tests/test_0b05c_ev04_mrr_contract_v04.py
```

`git diff --check ba4bd293... HEAD = PASS`; diff total: 12 archivos,
4311 inserciones, 0 eliminaciones.

## 5. Arquitectura v0.4

- Evaluador v0.4: productor canonico puro para MRR@100, MRR@200 legacy y
  contribucion 101-200; comparator exacto de ranking, case summary y dict completo.
- Preparador v0.4: genera seis artefactos estaticos, congela dependencias y
  rechaza cualquier root prospectivo existente o estado autorizado.
- Runner v0.4: conserva el orden formal de 19 pasos y bloquea
  `preflight_authorized()` antes de operaciones/escrituras con el gate actual.
- EV03: reutiliza `build_bm25_corrective_0b05c_v03.py` y el recovery v0.2 sin
  cambio cientifico.
- D1a: reutiliza `run_d1a_corrective_0b05c_v03.py`; no se creo wrapper v0.4.
- No se modificaron builder, runner, specs, outputs ni tests historicos v0.3.

## 6. Canonical metrics dict v0.4

El builder parte de `hierarchical.metrics_from_cases(case_rows)` y conserva sus
83 claves legacy: 26 valores metricos en el orden legacy, sus pares
`*_numerator`/`*_denominator`, `cases_evaluated`, `cases_with_retrieval`,
`zero_retrieval_cases`, `not_found_at_depth` y `metric_table`.

Agrega nueve claves prospectivas, para 92 claves totales:

```text
mrr_at_100
mrr_at_200
mrr_at_100_numerator
mrr_at_200_numerator
mrr_at_100_denominator
mrr_at_200_denominator
mrr_definition
mrr_101_200_contribution_numerator
mrr_101_200_contribution
```

El `metric_table` tiene 27 filas, cada una exactamente con
`metric,numerator,denominator,value`; empieza por `mrr_at_100`, `mrr_at_200` y
continua con las 25 filas legacy posteriores a `mrr`.

- MRR@100: `S100 = sum(Fraction(1, rank_ref))` para `1 <= rank_ref <= 100`;
  numerador `float(S100)` y valor `float(S100/N)`, sin acumulacion float.
- MRR@200: `sum(float(reciprocal_rank))` en orden del case summary; `mrr_at_200`,
  numerador y denominador son aliases exactos, en valor y tipo, de `mrr` legacy.
- Contribucion: `C101_200 = S200-S100` racional; salidas `float(C101_200)` y
  `float(C101_200/N)`.
- Expected y actual se construyen mediante llamadas independientes; se comparan
  key order, tipos, schema, metric-table order y valores por igualdad exacta.
- No hay `isclose`, tolerancias, redondeo de conveniencia, `nextafter`, escalares
  output hardcoded en produccion ni uso del `.77` historico como oracle.

## 7. Shadow A-F

```makefile
Shadow_A = PASS
N = 1056
mrr_at_100 = 0.04198129438896378
mrr_at_100_hex = 0x1.57e927ce3818cp-5
mrr_at_100_numerator = 44.33224687474575
mrr_at_200 = 0.04334161160288281
mrr_at_200_hex = 0x1.630df28c7d779p-5
mrr_at_200_numerator = 45.76874185264425
contribution_101_200 = 0.0013603172139190346
contribution_101_200_hex = 0x1.649957c8abdbep-10
contribution_101_200_numerator = 1.4364949778985006

Shadow_B = PASS / independent objects and calls compare exactly
Shadow_C = PASS_EXACT / frozen ranking + frozen case summary + canonical metrics
Shadow_D = PASS / all eight mutations rejected
Shadow_E = PASS / no historical-oracle leakage in producer
Shadow_F = PASS / rational fields order invariant; MRR200 keeps legacy row-order contract
```

La unica diferencia conocida es prospectiva y explicada: Gate C conserva
MRR@100 `.77` como procedencia inmutable; v0.4 deriva `.78` racionalmente. Todos
los campos legacy estables coinciden con el contrato frozen.

## 8. Negative controls

Todos produjeron `ContractViolation`/fail-closed:

```makefile
mrr_at_100_one_ulp = FAIL_CLOSED
mrr_at_200_alias_mismatch = FAIL_CLOSED
contribution_one_ulp = FAIL_CLOSED
missing_key = FAIL_CLOSED
extra_key = FAIL_CLOSED
metric_table_order_or_schema = FAIL_CLOSED
ranking_changed = FAIL_CLOSED
case_summary_changed = FAIL_CLOSED
preflight_authorized_before_side_effect = FAIL_CLOSED
```

## 9. Gate, specs y future roots

```makefile
gate_status = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED
authorization_readiness = NOT_AUTHORIZED
EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED
EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED
D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED
UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED
attempt05 = NOT_AUTHORIZED / NOT_EXECUTED
authorization_record_v0.4_present = false
runtime_output_roots_created = false
```

Los 16 roots nuevos y ausentes son:

```text
data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.4
outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.4
data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.4.jsonl
data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.4
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.4
data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.4
outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.4
data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.4.jsonl
data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.4
outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.4
data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.4.jsonl
data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.4
outputs/evaluation/d1a_corrective_0b05c_v0.4
outputs/audits/d1a_corrective_0b05c_runtime_v0.4
outputs/evaluation/0b05c_corrective_numerical_v0.4
outputs/audits/0b05c_corrective_numerical_runtime_v0.4
```

## 10. Tests locales

Clasificacion probatoria de todas las ejecuciones:
`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

```text
python -B -m unittest tests.test_0b05c_ev04_mrr_contract_v04 tests.test_0b05c_corrective_numerical_gate_v04
29/29 PASS

python -B -m unittest tests.test_0b05c_corrective_numerical_gate_v03
26/26 PASS en baseline historico preautorizacion 8b1444aed67d322714189846f98a3169145ea3d4

python -B -m unittest tests.test_0b05c_ev03_historical_builder_recovery_v02
15 PASS / 1 SKIP

python -B -m unittest tests.test_0b05c_corrective_numerical_gate_v02
56/56 PASS en baseline historico preautorizacion c44f447cb941c512cd70712cf7c3e4bc670ab05a

python -B -m unittest tests.test_0b05c_corrective_numerical_gate_v01 tests.test_0b05c_f003_microclose_v01 tests.test_0b05c_f003_residual_v01
49/49 PASS en baseline historico preautorizacion 0e074db638f6b7163d98d34f08f76e1efde07b7f

python -B -m src.experiments.prepare_0b05c_corrective_numerical_gate_v04 --preflight
PASS / PREEXECUTION_CLOSED_READONLY

python -B -m unittest tests.test_0b05c_corrective_numerical_gate_v04
11/11 PASS despues de la correccion nominal final
```

Las primeras ejecuciones directas de las suites v0.3/v0.2 sobre `main` actual
mostraron, respectivamente, `7 failures + 1 error` y `4 failures + 2 errors`
porque esas suites historicas exigen artefactos candidatos cerrados mientras
sus artefactos actuales registran autorizaciones consumidas. No son regresiones
del codigo v0.4. Se repitieron de forma read-only en sus baselines frozen
preautorizacion, donde pasaron completas. No se modifico ninguna suite historica.

No se ejecuto la suite total porque Prompt31 permite omitir pruebas costosas y
los contratos directamente afectados quedaron cubiertos por las suites listadas.

## 11. No ejecucion y estado cientifico

```makefile
retrieval_executed = false
EV03_real_executed = false
EV04_real_executed = false
D1a_executed = false
EVAL_real_executed = false
model_inference_executed = false
Attempt05_executed = false
corrective_metrics_computed = false
historical_outputs_modified = false
Plan_Maestro_modified = false
article_modified = false
EXP11B_modified = false
EXP12_modified = false

V04_CANDIDATE = BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
V04_GATE = DEFINED / UNAUTHORIZED
V04_AUTHORIZATION = NOT_CREATED
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

`BLOCKERS = NONE_FOR_EXTERNAL_AUDIT`.
