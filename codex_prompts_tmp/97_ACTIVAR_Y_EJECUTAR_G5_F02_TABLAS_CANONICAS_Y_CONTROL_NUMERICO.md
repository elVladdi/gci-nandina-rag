# PROMPT 97 — ACTIVAR Y EJECUTAR G5-F02: TABLAS CANÓNICAS Y CONTROL NUMÉRICO

## 0. Naturaleza, alcance y autorización

Esta ejecución corresponde exclusivamente a **G5-F02 — Tablas canónicas y control numérico**.

Estado canónico al diseñar este prompt:

```text
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
GROUP5 = IN_PROGRESS
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

El usuario dejó una instrucción permanente de continuidad automática del flujo experimental. La **invocación explícita de este Prompt97** constituye autorización únicamente para activar y ejecutar G5-F02.

Esta ejecución autoriza:

1. activar administrativamente G5-F02;
2. materializar las tablas científicas definidas y aprobadas por G5-F01;
3. generar una transformación determinista y versionada para construir esas tablas a partir de outputs congelados;
4. generar un ledger y control numérico reproducible `celda/valor → archivo fuente → campo/row-id`;
5. publicar un candidato G5-F02 pendiente de auditoría externa.

Esta ejecución **no autoriza**:

- recalcular métricas científicas;
- generar nueva inferencia, bootstrap, intervalos o p-values;
- redecidir HE2 o HE5;
- alterar la arquitectura aprobada de G5-F01;
- añadir o eliminar tablas por conveniencia narrativa;
- usar resultados supersedidos;
- materializar EXP12 como rendimiento;
- modificar artículo o tesis;
- activar ni ejecutar G5-F03;
- cerrar Grupo 5;
- iniciar Grupo 6.

---

## 1. Preflight obligatorio y refs congelados

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = d5729887f47c36d8cf42d87090c40f9668e5ae84
origin/docs/plan-maestro-temporal-2026-08-31 = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
origin/docs/fichas-grupos-3-8 = 86211dee649f2676f4cb3747ba116da147a7d37f
origin/article/main-manuscript = b2b338493f4045a772e6bbb40a606fc63cea9c79
```

Gobernanza inmediata:

```text
PROMPT94_SOURCE = 37edbc97610395ef655379628d63f0d8847d117c
PROMPT94_RESPONSE = 9442027fc0d96ee28fe9acd39f5ab473078742a4
PROMPT95_SOURCE = c36b0d18c4d3588c92d95c1c17596384e2697e2f
PROMPT95_RESPONSE = 9de82202002cfbb7520813a22305ad3e0b6415a0
PROMPT96_SOURCE = fc7e84798b059ea82ca4b3a4fb10ccf6a551a9ef
PROMPT96_RESPONSE = fd9c11a0ca45e19f688f874396de2fa5e7f961d8
G5_F01_INTEGRATION_COMMIT = d5729887f47c36d8cf42d87090c40f9668e5ae84
G5_F01_FICHAS_CLOSURE = 86211dee649f2676f4cb3747ba116da147a7d37f
G5_F01_PLAN_RECONCILIATION = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
```

Ficha rectora:

```text
docs/fichas/grupos_3_8/grupo_5/G5_F02_TABLAS_CANONICAS_Y_CONTROL_NUMERICO.md
blob = e7468e6815af04b5719ea451fdab326e5074d33e
```

Ficha siguiente, solo para preservar frontera de autorización:

```text
docs/fichas/grupos_3_8/grupo_5/G5_F03_ANEXOS_Y_CIERRE.md
blob = 982f6be22f7cae81e9ecdea3ae1940b57db8b085
```

Artefactos rectores G5-F01 ya integrados:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245
```

La rama editorial es **solo lectura / observacional**. Si avanza concurrentemente, registra el HEAD final como advertencia no bloqueante siempre que Prompt97 no la modifique.

Si `main`, Plan o fichas presentan drift no explicado:

```text
STOP / G5_F02_REF_DRIFT
```

---

## 2. Activación administrativa prospectiva obligatoria

Antes de generar tablas o scripts, trabaja únicamente en:

```text
branch = docs/fichas-grupos-3-8
base = 86211dee649f2676f4cb3747ba116da147a7d37f
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo para dejar:

```text
G5-F01 = CLOSED / APPROVED
G5-F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G5-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP5 = IN_PROGRESS
```

Añade bloque de activación con, como mínimo:

```text
FICHA = G5-F02
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT97_EXPLICIT_EXECUTION / STANDING_CONTINUATION_INSTRUCTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
MAIN_AT_ACTIVATION = d5729887f47c36d8cf42d87090c40f9668e5ae84
PLAN_AT_ACTIVATION = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
FICHAS_AT_ACTIVATION = 86211dee649f2676f4cb3747ba116da147a7d37f
ARTICLE_HEAD_OBSERVED = <HEAD observado>
PROMPT97_COMMIT = <commit fuente invocado>
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP5 = IN_PROGRESS
G5_F03_AUTHORIZED = false
```

Haz un único commit administrativo y push normal.

Si no puede publicarse:

```text
STOP / G5_F02_ACTIVATION_PUBLICATION_FAILED
```

---

## 3. Objetivo exacto

La ficha G5-F02 exige:

> Materializar las tablas científicas desde outputs congelados y verificar que cada cifra reproduce exactamente la fuente aprobada.

G5-F02 **no decide qué mostrar**. Esa decisión ya fue congelada en G5-F01.

La regla de materialización es:

```text
MATERIALIZE = todas y solo las entradas de presentation_registry
              donde materialize_in_g5_f02 = true
```

En el registro aprobado deben resultar exactamente **9 estructuras tabulares**:

```text
G5-MAIN-01
G5-MAIN-02
G5-SECONDARY-01
G5-SECONDARY-02
G5-APPENDIX-01
G5-APPENDIX-02
G5-APPENDIX-03
G5-APPENDIX-04
G5-APPENDIX-05
```

Los destinos `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON` **no** generan tablas numéricas en esta ficha.

No agregues tablas nuevas aunque parezcan útiles. No elimines ninguna de las nueve por longitud, favorabilidad o complejidad.

---

## 4. Contrato científico congelado

Preserva exactamente:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION when dependency applies
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_SERIES = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42

HE2 = SUPPORTED
HE5 = INCONCLUSIVE

EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

También:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_CORRECTNESS
AUDITABLE_EXPLANATION != LEGAL_CORRECTNESS
```

Las 11 limitaciones no bloqueantes de Grupo 2B siguen vigentes cuando correspondan.

---

## 5. Precedencia de fuentes y política de números

La arquitectura G5-F01 integrada es la autoridad sobre:

- qué tabla existe;
- rol científico;
- columnas/contenido requerido;
- denominador;
- unidad;
- incertidumbre;
- cualificaciones;
- fuentes permitidas.

Para **cada valor científico** materializado:

1. usa el `source_paths` y `source_blobs_or_row_ids` del registro G5-F01;
2. verifica que el blob de la fuente en `main` coincida con el blob congelado;
3. copia el valor ya aprobado desde su campo/row-id;
4. no uses un output alternativo si el registro no lo autoriza;
5. registra la trazabilidad exacta en el ledger de crosscheck.

No redondees silenciosamente. Si se aplica formato decimal de presentación, conserva en el ledger:

```text
source_value_exact
rendered_value
render_rule
```

La representación puede formatearse para lectura, pero el **valor científico fuente no cambia**.

No copies manualmente números sin una ruta de transformación reproducible.

---

## 6. Regla crítica G5-MAIN-01 — estimando e incertidumbre

La corrección aprobada de G5-F01 es obligatoria.

Para cada comparación y métrica, separa explícitamente:

```text
historical_observed_value
comparator_observed_value
paired_difference_historical_minus_comparator
frozen_99pct_ci_lower_for_paired_difference
frozen_99pct_ci_upper_for_paired_difference
```

Los campos de G3-F03:

```text
point_estimate
ci_lower
ci_upper
```

pertenecen al estimando:

```text
paired_difference_historical_minus_comparator
```

No pertenecen a `historical_observed_value` ni a `comparator_observed_value`.

Está prohibido:

- colocar el CI de la diferencia junto a un valor absoluto de brazo de manera que parezca su CI;
- calcular nuevos CI por brazo;
- recalcular el contraste como fuente científica primaria.

Puede realizarse una resta únicamente como **crosscheck aritmético secundario** del valor congelado ya materializado. Si se hace, debe registrarse como `VERIFICATION_ONLY` y nunca reemplazar la fuente aprobada del `paired_difference`.

Condiciones finales:

```text
HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
```

---

## 7. Reglas específicas de las demás tablas

### G5-MAIN-02

Materializa Recall@100, Recall@200, diferencia pareada y el CI congelado del contraste aprobado. `Pool@200` puede figurar únicamente como contexto y no como segundo contraste confirmatorio.

### G5-SECONDARY-01

Materializa Phase E con el rol `DESCRIPTIVE_ONLY`. No generes CI ni test. Mantén denominadores literales por pool/variante/profundidad.

### G5-SECONDARY-02

Materializa componentes descriptivos HE5 usando categorías literales congeladas. No inventes un threshold de “concentración” ni conviertas un bucket en “insuficiente” si la fuente no lo define así. `HE5` permanece `INCONCLUSIVE`.

### G5-APPENDIX-01

Top-50 es suplementario y no participa en la decisión HE2. Usa únicamente los intervalos suplementarios congelados.

### G5-APPENDIX-02

EXP11A es sensibilidad conjunta tamaño/composición. No presentes una tendencia causal o monotónica del tamaño. No generes inferencia nueva.

### G5-APPENDIX-03

EXP11B representa diez pares de seeds observados. No trates `10 × 1056` como observaciones inferenciales independientes y no infieras a una superpoblación de seeds.

### G5-APPENDIX-04

Usa exclusivamente Attempt06 vigente:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
OVERALL = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

Attempts 03/04/05 e interpretaciones supersedidas no pueden aportar ningún valor final.

### G5-APPENDIX-05

La unión diagnóstica Phase E es techo descriptivo/diagnóstico, no rendimiento de producción ni evidencia confirmatoria.

### EXP12

No existe tabla G5-F02 de EXP12.

Debe cumplirse:

```text
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0
```

---

## 8. Transformación reproducible obligatoria

Versiona un script determinista:

```text
scripts/results/group5/materialize_g5_tables_v0_1.py
```

El script debe:

1. leer exclusivamente fuentes aprobadas existentes en el checkout basado en `main` congelado;
2. verificar blobs/hashes o equivalentes antes de usar las fuentes;
3. leer `g5_table_registry_v0.1.json` y seleccionar exactamente `materialize_in_g5_f02=true`;
4. producir exactamente las nueve tablas CSV canónicas definidas en la sección 9;
5. producir el Markdown agregado definido en la sección 9 a partir de esos CSV;
6. producir el crosscheck JSON con ledger de trazabilidad;
7. fallar si una fuente/row-id/campo requerido no existe;
8. fallar si detecta fuente supersedida;
9. fallar si una tabla numérica intenta materializar EXP12;
10. no acceder a red, LLM, APIs externas ni rama editorial.

La generación debe ser determinista sobre el mismo checkout y las mismas fuentes.

---

## 9. Outputs científicos-documentales exactos

Crea exactamente estos **12 paths nuevos** en la rama candidata:

```text
scripts/results/group5/materialize_g5_tables_v0_1.py

docs/results/group5/g5_canonical_tables_v0.1.md

outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv
outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv
outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv

outputs/results/group5/g5_numeric_crosscheck_v0.1.json
```

No crees archivos adicionales en el candidato.

Los CSV son la materialización canónica de cada tabla. El Markdown es una representación humana generada desde los CSV por el script; no es una segunda fuente científica independiente.

---

## 10. Contrato del crosscheck JSON

`outputs/results/group5/g5_numeric_crosscheck_v0.1.json` debe incluir como mínimo:

```text
artifact_id
status
ficha
main_base
plan_snapshot
fichas_activation_commit
prompt97_commit
script_path
script_sha256_or_git_blob
source_registry_snapshot
canonical_table_registry
cell_value_ledger
markdown_render_checks
validation
```

### 10.1 Ledger obligatorio

Para cada valor científico materializado registra, como mínimo:

```text
presentation_id
canonical_csv_path
row_key
column_name
rendered_value
source_value_exact
source_path
source_blob
source_row_or_record_id
source_field
transformation_type
render_rule
verification_status
```

`transformation_type` solo puede usar categorías como:

```text
DIRECT_COPY
DIRECT_COPY_WITH_PRESENTATION_FORMATTING
VERIFICATION_ONLY
TEXT_LABEL_FROM_FROZEN_REGISTRY
```

Ningún valor científico puede tener origen `MANUAL`, `INFERRED`, `RECOMPUTED_METRIC` o equivalente.

### 10.2 Control de Markdown

Para cada tabla del Markdown registra:

```text
presentation_id
source_csv
csv_blob_or_sha256
markdown_row_count
csv_row_count
values_match_csv = true
```

---

## 11. Política de discrepancias

Una discrepancia es cualquier caso en el que:

- el valor materializado difiere de la fuente aprobada fuera de una regla de formato declarada;
- el denominador difiere;
- el nivel de CI difiere;
- el CI se asocia al estimando incorrecto;
- se usa un row-id/campo distinto al autorizado sin justificación gobernada;
- Markdown y CSV discrepan;
- se usa una fuente supersedida.

No “corrijas” la fuente científica desde G5-F02.

Si detectas una discrepancia en una fuente aprobada:

```text
STOP / G5_F02_SOURCE_DISCREPANCY
```

y documenta el caso sin modificar el resultado científico.

Condición de PASS:

```text
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
```

---

## 12. RPRE obligatorio antes de publicar candidato

Exige `PASS` para:

```text
RPRE_G5_F02_SOURCE_CONTRACT
RPRE_G5_F02_G5_F01_CLOSED
RPRE_G5_F02_NINE_TABLE_ARCHITECTURE_FROZEN
RPRE_G5_F02_NO_NEW_SCIENCE
RPRE_G5_F02_NO_RECOMPUTATION
RPRE_G5_F02_NO_NEW_INFERENCE
RPRE_G5_F02_NO_NEW_CI
RPRE_G5_F02_HE2A_ESTIMAND_CI_BINDING
RPRE_G5_F02_HE2_HE5_PRESERVATION
RPRE_G5_F02_ATTEMPT06_CURRENT_ONLY
RPRE_G5_F02_EXP11A_NONCAUSAL
RPRE_G5_F02_EXP11B_DESCRIPTIVE_ONLY
RPRE_G5_F02_EXP12_NO_PERFORMANCE_TABLE
RPRE_G5_F02_NO_SUPERSEDED_NUMERIC_SOURCE
RPRE_G5_F02_CELL_LEDGER_COMPLETE
RPRE_G5_F02_MARKDOWN_FROM_CSV
RPRE_G5_F02_ARTICLE_READONLY
RPRE_G5_F03_NOT_STARTED
```

Si falla cualquiera:

```text
STOP / G5_F02_RPRE_FAILED
```

---

## 13. Rama candidata y topología

Crea desde `origin/main` exactamente:

```text
branch = codex/group5-f02-canonical-tables-v01
base = d5729887f47c36d8cf42d87090c40f9668e5ae84
```

Debe contener exactamente **un commit científico-documental** y los **12 paths** definidos en la sección 9.

Al final:

```text
G5_F02_COMMITS_AHEAD = 1
G5_F02_COMMITS_BEHIND = 0
G5_F02_CHANGED_PATH_COUNT = 12
```

No modifiques ningún archivo previo de G3/G4/G5-F01, configuración experimental, Plan, artículo o tesis dentro de la rama candidata.

---

## 14. Validaciones obligatorias

El crosscheck JSON y la verificación terminal deben demostrar, como mínimo:

```text
EXPECTED_CANONICAL_TABLE_COUNT = 9
MATERIALIZED_CANONICAL_TABLE_COUNT = 9
MISSING_CANONICAL_TABLE_COUNT = 0
UNAUTHORIZED_EXTRA_TABLE_COUNT = 0

G3_EVIDENCE_FAMILY_EXPECTED_COUNT = 16
G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G4_CONTROLLED_CLAIM_EXPECTED_COUNT = 18
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18

UNTRACED_SCIENTIFIC_VALUE_COUNT = 0
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
DENOMINATOR_MISMATCH_COUNT = 0
UNIT_MISMATCH_COUNT = 0
CI_LEVEL_MISMATCH_COUNT = 0

HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0

EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
EXPERIMENTS_RERUN = false
RETRIEVAL_EXECUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
G5_F03_STARTED = false
```

No reduzcas artificialmente universos o conteos para obtener PASS.

---

## 15. Estado del candidato

Todos los outputs G5-F02 deben quedar gobernados como:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G5-F02
GROUP5_CLOSED = false
G5_F03_AUTHORIZED = false
```

No integres a `main` durante Prompt97.

---

## 16. Actualización administrativa postejecución

Después de publicar y validar el candidato, actualiza exclusivamente:

```text
branch = docs/fichas-grupos-3-8
base = <commit de activación Prompt97>
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Deja:

```text
G5-F01 = CLOSED / APPROVED
G5-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G5-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP5 = IN_PROGRESS
```

Añade bloque con al menos:

```text
FICHA = G5-F02
PROMPT97_COMMIT = <source>
ACTIVATION_COMMIT = <activation>
CANDIDATE_COMMIT = <candidate>
CANDIDATE_PARENT = d5729887f47c36d8cf42d87090c40f9668e5ae84
CHANGED_PATH_COUNT = 12
MATERIALIZED_CANONICAL_TABLE_COUNT = 9
UNTRACED_SCIENTIFIC_VALUE_COUNT = 0
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP5 = IN_PROGRESS
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false
PENDING_EXTERNAL_AUDIT = true
```

No actualices todavía el Plan Maestro. Se reconciliará después de auditoría externa e integración/cierre de G5-F02.

---

## 17. Verificación final

Tras todos los push, ejecuta `git fetch origin` y verifica:

```text
origin/main = d5729887f47c36d8cf42d87090c40f9668e5ae84
origin/docs/plan-maestro-temporal-2026-08-31 = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8

G5_F02_COMMITS_AHEAD = 1
G5_F02_COMMITS_BEHIND = 0
G5_F02_CHANGED_PATH_COUNT = 12

EXPECTED_CANONICAL_TABLE_COUNT = 9
MATERIALIZED_CANONICAL_TABLE_COUNT = 9
UNAUTHORIZED_EXTRA_TABLE_COUNT = 0
UNTRACED_SCIENTIFIC_VALUE_COUNT = 0
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED = false
GROUP5 = IN_PROGRESS
G5_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_STARTED = false
```

Si la rama editorial avanzó concurrentemente, registra el HEAD final; no lo trates como bloqueo mientras Prompt97 no la haya modificado.

---

## 18. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/97_RESPUESTA_ACTIVAR_Y_EJECUTAR_G5_F02_TABLAS_CANONICAS_Y_CONTROL_NUMERICO.md
```

El commit de respuesta debe añadir únicamente ese archivo.

Reporte terminal mínimo:

```text
PROMPT97 = COMPLETED

PREFLIGHT_MAIN = d5729887f47c36d8cf42d87090c40f9668e5ae84
PREFLIGHT_PLAN = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
PREFLIGHT_FICHAS = 86211dee649f2676f4cb3747ba116da147a7d37f
ARTICLE_HEAD_PREFLIGHT = ...
PROMPT97_COMMIT = ...

ACTIVATION_COMMIT = ...
CANDIDATE_BRANCH = codex/group5-f02-canonical-tables-v01
CANDIDATE_COMMIT = ...
CANDIDATE_PARENT = d5729887f47c36d8cf42d87090c40f9668e5ae84
CANDIDATE_COMMITS_AHEAD = 1
CANDIDATE_COMMITS_BEHIND = 0
CANDIDATE_CHANGED_PATH_COUNT = 12
SCRIPT_BLOB = ...
CANONICAL_TABLES_MD_BLOB = ...
NUMERIC_CROSSCHECK_BLOB = ...

EXPECTED_CANONICAL_TABLE_COUNT = 9
MATERIALIZED_CANONICAL_TABLE_COUNT = 9
UNAUTHORIZED_EXTRA_TABLE_COUNT = 0
UNTRACED_SCIENTIFIC_VALUE_COUNT = 0
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
DENOMINATOR_MISMATCH_COUNT = 0
UNIT_MISMATCH_COUNT = 0
CI_LEVEL_MISMATCH_COUNT = 0
HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0
EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
ARTICLE_MODIFIED_BY_PROMPT97 = false

POSTEXEC_FICHAS_COMMIT = ...
G5_F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
G5_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_STARTED = false

ARTICLE_HEAD_FINAL_OBSERVED = ...
BLOCKERS = NONE
WARNINGS = ...
```
