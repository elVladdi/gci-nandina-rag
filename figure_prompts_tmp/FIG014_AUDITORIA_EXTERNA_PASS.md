# FIG014 — Auditoría externa de IA Experimental

## Dictamen

```text
FIG014_EXTERNAL_AUDIT = PASS
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
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Verificación independiente

Se auditó la respuesta `figure_prompts_tmp/FIG014_RESPUESTA_RESOLVER_LEGIBILIDAD_H100_FIGURA6_G7_F02.md@e667642115f2fbd27e7052e8cfd43fa8af1a9d95` contra el problema contractual documentado en FIG013 y las invariantes de FIG012.

La alternativa seleccionada `H100 (ref.)` es la intervención mínima compatible con el contrato científico y editorial. Con los valores medidos por el renderer gobernante, la separación entre los centros de H75 y H100 es 66.0 unidades SVG; los anchos son 26.4 para `H75` y 70.4 para `H100 (ref.)`. La suma de semianchos es 48.4, por lo que queda una holgura horizontal positiva de 17.6 unidades SVG sin cambiar tamaño de fuente, anclaje ni posición. El tamaño efectivo permanece aproximadamente en 8.7 pt, por encima del mínimo de 8 pt.

La solución conserva la quinta condición H100 en la misma posición categórica, mantiene el separador y el diamante científico, y no altera ninguna coordenada de puntos, eje, gridline, jitter o panel. La semántica completa permanece disponible en el caption aprobado: `H100 (n=1, referencia congelada)`. Por tanto, la abreviatura visible no convierte H100 en una condición replicada ni debilita su trazabilidad.

La alternativa de reducir `H100 (referencia)` a una sola línea no es preferible porque la reducción necesaria para separación limpia llevaría el tamaño efectivo por debajo del mínimo autorizado. El salto de línea y el reposicionamiento eran viables pero implicaban mayor intervención tipográfica sin beneficio científico adicional.

## Consecuencia de gobernanza

Se autoriza una nueva regeneración técnica determinística de Figura 6 usando `H100 (ref.)` como única modificación respecto del contrato textual resuelto para esa etiqueta. La ejecución corresponde a CODEX. No se autoriza todavía la integración en DOCX, A043 ni 121G. El candidato deberá pasar auditoría externa antes de cualquier integración.
