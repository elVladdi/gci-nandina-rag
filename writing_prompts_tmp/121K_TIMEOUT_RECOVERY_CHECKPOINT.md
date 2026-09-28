# 121K — Recuperación de checkpoint tras timeout de streaming

## 0. Actor y alcance

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

Este prompt NO autoriza reejecutar 121K, NO autoriza aplicar correcciones nuevas y NO autoriza ejecutar 121K-R1. Su único objetivo es **recuperar y preservar el checkpoint ya producido por la ejecución interrumpida del 121K original** después de un timeout de streaming de ChatGPT.

No eres CODEX. No eres la IA Experimental. No edites contenido científico ni editorial. No hagas búsqueda web. No recalcules métricas. No modifiques el repositorio salvo lo expresamente indicado en este prompt. No ejecutes A061, A073–A082, 4.3, 121L ni ningún bloque posterior.

Contexto:

```text
SOURCE_EXECUTION_PROMPT = writing_prompts_tmp/121K_EJECUTAR_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
SOURCE_EXECUTION_COMMIT = 5f60b8bf116b5d638ad65b69e4d603a61e40e072
SOURCE_EXECUTION_STATUS = INTERRUPTED_BY_CHATGPT_STREAM_TIMEOUT / FORMAL_COMPLETION_NOT_CONFIRMED
121J_EXTERNAL_AUDIT = PASS
121K_R1_EXISTS = true
121K_R1_EXECUTION = NOT_AUTHORIZED_BY_THIS_RECOVERY_PROMPT
```

---

## 1. Regla principal: NO REEJECUTAR

No vuelvas a abrir J para repetir A053–A060.

No rehagas 4.2.

No intentes completar cambios faltantes.

No repitas comentarios ni filas de trazabilidad.

No pulses/reproduzcas lógica equivalente a “retry execution”.

Tu tarea es solo inspeccionar el estado persistente que haya quedado en el entorno de la ejecución interrumpida y devolverlo para auditoría externa.

---

## 2. Buscar checkpoint existente

Busca únicamente artefactos ya existentes producidos por la ejecución interrumpida, con prioridad para:

```text
Molleapasa_gv_G7F02_REVIEW_V03_K.docx
g7_thesis_claim_traceability_v0.3_K.csv
writing_prompts_tmp/121K_RESPUESTA_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
```

También puedes identificar artefactos temporales de renderizado o QA ya creados, pero NO los regeneres.

Si no existe DOCX K ni CSV K, devuelve:

```text
CHECKPOINT_RECOVERY = NO_PERSISTED_K_ARTIFACTS_FOUND
RECOVERY_ACTION = STOPPED_PRECONDITION
```

y detente.

Si existe solo uno de los dos artefactos principales, devuelve:

```text
CHECKPOINT_RECOVERY = PARTIAL_ARTIFACT_SET
RECOVERY_ACTION = STOPPED_PRECONDITION
```

preserva y entrega el artefacto existente sin modificarlo, e informa cuál falta.

---

## 3. Inspección de solo lectura

Para cada artefacto K encontrado:

### DOCX K
- calcula SHA-256;
- reporta tamaño en bytes;
- verifica que el ZIP/OOXML abre correctamente;
- reporta, sin modificar: número de tablas, comentarios, `SEQ Figura`, archivos de medios, `w:del` y `w:ins`;
- identifica si Tabla 21 existe y su dimensión observable;
- identifica si 4.3 existe y permanece después de 4.2;
- NO corrijas nada.

### CSV K
- calcula SHA-256;
- reporta tamaño en bytes;
- reporta número de filas de datos;
- verifica si las primeras 113 filas heredadas permanecen como prefijo byte-idéntico al CSV J si el CSV J sigue disponible en el entorno;
- identifica cuántas filas nuevas K existen y sus `plan_id`/`comment_id` observables;
- NO añadas ni elimines filas.

### Respuesta oficial local no publicada
Si existe una respuesta 121K local que no llegó a Git, preserva su contenido y entrégala como artefacto separado. No la publiques como “COMPLETE” por tu cuenta.

---

## 4. Estado de acciones observado

Sin editar nada, clasifica cada acción según evidencia material encontrada:

```text
A053 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
A054 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
A055 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
A056 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
A057 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
A058 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
A059 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
A060 = COMPLETE_OBSERVED | PARTIAL_OBSERVED | NOT_OBSERVED | UNKNOWN
```

No conviertas esta clasificación en auditoría externa ni PASS científico. Es únicamente inventario de checkpoint.

---

## 5. Control de contaminación accidental

Reporta únicamente si observas evidencia de que durante la ejecución interrumpida se modificó algo fuera de A053–A060, en particular:

- A061 o posteriores;
- A073–A082;
- 4.3 o posteriores;
- Tabla 22 o posteriores;
- Figura 11 o posteriores;
- Lista de Tablas, Lista de Figuras o índice;
- nuevas referencias bibliográficas;
- nueva búsqueda web incorporada al manuscrito.

No corrijas ninguna contaminación. Solo repórtala.

---

## 6. Entrega obligatoria

Si los artefactos K existen, **adjúntalos/entrégalos tal como están** para auditoría externa:

```text
Molleapasa_gv_G7F02_REVIEW_V03_K.docx
g7_thesis_claim_traceability_v0.3_K.csv
```

Si existe respuesta local parcial, entrégala también.

Devuelve un reporte final con este formato mínimo:

```text
121K_TIMEOUT_RECOVERY = COMPLETE | STOPPED_PRECONDITION
SOURCE_EXECUTION = 121K_ORIGINAL
SOURCE_EXECUTION_FORMAL_STATUS = INTERRUPTED_BY_STREAM_TIMEOUT
DOCX_K_FOUND = true|false
DOCX_K_SHA256 = <hash|NA>
DOCX_K_SIZE = <bytes|NA>
CSV_K_FOUND = true|false
CSV_K_SHA256 = <hash|NA>
CSV_K_SIZE = <bytes|NA>
CSV_K_ROWS = <n|NA>
LOCAL_121K_RESPONSE_FOUND = true|false
A053_STATUS = ...
A054_STATUS = ...
A055_STATUS = ...
A056_STATUS = ...
A057_STATUS = ...
A058_STATUS = ...
A059_STATUS = ...
A060_STATUS = ...
OUT_OF_SCOPE_MODIFICATION_EVIDENCE = NONE | OBSERVED | UNKNOWN
NO_EDITS_PERFORMED_BY_RECOVERY = true
121K_R1_EXECUTED = false
121L_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente después de entregar el checkpoint. No continúes la tesis y no emitas PASS/FAIL de auditoría externa.