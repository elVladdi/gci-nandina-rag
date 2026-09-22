# PROMPT103 — ACTIVAR Y EJECUTAR G6-F01: CATÁLOGO Y ESPECIFICACIÓN DE FIGURAS

## 0. Naturaleza y autorización

Ejecuta **exclusivamente** G6-F01 — Catálogo y especificación de figuras.

La auditoría externa independiente de Prompt102 determinó:

```text
PROMPT102_EXTERNAL_AUDIT = PASS
GROUP5 = CLOSED / APPROVED
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = NOT_STARTED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

La invocación explícita de este Prompt103 constituye autorización únicamente para:

1. realizar el RPRE de G6-F01;
2. activar G6-F01 en el registro de fichas;
3. diseñar y versionar el catálogo machine-readable de figuras;
4. dejar G6-F01 como candidato pendiente de auditoría externa.

No autoriza:

- generar PNG, SVG, PDF ni otra figura;
- escribir scripts de generación de figuras;
- ejecutar G6-F02 o G6-F03;
- modificar las nueve tablas canónicas de Grupo 5;
- calcular métricas, deltas científicos nuevos, intervalos, p-values o inferencia;
- modificar HE2=SUPPORTED ni HE5=INCONCLUSIVE;
- reabrir EXP12;
- modificar artículo o tesis;
- modificar el Plan Maestro;
- realizar búsqueda bibliográfica;
- iniciar Grupo 7.

---

## 1. Workspace local canónico obligatorio

Trabaja exclusivamente dentro del repositorio local canónico:

```text
C:/Users/Vladimir/OneDrive/Documentos/Maestría UNMSM/LLM_RGA_NANDINA
```

Antes de cualquier operación registra y verifica:

```text
git rev-parse --show-toplevel
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git status --porcelain
git worktree list --porcelain
```

Debe cumplirse:

```text
WORKSPACE_ROOT_MATCH_EXPECTED = true
WORKSPACE_ORIGIN_REPOSITORY = elVladdi/gci-nandina-rag
USER_CANONICAL_LOCAL_PATH_FROZEN = true
```

No uses otro clon como workspace principal. No crees un clon alternativo ni un worktree nuevo. No limpies, resetees, borres, sobrescribas ni hagas stash de cambios locales preexistentes del usuario.

Los warnings por metadata histórica de worktrees son no bloqueantes si no interfieren con los paths gobernados.

---

## 2. Refs congelados y preflight

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = ca065618d5df0019f76ef5a971e858d91c263e1f
origin/docs/fichas-grupos-3-8 = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
origin/docs/plan-maestro-temporal-2026-08-31 = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
PROMPT102_SOURCE = 999b0f6fe411fd774ec1d2af99bea6554c4d1313
PROMPT102_RESPONSE = 242ac8c2b32bd1af1fa03f4e8e6b7733ee952e97
ARTICLE_HEAD_AT_DESIGN = db01f6432464e97d428de7e3d5a5c1e80b34e528
```

La rama editorial es solo observacional. Registra su HEAD al inicio y al final. Su avance concurrente no es bloqueo si Prompt103 no la modifica.

Verifica además en fichas y Plan:

```text
GROUP5 = CLOSED / APPROVED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
GROUP6 = NOT_STARTED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Si `main`, fichas o Plan presentan drift experimental no explicado:

```text
STOP / G6_F01_REF_DRIFT
```

---

## 3. Fuentes científicas congeladas

G6-F01 debe consumir únicamente evidencia ya integrada en `main`.

Fuentes rectoras mínimas:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245

docs/results/group5/g5_canonical_tables_v0.1.md
blob = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d

outputs/results/group5/g5_numeric_crosscheck_v0.1.json
blob = a28af8df10f6d6bb4fdb02458288b41e34e1dc78

docs/results/group5/g5_appendix_registry_v0.1.md
blob = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a

outputs/audits/group5_closure_v0.1.json
blob = 1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf

outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
blob = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab

outputs/analysis/group4/g4_limitations_registry_v0.1.json
blob = ae00b93431e912cb78a58344057d9bf7a51fcd47
```

Las nueve tablas canónicas G5-F02 son el universo numérico inmediato para las figuras de resultados. Verifica sus blobs actuales desde `main` y regístralos en el output. Como mínimo deben incluir:

```text
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
blob = cb68583ee2260e4455796bac99ad90995ca7ef92

outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
blob = 359e4e19b5ef1d44983c03039162209293b2a44c

outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61

outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
blob = 727076a0d09735a87f45f6522d2a0ecead2cee17

outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv
blob = c2ded734af9ea340d715483b6e8cc00a7536dfea

outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403

outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv
blob = 76c8c6c588c7e809c6be64f7192f497c491fb692

outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv
blob = 490ef570fa1674e2eecad7f0a3cdf34ba96204db

outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv
blob = f43cce08d1d7bc3cef64698dbebf14eae4b26ed5
```

No uses Attempts 03/04/05 ni ningún output superseded.

---

## 4. Contrato científico inmutable

Preserva exactamente:

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
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Guardrails obligatorios:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

Semántica vigente de Attempt06:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
OVERALL = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

EXP12 no puede convertirse en figura de rendimiento.

---

## 5. RPRE obligatorio antes de activar

Documenta PASS/FAIL para, como mínimo:

```text
RPRE_G6_F01_SOURCE_CONTRACT
RPRE_G6_F01_GROUP5_CLOSED
RPRE_G6_F01_PLAN_RECONCILED
RPRE_G6_F01_G5_TABLE_BLOB_IDENTITY
RPRE_G6_F01_G4_CLAIM_TRACEABILITY
RPRE_G6_F01_NO_NEW_SCIENCE
RPRE_G6_F01_NO_RECOMPUTATION
RPRE_G6_F01_HE2_HE5_PRESERVATION
RPRE_G6_F01_ATTEMPT06_CURRENT_ONLY
RPRE_G6_F01_EXP11A_NONCAUSAL
RPRE_G6_F01_EXP11B_DESCRIPTIVE_ONLY
RPRE_G6_F01_EXP12_NO_PERFORMANCE
RPRE_G6_F01_AXIS_INTEGRITY_POLICY
RPRE_G6_F01_FAVORABILITY_SELECTION_PROHIBITED
RPRE_G6_F01_ARTICLE_READONLY
RPRE_G6_F01_G6_F02_NOT_STARTED
```

Si falla un control material:

```text
STOP / G6_F01_RPRE_FAILED
```

---

## 6. Activación de G6-F01

Solo después de RPRE PASS, trabaja sobre:

```text
branch = docs/fichas-grupos-3-8
base = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
file = docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Modifica exclusivamente ese archivo.

Cambia:

```text
G6-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

por:

```text
G6-F01 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
```

Mantén:

```text
G6-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
```

Si las filas históricas de G6-F02/G6-F03 solo dicen `PROSPECTIVE`, puedes precisar `PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED` sin activarlas.

Añade un bloque de activación que registre main, Plan, fichas, artículo observado, Prompt103 y RPRE.

Haz un único commit administrativo y push normal.

---

## 7. Objetivo científico de G6-F01

Crear exclusivamente:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

Este registro define **qué figuras deben existir y cómo deben construirse**, pero no genera ninguna figura.

El catálogo debe responder, para cada figura:

- qué pregunta visual responde;
- qué claim(s) congelados comunica;
- qué fuente exacta y blob consume;
- qué columnas/filas usa;
- qué transformación de presentación está permitida;
- qué codificación visual se usará;
- qué ejes, unidades, escalas y rangos son válidos;
- cuál es la población/N/denominador;
- qué incertidumbre ya congelada puede representarse;
- qué incertidumbre no está autorizada;
- qué advertencias deben permanecer visibles;
- qué caption de trabajo corresponde;
- cuál será su destino previsto.

No conviertas la selección de figuras en una nueva selección de resultados. La decisión de incluir/omitir una figura debe basarse en rol científico + utilidad visual, nunca en favorabilidad.

---

## 8. Catálogo obligatorio: seis figuras

El registro debe contener exactamente **6 especificaciones de figura**.

### G6-FIG-01 — HE2_A: desempeño absoluto y contrastes pareados primarios

Fuente primaria:

```text
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
```

Claims:

```text
G3C-001
G3C-002
G3C-003
```

Rol:

```text
PRIMARY_INFERENTIAL / MAIN_RESULTS
```

Debe ser una figura multipanel que mantenga separados:

**Panel A — valores absolutos observados**
- Historical, Flat Attempt06, Hierarchical Attempt06 y D1a Attempt06.
- Métricas: Top-1, Top-3, Top-5, Top-10, MRR@100.
- usar `historical_observed_value` y `comparator_observed_value`;
- no mostrar CI por brazo;
- escala lineal de 0 a 1;
- usar puntos agrupados, no líneas que sugieran una trayectoria continua entre MRR y Top-k;
- al deduplicar el valor historical repetido por comparador, verificar identidad exacta; no promediar.

**Panel B — estimando pareado**
- `paired_difference_historical_minus_comparator`;
- CI 99% ya congelado, usando exclusivamente las columnas correspondientes;
- formato tipo forest/dot-whisker;
- línea de referencia en 0;
- escala lineal que incluya 0 y todos los extremos del CI, sin truncar para magnificar diferencias;
- el CI pertenece al estimando pareado y nunca a los brazos absolutos.

Caption de trabajo debe mencionar benchmark interno Capítulo 87, 1,056 series, 67 DAM, contraste no causal y CI cluster-bootstrap congelado del estimando pareado.

### G6-FIG-02 — HE2_B: cobertura profunda jerárquica

Fuente:

```text
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
```

Claim:

```text
G3C-004
```

Rol:

```text
PRIMARY_INFERENTIAL / MAIN_RESULTS
```

Dos paneles o una composición equivalente científicamente clara:

- valores absolutos Recall@100 y Recall@200 en escala 0–1;
- contraste `Recall@200 - Recall@100` con su CI congelado;
- la escala del contraste debe incluir 0;
- `Pool@200 context` puede anotarse como contexto, pero no como segundo contraste confirmatorio;
- no calcular nuevos intervalos.

Conserva exactamente el nivel de CI documentado en la fuente G3/G5; no lo sustituyas por 99% si la fuente de HE2_B usa otro nivel.

### G6-FIG-03 — Phase E: cobertura descriptiva por profundidad

Fuente:

```text
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
```

Claim:

```text
G3C-005
```

Rol:

```text
DESCRIPTIVE_SUPPLEMENTARY / SECONDARY_RESULTS
```

Especificación:

- eje x: depth literal 50, 100, 200;
- eje y: `exact-NANDINA coverage`;
- líneas/puntos por todas las variantes presentes, sin excluir ninguna por solapamiento o desempeño;
- escala y de 0 a 1;
- no CI;
- no rol confirmatorio;
- no presentar la unión diagnóstica de G5-APPENDIX-05 como rendimiento en esta figura.

### G6-FIG-04 — EXP11A: sensibilidad conjunta tamaño/composición

Fuente:

```text
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
```

Claim:

```text
G3C-007
```

Rol:

```text
DESCRIPTIVE_SENSITIVITY / APPENDIX
```

Especificación:

- seis small multiples: Top1, Top3, Top5, Top10, Top50 y MRR;
- eje x **categórico**, no continuo: H25, H50, H75, H100;
- mostrar todas las corridas observadas disponibles para H25/H50/H75 y la referencia H100;
- los `FROZEN_CONDITION_SUMMARY` pueden mostrarse como marcadores de resumen solo porque ya existen en la fuente;
- no calcular nuevos promedios, SD, CI ni bandas;
- no dibujar línea de tendencia/regresión;
- no describir H25→H100 como efecto causal del tamaño;
- hacer visible que tamaño y composición cambian conjuntamente.

### G6-FIG-05 — EXP11B: comparación pareada H150/H200 por seeds observados

Fuente:

```text
outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv
```

Claim:

```text
G3C-008
```

Rol:

```text
DESCRIPTIVE_SENSITIVITY / APPENDIX
```

Especificación:

- seis small multiples: Top1, Top3, Top5, Top10, Top50 y MRR;
- eje x categórico: H150, H200;
- unir con una línea únicamente los dos valores que comparten el mismo `seed pair`;
- mostrar los diez pares observados;
- puede mostrarse el `FROZEN_CONDITION_SUMMARY` como marcador separado;
- no tratar 10×1056 como observaciones independientes;
- no calcular CI ni inferencia a superpoblación de seeds;
- no ordenar los seeds por magnitud del efecto para favorecer una narrativa.

### G6-FIG-06 — HE5: componentes descriptivos

Fuente:

```text
outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
```

Claims:

```text
G3C-012
G3C-013
```

Rol:

```text
DESCRIPTIVE_HE5 / SECONDARY_RESULTS
```

Debe separar dos paneles con unidades distintas:

**Panel A — errores jerárquicos históricos**
- categorías literales SAME_CHAPTER, SAME_HS4, SAME_HS6;
- y = `error_count`;
- barras o puntos desde cero;
- denominador permanece vacío porque la fuente no materializa uno;
- no convertir los conteos en proporciones.

**Panel B — desempeño por soporte histórico literal**
- categorías 1 DAM, 2 DAM, 3-4 DAM, 5+ DAM;
- métricas top1_rate, top3_rate y mean_reciprocal_rank;
- escala 0–1;
- mostrar denominadores literales de cada bucket en etiqueta/caption;
- no inventar un umbral de "insuficiencia";
- no inferir monotonicidad, causalidad ni apoyo inferencial a HE5.

Caption de trabajo debe indicar explícitamente `HE5 = INCONCLUSIVE` y `DESCRIPTIVE_ONLY`.

---

## 9. Presentaciones que NO tendrán figura separada

El JSON debe contener un `nonfigure_dispositions` explícito para las tres tablas canónicas restantes:

```text
G5-APPENDIX-01  Top-50 supplementary
G5-APPENDIX-04  0B-05C Attempt06 corrective sensitivity
G5-APPENDIX-05  Phase E diagnostic union
```

Disposición gobernante:

### G5-APPENDIX-01

```text
TABLE_ONLY_SUPPLEMENTARY
```

Razón: Top-50 es suplementario y no decide HE2; una figura separada duplicaría G6-FIG-01 y podría elevar indebidamente su peso narrativo.

### G5-APPENDIX-04

```text
TABLE_ONLY_CORRECTIVE_SENSITIVITY
```

Razón: la tabla conserva completa la semántica method-dependent de EV03/EV04/D1a. Una figura separada de deltas heterogéneos puede magnificar visualmente cambios diminutos o mezclar escalas. Los valores corregidos vigentes ya alimentan las comparaciones primarias pertinentes.

### G5-APPENDIX-05

```text
TABLE_ONLY_DIAGNOSTIC
```

Razón: es un techo diagnóstico descriptivo, no rendimiento confirmatorio.

Registra también que:

```text
EXP12 = TEXT_ONLY_NOT_ESTIMABLE / NO_PERFORMANCE_FIGURE
G5-TEXT-02 = NO_FIGURE / NOT_ESTIMABLE
G5-TEXT-03 = NO_NUMERIC_FIGURE / LIMITATION
G5-TEXT-04 = NO_RESULTS_FIGURE / ARCHITECTURAL_GUARDRAIL
G5-NOTRESULT-01..03 = NO_FIGURE / NOT_RESULTS
```

No inventes una figura para llenar esos espacios.

---

## 10. Transformaciones permitidas y prohibidas

Transformaciones de **presentación** permitidas:

```text
WIDE_TO_LONG_RESHAPE
FILTER_BY_FROZEN_ROW_TYPE
PANEL_SPLIT
FROZEN_ORDERING
EXACT_DUPLICATE_DEDUPLICATION_AFTER_IDENTITY_CHECK
PAIR_BY_EXISTING_SEED_ID
PERCENT_FORMATTING_FOR_DISPLAY_ONLY
LABEL_TRANSLATION_FOR_DISPLAY_ONLY
```

No deben cambiar los valores fuente.

Prohibido:

```text
NEW_MEAN_CALCULATION
NEW_SD_CALCULATION
NEW_DELTA_CALCULATION_AS_SCIENTIFIC_RESULT
NEW_CI_CALCULATION
NEW_P_VALUE
SMOOTHING
REGRESSION
POSTHOC_THRESHOLDING
FAVORABILITY_SORTING
AXIS_TRUNCATION_TO_MAGNIFY_EFFECT
LOG_SCALE_WITHOUT_PREAPPROVED_JUSTIFICATION
OMIT_NEGATIVE_OR_NULL_COMPONENTS
```

Si una figura necesita un valor que no existe en las fuentes congeladas, la especificación debe declarar `NOT_AVAILABLE / DO_NOT_DERIVE`, no calcularlo.

---

## 11. Política de ejes e integridad visual

Cada spec debe contener `axis_integrity` con reglas machine-readable.

Como mínimo:

- métricas acotadas [0,1] → rango 0–1 cuando se muestran valores absolutos;
- conteos → baseline 0;
- contrastes con CI → incluir siempre la referencia 0 y todos los extremos de CI;
- no truncar ejes para exagerar diferencias;
- no usar doble eje y;
- no usar 3D;
- no usar áreas/perspectiva que distorsionen magnitud;
- las categorías deben conservar orden científico predefinido, no ordenarse por resultado;
- si dos series se superponen, conservarlas y resolver mediante marcador/estilo, no ocultarlas.

---

## 12. Accesibilidad preliminar

G6-F01 define requisitos; G6-F03 hará la auditoría final.

Cada figura debe especificar:

```text
COLOR_IS_NOT_SOLE_ENCODING = true
MARKER_OR_LINESTYLE_REDUNDANCY = true cuando haya series múltiples
GRAYSCALE_DISTINGUISHABLE_REQUIRED = true
FONT_AND_LABEL_LEGIBILITY_REQUIRED = true
BACKGROUND = light/white
NO_DECORATIVE_3D = true
```

No fijes una paleta por conveniencia narrativa. La semántica de colores/markers debe ser consistente entre figuras cuando una misma entidad reaparece.

---

## 13. Schema mínimo del JSON

El JSON debe ser válido y contener, como mínimo:

```text
artifact_id
status
ficha
main_base
plan_snapshot
fichas_activation_commit
prompt103_commit
article_head_observed
scientific_scope
source_registry
selection_policy
figure_specs
nonfigure_dispositions
presentation_coverage
validation
```

Cada `figure_specs[]` debe incluir:

```text
figure_id
title_working
scientific_role
intended_destination
visual_question
related_claim_ids
related_evidence_family_ids
source_artifacts[]:
  path
  blob
  columns
  row_filters
population:
  unit_of_analysis
  N
  DAM_N
  denominator_notes
allowed_transformations
forbidden_transformations
panels[]
axis_integrity
uncertainty:
  type
  level
  source_binding
  new_uncertainty_authorized=false
working_caption
mandatory_qualifications
forbidden_interpretations
accessibility_requirements
generation_status = SPEC_ONLY_NOT_GENERATED
```

`working_caption` es provisional. No sustituye el caption final de G6-F03.

---

## 14. Cobertura y validaciones obligatorias

El catálogo debe demostrar:

```text
EXPECTED_FIGURE_SPEC_COUNT = 6
FIGURE_SPEC_COUNT = 6

EXPECTED_CANONICAL_TABLE_PRESENTATION_COUNT = 9
ACCOUNTED_CANONICAL_TABLE_PRESENTATION_COUNT = 9
UNACCOUNTED_CANONICAL_TABLE_PRESENTATION_COUNT = 0

FIGURE_MAPPED_CANONICAL_PRESENTATION_COUNT = 6
TABLE_ONLY_CANONICAL_PRESENTATION_COUNT = 3

FAVORABILITY_BASED_SELECTION_COUNT = 0
UNJUSTIFIED_OMISSION_COUNT = 0
SUPERSEDED_SOURCE_USED_COUNT = 0
NEW_SCIENTIFIC_METRIC_VALUE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
FIGURE_FILE_CREATED_COUNT = 0
FIGURE_SCRIPT_CREATED_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false
EXP12_PERFORMANCE_FIGURE_COUNT = 0
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
G6_F02_STARTED = false
G6_F02_AUTHORIZED = false
```

Además verifica específicamente:

```text
HE2A_ABSOLUTE_ARM_CI_CREATED_COUNT = 0
HE2A_PAIRED_CI_BOUND_CORRECTLY = true
HE2B_CI_LEVEL_PRESERVED = true
EXP11A_CAUSAL_TREND_SPEC_COUNT = 0
EXP11B_SUPERPOPULATION_INFERENCE_SPEC_COUNT = 0
HE5_POSTHOC_INSUFFICIENCY_THRESHOLD_COUNT = 0
TRUNCATED_AXIS_SPEC_COUNT = 0
DUAL_Y_AXIS_SPEC_COUNT = 0
```

---

## 15. Rama candidata y publicación

Crea desde `main` exacto:

```text
branch = codex/group6-f01-figure-spec-registry-v01
base = ca065618d5df0019f76ef5a971e858d91c263e1f
```

Añade **únicamente**:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

No añadas figuras, scripts, Markdown auxiliar ni outputs adicionales.

Debe quedar:

```text
CANDIDATE_PARENT = ca065618d5df0019f76ef5a971e858d91c263e1f
CANDIDATE_COMMITS_AHEAD = 1
CANDIDATE_COMMITS_BEHIND = 0
CANDIDATE_CHANGED_PATH_COUNT = 1
```

Haz un único commit candidato y push normal.

`main` no debe modificarse en Prompt103.

---

## 16. Postejecución en fichas

Después de publicar el candidato, trabaja nuevamente sobre la rama de fichas, partiendo del commit de activación creado en este Prompt103.

Modifica exclusivamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Deja:

```text
G6-F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
```

Registra:

```text
FICHA = G6-F01
PROMPT103_SOURCE = <commit fuente real>
ACTIVATION_COMMIT = <commit>
CANDIDATE_BRANCH = codex/group6-f01-figure-spec-registry-v01
CANDIDATE_COMMIT = <commit>
CANDIDATE_PARENT = ca065618d5df0019f76ef5a971e858d91c263e1f
FIGURE_SPEC_REGISTRY_BLOB = <blob>
FIGURE_SPEC_COUNT = 6
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false
PENDING_EXTERNAL_AUDIT = true
```

Haz un único commit administrativo y push normal.

No modifiques el Plan Maestro en esta ejecución.

---

## 17. Reporte terminal obligatorio

Crea y publica en `codex/prompts-temporary`:

```text
codex_prompts_tmp/103_RESPUESTA_ACTIVAR_Y_EJECUTAR_G6_F01_CATALOGO_Y_ESPECIFICACION_FIGURAS.md
```

El reporte debe incluir, como mínimo:

```text
PROMPT103 = COMPLETED

WORKSPACE_ROOT_OBSERVED
WORKSPACE_ROOT_MATCH_EXPECTED
WORKSPACE_ORIGIN_URL
WORKSPACE_INITIAL_BRANCH
WORKSPACE_INITIAL_HEAD
WORKSPACE_INITIAL_DIRTY_COUNT
USER_CANONICAL_LOCAL_PATH_FROZEN
LOCAL_PERSISTENCE_IN_USER_FOLDER_ASSERTED

PREFLIGHT_MAIN
PREFLIGHT_PLAN
PREFLIGHT_FICHAS
ARTICLE_HEAD_PREFLIGHT
PROMPT103_COMMIT

RPRE_* = PASS/FAIL

ACTIVATION_FICHAS_COMMIT

CANDIDATE_BRANCH
CANDIDATE_COMMIT
CANDIDATE_PARENT
CANDIDATE_TREE
CANDIDATE_COMMITS_AHEAD
CANDIDATE_COMMITS_BEHIND
CANDIDATE_CHANGED_PATH_COUNT
FIGURE_SPEC_REGISTRY_BLOB

EXPECTED_FIGURE_SPEC_COUNT = 6
FIGURE_SPEC_COUNT = 6
EXPECTED_CANONICAL_TABLE_PRESENTATION_COUNT = 9
ACCOUNTED_CANONICAL_TABLE_PRESENTATION_COUNT = 9
FIGURE_MAPPED_CANONICAL_PRESENTATION_COUNT = 6
TABLE_ONLY_CANONICAL_PRESENTATION_COUNT = 3
FAVORABILITY_BASED_SELECTION_COUNT = 0
UNJUSTIFIED_OMISSION_COUNT = 0
SUPERSEDED_SOURCE_USED_COUNT = 0
NEW_SCIENTIFIC_METRIC_VALUE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
FIGURE_FILE_CREATED_COUNT = 0
FIGURE_SCRIPT_CREATED_COUNT = 0
HE2A_ABSOLUTE_ARM_CI_CREATED_COUNT = 0
HE2A_PAIRED_CI_BOUND_CORRECTLY = true
HE2B_CI_LEVEL_PRESERVED = true
EXP11A_CAUSAL_TREND_SPEC_COUNT = 0
EXP11B_SUPERPOPULATION_INFERENCE_SPEC_COUNT = 0
HE5_POSTHOC_INSUFFICIENCY_THRESHOLD_COUNT = 0
TRUNCATED_AXIS_SPEC_COUNT = 0
DUAL_Y_AXIS_SPEC_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false
EXP12_PERFORMANCE_FIGURE_COUNT = 0
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
MAIN_MODIFIED = false
PLAN_MODIFIED = false
G6_F02_AUTHORIZED = false
G6_F02_STARTED = false

POSTEXECUTION_FICHAS_COMMIT
G6_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
G6_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED

FINAL_ORIGIN_MAIN
FINAL_ORIGIN_PLAN
FINAL_ORIGIN_FICHAS
ARTICLE_HEAD_FINAL_OBSERVED
WORKSPACE_FINAL_BRANCH
WORKSPACE_FINAL_HEAD
WORKSPACE_FINAL_DIRTY_COUNT
BLOCKERS
WARNINGS
```

El commit del reporte debe añadir únicamente ese archivo y tener como padre el commit fuente de Prompt103 vigente en `codex/prompts-temporary`.

---

## 18. Estado terminal esperado

Si todo pasa:

```text
G6_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
G6_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F02_AUTHORIZED = false
```

No integres el candidato a `main` todavía. No ejecutes G6-F02.