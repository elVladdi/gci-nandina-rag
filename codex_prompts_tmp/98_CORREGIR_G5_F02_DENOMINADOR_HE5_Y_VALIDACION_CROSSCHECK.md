# PROMPT 98 — CORREGIR G5-F02: DENOMINADOR HE5 Y VALIDACIÓN REAL DEL CROSSCHECK

## 0. Naturaleza y alcance

Esta ejecución corrige exclusivamente defectos localizados detectados por auditoría externa sobre el candidato G5-F02 generado por Prompt97.

Dictamen gobernante:

```text
PROMPT97_EXTERNAL_AUDIT = PASS_WITH_CORRECTION_REQUIRED
G5_F02_SCIENTIFIC_CONTENT = SUBSTANTIVELY_PASS
G5_F02_SOURCE_FIDELITY = FAIL_LOCALIZED
G5_F02_CROSSCHECK_IMPLEMENTATION = FAIL_LOCALIZED
SCIENTIFIC_RECOMPUTATION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
CORRECTION_SCOPE = HE5_HIERARCHY_DENOMINATOR_AND_CROSSCHECK_VALIDATION_ONLY
G5_F02 = NOT_APPROVABLE_FOR_INTEGRATION_YET
GROUP5 = IN_PROGRESS
G5_F03_AUTHORIZED = false
```

La corrección no cambia resultados, métricas, hipótesis, intervalos, jerarquía de presentación ni las nueve estructuras tabulares aprobadas. Corrige:

1. tres denominadores no soportados en `G5-SECONDARY-02`;
2. la lógica de validación para que los contadores de discrepancias se calculen realmente contra las fuentes/artefactos y no se asignen como constantes;
3. la generación del Markdown para que se lea desde los CSV canónicos ya escritos, tal como exigía Prompt97.

No autoriza integración a `main`, actualización del Plan Maestro, nueva ciencia, nueva inferencia, recalcular métricas, modificar artículo/tesis, activar G5-F03 ni cerrar Grupo 5.

---

## 1. Refs congelados

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = d5729887f47c36d8cf42d87090c40f9668e5ae84
origin/docs/plan-maestro-temporal-2026-08-31 = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
origin/docs/fichas-grupos-3-8 = 1927ca9496615f19068812905afe4abe9800f979
origin/codex/group5-f02-canonical-tables-v01 = 9a8ca23ef607b5975b46a4336e033fc44ebe9453
origin/article/main-manuscript = b2b338493f4045a772e6bbb40a606fc63cea9c79
```

Gobernanza inmediata:

```text
PROMPT97_SOURCE = 5b5de5acc62cbf5dfd08f044870f815369ee6c96
PROMPT97_RESPONSE = 8596fe65e5aa50f6b245f13450fc4a64ae5397a8
PROMPT97_ACTIVATION = bab760ec7ac3494a792e9c212fb6b887e4c659c0
PROMPT97_POSTEXEC_FICHAS = 1927ca9496615f19068812905afe4abe9800f979
PROMPT97_CANDIDATE_V01 = 9a8ca23ef607b5975b46a4336e033fc44ebe9453
```

Blobs v01 relevantes:

```text
V01_SCRIPT_BLOB = f580bed011404614ad87347936be60102ae2027e
V01_CANONICAL_TABLES_MD_BLOB = 9f1b55772e603611cb02c9111feeb1285b9b42de
V01_NUMERIC_CROSSCHECK_BLOB = 31071ccebe5032aa7f894a8ebbb492408b89431d
V01_G5_SECONDARY_02_BLOB = 6a4951d46d16b878b350511342093673dff2b86b
```

Artefactos G5-F01 rectores permanecen inmutables:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245
```

Fuentes decisivas para esta corrección:

```text
outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_hierarchy_errors_v0.2.csv
blob = b5bd099114e7262f316dfc846b867bec9e7f176d

outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
blob = c63619b56a07e6b6d7be78b515d941ec3b205c41
```

Si `main`, Plan o fichas presentan drift no explicado:

```text
STOP / G5_F02_CORRECTION_REF_DRIFT
```

La rama editorial sigue siendo solo observacional.

---

## 2. Observabilidad del workspace local

No existe todavía una ruta local canónica fijada por el usuario. Por ello, **no inventes una ruta** ni afirmes que trabajas en la carpeta local personal del usuario.

Antes de cualquier cambio registra:

```text
WORKSPACE_ROOT_OBSERVED = <git rev-parse --show-toplevel>
WORKSPACE_ORIGIN_URL = <git remote get-url origin>
WORKSPACE_INITIAL_BRANCH = <git branch --show-current>
WORKSPACE_INITIAL_HEAD = <git rev-parse HEAD>
WORKSPACE_INITIAL_DIRTY_COUNT = <git status --porcelain | conteo>
WORKTREE_LIST_OBSERVED = <git worktree list --porcelain resumido>
```

Verifica que `origin` corresponda a `elVladdi/gci-nandina-rag`.

No crees un clon o worktree adicional **solo** para esta corrección si el workspace actual ya permite ejecutar el flujo. Si el entorno gestionado por Codex usa un workspace aislado/temporal, repórtalo sin afirmar persistencia en una carpeta local del usuario.

Al final reporta nuevamente root, branch, HEAD y dirty count. Hasta que el usuario fije una ruta canónica, debe constar:

```text
USER_CANONICAL_LOCAL_PATH_FROZEN = false
LOCAL_PERSISTENCE_IN_USER_FOLDER_ASSERTED = false
```

---

## 3. Defecto D98-01 — denominadores HE5 jerárquicos fabricados

En el candidato v01, `G5-SECONDARY-02` materializó:

```text
SAME_CHAPTER denominator = 147
SAME_HS4     denominator = 284
SAME_HS6     denominator = 87
```

Esto no está soportado por la fuente congelada.

La fuente `he5_historical_hierarchy_errors_v0.2.csv` solo contiene:

```text
historical_error_hierarchy,errors
SAME_CHAPTER,147
SAME_HS4,284
SAME_HS6,87
```

No contiene campo denominador.

Además, las filas canónicas G3:

```text
G3F02-0529
G3F02-0530
G3F02-0531
```

tienen:

```text
metric_name = error_count
observed_numerator = 147 / 284 / 87
observed_denominator = <vacío>
observed_value = 147 / 284 / 87
value_unit = count
```

Por tanto, los conteos de categoría **no pueden duplicarse como denominador**.

### Corrección obligatoria

Para las tres filas `HE5-HIER-*`:

```text
denominator = ""
frozen descriptive metric = 147 / 284 / 87
metric name = error_count
```

El campo `denominator` debe preservar literalmente la ausencia de denominador congelado.

No sustituyas el vacío por:

- 147/284/87;
- 518;
- 1056;
- porcentajes derivados;
- `0`;
- `NA` que pueda interpretarse como valor medido;
- ningún denominador inferido.

La ausencia debe explicarse en el Markdown como metadato de fuente: para estas tres categorías se materializaron conteos descriptivos y el registro G3 no contiene `observed_denominator`.

No calcules proporciones jerárquicas nuevas.

Debe cumplirse:

```text
HE5_HIERARCHY_ROW_COUNT = 3
HE5_HIERARCHY_ROWS_WITH_FROZEN_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_NONEMPTY_RENDERED_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_FABRICATED_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_ERROR_COUNT_VALUES_PRESERVED = true
```

---

## 4. Defecto D98-02 — contadores de crosscheck declarados sin cálculo real

En v01, varios contadores de validación se asignaron directamente a `0`, entre ellos:

```text
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT
MARKDOWN_CSV_VALUE_MISMATCH_COUNT
DENOMINATOR_MISMATCH_COUNT
UNIT_MISMATCH_COUNT
CI_LEVEL_MISMATCH_COUNT
```

Esto permitió que `DENOMINATOR_MISMATCH_COUNT = 0` coexistiera con los tres denominadores no soportados.

### Corrección obligatoria

El script v02 debe derivar estos contadores mediante comprobaciones ejecutadas sobre fuentes, ledger y outputs generados.

Como mínimo:

1. **denominadores:** comparar cada denominador materializado contra el estado congelado de la fuente/registro autorizado; el vacío esperado de G3F02-0529:0531 debe verificarse como vacío y no como mismatch;
2. **valores científicos:** para cada entrada `DIRECT_COPY`, reabrir la fuente y verificar que el valor renderizado corresponde al campo/row-id registrado, salvo regla de formato explícita;
3. **fuentes supersedidas:** comprobar que todos los paths científicos usados pertenecen a los paths autorizados por el registro G5-F01 y que Attempt06 es el único estado 0B-05C usado;
4. **unidades:** verificar las unidades cuando estén gobernadas por G3/F01; no inventar unidad ausente;
5. **CI:** verificar nivel y asociación al estimando para HE2_A, HE2_B y Top-50 contra G3-F03;
6. **ledger:** ninguna entrada científica puede declararse `PASS` sin comprobación de la fuente correspondiente.

No basta con asignar literales `0` o `true` en el diccionario de validación.

Añade:

```text
VALIDATION_COUNTERS_COMPUTED_FROM_CHECKS = true
HARDCODED_PASS_VALIDATION_COUNTER_COUNT = 0
```

Los flags científicos que expresan una condición gobernada (`HE2`, `HE5`, etc.) pueden seguir siendo constantes congeladas; los **contadores de discrepancia** deben provenir de comprobaciones.

---

## 5. Defecto D98-03 — Markdown debe generarse desde los CSV

Prompt97 exigía que el Markdown agregado se produjera **a partir de los CSV canónicos**.

En v01 el script escribió los CSV, pero construyó el Markdown usando nuevamente la estructura `tables` en memoria.

### Corrección obligatoria

Después de escribir cada CSV:

1. vuelve a abrir el CSV canónico desde disco;
2. usa esas filas re-leídas como única fuente para renderizar la tabla correspondiente en `g5_canonical_tables_v0.1.md`;
3. vuelve a leer/validar el CSV para `markdown_render_checks`;
4. calcula realmente `MARKDOWN_CSV_VALUE_MISMATCH_COUNT`.

Debe cumplirse:

```text
MARKDOWN_RENDER_SOURCE = CANONICAL_CSV_FILES
MARKDOWN_RENDERED_FROM_REREAD_CSV = true
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
```

---

## 6. Alcance científico congelado

Preserva exactamente:

```text
EXPECTED_CANONICAL_TABLE_COUNT = 9
MATERIALIZED_CANONICAL_TABLE_COUNT = 9

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

No modifiques:

- G5-MAIN-01 salvo que sea necesario para que las nuevas validaciones computadas confirmen exactamente lo ya materializado;
- G5-MAIN-02;
- Phase E;
- EXP11A;
- EXP11B;
- Attempt06;
- Top-50;
- decisión HE2/HE5;
- ninguna cifra científica aprobada.

EXP12 continúa sin tabla de rendimiento.

---

## 7. Rama candidata v02 y topología

La v01 permanece historia inmutable.

Crea desde `origin/main`:

```text
branch = codex/group5-f02-canonical-tables-v02
base = d5729887f47c36d8cf42d87090c40f9668e5ae84
```

La rama v02 debe tener exactamente un commit científico-documental y los mismos **12 paths** definidos por Prompt97.

Comparando v01 contra v02, los únicos contenidos que se espera que cambien son:

```text
scripts/results/group5/materialize_g5_tables_v0_1.py
docs/results/group5/g5_canonical_tables_v0.1.md
outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
outputs/results/group5/g5_numeric_crosscheck_v0.1.json
```

Los otros ocho CSV canónicos deben permanecer byte-identical respecto de v01.

Debe cumplirse:

```text
V02_COMMITS_AHEAD = 1
V02_COMMITS_BEHIND = 0
V02_CHANGED_PATH_COUNT_FROM_MAIN = 12
V01_V02_EXPECTED_CONTENT_DELTA_PATH_COUNT = 4
V01_V02_UNEXPECTED_CONTENT_DELTA_PATH_COUNT = 0
V01_V02_NON_TARGET_CSV_DELTA_COUNT = 0
```

Si una corrección necesaria exige modificar otra tabla científica, detente:

```text
STOP / G5_F02_CORRECTION_SCOPE_EXPANSION_REQUIRED
```

---

## 8. Validación v02 obligatoria

El nuevo crosscheck debe demostrar mediante comprobaciones reales:

```text
EXPECTED_CANONICAL_TABLE_COUNT = 9
MATERIALIZED_CANONICAL_TABLE_COUNT = 9
MISSING_CANONICAL_TABLE_COUNT = 0
UNAUTHORIZED_EXTRA_TABLE_COUNT = 0

G3_EVIDENCE_FAMILY_MAPPED_COUNT = 16
G4_CONTROLLED_CLAIM_MAPPED_COUNT = 18

UNTRACED_SCIENTIFIC_VALUE_COUNT = 0
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
DENOMINATOR_MISMATCH_COUNT = 0
UNIT_MISMATCH_COUNT = 0
CI_LEVEL_MISMATCH_COUNT = 0

VALIDATION_COUNTERS_COMPUTED_FROM_CHECKS = true
HARDCODED_PASS_VALIDATION_COUNTER_COUNT = 0

HE5_HIERARCHY_ROW_COUNT = 3
HE5_HIERARCHY_ROWS_WITH_FROZEN_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_NONEMPTY_RENDERED_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_FABRICATED_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_ERROR_COUNT_VALUES_PRESERVED = true

MARKDOWN_RENDER_SOURCE = CANONICAL_CSV_FILES
MARKDOWN_RENDERED_FROM_REREAD_CSV = true

HE2A_PAIRED_DIFFERENCE_CI_BINDING_COMPLETE = true
HE2A_CI_MISBOUND_TO_ARM_ESTIMATE_COUNT = 0
HE2A_ARM_LEVEL_NEW_CI_COUNT = 0

EXP12_PERFORMANCE_TABLE_ROW_COUNT = 0
EXP12_FABRICATED_METRIC_COUNT = 0

SCIENTIFIC_METRIC_VALUE_DELTA_COUNT = 0
SCIENTIFIC_CLAIM_STRENGTH_DELTA_COUNT = 0
NEW_SCIENTIFIC_STATEMENT_COUNT = 0

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

Ejecuta además una regeneración limpia del candidato v02 y confirma byte-identidad de los 12 outputs generados/controlados que correspondan.

---

## 9. Estado administrativo postcorrección

Después de publicar y validar v02, actualiza exclusivamente:

```text
branch = docs/fichas-grupos-3-8
base = 1927ca9496615f19068812905afe4abe9800f979
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Mantén:

```text
G5-F01 = CLOSED / APPROVED
G5-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G5-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP5 = IN_PROGRESS
```

Añade bloque:

```text
FICHA = G5-F02
CORRECTIVE_PROMPT = PROMPT98
SUPERSEDED_CANDIDATE = 9a8ca23ef607b5975b46a4336e033fc44ebe9453
CURRENT_CANDIDATE = <v02>
CORRECTION_SCOPE = HE5_HIERARCHY_DENOMINATOR_AND_CROSSCHECK_VALIDATION_ONLY
SCIENTIFIC_RECOMPUTATION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP5 = IN_PROGRESS
G5_F03_AUTHORIZED = false
G5_F03_STARTED = false
PENDING_EXTERNAL_AUDIT = true
```

No actualices Plan Maestro.

---

## 10. Persistencia de respuesta

Crea exclusivamente en `codex/prompts-temporary`:

```text
codex_prompts_tmp/98_RESPUESTA_CORREGIR_G5_F02_DENOMINADOR_HE5_Y_VALIDACION_CROSSCHECK.md
```

El commit de respuesta debe añadir únicamente ese archivo.

Reporte terminal mínimo:

```text
PROMPT98 = COMPLETED

WORKSPACE_ROOT_OBSERVED = ...
WORKSPACE_ORIGIN_URL = ...
WORKSPACE_INITIAL_BRANCH = ...
WORKSPACE_INITIAL_HEAD = ...
WORKSPACE_INITIAL_DIRTY_COUNT = ...
USER_CANONICAL_LOCAL_PATH_FROZEN = false
LOCAL_PERSISTENCE_IN_USER_FOLDER_ASSERTED = false

PREFLIGHT_MAIN = d5729887f47c36d8cf42d87090c40f9668e5ae84
PREFLIGHT_PLAN = cd331d400d22cbcbbd47a9389b5cac9e90ad53e8
PREFLIGHT_FICHAS = 1927ca9496615f19068812905afe4abe9800f979
PREFLIGHT_V01 = 9a8ca23ef607b5975b46a4336e033fc44ebe9453
ARTICLE_HEAD_PREFLIGHT = ...
PROMPT98_COMMIT = ...

V02_BRANCH = codex/group5-f02-canonical-tables-v02
V02_CANDIDATE = ...
V02_PARENT = d5729887f47c36d8cf42d87090c40f9668e5ae84
V02_COMMITS_AHEAD = 1
V02_COMMITS_BEHIND = 0
V02_CHANGED_PATH_COUNT_FROM_MAIN = 12
V01_V02_EXPECTED_CONTENT_DELTA_PATH_COUNT = 4
V01_V02_UNEXPECTED_CONTENT_DELTA_PATH_COUNT = 0
V01_V02_NON_TARGET_CSV_DELTA_COUNT = 0

HE5_HIERARCHY_ROW_COUNT = 3
HE5_HIERARCHY_ROWS_WITH_FROZEN_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_NONEMPTY_RENDERED_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_FABRICATED_DENOMINATOR_COUNT = 0
HE5_HIERARCHY_ERROR_COUNT_VALUES_PRESERVED = true

VALIDATION_COUNTERS_COMPUTED_FROM_CHECKS = true
HARDCODED_PASS_VALIDATION_COUNTER_COUNT = 0
MARKDOWN_RENDER_SOURCE = CANONICAL_CSV_FILES
MARKDOWN_RENDERED_FROM_REREAD_CSV = true

UNTRACED_SCIENTIFIC_VALUE_COUNT = 0
UNEXPLAINED_NUMERIC_DISCREPANCY_COUNT = 0
SUPERSEDED_NUMERIC_SOURCE_USED_COUNT = 0
MARKDOWN_CSV_VALUE_MISMATCH_COUNT = 0
DENOMINATOR_MISMATCH_COUNT = 0
UNIT_MISMATCH_COUNT = 0
CI_LEVEL_MISMATCH_COUNT = 0
SCIENTIFIC_METRIC_VALUE_DELTA_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
NEW_INFERENCE_PERFORMED = false
NEW_CI_CALCULATED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
G5_F03_STARTED = false

POSTCORRECTION_FICHAS_COMMIT = ...
G5_F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP5 = IN_PROGRESS
G5_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G5_F03_AUTHORIZED = false

WORKSPACE_FINAL_BRANCH = ...
WORKSPACE_FINAL_HEAD = ...
WORKSPACE_FINAL_DIRTY_COUNT = ...
ARTICLE_HEAD_FINAL_OBSERVED = ...
BLOCKERS = NONE
WARNINGS = ...
```

No integres v02 a `main` durante Prompt98.
