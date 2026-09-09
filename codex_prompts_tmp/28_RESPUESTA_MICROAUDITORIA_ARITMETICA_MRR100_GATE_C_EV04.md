# Respuesta Prompt28 - Microauditoria aritmetica MRR@100 de Gate C / EV04

## A. Preflight Git

```text
repository = elVladdi/gci-nandina-rag
scientific_base_main = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
origin_main = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
canonical_plan = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
scientific_branch = codex/0b05c-ev04-mrr100-arithmetic-provenance-v03
scientific_parent = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
attempt05 = NOT_AUTHORIZED / NOT_EXECUTED
case_count = 1056
source_bindings_all_match_expected = true
```

Bindings Git verificados:

| Fuente | Ref | Blob SHA1 |
|---|---|---|
| Diagnostico estatico Attempt04 | `HEAD` | `fca5712c615960b41cb2741c2164f19fc00df9dd` |
| `run_metadata.json` congelado | `HEAD` | `3cbbabd9d9446958e5a0b386f13bd32aec817fa1` |
| `normative_hierarchical_case_summary.csv` | `HEAD` | `5421bf1bf2082e2ba66ce045f804f1d02b77fd58` |
| `normative_hierarchical_metrics.json` | `HEAD` | `bc3b34cae7d8832426e6b2b56cb3d2d1541cdd57` |
| `gate_c_microaudit_v0.2.json` | `HEAD` | `098bc50f382a54c9dca7025d0e2d4364ac27ad3b` |
| `gate_c_microaudit_v0.2.md` | `HEAD` | `2749d3328a0f72c43e0f69a89d36293a7b86f042` |
| `limitation_stratified_metrics_v0.2.csv` | `HEAD` | `3e13cd52e8fac58bf4452c1c83a1fb11e233508b` |
| Test historico Gate C | `ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97` | `1d3e45c19b29ce7f1a38a4721f01b7e70d270e3c` |
| Productor v0.3 actual | `HEAD` | `3fb1346dcee357d7b1d2d430e3ca98c0bba1d1a0` |
| Runner jerarquico historico | `ce239059d748a4baf8a2113df5398f50c0e14a58` | `aadbec6bdc5c152def0a7e925d2cf30f16aa4c7d` |
| Inventario Gate C | `HEAD` | `adcd8da4b3f6c48d84535a0068cdd83d5bf7806a` |
| Comparacion flat Gate C | `HEAD` | `e1c34db96121f88f05d3371e41256cd470626a4f` |
| Summary Gate C | `HEAD` | `dac91901821349ace513468fc8db5de88e68f1c3` |
| Metadata padre Gate C | `13d317630bbe59e91bc1058800d4593ba6ace66a` | `305ad5c29d2a37b584c5f892cc5ac4a0c8a70e17` |

## B. Evidencia historica Gate C

```text
gate_c_commit = ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97
gate_c_parent = 13d317630bbe59e91bc1058800d4593ba6ace66a
initial_outputs_commit = 001580944b417e81634dd6d11a9d2facc9ed29be
historical_runner_commit = ce239059d748a4baf8a2113df5398f50c0e14a58
gate_c_changed_path_count = 10
gate_c_changed_producer_code = false
parent_run_metadata_contains_mrr_at_100 = false
```

El diff completo de Gate C agrega o modifica diez paths documentales, de outputs y del test, pero ningun productor. `gate_c_microaudit_v0.2.json` declara `source_artifacts_only` y cita el case summary como fuente de MRR, sin congelar el reductor ni un script ejecutable de microauditoria.

El test historico lee con `csv.DictReader`, reconstruye `reciprocal_sum_100` mediante Python `sum((1 / int(row["rank_ref"])) ...)` en orden CSV, y compara MRR@100 con `assertAlmostEqual`. No exige igualdad bit-exacta. El runner historico aporta evidencia de Python `sum(float(reciprocal_rank))` para el MRR@200 legado, pero no vincula los bits `.77` de MRR@100 con una ejecucion identificable.

## C. Inconsistencia versionada `.77` / `.78`

```text
Gate C frozen numerator = 44.33224687474574 = 0x1.62a8710ca9d97p+5
Gate C frozen MRR@100 = 0.04198129438896377 = 0x1.57e927ce3818bp-5
stratified parent_hs4_present, N=1056 = 0.04198129438896378 = 0x1.57e927ce3818cp-5
stratified not_both_parents_missing, N=1056 = 0.04198129438896378 = 0x1.57e927ce3818cp-5
coexistence_ulp_distance = 1
```

Ambos valores coexisten en artefactos versionados. Se preservan como una senal de auditoria; no se declara uno correcto y el otro incorrecto, ni se normaliza retrospectivamente ningun resultado.

## D. Matriz completa de rutas aritmeticas

Entorno historico documentado: Python `3.12.13`, NumPy `2.3.5`, pandas `3.0.1`, Windows 11. Entorno ejecutado: CPython `3.12.14`, NumPy `2.3.5`, pandas `3.0.1`, `Windows-11-10.0.26200-SP0`. La diferencia de patch de Python impide atribuir provenance historica a partir de una coincidencia local por si sola.

Todas las rutas usaron `csv.DictReader` con `utf-8-sig`, conversion posterior a `float` y el orden natural congelado del CSV. `filtered_nonzero` conserva ese orden tras filtrar; `full_zero` conserva sus 1056 posiciones. Bibliotecas: `PY=Python 3.12.14`, `NP=NumPy 2.3.5`, `PD=pandas 3.0.1`.

Resultados numericos observados, usados en la columna `Resultado`:

```text
M100-A:
  numerator repr=44.33224687474575 hex=0x1.62a8710ca9d98p+5 equal=false ULP=1 delta=7.105427357601002e-15
  value     repr=0.04198129438896378 hex=0x1.57e927ce3818cp-5 equal=false ULP=1 delta=6.938893903907228e-18

M200-A:
  numerator repr=45.76874185264425 hex=0x1.6e266220e1635p+5 equal=true ULP=0 delta=0
  value     repr=0.04334161160288281 hex=0x1.630df28c7d779p-5 equal=true ULP=0 delta=0

M200-B:
  numerator repr=45.768741852644254 hex=0x1.6e266220e1636p+5 equal=false ULP=1 delta=7.105427357601002e-15
  value     repr=0.043341611602882815 hex=0x1.630df28c7d77ap-5 equal=false ULP=1 delta=6.938893903907228e-18
```

Las 48 rutas probadas son:

| Ruta exacta | Lib | Longitud | Resultado |
|---|---:|---:|---:|
| `mrr_at_100.rank_ref.filtered_nonzero.python_builtin_sum` | PY | 107 | M100-A |
| `mrr_at_100.rank_ref.filtered_nonzero.math_fsum` | PY | 107 | M100-A |
| `mrr_at_100.rank_ref.filtered_nonzero.numpy_sum_float64` | NP | 107 | M100-A |
| `mrr_at_100.rank_ref.filtered_nonzero.numpy_add_reduce_float64` | NP | 107 | M100-A |
| `mrr_at_100.rank_ref.filtered_nonzero.pandas_series_sum_float64` | PD | 107 | M100-A |
| `mrr_at_100.rank_ref.full_zero.python_builtin_sum` | PY | 1056 | M100-A |
| `mrr_at_100.rank_ref.full_zero.math_fsum` | PY | 1056 | M100-A |
| `mrr_at_100.rank_ref.full_zero.numpy_sum_float64` | NP | 1056 | M100-A |
| `mrr_at_100.rank_ref.full_zero.numpy_add_reduce_float64` | NP | 1056 | M100-A |
| `mrr_at_100.rank_ref.full_zero.pandas_series_sum_float64` | PD | 1056 | M100-A |
| `mrr_at_100.rank_ref.full_zero.numpy_mean_float64` | NP | 1056 | M100-A |
| `mrr_at_100.rank_ref.full_zero.pandas_series_mean_float64` | PD | 1056 | M100-A |
| `mrr_at_100.reciprocal_rank.filtered_nonzero.python_builtin_sum` | PY | 107 | M100-A |
| `mrr_at_100.reciprocal_rank.filtered_nonzero.math_fsum` | PY | 107 | M100-A |
| `mrr_at_100.reciprocal_rank.filtered_nonzero.numpy_sum_float64` | NP | 107 | M100-A |
| `mrr_at_100.reciprocal_rank.filtered_nonzero.numpy_add_reduce_float64` | NP | 107 | M100-A |
| `mrr_at_100.reciprocal_rank.filtered_nonzero.pandas_series_sum_float64` | PD | 107 | M100-A |
| `mrr_at_100.reciprocal_rank.full_zero.python_builtin_sum` | PY | 1056 | M100-A |
| `mrr_at_100.reciprocal_rank.full_zero.math_fsum` | PY | 1056 | M100-A |
| `mrr_at_100.reciprocal_rank.full_zero.numpy_sum_float64` | NP | 1056 | M100-A |
| `mrr_at_100.reciprocal_rank.full_zero.numpy_add_reduce_float64` | NP | 1056 | M100-A |
| `mrr_at_100.reciprocal_rank.full_zero.pandas_series_sum_float64` | PD | 1056 | M100-A |
| `mrr_at_100.reciprocal_rank.full_zero.numpy_mean_float64` | NP | 1056 | M100-A |
| `mrr_at_100.reciprocal_rank.full_zero.pandas_series_mean_float64` | PD | 1056 | M100-A |
| `mrr_at_200.rank_ref.filtered_nonzero.python_builtin_sum` | PY | 321 | M200-A |
| `mrr_at_200.rank_ref.filtered_nonzero.math_fsum` | PY | 321 | M200-A |
| `mrr_at_200.rank_ref.filtered_nonzero.numpy_sum_float64` | NP | 321 | M200-B |
| `mrr_at_200.rank_ref.filtered_nonzero.numpy_add_reduce_float64` | NP | 321 | M200-B |
| `mrr_at_200.rank_ref.filtered_nonzero.pandas_series_sum_float64` | PD | 321 | M200-B |
| `mrr_at_200.rank_ref.full_zero.python_builtin_sum` | PY | 1056 | M200-A |
| `mrr_at_200.rank_ref.full_zero.math_fsum` | PY | 1056 | M200-A |
| `mrr_at_200.rank_ref.full_zero.numpy_sum_float64` | NP | 1056 | M200-B |
| `mrr_at_200.rank_ref.full_zero.numpy_add_reduce_float64` | NP | 1056 | M200-B |
| `mrr_at_200.rank_ref.full_zero.pandas_series_sum_float64` | PD | 1056 | M200-B |
| `mrr_at_200.rank_ref.full_zero.numpy_mean_float64` | NP | 1056 | M200-B |
| `mrr_at_200.rank_ref.full_zero.pandas_series_mean_float64` | PD | 1056 | M200-B |
| `mrr_at_200.reciprocal_rank.filtered_nonzero.python_builtin_sum` | PY | 321 | M200-A |
| `mrr_at_200.reciprocal_rank.filtered_nonzero.math_fsum` | PY | 321 | M200-A |
| `mrr_at_200.reciprocal_rank.filtered_nonzero.numpy_sum_float64` | NP | 321 | M200-B |
| `mrr_at_200.reciprocal_rank.filtered_nonzero.numpy_add_reduce_float64` | NP | 321 | M200-B |
| `mrr_at_200.reciprocal_rank.filtered_nonzero.pandas_series_sum_float64` | PD | 321 | M200-B |
| `mrr_at_200.reciprocal_rank.full_zero.python_builtin_sum` | PY | 1056 | M200-A |
| `mrr_at_200.reciprocal_rank.full_zero.math_fsum` | PY | 1056 | M200-A |
| `mrr_at_200.reciprocal_rank.full_zero.numpy_sum_float64` | NP | 1056 | M200-B |
| `mrr_at_200.reciprocal_rank.full_zero.numpy_add_reduce_float64` | NP | 1056 | M200-B |
| `mrr_at_200.reciprocal_rank.full_zero.pandas_series_sum_float64` | PD | 1056 | M200-B |
| `mrr_at_200.reciprocal_rank.full_zero.numpy_mean_float64` | NP | 1056 | M200-B |
| `mrr_at_200.reciprocal_rank.full_zero.pandas_series_mean_float64` | PD | 1056 | M200-B |

```text
arithmetic_route_count = 48
rank_ref_vs_reciprocal_rank_source_mismatch_count = 0
mrr100_numeric_matching_routes = []
mrr200_numeric_matching_route_count = 8
numeric_matching_routes = []
```

## E. Provenance

`NUMERIC_MATCH`: ninguna de las 24 rutas MRR@100 historicamente plausibles reproduce los bits congelados. Ocho rutas MRR@200, las de `python_builtin_sum` y `math_fsum` para ambas fuentes y ambas formas de vector, reproducen numerador y valor bit-exactos.

`HISTORICAL_PROVENANCE`: ninguna ruta queda soportada para los bits congelados MRR@100. Existe evidencia positiva de que Gate C recomputo desde el case summary y de la formula Python `sum(1 / int(rank_ref))` en el test, pero esa formula produce `.78` localmente y el test solo exige proximidad. Falta un productor versionado de los campos nuevos, un reductor congelado y un registro de ejecucion que vincule `.77` con una ruta concreta.

Una coincidencia en MRR@200 no prueba la procedencia de MRR@100. No se efectuaron permutaciones, busqueda combinatoria, redondeo ni tolerancias.

## F. Clasificacion final

```text
causal_classification = HISTORICAL_ARITHMETIC_PATH_NOT_RECOVERED
```

Corresponde exactamente a la clase C: ninguna ruta historicamente plausible ensayada reproduce bit-exacto el frozen MRR@100.

## G. Readiness v0.4

```text
v04_recovery_readiness = NOT_READY_NEEDS_METHODOLOGICAL_DECISION
```

Recomendacion prospectiva:

1. Definir y versionar un unico reductor, parser, orden y precision para MRR.
2. Congelar el entorno ejecutable y registrar `repr` y `float.hex` de numerador y cociente.
3. Elegir explicitamente si `.77` se preserva como referencia historica o `.78` como recomputacion reproducible.
4. Mantener `PASS_EXACT`; no usar tolerancias, redondeo ni escalares hardcodeados.
5. Construir v0.4 solo despues de una decision metodologica externa versionada.

## H. Candidato cientifico

```text
branch = codex/0b05c-ev04-mrr100-arithmetic-provenance-v03
commit = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
parent = 6187ca29357c42c43675fb8e5ffdacbb4705ee83
tree = 401ee00fa621e2f084278ef5bf5ee5b8d7771fd2
path = outputs/audits/0b05c_ev04_gatec_mrr100_arithmetic_provenance_v0.3/ev04_gatec_mrr100_arithmetic_provenance_v0.3.json
blob_sha1 = c3667f85b4f8ec51f026e2e3b706062da586a7f1
changed_paths = 1
commit_count_over_base = 1
remote_head_matches = true
main_integrated = false
```

## I. Aislamiento

```text
git_versioned_facts = INDEPENDENTLY_REPRODUCIBLE_FROM_GIT_OBJECTS
local_arithmetic_reproduction = CODEX_LOCAL_PURE_READ_ONLY_COMPUTATION
github_ci = NO_VERSIONED_GITHUB_ACTIONS_WORKFLOW / NO_GITHUB_CI_EVIDENCE_USED
retrieval_executed = false
indexes_built = false
ev03_executed = false
ev04_real_executed = false
d1a_executed = false
eval_real_executed = false
model_inference_executed = false
v04_built = false
v04_authorization_created = false
attempt05_authorized = false
attempt05_executed = false
main_modified = false
canonical_plan_modified = false
article_modified = false
historical_artifacts_modified = false
pass_exact_weakened = false
tolerance_or_rounding_introduced = false
metric_impact = NOT_DETERMINED
closure = NOT_AUTHORIZED
```

## J. Persistencia administrativa

```text
administrative_branch = codex/prompts-temporary
administrative_path = codex_prompts_tmp/28_RESPUESTA_MICROAUDITORIA_ARITMETICA_MRR100_GATE_C_EV04.md
administrative_commit = THIS_COMMIT / HEAD QUE AGREGA EXCLUSIVAMENTE ESTE ARCHIVO
scientific_and_administrative_history_mixed = false
```

## K. Estado cientifico

```text
GROUP_2 = EN_CURSO
0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED
0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04
EV04_ATTEMPT04_STATIC_DIAGNOSIS = VERSIONED / INTEGRATED
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```
