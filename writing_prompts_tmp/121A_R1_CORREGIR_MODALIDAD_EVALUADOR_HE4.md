# PROMPT121A-R1 — CORRECCIÓN MÍNIMA DE MODALIDAD DEL EVALUADOR HE4

## Rol
Actúa como **IA de Redacción Científica**. Esta ejecución corrige exclusivamente un hallazgo puntual de la auditoría externa del Bloque 121A. No reejecutes el bloque completo ni avances a 121B.

## Estado vinculante
```text
PROMPT121A_EXTERNAL_AUDIT = REVISION_REQUIRED
REVIEWABILITY = PASS
STRUCTURAL_SCOPE = PASS
SCIENTIFIC_NUMERIC_ALIGNMENT = PASS
HE4_EVALUATOR_MODALITY_WORDING = REVISION_REQUIRED
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Entrada única
Usa exclusivamente:
```text
Molleapasa_gv_G7F02_REVIEW_V03_A.docx
SHA256 = 1fd31c674b12caea059adf722ef0530c4974880dd1d903c7b1df9ef9abd50505
SIZE_BYTES = 4170545
```

y su trazabilidad:
```text
g7_thesis_claim_traceability_v0.3_A.csv
SHA256 = d0da815a18e02ec306346e06864446df3696fd15240ed71f86670c1ffe80e713
SIZE_BYTES = 8228
```

Si no coinciden exactamente, STOP.

## Hallazgo a corregir
La fuente científica gobernante de HE4 registra:
```text
evaluator_identifier = independent_ai_reviewer_01
evaluator_modality = AI_EXPERT_ROLE
human_scoring = false
llm_as_judge = true
```

Por tanto, la formulación visible:
```text
"revisor independiente asistido por IA bajo un rol experto"
```
es ambigua porque puede interpretarse como un revisor humano asistido por IA. La fuente indica que el evaluador era de IA y que no hubo puntuación humana.

Fuente gobernante:
```text
outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_he4_joint_jk_assessment_v0.2.json
```

## Alcance EXCLUSIVO
Corrige únicamente las dos formulaciones visibles siguientes:

### 1. Tabla 1 — VD3, columna Técnica/fuente
Sustituye únicamente el fragmento nuevo que actualmente dice:
```text
evaluación cualitativa mediante una rúbrica aplicada a 50 fichas por un revisor independiente asistido por IA bajo un rol experto; no correspondió a evaluación humana.
```
por:
```text
evaluación cualitativa mediante una rúbrica aplicada a 50 fichas por un evaluador independiente de inteligencia artificial, configurado bajo un rol experto; no hubo puntuación humana.
```

### 2. Tabla 2 — fila HE4, columna Técnicas
Sustituye únicamente el fragmento nuevo que actualmente dice:
```text
evaluación cualitativa mediante una rúbrica de verificabilidad, trazabilidad y concordancia evidencia-justificación aplicada a 50 fichas por un revisor independiente asistido por IA bajo un rol experto; no correspondió a evaluación humana.
```
por:
```text
evaluación cualitativa mediante una rúbrica de verificabilidad, trazabilidad y concordancia evidencia-justificación aplicada a 50 fichas por un evaluador independiente de inteligencia artificial, configurado bajo un rol experto; no hubo puntuación humana.
```

## Marcado de revisión
Preserva el esquema vigente:
- el texto anterior del baseline ya tachado+amarillo permanece intacto;
- sustituye solo el texto nuevo amarillo correspondiente a estas dos formulaciones;
- el nuevo texto corregido sigue amarillo y no tachado;
- no añadas otra capa de tachado para el texto de V03_A que se corrige: esta R1 es corrección técnica del candidato de revisión, no una nueva ronda de cambios científicos para el autor.

## Comentarios y trazabilidad
Actualiza únicamente los comentarios asociados a:
```text
comment_id = 347
comment_id = 350
```
para que describan inequívocamente que:
- el evaluador fue un evaluador independiente de IA;
- operó bajo una rúbrica de rol experto;
- no hubo puntuación humana;
- esto constituye una limitación de modalidad respecto del protocolo previsto.

Mantén los seis encabezados obligatorios en español.

Actualiza únicamente las filas:
```text
G7F02-V03A-005
G7F02-V03A-008
```
del CSV para reflejar la nueva formulación. Las otras 12 filas deben quedar semánticamente idénticas.

## Prohibiciones
No modifiques:
- ninguna otra celda, párrafo, tabla o sección;
- ningún número científico;
- comentarios distintos de 347 y 350;
- las hipótesis;
- A073/A074;
- 3.5 en adelante;
- figuras;
- listas;
- GitHub fuera de la respuesta de ejecución.

## Salidas
Genera:
```text
Molleapasa_gv_G7F02_REVIEW_V03_A_R1.docx
g7_thesis_claim_traceability_v0.3_A_R1.csv
```

Renderiza y revisa únicamente las páginas donde aparecen las dos celdas modificadas.

Publica:
```text
writing_prompts_tmp/121A_R1_RESPUESTA_CORREGIR_MODALIDAD_EVALUADOR_HE4.md
```

Incluye al menos:
```text
PROMPT121A_R1_EXECUTION
INPUT_SHA256
OUTPUT_SHA256
TRACE_INPUT_SHA256
TRACE_OUTPUT_SHA256
VISIBLE_TEXT_LOCATIONS_CHANGED = 2
COMMENTS_CHANGED = 2
TRACE_ROWS_CHANGED = 2
OTHER_VISIBLE_CHANGES = 0
OTHER_COMMENT_CHANGES = 0
OTHER_TRACE_ROW_CHANGES = 0
HE4_EVALUATOR_MODALITY_WORDING = CORRECTED
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Detente. No ejecutes 121B.