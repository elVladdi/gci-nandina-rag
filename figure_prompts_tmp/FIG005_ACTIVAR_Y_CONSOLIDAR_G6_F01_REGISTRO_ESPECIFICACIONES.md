# FIG005 — ACTIVAR Y CONSOLIDAR G6-F01: REGISTRO CANÓNICO DE ESPECIFICACIONES DE FIGURAS

## 0. Rol y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto de tesis.

Ejecuta exclusivamente FIG005.

FIG001–FIG004 ya fueron auditados externamente y quedaron aprobados como base conceptual. FIG005 debe convertir esas decisiones en el **único output formal de G6-F01**:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

FIG005 constituye la ejecución documental formal de **G6-F01 — Catálogo y especificación de figuras**. Debe activar G6-F01, construir un candidato de registro machine-readable y dejarlo pendiente de auditoría externa.

FIG005 **NO** genera figuras ni scripts.

No autoriza:

- ejecutar G6-F02;
- generar PNG, SVG, PDF, EPS o mockups finales;
- escribir scripts Python;
- modificar `main` directamente;
- modificar Plan Maestro;
- modificar artículo o tesis;
- recalcular métricas, promedios, deltas, CI, p-values o inferencia;
- crear nuevas figuras fuera del catálogo aprobado;
- redecidir HE2 o HE5;
- reabrir EXP12;
- usar resultados superseded.

---

## 1. Repositorio y ramas

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Rama de prompts/respuestas:

```text
codex/prompts-temporary
```

Rama de estado de fichas:

```text
docs/fichas-grupos-3-8
```

Rama científica base:

```text
main
```

Rama candidata que debes crear desde `main` exactamente:

```text
figures/g6-f01-spec-registry-v01
```

No uses otra rama candidata.

---

## 2. Refs rectoras congeladas

Antes de modificar nada, verifica:

```text
MAIN_BASE = ca065618d5df0019f76ef5a971e858d91c263e1f
PLAN_BASE = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
FICHAS_BASE = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
FIG004_RESPONSE = 89d95744b2ab446245a5522eefc8279f673a8a7c
```

Si `main`, Plan o fichas han sufrido drift material respecto de estas bases, detente y repórtalo. Un avance editorial concurrente no es bloqueante salvo que altere ciencia congelada o los artefactos rectores de G6-F01.

---

## 3. Ficha rectora G6-F01

Fuente:

```text
docs/fichas/grupos_3_8/grupo_6/G6_F01_CATALOGO_Y_ESPECIFICACION_FIGURAS.md
blob = 80771ddbfb4b4e54c90ed92f43942d8e3d30a764
```

Objetivo rector:

> Definir cada figura antes de generarla: pregunta visual, fuente exacta, transformación, eje, unidad, incertidumbre, caption y claim asociado.

Output único:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

El registro operacional vigente en `04_REGISTRO_ESTADO_FICHAS.md` es la fuente de verdad del estado actual y debe mostrar antes de FIG005:

```text
G6-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6-F02 = PROSPECTIVE
GROUP6 = NOT_STARTED
```

No cambies el encabezado histórico de estado dentro del archivo individual de ficha; solo actualiza el registro operacional.

---

## 4. Respuestas aprobadas que debes consolidar

### FIG001 — catálogo crítico

```text
figure_prompts_tmp/FIG001_RESPUESTA_REVISION_CRITICA_CATALOGO_INICIAL.md
commit = 2c31d0c7112abedab224023b33d8173f116b3712
```

Decisión aprobada:

```text
CATALOGO_FINAL_PRELIMINAR = 3 figuras

G6-FIG-01 = HE2_A + HE2_B / PRINCIPAL
G6-FIG-02 = Phase E / SECUNDARIA
G6-FIG-03 = EXP11A / ANEXO

EXP11B = TABLE_ONLY
HE5_COMPONENTS = TABLE_ONLY
TOP50 = TABLE_ONLY
ATTEMPT06_CORRECTIVE = TABLE_ONLY
PHASE_E_DIAGNOSTIC_UNION = TABLE_ONLY
EXP12 = TEXT_ONLY_NOT_ESTIMABLE
```

### FIG002 — G6-FIG-01

```text
figure_prompts_tmp/FIG002_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_01.md
commit = d2f9e07923789709a52622bea922be84aefc526d
```

Contrato aprobado mínimo:

```text
figure_id = G6-FIG-01
panel_count = 3
orientation = VERTICAL / PORTRAIT
aspect_ratio = 4:5 approx
role = PRIMARY_INFERENTIAL
claims = G3C-001, G3C-002, G3C-003, G3C-004
Panel A = grouped dot plot, valores absolutos HE2_A, no arm-level CI, x=[0,1]
Panel B = grouped dot-whisker, 15 contrastes Historical-comparator, CI99%, x=[-0.10,1.00], reference x=0
Panel C = single-estimate dot-whisker HE2_B, CI95%, contexto Recall@100/Recall@200, x=[-0.10,1.00]
```

Fuentes:

```text
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
blob = cb68583ee2260e4455796bac99ad90995ca7ef92

outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
blob = 359e4e19b5ef1d44983c03039162209293b2a44c
```

### FIG003 — G6-FIG-02

```text
figure_prompts_tmp/FIG003_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_02_PHASE_E.md
commit = a9059e9a22a33e7a088ac832d00fcb941a49e4b7
```

Contrato aprobado mínimo:

```text
figure_id = G6-FIG-02
panel_count = 1
orientation = HORIZONTAL
aspect_ratio = 16:9 approx
role = DESCRIPTIVE_SUPPLEMENTARY
claim = G3C-005
chart_type = GROUPED_DOT_PLOT_NO_LINES
x = depth categories [50,100,200]
y = exact-NANDINA coverage, [0,0.35]
uncertainty = DESCRIPTIVE_NO_CI_AUTHORIZED
```

Variantes formales:

```text
hierarchical_only
dual_only
hierarchical_first_100
hierarchical_80_dual_backfill_20
```

Contexto adicional:

```text
hierarchical_70_dual_backfill_30
```

Fuente:

```text
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
```

`diagnostic_union_hierarchical_dual` queda excluido como rendimiento ordinario.

### FIG004 — G6-FIG-03

```text
figure_prompts_tmp/FIG004_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_03_EXP11A.md
commit = 89d95744b2ab446245a5522eefc8279f673a8a7c
```

Contrato aprobado mínimo:

```text
figure_id = G6-FIG-03
panel_count = 6
layout = 2x3
orientation = LANDSCAPE
aspect_ratio = 3:2
role = DESCRIPTIVE_SENSITIVITY / NONCAUSAL
claim = G3C-007
metrics = Top1, Top3, Top5, Top10, Top50, MRR
chart_type = categorical strip/dot small multiples
condition_order = H25, H50-D1, H50-D2, H75, H100 ref.
y_range = [0,1]
uncertainty = NONE
summary_policy = table only; no summary markers
observed runs = 31
counts = 10 / 5 / 5 / 10 / 1
```

Fuente:

```text
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403
```

Supporting sources:

```text
outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv
blob = 9b434d7e09e6db7e9de061953b59c53aac2337ad

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
blob = 535dd377d107ddcbf09ecaa13cd66ca723ee738d
```

---

## 5. Contrato científico inmutable

Preserva:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

No conviertas ninguna decisión visual en nueva evidencia científica.

---

## 6. Activación operacional de G6-F01

Antes de crear el candidato, sobre `docs/fichas-grupos-3-8` y partiendo exactamente de `FICHAS_BASE`, modifica **solo**:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Añade un bloque de activación y actualiza la fila G6-F01 a:

```text
G6-F01 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
GROUP6 = IN_PROGRESS
G6-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

El bloque debe registrar como mínimo:

```text
FICHA = G6-F01
USER_AUTHORIZATION = FIG005_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
MAIN_AT_ACTIVATION = ca065618d5df0019f76ef5a971e858d91c263e1f
PLAN_AT_ACTIVATION = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
FICHAS_AT_ACTIVATION = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
FIG001_RESPONSE = 2c31d0c7112abedab224023b33d8173f116b3712
FIG002_RESPONSE = d2f9e07923789709a52622bea922be84aefc526d
FIG003_RESPONSE = a9059e9a22a33e7a088ac832d00fcb941a49e4b7
FIG004_RESPONSE = 89d95744b2ab446245a5522eefc8279f673a8a7c
G6_F02_AUTHORIZED = false
```

No actualices Plan Maestro en FIG005.

---

## 7. Candidato G6-F01

Crea la rama:

```text
figures/g6-f01-spec-registry-v01
```

exactamente desde:

```text
ca065618d5df0019f76ef5a971e858d91c263e1f
```

En esa rama añade **exactamente un archivo nuevo**:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

No modifiques ningún otro path.

El candidato esperado debe quedar:

```text
COMMITS_AHEAD = 1
COMMITS_BEHIND = 0
CHANGED_PATH_COUNT = 1
```

---

## 8. Esquema obligatorio del JSON

El JSON debe ser machine-readable, válido y estable. Debe incluir al menos:

```text
artifact_id
version
status
ficha
created_from_main
scientific_scope
approved_design_sources
figure_spec_count
figures
non_figure_dispositions
validation
```

### 8.1 Encabezado

```text
artifact_id = G6_F01_FIGURE_SPEC_REGISTRY_v0.1
version = v0.1
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G6-F01
created_from_main = ca065618d5df0019f76ef5a971e858d91c263e1f
figure_spec_count = 3
```

### 8.2 Cada figura

Cada objeto en `figures` debe contener, sin omitir los requisitos de la ficha:

```text
figure_id
working_title
scientific_question
scientific_role
destination
claim_ids
source_artifacts[]
source_hashes[]
columns_used[]
row_filter_or_inventory
transformations_allowed[]
transformations_forbidden[]
panel_count
layout
chart_type
axes
units
scales
ranges
N_and_denominator
uncertainty_policy
marks_and_encoding
accessibility_requirements
caption_working
implementation_validation_checks[]
source_design_response
```

No inventes datos que no estén en FIG002–FIG004 o las fuentes congeladas. Cuando una figura usa más de una fuente, enumera cada fuente/hash de forma explícita.

### 8.3 Disposiciones de no-figura

Incluye exactamente seis entradas principales en `non_figure_dispositions`:

```text
EXP11B_H150_H200 = TABLE_ONLY_DESCRIPTIVE_SENSITIVITY
HE5_COMPONENTS = TABLE_ONLY_HE5_DESCRIPTIVE
TOP50_SUPPLEMENTARY = TABLE_ONLY_SUPPLEMENTARY
0B05C_ATTEMPT06_CORRECTIVE = TABLE_ONLY_CORRECTIVE_SENSITIVITY
PHASE_E_DIAGNOSTIC_UNION = TABLE_ONLY_DIAGNOSTIC
EXP12 = TEXT_ONLY_NOT_ESTIMABLE_NO_PERFORMANCE_FIGURE
```

Cada entrada debe incluir una razón breve y el artefacto canónico correspondiente cuando exista. No generes una figura sustituta para ocupar espacio.

---

## 9. Validaciones obligatorias del candidato

Debes calcular/verificar documentalmente y registrar en `validation`:

```text
FIGURE_SPEC_COUNT = 3
NON_FIGURE_DISPOSITION_COUNT = 6

G6_FIG_01_SOURCE_BLOBS_MATCH = true
G6_FIG_02_SOURCE_BLOB_MATCH = true
G6_FIG_03_SOURCE_BLOBS_MATCH = true

G6_FIG_01_HE2A_CI_LEVEL = 99%
G6_FIG_01_HE2B_CI_LEVEL = 95%
G6_FIG_01_ARM_LEVEL_CI_AUTHORIZED = false

G6_FIG_02_FORMAL_VARIANT_COUNT = 4
G6_FIG_02_CONTEXT_VARIANT_COUNT = 1
G6_FIG_02_CI_AUTHORIZED = false
G6_FIG_02_DIAGNOSTIC_UNION_INCLUDED_AS_PERFORMANCE = false

G6_FIG_03_OBSERVED_RUN_COUNT = 31
G6_FIG_03_CONDITION_COUNTS = [10,5,5,10,1]
G6_FIG_03_FROZEN_SUMMARY_COUNT = 6
G6_FIG_03_SUMMARIES_PLOTTED = false
G6_FIG_03_CI_AUTHORIZED = false
G6_FIG_03_CAUSAL_SIZE_INTERPRETATION = false

NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
FIGURE_BINARY_COUNT = 0
FIGURE_SCRIPT_COUNT = 0
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
EXP12_REOPENED = false
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
```

---

## 10. Estado postejecución en fichas

Después de crear el candidato, sobre la rama `docs/fichas-grupos-3-8`, desde el commit de activación generado en esta misma ejecución, modifica nuevamente **solo**:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Deja:

```text
G6-F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
G6-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Añade un bloque postejecución con:

```text
G6_F01_BRANCH
G6_F01_CANDIDATE_COMMIT
G6_F01_CANDIDATE_PARENT
G6_F01_CHANGED_PATH_COUNT
G6_F01_CHANGED_PATHS
FIGURE_SPEC_COUNT
NON_FIGURE_DISPOSITION_COUNT
EXTERNAL_AUDIT = PENDING
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
```

No cierres G6-F01. No cierres Grupo 6.

---

## 11. Respuesta oficial de FIG005

Al terminar, guarda la respuesta oficial en:

```text
figure_prompts_tmp/FIG005_RESPUESTA_ACTIVAR_Y_CONSOLIDAR_G6_F01_REGISTRO_ESPECIFICACIONES.md
```

sobre:

```text
codex/prompts-temporary
```

El commit de respuesta debe añadir únicamente ese archivo respecto del commit de FIG005.

La respuesta debe reportar como mínimo:

```text
FIG005_EXECUTION = COMPLETE / BLOCKED
SOURCE_CONTRACT = PASS / FAIL

ACTIVATION_COMMIT
FICHAS_POSTEXEC_COMMIT

G6_F01_BRANCH
G6_F01_CANDIDATE_COMMIT
G6_F01_CANDIDATE_PARENT
COMMITS_AHEAD
COMMITS_BEHIND
CHANGED_PATH_COUNT
CHANGED_PATHS

FIGURE_SPEC_COUNT
NON_FIGURE_DISPOSITION_COUNT

NEW_SCIENTIFIC_METRIC_COUNT
NEW_INFERENCE_COUNT
NEW_CI_COUNT
NEW_P_VALUE_COUNT
FIGURE_BINARY_COUNT
FIGURE_SCRIPT_COUNT

MAIN_FINAL
PLAN_FINAL
FICHAS_FINAL
G6_F01_FINAL_STATE
GROUP6_FINAL_STATE
G6_F02_FINAL_STATE

EXTERNAL_AUDIT = PENDING
```

Si algo no cumple, no lo maquilles: reporta `BLOCKED` y detalla el punto exacto.

---

## 12. Disposición esperada

Si todo cumple:

```text
FIG005_EXECUTION = COMPLETE
G6_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
G6_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING
```

La ejecución de FIG005 no constituye aprobación ni autorización de G6-F02.