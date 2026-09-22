# FIG004 — Respuesta oficial: especificación científico-visual de G6-FIG-03 (EXP11A)

## 0. Alcance y verificación de trazabilidad

Se ejecutó exclusivamente `figure_prompts_tmp/FIG004_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_03_EXP11A.md@6fcda917784d0a55b1788ea5e16f5492f3c33645`.

No se generaron imágenes, mockups ni scripts; no se modificaron `main`, Plan Maestro, fichas, artículo o tesis; no se recalcularon métricas, promedios, diferencias, CI, p-values ni inferencia; no se ejecutó G6-F02.

Se verificaron sin drift material las fuentes rectoras exigidas:

- `outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv` — blob `cf3aedab5935d6af9b3ac7be7b51b954fcb9c403`.
- `outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv` — blob `da0351cb523fc7f3b45a83e072765a07f809b7fe`.
- `outputs/analysis/group4/g4_limitations_registry_v0.1.json` — blob `ae00b93431e912cb78a58344057d9bf7a51fcd47`.
- `outputs/results/group5/g5_table_registry_v0.1.json` — blob `4fe9318d52fad093066ff9f42d524fc95e436245`.
- `docs/results/group5/g5_results_presentation_plan_v0.1.md` — blob `9eaf780f3a2f6c8579dc80867ed3a86e96683894`.
- `docs/results/group5/g5_appendix_registry_v0.1.md` — blob `9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a`.
- `outputs/audits/group5_closure_v0.1.json` — blob `1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf`.

Para resolver la semántica de corridas y summaries se verificaron además las fuentes vigentes registradas por G5:

- `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv` — blob `9b434d7e09e6db7e9de061953b59c53aac2337ad`.
- `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv` — blob `535dd377d107ddcbf09ecaa13cd66ca723ee738d`.

El contrato científico permanece:

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
```

El claim rector `G3C-007` mantiene exactamente el rol `SENSITIVITY`, `DESCRIPTIVE_SENSITIVITY`, `NONCAUSAL`, con la limitación obligatoria de que tamaño y composición están acoplados y con prohibición expresa de atribuir un efecto causal aislado o monotónico al tamaño del banco.

---

# A. Inventario y trazabilidad de EXP11A

## A.1 Corridas observadas

El CSV canónico contiene **31 filas `OBSERVED_RUN`**:

| Condición observada | Corridas verificadas | Nota de trazabilidad |
|---|---:|---|
| `H25` | 10 | `H25-R01` a `H25-R10` |
| `H50` | 10 | cinco `D1` y cinco `D2` |
| `H75` | 10 | `H75-R01` a `H75-R10` |
| `H100` | 1 | `H100_REEXECUTED_CHECK / FROZEN_REFERENCE` |

La fuente de corridas `exp11_metrics_by_run.csv` materializa `dominant_stratum=D1` para `H50-D1-R01..R05` y `dominant_stratum=D2` para `H50-D2-R01..R05`. La distinción D1/D2 no se infiere del orden de filas.

```text
OBSERVED_RUN_COUNT_TOTAL = 31
OBSERVED_RUN_COUNTS_BY_CONDITION = {H25: 10, H50: 10, H75: 10, H100: 1}
H50_D1_RUN_COUNT = 5
H50_D2_RUN_COUNT = 5
```

## A.2 Summaries congelados

El CSV canónico contiene **6 filas `FROZEN_CONDITION_SUMMARY`**:

1. `H25`, 10 réplicas observadas.
2. `H50`, 10 réplicas observadas, summary global.
3. `H75`, 10 réplicas observadas.
4. `H100`, 1 réplica, `FROZEN_REFERENCE`.
5. `H50`, 5 réplicas, correspondiente a `H50_D1_DIAGNOSTIC`.
6. `H50`, 5 réplicas, correspondiente a `H50_D2_DIAGNOSTIC`.

Las dos filas H50 de cinco réplicas tienen el mismo `row_key` canónico (`SUMMARY-H50`), por lo que el `row_key` por sí solo no identifica D1/D2. Sin embargo, la fuente congelada `exp11_metrics_by_condition.csv` distingue inequívocamente `aggregation_scope=H50_D1_DIAGNOSTIC` y `aggregation_scope=H50_D2_DIAGNOSTIC`, y sus valores métricos y metadatos composicionales coinciden uno a uno con las dos filas canónicas de cinco réplicas. La resolución, por tanto, se hace por trazabilidad a la fuente versionada, no por orden de aparición.

```text
FROZEN_SUMMARY_COUNT_TOTAL = 6
H50_SUMMARY_TRACEABILITY = PASS
```

## A.3 Política sobre summaries en la figura

**Los summaries congelados no se graficarán.** Esta decisión es deliberada y no constituye omisión oportunista:

- el objetivo visual de EXP11A es hacer visible la dispersión entre corridas observadas;
- el summary global H50 volvería a colapsar D1/D2, precisamente la heterogeneidad composicional que debe conservarse;
- el summary H100 reproduce la única referencia observada y dibujarlo adicionalmente generaría duplicación visual de una sola corrida;
- los summaries D1/D2 son trazables, pero añadirlos junto con los puntos no aporta una función imprescindible y aumentaría la complejidad perceptual;
- los seis summaries permanecen íntegramente en la tabla canónica y en el inventario de esta especificación.

No se calculará ningún summary alternativo.

---

# B. Dictamen de necesidad y arquitectura visual

La figura **sí aporta comprensión adicional frente a la tabla**. La tabla es necesaria para valores exactos y metadatos composicionales, pero una visualización por corrida permite observar simultáneamente la dispersión interna de H25/H50/H75, la diferenciación explícita de H50-D1/H50-D2 y el carácter singular de H100 como referencia congelada.

La figura no debe presentar una narrativa de incremento o decremento con el tamaño. Su pregunta científica queda formulada como:

> ¿Cómo varían descriptivamente las seis métricas de recuperación entre las condiciones de banco observadas en EXP11A, cuando tamaño y composición cambian conjuntamente?

Especificación general:

```text
FIGURE_ID = G6-FIG-03
FINAL_PANEL_COUNT = 6
ORIENTATION = LANDSCAPE
RECOMMENDED_ASPECT_RATIO = 3:2
LAYOUT = 2 rows × 3 columns
READING_ORDER = Top1 → Top3 → Top5 → Top10 → Top50 → MRR
DESTINATION = APPENDIX
SCIENTIFIC_ROLE = DESCRIPTIVE_SENSITIVITY / NONCAUSAL
CLAIM_IDS = [G3C-007]
```

Los seis paneles conservan las seis métricas congeladas; no se elimina ninguna por magnitud, apariencia o conveniencia narrativa.

---

# C. Tipo de gráfico: comparación de alternativas

## C.1 Alternativa A — seis small multiples con puntos por corrida

**SELECCIONADA.** Cada panel usa la misma estructura categórica y muestra todas las corridas observadas de una única métrica. Esta opción preserva la dispersión, mantiene las métricas separadas semánticamente y permite usar el rango completo `[0,1]` sin recurrir a truncamientos.

## C.2 Alternativa B — heatmap corrida × métrica

**DESCARTADA.** Un heatmap convierte diferencias métricas en intensidad visual y dificulta distinguir la distribución dentro de cada condición. Además, exigiría una lectura dependiente de escala cromática, menos robusta en impresión y escala de grises, y haría menos evidente que H100 es una única referencia.

## C.3 Alternativa C — parallel coordinates / spaghetti multimetric

**DESCARTADA.** Con 31 corridas produciría alta superposición y daría apariencia de trayectorias multivariadas entre métricas que tienen significados distintos. La conectividad visual favorecería patrones narrativos no necesarios para el claim descriptivo.

## C.4 Alternativa D — solo summaries congelados

**DESCARTADA.** Ocultaría la dispersión observada, reduciría H50 a una centralidad que puede borrar D1/D2 y pondría una referencia H100 de una sola corrida al mismo nivel perceptual que condiciones con diez réplicas.

Tampoco se autoriza sustituir los puntos por boxplots, violines, bandas o intervalos, porque esas formas requerirían nuevos cuantiles, densidades o resúmenes no congelados.

---

# D. Especificación panel por panel

Todos los paneles comparten la misma arquitectura:

```text
chart_type = small-multiple strip/dot plot
category_axis = observed bank condition
condition_order = [H25, H50-D1, H50-D2, H75, H100 ref.]
y_range = [0,1]
axis_breaks = PROHIBITED
trend_lines = PROHIBITED
connections_between_conditions = PROHIBITED
uncertainty = NONE
```

| Panel | Métrica | Unidad | Fuente | Marcas |
|---|---|---|---|---|
| A | `Top1` | proporción de series, `[0,1]` | 31 `OBSERVED_RUN` canónicos | puntos por corrida; H100 como referencia única |
| B | `Top3` | proporción de series, `[0,1]` | idem | idem |
| C | `Top5` | proporción de series, `[0,1]` | idem | idem |
| D | `Top10` | proporción de series, `[0,1]` | idem | idem |
| E | `Top50` | proporción de series, `[0,1]` | idem | idem |
| F | `MRR` | puntuación adimensional, `[0,1]` | idem | idem |

## D.1 Eje de condición

El eje x se denominará:

```text
Condición observada de banco (tamaño nominal + composición)
```

Orden fijo:

```text
H25 | H50-D1 | H50-D2 | H75 | H100 ref.
```

Este orden procede de la estructura experimental documentada y de la necesidad de mostrar D1/D2 contiguos dentro de H50; **no** se ordena por rendimiento.

Se añadirá una separación visual fina antes de `H100 ref.` para remarcar que es una referencia congelada de una sola corrida y no una condición con diez réplicas. La separación no codifica favorabilidad.

La figura y el caption deben indicar que H25, H75 y H100 también tienen composiciones observadas propias; D1/D2 son una distinción explícita dentro de H50, no una afirmación de homogeneidad composicional para las demás condiciones.

## D.2 Eje y escala vertical

Para todos los paneles:

```text
y_scale = linear
y_range = [0,1]
reference_baseline = 0
major_grid = 0, 0.25, 0.50, 0.75, 1.00
axis_breaks = prohibited
```

No se usa un rango estrecho por panel. Esta decisión evita magnificar artificialmente la variación entre corridas, especialmente en `Top50`.

---

# E. Marcas, jitter y codificación visual

## E.1 Corridas individuales

- Marcador base: círculo abierto de peso visual medio.
- Cada corrida se muestra exactamente una vez por panel.
- No hay líneas entre corridas ni entre condiciones.
- No se codifica rendimiento mediante tamaño, saturación u opacidad.

Para evitar solapamiento se autoriza **jitter horizontal determinista y exclusivamente visual**:

```text
H25 / H75, n=10:
[-0.18, -0.14, -0.10, -0.06, -0.02, +0.02, +0.06, +0.10, +0.14, +0.18]

H50-D1 / H50-D2, n=5:
[-0.12, -0.06, 0, +0.06, +0.12]

H100 ref., n=1:
0
```

Los offsets se asignan por `run/seed` en orden alfanumérico y se mantienen idénticos en los seis paneles. El jitter no depende del valor de la métrica ni de ningún atributo composicional.

## E.2 H100 frozen reference

- Marcador distinto: diamante.
- Un único punto por panel.
- Sin jitter.
- Etiqueta categórica `H100 ref.`.
- No se dibuja el `SUMMARY-H100` como una segunda marca porque representa la misma única referencia.

## E.3 H50-D1 / H50-D2

D1 y D2 se distinguen principalmente por **posición categórica separada** (`H50-D1`, `H50-D2`). El color puede utilizarse solo como codificación secundaria de igual peso perceptual, nunca como señal de mejor/peor. La figura debe seguir siendo interpretable sin color.

## E.4 Color y escala de grises

La semántica principal descansa en posición x y forma del marcador. Una paleta categórica sobria puede aplicarse posteriormente, sin jerarquía de luminancia deliberada. En escala de grises deben conservarse:

- categorías legibles por posición y etiqueta;
- corrida individual = círculo abierto;
- H100 reference = diamante;
- separación vertical antes de H100.

No se fijan hexadecimales en FIG004.

---

# F. Accesibilidad y tipografía

Especificación mínima para implementación:

- fuente sans serif;
- tamaño mínimo efectivo en salida final: `8.5 pt`;
- títulos de panel: `9.5–10 pt`;
- etiquetas de ejes/leyenda: `8.5–9 pt`;
- marcadores suficientemente grandes para distinguir círculos y diamante en impresión;
- gridlines horizontales finas y claras; sin gridlines verticales;
- fondo blanco o muy claro;
- no depender exclusivamente del color;
- no usar sombras, 3D, degradados o áreas decorativas;
- categorías x en texto horizontal; no ordenar por favorabilidad.

Orden de leyenda, si se requiere leyenda de marcas:

```text
1. Corrida observada
2. H100 — referencia congelada
```

Las categorías H25/H50-D1/H50-D2/H75/H100 se leen directamente en el eje x y no requieren una segunda leyenda redundante.

---

# G. Política de información composicional

Los campos ya congelados de `bank composition` (`rows`, `DAM`/medidas asociadas de diversidad efectiva según la fuente, `HHI`, `coverage`, `sha256`) **no se convierten en covariables gráficas**.

Política:

```text
PANEL:
- solo condición observada y subestrato H50-D1/H50-D2.

LEGEND:
- no incluir rows, DAM, HHI o coverage.

CAPTION:
- declarar explícitamente que tamaño y composición varían conjuntamente y que H25/H75/H100 conservan composiciones propias.

CANONICAL TABLE:
- conservar los metadatos composicionales detallados y los summaries congelados.
```

No se calculan correlaciones, slopes, bins, clases post hoc ni relaciones entre HHI/cobertura y desempeño.

---

# H. Política de etiquetas numéricas

```text
numeric_labels_on_points = NO
run_ids_inside_panels = NO
summary_values_inside_panels = NO
N=1056 repeated_per_panel = NO
```

La figura prioriza estructura y dispersión; los valores exactos permanecen en la tabla canónica. El caption declarará el universo del benchmark y los conteos de corridas por condición.

---

# I. Caption de trabajo

**Figura G6-FIG-03. Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A).** Los seis paneles muestran `Top1`, `Top3`, `Top5`, `Top10`, `Top50` y `MRR` para las corridas observadas en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA): H25 (`n=10`), H50-D1 (`n=5`), H50-D2 (`n=5`), H75 (`n=10`) y la referencia congelada H100 (`n=1`). D1/D2 son subestratos de composición documentados dentro de H50; H25, H75 y H100 también conservan sus composiciones observadas. Los puntos representan corridas individuales y H100 se muestra como una única referencia, no como una distribución de réplicas. EXP11A es una sensibilidad descriptiva y no causal en la que tamaño y composición varían conjuntamente; por ello, el eje de condiciones no identifica un efecto causal aislado ni monotónico del tamaño. No se muestran ni calculan CI, p-values, regresiones, suavizados ni agregados nuevos; los summaries congelados permanecen en la tabla canónica y no se duplican en la figura.

Caption sujeto a revisión posterior en G6-F03.

---

# J. Contrato conceptual machine-readable

```text
figure_id = G6-FIG-03
working_title = Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A)
scientific_role = DESCRIPTIVE_SENSITIVITY / NONCAUSAL
destination = APPENDIX
claim_ids = [G3C-007]
source_path = outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
source_blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403
supporting_run_source = outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv@9b434d7e09e6db7e9de061953b59c53aac2337ad
supporting_summary_source = outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv@535dd377d107ddcbf09ecaa13cd66ca723ee738d
observed_run_inventory = total 31; H25=10; H50-D1=5; H50-D2=5; H75=10; H100_ref=1
frozen_summary_inventory = total 6; H25=1; H50_overall=1; H50_D1=1; H50_D2=1; H75=1; H100_ref=1
panel_count = 6
panel_metrics = [Top1, Top3, Top5, Top10, Top50, MRR]
chart_type = 2x3 small-multiple categorical strip/dot plots
condition_axis = observed bank condition (nominal size + composition)
condition_order = [H25, H50-D1, H50-D2, H75, H100 ref.]
h50_d1_d2_encoding = separate adjacent x categories; documented dominant_stratum; no order inference
h100_reference_policy = one diamond per panel; single frozen reference; no duplicate summary mark
x_axis_or_category_axis = categorical; not continuous dose axis
y_axis = frozen absolute metric value
y_range = [0,1]
unit = Top-k proportion; MRR unitless score
marks = open circles for observed runs; diamond for H100 reference
summary_policy = inventory and table only; no summary markers in figure
composition_context_policy = explicit coupled-design caption; detailed rows/DAM/HHI/coverage remain in canonical table
legend_order = [Observed run, H100 frozen reference]
uncertainty_policy = NO CI / NO error bars / NO p-values
numeric_label_policy = no point labels; exact values retained in canonical table
forbidden_transformations = new mean/median/delta/CI/p-value; boxplot/violin-derived summaries; regression; smoothing; interpolation; performance sorting; axis truncation; post-hoc composition bins; causal size interpretation
accessibility_requirements = position+shape redundancy; grayscale-readable; minimum 8.5 pt; light horizontal grid; no color-only semantics
```

---

# K. Validaciones de implementación posterior

La implementación futura deberá verificar antes de exportar cualquier figura:

1. identidad exacta del blob canónico `cf3aedab...`;
2. presencia de 31 `OBSERVED_RUN` y 6 `FROZEN_CONDITION_SUMMARY`;
3. conteos `10 / 5 / 5 / 10 / 1` para `H25 / H50-D1 / H50-D2 / H75 / H100 ref.`;
4. correspondencia D1/D2 con `dominant_stratum` y con los scopes `H50_D1_DIAGNOSTIC` / `H50_D2_DIAGNOSTIC` de la fuente congelada;
5. seis paneles y seis métricas, sin omisiones;
6. rango vertical exacto `[0,1]` en todos los paneles;
7. ausencia de CI, barras de error, p-values, asteriscos, regresiones, smooths y líneas entre condiciones;
8. uso del mismo jitter determinista por `run/seed` en los seis paneles;
9. una sola marca H100 por panel;
10. ausencia de summaries graficados;
11. orden de condiciones fijo y no dependiente del desempeño;
12. caption con la limitación conjunta tamaño/composición y la naturaleza no causal;
13. ninguna modificación de artículo, tesis, fichas, Plan Maestro o G6-F02 durante esta etapa.

---

# L. Checklist obligatorio FIG004

| Control | Estado | Justificación |
|---|---|---|
| `FIG004_SOURCE_BLOB_IDENTITY` | PASS | Blob canónico y fuentes rectoras coinciden con los hashes congelados exigidos. |
| `FIG004_G3C007_TRACEABILITY` | PASS | `G3C-007` se verificó en la matriz G4 como sensibilidad descriptiva, no causal. |
| `FIG004_OBSERVED_RUN_INVENTORY_COMPLETE` | PASS | 31 corridas observadas contabilizadas: 10 H25, 10 H50, 10 H75, 1 H100. |
| `FIG004_H50_D1_D2_RESOLVED` | PASS | `dominant_stratum` documenta D1/D2; 5 corridas por subestrato. |
| `FIG004_H100_REFERENCE_ROLE_PRESERVED` | PASS | H100 se representa como única referencia congelada, no como distribución. |
| `FIG004_FROZEN_SUMMARY_INVENTORY_COMPLETE` | PASS | Se contabilizaron las 6 filas summary y su semántica. |
| `FIG004_NO_AMBIGUOUS_SUMMARY_USED` | PASS | Ningún summary se grafica; la semántica D1/D2 fue resuelta únicamente para inventario/trazabilidad. |
| `FIG004_ALL_SIX_METRICS_ACCOUNTED` | PASS | Top1, Top3, Top5, Top10, Top50 y MRR tienen panel propio. |
| `FIG004_RUN_LEVEL_DISPERSION_VISIBLE` | PASS | Todas las corridas observadas se muestran como puntos individuales. |
| `FIG004_SIZE_COMPOSITION_COUPLING_VISIBLE` | PASS | Eje, caption y política composicional describen condiciones observadas de banco, no tamaño puro. |
| `FIG004_NO_ISOLATED_SIZE_CAUSAL_CLAIM` | PASS | No se atribuye causalidad al tamaño. |
| `FIG004_NO_MONOTONIC_DOSE_RESPONSE_IMPLICATION` | PASS | Eje categórico, sin líneas ni trend fit; no se modela H25→H100 como dosis. |
| `FIG004_NO_NEW_AGGREGATION` | PASS | No se calcula ningún summary nuevo; los summaries existentes tampoco se transforman. |
| `FIG004_NO_NEW_CI` | PASS | No se crean ni muestran CI. |
| `FIG004_NO_P_VALUE` | PASS | No se crean ni muestran p-values. |
| `FIG004_NO_REGRESSION_OR_SMOOTH` | PASS | Regresión, smooth e interpolación están prohibidos. |
| `FIG004_NO_CHERRY_PICKING` | PASS | Se muestran las 31 corridas y las seis métricas; ninguna selección depende de favorabilidad. |
| `FIG004_AXIS_INTEGRITY` | PASS | Todos los paneles usan `[0,1]`, sin truncamiento ni axis breaks. |
| `FIG004_ACCESSIBLE_WITHOUT_COLOR_ONLY` | PASS | Posición, etiquetas y formas sostienen la semántica; color es secundario. |
| `FIG004_NO_ARTICLE_OR_THESIS_MODIFICATION` | PASS | No se modificó artículo ni tesis. |
| `FIG004_NO_G6_F02_EXECUTION` | PASS | G6-F02 no fue ejecutado. |

---

# M. Disposición terminal

```text
FIG004_DISPOSITION = APPROVABLE_FOR_IMPLEMENTATION_SPEC
```

La especificación queda cerrada conceptualmente para auditoría externa. Esta disposición **no autoriza** generar la figura ni ejecutar G6-F02.