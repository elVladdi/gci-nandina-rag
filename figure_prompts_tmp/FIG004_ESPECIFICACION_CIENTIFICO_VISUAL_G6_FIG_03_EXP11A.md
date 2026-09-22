# FIG004 — ESPECIFICACIÓN CIENTÍFICO-VISUAL DE G6-FIG-03 (EXP11A)

## 0. Rol y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto de tesis.

Ejecuta exclusivamente FIG004.

FIG001 fue auditado externamente y aprobó un catálogo preliminar de tres figuras. FIG002 aprobó la especificación de `G6-FIG-01`. FIG003 aprobó la especificación de `G6-FIG-02`. En FIG004 debes trabajar únicamente sobre:

```text
G6-FIG-03 — Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A)
```

FIG004 **no genera todavía una imagen**. Debe cerrar la especificación científico-visual exacta de esta figura para una implementación reproducible posterior.

No autoriza:

- generar PNG, SVG, PDF o mockup final;
- escribir scripts Python;
- modificar `main`, Plan Maestro, fichas, artículo o tesis;
- recalcular métricas, promedios, diferencias, CI, p-values o inferencia;
- crear nuevos agregados científicos;
- interpretar EXP11A como un experimento causal de tamaño;
- afirmar una relación monotónica tamaño→desempeño;
- redecidir HE2 o HE5;
- diseñar nuevas figuras fuera del catálogo aprobado;
- ejecutar G6-F02.

---

## 1. Trazabilidad obligatoria

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Rama de prompts/respuestas:

```text
codex/prompts-temporary
```

FIG001 aprobado:

```text
figure_prompts_tmp/FIG001_RESPUESTA_REVISION_CRITICA_CATALOGO_INICIAL.md
commit = 2c31d0c7112abedab224023b33d8173f116b3712
```

FIG002 aprobado:

```text
figure_prompts_tmp/FIG002_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_01.md
commit = d2f9e07923789709a52622bea922be84aefc526d
```

FIG003 aprobado:

```text
figure_prompts_tmp/FIG003_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_02_PHASE_E.md
commit = a9059e9a22a33e7a088ac832d00fcb941a49e4b7
```

Refs científicas vigentes al diseñar FIG004:

```text
main = ca065618d5df0019f76ef5a971e858d91c263e1f
plan = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
fichas = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
```

Si existe drift científico material en las fuentes gobernadas, detén la especificación y repórtalo.

---

## 2. Fuentes científicas obligatorias

### 2.1 Tabla canónica EXP11A

```text
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403
```

Columnas gobernadas:

```text
row_key
row type
condition
run/seed
bank composition
denominator
Top1
Top3
Top5
Top10
Top50
MRR
source version
```

Debes verificar directamente la estructura completa del CSV y contabilizar por separado:

```text
OBSERVED_RUN
FROZEN_CONDITION_SUMMARY
```

Como control mínimo esperado, verifica si el inventario observado corresponde a:

```text
H25  = 10 observed runs
H50  = 10 observed runs, con dos composiciones D1/D2 de 5 corridas cada una
H75  = 10 observed runs
H100 = 1 frozen-reference observed run
```

No tomes estos conteos como ciertos sin verificarlos en el CSV.

La columna `bank composition` conserva metadatos ya materializados como:

```text
rows
DAM
HHI
coverage
sha256
```

No derives nuevos indicadores desde esos campos.

### 2.2 Claim controlado

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
blob = da0351cb523fc7f3b45a83e072765a07f809b7fe
```

Claim rector:

```text
G3C-007
EXP11A measures joint bank-size/composition sensitivity.
```

Contrato del claim:

```text
claim_type = SENSITIVITY
hypothesis_link = NONE
evidence_class = SENSITIVITY
uncertainty_status = DESCRIPTIVE_NO_CI_AUTHORIZED
allowed_strength = DESCRIPTIVE_SENSITIVITY
causal_status = NONCAUSAL
scope = H25/H50/H75 plus frozen H100 reference
mandatory_limitation = Size and composition are coupled
forbidden_overclaim = Do not claim an isolated causal size effect
```

### 2.3 Limitaciones rectoras

Consulta también:

```text
outputs/analysis/group4/g4_limitations_registry_v0.1.json
blob = ae00b93431e912cb78a58344057d9bf7a51fcd47

outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245

docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

docs/results/group5/g5_appendix_registry_v0.1.md
blob = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a

outputs/audits/group5_closure_v0.1.json
blob = 1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf
```

Si necesitas resolver la semántica exacta de D1/D2 o de los summaries, consulta las fuentes originales ya registradas en el `source version`, pero no uses fuentes superseded.

---

## 3. Contrato científico inmutable

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
```

Para EXP11A:

```text
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
```

Esto implica:

- tamaño y composición del banco varían conjuntamente;
- no se identifica un efecto causal aislado del tamaño;
- H25/H50/H75/H100 no deben interpretarse como niveles de dosis de una intervención;
- no se autoriza regresión, trend fit, smooth, interpolación ni slope causal;
- no se autoriza CI nuevo;
- no se autoriza inferencia sobre una superpoblación de bancos;
- los summaries ya congelados pueden usarse solo si su identidad y significado se verifican inequívocamente;
- no se puede calcular un nuevo summary, delta o promedio para facilitar la gráfica.

Guardrails globales:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

---

## 4. Decisión de FIG001 que FIG004 debe desarrollar

FIG001 aprobó conceptualmente:

```text
G6-FIG-03 = KEEP + MODIFY + MOVE_TO_APPENDIX
ROL = DESCRIPTIVE_SENSITIVITY / NONCAUSAL
DESTINO = APPENDIX
CLAIM = G3C-007
```

También detectó un riesgo específico:

```text
H50 contiene composiciones D1/D2 materialmente distintas.
```

La figura no puede colapsar esa heterogeneidad de forma que sugiera que toda la variación responde únicamente al tamaño H50.

FIG004 debe decidir cómo preservar de forma visual suficiente la dimensión composicional sin convertir el gráfico en una visualización multivariable ilegible.

---

## 5. Preguntas que FIG004 debe resolver

### 5.1 Inventario y trazabilidad de corridas

Antes de diseñar:

1. contabiliza todos los `OBSERVED_RUN` por condición;
2. identifica de manera documental las corridas H50-D1 y H50-D2;
3. identifica la única referencia H100 si efectivamente existe como `OBSERVED_RUN` congelado;
4. contabiliza y clasifica todos los `FROZEN_CONDITION_SUMMARY`;
5. determina si los summaries H50 permiten distinguir D1/D2 inequívocamente por campos congelados o si deben permanecer fuera de la figura por ambigüedad de identificación;
6. no infieras etiquetas D1/D2 desde el orden de filas.

Emite:

```text
OBSERVED_RUN_COUNT_TOTAL
OBSERVED_RUN_COUNTS_BY_CONDITION
H50_D1_RUN_COUNT
H50_D2_RUN_COUNT
FROZEN_SUMMARY_COUNT_TOTAL
H50_SUMMARY_TRACEABILITY = PASS / FAIL / PARTIAL
```

Si una parte de la semántica no puede resolverse con fuentes congeladas, decláralo y diseña la figura sin usar esa parte.

### 5.2 Necesidad y arquitectura visual

Confirma que la figura sigue aportando comprensión frente a la tabla.

Determina:

- número exacto de paneles;
- orientación;
- relación de aspecto;
- orden de lectura;
- si las seis métricas deben aparecer;
- si conviene small multiples;
- si H100 debe visualizarse como referencia aparte;
- cómo representar H50-D1/H50-D2 sin insinuar que las demás condiciones tienen composición fija.

La solución debe ser apta para anexo de tesis, no para convertir EXP11A en resultado primario.

### 5.3 Tipo de gráfico

Evalúa críticamente al menos:

```text
A. seis small multiples, uno por métrica, con puntos de corridas observadas por condición
B. heatmap corrida × métrica
C. parallel-coordinates / spaghetti multimetric
D. solo summaries congelados por condición
```

Puedes proponer otra alternativa si está mejor justificada.

Debes privilegiar la visibilidad de la dispersión observada sin crear una lectura causal tamaño→desempeño.

### 5.4 Eje de condición y dimensión composicional

Decide si el eje categórico debe usar, por ejemplo:

```text
H25
H50-D1
H50-D2
H75
H100 reference
```

o alguna alternativa científicamente mejor.

Pero recuerda:

- H25, H75 y H100 también tienen composición propia;
- D1/D2 son una distinción explícita dentro de H50, no una licencia para describir las otras condiciones como composicionalmente homogéneas;
- `bank composition` contiene `rows`, `DAM`, `HHI` y `coverage`, pero no debes crear nuevas categorías post hoc a partir de esos valores.

Define cómo comunicarás en panel/leyenda/caption que el eje representa **condiciones observadas de banco**, no un factor causal puro de tamaño.

### 5.5 Métricas y escalas

Métricas congeladas:

```text
Top1
Top3
Top5
Top10
Top50
MRR
```

Para cada panel o codificación determina:

```text
metric label
scale
range
unit
reference marks
```

Regla por defecto para métricas absolutas de rendimiento:

```text
range = [0,1]
```

Cualquier desviación debe justificarse fuertemente. No truncar ejes para magnificar variación entre corridas.

### 5.6 Corridas, summaries y H100

Debes resolver si mostrar:

- puntos de todas las corridas observadas;
- summaries congelados como marcas adicionales;
- solo corridas observadas;
- H100 como punto de referencia separado.

Reglas:

- no ocultar dispersión observada detrás de un summary;
- no calcular error bars alrededor de summaries;
- no inventar CI;
- no usar summaries ambiguos;
- no tratar H100 de una sola corrida como equivalente a una distribución de 10 réplicas;
- si se muestran summaries, deben distinguirse claramente de corridas individuales y estar vinculados a artefactos congelados.

### 5.7 Codificación visual y accesibilidad

Define:

- marcador de corrida individual;
- marcador de summary, si se usa;
- tratamiento específico H50-D1/H50-D2;
- tratamiento de H100 reference;
- uso secundario del color;
- símbolos redundantes;
- orden de leyenda;
- legibilidad en escala de grises;
- tamaño mínimo de fuente;
- gridlines;
- necesidad o no de jitter determinista.

Si usas jitter, debe ser **determinista y exclusivamente visual**, no aleatorio ni asociado a un valor científico.

No uses tamaño de punto, saturación u opacidad para codificar “mejor”/“peor”.

### 5.8 Información composicional

Decide qué información de:

```text
rows
DAM
HHI
coverage
```

debe aparecer:

- en el panel;
- en la leyenda;
- en el caption;
- o permanecer solo en la tabla canónica.

La figura debe preservar el mensaje de acoplamiento tamaño/composición, pero no debe convertirse en una gráfica de cuatro covariables simultáneas.

No derives correlaciones ni relaciones entre HHI/cobertura y desempeño.

### 5.9 Caption de trabajo

Redacta un caption preliminar que incluya obligatoriamente:

- EXP11A;
- benchmark interno offline del Capítulo 87;
- 1,056 series / 67 DAM / 42 NANDINA;
- sensibilidad conjunta de tamaño y composición;
- H25/H50/H75 y H100 frozen reference;
- naturaleza descriptiva/no causal;
- número de corridas observadas por condición;
- tratamiento H50-D1/H50-D2;
- advertencia de que H100 es una única referencia si eso se verifica;
- ausencia de CI/test inferencial nuevo;
- prohibición de interpretar el eje como efecto causal aislado del tamaño.

El caption definitivo se revisará en G6-F03.

---

## 6. Contrato machine-readable conceptual de la figura

La respuesta debe cerrar una especificación equivalente a:

```text
figure_id
working_title
scientific_role
destination
claim_ids
source_path
source_blob
observed_run_inventory
frozen_summary_inventory
panel_count
panel_metrics
chart_type
condition_axis
condition_order
h50_d1_d2_encoding
h100_reference_policy
x_axis_or_category_axis
y_axis
y_range
unit
marks
summary_policy
composition_context_policy
legend_order
uncertainty_policy
numeric_label_policy
caption_working
forbidden_transformations
accessibility_requirements
implementation_validation_checks
```

No escribas todavía JSON operativo ni scripts; esta es la especificación conceptual auditada que posteriormente se consolidará.

---

## 7. Controles obligatorios de auditoría FIG004

Emite PASS/FAIL para:

```text
FIG004_SOURCE_BLOB_IDENTITY
FIG004_G3C007_TRACEABILITY
FIG004_OBSERVED_RUN_INVENTORY_COMPLETE
FIG004_H50_D1_D2_RESOLVED
FIG004_H100_REFERENCE_ROLE_PRESERVED
FIG004_FROZEN_SUMMARY_INVENTORY_COMPLETE
FIG004_NO_AMBIGUOUS_SUMMARY_USED
FIG004_ALL_SIX_METRICS_ACCOUNTED
FIG004_RUN_LEVEL_DISPERSION_VISIBLE
FIG004_SIZE_COMPOSITION_COUPLING_VISIBLE
FIG004_NO_ISOLATED_SIZE_CAUSAL_CLAIM
FIG004_NO_MONOTONIC_DOSE_RESPONSE_IMPLICATION
FIG004_NO_NEW_AGGREGATION
FIG004_NO_NEW_CI
FIG004_NO_P_VALUE
FIG004_NO_REGRESSION_OR_SMOOTH
FIG004_NO_CHERRY_PICKING
FIG004_AXIS_INTEGRITY
FIG004_ACCESSIBLE_WITHOUT_COLOR_ONLY
FIG004_NO_ARTICLE_OR_THESIS_MODIFICATION
FIG004_NO_G6_F02_EXECUTION
```

Si un control material falla, no cierres la especificación como aprobable. Explica el bloqueo.

---

## 8. Regla de no avance

FIG004 termina con la especificación de `G6-FIG-03`.

No:

- generes la figura;
- escribas código;
- consolides todavía el registro final G6-F01;
- actualices fichas o Plan;
- ejecutes G6-F02.

El siguiente paso será definido después de auditoría externa de FIG004.

---

## 9. Persistencia obligatoria de respuesta

La respuesta oficial debe almacenarse en:

```text
branch = codex/prompts-temporary
path = figure_prompts_tmp/FIG004_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_03_EXP11A.md
```

Debes crear únicamente ese archivo en esta rama para la respuesta de FIG004.

No modifiques FIG004 ni ningún otro archivo.

Commit recomendado:

```text
figures: record FIG004 EXP11A specification
```

Al terminar, responde en el chat únicamente con:

```text
Rama: codex/prompts-temporary

Archivo de respuesta:
figure_prompts_tmp/FIG004_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_03_EXP11A.md

Commit:
<SHA>
```

No pegues nuevamente el contenido completo de la respuesta en el chat.
