# PROMPT121F — Ejecutar G7-F02 REVIEW V03 — Bloque F: resultados 4.1.4 y Tablas 14–15

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No eres la IA Diseñadora y Auditora de Figuras Científicas.

Este bloque queda autorizado después del cierre externo de `121E-FIG45-R1`:

```text
PROMPT121E_FIG45_R1_EXTERNAL_AUDIT = PASS
PROMPT121E_FIG45_EXTERNAL_AUDIT_FINAL = PASS_AFTER_R1
PROMPT121E_FIG45 = APPROVED
121F_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Ejecuta **exclusivamente A041 y A042** del plan aprobado de G7-F02.

No ejecutes A043. No modifiques Figura 6. No ejecutes 121G ni ningún bloque posterior.

---

## 1. Precondición G7-F01 — fuente congelada obligatoria

Antes de modificar cualquier archivo, lee íntegramente el artefacto exacto:

```text
REPOSITORY = elVladdi/gci-nandina-rag
REF = d91298758dba674003bf650e7a303c36bd0b74d9
PATH = docs/writing/group7/g7_writing_source_freeze_v0.1.json
ARTIFACT_ID = G7_F01_WRITING_SOURCE_FREEZE_v0.1
```

No intentes localizar otro “source freeze” por semejanza de nombre. Este es el artefacto exacto requerido por 121F.

Respeta su precedencia:

- el proyecto aprobado gobierna formulaciones de problema, objetivos e hipótesis;
- G3 gobierna inferencia y HE2/HE5;
- G4 gobierna fuerza de claims y límites;
- G5 gobierna números presentados;
- G6 gobierna figuras y captions científicos.

Si no puedes leer exactamente ese archivo en ese commit, `STOPPED_PRECONDITION`.

---

## 2. Entradas obligatorias

Usa exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E_FIG45_R1.docx
SHA256 = a8c3054b12174fc72138fc5ee84f9d075e791a236e0eb7ca82fa89edbae4f310
SIZE = 4570032 bytes

g7_thesis_claim_traceability_v0.3_E_FIG45_R1.csv
SHA256 = d4e660771a189c962d7237a73bb897de9871ad57d4ad32a7d5b0b2c451e1a356
INHERITED_TRACE_ROWS = 101
```

Recalcula los SHA-256 antes de editar. Si alguno no coincide, `STOPPED_PRECONDITION`.

No reconstruyas el DOCX desde una versión anterior.

---

## 3. Fuentes científicas gobernantes para este bloque

Lee antes de redactar:

```text
# Fuente G5 congelada por G7-F01
PATH = docs/results/group5/g5_canonical_tables_v0.1.md
BLOB = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d
ROLE = CANONICAL_NUMERIC_PRESENTATION

PATH = outputs/results/group5/g5_table_registry_v0.1.json
BLOB = 4fe9318d52fad093066ff9f42d524fc95e436245
ROLE = CANONICAL_TABLE_INVENTORY
```

Para la recuperación histórica, verifica además la fuente primaria vinculada por G5:

```text
PATH = outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json
BLOB = a43893eca3dd756a1ff11935a9cf55afb728e8f4
VERSION = v0.2
```

Para A042 usa la presentación congelada G5-SECONDARY-02 y su fuente literal de soporte histórico. No sustituyas estos buckets por los antiguos buckets basados en conteo de series.

No recalcules métricas. No generes inferencia nueva.

---

## 4. Alcance único

Modifica únicamente:

```text
4.1.4. Resultados de la recuperación histórica
Tabla 14
Tabla 15
prosa inmediata de 4.1.4 necesaria para interpretar esas dos tablas
```

No modifiques:

- la Figura 6 ni su caption;
- 4.1.5 ni secciones posteriores;
- 4.1.3 ni las Figuras 4–5 aprobadas;
- ninguna sección anterior;
- la Lista de Tablas o Lista de Figuras;
- numeración oficial de tablas o figuras;
- ningún otro objeto gráfico.

### A043 / Figura 6

```text
A043_EXECUTED = false
FIGURE_6_CHANGED = false
```

A043 queda reservado para un bloque posterior bajo **IA Diseñadora y Auditora de Figuras Científicas**. No diseñes, regeneres, reemplaces ni adaptes la Figura 6 en 121F.

---

## 5. Contrato editorial REVIEW V03

Aplica íntegramente el contrato aprobado de Prompt119:

- conserva el formato nativo de la tesis;
- edición mínima: fragmento → celda → fila;
- no recrees una tabla completa si puede corregirse el objeto existente;
- los textos/valores antiguos realmente sustituidos deben quedar **amarillo + tachado + visibles**;
- los textos/valores nuevos deben quedar **amarillo, sin tachado**;
- contenido no modificado = formato normal;
- no uses `w:del`;
- no introduzcas en el texto visible IDs internos de grupos, prompts, fichas, gates, commits, rutas o hashes;
- todos los comentarios nuevos deben estar en español y usar exactamente los seis encabezados obligatorios:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Los paths/hashes pueden aparecer en comentarios para trazabilidad, pero no en la prosa visible de la tesis.

---

## 6. A041 — Recuperación histórica global / Tabla 14

### 6.1 Corrección de población y banco

El texto actualmente visible conserva cifras legacy `3 000` y `1 006`. Deben quedar sustituidas, bajo convención REVIEW, por el estado v0.2:

```text
BANCO_HISTORICO = 2 950 series
EVAL = 1 056 series
EVAL_DAM = 67
EVAL_NANDINA = 42
```

No describas `1 056` como una población externa ni como muestra probabilística.

### 6.2 Valores vigentes de la recuperación histórica

Usa exactamente:

```text
Casos evaluados = 1 056
Top-1 = 0.509469696969697 = 538/1056
Top-3 = 0.6714015151515151 = 709/1056
Top-5 = 0.7632575757575758 = 806/1056
Top-10 = 0.8910984848484849 = 941/1056
Top-50 = 0.9914772727272727 = 1047/1056
MRR@100 = 0.6297077493524843
```

Para el texto de tesis, redondea a cuatro decimales cuando corresponda:

```text
Top-1 = 0,5095
Top-3 = 0,6714
Top-5 = 0,7633
Top-10 = 0,8911
Top-50 = 0,9915
MRR@100 = 0,6297
```

`Top-50` es **suplementario** y no forma parte de los cinco estimandos primarios HE2_A. Debe indicarse como contexto descriptivo/suplementario y no como nueva evidencia confirmatoria.

### 6.3 Tabla 14

Conserva el objeto de Tabla 14 y actualízalo in place. El título activo final propuesto debe ser natural para tesis y evitar que “global” se interprete como desempeño end-to-end del framework. Usa:

```text
Desempeño de la recuperación histórica en el conjunto interno de evaluación
```

La parte activa de Tabla 14 debe presentar, como mínimo:

```text
Indicador        Valor     Lectura
Casos evaluados  1 056     Total del conjunto interno de evaluación
Top-1            0,5095    538 casos
Top-3            0,6714    709 casos
Top-5            0,7633    806 casos
Top-10           0,8911    941 casos
Top-50           0,9915    1 047 casos; resultado suplementario
MRR@100          0,6297    Rango recíproco medio
```

Las filas legacy que ya no formen parte de la presentación gobernante —por ejemplo Top-20, Recall@100, Partida@10, HS-6@10 o valores v0.1— no deben permanecer como afirmaciones activas. Si se retiran de la presentación propuesta, conserva sus contenidos anteriores visibles como revisión mediante amarillo + tachado y modifica la estructura del mismo objeto tabla, sin crear un nuevo objeto Tabla 14.

No inventes ni recalcules valores para filas legacy no gobernadas por G5.

### 6.4 Interpretación permitida A041

Puedes indicar, con redacción natural, que:

- 538/1 056 casos estuvieron en Top-1;
- 709/1 056 en Top-3;
- 806/1 056 en Top-5;
- 941/1 056 en Top-10;
- 1 047/1 056 en Top-50;
- nueve series no alcanzaron coincidencia exacta dentro del Top-50;
- MRR@100 fue 0,6297.

Debes incluir una delimitación equivalente a:

> Estas cifras describen exclusivamente la recuperación histórica en el benchmark interno del Capítulo 87 y no representan la exactitud global del framework RAG, corrección jurídica ni validez externa.

No conviertas valores observados del brazo histórico en intervalos de confianza por brazo. No introduzcas valores p.

---

## 7. A042 — Soporte histórico por DAM / Tabla 15

### 7.1 Corrección conceptual obligatoria

La Tabla 15 legacy usa buckets basados en cantidad de casos/series históricas (`1`, `2–4`, `5–9`, `10+`). Esa presentación queda superseded para este bloque.

La presentación gobernante usa **número de DAM históricas que contienen la subpartida de referencia**.

Usa exactamente estos cuatro buckets literales y valores:

```text
Bucket   Casos   Top-1      Top-3      MRR
1 DAM    27      0.370370   0.703704   0.564447
2 DAM    21      0.047619   0.190476   0.239384
3–4 DAM  425     0.691765   0.767059   0.760152
5+ DAM   583     0.399657   0.617496   0.551697
```

Para tesis, redondea a cuatro decimales:

```text
1 DAM    27      0,3704   0,7037   0,5644
2 DAM    21      0,0476   0,1905   0,2394
3–4 DAM  425     0,6918   0,7671   0,7602
5+ DAM   583     0,3997   0,6175   0,5517
```

La suma de casos es 1 056. No presentes esa suma como evidencia de independencia entre casos; la DAM sigue siendo el grupo de dependencia cuando corresponde.

### 7.2 Tabla 15

Conserva el objeto Tabla 15 y actualiza su estructura in place. El título activo final propuesto debe ser:

```text
Desempeño descriptivo de la recuperación histórica según soporte histórico por DAM
```

La parte activa de la tabla debe contener únicamente las columnas científicamente gobernadas para esta presentación:

```text
Soporte histórico por DAM | Casos | Top-1 | Top-3 | MRR
```

No mantengas activas las columnas legacy `Top-10` y `Top-100` si no están gobernadas por G5-SECONDARY-02. Si su supresión exige una modificación estructural, conserva el texto legacy con amarillo + tachado según REVIEW V03 y modifica el mismo objeto Tabla 15; no lo reemplaces por una tabla nueva.

### 7.3 Interpretación permitida A042

Esta evidencia es **DESCRIPTIVE_ONLY**.

Debes dejar claro que:

- los resultados no muestran una relación monotónica simple entre número de DAM históricas y desempeño;
- las categorías tienen tamaños muy distintos;
- no se autoriza inferencia causal ni inferencia poblacional externa;
- no se define ningún umbral post hoc de “precedentes insuficientes”;
- ningún bucket puede ser renombrado como `insuficiente`, `bajo soporte crítico` o equivalente;
- esta evidencia contribuye al análisis descriptivo de HE5, cuya disposición permanece `INCONCLUSIVE`.

Una redacción compatible es:

> Los valores variaron entre categorías y no siguieron un gradiente monotónico con el número de DAM históricas. Dado su carácter descriptivo y los tamaños desiguales de los grupos, estos resultados no permiten establecer un umbral de suficiencia de precedentes ni una relación causal; se conservan como evidencia descriptiva para el análisis de HE5.

Puedes mejorar la naturalidad, pero no aumentar la fuerza del claim.

---

## 8. Figura 6 — bloqueo explícito

La Figura 6 visible en la copia actual es legacy y su reemplazo corresponde a A043.

En 121F:

```text
FIGURE_6_CHANGED = false
FIGURE_6_CAPTION_CHANGED = false
A043_EXECUTED = false
```

No insertes una figura candidata, no regeneres ningún PNG/SVG, no añadas un comentario de Figura 6 y no añadas una fila A043.

El reemplazo posterior deberá representar la sensibilidad conjunta tamaño–composición EXP11A y será gestionado por la **IA Diseñadora y Auditora de Figuras Científicas**, no por la IA de Redacción.

---

## 9. Comentarios Word

Añade comentarios solo sobre cambios reales A041/A042. Para mantener revisión manejable, usa **exactamente dos comentarios nuevos**:

1. uno asociado a A041 / actualización de la recuperación histórica y Tabla 14;
2. uno asociado a A042 / actualización del soporte histórico por DAM y Tabla 15.

Ambos deben usar los seis encabezados obligatorios. Deben explicar números, fuente gobernante, efecto en la tesis y límites de interpretación.

No modifiques los 191 comentarios heredados.

Resultado esperado:

```text
INHERITED_COMMENT_COUNT = 191
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 193
```

Los IDs nuevos deben seguir la secuencia disponible; no renumeres comentarios heredados.

---

## 10. Trazabilidad acumulativa

Conserva byte-lógicamente las 101 filas heredadas: no cambies sus valores científicos/editoriales.

Añade exactamente dos filas nuevas, una por plan ID:

```text
A041 = 4.1.4 + Tabla 14
A042 = Tabla 15 + interpretación inmediata
```

Usa IDs nuevos secuenciales `G7F02-V03F-001` y `G7F02-V03F-002`.

Cada fila debe registrar al menos:

- `plan_id` correcto;
- `change_type` coherente con `TABLE_STRUCTURE_UPDATE / EXISTING_TABLE_ROW_UPDATE`;
- fuente gobernante;
- valores antiguos afectados;
- valores nuevos;
- comentario Word asociado;
- `scientific_recomputation = NO`;
- `new_inference = NO`;
- `figure_change = NO`;
- `state = APPLIED`.

Resultado esperado:

```text
INHERITED_TRACE_ROWS = 101
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 103
```

---

## 11. Validaciones obligatorias

Antes de entregar verifica:

```text
BASELINE_TABLE_OBJECT_COUNT = 24
FINAL_TABLE_OBJECT_COUNT = 24

INHERITED_COMMENT_COUNT = 191
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 193
ALL_COMMENT_IDS_ANCHORED = true

TRACKED_DELETION_COUNT = 0
INHERITED_TRACE_ROWS = 101
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 103

FIGURE_4_CHANGED = false
FIGURE_5_CHANGED = false
FIGURE_6_CHANGED = false
A043_EXECUTED = false
NEW_SEQ_FIGURE_FIELDS = 0

OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

En el texto activo nuevo de 4.1.4 no deben quedar como afirmaciones vigentes:

```text
3 000 [como tamaño actual del banco]
1 006 [como tamaño actual de evaluación]
Top-1 = 0,8628
Top-3 = 0,9374
MRR = 0,9062
buckets 1 / 2–4 / 5–9 / 10+ [como soporte vigente]
```

Las ocurrencias antiguas pueden permanecer únicamente si están marcadas amarillo + tachado como revisión superseded.

No introduzcas en texto visible nuevo:

```text
G3
G4
G5
G6
A041
A042
A043
Prompt
source freeze
gate
commit
blob
EXP11A
```

`EXP11A` se reserva para el posterior trabajo de Figura 6 y no debe adelantarse en este bloque salvo que ya existiera en texto heredado fuera del alcance.

---

## 12. QA visual localizado

Renderiza el DOCX resultante.

Inspecciona visualmente todas las páginas que contengan:

- inicio de 4.1.4;
- Tabla 14 completa;
- interpretación posterior de Tabla 14;
- Tabla 15 completa;
- interpretación posterior de Tabla 15;
- Figura 6 legacy sin cambios;
- inicio de 4.1.5 como frontera.

Verifica:

- ningún clipping;
- ninguna fila cortada ilegiblemente;
- columnas legibles;
- ningún desbordamiento;
- no duplicación de Tabla 14 o Tabla 15;
- no recreación accidental de objetos tabla;
- continuidad razonable del texto;
- Figura 6 y 4.1.5 intactas.

Si la estructura de Tabla 15 no puede modificarse de forma segura sin recrear el objeto completo, `STOP` y reporta el bloqueo. No sacrifiques la revisión fila/celda por una reconstrucción silenciosa.

---

## 13. Salidas

Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
g7_thesis_claim_traceability_v0.3_F.csv
```

No sobrescribas R1.

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121F_RESPUESTA_G7_F02_V03_BLOQUE_F_RESULTADOS_4_1_4_TABLAS.md
```

sobre `codex/prompts-temporary`.

La respuesta debe incluir SHA-256 y tamaño de ambas salidas y este estado terminal:

```text
PROMPT121F_EXECUTION = COMPLETE | STOPPED_PRECONDITION
A041_APPLIED = true|false
A042_APPLIED = true|false
A043_EXECUTED = false
TABLE_14_UPDATED_IN_PLACE = true|false
TABLE_15_UPDATED_IN_PLACE = true|false
FIGURE_6_CHANGED = false
INHERITED_TRACE_ROWS = 101
INHERITED_TRACE_ROWS_CHANGED = 0|<n>
NEW_TRACE_ROWS_ADDED = 2|<n>
INHERITED_COMMENT_COUNT = 191
COMMENTS_ADDED = 2|<n>
TOTAL_COMMENT_COUNT = 193|<n>
TRACKED_DELETION_COUNT = 0|<n>
ALL_COMMENT_IDS_ANCHORED = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0|<n>
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0|<n>
LOCAL_VISUAL_REVIEW = PASS|FAIL
121G_EXECUTED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Detente para auditoría externa. No ejecutes A043, 121G ni ningún bloque posterior.
