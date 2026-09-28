# PROMPT121I — Ejecutar G7-F02 REVIEW V03 — Bloque I: 4.1.7 explicación auditable del Top-3

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No regeneres figuras, no recalcules métricas y no ejecutes 4.1.8 ni ningún bloque posterior.

Esta ejecución queda autorizada exclusivamente después del PASS externo de 121H-R1:

```text
PROMPT121H_R1_EXTERNAL_AUDIT = PASS
A046_EXTERNAL_AUDIT = PASS_AFTER_R1
A047_EXTERNAL_AUDIT = PASS
121I_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría gobernante:

```text
writing_prompts_tmp/121H_R1_AUDITORIA_EXTERNA_PASS.md
@ e04f2aab40201abc600d303722ecdda583fc0612
```

Lee íntegramente además:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
@ 583138f94646b1e84de1c28f32342e59f82988a3

docs/writing/group7/g7_writing_source_freeze_v0.1.md
GIT_BLOB = feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430

docs/writing/group7/g7_writing_source_freeze_v0.1.json
GIT_BLOB = 776fcb52e8ada9967504001b897c75b4108bfb63
```

Ejecuta exclusivamente **A048, A049 y A050** del plan aprobado.

No ejecutes A051, 4.1.8, 121J ni ningún bloque posterior.

---

## 1. Entradas acumulativas exactas

Trabaja exclusivamente sobre los artefactos H_R1 aprobados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_H_R1.docx
SHA256 = 810b42ba934e411e893357e5713651e7b8f7d08df3c74b739eac49d387cff909
SIZE = 4667064

g7_thesis_claim_traceability_v0.3_H_R1.csv
SHA256 = bc9bf9cebe931e8747ca91c80f86726459f5a99b24e0c7dd076e3fa2e7314a31
SIZE = 100004
ROWS = 108
```

Verifica ambos hashes, tamaños y filas antes de editar. Si alguno no coincide, `STOPPED_PRECONDITION`.

No reconstruyas H_R1 desde H, G ni versiones anteriores. No modifiques A046/A047 ya aprobados.

Estado estructural heredado que debe preservarse salvo lo explícitamente autorizado en este prompt:

```text
TABLE_OBJECT_COUNT = 24
COMMENT_COUNT = 198
TRACE_ROWS = 108
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
```

---

## 2. Fuentes científicas gobernantes para HE4 / 4.1.7

Lee íntegramente y verifica los blobs congelados:

```text
outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_he4_joint_jk_assessment_v0.2.json
GIT_BLOB = b617b4f397d0ffb4f8882ddda06790b1c539543e

outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_findings_v0.2.md
GIT_BLOB = 4b9dd1b3079235b2c54d5777fc788f0e98b27e32

outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv
GIT_BLOB = 28cd7fbc492ecc4d4744ec5c3433ce5342213e79
```

Estado científico vinculante:

```text
HE4 = PARTIALLY_SUPPORTED
EVALUATED_CASES = 50

STRUCTURAL_TOP3_ORDER_PRESERVATION = 50/50 = 1.00
TRACEABILITY_COMPLETENESS = 50/50 = 1.00
GENERIC_NORMATIVE_WARNING_CONTROL = 41/50 = 0.82

QUALITATIVE_AUDITABLE = 28/50 = 0.56
QUALITATIVE_NOT_AUDITABLE = 22/50 = 0.44
HARD_VIOLATIONS = 0/50 = 0.00

EVALUATOR_MODALITY = AI_EXPERT_ROLE
EVALUATOR_IDENTIFIER = independent_ai_reviewer_01
HUMAN_SCORING = false
LLM_AS_JUDGE = true
GROUND_TRUTH_EXPOSED = false
REFERENCE_RANK_EXPOSED = false
BUCKET_EXPOSED = false
EXTERNAL_EVIDENCE_USED = false
WEB_USED = false
RETRIEVAL_USED = false

QUALITATIVE_TOTAL_MEAN = 11.72
QUALITATIVE_TOTAL_MEDIAN = 12.0
QUALITATIVE_TOTAL_RANGE = 6-15
TRACEABILITY_MEAN = 2.00
VERIFIABILITY_MEAN = 0.54

LIMITATION_1 = PROMPT_SCHEMA_SPECIFICATION_MISMATCH
LIMITATION_2 = EVALUATOR_MODALITY_DEVIATION
```

Interpretación obligatoria:

- los controles estructurales y la evaluación cualitativa miden propiedades distintas y no son intercambiables;
- que 50/50 casos preserven Top-3/orden y trazabilidad **no** implica que 50/50 sean cualitativamente auditables;
- 28/50 fichas cumplen el umbral cualitativo congelado y 22/50 no;
- no se registraron violaciones graves bajo la evaluación cualitativa congelada;
- la puntuación cualitativa fue realizada por un evaluador independiente de inteligencia artificial configurado bajo un rol experto, no por evaluación humana;
- conserva explícitamente la discrepancia entre la especificación del prompt y el esquema efectivamente evaluado, y la desviación de modalidad del evaluador;
- `advertencias_globales` quedó fuera de la evaluación por la discrepancia de esquema; no lo conviertas en una métrica inexistente;
- auditabilidad estructural/cualitativa no equivale a corrección jurídica de la clasificación;
- no generalices estos resultados fuera de las 50 fichas evaluadas ni fuera del benchmark interno;
- no introduzcas valores p, intervalos de confianza, causalidad, validación legal, puntuación humana ni inferencia de superpoblación.

No muestres en la tesis visible los identificadores técnicos `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`, `EVALUATOR_MODALITY_DEVIATION`, `AI_EXPERT_ROLE`, `independent_ai_reviewer_01`, nombres de archivos, blobs, commits, prompts, gates ni IDs de gobernanza. Traduce las limitaciones a español natural.

---

# 3. A048 — 4.1.7 y Tabla 18: controles estructurales y trazabilidad

## 3.1 Alcance de prosa

Modifica únicamente la prosa de **4.1.7. Resultados de la explicación auditable del Top-3** necesaria para sincronizarla con el estado HE4 vigente.

Debes conservar el estilo nativo y la lógica de REVIEW V03:

- texto legacy sustituido = **amarillo + tachado**, visible, sin `w:del`;
- texto nuevo = **amarillo, no tachado**;
- texto no afectado = formato normal.

La presentación activa debe dejar claro que:

1. se evaluaron 50 fichas del explicador Top-3;
2. en las 50/50 se preservaron el Top-3 y su orden;
3. la trazabilidad candidato–evidencia fue completa en 50/50;
4. el control de advertencia normativa genérica se cumplió en 41/50;
5. el cumplimiento estructural no equivale a calidad cualitativa ni a corrección jurídica;
6. la evaluación cualitativa se presenta separadamente en Tabla 19;
7. la discrepancia entre especificación del prompt y esquema evaluado permanece como limitación metodológica.

No presentes un **puntaje medio de auditabilidad de 0,9520** como resultado vigente principal. No conviertas los antiguos quince controles binarios en una escala universal validada.

## 3.2 Tabla 18 — actualizar el mismo objeto

Mantén el mismo objeto Tabla 18 y su numeración. **No crees una tabla nueva ni reemplaces el objeto completo.**

Conserva tres columnas y las trece filas de datos existentes. Actualiza contenido por celda/fila dentro del mismo objeto. Para cada celda realmente modificada:

- texto anterior visible = amarillo + tachado;
- texto nuevo = amarillo y no tachado;
- contenido no afectado = formato normal.

Título activo recomendado:

```text
Controles estructurales y de trazabilidad de las explicaciones Top-3
```

Usa las trece filas de datos para presentar, como mínimo, este contenido sin cambiar su significado:

| Control | Resultado | Lectura |
|---|---:|---|
| Fichas evaluadas | 50 | Base de evaluación HE4 |
| Top-3 y orden preservados | 50/50 | 100 % |
| Trazabilidad candidato–evidencia completa | 50/50 | 100 % |
| Advertencia normativa genérica conforme | 41/50 | 82 % |
| Advertencia normativa genérica faltante | 9/50 | 18 % |
| Etiqueta de referencia expuesta al evaluador | No | Control de evaluación |
| Posición de referencia expuesta al evaluador | No | Control de evaluación |
| Grupos/buckets de dificultad expuestos | No | Control de evaluación |
| Evidencia externa utilizada | No | Sin evidencia externa |
| Web utilizada | No | No |
| Recuperación adicional utilizada por el evaluador | No | No |
| Puntuación humana | No | Evaluación no humana |
| Estado del componente estructural | Aprobado con limitación | Discrepancia entre especificación del prompt y esquema evaluado |

Puedes ajustar únicamente redacción menor para encajar en el estilo nativo, sin cambiar números, denominadores o significado científico.

La nota inmediata debe aclarar que los controles estructurales verifican preservación y trazabilidad; no demuestran corrección jurídica ni sustituyen la evaluación cualitativa. También debe declarar en español natural la discrepancia de esquema sin exponer el ID interno.

---

# 4. A049 — Tabla 19: evaluación cualitativa HE4

## 4.1 Objeto y presentación

Mantén el mismo objeto Tabla 19 y su numeración. **No crees una tabla nueva ni sustituyas el objeto completo.**

Conserva cuatro columnas y las siete filas de datos existentes. Actualiza contenido por celda/fila. Para cada celda realmente modificada:

- texto anterior visible = amarillo + tachado;
- texto nuevo = amarillo y no tachado;
- contenido no afectado = formato normal.

Título activo recomendado:

```text
Evaluación cualitativa de la auditabilidad de las explicaciones Top-3
```

Presentación activa mínima requerida:

| Resultado | Cantidad / valor | Tasa / resumen | Base o lectura |
|---|---:|---:|---|
| Fichas evaluadas | 50 | 100 % | Evaluación cualitativa |
| Fichas auditables | 28 | 56 % | Umbral cualitativo congelado |
| Fichas no auditables | 22 | 44 % | Umbral cualitativo congelado |
| Violaciones graves | 0 | 0 % | Ninguna observada |
| Trazabilidad | 2,00 | Mediana 2,0 | Media de la dimensión |
| Verificabilidad | 0,54 | Mediana 1,0 | Media de la dimensión |
| Modalidad de evaluación | IA independiente | Sin puntuación humana | Rol experto predefinido |

No mantengas como presentación activa las categorías legacy `Soporte alto`, `Soporte medio`, `Soporte bajo`, ni los antiguos conteos de coincidencias/advertencias que pertenecen a un estado anterior de evaluación.

La nota inmediata debe declarar que:

- la evaluación cualitativa fue realizada por una IA independiente configurada bajo un rol experto;
- no hubo puntuación humana;
- esta modalidad difiere de la revisión humana preparada originalmente y constituye una limitación metodológica;
- la auditabilidad cualitativa no equivale a corrección jurídica de la clasificación.

## 4.2 Interpretación inmediata

Corrige la interpretación posterior a Tabla 19 para expresar, en español natural y sin IDs internos:

- 28 de 50 fichas fueron auditables bajo el umbral cualitativo congelado;
- 22 de 50 no lo fueron;
- no hubo violaciones graves;
- los 50/50 pases estructurales de Tabla 18 no contradicen el resultado 28/50 porque las tablas evalúan propiedades diferentes;
- la verificabilidad fue la dimensión más débil entre las dos dimensiones resumidas aquí, mientras la trazabilidad alcanzó su máximo medio;
- la modalidad de evaluación mediante IA y la discrepancia de esquema limitan la fuerza interpretativa;
- no se infiere corrección jurídica, validación experta humana ni generalización externa.

No conviertas la ausencia de violaciones graves en evidencia de corrección legal o de clasificación correcta.

---

# 5. A050 — Figura 9: supresión propuesta sin eliminación física

La Figura 9 legacy comunica un score/control agregado de un estado anterior y queda superseded por la separación vigente entre Tabla 18 (estructura/trazabilidad) y Tabla 19 (evaluación cualitativa).

En esta REVIEW V03:

1. **no elimines físicamente la Figura 9**;
2. conserva su número oficial `Figura 9` y su campo `SEQ Figura` existente;
3. conserva la imagen legacy byte-idéntica;
4. marca el caption/leyenda legacy superseded con **amarillo + tachado**;
5. inmediatamente después de la figura/caption inserta una línea temporal de revisión, con estilo normal/no-caption y resaltado amarillo:

```text
PROPUESTA DE SUPRESIÓN DEL ELEMENTO GRÁFICO ANTERIOR — SE CONSERVA PARA REVISIÓN / NO ES NUMERACIÓN FINAL
```

6. no insertes imagen de reemplazo;
7. no crees un segundo `SEQ Figura`;
8. no renumeres Figuras 10–12;
9. no modifiques la Lista de Figuras;
10. no modifiques 4.1.8.

La razón visible no debe contener IDs internos. El detalle técnico queda en comentario/trazabilidad, no en el cuerpo visible.

---

# 6. Comentarios Word

Conserva sin modificación los **198 comentarios heredados** y añade **exactamente 3 comentarios nuevos**:

```text
A048 = comentario sobre 4.1.7 / Tabla 18
A049 = comentario sobre Tabla 19 / evaluación cualitativa
A050 = comentario sobre supresión propuesta de Figura 9
```

Usa estos IDs salvo que la verificación estructural demuestre que ya están ocupados:

```text
A048 -> comment_id 449
A049 -> comment_id 450
A050 -> comment_id 451
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

### A048 — contenido mínimo

Debe explicar:

- 50 fichas evaluadas;
- preservación Top-3/orden 50/50;
- trazabilidad completa 50/50;
- advertencia normativa genérica 41/50;
- discrepancia entre especificación del prompt y esquema evaluado;
- controles estructurales ≠ calidad cualitativa ≠ corrección jurídica.

### A049 — contenido mínimo

Debe explicar:

- 28/50 auditables y 22/50 no auditables;
- 0 violaciones graves;
- evaluación por IA independiente bajo rol experto;
- ausencia de puntuación humana;
- desviación respecto de la modalidad humana originalmente preparada;
- limitación de generalización y de corrección jurídica.

### A050 — contenido mínimo

Debe explicar:

- Figura 9 legacy preservada físicamente;
- supresión únicamente propuesta en REVIEW V03;
- obsolescencia del score agregado frente a la separación estructural/cualitativa vigente;
- evidencia vigente concentrada en Tablas 18–19 y prosa;
- numeración 1–12 preservada hasta aceptación del autor;
- ninguna nueva figura ni nueva evidencia creada.

Paths, blobs y hashes pueden aparecer en comentarios para trazabilidad, pero no en el texto visible de tesis.

Resultado esperado:

```text
INHERITED_COMMENT_COUNT = 198
COMMENTS_ADDED = 3
TOTAL_COMMENT_COUNT = 201
ALL_COMMENT_IDS_ANCHORED = true
```

---

# 7. Trazabilidad

Conserva **byte-idénticas las 108 filas heredadas** y añade exactamente tres filas:

```text
A048 = 4.1.7 / Tabla 18
A049 = 4.1.7 / Tabla 19
A050 = 4.1.7 / Figura 9
```

Resultado esperado:

```text
INHERITED_TRACE_ROWS = 108
NEW_TRACE_ROWS_ADDED = 3
TOTAL_TRACE_ROWS = 111
```

Para A048 registra al menos:

```text
change_type = TABLE_STRUCTURE_UPDATE / PARAGRAPH_UPDATE_MINIMAL
presentation_mode = EXISTING_TABLE_ROW_UPDATE
cases = 50
top3_order_preservation = 50/50
traceability_completeness = 50/50
generic_normative_warning_control = 41/50
prompt_schema_limitation = DOCUMENTED
scientific_data_change = NO
new_inference = NO
internal_ids_visible = NO
status = APPLIED
```

Para A049 registra al menos:

```text
change_type = TABLE_STRUCTURE_UPDATE / PARAGRAPH_UPDATE_MINIMAL
presentation_mode = EXISTING_TABLE_ROW_UPDATE
auditable = 28/50
not_auditable = 22/50
hard_violations = 0/50
evaluator_modality = AI_INDEPENDENT_EXPERT_ROLE
human_scoring = NO
evaluator_modality_limitation = DOCUMENTED
scientific_data_change = NO
new_inference = NO
internal_ids_visible = NO
status = APPLIED
```

Para A050 registra al menos:

```text
change_type = FIGURE_SUPPRESSION_PROPOSED
legacy_figure_preserved = YES
legacy_caption_visible = YES
legacy_caption_yellow_strikethrough = YES
replacement_image_inserted = NO
second_seq_figure_created = NO
figure_number_preserved = 9
scientific_data_change = NO
status = APPLIED
```

---

# 8. Validaciones estructurales obligatorias

Antes de entregar verifica:

```text
BASELINE_TABLE_OBJECT_COUNT = 24
FINAL_TABLE_OBJECT_COUNT = 24
TABLE_18_OBJECT_PRESERVED = true
TABLE_19_OBJECT_PRESERVED = true
TABLES_1_TO_17_UNCHANGED = true
TABLES_20_TO_24_UNCHANGED = true
TABLE_18_TBLPR_UNCHANGED = true
TABLE_18_TBLGRID_UNCHANGED = true
TABLE_19_TBLPR_UNCHANGED = true
TABLE_19_TBLGRID_UNCHANGED = true

INHERITED_COMMENT_COUNT = 198
COMMENTS_ADDED = 3
TOTAL_COMMENT_COUNT = 201
ALL_COMMENT_IDS_ANCHORED = true
INHERITED_COMMENTS_XML_CONTENT_UNCHANGED = true

INHERITED_TRACE_ROWS = 108
NEW_TRACE_ROWS_ADDED = 3
TOTAL_TRACE_ROWS = 111
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true

TRACKED_DELETION_COUNT = 0
SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
MEDIA_FILE_COUNT = 16
FIGURE_8_UNCHANGED = true
FIGURE_9_LEGACY_PHYSICALLY_PRESERVED = true
FIGURE_9_MEDIA_BINARY_UNCHANGED = true
FIGURE_10_TO_12_UNCHANGED = true
NEW_MEDIA_FILES = 0

4_1_6_UNCHANGED_FROM_H_R1 = true
4_1_8_AND_AFTER_OOXML_UNCHANGED_FROM_H_R1 = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

Busca en todo texto visible nuevo atribuible a esta ejecución y exige cero apariciones de identificadores internos, incluyendo:

```text
PROMPT_SCHEMA_SPECIFICATION_MISMATCH
EVALUATOR_MODALITY_DEVIATION
AI_EXPERT_ROLE
independent_ai_reviewer_01
EXP-04
Fase J
Fase K
Group1
G3
G4
G5
G6
G7
A048
A049
A050
prompt
blob
commit
gate
```

No interpretes `prompt` dentro de texto legacy heredado fuera del alcance como fallo; la búsqueda se aplica a texto visible **nuevo atribuible a 121I**.

---

# 9. QA visual obligatorio

Renderiza el DOCX resultante y revisa al menos desde el final de 4.1.6 hasta el inicio de 4.1.8.

Verifica visualmente:

- 4.1.6 permanece igual a H_R1;
- la prosa nueva de 4.1.7 usa amarillo sin tachado y la sustituida permanece amarilla + tachada;
- Tabla 18 conserva estilo y objeto, con contenido legible;
- Tabla 19 conserva estilo y objeto, con contenido legible;
- no hay celdas desbordadas, columnas ilegibles, clipping ni superposición;
- Figura 9 legacy se conserva sin deformación;
- caption legacy de Figura 9 queda amarillo + tachado;
- línea temporal de supresión aparece inmediatamente después, resaltada y fuera del estilo caption;
- no existe segunda numeración de Figura 9;
- 4.1.8 inicia intacta.

---

# 10. Salidas

No sobrescribas H_R1. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_I.docx
g7_thesis_claim_traceability_v0.3_I.csv
```

Publica respuesta oficial en:

```text
writing_prompts_tmp/121I_RESPUESTA_G7_F02_V03_BLOQUE_I_4_1_7_EXPLICACION_AUDITABLE.md
```

La respuesta debe reportar como mínimo:

```text
PROMPT121I_EXECUTION = COMPLETE | STOPPED_PRECONDITION
A048_APPLIED = true|false
A049_APPLIED = true|false
A050_APPLIED = true|false
TABLE_18_UPDATED_IN_PLACE = true|false
TABLE_19_UPDATED_IN_PLACE = true|false
FIGURE_9_LEGACY_PRESERVED = true|false
FIGURE_9_SUPPRESSION_PROPOSED = true|false
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
INHERITED_TRACE_ROWS = 108
NEW_TRACE_ROWS_ADDED = 3
TOTAL_TRACE_ROWS = 111
INHERITED_COMMENT_COUNT = 198
COMMENTS_ADDED = 3
TOTAL_COMMENT_COUNT = 201
ALL_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0
4_1_8_AND_AFTER_UNCHANGED_FROM_H_R1 = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS|FAIL
121J_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 4.1.8, 121J ni ningún bloque posterior.
