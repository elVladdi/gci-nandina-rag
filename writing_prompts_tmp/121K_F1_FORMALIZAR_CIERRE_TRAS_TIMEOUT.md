# PROMPT121K-F1 — Formalizar cierre de 121K recuperado tras timeout

## 0. Actor, propósito y prohibiciones

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

Este prompt es exclusivamente de **formalización documental del cierre de 121K**. No autoriza nuevas ediciones de tesis, no autoriza reejecutar A053–A060, no autoriza ejecutar 121K-R1 y no autoriza ningún bloque posterior.

No eres CODEX. No eres la IA Experimental.

```text
MODE = FORMALIZATION_ONLY / READ_ONLY_ON_K_ARTIFACTS
DOCX_EDITING = FORBIDDEN
CSV_EDITING = FORBIDDEN
REEXECUTE_121K = FORBIDDEN
EXECUTE_121K_R1 = FORBIDDEN
EXECUTE_A061 = FORBIDDEN
EXECUTE_A073_TO_A082 = FORBIDDEN
EXECUTE_4_3 = FORBIDDEN
EXECUTE_121L = FORBIDDEN
```

La auditoría externa gobernante es:

```text
writing_prompts_tmp/121K_AUDITORIA_EXTERNA_REVISION_FORMALIZACION.md
commit = 3c63de5306867f04a9f76fbf67bd4434f08914f5
status = REVISION_REQUIRED_FORMALIZATION_ONLY
scientific/editorial/structural/traceability/visual = PASS
```

El resultado material de A053–A060 ya fue auditado y **no requiere corrección de DOCX ni CSV**. El único defecto pendiente es que el timeout impidió persistir la respuesta oficial de ejecución.

---

## 1. Artefactos K inmutables

Localiza y verifica en modo de solo lectura exactamente estos artefactos recuperados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_K.docx
SHA256 = 93cad8010e02e1cdbae092bcba93e8d1f32310baf2e693554e1c3ae54cc2c279
SIZE = 4680083

g7_thesis_claim_traceability_v0.3_K.csv
SHA256 = 30438bef703edc512bcf88db62f1dc3340ac4666a3f00c98f716217df649ffd1
SIZE = 116276
ROWS = 121
```

Si cualquiera de estas identidades no coincide exactamente, devuelve:

```text
PROMPT121K_F1_FORMALIZATION = STOPPED_PRECONDITION
K_ARTIFACT_IDENTITY_MATCH = false
```

y detente sin modificar nada.

No regeneres los artefactos. No los vuelvas a guardar. No los normalices. No alteres metadatos. No re-renderices salvo lectura estrictamente necesaria para confirmar que son los mismos archivos; no sustituyas los hashes congelados.

---

## 2. Estado auditado que debes transcribir, no reinterpretar

La respuesta formal debe reflejar exactamente este estado observado y auditado:

```text
SOURCE_EXECUTION = 121K_ORIGINAL
SOURCE_EXECUTION_PROMPT = writing_prompts_tmp/121K_EJECUTAR_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
SOURCE_EXECUTION_COMMIT = 5f60b8bf116b5d638ad65b69e4d603a61e40e072
SOURCE_EXECUTION_INTERRUPTED_BY_STREAM_TIMEOUT = true
CHECKPOINT_RECOVERY_PERFORMED = true
CHECKPOINT_RECOVERY_WAS_READ_ONLY = true
NO_REEXECUTION_AFTER_TIMEOUT = true

A053_APPLIED = true
A054_APPLIED = true
A055_APPLIED = true
A056_APPLIED = true
A057_APPLIED = true
A058_APPLIED = true
A059_APPLIED = true
A060_APPLIED = true
TABLE_21_UPDATED_IN_PLACE = true
TABLE_21_ROW_COUNT = 7
TABLE_21_COLUMN_COUNT = 4
INHERITED_TRACE_ROWS = 113
NEW_TRACE_ROWS_ADDED = 8
TOTAL_TRACE_ROWS = 121
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true
INHERITED_COMMENT_COUNT = 203
COMMENTS_ADDED = 8
TOTAL_COMMENT_COUNT = 211
ALL_COMMENT_IDS_ANCHORED = true
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS
EXTERNAL_SCIENTIFIC_AUDIT = PASS
EXTERNAL_EDITORIAL_AUDIT = PASS
EXTERNAL_STRUCTURAL_AUDIT = PASS
EXTERNAL_TRACEABILITY_AUDIT = PASS
EXTERNAL_VISUAL_AUDIT = PASS
121K_R1_EXECUTED = false
121L_EXECUTED = false
```

No recalcules ciencia y no agregues nuevas afirmaciones. No conviertas esta formalización en una nueva auditoría.

---

## 3. Respuesta oficial que debes publicar

Crea exclusivamente este archivo Markdown en la rama `codex/prompts-temporary`:

```text
writing_prompts_tmp/121K_RESPUESTA_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
```

La respuesta debe explicar de forma explícita que:

1. la ejecución material del 121K original alcanzó A053–A060 antes del timeout;
2. el stream se interrumpió antes de persistir la respuesta oficial;
3. la recuperación fue estrictamente de solo lectura y no modificó K;
4. la IA Experimental auditó los artefactos recuperados y determinó PASS científico, editorial, estructural, de trazabilidad y visual;
5. no fue necesario ejecutar 121K-R1 ni corregir DOCX/CSV;
6. este archivo formaliza documentalmente el cierre recuperado, sin reejecución;
7. 121L permanece **NO EJECUTADO** y su autorización corresponde únicamente a una confirmación posterior de la IA Experimental.

Incluye obligatoriamente este bloque, con los valores exactos:

```text
PROMPT121K_EXECUTION = COMPLETE
COMPLETION_BASIS = RECOVERED_CHECKPOINT_EXTERNALLY_AUDITED
STREAM_TIMEOUT_OCCURRED = true
NO_REEXECUTION_PERFORMED = true
A053_APPLIED = true
A054_APPLIED = true
A055_APPLIED = true
A056_APPLIED = true
A057_APPLIED = true
A058_APPLIED = true
A059_APPLIED = true
A060_APPLIED = true
TABLE_21_UPDATED_IN_PLACE = true
INHERITED_TRACE_ROWS = 113
NEW_TRACE_ROWS_ADDED = 8
TOTAL_TRACE_ROWS = 121
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true
INHERITED_COMMENT_COUNT = 203
COMMENTS_ADDED = 8
TOTAL_COMMENT_COUNT = 211
ALL_COMMENT_IDS_ANCHORED = true
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS
EXTERNAL_ARTIFACT_AUDIT = PASS
DOCX_K_SHA256 = 93cad8010e02e1cdbae092bcba93e8d1f32310baf2e693554e1c3ae54cc2c279
DOCX_K_SIZE = 4680083
CSV_K_SHA256 = 30438bef703edc512bcf88db62f1dc3340ac4666a3f00c98f716217df649ffd1
CSV_K_SIZE = 116276
CSV_K_ROWS = 121
121K_R1_EXECUTED = false
121L_EXECUTED = false
EXTERNAL_CLOSURE_CONFIRMATION = PENDING_BY_IA_EXPERIMENTAL
```

No declares `121L_AUTHORIZED = true`; esa decisión no pertenece a la IA de Redacción.

---

## 4. Control de no modificación

Antes de terminar, vuelve a calcular únicamente los hashes de lectura del DOCX K y CSV K. Deben seguir siendo exactamente:

```text
DOCX_K_SHA256_AFTER_FORMALIZATION = 93cad8010e02e1cdbae092bcba93e8d1f32310baf2e693554e1c3ae54cc2c279
CSV_K_SHA256_AFTER_FORMALIZATION = 30438bef703edc512bcf88db62f1dc3340ac4666a3f00c98f716217df649ffd1
K_ARTIFACTS_MODIFIED_BY_FORMALIZATION = false
```

Si cambió cualquiera de los dos, no publiques un cierre correcto: reporta `STOPPED_PRECONDITION` y conserva evidencia del conflicto.

---

## 5. Entrega y parada

Devuelve:

```text
PROMPT121K_F1_FORMALIZATION = COMPLETE | STOPPED_PRECONDITION
OFFICIAL_121K_RESPONSE_PUBLISHED = true|false
K_ARTIFACT_IDENTITY_MATCH = true|false
K_ARTIFACTS_MODIFIED_BY_FORMALIZATION = false
121K_R1_EXECUTED = false
121L_EXECUTED = false
EXTERNAL_CLOSURE_CONFIRMATION = PENDING_BY_IA_EXPERIMENTAL
```

Si se publicó la respuesta, informa el commit exacto y el blob del archivo Markdown.

Detente. No ejecutes 121L, A061, A073–A082, 4.3 ni ningún bloque posterior.