# PROMPT 81 — ACTIVAR Y EJECUTAR EXCLUSIVAMENTE G3-F02: REGISTRO MAESTRO DE MÉTRICAS Y POBLACIONES

## Rol y alcance

Actúa como **ejecutor técnico controlado**.

Este prompt permanece inerte hasta que el autor lo invoque expresamente. La ejecución del prompt corto que referencia este archivo constituye autorización del autor **únicamente para G3-F02**.

G3-F01 ya fue cerrado tras auditoría y reauditoría externa, integrado a `main` y reconciliado en el Plan Maestro y el registro de fichas. G3-F02 debe construir una matriz única, auditable y versionada de métricas, poblaciones, resultados congelados y procedencia, sin ejecutar todavía inferencia.

Este prompt:

- activa formalmente G3-F02 antes de producir evidencia científica;
- construye el registro maestro exigido por la ficha G3-F02;
- usa exclusivamente fuentes permitidas por el contrato G3-F01 integrado;
- NO recalcula métricas científicas;
- NO ejecuta bootstrap, intervalos, p-values ni tamaños de efecto;
- NO decide HE2 ni HE5;
- NO inicia G3-F03;
- NO modifica el artículo.

---

## 1. Refs gobernantes y preflight remoto

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 366bf529c29cb999bfd043db33674a510ba184c7
origin/docs/plan-maestro-temporal-2026-08-31 = 59e7fc935dd5cde9a22bb2743a4116f35ad60a26
origin/docs/fichas-grupos-3-8 = ba9cc595778c4073b3bc20c60ad6a567bf514e9d
origin/codex/prompts-temporary = <commit que contiene este Prompt81>
```

Observa y registra el HEAD vigente de:

```text
origin/article/main-manuscript
```

pero un avance puramente editorial NO bloquea G3-F02 porque este bloque no modifica el artículo.

Si `main`, Plan o fichas difieren de los SHA anteriores:

```text
STOP / G3_F02_GOVERNANCE_REF_DRIFT
```

No resuelvas drift con rebase, merge, cherry-pick, amend, force-push ni reconstrucción manual.

---

## 2. Lecturas obligatorias

Lee íntegramente desde `origin/docs/fichas-grupos-3-8 = ba9cc595778c4073b3bc20c60ad6a567bf514e9d`:

```text
docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/01_GOBERNANZA_Y_ESTADOS.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
docs/fichas/grupos_3_8/grupo_3/G3_F02_REGISTRO_MAESTRO_METRICAS_Y_POBLACIONES.md
```

Lee íntegramente desde `origin/docs/plan-maestro-temporal-2026-08-31 = 59e7fc935dd5cde9a22bb2743a4116f35ad60a26`:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Lee íntegramente desde `origin/main = 366bf529c29cb999bfd043db33674a510ba184c7`:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

El JSON G3-F01 integrado es la **allowlist científica** de familias, fuentes, métricas, estimandos, exclusiones y clasificación de uso para G3-F02.

---

## 3. Precondición obligatoria de G3-F02

Antes de activar o generar outputs confirma conjuntamente:

```text
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F01_MAIN_INTEGRATION_COMMIT = 366bf529c29cb999bfd043db33674a510ba184c7
G3_F01_CORRECTED_EXTERNAL_REAUDIT = PASS
NEXT_ELIGIBLE_FICHA = G3-F02
G3_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Confirma también en el contrato integrado:

```text
ficha = G3-F01
revision = PROMPT79_CORRECTIVE_MICROCLOSE
UNIT_OF_ANALYSIS = SERIE
PRIMARY_ANALYTICAL_UNIT = SERIE
DEPENDENCE_HANDLING = DAM_CLUSTER_AWARE
EVAL_V02_N = 1056
EVAL_V02_DAM_N = 67
EVAL_V02_NANDINA_N = 42
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
classification_counts.evidence_family_count = 16
classification_counts.ELIGIBLE = 4
classification_counts.DESCRIPTIVE_ONLY = 11
classification_counts.NOT_ESTIMABLE = 1
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
```

Si no coincide:

```text
STOP / G3_F02_PRECONDITION_FAILED
```

---

## 4. Activación administrativa PREVIA a la ejecución científica

La activación de G3-F02 debe quedar materializada **antes** de crear su candidato científico.

Trabaja sobre:

```text
branch = docs/fichas-grupos-3-8
base = ba9cc595778c4073b3bc20c60ad6a567bf514e9d
```

Modifica únicamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

### 4.1 Normalización administrativa no bloqueante

El encabezado de la segunda columna del registro todavía dice `Estado inicial`, aunque ahora contiene estados vigentes como `CLOSED / APPROVED` y `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.

Normalízalo a:

```text
Estado actual
```

No alteres el contenido histórico de la reconciliación G3-F01.

### 4.2 Registro de activación G3-F02

Cambia únicamente la fila G3-F02 a:

```text
ACTIVE / AUTHORIZED / EXECUTION_PENDING
```

y agrega una sección explícita de activación con al menos:

```text
FICHA = G3-F02
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT81_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
ACTIVATION_DATE = 2026-09-19

MAIN_AT_ACTIVATION = 366bf529c29cb999bfd043db33674a510ba184c7
PLAN_AT_ACTIVATION = 59e7fc935dd5cde9a22bb2743a4116f35ad60a26
FICHAS_AT_ACTIVATION = ba9cc595778c4073b3bc20c60ad6a567bf514e9d
ARTICLE_HEAD_OBSERVED = <SHA observado>
PROMPT81_COMMIT = <commit que contiene Prompt81>

INPUT_CONTRACT_MD = docs/analysis/group3/g3_analytical_contract_v0.1.md
INPUT_CONTRACT_JSON = outputs/analysis/group3/g3_analytical_contract_v0.1.json

EXPECTED_OUTPUTS =
  outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
  outputs/analysis/group3/g3_metric_population_registry_v0.1.json
  outputs/analysis/group3/g3_metric_population_registry_v0.1_hash_ledger.csv

INFERENTIAL_CALCULATION_AUTHORIZED = false
METRICS_RECOMPUTATION_AUTHORIZED = false
HE2_DECISION_AUTHORIZED = false
HE5_DECISION_AUTHORIZED = false
G3_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING
RESULT = PENDING
```

Publica este cambio como **un commit administrativo previo** en `docs/fichas-grupos-3-8`.

Después ejecuta `git fetch origin` y confirma que el commit de activación es el HEAD remoto antes de producir los outputs científicos.

Si no puedes materializar la activación primero:

```text
STOP / G3_F02_ACTIVATION_NOT_MATERIALIZED
```

---

## 5. Principio rector del registro G3-F02

G3-F02 no crea ciencia nueva. Debe construir un **registro maestro estático** a partir de resultados y metadatos ya congelados.

Está permitido:

- leer/parsing de JSON/CSV/MD congelados;
- copiar valores científicos ya materializados;
- verificar identidad de claves, versiones, poblaciones y paths;
- obtener Git blob SHA;
- calcular SHA-256 y tamaño de archivos para trazabilidad;
- validar consistencia estructural entre outputs.

Está prohibido:

- recomputar Top-k, MRR, Recall, Pool, tasas, medias o deltas a partir de case-level si el valor no existe ya materializado como resultado congelado;
- calcular nuevos intervalos, errores estándar, bootstrap, pruebas, p-values o tamaños de efecto;
- combinar resultados de fuentes incompatibles;
- seleccionar métricas después de observar resultados;
- promover evidencia descriptiva a inferencial;
- crear una definición nueva de `insufficient historical precedents`;
- reabrir EXP12.

Si un valor científico requerido por el esquema no existe materializado en una fuente autorizada, no lo derives. Registra:

```text
observed_value = null
value_status = SOURCE_VALUE_NOT_MATERIALIZED
```

y conserva la fuente case-level para una ficha posterior solo si G3-F01 la autorizó.

---

## 6. Rama científica y outputs exactos

Crea desde exactamente:

```text
origin/main = 366bf529c29cb999bfd043db33674a510ba184c7
```

la rama:

```text
codex/group3-f02-metric-population-registry-v01
```

Publica **un solo commit científico** que añada exclusivamente:

```text
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1_hash_ledger.csv
```

No modifiques ningún archivo científico existente, incluido el contrato G3-F01.

Los outputs deben declarar:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G3-F02
source_main_commit = 366bf529c29cb999bfd043db33674a510ba184c7
source_plan_commit = 59e7fc935dd5cde9a22bb2743a4116f35ad60a26
source_fichas_activation_commit = <commit de activación G3-F02>
source_g3_f01_contract_commit = 366bf529c29cb999bfd043db33674a510ba184c7
prompt = PROMPT81
```

---

## 7. Granularidad obligatoria del registro

La unidad del registro es **una fila de resultado/estado de métrica bajo una condición y familia de evidencia concretas**.

Cada fila debe pertenecer a exactamente un `evidence_family_id` existente en G3-F01. No inventes familias nuevas.

El CSV debe incluir al menos estas columnas, en este orden o en un orden documentado y estable:

```text
registry_row_id
evidence_family_id
hypothesis_component
block_experiment
use_classification
record_role
condition_id
comparison_id
metric_name
metric_definition
observed_numerator
observed_denominator
observed_value
value_unit
value_status
dataset_id
dataset_sha256
n_series
n_dam
analysis_unit
dependency_group
source_path
source_git_blob
source_sha256
source_commit_binding
case_level_source_path
case_level_source_git_blob
estimand_id
estimand_text
expected_direction
future_analysis_status
multiplicity_family
paired_by
cluster_rule
frozen_exclusions
limitations
missing_reason
```

### 7.1 Valores permitidos clave

`use_classification` debe heredar exclusivamente una clasificación terminal de G3-F01:

```text
ELIGIBLE
DESCRIPTIVE_ONLY
NOT_ESTIMABLE
NOT_APPLICABLE
```

`record_role` debe ser uno de:

```text
PRIMARY_TARGET
SUPPLEMENTARY
DESCRIPTIVE
DIAGNOSTIC
NOT_ESTIMABLE
```

`future_analysis_status` debe ser uno de:

```text
INFERENTIAL_ELIGIBLE
DESCRIPTIVE_ONLY
NOT_ESTIMABLE
NOT_APPLICABLE
```

No uses en G3-F02:

```text
SUPPORTED
PARTIALLY_SUPPORTED
REJECTED
SIGNIFICANT
NONSIGNIFICANT
```

ni equivalentes decisionales sobre HE2/HE5.

---

## 8. Cobertura obligatoria de las 16 familias G3-F01

El registro debe contener las **16 familias** del contrato y ninguna adicional.

### 8.1 HE2_A — tres comparaciones de ranking temprano

Debes registrar por separado:

```text
HE2_A_HISTORICAL_VS_NORMATIVE_FLAT_ATTEMPT06
HE2_A_HISTORICAL_VS_NORMATIVE_HIERARCHICAL_ATTEMPT06
HE2_A_HISTORICAL_VS_D1A_ATTEMPT06
```

Para cada familia:

- representa ambos brazos/condiciones de la comparación;
- registra como primarias únicamente `Top-1`, `Top-3`, `Top-5`, `Top-10`, `MRR@100`;
- `Top-50` es `SUPPLEMENTARY`;
- usa el mismo EVAL v0.2 de 1,056 series / 67 DAM;
- conserva `SERIE` como unidad analítica y DAM como agrupamiento;
- usa histórico H100 congelado frente a las salidas **Attempt06 corrected Decision906** correspondientes;
- no uses como fuente primaria flat/hierarchical/D1a supersedidos cuando exista salida correctiva.

Para MRR histórico, registra explícitamente la equivalencia operacional con MRR@100 que sustenta el contrato: el ranking histórico congelado tiene profundidad 100. No inventes MRR@200 histórico.

### 8.2 HE2_B — cobertura profunda jerárquica

Para:

```text
HE2_B_HIERARCHICAL_DEEP_COVERAGE_ATTEMPT06
```

registra los resultados materializados de:

```text
Recall@100
Recall@200
Pool@200
```

según las fuentes corrected Attempt06 autorizadas. La comparación inferencial futura permanece el contraste prospectivo 200 vs 100 fijado en G3-F01; G3-F02 no lo calcula.

### 8.3 HE2_B — Phase E candidate pools

Registra separadamente:

```text
HE2_B_PHASE_E_FROZEN_ROLE_POOLS
HE2_B_PHASE_E_70_30
HE2_B_PHASE_E_DIAGNOSTIC_UNION
```

Usa exclusivamente:

```text
outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/
```

Respeta:

- `hierarchical_only`, `dual_only`, `hierarchical_first_100`, `hierarchical_80_dual_backfill_20` = roles congelados `A_historical_defined`;
- `hierarchical_70_dual_backfill_30` = `B_historical_not_formally_frozen_for_v0_2`, solo descriptivo;
- `diagnostic_union_hierarchical_dual` = `not_a_ranking=true`, solo techo diagnóstico descriptivo;
- no uses EXP08 como fuente primaria de HE2_B.

Incluye Pool/coverage a profundidades 50/100/200 y solo los niveles suplementarios HS6/HS4/chapter que G3-F01 autorizó.

### 8.4 EXP11A

Para:

```text
EXP11A_HISTORICAL_BANK_SENSITIVITY
```

preserva:

- H25 = 10 runs;
- H50 = 10 runs;
- H75 = 10 runs;
- H100 = una referencia congelada;
- H50 D1/D2 = 5 pares por seed;
- EVAL = 1,056 series / 67 DAM por run;
- H100 = 2,950 series / 28 DAM;
- métricas congeladas Top-1/3/5/10/50 y MRR;
- tamaño y composición del banco acoplados;
- clasificación `DESCRIPTIVE_ONLY`;
- ningún efecto causal aislado de tamaño.

Registra los resultados ya materializados por run/condición que estén en las fuentes autorizadas del contrato. No derives nuevos promedios ni intervalos.

### 8.5 EXP11B

Para:

```text
EXP11B_H150_H200_PAIRED_SENSITIVITY
```

preserva:

- 10 H150 y 10 H200;
- pairing por las 10 seeds congeladas;
- EVAL = 1,056 repetido en cada run;
- las 21,120 filas case-run NO son observaciones independientes;
- métricas congeladas Top-1/3/5/10/50 y MRR;
- clasificación `DESCRIPTIVE_ONLY`;
- no inventar superpoblación de seeds ni inferencia H150/H200.

Registra valores ya materializados por banco/condición desde los outputs autorizados. No derives nuevos tests ni intervalos.

### 8.6 0B-05C Attempt06

Para:

```text
0B05C_ATTEMPT06_CORRECTIVE_SENSITIVITY
```

usa solo Attempt06 y sus resultados corrected:

- EV03: conservar su impacto agregado congelado;
- EV04: conservar el cambio MRR no cero congelado y demás métricas congeladas;
- D1a: conservar la comparación corrective vs original congelada;
- no usar Attempts01–05 ni outputs supersedidos como estado vigente.

Clasificación: `DESCRIPTIVE_ONLY`.

### 8.7 HE5

Registra las cinco familias existentes del contrato sin convertirlas en nuevas proposiciones:

```text
HE5_AMBIGUOUS_INCOMPLETE_DESCRIPTIONS
HE5_HIERARCHICAL_PROXIMITY
HE5_INSUFFICIENT_HISTORICAL_PRECEDENTS
HE5_INTERNAL_EVALUATION_SCOPE
HE5_EXPLANATION_EVIDENCE_LIMITS
```

Reglas:

- `HE5_AMBIGUOUS_INCOMPLETE_DESCRIPTIONS`: no tasa de prevalencia; `description_quality_operationalized=0` debe quedar explícito y la ausencia de valor no es fallo del sistema;
- `HE5_HIERARCHICAL_PROXIMITY`: registrar literalmente categorías/cuentas congeladas, sin nuevo contraste inferencial;
- `HE5_INSUFFICIENT_HISTORICAL_PRECEDENTS`: conservar literalmente `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`; ninguna se renombra retrospectivamente como “insuficiente”;
- `HE5_INTERNAL_EVALUATION_SCOPE`: registrar cobertura/límite del benchmark interno;
- `HE5_EXPLANATION_EVIDENCE_LIMITS`: conservar los tamaños/coberturas de muestras diagnósticas y no extrapolarlos a EVAL completo.

Todas continúan `DESCRIPTIVE_ONLY`.

### 8.8 EXP12

Para:

```text
EXP12_DIVERSITY
```

crea únicamente registro de estado:

```text
classification = NOT_ESTIMABLE
observed_value = null
value_status = NOT_ESTIMABLE
n_series = 0
n_dam = 0
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
D_HIGH_D_MID_D_LOW = NOT_SELECTED
```

No hay fila de efecto numérico, test ni retrieval.

---

## 9. Reglas estrictas de procedencia

Cada fila debe tener procedencia verificable.

Obligatorio:

1. `source_path` existe en `main = 366bf529...` o corresponde a una fuente explícitamente enlazada por G3-F01.
2. `source_git_blob` coincide con Git.
3. `source_sha256` se toma de manifest/ledger congelado cuando exista; si no existe, puede calcularse sobre los bytes congelados **solo para trazabilidad**, sin alterar la ciencia.
4. `source_commit_binding` identifica `main` y, si aplica, execution/authorization commit ya congelado.
5. Si una fila depende de un case-level futuro, `case_level_source_path` debe señalar el path exacto autorizado por G3-F01.
6. Ninguna fila puede usar `3,000/1,006` como benchmark vigente.
7. Ninguna fila puede mezclar v0.1 y v0.2 como si fueran la misma población.
8. Ninguna fila de 0B-05C puede usar como vigente una salida supersedida cuando exista su corrected Attempt06.

Cualquier path requerido que no exista o cualquier incompatibilidad no resoluble debe producir:

```text
STOP / G3_F02_PROVENANCE_OR_COMPATIBILITY_FAILURE
```

No completes datos faltantes por memoria o inferencia.

---

## 10. JSON maestro

`g3_metric_population_registry_v0.1.json` debe contener al menos:

```text
registry_id
status
ficha
prompt
source_main_commit
source_plan_commit
source_fichas_activation_commit
source_g3_f01_contract_commit
global_bindings
schema
rows
validation
classification_counts
family_counts
scientific_actions
```

`rows` debe reflejar uno-a-uno el CSV mediante `registry_row_id` único.

`global_bindings` debe conservar al menos:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACIÓN cuando exista dependencia
EVAL_V02_N = 1056
EVAL_V02_DAM_N = 67
EVAL_V02_NANDINA_N = 42
EVAL_V02_SHA256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
H100_N = 2950
H100_DAM_N = 28
H100_NANDINA_N = 66
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

`scientific_actions` debe declarar:

```text
METRICS_RECOMPUTED = false
INFERENTIAL_CALCULATION_PERFORMED = false
BOOTSTRAP_CALCULATED = false
P_VALUES_CALCULATED = false
EFFECT_SIZES_CALCULATED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false
G3_F03_STARTED = false
```

---

## 11. Ledger de hashes

`g3_metric_population_registry_v0.1_hash_ledger.csv` debe hashear únicamente los otros dos outputs, evitando autorreferencia.

Columnas mínimas:

```text
artifact_path
git_blob_after_commit
sha256
size_bytes
hash_scope
```

Filas exactas:

```text
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
```

`hash_scope` debe ser:

```text
OUTPUT_BYTES_EXCLUDING_SELF_REFERENTIAL_LEDGER
```

No intentes almacenar un SHA-256 autorreferencial del propio ledger.

---

## 12. Validaciones obligatorias antes de publicar el candidato

Antes del commit científico verifica:

```text
EVIDENCE_FAMILIES_EXPECTED = 16
EVIDENCE_FAMILIES_PRESENT = 16
UNKNOWN_EVIDENCE_FAMILIES = 0
MISSING_EVIDENCE_FAMILIES = 0
DUPLICATE_REGISTRY_ROW_ID = 0
ROWS_WITHOUT_SOURCE_PROVENANCE = 0
ROWS_USING_SUPERSEDED_3000_1006_AS_CURRENT = 0
ROWS_MIXING_INCOMPATIBLE_EVALSETS = 0
0B05C_NON_ATTEMPT06_CURRENT_ROWS = 0
EXP12_NUMERIC_EFFECT_ROWS = 0
HE2_HE5_DECISION_ROWS = 0
INFERENTIAL_OUTPUT_ROWS = 0
```

Además:

- las 4 familias `ELIGIBLE` G3-F01 están presentes;
- las 11 `DESCRIPTIVE_ONLY` están presentes;
- la única `NOT_ESTIMABLE` EXP12 está presente;
- Top-50 no aparece como primario en HE2_A;
- candidate-pool HE2_B no usa EXP08 como fuente primaria;
- EXP11B no usa `10 × 1056` como N inferencial;
- HE5 no crea umbral post hoc de precedentes insuficientes;
- CSV y JSON tienen el mismo conjunto de `registry_row_id` y semántica de filas.

Si falla cualquiera:

```text
STOP / G3_F02_REGISTRY_VALIDATION_FAILED
```

---

## 13. Publicación científica candidata

El branch debe quedar:

```text
base = 366bf529c29cb999bfd043db33674a510ba184c7
commits_ahead = 1
commits_behind = 0
changed_path_count = 3
```

Paths exactos:

```text
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1_hash_ledger.csv
```

No integres a `main`.

Estado del candidato:

```text
G3_F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT
G3_F03 = NOT_AUTHORIZED / NOT_EXECUTED
```

---

## 14. Actualización administrativa posterior a la ejecución, sin cierre

Después de publicar exitosamente el candidato científico, vuelve a la rama `docs/fichas-grupos-3-8` cuyo HEAD debe ser exactamente el commit de activación creado en §4.

Modifica nuevamente **solo**:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Actualiza G3-F02 a:

```text
CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

y agrega al registro de G3-F02:

```text
CANDIDATE_BRANCH = codex/group3-f02-metric-population-registry-v01
CANDIDATE_COMMIT = <SHA científico>
CANDIDATE_CHANGED_PATHS = <los tres paths exactos>
EVIDENCE_FAMILY_COUNT = 16
REGISTRY_ROW_COUNT = <n>
EXTERNAL_AUDIT = PENDING
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT
G3_F03_AUTHORIZED = false
G3_F03_STARTED = false
```

Publica un segundo commit administrativo de estado en la rama de fichas.

No cierres G3-F02. No modifiques el Plan Maestro en Prompt81; el Plan se reconciliará únicamente después de auditoría externa y cierre, como se hizo con G3-F01.

---

## 15. Persistencia administrativa de Prompt81

En `codex/prompts-temporary`, crea únicamente:

```text
codex_prompts_tmp/81_RESPUESTA_ACTIVAR_Y_EJECUTAR_G3_F02_REGISTRO_MAESTRO_METRICAS_Y_POBLACIONES.md
```

El commit administrativo de respuesta debe añadir solamente ese archivo.

La respuesta debe registrar:

- refs preflight;
- HEAD editorial observado;
- commit de activación G3-F02 en fichas;
- branch/commit científico candidato;
- commits ahead/behind;
- paths científicos;
- blob y SHA-256 de CSV/JSON/ledger;
- row count;
- conteo de familias y clasificaciones;
- resultado de todas las validaciones del §12;
- commit final de estado `CANDIDATE_PENDING_EXTERNAL_AUDIT` en fichas;
- confirmación de cero recomputación/inferencia;
- confirmación de G3-F03 no iniciado.

---

## 16. Prohibiciones absolutas

No:

- modificar `main`;
- modificar el Plan Maestro;
- modificar `article/main-manuscript`;
- modificar el contrato G3-F01;
- integrar el candidato G3-F02;
- recalcular métricas científicas;
- calcular nuevos deltas científicos desde case-level;
- ejecutar bootstrap, CI, p-values, tests o tamaños de efecto;
- decidir HE2 o HE5;
- activar/iniciar G3-F03;
- reabrir EXP12;
- reejecutar retrieval, EXP11A, EXP11B, 0B-05C o cualquier otro experimento;
- utilizar outputs supersedidos como ciencia vigente;
- realizar force-push, amend, rebase o squash para alterar historia científica.

---

## 17. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT81 = COMPLETED | STOP

PREFLIGHT_MAIN =
PREFLIGHT_PLAN =
PREFLIGHT_FICHAS =
ARTICLE_HEAD_OBSERVED =
PROMPT81_COMMIT =

G3_F02_ACTIVATION_COMMIT =
G3_F02_ACTIVATION_MATERIALIZED_BEFORE_EXECUTION = true|false

G3_F02_BRANCH = codex/group3-f02-metric-population-registry-v01
G3_F02_CANDIDATE_COMMIT =
G3_F02_COMMITS_AHEAD =
G3_F02_COMMITS_BEHIND =
G3_F02_CHANGED_PATH_COUNT =
G3_F02_CHANGED_PATHS =

REGISTRY_ROW_COUNT =
EVIDENCE_FAMILY_COUNT =
ELIGIBLE_FAMILY_COUNT =
DESCRIPTIVE_ONLY_FAMILY_COUNT =
NOT_ESTIMABLE_FAMILY_COUNT =
NOT_APPLICABLE_FAMILY_COUNT =

CSV_BLOB =
CSV_SHA256 =
JSON_BLOB =
JSON_SHA256 =
HASH_LEDGER_BLOB =

UNKNOWN_EVIDENCE_FAMILIES =
MISSING_EVIDENCE_FAMILIES =
DUPLICATE_REGISTRY_ROW_ID =
ROWS_WITHOUT_SOURCE_PROVENANCE =
ROWS_USING_SUPERSEDED_3000_1006_AS_CURRENT =
ROWS_MIXING_INCOMPATIBLE_EVALSETS =
0B05C_NON_ATTEMPT06_CURRENT_ROWS =
EXP12_NUMERIC_EFFECT_ROWS =
HE2_HE5_DECISION_ROWS =
INFERENTIAL_OUTPUT_ROWS =

G3_F02_FINAL_FICHAS_STATE_COMMIT =
G3_F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED

METRICS_RECOMPUTED = false
INFERENTIAL_CALCULATION_PERFORMED = false
BOOTSTRAP_CALCULATED = false
P_VALUES_CALCULATED = false
EFFECT_SIZES_CALCULATED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false
G3_F03_AUTHORIZED = false
G3_F03_STARTED = false

BLOCKERS =
WARNINGS =
```

Detente ahí. No ejecutes G3-F03.