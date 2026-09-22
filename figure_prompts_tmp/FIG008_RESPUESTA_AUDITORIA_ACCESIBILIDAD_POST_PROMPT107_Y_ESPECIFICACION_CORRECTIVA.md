# FIG008 — Respuesta de auditoría independiente de accesibilidad post-Prompt107 y especificación correctiva

## 1. DICTAMEN_TERMINAL

```text
FIG008_RESULT = ACCESSIBILITY_CORRECTION_REQUIRED
FIG01_ACCESSIBILITY_FINDING = CONFIRMED_BLOCKING
FIG02_ACCESSIBILITY_FINDING = CORRECTION_REQUIRED
FIG03_ACCESSIBILITY_FINDING = CORRECTION_REQUIRED
NEXT_ACTOR = CODEX
G6_F03_APPROVAL_AUTHORIZED = false
GROUP6_CLOSED = false
G7_F01_AUTHORIZED = false
```

El hallazgo bloqueante registrado por Prompt107 para G6-FIG-01 queda **confirmado independientemente**. Además, la auditoría preventiva identifica dos defectos formales adicionales que conviene corregir en la misma intervención técnica: el título del eje x de G6-FIG-02 no alcanza el mínimo de 10 pt exigido para etiquetas de eje, y los títulos de panel de G6-FIG-03 no alcanzan el objetivo de 9.5–10 pt fijado por el registry. En G6-FIG-02, los ticks y la leyenda también quedan muy por debajo de la recomendación de 9 pt; esto se clasifica como `NONBLOCKING_BUT_RECOMMENDED`, pero debe corregirse en la misma intervención para evitar deuda visual.

No se detecta ningún motivo científico para cambiar datos, métricas, CI, denominadores, orden, escalas, paneles, marks o claims.

---

## 2. Fuentes exactas revisadas

### Autoridad principal

```text
MAIN = 71b13caf6b97e254b4c701b23318bcb0682714bd

outputs/figures/group6/g6_figure_spec_registry_v0.1.json
  git blob = 44cc30fc3c38639c6aa4370cb6f317458041f1b1

outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
  git blob = 10616c7ddac277cc0e788af0b44322a5f93b59d4
```

### G6-FIG-01

```text
figures/group6/g6_fig_01_he2.svg
  git blob = 69748b888f3160407800c7548a978a7de27c138c

figures/group6/g6_fig_01_he2.png
  ledger = 2500 x 3125 px / 300 dpi

src/figures/group6/render_g6_fig_01_he2.py
  git blob = 5222113f6eb5867b1c9aa46214933c8879745127
```

### G6-FIG-02

```text
figures/group6/g6_fig_02_phase_e.svg
  git blob = 73e807e73a731e13d043f0a662b7e22c62b94c6a

figures/group6/g6_fig_02_phase_e.png
  ledger = 3000 x 1688 px / 300 dpi

src/figures/group6/render_g6_fig_02_phase_e.py
  git blob = 4f27d1db420dd1e3eaaa7fea394da88497381d3a
```

### G6-FIG-03

```text
figures/group6/g6_fig_03_exp11a.svg
  git blob = 9af7c3fd3308cf2a13067258e66de82adaba490a

figures/group6/g6_fig_03_exp11a.png
  ledger = 3000 x 2000 px / 300 dpi

src/figures/group6/render_g6_fig_03_exp11a.py
  git blob = ca522940c05e4c937eef54320c01966aaeb263ee
```

### Antecedente del STOP

```text
codex_prompts_tmp/107_RESPUESTA_CERRAR_G6_F02_Y_EJECUTAR_G6_F03_CAPTIONS_ACCESIBILIDAD.md
  commit = 7e46f10ba42dc2ea54562da1c1f0dffb9ee2bf9f
  git blob = f90f0e5ff5bc92b2a69af53940278c00f7eed14b
```

### Ficha rectora

```text
docs/fichas/grupos_3_8/grupo_6/G6_F03_CAPTIONS_ACCESIBILIDAD_Y_CIERRE.md
  branch = docs/fichas-grupos-3-8
  git blob = 68432ee2383cb510fcbd3267a592a8c2cd5b854d
```

El ledger confirma las identidades canónicas y tamaños de los seis outputs. Los headers PNG inspeccionados son consistentes con las dimensiones del ledger y contienen `pHYs = 11811 px/m`, equivalente a aproximadamente 300 dpi.

---

## 3. Auditoría independiente de G6-FIG-01

### 3.1 Requisito aprobado

El registry exige:

```text
Minimum effective font size = 8 pt
preferred axis/tick = 8.5–9 pt
```

La primera condición es obligatoria. La segunda es una preferencia explícita y no debe confundirse con el umbral bloqueante de 8 pt.

### 3.2 Tamaño mínimo materializado

El SVG actual declara:

```text
width = 1000
height = 1250
viewBox = 0 0 1000 1250
```

Como `width` y `height` no tienen unidad física, se interpretan como CSS px. El menor `font-size` no vacío materializado es:

```text
font-size = 8.5
```

y aparece en los labels de comparador del Panel B:

```text
Flat
Hierarchical
D1a
```

El script confirma que esos labels se generan mediante `c.text(..., 8.5, ...)`.

### 3.3 PNG: dimensiones, DPI y tamaño físico

El PNG actual tiene:

```text
width_px = 2500
height_px = 3125
dpi ≈ 300 x 300
physical_width = 2500 / 300 = 8.3333 in
physical_height = 3125 / 300 = 10.4167 in
```

La conversión geométrica de las unidades de dibujo al tamaño físico del PNG es:

```text
1000 drawing units -> 8.3333 in
1 drawing unit -> 8.3333 / 1000 in
1 drawing unit -> 0.6000 pt
```

Por tanto, usando la escala geométrica:

```text
8.5 units x 0.6000 pt/unit = 5.10 pt
```

El raster se genera con Pillow a `scale=2.5`. Para el tamaño 8.5:

```text
requested_raster_font_px = round(8.5 x 2.5)
                         = round(21.25)
                         = 21 px

effective_raster_font_pt = 21 / 300 x 72
                         = 5.04 pt
```

La diferencia `5.10` vs `5.04` procede únicamente del redondeo del tamaño de fuente a píxeles enteros antes de rasterizar. Para el PNG real, `5.04 pt` es la estimación nominal más fiel al parámetro de rasterización.

Resultado:

```text
PNG minimum effective font ≈ 5.04 pt
mandatory minimum = 8.00 pt
PNG = FAIL
```

### 3.4 SVG: tamaño físico efectivo bajo la declaración actual

En SVG, un user unit sin unidad física se trata como CSS px. Usando 96 CSS px/in:

```text
8.5 CSS px / 96 px/in x 72 pt/in = 6.375 pt
```

Resultado:

```text
SVG minimum effective font = 6.375 pt
mandatory minimum = 8.00 pt
SVG = FAIL
```

### 3.5 Textos afectados al tamaño físico nativo del PNG

La relación raster nominal es:

```text
effective_pt = round(font_size_units x 2.5) / 300 x 72
```

| `font-size` del artefacto | Raster px | Efectivo PNG | Ejemplos | Estado frente a 8 pt |
|---:|---:|---:|---|---|
| 18 | 45 | 10.80 pt | título general | PASS |
| 16 | 40 | 9.60 pt | letras A/B/C | PASS |
| 13 | 32 | 7.68 pt | títulos internos de panel | **FAIL** |
| 11 | 28 | 6.72 pt | títulos de ejes | **FAIL** |
| 10 | 25 | 6.00 pt | subtítulo, ticks, labels de métrica, contexto | **FAIL** |
| 9 | 22 | 5.28 pt | leyenda Panel A, labels auxiliares, identidad Panel C | **FAIL** |
| 8.5 | 21 | 5.04 pt | comparadores Panel B | **FAIL** |

Además, los ticks/ejes quedan muy por debajo de la preferencia explícita `8.5–9 pt`.

### 3.6 ¿Existe una interpretación razonable bajo la cual cumpla?

No. Interpretar literalmente `font-size="8.5"` como 8.5 pt ignoraría la semántica de SVG/CSS y el tamaño físico del raster. Bajo las dos representaciones vigentes:

```text
PNG actual ≈ 5.04 pt
SVG declarado = 6.375 pt
```

ambas están por debajo del mínimo efectivo de 8 pt. Un eventual escalado externo podría agrandar la figura, pero el requisito se aplica al artefacto aprobado en su tamaño de salida y no puede depender de que un editor lo amplíe posteriormente.

```text
FIG01_ACCESSIBILITY_FINDING = CONFIRMED_BLOCKING
```

### 3.7 Resto de controles de accesibilidad

```text
contrast_and_legibility = FAIL_ONLY_FOR_TYPOGRAPHIC_SIZE
marker_discrimination = PASS
color_independence = PASS
label_overlap_or_clipping = NO_MATERIAL_DEFECT_OBSERVED_IN_CURRENT_LAYOUT
internal_ids_hidden = PASS
axis_baseline_and_scale = PASS
caption_readiness = SCIENTIFIC_CONTENT_READY / VISUAL_ARTIFACT_NOT_READY
```

Las formas redundantes círculo/cuadrado/triángulo/diamante conservan interpretación en escala de grises. Los rangos `[0,1]` y `[-0.1,1]` y las referencias en cero permanecen adecuados. No se detecta motivo para cambiar marks, datos o escalas.

---

## 4. Auditoría preventiva de G6-FIG-02

### 4.1 Requisito aprobado

El registry establece:

```text
Minimum recommended 9 pt for ticks/legend
at least 10 pt for axis labels
```

La primera parte es una **recomendación**; la segunda es un **mínimo explícito** para etiquetas de eje.

### 4.2 Tamaño físico actual

PNG:

```text
3000 x 1688 px / 300 dpi
physical_width = 10.0000 in
physical_height = 5.6267 in
```

El canvas usa 1200 unidades de ancho; por escala geométrica:

```text
1 drawing unit = 10 / 1200 in = 1/120 in = 0.6000 pt
```

El SVG actual declara:

```text
width = 1200 CSS px
height = 675 CSS px
viewBox = 0 0 1200 675
```

por lo que su tamaño CSS nativo es `12.5 in x 7.03125 in` a 96 CSS px/in. No coincide físicamente con el PNG de 10 in de ancho.

### 4.3 Etiquetas de eje

#### Eje y

`Exact-NANDINA coverage` está materializado con `font-size=17`, rotado y fuera del campo de datos.

PNG real:

```text
round(17 x 2.5) = 42 px
42 / 300 x 72 = 10.08 pt
```

SVG actual:

```text
17 / 96 x 72 = 12.75 pt
```

Resultado:

```text
Y axis label = PASS
position outside data field = PASS
minimum 10 pt = PASS
```

#### Eje x

`Recovery depth (ordered categories)` está materializado con `font-size=11`.

PNG real:

```text
round(11 x 2.5) = 28 px
28 / 300 x 72 = 6.72 pt
```

SVG actual:

```text
11 / 96 x 72 = 8.25 pt
```

Ambos son inferiores al mínimo explícito de 10 pt.

```text
FIG02-XAXIS-LABEL = BLOCKING
```

Este defecto no fue resuelto por la corrección previa del eje y y debe incluirse en la próxima intervención.

### 4.4 Ticks y leyenda

Los ticks del eje y y las entradas de leyenda usan `font-size=9`:

```text
PNG: round(9 x 2.5) = 22 px -> 5.28 pt
SVG: 9 / 96 x 72 = 6.75 pt
```

Las categorías `50 / 100 / 200` usan `font-size=11`:

```text
PNG = 6.72 pt
SVG = 8.25 pt
```

Por tanto, **ninguno** alcanza la recomendación de 9 pt en el PNG nativo y tampoco la alcanza en el SVG actual.

La expresión `minimum recommended 9 pt` no debe convertirse retroactivamente en un requisito formal absoluto. Sin embargo, `5.28–6.72 pt` está materialmente lejos de 9 pt y constituye una legibilidad débil a tamaño de publicación. Como ya existe una corrección bloqueante del eje x, elevar ticks y leyenda al nivel recomendado en la misma intervención es la opción más conservadora y evita una nueva deuda de accesibilidad.

```text
FIG02-TICKS-LEGEND = NONBLOCKING_BUT_RECOMMENDED
```

Los textos auxiliares de 9–10 unidades —nota inferior, N/denominadores y subtítulo— quedan aproximadamente en `5.28–6.00 pt` en el PNG. El registry no les fija un umbral específico, por lo que no se clasifican como incumplimiento formal independiente; sí conviene elevarlos al menos al mínimo general de legibilidad adoptado en la intervención si puede hacerse sin alterar el layout científico.

### 4.5 Resto de controles

```text
contrast_and_legibility = PARTIAL_FAIL_TYPOGRAPHY
marker_discrimination = PASS
color_independence = PASS
label_overlap_or_clipping = NO_MATERIAL_DEFECT_OBSERVED
internal_ids_hidden = PASS
axis_baseline_and_scale = PASS / y starts at 0
caption_readiness = SCIENTIFIC_CONTENT_READY / VISUAL_ARTIFACT_NOT_READY
```

Las cinco variantes conservan símbolos propios; la variante 70/30 permanece abierta y con igual peso visual; no hay connecting lines ni diagnostic union como mark ordinario. No se propone cambiar nada de esa semántica.

---

## 5. Auditoría preventiva de G6-FIG-03

### 5.1 Requisito aprobado

El registry fija:

```text
minimum effective font size >= 8.5 pt
panel titles = 9.5–10 pt
observations remain discernible
no vertical jitter
no overlap/clipping material
```

### 5.2 Paridad física SVG/PNG

El SVG ya declara explícitamente:

```text
width = 10.0 in
height = 6.666666666666667 in
viewBox = 0 0 1200 800
```

Por tanto:

```text
1200 units / 10 in = 120 units/in
1 unit = 72/120 = 0.6 pt
```

El PNG es:

```text
3000 x 2000 px / 300 dpi = 10.0 x 6.6667 in
```

La paridad física vector/raster es correcta.

### 5.3 Mínimo efectivo general

El helper `text()` aplica:

```python
size = max(size, 14.5)
```

En SVG:

```text
14.5 / 120 x 72 = 8.70 pt
```

En PNG:

```text
round(14.5 x 2.5) = 36 px
36 / 300 x 72 = 8.64 pt
```

Resultado:

```text
minimum effective font >= 8.5 pt = PASS
```

### 5.4 Títulos de panel

Los seis títulos `Top1 / Top3 / Top5 / Top10 / Top50 / MRR` se invocan nominalmente con tamaño 12, pero el helper los eleva solo a 14.5 unidades. Por tanto su tamaño efectivo es el mismo mínimo anterior:

```text
SVG = 8.70 pt
PNG = 8.64 pt
required panel-title target = 9.5–10 pt
```

Resultado:

```text
FIG03-PANEL-TITLES = BLOCKING
```

El artefacto supera el mínimo general de 8.5 pt, pero **no** satisface el requisito específico de los títulos de panel.

### 5.5 Observaciones, jitter y solapamiento

El render vigente usa:

```text
observed-run circle radius = 2.2 drawing units
H100 diamond radius = 4.8 drawing units
H25/H75 horizontal jitter increment = 0.04 x 160 = 6.4 units
H50-D1/H50-D2 horizontal jitter increment = 0.06 x 160 = 9.6 units
vertical jitter = 0
```

La separación horizontal mínima entre centros de observaciones de una misma condición es superior al diámetro de los círculos (`4.4 units`), por lo que las observaciones permanecen discernibles aun cuando compartan valores y iguales o cercanos. No se observa motivo para volver a ampliar jitter o reducir markers.

```text
observations remain discernible = PASS
vertical jitter = 0 / PASS
material overlap = PASS
material clipping = PASS
```

### 5.6 Resto de controles

```text
contrast_and_legibility = PASS_EXCEPT_PANEL_TITLE_SIZE
marker_discrimination = PASS
color_independence = PASS
internal_ids_hidden = PASS
axis_baseline_and_scale = PASS / all panels [0,1]
caption_readiness = SCIENTIFIC_CONTENT_READY / VISUAL_ARTIFACT_NOT_READY
```

No se proponen cambios cosméticos adicionales en G6-FIG-03.

---

## 6. Matriz consolidada de hallazgos

| issue_id | figure_id | severity | Hallazgo | Estado |
|---|---|---|---|---|
| `FIG008-F01-01` | G6-FIG-01 | `BLOCKING` | Font mínimo real ≈5.04 pt PNG / 6.375 pt SVG, menor que 8 pt | CONFIRMED |
| `FIG008-F01-02` | G6-FIG-01 | `BLOCKING` | Títulos de panel, ejes, ticks, labels y leyenda adicionales también caen por debajo de 8 pt en PNG; ejes/ticks no alcanzan 8.5–9 pt preferidos | CONFIRMED / SAME_ROOT_CAUSE |
| `FIG008-F02-01` | G6-FIG-02 | `BLOCKING` | Título del eje x ≈6.72 pt PNG / 8.25 pt SVG, menor que el mínimo de 10 pt para axis labels | CONFIRMED |
| `FIG008-F02-02` | G6-FIG-02 | `NONBLOCKING_BUT_RECOMMENDED` | Ticks/leyenda ≈5.28–6.72 pt PNG y 6.75–8.25 pt SVG, por debajo de la recomendación de 9 pt | CONFIRMED |
| `FIG008-F02-03` | G6-FIG-02 | `INFORMATIONAL` | Textos auxiliares de 9–10 unidades quedan ≈5.28–6.00 pt en PNG; no tienen umbral propio congelado | OBSERVED |
| `FIG008-F03-01` | G6-FIG-03 | `BLOCKING` | Títulos de panel ≈8.64 pt PNG / 8.70 pt SVG, menores que 9.5–10 pt | CONFIRMED |
| `FIG008-F03-02` | G6-FIG-03 | `INFORMATIONAL` | Mínimo general 8.64/8.70 pt, observaciones discernibles, sin jitter vertical ni clipping material | PASS |

No se detectaron defectos adicionales en escalas, baselines, codificación redundante, orden científico, visibilidad de IDs internos o semántica de marcas.

---

## 7. Especificación correctiva mínima

La siguiente intervención debe ser **una sola corrección técnica consolidada** sobre los tres renders existentes. No es rediseño de figuras ni nueva ejecución científica.

### 7.1 G6-FIG-01

```text
figure_id = G6-FIG-01
issue_id = FIG008-F01-01 + FIG008-F01-02
severity = BLOCKING
current_state = min 5.04 pt PNG / 6.375 pt SVG; multiple text classes below 8 pt
required_target = every effective text >= 8 pt at native PNG size; axis/tick preferably 8.5–9 pt; SVG must also satisfy >=8 pt
```

**Cambio principal recomendado:** conservar el tamaño físico actual del PNG y aumentar la tipografía, en lugar de falsificar cumplimiento alterando solo DPI o ampliando artificialmente el tamaño físico de publicación.

Para mantener paridad vector/raster, se recomienda además declarar el SVG en unidades físicas correspondientes al PNG, siguiendo el patrón ya usado por G6-FIG-03:

```text
SVG width = 1000/120 in = 8.333333 in
SVG height = 1250/120 in = 10.416667 in
viewBox remains = 0 0 1000 1250
```

Con `120 drawing units/in`, objetivos seguros:

```text
general mandatory floor = >=13.5 drawing units
  nominal SVG = 13.5/120*72 = 8.10 pt
  raster = round(13.5*2.5)=34 px -> 8.16 pt

preferred axis/tick target = 15 drawing units
  SVG = 9.00 pt
  raster = round(37.5)=38 px -> 9.12 pt

panel titles recommended = 15–16 drawing units, subject to overlap validation
```

`allowed_visual_changes`:

- aumentar font sizes;
- pequeños desplazamientos de labels/márgenes para evitar colisiones producidas por el aumento tipográfico;
- declarar dimensiones físicas del SVG coherentes con el PNG;
- ampliar solo espacios blancos o márgenes si fuera imprescindible, sin cambiar las escalas científicas.

`forbidden_changes`:

- cambiar valores, CI, denominadores o métricas;
- cambiar los 15 contrastes de Panel B o el único contraste de Panel C;
- crear CI por brazo;
- mover rangos `[0,1]` y `[-0.1,1]` para magnificar diferencias;
- cambiar el orden de métricas/comparadores;
- alterar marks por favorabilidad;
- introducir p-values, inferencia o claims.

`validation_after_render`:

```text
all nonempty text >= 8.0 pt in PNG and SVG
axis/tick >= 8.5 pt preferred, target ~9 pt
no text overlap or clipping
all 15 Panel-B contrasts preserved
Panel-A arm CI count = 0
Panel-C confirmatory estimate count = 1
Pool@200 confirmatory mark count = 0
same scientific ranges and zero references
ledger updated to canonical Git bytes
```

### 7.2 G6-FIG-02

```text
figure_id = G6-FIG-02
issue_id = FIG008-F02-01 + FIG008-F02-02
severity = BLOCKING + NONBLOCKING_BUT_RECOMMENDED
current_state = x-axis label 6.72 pt PNG / 8.25 pt SVG; ticks/legend below recommended 9 pt
required_target = all axis labels >=10 pt; ticks/legend >=9 pt recommended and to be achieved in same correction
```

**Cambio principal recomendado:** mantener el canvas y datos actuales, normalizar el SVG a tamaño físico equivalente al PNG y aumentar solo tipografía/espacios necesarios.

Paridad física recomendada:

```text
SVG width = 10.0 in
SVG height = 675/120 in = 5.625 in
viewBox remains = 0 0 1200 675
```

Objetivos seguros a 120 units/in:

```text
axis labels >= 17 drawing units
  SVG = 10.2 pt
  PNG for 17 units = 42 px -> 10.08 pt

ticks/legend = 15 drawing units
  SVG = 9.0 pt
  PNG = 38 px -> 9.12 pt

supporting annotations: preferably >=13.5 units (~8.1 pt) when space allows
```

El y-axis label ya usa 17 unidades y debe conservarse fuera del campo de datos. El x-axis label debe elevarse desde 11 a al menos 17. Los ticks y entries de leyenda deben elevarse a 15 en esta misma intervención. Los labels `50/100/200`, al funcionar como ticks categóricos, también deben llevarse al objetivo recomendado de 9 pt.

`allowed_visual_changes`:

- font sizes;
- redistribución mínima de la caja de leyenda/márgenes;
- line breaks ya permitidos para labels largos;
- paridad física SVG/PNG.

`forbidden_changes`:

- cambiar las 15 marcas;
- cambiar valores o profundidades 50/100/200;
- unir puntos con líneas;
- incluir diagnostic union como rendimiento ordinario;
- alterar el estatus contextual de 70/30;
- introducir CI, p-values, tendencias o nuevos agregados.

`validation_after_render`:

```text
x-axis title >=10 pt PNG/SVG
y-axis title >=10 pt PNG/SVG and remains outside plot field
ticks/legend >=9 pt target
mark_count = 15
formal variants = 4
context-only 70/30 = 1
connecting lines = 0
CI = 0
p-values = 0
no overlap/clipping after larger typography
ledger updated to canonical Git bytes
```

### 7.3 G6-FIG-03

```text
figure_id = G6-FIG-03
issue_id = FIG008-F03-01
severity = BLOCKING
current_state = panel titles 8.64 pt PNG / 8.70 pt SVG
required_target = panel titles >=9.5 pt; minimum general text remains >=8.5 pt
```

La corrección debe ser mínima: **solo elevar los títulos de panel**, sin cambiar el floor general de 14.5, markers, jitter o geometría científica.

Objetivo recomendado:

```text
panel-title font-size = 16 drawing units
SVG = 16/120*72 = 9.60 pt
PNG = round(16*2.5)=40 px -> 9.60 pt
```

Para lograrlo, el helper no debe convertir explícitamente el título de panel de 16 a otro valor; el resto de textos puede permanecer con el floor de 14.5 que ya produce 8.64–8.70 pt.

`allowed_visual_changes`:

- aumentar únicamente títulos de panel a 16 units;
- microajuste vertical del título si fuera necesario para evitar colisión.

`forbidden_changes`:

- cambiar el jitter aprobado;
- añadir jitter vertical;
- cambiar marker radius;
- ocultar o agregar corridas;
- graficar summaries;
- cambiar `[0,1]`;
- introducir CI, p-values, regresión o smoothing;
- cambiar el orden H25 / H50-D1 / H50-D2 / H75 / H100 ref.

`validation_after_render`:

```text
minimum effective font >=8.5 pt
all six panel titles >=9.5 pt
observed_run_count = 31
condition counts = 10 / 5 / 5 / 10 / 1
summary marks = 0
vertical jitter = 0
observations discernible = true
no material overlap/clipping
ledger updated to canonical Git bytes
```

### 7.4 Validación transversal obligatoria tras la corrección

CODEX debe re-renderizar solo las figuras afectadas a partir de las mismas fuentes canónicas y actualizar el ledger. La auditoría posterior debe verificar:

```text
SCIENTIFIC_DATA_CHANGE_COUNT = 0
METRIC_CHANGE_COUNT = 0
CI_CHANGE_COUNT = 0
DENOMINATOR_CHANGE_COUNT = 0
CLAIM_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_P_VALUE_COUNT = 0
FIGURE_COUNT = 3
SVG_PNG_SCIENTIFIC_EQUIVALENCE = true
CANONICAL_LEDGER_MATCH = true
```

No se recomienda resolver el problema modificando solo el DPI metadata, declarando un tamaño físico artificialmente mayor o escalando el SVG externamente: esas soluciones desplazan el problema al pipeline editorial y no corrigen la accesibilidad nativa del artefacto.

---

## 8. Actor siguiente

```text
NEXT_ACTOR = CODEX
```

La razón es técnica y directa: existen correcciones que requieren modificar scripts de render, regenerar SVG/PNG y actualizar el ledger versionado. La IA Experimental debe intervenir **después** de ese candidato correctivo para verificar independientemente que las correcciones de accesibilidad se aplicaron sin drift científico y decidir la reanudación de G6-F03.

Secuencia recomendada:

```text
FIG008 external audit evidence
→ CODEX corrective render package
→ IA Experimental re-audit of corrected G6-F02 artifacts
→ if PASS, resume G6-F03
```

Esta respuesta no autoriza por sí misma ninguna modificación de `main` ni el cierre de G6-F03.

---

## 9. Declaraciones de no-ejecución / no-modificación

```text
FIG008_GITHUB_MODIFICATION = RESPONSE_FILE_ONLY
FIG008_MAIN_MODIFIED = false
FIG008_PLAN_MODIFIED = false
FIG008_FICHAS_MODIFIED = false
FIG008_FIGURES_EDITED = false
FIG008_FIGURES_REGENERATED = false
FIG008_RENDER_SCRIPTS_EDITED = false
FIG008_LEDGER_EDITED = false
FIG008_G6_F03_EXECUTED = false
FIG008_CAPTIONS_FINAL_CREATED = false
FIG008_GROUP6_CLOSED = false
FIG008_G7_ACTIVATED = false
FIG008_THESIS_MODIFIED = false
FIG008_ARTICLE_MODIFIED = false
FIG008_EXP12_REOPENED = false
FIG008_NEW_SCIENTIFIC_METRICS = 0
FIG008_NEW_INFERENCE = 0
FIG008_NEW_CI = 0
FIG008_NEW_P_VALUES = 0
```

La única escritura realizada por FIG008 es este archivo de respuesta en `codex/prompts-temporary`.
