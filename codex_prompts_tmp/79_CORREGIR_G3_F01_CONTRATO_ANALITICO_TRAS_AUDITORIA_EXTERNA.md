# PROMPT 79 — CORREGIR EXCLUSIVAMENTE G3-F01 TRAS AUDITORÍA EXTERNA

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

La IA Experimental realizó la auditoría externa independiente del candidato G3-F01 publicado en:

```text
branch = codex/group3-f01-analytical-contract-v01
commit = c727da94f5d38f530a839631c3ac9e427a1eb27e
parent = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

El dictamen externo es:

```text
G3_F01_EXTERNAL_AUDIT = BLOCKED_FOR_CORRECTION
SCIENTIFIC_RERUN_REQUIRED = false
INFERENTIAL_EXECUTION_AUTHORIZED = false
G3_F02_AUTHORIZED = false
```

Este Prompt79 ejecuta exclusivamente un **microcierre correctivo documental/prospectivo de G3-F01**. Debe corregir el contrato analítico antes de cualquier inferencia.

NO reejecutes retrieval, métricas, experimentos ni Attempt06. NO calcules p-values, intervalos, tamaños de efecto ni decisiones HE2/HE5. NO avances a G3-F02.

---

## 1. Refs gobernantes y preflight

Ejecuta `git fetch origin` y verifica:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
origin/codex/group3-f01-analytical-contract-v01 = c727da94f5d38f530a839631c3ac9e427a1eb27e
```

La rama editorial puede haber avanzado desde Prompt76. Verifica el HEAD vigente de:

```text
origin/article/main-manuscript
```

pero para la formulación aprobada de HE2/HE5 exige que continúen byte-idénticos los blobs congelados:

```text
article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md
blob = 52c45948bbc085a25faf4df850ae15e6ca682d17

article/reviews/0A01_AUTHOR_APPROVAL.md
blob = db5cd447df1d85ee0f9d271e2a85af66e050aea1
```

Si `main`, Plan, fichas o la rama candidata científica han cambiado, detente:

```text
STOP / SCIENTIFIC_REF_DRIFT_DETECTED
```

Un avance editorial por sí solo NO bloquea si ambos blobs congelados anteriores permanecen idénticos.

---

## 2. Hallazgos externos que deben corregirse

### G3F01-AUD-F001 — contrato estructuralmente incompleto

El candidato no materializó varios campos obligatorios exigidos por Prompt76 y la ficha G3-F01 para **cada familia de evidencia**.

Debes registrar explícitamente por familia, como mínimo:

- `evidence_family_id`;
- hipótesis/componente;
- bloque/experimento;
- paths científicos primarios;
- commit/binding científico;
- dataset/evalset exacto y hash cuando aplique;
- N de series/casos;
- N de DAM cuando aplique;
- unidad de observación;
- unidad de análisis;
- unidad de agrupamiento/dependencia;
- condiciones comparadas;
- métricas exactas elegibles;
- estimando exacto;
- dirección prevista cuando exista;
- exclusiones congeladas;
- comparabilidad directa o no;
- clasificación `ELIGIBLE | DESCRIPTIVE_ONLY | NOT_ESTIMABLE | NOT_APPLICABLE`;
- limitaciones;
- dependencia entre seeds/réplicas/condiciones;
- procedimiento prospectivo posterior, si procede;
- familia y regla de multiplicidad o justificación explícita de no aplicación.

No uses frases vagas como `common evaluation depth`, `declared depths`, `pre-specified buckets` o `if multiple contrasts are activated` sin identificar exactamente esos niveles/contrastes.

### G3F01-AUD-F002 — bindings globales obligatorios ausentes o insuficientes

El contrato corregido debe congelar explícitamente:

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
H100_SHA256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff

EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
SUPERSEDED_SPLIT_3000_1006 = EXCLUDED
```

Asimismo, ambos artefactos corregidos deben declarar literalmente:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G3-F01
revision = PROMPT79_CORRECTIVE_MICROCLOSE
```

### G3F01-AUD-F003 — HE2 incompleto y evidencia mal enlazada

HE2 permanece exactamente:

```text
La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.
```

La operacionalización aprobada identifica como métricas de desempeño primarias:

```text
Top-1
Top-3
Top-5
Top-10
MRR
```

y, para cobertura cuando corresponda:

```text
Recall@N / Pool@N
```

`Top-50` puede conservarse como métrica suplementaria/descriptiva cuando esté congelada en los artefactos, pero NO debe sustituir silenciosamente el conjunto primario aprobado anterior.

#### HE2_A — ranking temprano

No reduzcas HE2_A a histórico vs plano + jerárquico. Debes inventariar todas las estrategias normativas finales comparables del Grupo 1 que dispongan de Top-k/MRR sobre EVAL v0.2, incluida D1a cuando sea metodológicamente comparable.

Para 0B-05C rige obligatoriamente:

```text
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

Por tanto, para cualquier comparación futura que involucre EV03/flat, EV04/hierarchical o D1a, usa las salidas corregidas de Attempt06 cuando exista salida corregida case-level/metrics:

```text
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/
  normative_flat_metrics.json
  normative_flat_case_summary.csv

outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/
  normative_hierarchical_metrics.json
  normative_hierarchical_case_summary.csv

outputs/evaluation/d1a_corrective_0b05c_v0.5/
  d1a_metrics.json
  d1a_case_summary.csv
```

Usa además como trazabilidad de la corrección:

```text
outputs/audits/0b05c_attempt06_execution_v0.5/attempt06_execution_record_v0.5.json
outputs/evaluation/0b05c_corrective_numerical_v0.5/unified_sensitivity_summary_v0.5.json
```

No uses un output supersedido como fuente primaria de un contraste futuro cuando exista su salida Attempt06 corregida.

Antes de clasificar una comparación como `ELIGIBLE`, verifica estáticamente identidad de EVAL/case_id/label entre histórico y la estrategia normativa correspondiente. Si esa comparabilidad no puede probarse con artefactos congelados, clasifica conservadoramente.

#### HE2_B — cobertura profunda

El candidato v0.1 enlazó incorrectamente el componente de candidate-pool a EXP08 split sensitivity. Corrígelo.

La evidencia primaria del conjunto candidato está en:

```text
outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/
  candidate_pool_run_metadata.json
  candidate_pool_metrics.json
  candidate_pool_case_summary.csv
  candidate_pool_strategy_comparison.csv
  candidate_pool_compatibility.json
```

No uses `exp08_split_sensitivity_v01_vs_v02` como fuente primaria de cobertura candidate-pool de HE2_B.

Respeta la pre-especificación registrada en `candidate_pool_run_metadata.json`:

- variantes con `pre_specification = A_historical_defined` pueden evaluarse conforme a su rol congelado;
- `hierarchical_70_dual_backfill_30` está marcado `B_historical_not_formally_frozen_for_v0_2` y NO debe promoverse retrospectivamente a evidencia confirmatoria;
- `diagnostic_union_hierarchical_dual` es `diagnostic_union`, `not_a_ranking = true`; solo puede ser techo/diagnóstico descriptivo, nunca ranking confirmatorio.

Distingue explícitamente ranking temprano de cobertura profunda. Recall/Pool profundo no es MRR ni Top-k temprano.

### G3F01-AUD-F004 — riesgo de deriva del estimando por manejo de DAM

El texto v0.1 dice que la dependencia se maneja “aggregating case-level contributions within DAM before uncertainty estimation”. Esa formulación puede cambiar inadvertidamente el estimando desde una media/proporción por SERIE a una media con igual peso por DAM.

El contrato corregido debe preservar:

```text
PRIMARY_ANALYTICAL_UNIT = SERIE
DEPENDENCE_HANDLING = DAM_CLUSTER_AWARE
```

Si se usa bootstrap por clúster en una ficha posterior:

- remuestrea DAM como clústeres;
- transporta todas las series pertenecientes a cada DAM remuestreada;
- para comparaciones pareadas remuestrea exactamente los mismos DAM/casos en ambas estrategias;
- recomputa el estimando **ponderado por SERIE** sobre las observaciones remuestreadas;
- NO reemplaza el estimando primario por una media no ponderada de medias por DAM salvo que se declare expresamente como estimando secundario distinto.

G3-F01 no debe ejecutar ese bootstrap; solo debe congelar la regla.

Para cada familia `ELIGIBLE`, la regla prospectiva debe ser internamente completa: estimando, pairing/cluster, B/seed si usa resampling, CI, y tratamiento de multiplicidad. Si se planean p-values, define prospectivamente cómo se genera la distribución nula y la corrección múltiple. Si no se planean p-values, no invoques Holm de manera inconexa: define una estrategia coherente de intervalos/decisión múltiple o justifica por qué no aplica.

### G3F01-AUD-F005 — EXP11A/EXP11B y pseudorreplicación

EXP11A continúa:

```text
SENSITIVITY_ONLY
NO_ISOLATED_CAUSAL_BANK_SIZE_EFFECT
```

Registra EVAL=1,056, H100=2,950/28 DAM y los conteos congelados de corridas. H50 D1/D2 puede registrar pairing por seeds tal como aparece en el manifiesto, pero no debe convertirse en efecto causal aislado de tamaño.

Para EXP11B, los 10 H150 y 10 H200 están pareados por seed. No trates `10 runs × 1056 series` como observaciones independientes.

Una clasificación `ELIGIBLE` para inferencia H150 vs H200 solo es válida si el contrato define con precisión:

- cuál es la población/estimando inferencial de interés respecto de las 10 seeds/bancos;
- la unidad inferencial;
- cómo se conserva el pairing por seed;
- cómo se trata la repetición del mismo EVAL dentro de cada run;
- y por qué esa inferencia es defendible.

Si no existe una justificación prospectiva suficiente, clasifica EXP11B como `DESCRIPTIVE_ONLY` de sensibilidad. No inventes una superpoblación de seeds después de ver resultados.

### G3F01-AUD-F006 — HE5 requiere mayor conservadurismo operativo

HE5 permanece exactamente:

```text
Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.
```

Conserva como hechos congelados:

- la matriz integrada contiene 1,056 casos y DAM/SERIE;
- `description_quality_operationalized = 0` / no existe regla frozen case-level para afirmar prevalencia de descripción ambigua/incompleta;
- las categorías de proximidad jerárquica existen en la matriz;
- los buckets de soporte existentes deben describirse literalmente; no redefinas post hoc qué significa “insuficiente”;
- la validez sigue limitada al benchmark interno.

No conviertas una variable no operacionalizada en tasa de prevalencia. No selecciones un umbral de “bajo soporte” después de observar desempeño. Si una relación no tiene estimando/contraste prospectivo defendible, usa `DESCRIPTIVE_ONLY`.

La evidencia de explicación/evidencia puede registrarse como limitación diagnóstica porque el proyecto metodológico distingue fallas de datos, recuperación, evidencia y explicación, pero no la presentes como una quinta proposición literal independiente de HE5.

### G3F01-AUD-F007 — acceso de SRC-01 y desviación de gobernanza

La ficha G3-F01 exigía leer el proyecto aprobado y bloquear si no estaba accesible. Prompt76 autorizó usar la transcripción congelada aprobada porque Codex no tenía los bytes PDF montados.

NO falsifiques acceso directo al PDF.

Registra explícitamente:

```text
SRC01_DIRECT_PDF_BYTES_READ_BY_CODEX = false
SRC01_FROZEN_TRANSCRIPTION_USED = true
SRC01_FROZEN_TRANSCRIPTION_BLOB = 52c45948bbc085a25faf4df850ae15e6ca682d17
SRC01_AUTHOR_APPROVAL_BLOB = db5cd447df1d85ee0f9d271e2a85af66e050aea1
SRC01_EXTERNAL_AUDITOR_DIRECT_SOURCE_VERIFICATION = true
SRC01_HYPOTHESIS_TEXT_MISMATCH = false
SOURCE_ACCESS_GOVERNANCE_DEVIATION = DOCUMENTED
SCIENTIFIC_RERUN_REQUIRED_FOR_SRC01 = false
```

No cambies HE2/HE5. La IA Experimental verificó directamente el proyecto aprobado y confirmó que los textos congelados coinciden; la desviación de acceso debe permanecer visible para trazabilidad.

### G3F01-AUD-F008 — activación administrativa no materializada en el registro de fichas

`04_REGISTRO_ESTADO_FICHAS.md` establece que al activar una ficha deben añadirse commit de activación, refs, prompt, fecha, auditoría y resultado. Prompt76 no modificó esa rama y el registro continúa mostrando G3-F01 únicamente como `PROSPECTIVE`.

En Prompt79 **NO modifiques todavía `docs/fichas-grupos-3-8`**. Registra en ambos artefactos:

```text
G3_F01_ACTIVATION_REGISTRY_RECONCILIATION = REQUIRED_BEFORE_CLOSURE
G3_F01_ACTIVATION_WAS_USER_AUTHORIZED = true
G3_F01_ACTIVATION_REGISTRY_WAS_NOT_MATERIALIZED_PREEXECUTION = true
```

La reconciliación del registro será un gate administrativo posterior a la aprobación externa del contrato corregido. No reescribas retrospectivamente la historia de la ejecución.

---

## 3. Corrección del candidato

Trabaja exclusivamente sobre:

```text
codex/group3-f01-analytical-contract-v01
```

cuyo HEAD inicial debe ser:

```text
c727da94f5d38f530a839631c3ac9e427a1eb27e
```

No rebase, no amend, no squash y no force.

Crea **un único segundo commit correctivo** que modifique exclusivamente:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

No añadas ni modifiques ningún otro path científico.

Al finalizar, respecto de `main=a33fc7e...` debe cumplirse:

```text
commits_ahead = 2
commits_behind = 0
changed_path_count = 2
changed_paths =
  docs/analysis/group3/g3_analytical_contract_v0.1.md
  outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

El primer commit `c727da94...` debe permanecer intacto como evidencia histórica del candidato inicial.

---

## 4. Reglas de clasificación y cierre prospectivo

Las únicas clasificaciones terminales siguen siendo:

```text
ELIGIBLE
DESCRIPTIVE_ONLY
NOT_ESTIMABLE
NOT_APPLICABLE
```

No uses:

```text
SUPPORTED
PARTIALLY_SUPPORTED
REJECTED
SIGNIFICANT
NONSIGNIFICANT
```

No decidas HE2 ni HE5.

No selecciones un contraste, bucket, profundidad, variante o prueba porque produzca un resultado favorable.

Para cada familia, si falta un elemento necesario para inferencia prospectiva, degrada conservadoramente a `DESCRIPTIVE_ONLY` o `NOT_ESTIMABLE`; no rellenes el hueco por inferencia.

---

## 5. Prohibiciones absolutas

Durante Prompt79 NO:

- ejecutes tests estadísticos;
- calcules p-values;
- calcules nuevos intervalos;
- calcules tamaños de efecto;
- recalcules Top-k/MRR/Recall/Pool;
- ejecutes retrieval, BM25, dense retrieval o candidate generation;
- reejecutes Attempt06;
- reejecutes EXP11A/EXP11B/EXP12;
- abras EXP12;
- cambies seeds/thresholds/poblaciones/exclusiones;
- cambies HE2/HE5;
- modifiques `main`;
- modifiques el Plan Maestro;
- modifiques `article/main-manuscript`;
- modifiques `docs/fichas-grupos-3-8`;
- avances a G3-F02.

---

## 6. Validaciones obligatorias antes del commit

Verifica estáticamente, sin recomputar resultados:

1. que todos los `primary_paths` declarados existen en `main=a33fc7e...`;
2. que cualquier path Attempt06 usado corresponde a la rama correctiva Decision 906 vigente;
3. que los case summaries usados para comparaciones inferenciales futuras contienen identificadores que permiten pairing y DAM;
4. que candidate-pool usa los artefactos Phase E reales y no EXP08;
5. que D1a corregido aparece en el inventario HE2_A cuando metodológicamente comparable;
6. que `Top-1/3/5/10/MRR` quedan identificados como métricas primarias aprobadas de desempeño;
7. que Recall/Pool quedan separados como cobertura profunda;
8. que ningún componente usa el split 3,000/1,006;
9. que EXP12 sigue `NOT_ESTIMABLE`;
10. que no se introdujo ninguna inferencia ejecutada.

Si un path declarado no existe o una comparabilidad crítica no puede verificarse:

```text
STOP / CORRECTIVE_CONTRACT_SOURCE_OR_COMPARABILITY_FAILURE
```

---

## 7. Publicación y persistencia administrativa

Publica mediante push normal la rama científica corregida. No force.

Después, vuelve a:

```text
codex/prompts-temporary
```

y crea únicamente:

```text
codex_prompts_tmp/79_RESPUESTA_CORREGIR_G3_F01_CONTRATO_ANALITICO_TRAS_AUDITORIA_EXTERNA.md
```

El commit administrativo debe contener exclusivamente esa respuesta.

---

## 8. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT79 = COMPLETED | STOP

SOURCE_MAIN =
SOURCE_PLAN =
SOURCE_FICHAS =
ARTICLE_HEAD_OBSERVED =
SRC01_GROUND_TRUTH_BLOB_MATCH = true|false
SRC01_AUTHOR_APPROVAL_BLOB_MATCH = true|false

G3_F01_BRANCH =
G3_F01_INITIAL_COMMIT = c727da94f5d38f530a839631c3ac9e427a1eb27e
G3_F01_CORRECTIVE_COMMIT =
G3_F01_FINAL_REMOTE_HEAD =
G3_F01_COMMITS_AHEAD =
G3_F01_COMMITS_BEHIND =
G3_F01_CHANGED_PATH_COUNT =
G3_F01_CHANGED_PATHS =

EVIDENCE_FAMILY_COUNT =
ELIGIBLE_COUNT =
DESCRIPTIVE_ONLY_COUNT =
NOT_ESTIMABLE_COUNT =
NOT_APPLICABLE_COUNT =

HE2_A_NORMATIVE_STRATEGIES_INVENTORIED =
HE2_B_CANDIDATE_POOL_PRIMARY_SOURCE_CORRECTED = true|false
ATTEMPT06_ONLY_FOR_0B05C = true|false
D1A_CORRECTED_INCLUDED_WHERE_APPLICABLE = true|false
SERIE_ESTIMAND_PRESERVED = true|false
DAM_CLUSTER_HANDLING_PRESERVES_SERIE_WEIGHTING = true|false
EXP11B_PSEUDOREPLICATION_PROHIBITED = true|false
HE5_POSTHOC_LOW_SUPPORT_THRESHOLD_CREATED = false
SRC01_SOURCE_ACCESS_DEVIATION_DOCUMENTED = true|false
ACTIVATION_REGISTRY_RECONCILIATION_REQUIRED = true

INFERENTIAL_CALCULATION_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
SCIENTIFIC_EXPERIMENT_REEXECUTED = false
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false

G3_F01_EXTERNAL_AUDIT = PENDING_REAUDIT
G3_F02_AUTHORIZED = NO
BLOCKERS =
WARNINGS =
```

Detente ahí.