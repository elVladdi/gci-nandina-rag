# PROMPT121F — Auditoría externa

## Dictamen

```text
PROMPT121F_EXTERNAL_AUDIT = PASS
A041 = VERIFIED / COMPLETE
A042 = VERIFIED / COMPLETE
A043 = NOT_EXECUTED / DEFERRED_TO_FIGURE_WORKFLOW
INHERITED_TRACE_ROWS = 101
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 103
INHERITED_COMMENT_COUNT = 191
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 193
TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
SEQ_FIGURA_COUNT = 12
FIGURE_6_CHANGED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Identidad auditada

```text
OUTPUT_DOCX = Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575 bytes

OUTPUT_TRACE = g7_thesis_claim_traceability_v0.3_F.csv
SHA256 = 14d44b27012181bc943fa0325eb3c5964295ff040455ffe8c7c2b16f025eb337
SIZE = 93547 bytes
```

Los hashes y tamaños coinciden con la respuesta oficial de PROMPT121F publicada en `writing_prompts_tmp/121F_RESPUESTA_G7_F02_V03_BLOQUE_F_RESULTADOS_4_1_4_TABLAS.md` @ `c3e73e72bcee360e4b5365bc55361d37140ee7c3`.

## Auditoría de trazabilidad

El CSV candidato contiene 103 filas. Las primeras 101 filas son idénticas a la trazabilidad aprobada de entrada. Se añadieron exclusivamente:

- `G7F02-V03F-001` — `A041` — actualización de 4.1.4 y Tabla 14.
- `G7F02-V03F-002` — `A042` — actualización de Tabla 15 e interpretación inmediata.

Ambas filas registran `scientific_recomputation=NO`, `new_inference=NO`, `figure_change=NO` y estado `APPLIED`.

## Auditoría científica y editorial

### A041 / Tabla 14

La presentación activa queda sincronizada con las fuentes congeladas:

- banco histórico: 2 950 series;
- evaluación interna: 1 056 series / 67 DAM / 42 NANDINA;
- Top-1 = 0,5095 = 538/1 056;
- Top-3 = 0,6714 = 709/1 056;
- Top-5 = 0,7633 = 806/1 056;
- Top-10 = 0,8911 = 941/1 056;
- Top-50 = 0,9915 = 1 047/1 056, explícitamente suplementario;
- MRR@100 = 0,6297.

La prosa activa deja claro que nueve series no alcanzaron coincidencia exacta dentro del Top-50 y que los valores describen exclusivamente la recuperación histórica del benchmark interno del Capítulo 87, sin convertirlos en exactitud global del marco RAG, corrección jurídica o validez externa. No se introducen CI por brazo ni valores p.

Los valores y filas legacy permanecen únicamente como material de revisión amarillo + tachado cuando fueron sustituidos; no permanecen como afirmaciones activas.

### A042 / Tabla 15

La presentación activa usa el número de DAM históricas que contienen la subpartida de referencia, no los antiguos buckets por conteo de series:

```text
1 DAM    | 27  | Top-1 0,3704 | Top-3 0,7037 | MRR 0,5644
2 DAM    | 21  | Top-1 0,0476 | Top-3 0,1905 | MRR 0,2394
3–4 DAM  | 425 | Top-1 0,6918 | Top-3 0,7671 | MRR 0,7602
5+ DAM   | 583 | Top-1 0,3997 | Top-3 0,6175 | MRR 0,5517
```

La interpretación es correctamente descriptiva: no afirma gradiente monotónico, no define umbral post hoc de suficiencia, no introduce causalidad ni inferencia poblacional externa y mantiene HE5 como inconclusa.

## Auditoría OOXML y alcance

La comparación con la entrada aprobada confirmó:

- mismo conjunto de 66 entradas ZIP;
- únicamente `word/document.xml` y las partes de comentarios fueron modificadas;
- 24 objetos tabla antes y después;
- 0 elementos `w:del`;
- 193 comentarios totales;
- comentarios heredados 0–441 preservados textualmente;
- nuevos comentarios 442 y 443 correctamente anclados y con los seis encabezados obligatorios en español;
- 12 campos `SEQ Figura`;
- ningún binario `word/media/*` modificado;
- Figuras 4, 5 y 6 sin cambios;
- ninguna modificación visible ni de comentarios fuera del alcance A041/A042.

El texto visible nuevo del bloque no introduce IDs internos o lenguaje de gobernanza prohibido.

## QA visual independiente

Se renderizó independientemente el DOCX candidato y se inspeccionaron las páginas correspondientes al inicio de 4.1.4, Tablas 14–15, interpretaciones, Figura 6 legacy y frontera con 4.1.5. Las tablas son legibles y no presentan clipping, overflow, filas cortadas, duplicación de objetos o superposición. Figura 6 permanece legacy y sin cambios, conforme al bloqueo explícito de A043.

## Continuidad

PROMPT121F queda aprobado. No se autoriza 121G todavía porque A043 / Figura 6 sigue pendiente y el propio contrato de 121F la reserva para un bloque posterior bajo la IA Diseñadora y Auditora de Figuras Científicas.
