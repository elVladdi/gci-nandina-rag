# CODEX — DIAGNÓSTICO ESTÁTICO DEL MISMATCH DE MÉTRICAS EV04 / ATTEMPT04

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE DIAGNÓSTICO ESTÁTICO FORENSE** del fallo EV04 observado en Attempt04.

El microcierre de Attempt04 ya está integrado en `main`. Este bloque debe identificar, usando **solo artefactos versionados y cálculos puros/read-only**, si el productor v0.3 de métricas EV04 reproduce exactamente el diccionario de métricas congelado que consume el control Decision885 y, si no lo reproduce, aislar **todos los campos exactos** que difieren y el mecanismo aritmético/estructural que los causa.

NO ejecutes retrieval.
NO construyas índices.
NO ejecutes `evaluate_arm()`.
NO ejecutes EV03, EV04, D1a, EVAL real ni inferencia del modelo.
NO uses outputs parciales locales de Attempt04 como fuente científica.
NO construyas v0.4.
NO modifiques código, tests, gate, specs, authorization record ni failure record.
NO autorices Attempt05.
NO interpretes impacto D906.
NO actualices Plan ni article.

---

## 1. BASELINE GIT OBLIGATORIO

Haz fetch y verifica exactamente:

- `origin/main = 58ecf012d7c4ed609c3b10787fb583f69700ab02`;
- parent de main = `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- failure record integrado:
  `outputs/audits/0b05c_attempt04_failclosed_v0.3/attempt04_failure_record_v0.3.json`;
- failure record blob = `31f1cea387b8630191371f767c03cf13990646b0`;
- failure record: `root_cause_field_status = NOT_YET_ISOLATED`;
- gate readiness = `ATTEMPT04_CONSUMED / REAUTHORIZATION_REQUIRED`;
- Attempt05 = no autorizado.

Verifica además las siguientes identidades Git versionadas:

- evaluator v0.3:
  `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`
  blob `3fb1346dcee357d7b1d2d430e3ca98c0bba1d1a0`;
- comparator legacy:
  `src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py`
  blob `c6f4121fe5f5f50e71e27eb4cf1e28eb8986d062`;
- frozen EV04 run metadata:
  `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json`
  blob `3cbbabd9d9446958e5a0b386f13bd32aec817fa1`;
- frozen EV04 case summary:
  `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv`
  blob `5421bf1bf2082e2ba66ce045f804f1d02b77fd58`;
- frozen EV04 metrics artifact:
  `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json`
  blob `bc3b34cae7d8832426e6b2b56cb3d2d1541cdd57`.

Si cualquier identidad difiere: STOP / NO DIAGNÓSTICO.

---

## 2. FUENTES DE VERDAD DEL DIAGNÓSTICO

La fuente **exacta** que usa el runner v0.3 como `expected_metrics` para EV04 es:

`run_metadata.json["metrics"]`.

No sustituyas esa fuente por otra.

Usa `normative_hierarchical_metrics.json["metrics"]` únicamente como control secundario para comprobar si ambos artefactos históricos contienen el mismo diccionario de métricas.

La reconstrucción estática debe partir exclusivamente del **case summary congelado versionado**, no de outputs locales de Attempt04.

---

## 3. RECONSTRUCCIÓN PURA DEL PRODUCTOR v0.3

Puedes ejecutar Python local únicamente para cálculos read-only sobre archivos versionados. No escribas outputs experimentales ni invoques runners/evaluadores que hagan retrieval.

Carga las 1056 filas de:

`normative_hierarchical_case_summary.csv`

con la misma semántica de lectura del runner jerárquico (`hierarchical.read_csv` o una lectura equivalente que preserve los valores).

Reconstruye exactamente la ruta pura que pretende usar v0.3:

1. `base_metrics = hierarchical.metrics_from_cases(case_rows)`;
2. `reconstructed_v03 = build_ev04_enriched_metrics(case_rows, base_metrics, require_real_case_count=True)`.

No llames `evaluate_arm()`.

Verifica y reporta:

- N = 1056;
- nombres y número de keys top-level del esperado y reconstruido;
- keys faltantes/extra;
- igualdad exacta Python `expected_metrics == reconstructed_v03`;
- igualdad exacta de `metric_table`;
- igualdad exacta de nombres/orden/schema del `metric_table`.

---

## 4. DEEP DIFF OBLIGATORIO

Construye un deep diff determinista entre:

`expected = run_metadata["metrics"]`

y

`observed = reconstructed_v03`.

Debes reportar **todos** los mismatches, no solo el primero.

Para cada mismatch registra como mínimo:

- `json_path`;
- `expected_type`;
- `observed_type`;
- `expected_repr`;
- `observed_repr`;
- `equal_python`;
- si ambos son numéricos: `absolute_delta`.

Para floats añade obligatoriamente:

- `expected_float_hex = float(expected).hex()`;
- `observed_float_hex = float(observed).hex()`;
- ULP distance si puedes calcularla de forma determinista; si no, `NOT_COMPUTED`.

También distingue:

- top-level scalar mismatch;
- `metric_table[i].field` mismatch;
- key missing/extra;
- type-only mismatch.

No uses tolerancias: este diagnóstico es de igualdad exacta.

---

## 5. CONTROL HISTÓRICO SECUNDARIO

Compara exactamente:

`run_metadata.json["metrics"]`

contra

`normative_hierarchical_metrics.json["metrics"]`.

Reporta:

- igualdad exacta;
- mismatch count y paths si no son iguales.

Si divergen, recuerda que **el runner v0.3 usa `run_metadata["metrics"]` como expected**.

---

## 6. MICROAUDITORÍA ARITMÉTICA MRR

Independientemente de dónde aparezca el mismatch, calcula desde el case summary congelado y registra con `repr()` y `float.hex()`:

### MRR@100

- `sum(1.0 / rank_ref for 1 <= rank_ref <= 100)`;
- `sum(float(reciprocal_rank) for rows with 1 <= rank_ref <= 100)`;
- `math.fsum(1.0 / rank_ref ...)`;
- `math.fsum(float(reciprocal_rank) ...)`;
- cada numerador / 1056.

### MRR@200

Mismas cuatro variantes para `1 <= rank_ref <= 200`.

### Contribución 101–200

Para cada ruta aritmética coherente calcula:

- numerator200 - numerator100;
- `(numerator200 - numerator100) / 1056`.

Compara bit-a-bit/igualdad Python contra los valores congelados:

- `mrr_at_100_numerator`;
- `mrr_at_100`;
- `mrr_at_200_numerator`;
- `mrr_at_200`;
- `mrr_numerator`;
- `mrr`;
- `mrr_101_200_contribution_numerator`;
- `mrr_101_200_contribution`;
- filas `metric_table` de `mrr_at_100` y `mrr_at_200`.

El objetivo es identificar si existe un problema de **orden/forma de suma, redondeo IEEE-754, fuente reciprocal_rank vs rank_ref, schema, key o tipo**, sin inferirlo de antemano.

---

## 7. REPRODUCIR ESTÁTICAMENTE LA CONDICIÓN DEL COMPARATOR

Sin retrieval y sin generar outputs nuevos, ejecuta una prueba read-only del comparator usando:

- frozen ranking como expected y actual del ranking;
- frozen case summary como expected y actual del case summary;
- `run_metadata["metrics"]` como expected metrics;
- `reconstructed_v03` como actual metrics;
- schemas EV04 congelados.

Esto debe aislar el factor métricas: ranking/case summary se suministran idénticos por construcción.

Reporta:

- si `compare_control_reproduction()` devuelve PASS o lanza `Mandatory control reproduction is not exact`;
- `metrics_exact` calculado antes de la llamada;
- no atribuyas a runtime lo que solo se demuestra estáticamente.

---

## 8. CLASIFICACIÓN CAUSAL

Solo si el deep diff reproduce una divergencia determinista desde artefactos versionados, clasifica:

`ROOT_CAUSE_FIELD_STATUS = ISOLATED_FROM_VERSIONED_FROZEN_ARTIFACTS`

y enumera **todos** los `root_cause_json_paths`.

Además establece una `root_cause_class` descriptiva y precisa, por ejemplo:

- `FLOAT_ACCUMULATION_PATH_MISMATCH`;
- `METRIC_SCHEMA_MISMATCH`;
- `TOP_LEVEL_KEY_MISMATCH`;
- `METRIC_TABLE_VALUE_MISMATCH`;
- u otra clasificación sustentada por el diff.

No uses una de esas etiquetas si los datos no la justifican.

Si `expected_metrics == reconstructed_v03`, clasifica exactamente:

`ROOT_CAUSE_FIELD_STATUS = STATIC_RECONSTRUCTION_DOES_NOT_REPRODUCE_RUNTIME_FAILURE`

y **no inventes** un campo culpable. En ese caso el siguiente paso tendrá que ser otro diseño de diagnóstico, todavía sin Attempt05.

---

## 9. ARTEFACTO CIENTÍFICO DIAGNÓSTICO

Crea desde exactamente `58ecf012d7c4ed609c3b10787fb583f69700ab02` la rama:

`codex/0b05c-ev04-attempt04-static-metric-diagnosis-v03`

Crea **un solo archivo científico nuevo**:

`outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json`

No modifiques ningún archivo existente.

El JSON debe incluir como mínimo:

- `artifact_id = 0b05c_ev04_attempt04_metric_mismatch_diagnosis_v0.3`;
- `schema_version = 1`;
- `baseline_commit = 58ecf012...`;
- bindings Git de todas las fuentes de sección 1;
- `evidence_scope = VERSIONED_FROZEN_ARTIFACTS_AND_PURE_READ_ONLY_COMPUTATION`;
- `attempt04_runtime_outputs_used = false`;
- `retrieval_executed = false`;
- `evaluation_runner_executed = false`;
- `model_inference_executed = false`;
- igualdad run_metadata metrics vs metrics artifact;
- igualdad expected vs reconstructed v0.3;
- deep diff completo;
- microauditoría MRR completa;
- resultado del comparator estático;
- `root_cause_field_status`;
- `root_cause_json_paths`;
- `root_cause_class`;
- `attempt05_authorized = false`;
- `metric_impact = NOT_DETERMINED`;
- `closure = NOT_AUTHORIZED`.

Serializa UTF-8, LF, JSON determinista/ordenado. No incluyas timestamps no deterministas si no son necesarios.

---

## 10. VALIDACIÓN Y COMMIT

Antes de commit:

- diff científico = exactamente 1 archivo nuevo;
- ningún código/test/gate/spec/failure record/authorization record cambió;
- Plan/article intactos;
- EXP11B/EXP12 intactos;
- Attempt05 no autorizado;
- no hay outputs experimentales nuevos.

Crea exactamente un commit científico candidato con mensaje sugerido:

`docs: diagnose Attempt04 EV04 metric mismatch from frozen artifacts`

Push únicamente a:

`codex/0b05c-ev04-attempt04-static-metric-diagnosis-v03`

No merge a main.

Reporta SHA, parent, tree, changed path count (=1), blob del diagnóstico y compare base→candidato.

---

## 11. PERSISTENCIA ADMINISTRATIVA

Después del push científico, persiste únicamente:

`codex_prompts_tmp/26_RESPUESTA_DIAGNOSTICO_ESTATICO_MISMATCH_METRICAS_EV04_ATTEMPT04.md`

en `codex/prompts-temporary` con un commit response-only.

No modifiques este Prompt26 ni respuestas anteriores.
No mezcles rama administrativa con `main`.

---

## 12. REPORTE FINAL

Usa exactamente estas secciones:

### A. Baseline Git y fuentes
### B. Reconstrucción pura v0.3
### C. Deep diff completo
### D. Control histórico secundario
### E. Microauditoría aritmética MRR
### F. Comparator estático
### G. Clasificación causal
### H. Aislamiento y prohibiciones
### I. Commit científico candidato
### J. Persistencia administrativa
### K. Estado científico

Termina con:

`GROUP_2 = EN_CURSO`

`0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED`

`0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04`

`EV04_ATTEMPT04_ROOT_CAUSE_FIELD = <resultado exacto del diagnóstico>`

`ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
