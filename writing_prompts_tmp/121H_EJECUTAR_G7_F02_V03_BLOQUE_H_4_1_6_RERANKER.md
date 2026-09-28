# PROMPT121H — Ejecutar G7-F02 REVIEW V03 — Bloque H: 4.1.6 reordenamiento diagnóstico con LLM

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No regeneres figuras, no recalcules métricas y no ejecutes 4.1.7 ni ningún bloque posterior.

Esta ejecución queda autorizada exclusivamente después del PASS externo de 121G:

```text
PROMPT121G_EXTERNAL_AUDIT = PASS
A044_EXTERNAL_AUDIT = PASS
A045_EXTERNAL_AUDIT = PASS
121H_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría gobernante:

```text
writing_prompts_tmp/121G_AUDITORIA_EXTERNA_PASS.md
@ fa72963afd28acb15cb0f7c3141c40a00fc0c2ac
```

Lee íntegramente además:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md

docs/writing/group7/g7_writing_source_freeze_v0.1.md
blob feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430

docs/writing/group7/g7_writing_source_freeze_v0.1.json
blob 776fcb52e8ada9967504001b897c75b4108bfb63
```

Ejecuta exclusivamente **A046 y A047** del plan aprobado.

---

## 1. Entradas acumulativas exactas

Trabaja exclusivamente sobre los artefactos G aprobados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_G.docx
SHA256 = aaa5dbd7f65b9db13c75b82fb7bcbbd75373fb67e4c3b683de0c7181ec13eeaf
SIZE = 4664480

g7_thesis_claim_traceability_v0.3_G.csv
SHA256 = 9b65ddc4773996c272a6d3809bcae8b3321058db123d16dee56be3985b171857
SIZE = 97500
ROWS = 106
```

Verifica ambos hashes antes de editar. Si alguno no coincide, `STOPPED_PRECONDITION`.

No reconstruyas G desde versiones previas. No modifiques A044/A045 ya aprobados.

---

## 2. Fuentes científicas gobernantes para A046

Lee íntegramente y verifica sus blobs congelados:

```text
outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_metrics_v0.2.json
GIT_BLOB = 15800df93cf77f4f2c6e83ac6cb692be013bbeb3

outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/summary.md
GIT_BLOB = 2e356497695551c9df61fb36e70d0cd6d2003daa

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
GIT_BLOB = 129a67b15db429b86af059d61753b1942c8f243f
```

Estado científico vinculante:

```text
SCOPE = DIAGNOSTIC SAMPLE ONLY
SAMPLE_CASES = 20
REFERENCE_IN_POOL = 19
REFERENCE_NOT_IN_POOL = 1

TOP1_BEFORE = 0.5000
TOP1_AFTER = 0.5000
DELTA_TOP1 = 0.0000

TOP3_BEFORE = 0.6500
TOP3_AFTER = 0.6500
DELTA_TOP3 = 0.0000

TOP5_BEFORE = 0.8000
TOP5_AFTER = 0.8000
DELTA_TOP5 = 0.0000

MRR_BEFORE = 0.632638888888889
MRR_AFTER = 0.632638888888889
DELTA_MRR = 0.0000

DELTA_RR_POSITIVE = 0
DELTA_RR_ZERO = 19
DELTA_RR_NEGATIVE = 0

PAIRED_INFERENCE = NOT_RUN
PRE_SPECIFIED_INFERENTIAL_TEST = NONE
HE3 = SUPPORTED
```

Interpretación obligatoria:

- el reordenador LLM es **diagnóstico**, no forma parte del flujo principal;
- las métricas agregadas Top-1, Top-3, Top-5 y MRR no cambiaron en la muestra observada;
- entre los 19 casos con referencia presente en el pool, no hubo cambios positivos ni negativos del rango recíproco;
- un caso tuvo la referencia fuera del pool y no debe convertirse en evidencia de mejora o degradación del reordenador;
- no se ejecutó una prueba inferencial pareada preespecificada;
- no generalices el comportamiento del reordenador fuera de la muestra diagnóstica observada;
- no describas invariancia diagnóstica como demostración de que un LLM nunca puede mejorar un ranking;
- no atribuyas al LLM el ranking principal del piloto.

No introduzcas valores p, intervalos de confianza, causalidad ni inferencia de superpoblación.

---

# 3. A046 — 4.1.6 y Tabla 17

## 3.1 Alcance

Modifica únicamente:

- la prosa de **4.1.6. Resultados del reordenamiento diagnóstico con LLM** que haya quedado desactualizada;
- el objeto existente **Tabla 17**;
- su nota inmediata y la interpretación inmediata necesaria para evitar contradicciones.

No modifiques:

- 4.1.5, Tabla 16 ni Figura 7;
- 4.1.7;
- Tabla 18;
- Figura 9;
- ninguna sección anterior o posterior;
- numeración de tablas o figuras;
- Lista de Tablas o Lista de Figuras en esta ejecución.

## 3.2 Corrección de prosa

Elimina de la presentación activa los valores legacy:

```text
Top-1 0.2500 -> 0.2000
Top-3 0.4500 -> 0.4500
Top-5 0.5000 -> 0.4500
Top-10 0.5000 -> 0.5000
MRR 0.3542 -> 0.3083
4 casos perdidos
16 sin cambio
13 rankings incompletos
```

Conserva el texto anterior visible cuando sea sustituido: **amarillo + tachado**, sin `w:del`.

La nueva prosa debe expresar, en español natural y sin IDs internos visibles, que:

1. la prueba fue diagnóstica y comprendió 20 casos;
2. la referencia estuvo dentro del pool en 19 casos y fuera del pool en 1;
3. Top-1 permaneció 0,5000 antes/después;
4. Top-3 permaneció 0,6500 antes/después;
5. Top-5 permaneció 0,8000 antes/después;
6. MRR permaneció aproximadamente 0,6326 antes/después;
7. entre los 19 casos con referencia en el pool, la variación del rango recíproco fue 0 positiva, 19 cero y 0 negativa;
8. no hubo prueba inferencial preespecificada;
9. el resultado se limita a la muestra diagnóstica observada y no se usa para reordenar el flujo principal.

No uses `EXP-04`, `Fase G`, `HE3-G`, `Group1`, nombres de archivos, blobs, commits, prompts ni estados de gate en la prosa visible.

## 3.3 Tabla 17 — actualizar el mismo objeto

Mantén el mismo objeto Tabla 17 y su numeración. No crees una nueva tabla.

Conserva cuatro columnas y las nueve filas de datos existentes, actualizando el contenido en el mismo objeto. No sustituyas la tabla completa.

Presentación activa mínima requerida:

| Indicador | Original / entrada | LLM / salida | Cambio o lectura |
|---|---:|---:|---|
| Casos evaluados | 20 | 20 | Muestra diagnóstica |
| Referencia presente en el pool | 19 | 19 | 1 caso con referencia fuera del pool |
| Top-1 | 0,5000 | 0,5000 | 0,0000 |
| Top-3 | 0,6500 | 0,6500 | 0,0000 |
| Top-5 | 0,8000 | 0,8000 | 0,0000 |
| MRR | 0,6326 | 0,6326 | 0,0000 |
| Casos con variación positiva del rango recíproco | — | 0 | Ninguno |
| Casos sin variación del rango recíproco | — | 19 | Entre casos con referencia en el pool |
| Casos con variación negativa del rango recíproco | — | 0 | Ninguno |

Puedes ajustar únicamente redacción menor de encabezados/celdas para conservar el estilo nativo del documento, sin cambiar los números ni su significado.

Para cada celda realmente modificada:

- texto anterior visible = amarillo + tachado;
- texto nuevo = amarillo y no tachado;
- contenido no afectado = formato normal.

No mantengas como presentación activa `Top-10`, `casos ganados/perdidos`, `rankings incompletos` ni otras cifras legacy que no correspondan al estado gobernante actual.

La nota debe aclarar que:

- la muestra es diagnóstica de 20 casos;
- 19 casos tuvieron referencia en el pool y 1 no;
- no se ejecutó prueba inferencial preespecificada;
- ausencia de cambio observado no implica generalización sobre el comportamiento del LLM fuera de la muestra.

---

# 4. A047 — Figura 8: supresión propuesta sin eliminación física

La Figura 8 legacy queda superseded porque representa la degradación de un estado diagnóstico anterior que contradice las métricas gobernantes actuales. El resultado vigente se comunica mejor mediante Tabla 17 + síntesis textual.

En esta REVIEW V03:

1. **no elimines físicamente la Figura 8**;
2. conserva su número oficial `Figura 8` y su campo `SEQ Figura` existente;
3. conserva la imagen legacy byte-idéntica;
4. marca el caption/leyenda legacy que queda superseded con **amarillo + tachado**;
5. inmediatamente después de la figura/caption inserta una línea temporal de revisión, con estilo normal/no-caption y resaltado amarillo:

```text
PROPUESTA DE SUPRESIÓN DEL ELEMENTO GRÁFICO ANTERIOR — SE CONSERVA PARA REVISIÓN / NO ES NUMERACIÓN FINAL
```

6. no insertes imagen de reemplazo;
7. no crees un segundo `SEQ Figura`;
8. no renumeres Figuras 9–12;
9. no modifiques la Lista de Figuras;
10. no modifiques 4.1.7.

La razón visible de supresión no debe contener IDs internos. El detalle técnico queda en comentario/trazabilidad, no en el cuerpo visible.

---

# 5. Comentarios Word

Añade **exactamente 2 comentarios nuevos**:

```text
A046 = comentario sobre corrección de 4.1.6 / Tabla 17
A047 = comentario sobre supresión propuesta de Figura 8
```

No modifiques los 196 comentarios heredados.

Usa los siguientes IDs nuevos, salvo que la verificación estructural demuestre que ya están ocupados:

```text
A046 -> comment_id 447
A047 -> comment_id 448
```

Cada comentario debe estar íntegramente en español y contener exactamente estos seis apartados:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

### A046 — contenido mínimo

Debe explicar:

- muestra diagnóstica de 20 casos;
- 19 con referencia en pool y 1 fuera;
- Top-1, Top-3, Top-5 y MRR sin cambio antes/después;
- 0/19/0 variaciones positiva/cero/negativa del rango recíproco entre casos con referencia;
- ausencia de prueba inferencial preespecificada;
- carácter diagnóstico y no generalizable.

### A047 — contenido mínimo

Debe explicar:

- Figura 8 legacy preservada físicamente;
- supresión únicamente propuesta en REVIEW V03;
- obsolescencia respecto del estado diagnóstico vigente;
- evidencia vigente concentrada en Tabla 17 y prosa;
- numeración 1–12 preservada hasta aceptación del autor;
- ninguna nueva figura ni nueva evidencia creada.

Paths, blobs y hashes pueden aparecer en comentarios para trazabilidad, pero no en el texto visible de tesis.

---

# 6. Trazabilidad

Conserva **byte-idénticas las 106 filas heredadas** y añade exactamente dos filas:

```text
A046 = 4.1.6 / Tabla 17
A047 = Figura 8
```

Resultado esperado:

```text
INHERITED_TRACE_ROWS = 106
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 108
```

Para A046 registra al menos:

```text
change_type = TABLE_STRUCTURE_UPDATE / PARAGRAPH_UPDATE_MINIMAL
presentation_mode = EXISTING_TABLE_ROW_UPDATE
sample_cases = 20
reference_in_pool = 19
reference_not_in_pool = 1
top1_before_after = 0.5000/0.5000
top3_before_after = 0.6500/0.6500
top5_before_after = 0.8000/0.8000
mrr_before_after = 0.6326/0.6326
delta_rr_distribution = positive:0 / zero:19 / negative:0
paired_inference = NOT_RUN
scientific_data_change = NO
new_inference = NO
internal_ids_visible = NO
status = APPLIED
```

Para A047 registra al menos:

```text
change_type = FIGURE_SUPPRESSION_PROPOSED
legacy_figure_preserved = YES
legacy_caption_visible = YES
legacy_caption_yellow_strikethrough = YES
replacement_image_inserted = NO
second_seq_figure_created = NO
figure_number_preserved = 8
scientific_data_change = NO
status = APPLIED
```

---

# 7. Validaciones estructurales obligatorias

Antes de entregar verifica:

```text
BASELINE_TABLE_OBJECT_COUNT = 24
FINAL_TABLE_OBJECT_COUNT = 24
TABLE_17_OBJECT_PRESERVED = true
TABLES_1_TO_16_UNCHANGED = true
TABLES_18_TO_24_UNCHANGED = true

INHERITED_COMMENT_COUNT = 196
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 198
ALL_COMMENT_IDS_ANCHORED = true

INHERITED_TRACE_ROWS = 106
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 108

TRACKED_DELETION_COUNT = 0
SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
FIGURE_7_UNCHANGED = true
FIGURE_8_LEGACY_PHYSICALLY_PRESERVED = true
FIGURE_8_MEDIA_BINARY_UNCHANGED = true
FIGURE_9_TO_12_UNCHANGED = true
NEW_MEDIA_FILES = 0

OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

Busca en todo texto visible nuevo atribuible a esta ejecución y exige cero apariciones de:

```text
EXP-04
Fase G
HE3-G
Group1
G3
G4
G5
G6
G7
A046
A047
Prompt
source freeze
gate
commit
blob
reranker_metrics_v0.2.json
```

Los términos científicos visibles `Top-1`, `Top-3`, `Top-5`, `MRR`, `NANDINA`, `BM25`, `LLM` pueden mantenerse cuando correspondan.

---

# 8. QA visual localizado

Renderiza el DOCX resultante e inspecciona las páginas que cubran:

- final de Figura 7 / inicio de 4.1.6;
- prosa corregida de 4.1.6;
- Tabla 17 completa y su nota;
- Figura 8 legacy y su caption marcado;
- línea temporal de supresión propuesta;
- inicio de 4.1.7 como frontera posterior.

Verifica:

- ningún clipping ni solapamiento;
- Tabla 17 legible y sin filas/celdas desbordadas;
- cambios antiguos/nuevos distinguibles;
- Figura 8 físicamente visible y no deformada;
- caption legacy de Figura 8 visible con amarillo+tachado;
- línea de supresión propuesta visible;
- ninguna segunda numeración de Figura 8;
- continuidad razonable hacia 4.1.7;
- 4.1.7 intacta.

Si el layout materialmente falla, `STOPPED_PRECONDITION`; no cambies márgenes, secciones, tamaño de página ni estilos globales para hacerlo caber.

---

# 9. Salidas

No sobrescribas G. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_H.docx
g7_thesis_claim_traceability_v0.3_H.csv
```

Publica una respuesta oficial en:

```text
writing_prompts_tmp/121H_RESPUESTA_G7_F02_V03_BLOQUE_H_4_1_6_RERANKER.md
```

La respuesta debe incluir hashes SHA-256 y tamaños de ambas salidas y el siguiente resumen verificable:

```text
PROMPT121H_EXECUTION = COMPLETE
A046_APPLIED = true
A047_APPLIED = true
TABLE_17_UPDATED_IN_PLACE = true
FIGURE_8_LEGACY_PRESERVED = true
FIGURE_8_SUPPRESSION_PROPOSED = true
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
INHERITED_TRACE_ROWS = 106
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 108
INHERITED_COMMENT_COUNT = 196
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 198
ALL_COMMENT_IDS_ANCHORED = true
TRACKED_DELETION_COUNT = 0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS
121I_EXECUTED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 4.1.7, 121I ni ningún bloque posterior.