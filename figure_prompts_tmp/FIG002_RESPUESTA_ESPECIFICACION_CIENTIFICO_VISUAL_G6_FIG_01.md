# FIG002 — Respuesta oficial: especificación científico-visual de G6-FIG-01

## 0. Alcance y verificación de trazabilidad

Se ejecutó exclusivamente `figure_prompts_tmp/FIG002_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_01.md` en el commit `8f29869d3d706a39f32fece1fe8c767f6bbe7f4d`.

Se tomó como base conceptual aprobada `figure_prompts_tmp/FIG001_RESPUESTA_REVISION_CRITICA_CATALOGO_INICIAL.md@2c31d0c7112abedab224023b33d8173f116b3712`.

No se generó ninguna figura, mockup, PNG, SVG, PDF ni script; no se modificó `main`, Plan Maestro, fichas, artículo o tesis; no se recalcularon métricas, diferencias, intervalos, p-values ni inferencia; no se reabrió EXP12; no se diseñaron G6-FIG-02 ni G6-FIG-03.

### 0.1 Verificación de fuentes congeladas

Todas las fuentes científicas obligatorias continúan presentes en `main = ca065618d5df0019f76ef5a971e858d91c263e1f` con los blobs congelados requeridos:

| Fuente | Blob esperado | Blob observado | Estado |
|---|---|---|---|
| `outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv` | `cb68583ee2260e4455796bac99ad90995ca7ef92` | `cb68583ee2260e4455796bac99ad90995ca7ef92` | PASS |
| `outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv` | `359e4e19b5ef1d44983c03039162209293b2a44c` | `359e4e19b5ef1d44983c03039162209293b2a44c` | PASS |
| `outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv` | `da0351cb523fc7f3b45a83e072765a07f809b7fe` | `da0351cb523fc7f3b45a83e072765a07f809b7fe` | PASS |
| `outputs/results/group5/g5_table_registry_v0.1.json` | `4fe9318d52fad093066ff9f42d524fc95e436245` | `4fe9318d52fad093066ff9f42d524fc95e436245` | PASS |
| `docs/results/group5/g5_results_presentation_plan_v0.1.md` | `9eaf780f3a2f6c8579dc80867ed3a86e96683894` | `9eaf780f3a2f6c8579dc80867ed3a86e96683894` | PASS |
| `docs/results/group5/g5_canonical_tables_v0.1.md` | `9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d` | `9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d` | PASS |
| `outputs/audits/group5_closure_v0.1.json` | `1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf` | `1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf` | PASS |

**Drift científico material:** no detectado.

Se preserva el contrato congelado:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
HE2 = SUPPORTED
```

También permanecen vigentes los guardrails que impiden equiparar la superioridad del retrieval histórico con exactitud global del RAG, la evidencia normativa con corrección jurídica vinculante o la explicación auditable con corrección clasificatoria/jurídica.

---

# A. Dictamen de composición

```text
FIGURE_ID = G6-FIG-01
FINAL_PANEL_COUNT = 3
ORIENTATION = VERTICAL / PORTRAIT
RECOMMENDED_ASPECT_RATIO = 4:5 (width:height ≈ 0.80)
READING_ORDER = A → B → C
MERGE_HE2A_HE2B = true
```

## A.1 Arquitectura general elegida

Se recomienda una figura vertical de tres paneles apilados, todos a ancho completo y con una sola dirección de lectura de arriba hacia abajo:

1. **Panel A — HE2_A: valores absolutos observados.** Contextualiza el nivel de desempeño de Historical y los tres comparadores corregidos en las cinco métricas primarias.
2. **Panel B — HE2_A: contrastes pareados.** Constituye el núcleo inferencial de la figura y muestra los 15 estimandos `Historical − comparator` con sus CI de 99%.
3. **Panel C — HE2_B: cobertura profunda.** Integra el único contraste primario `Recall@200 − Recall@100` con CI de 95%, conservando los valores absolutos solo como contexto textual breve.

Distribución vertical recomendada del área útil, excluyendo título/leyenda/caption:

```text
Panel A ≈ 32%
Panel B ≈ 48%
Panel C ≈ 20%
```

El Panel B recibe mayor altura porque contiene 15 estimandos con incertidumbre y constituye la lectura inferencial principal de HE2_A. El Panel C se mantiene deliberadamente compacto para conservar el peso científico de `G3C-004` sin sobrerrepresentar visualmente un único contraste.

## A.2 Justificación del número de paneles

**Tres paneles** es la solución mínima que preserva simultáneamente tres semánticas distintas:

- valores absolutos por brazo sin CI;
- diferencias pareadas HE2_A con CI de 99%;
- diferencia pareada HE2_B con CI de 95%.

Una solución de **dos paneles** obligaría a mezclar HE2_B dentro del panel de contrastes HE2_A o dentro del panel de valores absolutos, aumentando el riesgo de confundir niveles de CI, estimandos y roles científicos. Una solución de **cuatro paneles** exigiría separar artificialmente los valores absolutos y el contraste de HE2_B o fragmentar HE2_A sin necesidad científica, incrementando complejidad visual sin añadir evidencia.

No existe motivo para revisar la decisión de FIG001 de fusionar HE2_A y HE2_B en una única figura principal.

---

# B. Especificación panel por panel

## B.1 Panel A — HE2_A: desempeño absoluto observado

```text
panel_id = A
scientific_question = ¿Cuál es el valor observado de cada método en las cinco métricas primarias de ranking temprano?
claim_ids = G3C-001, G3C-002, G3C-003 (contexto descriptivo de los brazos; la inferencia está en Panel B)
source_path = outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
source_blob = cb68583ee2260e4455796bac99ad90995ca7ef92
chart_type = GROUPED_DOT_PLOT
```

### Filas y columnas utilizadas

Se utilizan las 15 filas `G3F03-0001:G3F03-0015`, con las columnas:

```text
comparison
metric
historical_observed_value
comparator_observed_value
EVAL_N
DAM_N
source_version
```

Mapeo visual:

- `Historical`: un único punto por métrica. Los valores históricos aparecen repetidos en las tres familias de comparación del CSV por estructura tabular; **se visualizan una sola vez por métrica**.
- `Flat (Attempt06)`: `comparator_observed_value` de `HISTORICAL_MINUS_FLAT`.
- `Hierarchical (Attempt06)`: `comparator_observed_value` de `HISTORICAL_MINUS_HIERARCHICAL`.
- `D1a (Attempt06)`: `comparator_observed_value` de `HISTORICAL_MINUS_D1A`.

La implementación debe verificar que los tres valores históricos repetidos para cada métrica son idénticos antes de deduplicarlos visualmente. Si no lo fueran, debe detenerse la implementación; no se autoriza promediarlos ni seleccionar uno por conveniencia.

### Marcas

- Solo puntos/símbolos.
- Cuatro posiciones verticales fijas dentro de cada banda de métrica, en orden de leyenda.
- No usar jitter aleatorio.
- No usar líneas que conecten métricas ni métodos.
- No usar barras, áreas, volumen ni 3D.

### Ejes

```text
x_axis = Observed metric value
x_scale = linear
x_range = [0.00, 1.00]
y_axis = Primary metric
y_order = Top-1, Top-3, Top-5, Top-10, MRR@100
unit = proportion-scale metric value
reference_lines = none; major x-gridlines only
axis_breaks = prohibited
```

Ticks recomendados del eje x:

```text
0.0, 0.2, 0.4, 0.6, 0.8, 1.0
```

No se permite truncar el eje absoluto para hacer más visibles las diferencias de baja magnitud entre comparadores.

### Codificación

- `Historical`: círculo relleno.
- `Flat (Attempt06)`: cuadrado abierto.
- `Hierarchical (Attempt06)`: triángulo abierto.
- `D1a (Attempt06)`: rombo abierto.
- Color cualitativo consistente con los mismos métodos en los demás paneles, pero la forma del marcador debe permitir identificar cada método sin color.

Orden de leyenda:

```text
Historical
Flat (Attempt06)
Hierarchical (Attempt06)
D1a (Attempt06)
```

Se recomienda una sola leyenda compartida para toda la figura, ubicada arriba del Panel A o entre el título y el Panel A.

### Incertidumbre

```text
uncertainty = NONE AT ARM LEVEL
```

No se dibuja ningún CI, error bar, banda o sombra alrededor de los valores absolutos.

### Anotaciones

- No mostrar etiquetas numéricas junto a los 20 puntos; la tabla canónica conserva los valores exactos y la figura debe priorizar patrón visual.
- No repetir `N=1056` ni `67 DAM` dentro del panel; se reservan al caption.
- El subtítulo del panel debe indicar explícitamente: `Observed arm values; no arm-level CI` o equivalente en español.

### Transformaciones prohibidas

- Promediar los tres valores históricos repetidos.
- Repetir Historical tres veces por comparación.
- Calcular CI por brazo.
- Convertir Top-k y MRR@100 en una trayectoria continua.
- Reordenar métricas por valor observado.
- Normalizar cada métrica por su máximo.
- Truncar el eje absoluto.
- Convertir la figura en ranking del sistema RAG completo.

### Controles de riesgo

- La deduplicación visual de Historical evita pseudorreplicación gráfica.
- La ausencia de líneas evita implicar continuidad entre Top-1/3/5/10 y MRR@100.
- El rango completo `[0,1]` impide exagerar diferencias absolutas.
- Forma + color evita dependencia exclusiva de la paleta.

---

## B.2 Panel B — HE2_A: diferencias pareadas Historical − comparator

```text
panel_id = B
scientific_question = ¿Cuál es la magnitud y la incertidumbre de los 15 contrastes pareados Historical − comparator en las cinco métricas primarias?
claim_ids = G3C-001, G3C-002, G3C-003
source_path = outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
source_blob = cb68583ee2260e4455796bac99ad90995ca7ef92
chart_type = GROUPED_DOT_WHISKER_PLOT
```

### Filas y columnas utilizadas

Se utilizan las 15 filas `G3F03-0001:G3F03-0015` y exclusivamente las columnas:

```text
comparison
metric
paired_difference_historical_minus_comparator
frozen_99pct_ci_lower_for_paired_difference
frozen_99pct_ci_upper_for_paired_difference
EVAL_N
DAM_N
source_version
```

No se vuelven a usar los valores absolutos de brazo en este panel.

### Marcas

Por cada combinación `metric × comparator`:

- un punto en `paired_difference_historical_minus_comparator`;
- un whisker horizontal desde `frozen_99pct_ci_lower_for_paired_difference` hasta `frozen_99pct_ci_upper_for_paired_difference`;
- caps discretos en ambos extremos del CI;
- tres posiciones verticales fijas dentro de cada banda de métrica, en orden Flat, Hierarchical, D1a.

No usar jitter aleatorio.

### Ejes

```text
x_axis = Paired difference (Historical − comparator)
x_scale = linear
x_range = [-0.10, 1.00]
y_axis = Primary metric
y_order = Top-1, Top-3, Top-5, Top-10, MRR@100
unit = absolute difference in proportion-scale metric value
reference_lines = vertical line at x = 0
axis_breaks = prohibited
```

El pequeño margen negativo mantiene la referencia nula dentro del área gráfica, sin usar un eje truncado ni excluir ningún CI congelado. No existe necesidad de mostrar todo el soporte teórico `[-1,1]`; el rango propuesto contiene cero y todos los intervalos congelados con margen visual suficiente.

Ticks recomendados:

```text
-0.1, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0
```

### Codificación

Los tres comparadores usan los mismos símbolos asignados en el Panel A:

- Flat: cuadrado.
- Hierarchical: triángulo.
- D1a: rombo.

El color puede reforzar la identidad del comparador, pero la forma del punto es obligatoria. Los whiskers deben heredar el color del comparador o, si la versión final requiere mayor sobriedad, usar un gris oscuro común conservando el punto codificado por forma y color. En ambos casos la interpretación no puede depender solo del color.

La leyenda compartida de métodos se mantiene; el título o subtítulo del panel debe declarar de forma visible:

```text
Historical − comparator; 99% CI for paired differences
```

### Incertidumbre

```text
uncertainty = frozen 99% CI bound only to paired_difference_historical_minus_comparator
```

El CI de 99% nunca debe aparecer visualmente unido a `historical_observed_value` ni a `comparator_observed_value`.

### Anotaciones

- No mostrar p-values.
- No usar asteriscos de significancia.
- No etiquetar cada uno de los 15 puntos con su valor numérico; la estimación se lee del eje y la tabla canónica conserva precisión exacta.
- No mostrar `N=1056` o `67 DAM` dentro del panel.
- Rounding de ejes únicamente para presentación; no alterar datos fuente.

### Transformaciones prohibidas

- Reordenar métricas o comparadores por magnitud del efecto.
- Omitir alguno de los 15 contrastes.
- Promediar contrastes entre métricas o comparadores.
- Calcular un efecto global.
- Cambiar CI de 99% por 95%.
- Calcular nuevos CI o p-values.
- Estandarizar diferencias.
- Recortar whiskers.
- Convertir el contraste a mejora relativa o porcentaje relativo.

### Controles de riesgo

- Línea de cero visible.
- Etiqueta explícita `Historical − comparator`.
- CI de 99% declarado en el propio panel.
- Misma secuencia de métricas que el Panel A.
- Tres comparadores visibles en cada métrica, sin cherry-picking.

---

## B.3 Panel C — HE2_B: contraste de cobertura profunda

```text
panel_id = C
scientific_question = ¿Cuánto aumenta la cobertura jerárquica corregida de Recall@100 a Recall@200 bajo el contraste primario HE2_B?
claim_ids = G3C-004
source_path = outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
source_blob = 359e4e19b5ef1d44983c03039162209293b2a44c
chart_type = SINGLE_ESTIMATE_DOT_WHISKER_WITH_CONTEXT_ANNOTATION
```

### Fila y columnas utilizadas

Fila:

```text
G3F03-0016
```

Columnas:

```text
comparison
Recall@100
Recall@200
paired difference
frozen CI lower
frozen CI upper
EVAL_N
DAM_N
source version
```

`Pool@200 context` se conserva en la fuente, pero **no se representa como un segundo punto, barra, intervalo o estimando**. Su valor coincide con Recall@200 y su duplicación produciría una falsa impresión de evidencia confirmatoria adicional.

### Marcas

- Un único punto en `paired difference = 0.20265151515151514`.
- Un whisker horizontal con `CI95% = [0.06676310583580614, 0.34160130792395144]`.
- Línea vertical de referencia en cero.
- Símbolo del punto: triángulo, consistente con `Hierarchical (Attempt06)`.

### Ejes

```text
x_axis = Paired difference (Recall@200 − Recall@100)
x_scale = linear
x_range = [-0.10, 1.00]
y_axis = single row: Hierarchical (Attempt06)
y_order = single row
unit = absolute difference in recall
reference_lines = vertical line at x = 0
axis_breaks = prohibited
```

Se conserva la misma escala de contraste del Panel B para impedir que un eje más estrecho magnifique visualmente el único efecto HE2_B.

### Codificación y anotación

El panel debe llevar una etiqueta visible:

```text
95% CI
```

Debe incluir, como contexto textual breve y no como dos series inferenciales:

```text
Recall@100 = 0.101
Recall@200 = 0.304
Δ = 0.203; 95% CI [0.067, 0.342]
```

Formato de visualización: tres decimales, manteniendo los valores completos en la fuente.

No se muestra una segunda anotación `Pool@200 = 0.304` porque duplicaría el mismo valor y el registro científico prohíbe conferirle rol confirmatorio independiente.

### Incertidumbre

```text
uncertainty = single frozen 95% CI for Recall@200 − Recall@100
```

El Panel C debe estar visualmente separado del Panel B mediante espacio vertical y encabezado propio, de modo que el lector no pueda interpretar su CI de 95% como parte de la familia de CI de 99% de HE2_A.

### Transformaciones prohibidas

- Graficar `Pool@200 context` como evidencia adicional.
- Calcular un segundo contraste.
- Calcular CI para Recall@100 o Recall@200 por separado.
- Convertir `0.2027` a incremento porcentual relativo.
- Cambiar el CI de 95% a 99% para homogeneizar la figura.
- Mezclar este estimando en el Panel B como si perteneciera a la misma familia inferencial.

### Controles de riesgo

- Un solo estimando gráfico.
- CI 95% explícito en título/subtítulo y anotación.
- Valores absolutos mostrados únicamente como contexto textual.
- `Pool@200` no duplicado.
- Escala del contraste idéntica a la de Panel B.

---

# C. Comparación de alternativas descartadas

## C.1 Panel A — desempeño absoluto HE2_A

### A. Dot plot agrupado — **SELECCIONADO**

Ventajas:

- permite mostrar cuatro métodos en cinco métricas con poco ink;
- preserva el eje absoluto `[0,1]` sin ocupar área con barras;
- hace posible deduplicar Historical una sola vez por métrica;
- admite forma + color para accesibilidad;
- no induce continuidad entre métricas al no usar líneas.

### B. Barras agrupadas — descartado

Razones:

- aumenta innecesariamente el peso visual de Historical por área/longitud;
- las barras muy pequeñas de Flat, Hierarchical y D1a cerca de cero son difíciles de comparar;
- requiere mucho espacio para 20 barras;
- el área rectangular añade saliencia sin aportar información respecto a la posición de un punto en un eje común.

### C. Small multiples por métrica — descartado

Razones:

- cinco subpaneles adicionales fragmentarían la lectura;
- repetirían ejes y leyendas;
- aumentarían el costo visual sin resolver un problema que el dot plot agrupado ya resuelve mediante posiciones fijas y símbolos distintos;
- elevarían el número total de paneles funcionales muy por encima de lo necesario.

**Decisión:** `GROUPED_DOT_PLOT`.

---

## C.2 Panel B — contrastes pareados HE2_A

### A. Forest plot clásico de 15 filas — descartado como forma principal

Es científicamente válido, pero menos eficiente para esta figura porque separaría cada contraste en una fila independiente y consumiría demasiada altura. Además, haría menos inmediata la comparación de los tres comparadores dentro de la misma métrica.

### B. Dot-whisker agrupado — **SELECCIONADO**

Ventajas:

- conserva las cinco métricas como grupos estables;
- muestra simultáneamente los tres comparadores por métrica;
- representa directamente el estimando y su CI;
- preserva la referencia en cero;
- reduce altura respecto de un forest de 15 filas sin perder ningún contraste;
- mantiene la identidad de comparadores mediante los mismos símbolos del Panel A.

### C. Heatmap de diferencias — descartado

Razones:

- una matriz de color puede mostrar magnitud de puntos estimados, pero no representa adecuadamente los 15 CI;
- añadir texto de CI dentro de celdas convertiría la figura en una tabla coloreada;
- depende más del color y es menos accesible en escala de grises;
- debilita la referencia visual a cero.

**Decisión:** `GROUPED_DOT_WHISKER_PLOT`.

---

## C.3 Integración de HE2_B

### A. Mini-panel con dos valores absolutos + mini forest — descartado

Mostrar Recall@100 y Recall@200 como marcas independientes y además el contraste produciría tres elementos gráficos para una sola comparación primaria. Eso incrementa el riesgo de interpretar los valores absolutos o `Pool@200` como evidencia inferencial adicional.

### B. Un solo panel de contraste con anotación de Recall@100/Recall@200 — **SELECCIONADO**

Ventajas:

- concentra la inferencia en el único estimando autorizado;
- conserva los dos valores absolutos como contexto sin otorgarles CI ni peso confirmatorio independiente;
- facilita etiquetar inequívocamente el CI de 95%;
- evita duplicar `Pool@200 context`.

### C. Bloque textual con un único estimando gráfico — descartado

Es científicamente seguro, pero reduce demasiado la continuidad visual de la figura y se acerca a una nota tabular. La opción B conserva la misma gramática gráfica de point estimate + whisker del Panel B y sigue siendo compacta.

**Decisión:** `SINGLE_ESTIMATE_DOT_WHISKER_WITH_CONTEXT_ANNOTATION`.

---

# D. Especificación de accesibilidad e implementación visual

## D.1 Color y codificación redundante

La figura puede usar una paleta cualitativa sobria y apta para daltonismo, pero **ninguna identidad depende solo del color**.

Codificación obligatoria:

| Método | Forma | Relleno | Uso |
|---|---|---|---|
| Historical | círculo | relleno | Panel A |
| Flat (Attempt06) | cuadrado | abierto | Paneles A/B |
| Hierarchical (Attempt06) | triángulo | abierto | Paneles A/B/C |
| D1a (Attempt06) | rombo | abierto | Paneles A/B |

No se fijan valores hexadecimales en FIG002. La paleta final puede congelarse durante la implementación, siempre que mantenga contraste suficiente y sea distinguible en impresión en escala de grises.

## D.2 Funcionamiento en escala de grises

La figura debe seguir siendo interpretable al convertirla a escala de grises porque:

- cada método tiene una forma diferente;
- Historical además se distingue por marcador relleno;
- los paneles B y C declaran explícitamente el estimando en texto/eje;
- los CI no dependen del color para indicar su significado;
- Panel C etiqueta explícitamente `95% CI` y Panel B `99% CI`.

## D.3 Tipografía

A tamaño final de impresión:

```text
minimum_font_size = 8 pt
preferred_axis_and_tick_size = 8.5–9 pt
panel_label_size = 10–11 pt bold
panel_title_size = 9.5–10 pt
legend_size = 8.5–9 pt
```

No reducir la tipografía por debajo de 8 pt para encajar la figura; si el entorno de publicación exige menor ancho, debe aumentarse la altura o dividirse la página, no comprimir ilegiblemente el contenido.

## D.4 Puntos, líneas y CI

- Diámetro de marcador recomendado: aproximadamente 4.5–5.5 pt a tamaño final.
- Contorno de marcador: aproximadamente 0.8 pt.
- Línea de CI: aproximadamente 0.8–1.0 pt.
- Caps: visibles pero discretos, de aproximadamente 3–4 pt de alto.
- Línea de cero: aproximadamente 1.0 pt; más visible que las gridlines, menos dominante que los datos.

## D.5 Gridlines

- Solo gridlines mayores en el eje x.
- Muy finas y visualmente secundarias.
- No usar grid vertical + horizontal simultáneo si genera retícula densa.
- No usar fondos coloreados por panel.

## D.6 Espaciado y jerarquía

- Paneles claramente separados por espacio en blanco.
- Panel B con mayor altura relativa.
- Panel C compacto, sin caja o color de fondo que lo haga parecer más importante que HE2_A.
- Etiquetas `A`, `B`, `C` alineadas en el margen izquierdo.
- Sin sombras, degradados, 3D, pictogramas ni decoraciones no informativas.

---

# E. Etiquetas, redondeo y anotaciones

## E.1 Nombres visibles

Métodos:

```text
Historical
Flat (Attempt06)
Hierarchical (Attempt06)
D1a (Attempt06)
```

Métricas:

```text
Top-1
Top-3
Top-5
Top-10
MRR@100
```

Contrastes:

```text
Historical − comparator
Recall@200 − Recall@100
```

No sustituir `Historical − comparator` por expresiones como “improvement” o “effect” sin cualificación, porque el contrato es no causal.

## E.2 Valores numéricos

- Panel A: no etiquetas numéricas junto a puntos.
- Panel B: no etiquetas numéricas junto a los 15 puntos/CI.
- Panel C: mostrar tres decimales para los dos valores absolutos, el delta y límites del CI.
- Los datos subyacentes se mantienen con la precisión completa del CSV.

## E.3 N y denominadores

`N=1056 series`, `67 DAM` y `42 NANDINA` deben aparecer una sola vez en el caption de trabajo, no repetidos dentro de los paneles.

## E.4 Etiquetado de incertidumbre

Obligatorio dentro de la propia figura:

- Panel B: `99% CI`.
- Panel C: `95% CI`.

No confiar únicamente en el caption para esta distinción.

---

# F. Caption de trabajo

**Caption preliminar — sujeto a revisión posterior en G6-F03:**

> **G6-FIG-01. Evidencia primaria de HE2 en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM, 42 NANDINA).** (A) Valores observados de Historical y de los tres comparadores corregidos Attempt06 en Top-1, Top-3, Top-5, Top-10 y MRR@100; los valores por brazo son descriptivos y no tienen CI autorizado. (B) Diferencias pareadas `Historical − comparator` para las cinco métricas primarias, con CI congelados de 99%. (C) Contraste HE2_B del retrieval jerárquico corregido, `Recall@200 − Recall@100`, con CI congelado de 95%; Recall@100 y Recall@200 se muestran solo como contexto y `Pool@200` no se duplica como evidencia confirmatoria. Los contrastes son no causales y se limitan al benchmark interno; la figura no representa exactitud global del framework RAG.

---

# G. Checklist de controles FIG002

| Control | Estado | Justificación |
|---|---|---|
| `FIG002_HE2A_ABSOLUTE_VS_CONTRAST_SEPARATION` | PASS | Panel A contiene solo valores absolutos; Panel B contiene exclusivamente diferencias pareadas e intervalos. |
| `FIG002_HE2A_CI_BOUND_TO_PAIRED_DIFFERENCE_ONLY` | PASS | Los CI de 99% se dibujan únicamente alrededor de `paired_difference_historical_minus_comparator`. |
| `FIG002_HE2B_95CI_SEPARATED_FROM_HE2A_99CI` | PASS | HE2_B se ubica en Panel C separado, con etiqueta explícita `95% CI`; Panel B declara `99% CI`. |
| `FIG002_POOL200_NOT_DUPLICATED_AS_CONFIRMATORY` | PASS | `Pool@200 context` no se representa como marca ni estimando; tampoco se repite numéricamente. |
| `FIG002_NO_ARM_LEVEL_CI` | PASS | Panel A no contiene barras de error, bandas ni CI por brazo. |
| `FIG002_NO_TRUNCATED_ABSOLUTE_AXIS` | PASS | Panel A usa eje absoluto lineal `[0,1]`. |
| `FIG002_NO_METRIC_TRAJECTORY_IMPLICATION` | PASS | No existen líneas entre Top-1/3/5/10/MRR@100; los puntos son discretos y las métricas permanecen categóricas. |
| `FIG002_NO_PSEUDOREPLICATION_OF_HISTORICAL` | PASS | Historical se visualiza una sola vez por métrica, pese a su repetición estructural en las tres comparaciones del CSV. |
| `FIG002_NO_CHERRY_PICKING` | PASS | Se incluyen las cinco métricas primarias, los tres comparadores y el único contraste HE2_B; no se omite ningún contraste por magnitud o favorabilidad. |
| `FIG002_NO_NEW_METRICS` | PASS | Solo se usan métricas y diferencias congeladas en G5-MAIN-01 y G5-MAIN-02; no se introducen mejoras relativas ni agregados nuevos. |
| `FIG002_NO_NEW_INFERENCE` | PASS | No se calculan nuevos CI, p-values, tests, promedios inferenciales ni efectos globales. |
| `FIG002_NO_GLOBAL_RAG_ACCURACY_OVERCLAIM` | PASS | El caption limita explícitamente la evidencia al retrieval dentro del benchmark interno y niega que represente exactitud global del RAG. |
| `FIG002_ACCESSIBLE_WITHOUT_COLOR_ONLY` | PASS | Identidad redundante mediante círculo/cuadrado/triángulo/rombo, relleno y texto; la figura debe funcionar en escala de grises. |

Todos los controles requeridos quedan en `PASS`.

---

# H. Disposición terminal

```text
APPROVABLE_FOR_IMPLEMENTATION_SPEC
```

La especificación científico-visual de `G6-FIG-01` queda suficientemente cerrada para auditoría externa y posterior implementación reproducible, sin que esta disposición autorice todavía generar la figura ni ejecutar G6-F02.
