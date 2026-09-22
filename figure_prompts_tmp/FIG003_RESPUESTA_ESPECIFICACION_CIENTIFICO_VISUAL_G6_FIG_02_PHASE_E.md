# FIG003 — Respuesta oficial: especificación científico-visual de G6-FIG-02 (Phase E)

## 0. Alcance y verificación de trazabilidad

Se ejecutó exclusivamente `figure_prompts_tmp/FIG003_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_02_PHASE_E.md` en el commit `58580c0df966f12e3a80e39edc46963f63acd4b1`.

No se generaron imágenes, mockups finales ni scripts; no se modificaron `main`, Plan Maestro, fichas, artículo o tesis; no se recalcularon métricas, porcentajes, diferencias, intervalos, p-values ni inferencia; no se promovió Phase E a evidencia confirmatoria; no se incorporó `diagnostic_union` como rendimiento; no se diseñó `G6-FIG-03` y no se ejecutó G6-F02.

Las fuentes gobernadas exigidas por FIG003 permanecen presentes con los blobs congelados esperados. No se detectó drift científico material que obligue a detener la especificación.

| Fuente | Blob esperado | Blob verificado | Estado |
|---|---|---|---|
| `outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv` | `fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61` | `fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61` | MATCH |
| `outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv` | `da0351cb523fc7f3b45a83e072765a07f809b7fe` | `da0351cb523fc7f3b45a83e072765a07f809b7fe` | MATCH |
| `outputs/results/group5/g5_table_registry_v0.1.json` | `4fe9318d52fad093066ff9f42d524fc95e436245` | `4fe9318d52fad093066ff9f42d524fc95e436245` | MATCH |
| `docs/results/group5/g5_results_presentation_plan_v0.1.md` | `9eaf780f3a2f6c8579dc80867ed3a86e96683894` | `9eaf780f3a2f6c8579dc80867ed3a86e96683894` | MATCH |
| `docs/results/group5/g5_canonical_tables_v0.1.md` | `9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d` | `9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d` | MATCH |
| `outputs/audits/group5_closure_v0.1.json` | `1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf` | `1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf` | MATCH |
| `outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv` | `f43cce08d1d7bc3cef64698dbebf14eae4b26ed5` | `f43cce08d1d7bc3cef64698dbebf14eae4b26ed5` | MATCH |

Como fuente adicional necesaria para resolver la ambigüedad de trazabilidad de variantes se verificó `outputs/analysis/group3/g3_metric_population_registry_v0.1.csv`, blob `c63619b56a07e6b6d7be78b515d941ec3b205c41`.

Se preserva el contrato científico:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
HE2 = SUPPORTED
```

Phase E permanece `DESCRIPTIVE_ONLY`, sin CI, p-values ni contraste inferencial entre variantes.

---

# A. Resolución obligatoria de trazabilidad de G3C-005

El claim `G3C-005` referencia exactamente doce filas del registro G3:

```text
G3F02-0040; G3F02-0044; G3F02-0048
G3F02-0052; G3F02-0056; G3F02-0060
G3F02-0064; G3F02-0068; G3F02-0072
G3F02-0076; G3F02-0080; G3F02-0084
```

Esas filas corresponden inequívocamente a cuatro variantes y a sus tres profundidades 50/100/200:

```text
hierarchical_only
  G3F02-0040 / 0044 / 0048

dual_only
  G3F02-0052 / 0056 / 0060

hierarchical_first_100
  G3F02-0064 / 0068 / 0072

hierarchical_80_dual_backfill_20
  G3F02-0076 / 0080 / 0084
```

Las cuatro pertenecen a la familia `HE2_B_PHASE_E_FROZEN_ROLE_POOLS`, cuyo registro señala que `A_historical_defined` permite su evaluación en el rol congelado y excluye expresamente la variante 70/30 de esa familia.

Por separado, `hierarchical_70_dual_backfill_30` aparece desde `G3F02-0088` bajo la familia distinta `HE2_B_PHASE_E_70_30`; el registro congela para esa familia la limitación: `the 70/30 variant was not formally frozen for v0.2`. Por tanto, sus tres filas exact-NANDINA de la tabla canónica son contexto descriptivo adicional, pero no forman parte de las cuatro variantes que sustentan formalmente `G3C-005`.

```text
FORMAL_G3C005_VARIANTS = [
  hierarchical_only,
  dual_only,
  hierarchical_first_100,
  hierarchical_80_dual_backfill_20
]

CONTEXT_ONLY_VARIANTS = [
  hierarchical_70_dual_backfill_30
]

TRACEABILITY_RESOLUTION = PASS
```

La quinta variante se mantendrá visible para contabilizar las 15 filas canónicas y evitar selección oportunista, pero su rol contextual será explícito en leyenda y caption.

`diagnostic_union_hierarchical_dual` no pertenece a este conjunto. Su tabla canónica de anexo lo clasifica como `diagnostic_union`; se excluye de la figura de rendimiento descriptivo ordinario.

---

# B. Dictamen de necesidad y arquitectura visual

## B.1 Necesidad científica

**DICTAMEN: KEEP AS FIGURE.**

La figura sigue aportando comprensión respecto de la tabla porque el patrón principal que se desea comunicar es estructural: cómo cambia la cobertura exacta NANDINA entre las profundidades discretas 50, 100 y 200 y cómo se sitúan las cinco variantes en cada profundidad. La tabla es superior para consulta exacta de numeradores, denominadores y valores completos; la figura es superior para reconocer de inmediato el aumento descriptivo de cobertura y las zonas de coincidencia o divergencia entre variantes.

La figura no debe intentar demostrar diferencias estadísticas entre variantes. Su función es descriptiva y complementaria a HE2_B.

## B.2 Arquitectura elegida

```text
FIGURE_ID = G6-FIG-02
WORKING_TITLE = Cobertura exacta NANDINA de Phase E según profundidad y variante
SCIENTIFIC_ROLE = DESCRIPTIVE_SUPPLEMENTARY
DESTINATION = SECONDARY
CLAIM_IDS = [G3C-005]
PANEL_COUNT = 1
ORIENTATION = HORIZONTAL
RECOMMENDED_ASPECT_RATIO = 16:9 aproximado
READING_ORDER = izquierda a derecha por profundidad: 50 -> 100 -> 200
```

Se recomienda **un único panel**. Cinco variantes × tres profundidades son manejables en una sola vista si se evita la superposición mediante agrupamiento horizontal controlado de marcadores dentro de cada profundidad.

No existe una razón científica suficiente para usar small multiples: separar cada variante en un panel eliminaría la superposición, pero dificultaría la comparación directa entre variantes, multiplicaría ejes idénticos y aumentaría innecesariamente la complejidad visual.

---

# C. Tipo de gráfico: comparación deliberada de alternativas

## C.1 Alternativa A — connected dot / line chart

**NO SELECCIONADA.**

Ventaja: comunica con rapidez que la cobertura observada es mayor a profundidades superiores.

Problemas:

1. varias variantes comparten exactamente los mismos valores en profundidad 50 y/o 100, y tres alcanzan exactamente `0.3039772727272727` en profundidad 200; las líneas y puntos quedarían superpuestos y ocultarían series;
2. la conexión puede interpretarse como trayectoria continua, tendencia modelada o incluso secuencia temporal, aunque la profundidad sea solo un parámetro discreto de recuperación;
3. distinguir cinco series solapadas exigiría exceso de estilos de línea, reduciendo legibilidad y accesibilidad.

Por estas razones, la línea aporta menos claridad de la que aparenta.

## C.2 Alternativa B — grouped dot plot sin líneas

**SELECCIONADA.**

Cada profundidad se trata como una categoría ordenada. Dentro de cada categoría se muestran cinco puntos con un pequeño desplazamiento horizontal fijo por variante. El desplazamiento es puramente gráfico para evitar oclusión; no modifica la profundidad ni representa un valor numérico distinto.

Ventajas:

- hace visibles las 15 filas canónicas;
- evita que valores idénticos oculten variantes completas;
- mantiene la comparación directa entre profundidades y variantes;
- no introduce interpolación, tendencia ni trayectoria temporal;
- permite distinguir rol formal/contextual mediante marcador y leyenda sin alterar el peso cuantitativo de los puntos;
- funciona con una sola escala y un solo panel.

## C.3 Alternativa C — heatmap variante × profundidad

**NO SELECCIONADA.**

Un heatmap compactaría bien 5 × 3 celdas, pero convertiría el color en el canal cuantitativo principal y haría que la percepción de diferencias pequeñas dependiera de la paleta y de su normalización. Además, es menos preciso para comparar valores próximos, exige etiquetas numéricas para recuperar precisión y presenta una dependencia de color más difícil de resolver en escala de grises.

### Selección final

```text
CHART_TYPE = GROUPED_DOT_PLOT_NO_LINES
```

---

# D. Especificación científico-visual exacta

## D.1 Fuente y filas

```text
source_path = outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
source_blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
rows_used = all 15 canonical rows
```

Columnas utilizadas:

```text
VISUAL_ENCODING:
- variant
- depth
- exact-NANDINA coverage

CAPTION / SCOPE VALIDATION:
- cases
- denominator
- source version

NOT_VISUALLY_ENCODED:
- nominal_size
- effective_size_mean
- exact_numerator
```

`exact_numerator`, `nominal_size` y `effective_size_mean` permanecen disponibles en la tabla canónica, pero no se añaden al panel porque generarían ruido y no responden a la pregunta visual principal.

## D.2 Pregunta visual

> ¿Cómo varía descriptivamente la cobertura exacta NANDINA de los pools Phase E entre las profundidades de recuperación 50, 100 y 200, y cómo se comparan visualmente las variantes formales de G3C-005 con la variante 70/30 incluida solo como contexto descriptivo?

## D.3 Eje X

```text
x_axis = Profundidad de recuperación
x_order = [50, 100, 200]
x_scale = categorical ordered
x_positions = three equally spaced categorical anchors
within_depth_dodge = fixed symmetric visual offsets for the five variants
axis_breaks = PROHIBITED
```

La elección categórica es deliberada: 50, 100 y 200 son los tres niveles discretos observados y no se modela el espacio intermedio. No se inferirá continuidad entre profundidades.

El `within_depth_dodge` debe ser pequeño, constante y simétrico alrededor de cada ancla de profundidad. Los ticks continúan siendo exclusivamente `50`, `100` y `200`; los offsets no constituyen valores de profundidad y no deben aparecer en la escala.

## D.4 Eje Y

```text
y_axis = Cobertura exacta NANDINA
y_scale = linear
y_range = [0.00, 0.35]
unit = proportion
reference_lines = none beyond baseline/grid ticks
axis_breaks = PROHIBITED
```

### Justificación del rango `[0, 0.35]`

El máximo ordinario materializado entre las cinco variantes es `0.3039772727272727`. Un máximo de `0.35` conserva:

- baseline exacto en cero;
- todos los valores con margen superior visible;
- suficiente resolución para distinguir la separación material en profundidad 200;
- integridad visual frente a pequeñas diferencias en profundidades 50/100, que continúan siendo pequeñas en la escala y no se magnifican mediante truncamiento.

No se requiere extender hasta 1.0 porque la figura no compara contra el máximo teórico de cobertura como claim científico; mostrar 0–1 reduciría sustancialmente la legibilidad de las diferencias observadas sin añadir información. La condición de integridad se preserva mediante baseline cero y ausencia de eje truncado.

Ticks recomendados:

```text
0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35
```

Gridlines horizontales finas únicamente en ticks principales. Sin gridlines verticales dominantes.

---

# E. Codificación de variantes y accesibilidad

## E.1 Principio general

El color puede utilizarse como canal secundario, pero **la identidad de variante nunca dependerá solo del color**. Cada variante tendrá una forma de marcador única. Todos los marcadores tendrán el mismo tamaño nominal, grosor de borde y presencia visual; no se usarán opacidad, saturación o tamaño para insinuar mejor/peor desempeño.

## E.2 Mapeo conceptual de marcadores

Orden de leyenda y codificación:

1. `hierarchical_only` — círculo relleno;
2. `dual_only` — cuadrado relleno;
3. `hierarchical_first_100` — triángulo relleno;
4. `hierarchical_80_dual_backfill_20` — rombo relleno;
5. `hierarchical_70_dual_backfill_30` — hexágono abierto, etiquetado explícitamente como `contexto descriptivo`.

El marcador abierto de la variante 70/30 **codifica rol de trazabilidad, no calidad ni favorabilidad**. Debe conservar igual tamaño, borde y contraste que los marcadores formales.

La leyenda debe dividirse conceptualmente en dos bloques:

```text
Variantes formales de G3C-005
- hierarchical_only
- dual_only
- hierarchical_first_100
- hierarchical_80_dual_backfill_20

Contexto descriptivo adicional
- hierarchical_70_dual_backfill_30
```

No se congela todavía una paleta hexadecimal. Si se utiliza color, las cinco identidades deben conservar contraste suficiente y los cuatro marcadores formales no deben compartir una gradación ordenada que pueda leerse como ranking. La variante contextual tampoco debe representarse con baja opacidad o gris degradado.

La figura debe seguir siendo interpretable impresa en escala de grises gracias a la forma de los marcadores, el tratamiento abierto/relleno y la agrupación textual de la leyenda.

---

# F. Política de etiquetas y valores

## F.1 Nombres de variantes

La implementación debe conservar las identidades literales de las variantes en la leyenda para evitar ambigüedad de trazabilidad:

```text
hierarchical_only
dual_only
hierarchical_first_100
hierarchical_80_dual_backfill_20
hierarchical_70_dual_backfill_30
```

Puede permitirse salto de línea tipográfico en las etiquetas largas, sin cambiar el identificador.

## F.2 Valores numéricos dentro del panel

```text
numeric_point_labels = NO
```

No se recomienda imprimir los 15 valores al lado de los puntos porque las diferencias en 50/100 son muy próximas y la figura perdería legibilidad. La tabla canónica conserva los valores exactos.

El eje Y se muestra en proporción y los puntos se ubican copiando directamente los valores congelados; no se derivan porcentajes nuevos.

## F.3 N, denominador y numeradores

- `N = 1056 series` no se repetirá dentro de cada profundidad; se declara una sola vez en el caption.
- `67 DAM` y `42 NANDINA` se declaran en el caption como alcance del benchmark.
- `denominator = 1056` se valida para las 15 filas, pero no se repite junto a cada punto.
- `exact_numerator` no se mostrará en el panel; permanece en la tabla canónica.

---

# G. Incertidumbre y transformaciones prohibidas

La figura es estrictamente descriptiva.

```text
UNCERTAINTY_POLICY = DESCRIPTIVE_NO_CI_AUTHORIZED
```

Prohibiciones explícitas:

```text
NO CI
NO error bars
NO p-values
NO significance stars
NO inferential comparison
NO regression
NO trend fit
NO smoothing
NO interpolation
NO new aggregate
NO new difference metric
NO ranking by favorability
NO sorting by observed performance
NO axis truncation above zero
NO diagnostic_union as ordinary variant
NO conversion of Phase E into confirmatory HE2 evidence
```

El orden de variantes no se definirá por sus valores observados, sino por la trazabilidad congelada: primero las cuatro variantes formales en el orden de G3C-005 / registro G3 y luego la variante 70/30 contextual.

---

# H. Caption de trabajo

**Caption preliminar — sujeto a revisión posterior en G6-F03:**

> **G6-FIG-02. Cobertura exacta NANDINA de Phase E según profundidad y variante.** Se muestran las proporciones descriptivas congeladas de cobertura exacta NANDINA a profundidades de recuperación 50, 100 y 200 en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA). `hierarchical_only`, `dual_only`, `hierarchical_first_100` y `hierarchical_80_dual_backfill_20` son las cuatro variantes `A_historical_defined` que sustentan el claim descriptivo G3C-005; `hierarchical_70_dual_backfill_30` se incluye únicamente como contexto descriptivo adicional. No se presentan intervalos de confianza, p-values ni contrastes inferenciales entre variantes. La unión diagnóstica `diagnostic_union_hierarchical_dual` se excluye porque constituye un techo diagnóstico y no una variante de rendimiento ordinario. La figura no modifica la evidencia confirmatoria ni la disposición de HE2.

---

# I. Contrato conceptual machine-readable

```text
figure_id = G6-FIG-02
working_title = Cobertura exacta NANDINA de Phase E según profundidad y variante
scientific_role = DESCRIPTIVE_SUPPLEMENTARY
destination = SECONDARY
claim_ids = [G3C-005]
source_path = outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
source_blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
formal_claim_variants = [hierarchical_only, dual_only, hierarchical_first_100, hierarchical_80_dual_backfill_20]
context_only_variants = [hierarchical_70_dual_backfill_30]
panel_count = 1
chart_type = GROUPED_DOT_PLOT_NO_LINES
x_axis = depth / Profundidad de recuperación
x_order = [50, 100, 200]
x_scale = ordered categorical
y_axis = exact-NANDINA coverage / Cobertura exacta NANDINA
y_range = [0.00, 0.35]
unit = proportion
marks = equal-size distinct point markers; no connecting lines
variant_encoding = marker shape primary; color secondary; context role shown by open marker + explicit legend subgroup
legend_order = [hierarchical_only, dual_only, hierarchical_first_100, hierarchical_80_dual_backfill_20, hierarchical_70_dual_backfill_30(context)]
uncertainty_policy = DESCRIPTIVE_NO_CI_AUTHORIZED
numeric_label_policy = no per-point numeric labels; values copied to positions from frozen canonical CSV; exact numbers remain in table
caption_working = defined in Section H
forbidden_transformations = [CI, p-values, significance stars, inferential contrasts, regression, smoothing, interpolation, new aggregates, new differences, favorability sorting, diagnostic_union as performance]
accessibility_requirements = [grayscale-readable, unique marker per variant, no color-only identity, equal visual weight, minimum text size sufficient for thesis print]
implementation_validation_checks = [15 points, 5 variants x 3 depths, 12 formal-claim rows + 3 context rows, no diagnostic_union, y baseline 0, y max 0.35, no CI/error bars, fixed source order, exact canonical values only]
```

---

# J. Requisitos de implementación y accesibilidad para G6-F02

Sin ejecutar todavía G6-F02, la futura implementación debe cumplir:

1. renderizar exactamente 15 marcas, una por cada fila canónica;
2. mantener tres únicas categorías X: 50, 100 y 200;
3. aplicar un offset horizontal pequeño, determinista y simétrico por variante dentro de cada categoría, sin modificar el dato de profundidad;
4. ubicar cada punto Y copiando exclusivamente `exact-NANDINA coverage` de la tabla canónica;
5. conservar `ymin = 0` y `ymax = 0.35`;
6. no dibujar líneas de conexión entre profundidades;
7. no dibujar barras de error, CI ni anotaciones de significancia;
8. no incluir `diagnostic_union_hierarchical_dual`;
9. conservar las cuatro variantes de G3C-005 y la variante 70/30 contextual;
10. distinguir la variante contextual por rol, no por menor opacidad, menor tamaño o menor contraste;
11. garantizar que los cinco marcadores se distingan sin color;
12. usar tipografía mínima recomendada de 9 pt al tamaño final de impresión para ticks/leyenda y al menos 10 pt para etiquetas de ejes; el título de panel/figura se ajustará al estilo editorial final;
13. usar gridlines horizontales principales finas y visualmente subordinadas a las marcas;
14. no añadir numeradores, promedios, deltas ni porcentajes calculados;
15. validar por comparación programática posterior que las 15 coordenadas Y coincidan con el CSV canónico dentro de representación numérica de lectura, sin recomputación científica.

---

# K. Checklist obligatorio de auditoría FIG003

| Control | Estado | Justificación |
|---|---|---|
| `FIG003_SOURCE_BLOB_IDENTITY` | PASS | Todos los blobs obligatorios coinciden con los congelados indicados por FIG003. |
| `FIG003_G3C005_TRACEABILITY_RESOLVED` | PASS | Los 12 IDs fuente de G3C-005 se mapearon directamente al registro G3. |
| `FIG003_FOUR_FORMAL_VARIANTS_IDENTIFIED` | PASS | Se identificaron `hierarchical_only`, `dual_only`, `hierarchical_first_100` y `hierarchical_80_dual_backfill_20`. |
| `FIG003_CONTEXT_VARIANTS_EXPLICIT` | PASS | `hierarchical_70_dual_backfill_30` queda explícitamente como contexto descriptivo adicional. |
| `FIG003_ALL_CANONICAL_ROWS_ACCOUNTED` | PASS | La especificación representa las 15 filas: 12 formales + 3 contextuales. |
| `FIG003_NO_CHERRY_PICKING` | PASS | Se conservan las cinco variantes de la tabla canónica y las tres profundidades. |
| `FIG003_DESCRIPTIVE_ONLY` | PASS | Rol fijado como `DESCRIPTIVE_SUPPLEMENTARY`; no se formula contraste confirmatorio. |
| `FIG003_NO_CI` | PASS | No se autorizan ni representan CI o error bars. |
| `FIG003_NO_NEW_INFERENCE` | PASS | No se introducen pruebas, p-values, significancia ni inferencia entre variantes. |
| `FIG003_NO_NEW_METRICS` | PASS | Solo se grafica `exact-NANDINA coverage` congelada; no se derivan métricas adicionales. |
| `FIG003_DIAGNOSTIC_UNION_EXCLUDED_FROM_PERFORMANCE` | PASS | `diagnostic_union_hierarchical_dual` queda fuera de las 15 marcas ordinarias. |
| `FIG003_AXIS_BASELINE_INTEGRITY` | PASS | Eje Y lineal inicia en 0; no hay breaks ni truncamiento basal. |
| `FIG003_NO_FAVORABILITY_ENCODING` | PASS | Orden, tamaño y peso visual no dependen del desempeño observado. |
| `FIG003_ACCESSIBLE_WITHOUT_COLOR_ONLY` | PASS | Cada variante posee marcador distinto y la figura debe funcionar en escala de grises. |
| `FIG003_HE2_PRESERVED` | PASS | La figura es descriptiva y no redecide ni amplía el soporte confirmatorio de HE2. |

Todos los controles obligatorios quedan en `PASS`.

---

# L. Disposición terminal

```text
FIG003_DISPOSITION = APPROVABLE_FOR_IMPLEMENTATION_SPEC
```

La especificación científico-visual de `G6-FIG-02` queda cerrada para auditoría externa. Esta disposición **no autoriza todavía la generación de la figura ni la ejecución de G6-F02**.
