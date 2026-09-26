# PROMPT121A — G7-F02 V03, BLOQUE A: METODOLOGÍA 3.1–3.4

## Rol
Actúa como **IA de Redacción Científica**. Este prompt sustituye operativamente a Prompt120, que queda **SUPERSEDED_FOR_EXECUTION por ejecución modular** debido a timeouts. No ejecutes Prompt120 completo.

## Estado
```text
PROMPT119_EXTERNAL_AUDIT = PASS
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
V01_V02 = REJECTED / DO_NOT_USE
G7_F03_AUTHORIZED = false
```

## Entrada única
Parte exclusivamente de:
```text
Molleapasa_gv_vigente_2026-09-22.docx
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
```
Verifica hash antes de editar. No uses V01/V02 como fuente.

Usa como plan vinculante:
```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
commit = 583138f94646b1e84de1c28f32342e59f82988a3
```

## Alcance EXCLUSIVO de este bloque
Modifica únicamente:
- 3.1 Hipótesis, variables y matriz de consistencia;
- 3.2 Tipo y diseño de investigación;
- 3.3 Unidad de análisis;
- 3.4 Población de estudio;
- Tablas 1, 2 y 3 solo donde Prompt119 autoriza cambios;
- referencias cruzadas A073 y A074.

Ejecuta exclusivamente las filas de Matriz A de Prompt119 correspondientes a A003–A015 y A073–A074.

NO toques todavía:
- 3.5 en adelante;
- Capítulo 4;
- conclusiones/recomendaciones;
- Lista de Tablas o Lista de Figuras;
- ninguna figura;
- otras referencias cruzadas A075–A082.

## Reglas editoriales mínimas
- Mantén formato/estilo del baseline.
- No reconstruyas el DOCX.
- No dupliques tablas.
- Cambios en tablas: fragmento/celda/fila mínima.
- Texto anterior modificado: **amarillo + tachado + visible**.
- Texto nuevo: **amarillo + no tachado**.
- Texto sin cambios: normal.
- No uses `w:del` para ocultar texto.
- Comentarios solo cuando haya cambio real.
- Cada comentario, íntegramente en español, debe contener:
```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```
- Prohibido filtrar G1–G8, fichas, prompts, source freeze, claim IDs, gates, commits o estados administrativos a la prosa visible.
- No crear ciencia, métricas, inferencias, CI, p-values o referencias nuevas.
- Problema, objetivos e hipótesis aprobadas permanecen intactos salvo correcciones expresamente autorizadas por Prompt119.

## Salida acumulativa
Genera:
```text
Molleapasa_gv_G7F02_REVIEW_V03_A.docx
```
Este archivo será la entrada del siguiente bloque. No generes aún la V03 final.

Genera además una trazabilidad parcial:
```text
g7_thesis_claim_traceability_v0.3_A.csv
```
solo para cambios efectivamente aplicados en este bloque.

## Validación local del bloque
Verifica únicamente:
- integridad ZIP del DOCX;
- baseline original no modificado;
- Tablas 1–3 siguen siendo exactamente 3 objetos;
- ninguna sección fuera de 3.1–3.4 fue modificada;
- A073 y A074 aplicadas correctamente;
- 0 términos de gobernanza interna introducidos en el alcance editado;
- comentarios del bloque en español;
- no renderices ni audites visualmente todo el documento: revisa solo páginas afectadas por 3.1–3.4.

## Respuesta
Publica:
```text
writing_prompts_tmp/121A_RESPUESTA_G7_F02_V03_BLOQUE_A.md
```
Incluye:
```text
PROMPT121A_EXECUTION
INPUT_SHA256
OUTPUT_SHA256
OUTPUT_SIZE_BYTES
SECTIONS_MODIFIED
TABLES_1_3_OBJECT_COUNT
A073_APPLIED
A074_APPLIED
COMMENTS_ADDED
TRACE_ROWS_ADDED
OUT_OF_SCOPE_MODIFICATIONS
BASELINE_MODIFIED
G7_F02_STATE
G7_F03_AUTHORIZED
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Terminal esperado:
```text
PROMPT121A_EXECUTION = COMPLETE
OUT_OF_SCOPE_MODIFICATIONS = 0
BASELINE_MODIFIED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Detente. No ejecutes el siguiente bloque hasta auditoría externa.