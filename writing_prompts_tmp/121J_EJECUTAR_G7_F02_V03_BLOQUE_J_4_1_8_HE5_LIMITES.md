# PROMPT121J — Ejecutar G7-F02 REVIEW V03 — Bloque J: 4.1.8 patrones de error y límites HE5

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No recalcules métricas, no generes figuras y no ejecutes 4.2 ni ningún bloque posterior.

Esta ejecución queda autorizada exclusivamente después del PASS externo de 121I:

```text
PROMPT121I_EXTERNAL_AUDIT = PASS
A048_EXTERNAL_AUDIT = PASS
A049_EXTERNAL_AUDIT = PASS
A050_EXTERNAL_AUDIT = PASS
121J_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría gobernante:

```text
writing_prompts_tmp/121I_AUDITORIA_EXTERNA_PASS.md
```

Ejecuta exclusivamente **A051 y A052** del plan aprobado.

No ejecutes A053, 4.2, 121K ni ningún bloque posterior.

---

## 1. Entradas acumulativas exactas

Trabaja exclusivamente sobre:

```text
Molleapasa_gv_G7F02_REVIEW_V03_I.docx
SHA256 = a70d80d2c0438c280a8e4ff673d5502486c6080c4c5456b2f1ad0bce5913f79a
SIZE = 4670468

g7_thesis_claim_traceability_v0.3_I.csv
SHA256 = 08921f63532fc9f55014f77e3e210dc4bfe0c833882630f34da4e6d3df031f2a
SIZE = 103747
ROWS = 111
```

Verifica hashes, tamaños y filas antes de editar. Si alguno no coincide, `STOPPED_PRECONDITION`.

No reconstruyas I desde versiones anteriores.

Estado heredado obligatorio:

```text
TABLE_OBJECT_COUNT = 24
COMMENT_COUNT = 201
TRACE_ROWS = 111
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
```

---

## 2. Fuentes científicas gobernantes

Lee y verifica las siguientes fuentes congeladas:

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
GIT_BLOB = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61

outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_hierarchy_errors_v0.2.csv
GIT_BLOB = b5bd099114e7262f316dfc846b867bec9e7f176d

outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_errors_by_support_v0.2.csv
GIT_BLOB = 0f70928ba83eec87c116e62cf104f505293bc092

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
GIT_BLOB = 129a67b15db429b86af059d61753b1942c8f243f

docs/writing/group7/g7_writing_source_freeze_v0.1.md
GIT_BLOB = feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430
```

Estado científico vinculante:

```text
HE5 = INCONCLUSIVE

DESCRIPTION_QUALITY = NOT_ESTIMABLE
DESCRIPTION_QUALITY_REASON = no prospective operationalization; no post-hoc prevalence rule

HIERARCHY = DESCRIPTIVE_ONLY
SAME_CHAPTER_ERRORS = 147
SAME_HS4_ERRORS = 284
SAME_HS6_ERRORS = 87
HIERARCHY_PROSPECTIVE_CONCENTRATION_THRESHOLD = NONE

PRECEDENT_SUPPORT = DESCRIPTIVE_ONLY
SUPPORT_BUCKET_1_DAM_CASES = 27
SUPPORT_BUCKET_2_DAM_CASES = 21
SUPPORT_BUCKET_3_4_DAM_CASES = 425
SUPPORT_BUCKET_5PLUS_DAM_CASES = 583
FROZEN_INSUFFICIENCY_THRESHOLD = NONE

INTERNAL_VALIDITY = DOCUMENTED_LIMITATION
EVAL_SERIES = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
EMPIRICAL_SCOPE = Capítulo 87 / offline / evaluación interna
EXTERNAL_VALIDATION = NONE

EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11A_RULE = tamaño y composición varían conjuntamente; no efecto causal aislado ni monotónico del tamaño

EXP11B = DESCRIPTIVE / TEN_OBSERVED_SEED_PAIRS
EXP11B_RULE = no inferencia a una superpoblación de semillas; 10 x 1056 no son observaciones independientes

EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE
EXP12_RETRIEVAL_PERFORMED = false
EXP12_REOPEN = forbidden
```

Interpretación obligatoria:

- HE5 permanece **inconclusa**;
- ausencia de estimabilidad no es evidencia positiva ni negativa;
- los conteos jerárquicos son descriptivos y no autorizan umbral de concentración;
- los grupos de soporte histórico deben conservarse literalmente y ninguno puede etiquetarse retrospectivamente como «insuficiente»;
- el alcance interno/offline no demuestra validez externa;
- EXP11A no identifica causalmente tamaño por separado de composición;
- EXP11B describe diez pares observados y no autoriza inferencia a una población de semillas;
- EXP12 no se reabre, no se ejecuta recuperación y su efecto de diversidad permanece no estimable;
- no introduzcas valores p, nuevos intervalos, causalidad, umbrales post hoc, generalización externa ni nueva evidencia.

No muestres IDs internos `EXP11A`, `EXP11B`, `EXP12`, `G3F02-*`, nombres de archivos, blobs, commits, prompts, gates ni etiquetas de gobernanza en el texto visible de la tesis. Traduce todo a español natural.

---

# 3. A051 — 4.1.8 y Tabla 20

## 3.1 Prosa de 4.1.8

Modifica únicamente la prosa de **4.1.8. Patrones de error y límites observados** necesaria para reemplazar el estado legacy y presentar la evidencia vigente.

Contrato REVIEW V03:

- texto legacy sustituido = amarillo + tachado, visible, sin `w:del`;
- texto nuevo = amarillo, no tachado;
- texto no afectado = formato normal.

La prosa activa debe expresar en lenguaje natural:

1. HE5 permanece inconclusa;
2. la calidad descriptiva no fue operacionalizada prospectivamente y no es estimable como concentración o prevalencia;
3. la proximidad jerárquica se describe con conteos observados, sin umbral confirmatorio;
4. el soporte histórico se describe por `1 DAM`, `2 DAM`, `3–4 DAM` y `5+ DAM`, sin declarar retrospectivamente un grupo «insuficiente»;
5. el benchmark es interno/offline de Capítulo 87 y no aporta validación externa;
6. las sensibilidades de tamaño/composición son descriptivas/no causales bajo sus respectivos límites;
7. el análisis de diversidad quedó cerrado sin recuperación y su efecto no es estimable;
8. no se crean nuevas categorías, umbrales o inferencias.

Elimina de la presentación activa afirmaciones legacy como que falta generar un artefacto futuro para poder cerrar HE5 o que la conclusión depende de una codificación pendiente de 1 006 consultas.

## 3.2 Tabla 20 — mismo objeto

Mantén el mismo objeto **Tabla 20**, su numeración, tres columnas y nueve filas de datos. No crees una tabla nueva ni reemplaces el objeto completo.

Título activo recomendado:

```text
Patrones y límites observados con la evidencia disponible
```

Actualiza el contenido de las nueve filas para presentar exactamente estas nueve unidades de síntesis, en español natural y sin IDs internos visibles:

| Componente | Evidencia observada | Límite o lectura |
|---|---|---|
| Calidad descriptiva | No estimable | No se definió una operacionalización prospectiva; no se calcula concentración o prevalencia post hoc |
| Proximidad: mismo capítulo | 147 casos | Descriptivo; sin umbral prospectivo de concentración |
| Proximidad: misma partida HS-4 | 284 casos | Descriptivo; sin umbral prospectivo de concentración |
| Proximidad: misma subpartida HS-6 | 87 casos | Descriptivo; sin umbral prospectivo de concentración |
| Soporte por precedentes | 1 DAM: 27; 2 DAM: 21; 3–4 DAM: 425; 5+ DAM: 583 | Ningún grupo se define retrospectivamente como «insuficiente» |
| Alcance de validez | 1 056 series; 67 DAM; 42 NANDINA; Capítulo 87 offline | Benchmark interno; sin validación externa |
| Sensibilidad tamaño–composición | Condiciones observadas con tamaño y composición variando conjuntamente | Descriptiva y no causal; no identifica efecto aislado o monotónico del tamaño |
| Sensibilidad H150/H200 | Diez pares observados | Descriptiva; no inferencia a superpoblación de semillas ni independencia de 10×1 056 casos |
| Diversidad del banco histórico | Cerrado sin ejecutar recuperación | Efecto no estimable; no reabrir ni relajar post hoc el diseño |

Puedes ajustar redacción menor por estilo/anchura, sin cambiar significado, cifras o límites.

La nota inmediata debe indicar que una misma instancia puede contribuir a más de un patrón, que las categorías no constituyen una taxonomía causal y que HE5 permanece inconclusa.

La interpretación posterior debe sintetizar los límites sin declarar que los errores «se concentraron» en un componente no estimable o sin umbral prospectivo.

---

# 4. A052 — Figura 10: supresión propuesta

La Figura 10 legacy cuantifica categorías de error de un estado anterior y no existe una nueva figura equivalente autorizada por la evidencia vigente.

En REVIEW V03:

1. no elimines físicamente Figura 10;
2. conserva su número `Figura 10` y el `SEQ Figura` existente;
3. conserva la imagen legacy byte-idéntica;
4. marca el caption/leyenda legacy con amarillo + tachado;
5. inmediatamente después añade una línea temporal, estilo normal/no-caption y amarillo:

```text
PROPUESTA DE SUPRESIÓN DEL ELEMENTO GRÁFICO ANTERIOR — SE CONSERVA PARA REVISIÓN / NO ES NUMERACIÓN FINAL
```

6. no insertes imagen de reemplazo;
7. no crees un segundo `SEQ Figura`;
8. no renumeres Figuras 11–12;
9. no modifiques la Lista de Figuras;
10. no modifiques 4.2 ni nada posterior.

---

# 5. Comentarios Word

Conserva sin modificación los **201 comentarios heredados** y añade exactamente **2 comentarios nuevos**:

```text
A051 -> comment_id 452
A052 -> comment_id 453
```

Cada comentario nuevo debe contener, íntegramente en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

No modifiques el contenido ni los anclajes de comentarios heredados.

Resultado obligatorio:

```text
INHERITED_COMMENT_COUNT = 201
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 203
ALL_COMMENT_IDS_ANCHORED = true
```

---

# 6. Trazabilidad

Conserva las **111 filas heredadas** como prefijo byte-idéntico y añade exactamente dos filas:

```text
A051 / 4.1.8 + Tabla 20 / comment_id 452
A052 / Figura 10 / comment_id 453
```

Resultado obligatorio:

```text
INHERITED_TRACE_ROWS = 111
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 113
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true
```

Usa fuentes y blobs gobernantes indicados en este prompt. Registra `HE5 = INCONCLUSIVE` sin convertirla en supported/rejected.

---

# 7. Invariantes de alcance

Verifica:

```text
TABLE_OBJECT_COUNT = 24
TABLE_20_OBJECT_PRESERVED = true
TABLE_20_TBLPR_UNCHANGED = true
TABLE_20_TBLGRID_UNCHANGED = true
TABLES_1_TO_19_UNCHANGED = true
TABLES_21_TO_24_UNCHANGED = true

SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
MEDIA_FILE_COUNT = 16
NEW_MEDIA_FILES = 0
FIGURE_10_MEDIA_BINARY_UNCHANGED = true
FIGURE_11_TO_12_UNCHANGED = true

TRACKED_DELETION_COUNT = 0
4_1_7_UNCHANGED_FROM_I = true
4_2_AND_AFTER_OOXML_UNCHANGED_FROM_I = true
121K_EXECUTED = false
```

No modifiques 4.2, Tabla 21 ni ningún bloque posterior.

---

# 8. QA visual y estructural

Renderiza el DOCX final y revisa desde el inicio de 4.1.8 hasta el comienzo de 4.2.

Verifica:

- redline fragmentario/celda por celda, no reconstrucción masiva de Tabla 20;
- Tabla 20 legible sin clipping ni solapamiento;
- Figura 10 legacy visible y no deformada;
- caption legacy amarillo+tachado;
- línea de supresión claramente visible;
- 4.2 inicia intacta;
- todos los 203 comentarios anclados;
- 12 `SEQ Figura`;
- 0 `w:del`;
- ningún ID interno prohibido visible en el texto nuevo.

---

# 9. Salidas

No sobrescribas I. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_J.docx
g7_thesis_claim_traceability_v0.3_J.csv
```

Publica respuesta oficial en:

```text
writing_prompts_tmp/121J_RESPUESTA_G7_F02_V03_BLOQUE_J_4_1_8_HE5_LIMITES.md
```

Reporta como mínimo:

```text
PROMPT121J_EXECUTION = COMPLETE | STOPPED_PRECONDITION
A051_APPLIED = true|false
A052_APPLIED = true|false
TABLE_20_UPDATED_IN_PLACE = true|false
FIGURE_10_LEGACY_PRESERVED = true|false
FIGURE_10_SUPPRESSION_PROPOSED = true|false
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
INHERITED_TRACE_ROWS = 111
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 113
INHERITED_COMMENT_COUNT = 201
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 203
ALL_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0
4_2_AND_AFTER_UNCHANGED_FROM_I = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS|FAIL
121K_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 4.2 ni ningún bloque posterior.