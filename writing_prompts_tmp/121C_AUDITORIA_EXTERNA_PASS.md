# PROMPT121C — Auditoría externa independiente

```text
PROMPT121C_EXTERNAL_AUDIT = PASS
PROMPT121C_BLOCK_C = APPROVED
SCIENTIFIC_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false
NEXT_BLOCK_121D_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## 1. Artefactos auditados

Se auditó independientemente la ejecución de `PROMPT121C` contra su contrato, la salida binaria, la trazabilidad acumulativa y las fuentes científicas congeladas.

Salida DOCX:

```text
Molleapasa_gv_G7F02_REVIEW_V03_C.docx
SHA256 = 38b2b089a87b973a81be37108a2d303492de8a4a79a3acf99264750c1130deff
SIZE_BYTES = 4193389
```

Trazabilidad:

```text
g7_thesis_claim_traceability_v0.3_C.csv
SHA256 = 1ed85863b6a588ef2ce80cbfa05d105f1792de17fead99d2c634fafa19296c1f
SIZE_BYTES = 71377
TRACE_ROWS = 75
```

La identidad de ambos archivos coincide exactamente con la declarada en la respuesta oficial.

## 2. Integridad acumulativa

La comparación independiente con el Bloque B/R1 confirmó:

```text
INHERITED_TRACE_ROWS = 42
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 33
NEW_TRACE_ID_RANGE = G7F02-V03C-001 .. G7F02-V03C-033
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
```

Las 42 filas heredadas del CSV son idénticas y permanecen en el mismo orden. Las 33 filas nuevas pertenecen exclusivamente a `A026`, `A027`, `A028`, `A029`, `A030`, `A031`, `A032`, `A033`, `A034`, `A076` y `A077`.

## 3. Alcance OOXML

La comparación estructural independiente entre B/R1 y C confirmó que los elementos visibles modificados se encuentran exclusivamente dentro de la sección 3.8. Los elementos corporales anteriores a 3.8 y posteriores al cierre de 3.8 permanecen sin cambios.

```text
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
A076_APPLIED = true
A077_APPLIED = true
```

Las referencias corregidas quedan, al considerar el marcado de revisión:

```text
3.8.1: Tabla 9 -> Tabla 8
3.8.7: Tabla 10 -> Tabla 9
```

No se modificó el Capítulo 4.

## 4. Comentarios y marcado de revisión

La auditoría OOXML independiente confirmó:

```text
FINAL_COMMENT_COUNT = 167
COMMENT_RANGE_START_COUNT = 167
COMMENT_RANGE_END_COUNT = 167
COMMENT_REFERENCE_COUNT = 167
COMMENT_ID_SETS_EQUAL = true
ORPHAN_COMMENT_IDS = NONE
INHERITED_COMMENT_COUNT = 134
INHERITED_COMMENT_TEXT_CHANGED = 0
NEW_COMMENT_COUNT = 33
NEW_COMMENT_IDS = 385..417
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
```

Los 33 comentarios nuevos poseen los seis encabezados obligatorios en español. No existe `w:del`; el texto anterior modificado permanece visible con tachado y amarillo, y el texto nuevo permanece en amarillo sin tachado.

## 5. Auditoría científica

La sección 3.8 resultante es consistente con las fuentes gobernantes congeladas.

### HE2

Se preservan:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM
EVAL = 1056 series / 67 DAM / 42 NANDINA
BOOTSTRAP_REPLICATES = 10000
HE2_A = 15 primary paired contrasts / 99% CI
HE2_B = Recall@200 - Recall@100 / 95% CI
P_VALUES = none
```

La recuperación histórica se compara contra los tres comparadores normativos corregidos y la superioridad observada se restringe al desempeño de recuperación dentro del benchmark interno; no se transforma en exactitud global del framework RAG.

### HE1

La integridad, procedencia, trazabilidad y reproducibilidad se presentan como evidencia metodológica con limitaciones. No se fabrica una disposición terminal para HE1.

### HE3

La integración histórico-normativa se mantiene separada del reordenamiento diagnóstico. La evidencia normativa no modifica el ranking histórico y el LLM reordenador continúa como diagnóstico, no como flujo principal.

### HE4

La redacción separa correctamente los controles estructurales de la evaluación cualitativa. Se explicita que la evaluación cualitativa fue realizada por una IA independiente bajo rol experto, sin puntuación humana, y se preservan las limitaciones del esquema y de la modalidad del evaluador. La auditabilidad no se interpreta como corrección jurídica.

### HE5 y sensibilidades

Se preservan las fronteras aprobadas:

```text
HE5 = INCONCLUSIVE
DESCRIPTION_QUALITY = NOT_ESTIMABLE
HIERARCHICAL_PROXIMITY = DESCRIPTIVE_ONLY
HISTORICAL_PRECEDENTS = DESCRIPTIVE_ONLY / NO_POSTHOC_INSUFFICIENCY_THRESHOLD
INTERNAL_VALIDITY = DOCUMENTED_LIMITATION
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
```

### Disposiciones

La lectura final queda correctamente diferenciada:

```text
HG  = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
```

No se deriva retrospectivamente un dictamen agregado para HG.

## 6. QA visual independiente

El DOCX C fue renderizado independientemente con el renderer canónico de auditoría.

```text
RENDER_PAGE_COUNT = 136
PAGES_INSPECTED = 80-97
TABLE_8_VISUAL = PASS
TABLE_9_VISUAL = PASS
CLIPPING = NONE_OBSERVED
OVERFLOW = NONE_OBSERVED
BROKEN_TABLES = NONE_OBSERVED
UNEXPECTED_BLANK_PAGES = NONE_OBSERVED
BOUNDARY_BEFORE_3_8 = PASS
BOUNDARY_AFTER_3_8 = PASS
```

El conteo de 136 páginas coincide con la renderización declarada por el ejecutor. El marcado amarillo/tachado es visible y las tablas 8 y 9 permanecen legibles.

## 7. Dictamen

No se identificó deriva científica, modificación fuera de alcance, pérdida de comentarios heredados, ruptura de tablas, inferencia nueva, valor p nuevo, intervalo nuevo, generalización externa ni reapertura de EXP12.

```text
PROMPT121C_EXTERNAL_AUDIT = PASS
PROMPT121C_BLOCK_C = APPROVED
SCIENTIFIC_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false
NEXT_BLOCK_121D_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

La aprobación de este bloque no aprueba todavía G7-F02 ni autoriza G7-F03.