# PROMPT121C — G7-F02 V03, BLOQUE C: MÉTODOS DE ANÁLISIS 3.8

## Rol y estado

Actúa como **IA de Redacción Científica**. Continúa acumulativamente desde el Bloque B/R1 aprobado. No eres CODEX y no debes ejecutar bloques posteriores.

```text
PROMPT121B_R1_EXTERNAL_AUDIT = PASS
PROMPT121B_BLOCK_B = APPROVED
NEXT_BLOCK_121C_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría vinculante:

```text
writing_prompts_tmp/121B_R1_AUDITORIA_EXTERNA_PASS.md
commit = 3f4af4615c4d8ec2c744d61e6d6d11910886e38f
```

## Entrada única

Usa exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_B_R1.docx
SHA256 = 875194ffb8b7413ffba8cc6a5136e6496763ce5552af0f12879fcc30044a18e3
SIZE_BYTES = 4178136
```

Trazabilidad acumulativa:

```text
g7_thesis_claim_traceability_v0.3_B_R1.csv
SHA256 = 4f08e0e3911099afd9fdfb4ae6de890f9ad0f6d70d876f7d80a7aa7c93e8fa94
TRACE_ROWS_INHERITED = 42
```

Recalcula ambos hashes. Si no coinciden, STOP.

## Alcance exclusivo

Ejecuta solo las filas de Prompt119:

```text
A026 A027 A028 A029 A030 A031 A032 A033 A034 A076 A077
```

Archivo vinculante:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
commit = 583138f94646b1e84de1c28f32342e59f82988a3
```

Puedes modificar únicamente:

- 3.8.1 a 3.8.7;
- Tabla 8;
- Tabla 9;
- A076: referencia `Tabla 9` → `Tabla 8` en 3.8.1;
- A077: referencia `Tabla 10` → `Tabla 9` en 3.8.7.

NO modifiques 3.7.7 ni secciones anteriores, Capítulo 4, listas preliminares, figuras, bibliografía o conclusiones.

## Fuentes científicas

Antes de redactar, lee:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.md
docs/writing/group7/g7_writing_source_freeze_v0.1.json
```

Usa los **artefactos primarios congelados** que el JSON asigna a A026–A034; el source freeze es contrato de precedencia, no sustituto de esas fuentes.

Hechos vinculantes que deben preservarse:

```text
HG  = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE

HE2:
ANALYSIS_UNIT = SERIE
DEPENDENCY_GROUP = DAM
BOOTSTRAP_REPLICATES = 10000
15 contrastes primarios con IC 99%
1 contraste Recall@200 - Recall@100 con IC 95%
P_VALUES = none
alcance = benchmark interno fijo de clase 87

HE3:
ranking histórico invariante en 1056/1056 casos;
reordenamiento LLM = diagnóstico, no flujo principal.

HE4:
controles estructurales/Top-3 = 50/50;
evaluación cualitativa auditable = 28/50;
22/50 no auditables;
0 hard violations;
evaluador = IA independiente bajo rol experto, sin puntuación humana;
preservar las limitaciones por discrepancia del esquema del prompt y desviación de modalidad del evaluador, redactadas en español natural.

HE5:
calidad descriptiva = NOT_ESTIMABLE;
proximidad jerárquica = DESCRIPTIVE_ONLY;
precedentes = DESCRIPTIVE_ONLY;
validez interna = DOCUMENTED_LIMITATION.

EXP11A = sensibilidad conjunta tamaño-composición / NO causal.
EXP11B = descriptivo / diez pares observados / NO inferencia a superpoblación de semillas.
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN.
```

## Reglas de redacción

### 3.8.1 + Tabla 8

- Distingue claramente **inferencia primaria de HE2** del resto de análisis descriptivos.
- Actualiza Tabla 8 por celdas, no la reconstruyas.
- Elimina esquemas legacy de buckets/scores que ya no gobiernen.
- A076 debe quedar aplicado.

### 3.8.2 — HE1

- Describe cómo se analiza integridad/procedencia/reproducibilidad.
- **No declares HE1 respaldada, rechazada ni inconclusa.**
- La evidencia de reproducibilidad tiene limitaciones y no constituye disposición formal terminal.

### 3.8.3 — HE2

- Describe los comparadores y el procedimiento realmente ejecutado.
- Usa IC 99%/95% según corresponda; ningún valor p.
- No conviertas superioridad de recuperación histórica en exactitud global del RAG.

### 3.8.4 — HE3

- Separa integración histórica-normativa del reordenador diagnóstico.
- La evidencia normativa no reordena el ranking histórico.

### 3.8.5 — HE4

- Separa controles estructurales de evaluación cualitativa.
- Explica la modalidad real del evaluador sin ambigüedad humana.
- Auditabilidad no equivale a corrección jurídica.

### 3.8.6 — HE5 y sensibilidades

- HE5 permanece inconclusa.
- No inventes umbrales para “precedentes insuficientes”.
- EXP11A: sensibilidad conjunta, no efecto causal aislado del tamaño.
- EXP11B: solo diez pares observados; descriptivo.
- EXP12: cerrado sin recuperación; efecto de diversidad no estimable.

### 3.8.7 + Tabla 9

- Sustituye la regla decisional uniforme legacy por una regla de reporte compatible con las disposiciones anteriores.
- HG y HE1 quedan sin disposición formal terminal.
- Actualiza solo las filas materialmente afectadas de Tabla 9.
- A077 debe quedar aplicado.

## Convención de revisión

```text
ANTERIOR_MODIFICADO = amarillo + tachado + visible
NUEVO = amarillo + no tachado
SIN_CAMBIO = normal
```

Edita el fragmento mínimo posible. No uses `w:del`. No dupliques tablas.

## Comentarios

Solo donde exista cambio real. Cada comentario nuevo, íntegramente en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

No introduzcas en prosa visible G1–G8, fichas, prompts, gates, commits, claim IDs ni estados administrativos.

## Trazabilidad

Preserva byte-semánticamente las 42 filas heredadas. Añade solo filas por cambios reales de C:

```text
G7F02-V03C-001 ...
```

No generes filas para verificaciones sin modificación.

## Integridad heredada de comentarios

La entrada tiene 134 comentarios correctamente anclados. Al cerrar exige:

```text
INHERITED_COMMENT_COUNT = 134
INHERITED_ORPHAN_COMMENT_IDS = NONE
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
```

Los comentarios nuevos deben quedar también anclados. Si cualquier comentario heredado queda huérfano, STOP y no continúes.

## Salidas

```text
Molleapasa_gv_G7F02_REVIEW_V03_C.docx
g7_thesis_claim_traceability_v0.3_C.csv
```

No generes V03 final.

## QA obligatorio, localizado

Reporta al menos:

```text
INPUT_DOCX_SHA256
OUTPUT_DOCX_SHA256
INPUT_TRACE_SHA256
OUTPUT_TRACE_SHA256
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
INHERITED_TRACE_ROWS = 42
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED
A076_APPLIED = true
A077_APPLIED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
```

Renderiza e inspecciona **solo las páginas afectadas por 3.8 y una página de frontera antes/después**. No renderices el documento completo salvo que sea técnicamente necesario.

## Prohibiciones

No introduzcas nueva ciencia, nuevos p-values, nuevas métricas, nuevos IC, nuevas referencias, generalización externa, corrección jurídica, decisión formal de HG/HE1 ni reapertura de EXP12.

No ejecutes 121D ni ningún bloque posterior.

## Respuesta oficial

Publica:

```text
writing_prompts_tmp/121C_RESPUESTA_G7_F02_V03_BLOQUE_C_ANALISIS_3_8.md
```

en `codex/prompts-temporary` y detente con:

```text
PROMPT121C_EXECUTION = COMPLETE
A076_APPLIED = true
A077_APPLIED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
ALL_COMMENT_IDS_ANCHORED = true
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```
