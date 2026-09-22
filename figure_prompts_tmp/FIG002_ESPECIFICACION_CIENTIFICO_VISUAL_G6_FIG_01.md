# FIG002 — ESPECIFICACIÓN CIENTÍFICO-VISUAL DE G6-FIG-01

## 0. Rol y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto de tesis.

Ejecuta exclusivamente FIG002.

FIG001 fue auditado externamente y queda aprobado como base conceptual para continuar. El catálogo preliminar aprobado reduce las seis figuras iniciales a tres figuras recomendadas y dispone el resto como tabla/texto. Para FIG002 debes trabajar únicamente sobre la primera figura recomendada:

```text
G6-FIG-01 — Evidencia primaria de HE2: ranking temprano y cobertura profunda
```

FIG002 no genera una imagen. Su objetivo es cerrar la **especificación científica y visual exacta** que posteriormente podrá implementarse de forma reproducible.

No autoriza:

- generar PNG, SVG, PDF u otra figura final;
- generar mockups raster o vectoriales finales;
- escribir scripts Python;
- modificar `main`;
- modificar Plan Maestro;
- modificar fichas;
- modificar artículo o tesis;
- recalcular métricas, deltas científicos, CI, p-values o inferencia;
- crear incertidumbre nueva;
- redecidir HE2 o HE5;
- reabrir EXP12;
- usar resultados superseded;
- ejecutar G6-F02;
- diseñar todavía G6-FIG-02 o G6-FIG-03.

---

## 1. Trazabilidad obligatoria

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Rama de prompts/respuestas de esta IA:

```text
codex/prompts-temporary
```

FIG001 aprobado:

```text
figure_prompts_tmp/FIG001_RESPUESTA_REVISION_CRITICA_CATALOGO_INICIAL.md
commit = 2c31d0c7112abedab224023b33d8173f116b3712
```

Prompt FIG001:

```text
figure_prompts_tmp/FIG001_REVISION_CRITICA_CATALOGO_INICIAL.md
commit = b47fee61a58b345d6ca1e48058f97704b2b2244e
```

Refs rectoras vigentes al diseñar FIG002:

```text
main = ca065618d5df0019f76ef5a971e858d91c263e1f
plan = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
fichas = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
```

Antes de emitir la respuesta, verifica que las fuentes científicas citadas continúan presentes con los blobs congelados indicados abajo. Si existe drift científico material, detén la especificación y repórtalo.

---

## 2. Fuentes científicas obligatorias

### 2.1 Tabla primaria HE2_A

```text
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
blob = cb68583ee2260e4455796bac99ad90995ca7ef92
```

Contiene 15 filas:

```text
3 comparaciones × 5 métricas primarias
```

Comparaciones:

```text
HISTORICAL_MINUS_FLAT
HISTORICAL_MINUS_HIERARCHICAL
HISTORICAL_MINUS_D1A
```

Métricas:

```text
Top-1
Top-3
Top-5
Top-10
MRR@100
```

Columnas científicamente relevantes:

```text
comparison
metric
historical_observed_value
comparator_observed_value
paired_difference_historical_minus_comparator
frozen_99pct_ci_lower_for_paired_difference
frozen_99pct_ci_upper_for_paired_difference
EVAL_N
DAM_N
source_version
```

### 2.2 Tabla primaria HE2_B

```text
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
blob = 359e4e19b5ef1d44983c03039162209293b2a44c
```

Fila congelada:

```text
comparison = HIERARCHICAL_RECALL_200_MINUS_100
Recall@100 = 0.10132575757575757
Recall@200 = 0.3039772727272727
paired difference = 0.20265151515151514
frozen CI lower = 0.06676310583580614
frozen CI upper = 0.34160130792395144
Pool@200 context = 0.3039772727272727
EVAL_N = 1056
DAM_N = 67
```

### 2.3 Registro de claims controlados

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
blob = da0351cb523fc7f3b45a83e072765a07f809b7fe
```

Claims vinculados:

```text
G3C-001
Historical retrieval is superior to corrected flat normative retrieval for the five primary early-ranking metrics under the frozen HE2_A rule.

G3C-002
Historical retrieval is superior to corrected hierarchical normative retrieval for the five primary early-ranking metrics under the frozen HE2_A rule.

G3C-003
Historical retrieval is superior to corrected D1a retrieval for the five primary early-ranking metrics under the frozen HE2_A rule.

G3C-004
Corrected hierarchical coverage increases from Recall@100 to Recall@200 under the frozen HE2_B primary contrast.
```

### 2.4 Registros de presentación y cierre

Consulta además:

```text
outputs/results/group5/g5_table_registry_v0.1.json
blob = 4fe9318d52fad093066ff9f42d524fc95e436245

docs/results/group5/g5_results_presentation_plan_v0.1.md
blob = 9eaf780f3a2f6c8579dc80867ed3a86e96683894

docs/results/group5/g5_canonical_tables_v0.1.md
blob = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d

outputs/audits/group5_closure_v0.1.json
blob = 1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf
```

---

## 3. Contrato científico inmutable

Preserva exactamente:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42

HE2 = SUPPORTED
```

HE2_A:

- los valores absolutos por brazo son observaciones descriptivas del benchmark;
- los `point_estimate`/`paired_difference` y los CI de 99% pertenecen exclusivamente al contraste pareado histórico menos comparador;
- no existe CI por brazo autorizado;
- los contrastes son no causales;
- Top-50 no forma parte de las cinco métricas primarias de esta figura.

HE2_B:

- existe un único contraste primario Recall@200 menos Recall@100;
- su CI congelado es de 95%;
- `Pool@200 context` no es un segundo contraste confirmatorio;
- no debe duplicarse como evidencia independiente.

Guardrails:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

Attempt06 vigente:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
OVERALL = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

---

## 4. Decisión de FIG001 que FIG002 debe desarrollar

FIG001 aprobó conceptualmente:

```text
G6-FIG-01 = MERGE(HE2_A, HE2_B)
DESTINO = PRINCIPAL
ROL = PRIMARY_INFERENTIAL
CLAIMS = G3C-001, G3C-002, G3C-003, G3C-004
```

La fusión no es todavía una obligación de cuatro paneles. FIG002 debe decidir la composición exacta que mejor preserve la claridad científica.

Puedes proponer:

```text
2 paneles
3 paneles
4 paneles
```

pero debes justificar la decisión.

No puedes volver a separar HE2_B como una figura autónoma salvo que demuestres que la fusión produce un problema científico o visual serio. Si recomiendas separación, debes marcarlo como `REVISION_OF_FIG001_REQUIRED` y justificarlo explícitamente.

---

## 5. Preguntas que FIG002 debe resolver

### 5.1 Arquitectura general

Determina:

- número exacto de paneles;
- relación espacial entre paneles;
- orden de lectura;
- qué panel comunica valores absolutos;
- qué panel comunica diferencias pareadas;
- dónde y cómo integrar HE2_B;
- si la figura será horizontal o vertical;
- relación de aspecto recomendada;
- jerarquía visual entre HE2_A y HE2_B.

### 5.2 Panel de desempeño absoluto HE2_A

Debes decidir el diseño óptimo para mostrar:

```text
Historical
Flat Attempt06
Hierarchical Attempt06
D1a Attempt06
```

en:

```text
Top-1
Top-3
Top-5
Top-10
MRR@100
```

Restricciones:

- escala de desempeño absoluta entre 0 y 1;
- no CI por brazo;
- no líneas que unan métricas como si formaran una trayectoria continua;
- no usar área, volumen o 3D;
- no usar eje truncado que exagere diferencias;
- Historical no debe repetirse tres veces de forma que induzca pseudorreplicación visual;
- debe seguir siendo posible distinguir los tres comparadores corregidos.

Evalúa críticamente al menos estas alternativas:

```text
A. dot plot agrupado
B. barras agrupadas
C. small multiples por métrica
```

Selecciona una y justifica por qué las otras son inferiores.

### 5.3 Panel de contrastes pareados HE2_A

Debe mostrar los 15 contrastes:

```text
Historical − Flat
Historical − Hierarchical
Historical − D1a
```

para las cinco métricas primarias, con:

```text
paired_difference_historical_minus_comparator
CI 99%
```

Restricciones:

- debe existir referencia visual en cero;
- el CI corresponde al contraste, no a los brazos;
- no deben omitirse contrastes;
- no ordenar por magnitud observada si eso rompe el orden predefinido de métricas/comparadores;
- no usar significancia por asteriscos como sustituto del CI;
- no mostrar p-values inexistentes;
- no mezclar CI 99% de HE2_A con CI 95% de HE2_B sin etiqueta explícita.

Evalúa al menos:

```text
A. forest plot
B. dot-whisker grouped plot
C. heatmap de diferencias
```

Selecciona una alternativa y justifica.

### 5.4 Integración de HE2_B

Debes decidir la forma exacta de integrar:

```text
Recall@100 = 0.1013
Recall@200 = 0.3040
Δ = 0.2027
CI95% = [0.0668, 0.3416]
```

sin dar a `Pool@200 context` un rol confirmatorio adicional.

Evalúa críticamente:

```text
A. mini-panel con dos valores absolutos + un mini forest del contraste
B. un solo panel de contraste con anotación de Recall@100/Recall@200
C. bloque textual dentro de la figura acompañado de un único estimando gráfico
```

Selecciona una solución.

La diferencia de nivel de CI debe quedar visible:

```text
HE2_A = 99% CI
HE2_B = 95% CI
```

### 5.5 Codificación visual y accesibilidad

Define:

- uso de color;
- necesidad de símbolos/formas redundantes;
- orden de leyenda;
- si la figura debe funcionar en escala de grises;
- tamaño mínimo de fuente recomendado;
- grosor relativo de líneas de CI;
- tratamiento de gridlines;
- tratamiento de cero en contrastes;
- cómo evitar dependencia exclusiva del color;
- cómo distinguir Historical / Flat / Hierarchical / D1a.

No fijes colores hexadecimales todavía salvo que exista una razón científica/estandarizada imprescindible. La paleta definitiva puede congelarse al generar las figuras.

### 5.6 Ejes, escalas y unidades

Para cada panel especifica:

```text
x_axis
x_scale
x_range
y_axis
y_order
unit
reference_lines
axis_breaks = prohibited/allowed with justification
```

Por defecto:

```text
absolute performance range = [0,1]
```

Cualquier desviación debe justificarse expresamente.

### 5.7 Etiquetas y anotaciones

Decide:

- nombres abreviados de comparadores;
- nombres de métricas;
- si mostrar valores numéricos junto a puntos;
- número de decimales;
- si mostrar `N=1056` y `67 DAM` dentro de la figura o reservarlo al caption;
- cómo etiquetar `99% CI` y `95% CI` sin ambigüedad;
- cómo mantener visible que los contrastes son `Historical − comparator`.

No añadas interpretaciones causales ni jurídicas.

### 5.8 Caption de trabajo

FIG002 puede redactar un **caption de trabajo**, no definitivo.

Debe contener como mínimo:

- benchmark interno Capítulo 87;
- N=1056 series;
- 67 DAM;
- naturaleza no causal de los contrastes;
- HE2_A: cinco métricas primarias, tres comparadores, CI 99% para diferencias pareadas;
- HE2_B: Recall@200 − Recall@100, CI 95%;
- ausencia de CI por brazo;
- nota de que la figura no representa exactitud global del RAG.

Debe ser compacto y apto para revisión posterior en G6-F03.

---

## 6. Riesgos que debes auditar antes del dictamen

Emite PASS/FAIL para:

```text
FIG002_HE2A_ABSOLUTE_VS_CONTRAST_SEPARATION
FIG002_HE2A_CI_BOUND_TO_PAIRED_DIFFERENCE_ONLY
FIG002_HE2B_95CI_SEPARATED_FROM_HE2A_99CI
FIG002_POOL200_NOT_DUPLICATED_AS_CONFIRMATORY
FIG002_NO_ARM_LEVEL_CI
FIG002_NO_TRUNCATED_ABSOLUTE_AXIS
FIG002_NO_METRIC_TRAJECTORY_IMPLICATION
FIG002_NO_PSEUDOREPLICATION_OF_HISTORICAL
FIG002_NO_CHERRY_PICKING
FIG002_NO_NEW_METRICS
FIG002_NO_NEW_INFERENCE
FIG002_NO_GLOBAL_RAG_ACCURACY_OVERCLAIM
FIG002_ACCESSIBLE_WITHOUT_COLOR_ONLY
```

Si algún control queda FAIL, no declares la especificación lista para implementación.

---

## 7. Contenido mínimo de la respuesta

La respuesta debe contener:

### A. Dictamen de composición

```text
FIGURE_ID
FINAL_PANEL_COUNT
ORIENTATION
RECOMMENDED_ASPECT_RATIO
READING_ORDER
MERGE_HE2A_HE2B = true/false
```

### B. Especificación panel por panel

Para cada panel:

```text
panel_id
scientific_question
claim_ids
source_path
source_blob
rows/columns used
chart_type
marks
x_axis
y_axis
scale/range
reference lines
encoding
legend
uncertainty
annotations
forbidden transformations
risk controls
```

### C. Comparación de alternativas descartadas

Debe demostrar que la selección del tipo de gráfico fue deliberada y no arbitraria.

### D. Especificación de accesibilidad

Debe quedar suficientemente concreta para que G6-F02 pueda implementarla sin reinterpretar el diseño.

### E. Caption de trabajo

Caption preliminar sujeto a G6-F03.

### F. Checklist de controles

Los 13 controles FIG002 con PASS/FAIL y justificación breve.

### G. Disposición terminal

Una de:

```text
APPROVABLE_FOR_IMPLEMENTATION_SPEC
REVISION_REQUIRED
REVISION_OF_FIG001_REQUIRED
```

`APPROVABLE_FOR_IMPLEMENTATION_SPEC` no autoriza todavía generar la figura. Solo indica que su contrato visual está listo para auditoría externa.

---

## 8. Regla de no avance

FIG002 termina con la especificación detallada de G6-FIG-01.

No generes la figura.
No escribas scripts.
No avances a G6-FIG-02.
No avances a G6-F02.

El siguiente paso solo será definido después de auditoría externa de FIG002.

---

## 9. Persistencia obligatoria

Guarda la respuesta oficial en:

```text
branch = codex/prompts-temporary
path = figure_prompts_tmp/FIG002_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_01.md
```

Crea únicamente ese archivo en esta rama.

No modifiques FIG001, FIG002 ni ningún otro archivo.

Commit recomendado:

```text
figures: record FIG002 G6-FIG-01 specification
```

Al terminar, responde en el chat únicamente con:

```text
Rama: codex/prompts-temporary

Archivo de respuesta:
figure_prompts_tmp/FIG002_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_01.md

Commit:
<SHA>
```

No pegues el contenido completo en el chat.
