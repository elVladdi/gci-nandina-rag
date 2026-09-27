# PROMPT121E-FIG45-R1 — Corrección localizada del contrato de integración de Figuras 4 y 5

## 0. Actor

Actúa como **IA de Redacción Científica**.

No eres CODEX. No eres la IA Experimental. No regeneres figuras, no recalcules datos y no ejecutes 121F.

La auditoría externa de `121E-FIG45` concluyó:

```text
PROMPT121E_FIG45_EXTERNAL_AUDIT = REVISION_REQUIRED
FULL_RERUN_REQUIRED = false
TARGETED_REVISION_REQUIRED = true
SCIENTIFIC_DATA_CORRECTION_REQUIRED = false
FIGURE_BINARY_CORRECTION_REQUIRED = false
121F_AUTHORIZED = false
```

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/121E_FIG45_INTEGRAR_FIGURAS_4_5_REVIEW_V03.md
writing_prompts_tmp/121E_FIG45_AUDITORIA_EXTERNA_REVISION_REQUIRED.md
```

## 1. Entradas exactas de R1

Trabaja exclusivamente sobre los binarios auditados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E_FIG45.docx
SHA256 = e77e20a496b4075c14645005126637dfd0d8ed13201f52583b103d4147ed4897
SIZE = 4569156

g7_thesis_claim_traceability_v0.3_E_FIG45.csv
SHA256 = 9b8b81f0856bc1e23a861af1eda0c547eebc00ecbe49aed91ff8dee4e34db673
SIZE = 89000
ROWS = 101
```

Si alguno no coincide exactamente, STOP.

No regreses a E para reconstruir la integración. Esta es una corrección localizada de E_FIG45.

## 2. Alcance único

Corrige exclusivamente:

1. las dos líneas temporales de revisión de Figuras 4 y 5;
2. el caption propuesto de Figura 4;
3. el caption propuesto de Figura 5;
4. el texto de los comentarios 440 y 441;
5. las dos filas nuevas de trazabilidad;
6. la respuesta oficial y sus hashes/tamaños.

Todo lo demás queda congelado.

Está prohibido:

- sustituir o regenerar los PNG;
- cambiar las figuras legacy;
- modificar los captions legacy ya marcados;
- crear nuevos comentarios;
- cambiar IDs de comentarios;
- añadir filas adicionales al CSV;
- modificar cualquiera de las 99 filas heredadas;
- modificar tablas, 4.1.3 fuera de esos elementos, 4.1.4, Tabla 14, Figura 6 o cualquier otra sección;
- crear nuevos campos `SEQ Figura`;
- ejecutar 121F.

## 3. Corrección R1-01 — línea temporal exacta

En los dos bloques sustituye el texto actual:

```text
Propuesta de actualización de Figura 4 para revisión editorial de tesis (sin cambio de datos).
Propuesta de actualización de Figura 5 para revisión editorial de tesis (sin cambio de datos).
```

por **exactamente la misma línea para ambas figuras**:

```text
PROPUESTA DE REEMPLAZO DEL ELEMENTO GRÁFICO ANTERIOR — NO ES NUMERACIÓN FINAL
```

La línea debe quedar:

- resaltada en amarillo;
- sin tachado;
- estilo normal/no-caption;
- inmediatamente antes del PNG propuesto correspondiente.

## 4. Corrección R1-02 — caption propuesto Figura 4

Sustituye únicamente el caption propuesto corto actual por el texto **exacto e íntegro** definido en el apartado 5 de:

```text
writing_prompts_tmp/121E_FIG45_INTEGRAR_FIGURAS_4_5_REVIEW_V03.md
```

Debe comenzar exactamente con:

```text
Figura 4. Evidencia primaria de HE2: ordenamiento temprano y cobertura profunda en la evaluación interna realizada fuera de línea del Capítulo 87 (1 056 series, 67 DAM y 42 subpartidas NANDINA).
```

y conservar íntegramente el resto del caption obligatorio de ese apartado, incluidos:

- paneles A/B/C;
- cinco métricas y tres comparadores;
- ausencia de IC por brazo;
- 15 diferencias pareadas con IC del 99 %;
- `Recall@200 − Recall@100` con IC del 95 %;
- ausencia de valores p;
- carácter no causal;
- límite a la evaluación interna;
- prohibición de interpretarlo como exactitud global del RAG, corrección jurídica o validez externa.

Todo el caption propuesto debe quedar amarillo, no tachado y sin crear `SEQ Figura` adicional.

## 5. Corrección R1-03 — caption propuesto Figura 5

Sustituye únicamente el caption propuesto corto actual por el texto **exacto e íntegro** definido en el apartado 6 de:

```text
writing_prompts_tmp/121E_FIG45_INTEGRAR_FIGURAS_4_5_REVIEW_V03.md
```

Debe comenzar exactamente con:

```text
Figura 5. Cobertura exacta NANDINA según profundidad y variante en la evaluación interna realizada fuera de línea del Capítulo 87 (1 056 series, 67 DAM y 42 subpartidas NANDINA).
```

y conservar íntegramente:

- cinco variantes × tres profundidades;
- cuatro variantes descriptivas predefinidas;
- 70/30 solo como contexto descriptivo adicional;
- ausencia de IC, valores p, tendencias ajustadas e inferencia entre variantes;
- unión diagnóstica fuera del rendimiento ordinario;
- ausencia de orden de favorabilidad;
- ausencia de modificación de la evidencia confirmatoria/disposición HE2.

Todo el caption propuesto debe quedar amarillo, no tachado y sin `SEQ Figura` adicional.

## 6. Corrección R1-04 — comentario 440

No crees un tercer comentario. **Conserva ID 440 y su ancla actual**, pero reemplaza su texto para que contenga exactamente los seis encabezados:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Además del contenido ya válido, debe declarar explícitamente:

- legacy conservada para revisión;
- propuesta basada en el PNG aprobado sin recalcular datos;
- 15 contrastes pareados con IC del 99 %;
- un contraste profundo `Recall@200 − Recall@100` con IC del 95 %;
- ausencia de valores p;
- ausencia de IC por brazo;
- no representa exactitud global del RAG;
- no representa corrección jurídica.

## 7. Corrección R1-05 — comentario 441

Conserva ID 441 y su ancla actual. Reemplaza su texto manteniendo exactamente los mismos seis encabezados.

Debe declarar explícitamente:

- legacy conservada para revisión;
- propuesta basada en el PNG aprobado;
- cinco variantes × tres profundidades y 15 valores descriptivos;
- sin inferencia, IC, valores p ni ranking de favorabilidad;
- la variante 70/30 es solo contexto descriptivo adicional;
- la unión diagnóstica no representa rendimiento ordinario.

## 8. Corrección R1-06 — dos filas de trazabilidad

El CSV debe seguir teniendo exactamente 101 filas de datos:

```text
INHERITED_ROWS = 99
FIG45_ROWS = 2
TOTAL_ROWS = 101
```

Las 99 heredadas deben permanecer byte-lógicamente iguales.

Modifica solo las dos filas finales existentes:

### Figura 4

```text
trace_id = G7F02-V03E-FIG45-001
plan_id = A039
change_type = FIGURE_UPDATE
```

### Figura 5

```text
trace_id = G7F02-V03E-FIG45-002
plan_id = A040
change_type = FIGURE_UPDATE
```

Actualiza `review_v03_text_or_value` para reflejar el caption completo efectivamente insertado.

Preserva los blobs de imagen:

```text
Figura 4 = eb77a4f2289a8701d22ba399d9432defd2092e2a
Figura 5 = d63559e4da4b391d47968a60a41649c715d5408b
```

No cambies ningún otro campo salvo donde sea estrictamente necesario para que la fila describa fielmente el resultado R1.

## 9. Invariantes obligatorios después de R1

```text
TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
TOTAL_COMMENT_COUNT = 191
NEW_COMMENT_IDS = NONE
COMMENT_440_ANCHORED = true
COMMENT_441_ANCHORED = true
ALL_COMMENT_IDS_ANCHORED = true
SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
FIGURE_4_APPROVED_PNG_SHA256 = 5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e
FIGURE_5_APPROVED_PNG_SHA256 = aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

Los PNG aprobados deben permanecer byte-idénticos dentro del DOCX.

## 10. QA visual

Renderiza el Word R1 e inspecciona nuevamente:

- página anterior a Figura 4;
- Figura 4 legacy;
- línea temporal + propuesta Figura 4 + caption completo;
- Figura 5 legacy;
- línea temporal + propuesta Figura 5 + caption completo;
- inicio de 4.1.4 y Tabla 14.

Los captions completos pueden aumentar el número de páginas. Eso está permitido si no altera márgenes/secciones ni produce clipping, overlap o separación editorial inaceptable.

## 11. Salidas R1

No sobrescribas el candidato auditado. Genera:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E_FIG45_R1.docx
g7_thesis_claim_traceability_v0.3_E_FIG45_R1.csv
```

Publica/actualiza la respuesta oficial como:

```text
writing_prompts_tmp/121E_FIG45_R1_RESPUESTA_CORREGIR_CONTRATO_INTEGRACION_FIGURAS_4_5.md
```

La respuesta debe calcular los hashes **después de cerrar definitivamente los dos archivos** y reportar:

```text
PROMPT121E_FIG45_R1_EXECUTION = COMPLETE | STOPPED_PRECONDITION
TEMPORARY_LABELS_EXACT = true|false
TEMPORARY_LABELS_YELLOW = true|false
FIGURE_4_FULL_CAPTION_EXACT = true|false
FIGURE_5_FULL_CAPTION_EXACT = true|false
COMMENT_440_COMPLETED = true|false
COMMENT_441_COMPLETED = true|false
TRACE_PLAN_IDS = A039 / A040 | <detalle>
TRACE_CHANGE_TYPE = FIGURE_UPDATE | <detalle>
INHERITED_TRACE_ROWS_CHANGED = 0|<n>
TOTAL_TRACE_ROWS = 101|<n>
TOTAL_COMMENT_COUNT = 191|<n>
NEW_COMMENT_IDS = 0|<n>
TRACKED_DELETION_COUNT = 0|<n>
ALL_COMMENT_IDS_ANCHORED = true|false
NEW_SEQ_FIGURE_FIELDS = 0|<n>
FIGURE_BINARIES_UNCHANGED = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0|<n>
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0|<n>
LOCAL_VISUAL_REVIEW = PASS|FAIL
121F_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Incluye SHA-256 y tamaño exactos del DOCX y CSV R1. Detente para auditoría externa.