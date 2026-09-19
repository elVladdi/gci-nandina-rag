# PROMPT 84 — INTEGRAR Y CERRAR EXCLUSIVAMENTE G3-F03 TRAS AUDITORÍA EXTERNA

## 0. Naturaleza de esta ejecución

Esta es una ejecución **administrativa de integración y cierre** de G3-F03.

La IA Experimental realizó auditoría externa independiente del candidato producido por Prompt83 y el dictamen es:

```text
G3_F03_EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
SCIENTIFIC_RERUN_REQUIRED = false
INFERENTIAL_RECOMPUTATION_REQUIRED = false
G3_F04_AUTHORIZED = false
```

La auditoría externa verificó, entre otros puntos:

- la activación prospectiva de G3-F03 fue materializada antes de la ejecución inferencial;
- el candidato científico tiene padre exacto `adf70d6eb880c567d6efa0f27b5c79259b8db2a6`;
- el candidato está exactamente 1 commit delante y 0 detrás de `main` de entrada;
- existen exactamente 5 paths científicos nuevos y ningún archivo científico previo fue modificado;
- el script versionado es el mecanismo de cálculo de los resultados;
- se preservó `SERIE` como unidad analítica y `DAM / DECLARACIÓN` como cluster de dependencia;
- el bootstrap es `PAIRED_DAM_CLUSTER_PERCENTILE`, con `B=10000`, `seed=20263001`, `numpy.random.default_rng`/PCG64 y 67 DAM por replicate;
- la misma matriz de resampling se usa para todos los contrastes;
- el estimando bootstrap conserva ponderación por SERIE, no una media no ponderada de medias por DAM;
- los point estimates reconstruidos desde case-level coinciden con G3-F02 dentro de tolerancia `<=1e-12`;
- existen exactamente 16 resultados `PRIMARY_INFERENTIAL`: 15 HE2_A y 1 HE2_B;
- existen exactamente 3 resultados Top-50 `SUPPLEMENTARY` y sin rol decisional;
- HE2_A usa 99% marginal percentile CI dentro de cada familia de 5 métricas, conforme al Bonferroni prospectivo congelado;
- HE2_B usa un único contraste `Recall@200 - Recall@100` con 95% percentile CI;
- no se calcularon p-values;
- no se inventó un tamaño de efecto estandarizado post hoc;
- EXP11A, EXP11B, 0B-05C, HE5 y EXP12 no recibieron inferencia no autorizada;
- HE2 y HE5 permanecen sin decisión;
- G3-F04 no fue activada ni ejecutada;
- EXP12 no fue reabierto.

Los intervalos producidos son incertidumbre de resampling cluster-aware dentro del benchmark interno fijo de Clase 87. Su integración no autoriza una afirmación de validez externa ni constituye por sí misma una decisión de HE2/HE5.

Tu tarea es **integrar exactamente el candidato auditado**, reconciliar Plan Maestro y registro de fichas, y cerrar G3-F03. No debes activar ni ejecutar G3-F04.

---

## 1. Repositorio y refs congelados de entrada

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar cualquier cosa ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
origin/docs/plan-maestro-temporal-2026-08-31 = 12ac39ec18761bc926d196e71137de60c2a9956b
origin/docs/fichas-grupos-3-8 = b2c8bb0726be184250e18fd169dca45fc47f501d
```

Artículo observado al momento de esta auditoría:

```text
origin/article/main-manuscript = 45b0a5c61993178a71c7640c8051e3d7b24c0526
```

El artículo es solo observacional y no es input científico. Si avanza concurrentemente después del preflight, registra el drift como advertencia siempre que Prompt84 no lo modifique.

Candidato G3-F03 auditado:

```text
branch = codex/group3-f03-inference-v01
commit = 7d09f692da23367d3aba941db1febdca2baa8917
parent = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
```

Gobernanza de ejecución:

```text
PROMPT83_COMMIT = 10d94aeb982ad600229516ed27dd0fcc6b7264a0
PROMPT83_RESPONSE_COMMIT = 9155af0d8f95bc95232bb0f841b1175a467c0c5c
G3_F03_ACTIVATION_COMMIT = 6750ed15b0e8ed62f5deba517eddf92fa2616bca
G3_F03_POSTEXEC_FICHAS_COMMIT = b2c8bb0726be184250e18fd169dca45fc47f501d
```

Si `main`, Plan, fichas o la rama candidata científica presentan drift no explicado respecto de estos refs:

```text
STOP / REF_DRIFT_DETECTED
```

El avance de `codex/prompts-temporary` debido exclusivamente a la incorporación de Prompt84 es esperado y no constituye drift científico.

---

## 2. Verificación obligatoria del candidato antes de integrar

Compara:

```text
adf70d6eb880c567d6efa0f27b5c79259b8db2a6
..
7d09f692da23367d3aba941db1febdca2baa8917
```

Debe resultar exactamente:

```text
commits_ahead = 1
commits_behind = 0
changed_path_count = 5
```

Únicos paths permitidos:

```text
src/analysis/run_g3_f03_inference_v01.py
outputs/analysis/group3/g3_inferential_results_v0.1.csv
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
outputs/analysis/group3/g3_inferential_results_v0.1_hash_ledger.csv
```

Verifica exactamente los blobs auditados:

```text
SCRIPT_BLOB = 2378298c9db401c938ebfb3cd505b30cabad2c62
CSV_BLOB = cf3d8d85e099a300330da0214836e70af7a02253
JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
METHODS_MD_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
HASH_LEDGER_BLOB = b128966f1295ac8a853341b7f02ce7f9218157b8
```

Y los SHA-256 registrados:

```text
SCRIPT_SHA256 = 05199f33109e91b131768371235f7fa475bfb9f4364032cf680c167a6c5dae4e
CSV_SHA256 = 18c53532346140c7293affc299df3d780bb58fa7f5282326a3f547ae0086c29a
JSON_SHA256 = a02356e8d487051d1f1b002e55565242143cc8c2c82ad1aefa312592b636f1dc
METHODS_MD_SHA256 = 3fc158e3ffb6462790ab18ff37dedf536d52d45636ee6e2c83b0f2a1d7afabdc
HASH_LEDGER_SHA256 = 1be0ad9016af408aed742a9d16e8dbc64768e9de726a7628b3347610e8f6beee
```

Verifica además, sin recalcular inferencia:

```text
PRIMARY_INFERENTIAL_RESULT_COUNT = 16
HE2_A_PRIMARY_RESULT_COUNT = 15
HE2_B_PRIMARY_RESULT_COUNT = 1
SUPPLEMENTARY_TOP50_RESULT_COUNT = 3
P_VALUES_CALCULATED = false
STANDARDIZED_EFFECT_SIZE_INVENTED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false
G3_F04_STARTED = false
```

Las comprobaciones de integridad/hash/estructura están permitidas. **No vuelvas a ejecutar el bootstrap ni regeneres los outputs.**

Si la estructura, blobs, hashes o flags no coinciden:

```text
STOP / AUDITED_CANDIDATE_MISMATCH
```

---

## 3. Prohibiciones absolutas

Durante Prompt84 está prohibido:

- modificar cualquiera de los cinco artefactos científicos de G3-F03;
- reejecutar `run_g3_f03_inference_v01.py` para regenerar resultados;
- recalcular bootstrap o intervalos;
- recalcular métricas experimentales;
- calcular p-values;
- añadir contrastes;
- cambiar B, seed, quantiles, multiplicidad, unidad o cluster;
- decidir HE2;
- decidir HE5;
- redactar una disposición de hipótesis;
- activar o ejecutar G3-F04;
- reabrir EXP12;
- reejecutar retrieval/BM25/dense retrieval;
- modificar `article/main-manuscript`;
- modificar outputs de G3-F01/G3-F02;
- hacer force-push;
- hacer squash, rebase o amend del commit científico auditado.

---

## 4. Integración científica exacta a `main`

Integra el candidato auditado a `main` mediante **fast-forward only**.

Resultado obligatorio:

```text
origin/main = 7d09f692da23367d3aba941db1febdca2baa8917
```

No debe aparecer merge commit nuevo.

Después de integrar, los cinco blobs deben seguir siendo exactamente los indicados en la sección 2.

Si el fast-forward exacto no es posible:

```text
STOP / MAIN_FAST_FORWARD_NOT_POSSIBLE
```

---

## 5. Reconciliación del Plan Maestro

Trabaja exclusivamente sobre:

```text
branch: docs/plan-maestro-temporal-2026-08-31
file: docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Partiendo de:

```text
12ac39ec18761bc926d196e71137de60c2a9956b
```

Realiza el cambio mínimo necesario para registrar:

```text
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03_INTEGRATION_COMMIT = 7d09f692da23367d3aba941db1febdca2baa8917
G3_F03_PRIMARY_INFERENTIAL_RESULT_COUNT = 16
G3_F03_HE2_A_PRIMARY_RESULT_COUNT = 15
G3_F03_HE2_B_PRIMARY_RESULT_COUNT = 1
G3_F03_SUPPLEMENTARY_TOP50_RESULT_COUNT = 3
G3_F03_BOOTSTRAP = PAIRED_DAM_CLUSTER_PERCENTILE / B=10000 / SEED=20263001
NEXT_ELIGIBLE_FICHA = G3-F04
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Preserva explícitamente:

```text
STATISTICAL_INFERENCE_EXECUTED = true
P_VALUES_CALCULATED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```

Nota de semántica obligatoria: `STATISTICAL_INFERENCE_EXECUTED = true` describe exclusivamente la ejecución de los intervalos bootstrap autorizados en G3-F03. **No equivale a decisión de HE2/HE5.**

No reescribas historia previa ni modifiques otros grupos.

Haz un único commit administrativo del Plan para este cierre y publícalo mediante push normal.

---

## 6. Reconciliación del registro de fichas

Trabaja exclusivamente sobre:

```text
branch: docs/fichas-grupos-3-8
file: docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Partiendo de:

```text
b2c8bb0726be184250e18fd169dca45fc47f501d
```

### 6.1 Estado tabular

Actualiza únicamente lo necesario para que quede:

```text
G3-F01 = CLOSED / APPROVED
G3-F02 = CLOSED / APPROVED
G3-F03 = CLOSED / APPROVED
G3-F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Las fichas posteriores permanecen prospectivas/no autorizadas según sus precondiciones.

### 6.2 Registro de cierre G3-F03

Añade un bloque de cierre que conserve como mínimo:

```text
FICHA = G3-F03
ACTIVATION_COMMIT = 6750ed15b0e8ed62f5deba517eddf92fa2616bca
PROMPT83_COMMIT = 10d94aeb982ad600229516ed27dd0fcc6b7264a0
PROMPT83_RESPONSE_COMMIT = 9155af0d8f95bc95232bb0f841b1175a467c0c5c
CANDIDATE_COMMIT = 7d09f692da23367d3aba941db1febdca2baa8917
CANDIDATE_PARENT = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
SCIENTIFIC_RERUN_REQUIRED = false
INFERENTIAL_RECOMPUTATION_REQUIRED = false
PRIMARY_INFERENTIAL_RESULT_COUNT = 16
HE2_A_PRIMARY_RESULT_COUNT = 15
HE2_B_PRIMARY_RESULT_COUNT = 1
SUPPLEMENTARY_TOP50_RESULT_COUNT = 3
BOOTSTRAP_TYPE = PAIRED_DAM_CLUSTER_PERCENTILE
BOOTSTRAP_B = 10000
BOOTSTRAP_SEED = 20263001
P_VALUES_CALCULATED = false
INTEGRATION_COMMIT = 7d09f692da23367d3aba941db1febdca2baa8917
FINAL_G3_F03_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
STATISTICAL_INFERENCE_EXECUTED = true
HE2_DECIDED = false
HE5_DECIDED = false
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

No modifiques la ficha prospectiva original `G3_F03_INFERENCIA_Y_SENSIBILIDAD.md` para fingir cambios históricos; el registro dinámico conserva el estado operacional.

Haz un único commit administrativo del registro para este cierre y publícalo mediante push normal.

---

## 7. No activar G3-F04

El cierre correcto de Prompt84 deja:

```text
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

No crees rama científica de G3-F04.
No emitas `SUPPORTED`, `NOT_SUPPORTED`, `INCONCLUSIVE` ni ninguna disposición de HE2/HE5.

La autorización de G3-F04 requiere un prompt posterior de la IA Experimental después de verificar externamente Prompt84.

---

## 8. Respuesta administrativa de Prompt84

Al finalizar, crea en `codex/prompts-temporary`:

```text
codex_prompts_tmp/84_RESPUESTA_INTEGRAR_Y_CERRAR_G3_F03_TRAS_AUDITORIA_EXTERNA.md
```

Commit únicamente ese archivo administrativo en la rama de prompts.

La respuesta debe registrar al menos:

- refs de preflight;
- resultado de la verificación del candidato;
- `main` final;
- blobs finales de los cinco artefactos científicos;
- commit final del Plan Maestro;
- commit final del registro de fichas;
- head del artículo observado antes y después;
- confirmación de que Prompt84 no modificó el artículo;
- confirmación de que no hubo modificación ni recomputación científica;
- estado final de G3-F03;
- estado de G3-F04.

---

## 9. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT84 = COMPLETED | STOP

PREFLIGHT_MAIN =
PREFLIGHT_PLAN =
PREFLIGHT_FICHAS =
ARTICLE_HEAD_OBSERVED =
ARTICLE_HEAD_FINAL_OBSERVED =
ARTICLE_MODIFIED_BY_PROMPT84 = false

G3_F03_CANDIDATE_COMMIT =
G3_F03_COMMITS_AHEAD =
G3_F03_COMMITS_BEHIND =
G3_F03_CHANGED_PATH_COUNT =
G3_F03_CHANGED_PATHS =

MAIN_FINAL =
SCRIPT_BLOB_FINAL =
CSV_BLOB_FINAL =
JSON_BLOB_FINAL =
METHODS_MD_BLOB_FINAL =
HASH_LEDGER_BLOB_FINAL =

PLAN_CLOSURE_COMMIT =
FICHAS_CLOSURE_COMMIT =
PROMPT84_RESPONSE_COMMIT =

G3_F03_EXTERNAL_AUDIT = PASS
G3_F03_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
SCIENTIFIC_ARTIFACTS_MODIFIED = false
INFERENTIAL_RECOMPUTATION_PERFORMED = false
P_VALUES_CALCULATED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false

GROUP3 = IN_PROGRESS
STATISTICAL_INFERENCE_EXECUTED = true
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G3_F04_STARTED = false

BLOCKERS =
WARNINGS =
```
