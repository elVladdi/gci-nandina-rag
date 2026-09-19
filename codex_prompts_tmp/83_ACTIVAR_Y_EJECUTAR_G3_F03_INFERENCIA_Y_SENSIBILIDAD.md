# PROMPT 83 — ACTIVAR Y EJECUTAR EXCLUSIVAMENTE G3-F03: INFERENCIA Y ANÁLISIS DE SENSIBILIDAD

## 0. Naturaleza, autorización y límite de esta ejecución

La IA Experimental ha verificado externamente el cierre de G3-F02 y el usuario ha autorizado continuar con la siguiente ficha elegible.

Esta ejecución constituye autorización expresa **únicamente para G3-F03**.

Estado de entrada autorizado:

```text
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G3_F04 = PROSPECTIVE / NOT_AUTHORIZED
```

G3-F03 es la primera ficha de Grupo 3 que puede producir **incertidumbre inferencial**. Debe ejecutar solamente los procedimientos prospectivos congelados por G3-F01 y materializados por G3-F02.

**No decide HE2 ni HE5.** Esa decisión pertenece exclusivamente a G3-F04.

Prohibido usar las palabras/estados `SUPPORTED`, `NOT_SUPPORTED`, `INCONCLUSIVE`, `SIGNIFICANT`, `NONSIGNIFICANT` o equivalentes como decisión de hipótesis en los outputs de G3-F03.

---

## 1. Repositorio y refs científicos congelados

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar cualquier rama ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
origin/docs/plan-maestro-temporal-2026-08-31 = 12ac39ec18761bc926d196e71137de60c2a9956b
origin/docs/fichas-grupos-3-8 = d9725a6d6a0ab76ee2be07b5f93c2c978dd59d2c
```

Artículo observado al autorizar Prompt83:

```text
origin/article/main-manuscript = 45b0a5c61993178a71c7640c8051e3d7b24c0526
```

El artículo es **solo una referencia observacional** y no es input científico de G3-F03. Un avance editorial concurrente posterior no invalida esta ejecución mientras Prompt83 no modifique la rama del artículo. Registra cualquier drift editorial como advertencia, no como drift científico.

El avance de `codex/prompts-temporary` debido a la incorporación de Prompt83 también es esperado.

Si `main`, Plan Maestro o fichas presentan drift antes de la activación:

```text
STOP / SCIENTIFIC_OR_GOVERNANCE_REF_DRIFT
```

---

## 2. Fuentes rectoras obligatorias

Lee íntegramente y trata como vinculantes, en este orden:

### 2.1 Ficha G3-F03

Desde `origin/docs/fichas-grupos-3-8 = d9725a6d6a0ab76ee2be07b5f93c2c978dd59d2c`:

```text
docs/fichas/grupos_3_8/grupo_3/G3_F03_INFERENCIA_Y_SENSIBILIDAD.md
```

Blob esperado:

```text
176e03ed04fb2dbc54330905a14b896b5ccebab6
```

### 2.2 Contrato analítico G3-F01 integrado en main

Desde `origin/main = adf70d6eb880c567d6efa0f27b5c79259b8db2a6`:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

### 2.3 Registro maestro G3-F02 integrado en main

```text
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1_hash_ledger.csv
```

Blobs congelados:

```text
CSV_BLOB = c63619b56a07e6b6d7be78b515d941ec3b205c41
JSON_BLOB = 5ea33ca583b18426374fa15baf1b1759e76cd99e
HASH_LEDGER_BLOB = 521bfcdf34d03c4effa8b8ef19f9777b6827d439
```

SHA-256 congelados:

```text
CSV_SHA256 = 65294f0e81de358f8cdab4d3997d1c8fe03062f2d3e5b6a95cbca5da885c5c41
JSON_SHA256 = 673b43e9ef5ed20bc6aafa9c674e6bbdba5cdbd054dd47f40bf14d05c8d1ae7b
```

### 2.4 Registro operacional de fichas

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Debe indicar antes de activar:

```text
G3-F01 = CLOSED / APPROVED
G3-F02 = CLOSED / APPROVED
G3-F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G3-F04 = PROSPECTIVE
```

Si cualquiera de estas fuentes o estados no coincide:

```text
STOP / G3_F03_PRECONDITION_MISMATCH
```

---

## 3. Activación prospectiva obligatoria antes de calcular inferencia

Antes de leer/calcular cualquier resultado bootstrap de G3-F03, materializa la activación en la rama:

```text
docs/fichas-grupos-3-8
```

Archivo único a modificar en esta fase:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Actualiza G3-F03 a:

```text
ACTIVE / AUTHORIZED / EXECUTION_PENDING
```

Mantén:

```text
G3-F04 = PROSPECTIVE / NOT_AUTHORIZED
```

Añade un bloque de activación con, como mínimo:

```text
FICHA = G3-F03
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT83_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
ACTIVATION_DATE = 2026-09-19

MAIN_AT_ACTIVATION = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
PLAN_AT_ACTIVATION = 12ac39ec18761bc926d196e71137de60c2a9956b
FICHAS_AT_ACTIVATION = d9725a6d6a0ab76ee2be07b5f93c2c978dd59d2c
ARTICLE_HEAD_OBSERVED = 45b0a5c61993178a71c7640c8051e3d7b24c0526
PROMPT83_COMMIT = <commit exacto de este Prompt83>

G3_F01_CONTRACT = docs/analysis/group3/g3_analytical_contract_v0.1.md
G3_F02_REGISTRY = outputs/analysis/group3/g3_metric_population_registry_v0.1.csv

INFERENCE_AUTHORIZED = true
P_VALUES_AUTHORIZED = false
HE2_DECISION_AUTHORIZED = false
HE5_DECISION_AUTHORIZED = false
G3_F04_AUTHORIZED = false
```

Haz **un solo commit administrativo de activación** y push normal de la rama de fichas.

No modifiques todavía Plan Maestro.

Si no puedes materializar y publicar la activación antes del cálculo:

```text
STOP / ACTIVATION_NOT_MATERIALIZED
```

---

## 4. Revisión pre-run obligatoria de integridad

Después de la activación, pero antes del primer bootstrap:

1. Verifica blobs y SHA-256 del registro G3-F02.
2. Verifica que el registro contiene 548 filas y 16 familias de evidencia.
3. Verifica que existen exactamente 4 familias `ELIGIBLE`:

```text
HE2_A_HISTORICAL_VS_NORMATIVE_FLAT_ATTEMPT06
HE2_A_HISTORICAL_VS_NORMATIVE_HIERARCHICAL_ATTEMPT06
HE2_A_HISTORICAL_VS_D1A_ATTEMPT06
HE2_B_HIERARCHICAL_DEEP_COVERAGE_ATTEMPT06
```

4. Verifica que EVAL permanece:

```text
N_SERIES = 1056
N_DAM = 67
EVAL_SHA256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACIÓN
```

5. Para cada source/case-level source realmente usado, verifica que el path existe y que el blob Git coincide con G3-F02.
6. Verifica que no se usa el split 3000/1006.
7. Verifica que flat, hierarchical y D1a son exclusivamente los outputs corregidos de Attempt06/Decision906.
8. Verifica que los conjuntos de `case_id`/`id_unico` y etiquetas necesarios para el pareamiento coinciden exactamente.
9. Para D1a, DAM/SERIE debe recuperarse mediante el exact join congelado por `case_id`/`id_unico`; no inventes agrupamientos.
10. Antes de bootstrap, reconstruye los point estimates de los contrastes desde los case-level congelados y comprueba que coinciden con los valores/numeradores del registro G3-F02 con tolerancia numérica `<= 1e-12` cuando aplique.

Si cualquiera falla:

```text
STOP / PRE_INFERENCE_INTEGRITY_FAILURE
```

No continúes con inferencia parcial.

---

## 5. Alcance inferencial exacto

### 5.1 HE2_A — tres familias primarias

Para cada estrategia normativa corregida:

```text
flat
hierarchical
D1a
```

calcula los cinco contrastes primarios congelados:

```text
Top-1
Top-3
Top-5
Top-10
MRR@100
```

Total primario HE2_A:

```text
3 estrategias x 5 métricas = 15 contrastes
```

Estimando exacto:

```text
series-weighted mean of paired per-series (historical - normative) contributions
```

Contribuciones:

- Top-k: `I(rank_historical <= k) - I(rank_normative <= k)`.
- MRR@100: `RR100_historical - RR100_normative`, donde `RR100 = 1/rank` si `rank<=100`, y 0 en otro caso.

Dirección esperada congelada:

```text
historical - normative > 0
```

### 5.2 Top-50 suplementario

Top-50 permanece **SUPPLEMENTARY**, nunca primario.

Para cada una de las tres estrategias puedes calcular un intervalo bootstrap suplementario no ajustado al 95% usando el mismo resampling congelado, pero debes etiquetarlo explícitamente:

```text
ROLE = SUPPLEMENTARY
HYPOTHESIS_DECISION_ROLE = NONE
MULTIPLICITY_FAMILY = NOT_INCLUDED_IN_PRIMARY_FIVE_METRIC_FAMILY
CI_LEVEL = 0.95
```

Estos tres resultados no pueden utilizarse en G3-F03 para declarar apoyo/rechazo de HE2.

### 5.3 HE2_B — único contraste inferencial de cobertura profunda

Calcula exactamente un contraste:

```text
Recall@200 - Recall@100
```

sobre la familia jerárquica corregida Attempt06.

Estimando:

```text
series-weighted mean of paired per-series (hit_recall_200 - hit_recall_100)
```

Dirección esperada:

```text
Recall@200 - Recall@100 > 0
```

`Pool@200` puede preservarse como valor descriptivo equivalente de cobertura si la fuente lo materializa así, pero **no crea un segundo contraste inferencial duplicado**.

Total de contrastes inferenciales primarios de G3-F03:

```text
15 HE2_A + 1 HE2_B = 16
```

Más, como máximo:

```text
3 Top-50 supplementary uncertainty rows
```

---

## 6. Algoritmo bootstrap congelado para Prompt83

No selecciones método después de observar resultados.

Usa exactamente:

```text
BOOTSTRAP_TYPE = PAIRED_DAM_CLUSTER_PERCENTILE
B = 10000
SEED = 20263001
RNG = numpy.random.default_rng
RNG_BIT_GENERATOR = PCG64
CLUSTER_COUNT_PER_REPLICATE = 67
CLUSTER_LIST_ORDER = lexicographic sorted unique DAM identifiers
QUANTILE_METHOD = linear
PRIMARY_ESTIMAND_WEIGHTING = SERIES_WEIGHTED
```

### 6.1 Matriz de resampling

Inicializa una sola vez:

```python
rng = np.random.default_rng(20263001)
```

Genera una única matriz de índices de clusters de forma:

```text
(10000, 67)
```

muestreando con reemplazo sobre los 67 DAM ordenados lexicográficamente.

**Usa exactamente la misma matriz de resampling para todos los contrastes de G3-F03.**

### 6.2 Preservación del estimando por SERIE

Cada vez que un DAM aparece `m` veces en un replicate, todas sus series aparecen con multiplicidad `m`.

El estimando bootstrap debe calcularse como:

```text
sum(m_dam * sum_of_series_contributions_in_dam)
-------------------------------------------------
sum(m_dam * number_of_series_in_dam)
```

Esto preserva el estimando ponderado por SERIE.

**Prohibido** sustituirlo por la media no ponderada de medias por DAM.

### 6.3 Intervalos y multiplicidad

Para cada una de las tres familias primarias HE2_A:

```text
5 métricas primarias
99% marginal two-sided percentile CI
quantiles = [0.005, 0.995]
Bonferroni familywise coverage target = 95%
no p-values
```

Para HE2_B:

```text
1 contraste
95% two-sided percentile CI
quantiles = [0.025, 0.975]
no multiplicity adjustment
no p-values
```

Para Top-50 suplementario, si se calcula:

```text
95% two-sided percentile CI
no multiplicity adjustment
supplementary only
```

No produzcas intervalos alternativos BCa, normal, studentized ni bootstrap-t.

---

## 7. Tamaño de efecto e incertidumbre

La **medida de efecto** de G3-F03 es el estimando prospectivo ya congelado: diferencia pareada absoluta de contribuciones.

No inventes Cohen's d, odds ratio, risk ratio ni otro tamaño de efecto estandarizado/post hoc.

Para métricas de proporción (`Top-k`, `Recall`), reporta:

```text
point_estimate_absolute_difference
point_estimate_percentage_points = 100 * point_estimate_absolute_difference
CI en escala de diferencia absoluta
```

Para MRR@100 reporta la diferencia absoluta de reciprocal-rank medio y su CI.

Todos los outputs deben incluir:

```text
n_series = 1056
n_dam = 67
bootstrap_B = 10000
bootstrap_seed = 20263001
analysis_unit = SERIE
dependency_group = DAM / DECLARACIÓN
```

Los intervalos describen incertidumbre de resampling cluster-aware dentro del benchmark interno de Clase 87. **No autorizan una afirmación de validez externa poblacional.**

---

## 8. Familias que NO reciben inferencia en G3-F03

No calcules CI nuevos, tests ni p-values para:

```text
HE2_B_PHASE_E_FROZEN_ROLE_POOLS
HE2_B_PHASE_E_70_30
HE2_B_PHASE_E_DIAGNOSTIC_UNION
EXP11A_HISTORICAL_BANK_SENSITIVITY
EXP11B_H150_H200_PAIRED_SENSITIVITY
0B05C_ATTEMPT06_CORRECTIVE_SENSITIVITY
HE5_AMBIGUOUS_INCOMPLETE_DESCRIPTIONS
HE5_HIERARCHICAL_PROXIMITY
HE5_INSUFFICIENT_HISTORICAL_PRECEDENTS
HE5_INTERNAL_EVALUATION_SCOPE
HE5_EXPLANATION_EVIDENCE_LIMITS
EXP12_DIVERSITY
```

Tratamiento obligatorio:

- Phase E: solo descriptivo congelado.
- EXP11A: sensibilidad conjunta tamaño/composición; no efecto causal aislado.
- EXP11B: descriptivo; no superpoblación de seeds y no `10 x 1056` independientes.
- 0B-05C: Attempt06 corregido permanece estado científico vigente, solo descriptivo en esta ficha.
- HE5: todas sus familias permanecen `DESCRIPTIVE_ONLY`; no crear tests post hoc.
- EXP12: `NOT_ESTIMABLE`; no retrieval, no test, no reapertura.

El documento de métodos debe listar explícitamente estas exclusiones y sus motivos.

---

## 9. Rama científica y outputs autorizados

Crea desde exactamente:

```text
adf70d6eb880c567d6efa0f27b5c79259b8db2a6
```

la rama:

```text
codex/group3-f03-inference-v01
```

Crea exactamente estos cinco paths científicos nuevos:

```text
src/analysis/run_g3_f03_inference_v01.py
outputs/analysis/group3/g3_inferential_results_v0.1.csv
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
outputs/analysis/group3/g3_inferential_results_v0.1_hash_ledger.csv
```

No modifiques archivos científicos existentes.

El script debe ser el único mecanismo de cálculo de los resultados inferenciales. No copies manualmente intervalos desde consola al CSV/JSON.

Haz un solo commit científico con los cinco paths.

Estado de los artefactos:

```text
G3_F03_STATUS = CANDIDATE_PENDING_EXTERNAL_AUDIT
HE2_DECIDED = false
HE5_DECIDED = false
G3_F04_STARTED = false
```

---

## 10. Esquema mínimo de `g3_inferential_results_v0.1.csv`

Una fila por contraste/resultado de incertidumbre.

Columnas mínimas:

```text
result_id
hypothesis_component
evidence_family_id
role
comparison_id
metric_name
estimand
expected_direction
analysis_unit
dependency_group
n_series
n_dam
point_estimate
point_estimate_percentage_points
value_unit
bootstrap_type
bootstrap_B
bootstrap_seed
ci_method
ci_level
ci_lower
ci_upper
multiplicity_method
multiplicity_family
hypothesis_decision_role
source_registry_row_ids
source_case_level_paths
scope
limitations
```

Reglas:

- 16 filas `PRIMARY_INFERENTIAL` obligatorias.
- hasta 3 filas `SUPPLEMENTARY` para Top-50.
- `hypothesis_decision_role` debe ser `DEFERRED_TO_G3_F04` para primarios y `NONE` para Top-50.
- ningún campo puede contener `SUPPORTED`, `NOT_SUPPORTED`, `SIGNIFICANT`, `NONSIGNIFICANT` ni equivalente.

---

## 11. JSON y documento de métodos/checks

### 11.1 JSON

Debe contener, como mínimo:

- refs científicos de entrada;
- hashes/blobs verificados;
- parámetros exactos de bootstrap;
- versión de Python, NumPy y pandas usadas;
- inventario de 16 contrastes primarios;
- resultados fila por fila equivalentes al CSV;
- checks de integridad previos;
- conteo de filas por role;
- lista de familias descriptivas/no estimables deliberadamente no sometidas a inferencia;
- flags explícitos:

```text
P_VALUES_CALCULATED = false
STANDARDIZED_EFFECT_SIZE_INVENTED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false
G3_F04_STARTED = false
```

### 11.2 Methods and checks

`docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md` debe documentar:

1. precondiciones y fuentes congeladas;
2. reconstrucción de point estimates contra G3-F02;
3. reglas de pareamiento;
4. dependencia intra-DAM;
5. algoritmo exacto de bootstrap;
6. preservación de ponderación por SERIE;
7. multiplicidad de HE2_A;
8. único contraste HE2_B;
9. tratamiento suplementario de Top-50;
10. exclusión inferencial de EXP11A/EXP11B/0B-05C/HE5/EXP12 y motivos;
11. alcance interno de los intervalos;
12. ausencia de p-values y ausencia de decisión de hipótesis;
13. cualquier warning observado.

No redactes conclusiones del artículo.

---

## 12. Hash ledger y reproducibilidad inmediata

El ledger debe registrar para los otros cuatro artefactos científicos:

```text
artifact_path
git_blob_after_commit
sha256
size_bytes
hash_scope
```

No intentes incluir el hash del propio ledger dentro del ledger.

Antes del commit final:

1. ejecuta el script desde un working tree limpio respecto de inputs;
2. genera los outputs;
3. vuelve a ejecutar en un directorio temporal con los mismos inputs/refs;
4. confirma equivalencia byte a byte de CSV y JSON entre ambas ejecuciones;
5. si no es determinista, `STOP / NONDETERMINISTIC_INFERENCE_OUTPUT`.

No incluyas timestamps variables en CSV/JSON que impidan reproducibilidad byte-exacta.

---

## 13. Validaciones terminales del candidato

Antes de publicar la rama científica verifica:

```text
candidate_parent = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
commits_ahead = 1
commits_behind = 0
changed_path_count = 5
```

Los únicos paths cambiados deben ser los cinco de la sección 9.

Valida además:

```text
PRIMARY_INFERENTIAL_RESULT_COUNT = 16
HE2_A_PRIMARY_RESULT_COUNT = 15
HE2_B_PRIMARY_RESULT_COUNT = 1
SUPPLEMENTARY_TOP50_RESULT_COUNT = 0..3
P_VALUES_CALCULATED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false
G3_F04_STARTED = false
```

Si falla cualquiera:

```text
STOP / G3_F03_CANDIDATE_VALIDATION_FAILURE
```

Publica la rama mediante push normal, sin force-push.

---

## 14. Registro post-ejecución de fichas

Solo después de publicar el candidato científico, vuelve a la rama:

```text
docs/fichas-grupos-3-8
```

Partiendo del commit de activación creado en sección 3, actualiza el registro dinámico para dejar:

```text
G3-F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G3-F04 = PROSPECTIVE / NOT_AUTHORIZED
```

Añade un bloque con:

```text
G3_F03_BRANCH = codex/group3-f03-inference-v01
G3_F03_CANDIDATE_COMMIT = <sha>
G3_F03_CHANGED_PATH_COUNT = 5
PRIMARY_INFERENTIAL_RESULT_COUNT = 16
HE2_A_PRIMARY_RESULT_COUNT = 15
HE2_B_PRIMARY_RESULT_COUNT = 1
SUPPLEMENTARY_TOP50_RESULT_COUNT = <0..3>
P_VALUES_CALCULATED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXTERNAL_AUDIT = PENDING
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G3_F04_AUTHORIZED = false
G3_F04_STARTED = false
```

Haz un único commit administrativo post-ejecución y push normal.

No modifiques Plan Maestro todavía; su reconciliación corresponde al cierre posterior tras auditoría externa.

---

## 15. Prohibiciones absolutas

Durante Prompt83 está prohibido:

- modificar `article/main-manuscript`;
- modificar Plan Maestro;
- integrar el candidato a `main`;
- decidir HE2 o HE5;
- activar o ejecutar G3-F04;
- calcular p-values;
- añadir familias/contrastes post hoc;
- cambiar B, seed, cluster, ponderación o CI después de observar resultados;
- utilizar Top-50 como primario;
- ejecutar inferencia sobre HE5;
- inferir sobre EXP11A o EXP11B;
- reabrir outputs supersedidos de 0B-05C;
- reabrir EXP12;
- reejecutar retrieval/BM25/dense retrieval;
- modificar outputs experimentales congelados;
- tratar series dentro de DAM como independientes para el bootstrap;
- tratar las 10 réplicas EXP11B como superpoblación inferencial;
- afirmar causalidad aislada de tamaño de banco;
- hacer force-push, squash, rebase o amend de historia científica publicada.

---

## 16. Respuesta administrativa de Prompt83

Al finalizar crea, en `codex/prompts-temporary`:

```text
codex_prompts_tmp/83_RESPUESTA_ACTIVAR_Y_EJECUTAR_G3_F03_INFERENCIA_Y_SENSIBILIDAD.md
```

Commit únicamente ese archivo administrativo en la rama de prompts.

La respuesta debe registrar refs de entrada, activación, candidato, blobs/hashes de outputs, validaciones, conteos de resultados, ausencia de p-values/decisión HE2-HE5 y cualquier warning.

---

## 17. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT83 = COMPLETED | STOP

PREFLIGHT_MAIN =
PREFLIGHT_PLAN =
PREFLIGHT_FICHAS =
ARTICLE_HEAD_OBSERVED =
ARTICLE_HEAD_FINAL_OBSERVED =
ARTICLE_MODIFIED_BY_PROMPT83 = false

G3_F03_ACTIVATION_COMMIT =
G3_F03_BRANCH = codex/group3-f03-inference-v01
G3_F03_CANDIDATE_COMMIT =
G3_F03_CANDIDATE_PARENT =
G3_F03_COMMITS_AHEAD =
G3_F03_COMMITS_BEHIND =
G3_F03_CHANGED_PATH_COUNT =
G3_F03_CHANGED_PATHS =

PRIMARY_INFERENTIAL_RESULT_COUNT =
HE2_A_PRIMARY_RESULT_COUNT =
HE2_B_PRIMARY_RESULT_COUNT =
SUPPLEMENTARY_TOP50_RESULT_COUNT =

BOOTSTRAP_TYPE = PAIRED_DAM_CLUSTER_PERCENTILE
BOOTSTRAP_B = 10000
BOOTSTRAP_SEED = 20263001
HE2_A_PRIMARY_CI_LEVEL = 0.99
HE2_B_CI_LEVEL = 0.95

CSV_BLOB =
JSON_BLOB =
METHODS_MD_BLOB =
SCRIPT_BLOB =
HASH_LEDGER_BLOB =

G3_F03_POSTEXEC_FICHAS_COMMIT =
PROMPT83_RESPONSE_COMMIT = THIS_COMMIT

P_VALUES_CALCULATED = false
STANDARDIZED_EFFECT_SIZE_INVENTED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false
G3_F04_AUTHORIZED = false
G3_F04_STARTED = false

G3_F03_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED

BLOCKERS =
WARNINGS =
```
