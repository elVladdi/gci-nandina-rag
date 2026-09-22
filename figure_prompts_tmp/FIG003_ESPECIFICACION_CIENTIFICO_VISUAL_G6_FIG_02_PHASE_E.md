# FIG003 — ESPECIFICACIÓN CIENTÍFICO-VISUAL DE G6-FIG-02 (PHASE E)

## 0. Rol y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto de tesis.

Ejecuta exclusivamente FIG003.

FIG001 fue auditado externamente y aprobó un catálogo preliminar de tres figuras. FIG002 fue auditado externamente y aprobó la especificación de `G6-FIG-01`. En FIG003 debes trabajar únicamente sobre:

```text
G6-FIG-02 — Cobertura exacta NANDINA de Phase E según profundidad y variante
```

FIG003 **no genera todavía una imagen**. Debe cerrar la especificación científico-visual exacta de esta figura para una implementación reproducible posterior.

No autoriza:

- generar PNG, SVG, PDF o mockup final;
- escribir scripts Python;
- modificar `main`, Plan Maestro, fichas, artículo o tesis;
- recalcular métricas, porcentajes, diferencias, CI, p-values o inferencia;
- crear nuevos agregados científicos;
- promover Phase E a evidencia confirmatoria;
- redecidir HE2;
- incorporar el diagnostic union como rendimiento ordinario;
- diseñar G6-FIG-03;
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

Refs científicas vigentes al diseñar FIG003:

```text
main = ca065618d5df0019f76ef5a971e858d91c263e1f
plan = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
fichas = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
```

Si existe drift científico material en las fuentes gobernadas, detén la especificación y repórtalo.

---

## 2. Fuentes científicas obligatorias

### 2.1 Tabla canónica Phase E

```text
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
```

Contiene 15 filas:

```text
5 variantes × 3 profundidades (50, 100, 200)
```

Valores congelados que debes verificar directamente en GitHub:

```text
hierarchical_only
  depth 50  = 0.09090909090909091
  depth 100 = 0.10132575757575757
  depth 200 = 0.3039772727272727

dual_only
  depth 50  = 0.09185606060606061
  depth 100 = 0.10037878787878787
  depth 200 = 0.26609848484848486

hierarchical_first_100
  depth 50  = 0.09090909090909091
  depth 100 = 0.10132575757575757
  depth 200 = 0.26515151515151514

hierarchical_80_dual_backfill_20
  depth 50  = 0.09090909090909091
  depth 100 = 0.10132575757575757
  depth 200 = 0.3039772727272727

hierarchical_70_dual_backfill_30
  depth 50  = 0.09090909090909091
  depth 100 = 0.10227272727272728
  depth 200 = 0.3039772727272727
```

Columnas gobernadas:

```text
pool role
variant
depth
cases
nominal_size
effective_size_mean
exact_numerator
denominator
exact-NANDINA coverage
source version
```

No derives ninguna métrica adicional.

### 2.2 Claim controlado

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
blob = da0351cb523fc7f3b45a83e072765a07f809b7fe
```

Claim rector:

```text
G3C-005
The four A_historical_defined Phase E variants show descriptively increasing exact-NANDINA pool coverage at depths 50, 100, and 200.
```

Contrato del claim:

```text
claim_type = DESCRIPTIVE
hypothesis_link = HE2_B
evidence_class = DESCRIPTIVE
uncertainty_status = DESCRIPTIVE_NO_CI_AUTHORIZED
allowed_strength = DIRECTIONALLY_CONSISTENT_DESCRIPTIVE
causal_status = NONCAUSAL_DESCRIPTIVE
mandatory_limitation = No CI, p-value, or inferential contrast
forbidden_overclaim = Do not promote Phase E to confirmatory inference
```

### 2.3 Registros de presentación

Consulta también:

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

### 2.4 Diagnostic union — solo para exclusión/guardrail

```text
outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv
blob = f43cce08d1d7bc3cef64698dbebf14eae4b26ed5
```

Este artefacto es `DIAGNOSTIC_ONLY`. No debe agregarse como una sexta curva ordinaria ni tratarse como otra variante de rendimiento.

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
```

Para Phase E:

- los resultados son descriptivos;
- no existe CI autorizado;
- no existen p-values autorizados;
- no existe contraste inferencial autorizado entre variantes;
- no existe autorización para declarar una variante como “mejor” mediante prueba estadística;
- la figura no puede cambiar la disposición de HE2;
- la profundidad 50/100/200 es un parámetro de recuperación, no tiempo;
- `diagnostic_union` es un techo diagnóstico y no una sexta variante de rendimiento.

Guardrails globales:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

---

## 4. Ambigüedad que FIG003 debe resolver obligatoriamente

FIG001 detectó una tensión de trazabilidad:

```text
G3C-005 = cuatro variantes A_historical_defined
CSV canónico = cinco variantes, incluyendo dual_only
```

Antes de definir la figura debes verificar en las fuentes congeladas cuáles cuatro variantes corresponden formalmente a `A_historical_defined` y cuál variante queda como contexto descriptivo adicional.

No lo infieras solo por el nombre.

Debes emitir explícitamente:

```text
FORMAL_G3C005_VARIANTS = [...]
CONTEXT_ONLY_VARIANTS = [...]
TRACEABILITY_RESOLUTION = PASS / FAIL
```

Si las fuentes congeladas no permiten resolver inequívocamente esa correspondencia:

```text
STOP / PHASE_E_VARIANT_TRACEABILITY_UNRESOLVED
```

y no cierres la especificación visual.

Si se resuelve, la figura puede mostrar las cinco variantes para evitar selección oportunista, pero la codificación y el caption deben distinguir inequívocamente las cuatro que sustentan `G3C-005` de cualquier variante contextual adicional.

---

## 5. Preguntas que FIG003 debe resolver

### 5.1 Necesidad y arquitectura visual

Confirma primero que la figura sigue aportando comprensión frente a la tabla.

Determina:

- número exacto de paneles;
- orientación;
- relación de aspecto;
- orden de lectura;
- jerarquía visual;
- si las cinco variantes caben en un único panel sin confusión;
- si existe alguna razón científica para small multiples.

La solución preferida debe ser lo más simple posible.

### 5.2 Tipo de gráfico

Evalúa críticamente al menos:

```text
A. connected dot / line chart por variante a depths 50,100,200
B. grouped dot plot sin líneas
C. heatmap variante × profundidad
```

La profundidad puede representarse como eje ordenado porque 50/100/200 son niveles crecientes de recuperación, pero cualquier línea debe describirse como conexión visual entre profundidades observadas, no como trayectoria temporal ni modelo continuo.

Selecciona una alternativa y justifica por qué las otras son inferiores.

### 5.3 Ejes, escalas y unidades

Debes fijar:

```text
x_axis
x_order
x_scale
y_axis
y_scale
y_range
unit
reference_lines
axis_breaks
```

Para cobertura exact-NANDINA:

- el eje debe comenzar en cero;
- no es obligatorio llegar a 1.0 si existe una razón visual sólida;
- un máximo de 0.35 o 0.40 puede ser válido porque mantiene baseline cero y contiene todos los valores congelados con margen;
- no uses un rango que recorte o magnifique diferencias pequeñas de forma engañosa;
- cualquier rango distinto de `[0,1]` debe justificarse explícitamente en la respuesta y quedar visible en la especificación.

### 5.4 Codificación de variantes y trazabilidad del claim

Define:

- marcadores/formas;
- estilos de línea si se autorizan líneas;
- orden de leyenda;
- codificación redundante para escala de grises;
- tratamiento visual de `CONTEXT_ONLY_VARIANTS`;
- cómo distinguir contexto sin sugerir menor calidad científica ni favorabilidad;
- cómo evitar depender únicamente del color.

No uses grosor de línea o saturación para insinuar “mejor”/“peor”.

### 5.5 Etiquetas y valores

Decide:

- nombres abreviados legibles de las variantes;
- si se muestran valores numéricos;
- número de decimales;
- si los `exact_numerator` y denominadores deben aparecer en panel o solo caption/tabla;
- cómo mostrar que `N=1056` en cada profundidad sin repetir ruido visual.

No introduzcas porcentajes derivados si la implementación puede presentar directamente las proporciones congeladas o sus equivalentes de presentación sin cambiar precisión científica.

### 5.6 Incertidumbre y prohibiciones

Debe quedar inequívoco:

```text
NO CI
NO p-values
NO significance stars
NO inferential comparison
NO regression/trend fit
NO smoothing
NO interpolation
NO ranking by favorability
NO diagnostic_union as ordinary variant
```

### 5.7 Caption de trabajo

Redacta un caption preliminar que incluya obligatoriamente:

- Phase E;
- benchmark interno offline del Capítulo 87;
- 1,056 series / 67 DAM / 42 NANDINA;
- cobertura exact-NANDINA;
- profundidades 50/100/200;
- naturaleza descriptiva/no confirmatoria;
- ausencia de CI/test inferencial;
- distinción entre las variantes formales de `G3C-005` y cualquier variante contextual;
- exclusión del diagnostic union como rendimiento ordinario.

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
formal_claim_variants
context_only_variants
panel_count
chart_type
x_axis
x_order
y_axis
y_range
unit
marks
variant_encoding
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

## 7. Controles obligatorios de auditoría FIG003

Emite PASS/FAIL para:

```text
FIG003_SOURCE_BLOB_IDENTITY
FIG003_G3C005_TRACEABILITY_RESOLVED
FIG003_FOUR_FORMAL_VARIANTS_IDENTIFIED
FIG003_CONTEXT_VARIANTS_EXPLICIT
FIG003_ALL_CANONICAL_ROWS_ACCOUNTED
FIG003_NO_CHERRY_PICKING
FIG003_DESCRIPTIVE_ONLY
FIG003_NO_CI
FIG003_NO_NEW_INFERENCE
FIG003_NO_NEW_METRICS
FIG003_DIAGNOSTIC_UNION_EXCLUDED_FROM_PERFORMANCE
FIG003_AXIS_BASELINE_INTEGRITY
FIG003_NO_FAVORABILITY_ENCODING
FIG003_ACCESSIBLE_WITHOUT_COLOR_ONLY
FIG003_HE2_PRESERVED
```

Todos deben estar PASS para considerar FIG003 aprobable.

---

## 8. Regla de no avance

FIG003 termina con la especificación científico-visual de `G6-FIG-02`.

No generes la figura.
No escribas scripts.
No diseñes todavía G6-FIG-03.
No ejecutes G6-F02.

El siguiente paso será FIG004 únicamente después de auditoría externa de FIG003.

---

## 9. Persistencia obligatoria de la respuesta

Guarda exclusivamente:

```text
branch = codex/prompts-temporary
path = figure_prompts_tmp/FIG003_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_02_PHASE_E.md
```

No modifiques ningún otro archivo.

Commit recomendado:

```text
figures: record FIG003 Phase E specification
```

Al terminar responde en el chat únicamente:

```text
Rama: codex/prompts-temporary

Archivo de respuesta:
figure_prompts_tmp/FIG003_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_02_PHASE_E.md

Commit:
<SHA>
```

No pegues el contenido completo en el chat.
