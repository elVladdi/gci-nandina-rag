# FIG014 — Respuesta: resolver legibilidad de etiqueta H100 en Figura 6 / G7-F02

## 0. Alcance ejecutado

Se ejecutó exclusivamente `figure_prompts_tmp/FIG014_RESOLVER_LEGIBILIDAD_H100_FIGURA6_G7_F02.md@10272325f91cf56f25fdd6267a96d8683b00d896` bajo el rol de **IA Diseñadora y Auditora de Figuras Científicas**.

Se leyeron íntegramente los antecedentes gobernantes exigidos por FIG014:

- `figure_prompts_tmp/FIG012_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md@be0879c44b9d933bc0591bcf498b5e056cc31b20`.
- `figure_prompts_tmp/FIG012_AUDITORIA_EXTERNA_PASS.md@547e1dbfc34a03b9c569cf4d8c1792c88f94901b`.
- `figure_prompts_tmp/FIG013_REGENERAR_FIGURA6_TESIS_G7_F02.md@2e7a55900b6db32ba6711880e17a3f17ab82dee6`.
- `figure_prompts_tmp/FIG013_RESPUESTA_REGENERAR_FIGURA6_TESIS_G7_F02.md`.
- `figure_prompts_tmp/FIG013_AUDITORIA_EXTERNA_STOP_COMPLIANT.md`.

No se modificó el DOCX, no se regeneró SVG/PNG, no se modificaron scripts, no se ejecutó A043 y no se ejecutó 121G ni ningún bloque posterior.

Estado gobernante confirmado:

```text
FIG013_EXTERNAL_AUDIT = PASS_STOPPED_PRECONDITION
FIG013_STOP_COMPLIANT = true
FIGURE_6_CANDIDATE_CREATED = false
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
A043_EXECUTED = false
121G_AUTHORIZED = false
```

---

## 1. Problema de legibilidad confirmado

FIG013 verificó que `H100 (referencia)` no cabe en una sola línea manteniendo simultáneamente el tamaño, posición y anclaje originales del renderer G6: la etiqueta invade materialmente `H75` en los seis paneles.

Las mediciones gobernantes son:

```text
separación entre centros H75–H100 = 66.0 unidades SVG
ancho H75 = 26.4 unidades SVG
ancho H100 (referencia) = 116.8 unidades SVG
suma de semianchos = 71.6 unidades SVG
solapamiento horizontal = 5.6 unidades SVG
```

La auditoría externa de FIG013 confirmó que se trata de intersección real de tinta y que detenerse sin generar candidato fue conforme al contrato.

---

## 2. Auditoría de alternativas

### 2.1 `H100 (referencia)` con reducción local de fuente

**No recomendada / no cumple de forma segura.**

El tamaño actual de la etiqueta equivale aproximadamente a `8.7 pt` efectivos. Para eliminar el solapamiento manteniendo una sola línea y los mismos centros, la anchura de `H100 (referencia)` tendría que bajar de 116.8 a como máximo 105.6 unidades. Eso exige un factor aproximado de `0.904`, equivalente a unos `7.87 pt` efectivos.

Por tanto, la reducción suficiente para despejar completamente `H75` violaría el mínimo obligatorio `>= 8 pt`. A `8 pt` todavía queda una intersección horizontal residual aproximada de `0.9` unidades SVG.

```text
ALTERNATIVE_1 = REJECTED
reason = required font size would fall below 8 pt for clean one-line separation
```

### 2.2 `H100 (referencia)` con salto de línea

**Viable, pero no preferida.**

Separar en:

```text
H100
(referencia)
```

reduce la anchura máxima a la de `(referencia)`, aproximadamente 78.4 unidades SVG con la misma tipografía. Frente a `H75`, la suma de semianchos sería aproximadamente 52.4, dejando alrededor de 13.6 unidades de holgura horizontal.

No requiere mover la categoría ni la marca H100, y hay espacio vertical suficiente bajo ambos niveles de paneles. Sin embargo, introduce una segunda línea y modifica la presentación vertical del único rótulo categórico, por lo que es una intervención tipográfica mayor que una abreviatura inequívoca en una sola línea.

```text
ALTERNATIVE_2 = VIABLE_NOT_SELECTED
```

### 2.3 `H100 (ref.)`

**Seleccionada.**

Con el mismo tamaño y peso tipográfico del rótulo H100 original, `H100 (ref.)` ocupa aproximadamente `70.4` unidades SVG. Manteniendo los centros originales:

```text
ancho H75 = 26.4
ancho H100 (ref.) = 70.4
suma de semianchos = 48.4
separación entre centros = 66.0
holgura horizontal = 17.6 unidades SVG
```

La solución elimina el solapamiento sin reducir fuente, sin introducir salto de línea, sin mover el anclaje categórico y sin alterar la posición de ninguna marca científica.

`ref.` es una abreviatura editorial inequívoca en este contexto porque el caption aprobado conserva la formulación completa:

```text
H100 (n=1, referencia congelada)
```

y declara expresamente que H100 es una única referencia, no una distribución de réplicas.

```text
ALTERNATIVE_3 = SELECTED
```

### 2.4 Reposicionamiento/anclaje del nodo `H100 (referencia)`

**Viable en principio, pero no preferido.**

Manteniendo el texto completo y el tamaño original, bastaría aumentar al menos 5.6 unidades SVG la separación horizontal efectiva respecto de `H75`, o modificar localmente el anclaje del texto. Sin embargo, ello desplazaría visualmente la etiqueta respecto del centro de su categoría y es una intervención mayor que la abreviatura seleccionada.

No existe razón científica ni editorial para introducir ese desplazamiento cuando `H100 (ref.)` resuelve el bloqueo conservando exactamente la posición categórica original.

```text
ALTERNATIVE_4 = VIABLE_NOT_SELECTED
```

### 2.5 Combinaciones

No son necesarias. La alternativa 3 satisface simultáneamente legibilidad, tamaño mínimo, naturalidad académica, trazabilidad y mínima intervención.

```text
ALTERNATIVE_5 = NOT_NEEDED
```

---

## 3. Solución editorial aprobada

Se fija como solución única:

```text
H100_VISIBLE_LABEL = H100 (ref.)
H100_TEXT_FONT_SIZE = mantener (14.5 unidades SVG; ~8.7 pt efectivos)
H100_TEXT_LINE_BREAK = none
H100_TEXT_ANCHOR = mantener (middle / centrado en la categoría H100)
H100_TEXT_POSITION_ADJUSTMENT = none
```

Clasificación:

```text
TEXT_ONLY = true
TYPOGRAPHIC_LAYOUT_ONLY = false
SCIENTIFIC_GEOMETRY_CHANGE = false
SCIENTIFIC_DATA_CHANGE = false
```

La modificación futura deberá sustituir únicamente el texto visible del nodo de etiqueta H100. No se autoriza mover el centro de la categoría, el separador, el diamante H100, puntos, ejes, gridlines, jitter o cualquier otra marca.

---

## 4. Preservación semántica

La abreviatura `H100 (ref.)` no altera la semántica científica:

- H100 sigue siendo la quinta condición en el mismo orden categórico;
- sigue correspondiendo a la única referencia congelada de 2 950 series;
- permanece representada por un único diamante por panel;
- no se convierte en una condición replicada;
- el caption mantiene explícitamente `H100 (n=1, referencia congelada)`;
- no se altera la naturaleza descriptiva y no causal de la sensibilidad conjunta tamaño–composición;
- HE5 permanece `INCONCLUSIVE`.

---

## 5. Validación conceptual de legibilidad

Sin regenerar la figura final, la solución seleccionada cumple:

```text
NO_OVERLAP_WITH_H75 = PASS
NO_CLIPPING_EXPECTED = PASS
EFFECTIVE_FONT_SIZE_GE_8PT = PASS (~8.7 pt)
GRAYSCALE_READABILITY = PASS
H100_CATEGORY_POSITION_UNCHANGED = PASS
SEPARATOR_BEFORE_H100_UNCHANGED = PASS
POINTS_AXES_JITTER_GRIDLINES_UNCHANGED = PASS
```

La holgura horizontal calculada de aproximadamente `17.6` unidades SVG es mayor que cero y no requiere ninguna modificación posicional. La cadena abreviada permanece en una sola línea y conserva el mismo estilo tipográfico de H100.

---

## 6. Dictamen terminal

```text
FIG014_EXECUTION = COMPLETE
H100_LABEL_SOLUTION_APPROVED = true
H100_VISIBLE_LABEL = H100 (ref.)
H100_TEXT_FONT_SIZE = mantener (14.5 unidades SVG; ~8.7 pt efectivos)
H100_TEXT_LINE_BREAK = none
H100_TEXT_ANCHOR = mantener (middle / centrado)
H100_TEXT_POSITION_ADJUSTMENT = none
TEXT_ONLY = true
TYPOGRAPHIC_LAYOUT_ONLY = false
SCIENTIFIC_GEOMETRY_CHANGE = false
SCIENTIFIC_DATA_CHANGE = false
DOCX_MODIFIED = false
IMAGE_REGENERATED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Se detiene la ejecución para auditoría externa de la IA Experimental.