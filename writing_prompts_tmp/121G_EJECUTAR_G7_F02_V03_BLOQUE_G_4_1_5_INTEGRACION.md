# PROMPT121G — Ejecutar G7-F02 REVIEW V03 — Bloque G: 4.1.5 integración histórica–normativa

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No regeneres figuras, no recalcules métricas y no ejecutes 4.1.6 ni ningún bloque posterior.

Esta ejecución está autorizada exclusivamente después del PASS externo de A043:

```text
PROMPT121F_FIG6_R3_EXTERNAL_AUDIT = PASS
A043_EXTERNAL_AUDIT = PASS
121G_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/121F_FIG6_R3_AUDITORIA_EXTERNA_PASS.md
@ c9db87b41fb8a65dd636a1e6feeb4e64c0613809

writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md

docs/writing/group7/g7_writing_source_freeze_v0.1.md
blob feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430

docs/writing/group7/g7_writing_source_freeze_v0.1.json
blob 776fcb52e8ada9967504001b897c75b4108bfb63
```

Ejecuta exclusivamente **A044 y A045** del plan aprobado.

---

## 1. Entradas acumulativas exactas

Trabaja exclusivamente sobre los artefactos R3 aprobados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F_FIG6_R3.docx
SHA256 = 817b7614026f0ec470db06e268906686de2d859ebe2a6ac9372af5d14ac91902
SIZE = 4661445

g7_thesis_claim_traceability_v0.3_F_FIG6_R3.csv
SHA256 = 8d2b7f801f438b32cf32398df96d9df3d2077d532dbce0dad45e222eb99ed7b3
SIZE = 94876
ROWS = 104
```

Verifica ambos hashes antes de editar. Si alguno no coincide, `STOPPED_PRECONDITION`.

No reconstruyas R3 desde F. No reutilices resultados de los intentos con timeout de Figura 6.

---

## 2. Fuentes científicas gobernantes para A044

Lee íntegramente y verifica sus blobs congelados:

```text
outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_ranking_invariance.json
GIT_BLOB = b295b399d80eee5fb21d1fd582cccae9afef4bdd

outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_traceability.json
GIT_BLOB = 4fbe3128ce8f453d9ae47eff6f76106b97b1ceea

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
GIT_BLOB = 129a67b15db429b86af059d61753b1942c8f243f
```

Estado científico vinculante:

```text
EVAL = 1056 series / 67 DAM / 42 NANDINA
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION WHEN_APPLICABLE

RANKING_INVARIANCE = 1056 / 1056 = 1.0
TOP1_UNCHANGED = true
TOP3_UNCHANGED = true
POSITIONS_UNCHANGED = true
HISTORICAL_SCORES_UNCHANGED = true
NO_NEW_CANDIDATE_INSERTED = true
NO_CANDIDATE_REMOVED = true
NORMATIVE_SCORE_AFFECTS_ORDER = false

TRACEABILITY_COMPLETE = 3168 / 3168 = 1.0
PRECEDENT_COUNT_PER_CANDIDATE = 1 for 3168/3168
NORMATIVE_DOCUMENT_COUNT_PER_CANDIDATE = 1 for 3168/3168

HE3 = SUPPORTED
```

Interpretación obligatoria:

- la recuperación histórica genera y ordena los candidatos;
- la evidencia normativa se asocia después y **no reordena**;
- el Top-3 queda fijo;
- la trazabilidad completa significa que cada una de las 3,168 posiciones candidato-caso tiene precedente histórico y documento normativo identificable bajo el protocolo ejecutado;
- esto no equivale a exactitud global del RAG, corrección jurídica, suficiencia normativa ni validez externa;
- no conviertas la trazabilidad en una afirmación de que la evidencia es jurídicamente suficiente;
- no atribuyas al LLM el ranking principal.

No introduzcas nuevos valores p, IC, inferencia causal ni generalización externa.

---

# 3. A044 — 4.1.5 y Tabla 16

## 3.1 Alcance

Modifica únicamente:

- la prosa de **4.1.5. Resultados de la integración histórica–normativa** que haya quedado desactualizada;
- el objeto existente **Tabla 16**;
- su nota inmediata y la interpretación inmediata necesaria para evitar contradicciones.

No modifiques:

- 4.1.4, Tabla 14, Tabla 15 ni Figura 6;
- 4.1.6;
- Tabla 17;
- Figura 8;
- ninguna sección anterior o posterior;
- numeración de tablas o figuras;
- Lista de Tablas o Lista de Figuras en esta ejecución.

## 3.2 Corrección de prosa

Elimina de la presentación activa cualquier dependencia de los conteos legacy `1 006`, `373`, `633` y de la formulación de `backfill` como resultado gobernante de esta sección.

Conserva el texto anterior visible cuando sea sustituido: **amarillo + tachado**, sin `w:del`.

La nueva prosa debe expresar, en español natural y sin IDs internos visibles, que:

1. la integración se evaluó en 1 056 series;
2. la asociación de evidencia normativa dejó intacto el ranking histórico en 1 056/1 056 casos;
3. Top-1, Top-3, todas las posiciones y las puntuaciones históricas permanecieron sin cambios;
4. no se insertaron ni eliminaron candidatos;
5. las 3 168 relaciones candidato-caso del Top-3 tuvieron trazabilidad completa a un precedente histórico y a un documento normativo identificable;
6. la función de la evidencia normativa fue documental y no de reordenamiento;
7. estos controles no prueban corrección jurídica, suficiencia normativa ni validez externa.

No uses `Group1`, `F`, `HE3_F`, nombres de archivos, blobs, commits, prompts ni estados de gate en la prosa visible.

## 3.3 Tabla 16 — actualizar el mismo objeto

Mantén el mismo objeto Table 16 y su numeración. No crees una nueva tabla.

Actualiza la tabla a una presentación de **controles de invariancia y trazabilidad**, manteniendo cuatro columnas y, de ser posible, el mismo número de filas de datos. No sustituyas el objeto completo.

Presentación activa mínima requerida:

| Indicador | Estado histórico / entrada | Integración con evidencia | Resultado / lectura |
|---|---|---|---|
| Casos evaluados | 1 056 | 1 056 | Mismo benchmark interno |
| Ranking histórico invariante | 1 056 casos | 1 056/1 056 | 100 % sin cambio |
| Top-1 | Ranking histórico | Sin cambio | Invariante |
| Top-3 | Top-3 histórico fijo | Sin cambio | Invariante |
| Posiciones y puntuaciones históricas | Registradas por caso | Sin cambio | Invariantes |
| Candidatos insertados o eliminados | 0 | 0 | Ninguno |
| Trazabilidad candidato–precedente | 3 168 posiciones | 3 168/3 168 | Completa |
| Trazabilidad candidato–documento normativo | 3 168 posiciones | 3 168/3 168 | Completa |

Puedes ajustar únicamente redacción menor de encabezados/celdas para conservar el estilo nativo del documento, sin cambiar estos números ni su significado.

Para cada celda realmente modificada:

- texto anterior visible = amarillo + tachado;
- texto nuevo = amarillo y no tachado;
- contenido no afectado = formato normal.

No reemplaces la Tabla 16 completa por otra tabla.

La nota debe aclarar que `3 168 = 1 056 × 3` posiciones del Top-3 y que trazabilidad documental completa no equivale a corrección jurídica ni suficiencia probatoria.

---

# 4. A045 — Figura 7: supresión propuesta sin eliminación física

La Figura 7 legacy queda superseded porque su snapshot representa el estado anterior y la evidencia gobernante de integración queda comunicada con mayor fidelidad mediante Tabla 16 + síntesis textual.

En esta REVIEW V03:

1. **no elimines físicamente la Figura 7**;
2. conserva su número oficial `Figura 7` y su campo `SEQ Figura` existente;
3. conserva la imagen legacy byte-idéntica;
4. marca el caption/leyenda legacy que queda superseded con **amarillo + tachado**;
5. inmediatamente después de la figura/caption inserta una línea temporal de revisión, con estilo normal/no-caption y resaltado amarillo:

```text
PROPUESTA DE SUPRESIÓN DEL ELEMENTO GRÁFICO ANTERIOR — SE CONSERVA PARA REVISIÓN / NO ES NUMERACIÓN FINAL
```

6. no insertes imagen de reemplazo;
7. no crees un segundo `SEQ Figura`;
8. no renumeres Figuras 8–12;
9. no modifiques la Lista de Figuras;
10. no modifiques 4.1.6.

La razón visible de supresión no debe contener IDs internos. El detalle técnico queda en comentario/trazabilidad, no en el cuerpo visible.

---

# 5. Comentarios Word

Añade **exactamente 2 comentarios nuevos**:

```text
A044 = comentario sobre corrección de 4.1.5 / Tabla 16
A045 = comentario sobre supresión propuesta de Figura 7
```

No modifiques los 194 comentarios heredados.

Cada comentario debe estar íntegramente en español y contener exactamente estos seis apartados:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

### A044 — contenido mínimo

Debe explicar:

- reemplazo de conteos legacy por 1 056/1 056 casos de invariancia;
- 3 168/3 168 vínculos candidato–precedente y candidato–documento normativo;
- evidencia normativa asociada sin reordenamiento;
- no inserción/eliminación de candidatos;
- no equivalencia entre trazabilidad, corrección jurídica y validez externa.

### A045 — contenido mínimo

Debe explicar:

- Figura 7 legacy preservada físicamente;
- supresión únicamente propuesta en REVIEW V03;
- redundancia/obsolescencia respecto del estado científico gobernante;
- evidencia vigente concentrada en Tabla 16 y prosa;
- numeración 1–12 preservada hasta aceptación del autor;
- ninguna nueva figura ni nueva evidencia creada.

Paths, blobs y hashes pueden aparecer en los comentarios para trazabilidad, pero no en el texto visible de tesis.

---

# 6. Trazabilidad

Conserva **byte-idénticas las 104 filas heredadas** y añade exactamente dos filas:

```text
A044 = 4.1.5 / Tabla 16
A045 = Figura 7
```

Resultado esperado:

```text
INHERITED_TRACE_ROWS = 104
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 106
```

Para A044 registra al menos:

```text
change_type = TABLE_ROW_UPDATE / PARAGRAPH_UPDATE_MINIMAL
presentation_mode = EXISTING_TABLE_ROW_UPDATE
ranking_invariance = 1056/1056
traceability = 3168/3168
scientific_data_change = NO
new_inference = NO
internal_ids_visible = NO
status = APPLIED
```

Para A045 registra al menos:

```text
change_type = FIGURE_SUPPRESSION_PROPOSED
legacy_figure_preserved = YES
legacy_caption_visible = YES
legacy_caption_yellow_strikethrough = YES
replacement_image_inserted = NO
second_seq_figure_created = NO
figure_number_preserved = 7
scientific_data_change = NO
status = APPLIED
```

---

# 7. Validaciones estructurales obligatorias

Antes de entregar verifica:

```text
BASELINE_TABLE_OBJECT_COUNT = 24
FINAL_TABLE_OBJECT_COUNT = 24
TABLE_16_OBJECT_PRESERVED = true
TABLES_1_TO_15_UNCHANGED = true

INHERITED_COMMENT_COUNT = 194
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 196
ALL_COMMENT_IDS_ANCHORED = true

INHERITED_TRACE_ROWS = 104
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 106

TRACKED_DELETION_COUNT = 0
SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
FIGURE_6_UNCHANGED = true
FIGURE_7_LEGACY_PHYSICALLY_PRESERVED = true
FIGURE_7_MEDIA_BINARY_UNCHANGED = true
FIGURE_8_TO_12_UNCHANGED = true
NEW_MEDIA_FILES = 0

OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

Busca en todo texto visible nuevo atribuible a esta ejecución y exige cero apariciones de:

```text
Group1
HE3_F
G3
G4
G5
G6
G7
FIG015
A044
A045
Prompt
source freeze
gate
commit
blob
integration_ranking_invariance.json
integration_traceability.json
```

Los términos científicos visibles `Top-3`, `NANDINA`, `DAM`, `BM25`, `LLM` pueden mantenerse cuando correspondan.

---

# 8. QA visual localizado

Renderiza el DOCX resultante e inspecciona las páginas que cubran:

- final de Figura 6 / inicio de 4.1.5;
- prosa corregida de 4.1.5;
- Tabla 16 completa y su nota;
- Figura 7 legacy y su caption marcado;
- línea temporal de supresión propuesta;
- inicio de 4.1.6 como frontera posterior.

Verifica:

- ningún clipping ni solapamiento;
- Tabla 16 legible y sin filas/celdas desbordadas;
- cambios antiguos/nuevos distinguibles;
- Figura 7 físicamente visible y no deformada;
- caption legacy de Figura 7 visible con amarillo+tachado;
- línea de supresión propuesta visible;
- ninguna segunda numeración de Figura 7;
- continuidad razonable hacia 4.1.6;
- 4.1.6 intacta.

Si el layout materialmente falla, `STOPPED_PRECONDITION`; no cambies márgenes, secciones, tamaño de página ni estilos globales para hacerlo caber.

---

# 9. Salidas

No sobrescribas R3. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_G.docx
g7_thesis_claim_traceability_v0.3_G.csv
```

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121G_RESPUESTA_G7_F02_V03_BLOQUE_G_4_1_5_INTEGRACION.md
```

La respuesta debe incluir SHA-256 y tamaño exacto de ambas salidas y terminar con:

```text
PROMPT121G_EXECUTION = COMPLETE | STOPPED_PRECONDITION
A044_APPLIED = true|false
A045_APPLIED = true|false
TABLE_16_UPDATED_IN_PLACE = true|false
FIGURE_7_LEGACY_PRESERVED = true|false
FIGURE_7_SUPPRESSION_PROPOSED = true|false
NEW_MEDIA_FILES = 0|<n>
NEW_SEQ_FIGURE_FIELDS = 0|<n>
INHERITED_TRACE_ROWS = 104
NEW_TRACE_ROWS_ADDED = 2|<n>
TOTAL_TRACE_ROWS = 106|<n>
INHERITED_COMMENT_COUNT = 194
COMMENTS_ADDED = 2|<n>
TOTAL_COMMENT_COUNT = 196|<n>
ALL_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0|<n>
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0|<n>
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0|<n>
LOCAL_VISUAL_REVIEW = PASS|FAIL
121H_EXECUTED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 4.1.6, 121H ni ningún bloque posterior.