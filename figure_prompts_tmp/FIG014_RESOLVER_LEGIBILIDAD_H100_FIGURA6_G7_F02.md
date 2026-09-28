# FIG014 — Resolver legibilidad de etiqueta H100 en Figura 6 / G7-F02

## 0. Actor y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No eres la IA de Redacción Científica.

Ejecuta exclusivamente un microdictamen científico-editorial para resolver el bloqueo de legibilidad detectado en FIG013 sobre la etiqueta de condición H100 de la futura Figura 6.

No modifiques el DOCX. No regeneres SVG/PNG. No modifiques scripts. No ejecutes A043 ni 121G.

## 1. Estado gobernante

Lee íntegramente:

```text
figure_prompts_tmp/FIG012_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md
@ be0879c44b9d933bc0591bcf498b5e056cc31b20

figure_prompts_tmp/FIG012_AUDITORIA_EXTERNA_PASS.md
@ 547e1dbfc34a03b9c569cf4d8c1792c88f94901b

figure_prompts_tmp/FIG013_REGENERAR_FIGURA6_TESIS_G7_F02.md
@ 2e7a55900b6db32ba6711880e17a3f17ab82dee6

figure_prompts_tmp/FIG013_RESPUESTA_REGENERAR_FIGURA6_TESIS_G7_F02.md

figure_prompts_tmp/FIG013_AUDITORIA_EXTERNA_STOP_COMPLIANT.md
```

Estado vinculante:

```text
FIG013_EXTERNAL_AUDIT = PASS_STOPPED_PRECONDITION
FIG013_STOP_COMPLIANT = true
FIGURE_6_CANDIDATE_CREATED = false
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
A043_EXECUTED = false
121G_AUTHORIZED = false
```

## 2. Problema único a resolver

FIG012 aprobó naturalizar:

```text
H100 ref. -> H100 (referencia)
```

FIG013 demostró que esa cadena, manteniendo exactamente la tipografía, posición y anclaje originales, se solapa materialmente con `H75` en los seis paneles.

El prompt FIG013 no autorizaba ajustar tipografía/posición de etiquetas categóricas; por ello CODEX se detuvo correctamente.

Debes decidir la **solución editorial mínima** que preserve legibilidad y trazabilidad científica.

## 3. Invariantes científicos

No pueden cambiar:

- cinco condiciones y su orden: `H25 | H50-D1 | H50-D2 | H75 | H100`;
- semántica de H100 como única referencia congelada de 2 950 series;
- 31 corridas observadas;
- seis paneles;
- datos, puntos, jitter, ejes, gridlines, separador y escala `[0,1]`;
- posición científica de todas las marcas;
- interpretación descriptiva/no causal de la sensibilidad conjunta tamaño–composición;
- HE5 = INCONCLUSIVE.

La decisión puede afectar **únicamente el nodo de texto de la etiqueta H100** y, si fuera indispensable, su presentación tipográfica. No debe mover ninguna marca científica ni ninguna otra categoría.

## 4. Alternativas que debes auditar

Evalúa como mínimo:

1. `H100 (referencia)` con reducción local de fuente, siempre que el tamaño efectivo final sea >= 8 pt y siga siendo claramente legible.
2. `H100 (referencia)` con salto de línea exclusivamente dentro de ese rótulo.
3. `H100 (ref.)` como abreviatura editorial, siempre que el caption explique inequívocamente que H100 es la referencia congelada única.
4. Reposicionamiento/anclaje exclusivamente del nodo textual H100, sin desplazar categoría, separador, eje ni punto H100.
5. Combinaciones mínimas de las anteriores si una sola no resuelve el problema.

No elijas por conveniencia técnica. Prioriza naturalidad académica, legibilidad, consistencia con la tesis y mínima intervención.

## 5. Dictamen obligatorio

Debes producir una única solución recomendada y fijar exactamente:

```text
H100_VISIBLE_LABEL = <cadena final exacta>
H100_TEXT_FONT_SIZE = <mantener|nuevo valor>
H100_TEXT_LINE_BREAK = <none|detalle>
H100_TEXT_ANCHOR = <mantener|detalle>
H100_TEXT_POSITION_ADJUSTMENT = <none|detalle exacto>
```

Clasifica la solución:

```text
TEXT_ONLY = true|false
TYPOGRAPHIC_LAYOUT_ONLY = true|false
SCIENTIFIC_GEOMETRY_CHANGE = false
SCIENTIFIC_DATA_CHANGE = false
```

Debes justificar por qué la solución no altera la semántica científica ni confunde H100 con una condición replicada.

El caption aprobado en FIG012 puede conservar la forma completa `H100 (n=1, referencia congelada)` aunque el rótulo visual use una abreviatura.

## 6. Validación conceptual de legibilidad

Sin regenerar la figura final, verifica que la solución propuesta sea compatible con:

- ausencia de solapamiento con H75;
- ausencia de clipping;
- tamaño efectivo >= 8 pt;
- lectura en escala de grises;
- misma posición categórica H100;
- mismo separador antes de H100;
- ninguna modificación de puntos/ejes/jitter/gridlines.

Si ninguna solución cumple simultáneamente, reporta `STOPPED_NO_SAFE_TEXT_SOLUTION` y explica el bloqueo.

## 7. Salida

Publica exclusivamente:

```text
figure_prompts_tmp/FIG014_RESPUESTA_RESOLVER_LEGIBILIDAD_H100_FIGURA6_G7_F02.md
```

en `codex/prompts-temporary`.

Termina con:

```text
FIG014_EXECUTION = COMPLETE | STOPPED_NO_SAFE_TEXT_SOLUTION
H100_LABEL_SOLUTION_APPROVED = true|false
H100_VISIBLE_LABEL = <valor>
TEXT_ONLY = true|false
TYPOGRAPHIC_LAYOUT_ONLY = true|false
SCIENTIFIC_GEOMETRY_CHANGE = false
SCIENTIFIC_DATA_CHANGE = false
DOCX_MODIFIED = false
IMAGE_REGENERATED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa de la IA Experimental.
