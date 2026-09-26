# PROMPT121D_R1 — Corrección localizada A035: reporte DAM-disjoint en 4.1.1 y Tabla 10

## Rol y estado

Actúa como **IA de Redacción Científica**. Corrige exclusivamente el hallazgo de la auditoría externa de Prompt121D. No eres CODEX y no debes ejecutar 121E ni ningún bloque posterior.

```text
PROMPT121D_EXTERNAL_AUDIT = REVISION_REQUIRED
PROMPT121D_BLOCK_D = REVISION_REQUIRED / NOT_APPROVED
NUMERICAL_CORRECTION_REQUIRED = false
RESULT_REPORTING_CORRECTION_REQUIRED = true
TARGETED_REVISION_REQUIRED = true
FULL_RERUN_REQUIRED = false
A036 = VERIFIED / KEEP
NEXT_BLOCK_121E_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría vinculante:

```text
writing_prompts_tmp/121D_AUDITORIA_EXTERNA_REVISION_REQUIRED.md
commit = aefaadab1718ea906a0419c36ea2fca04c2358ca
```

## Entrada única

Usa exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_D.docx
SHA256 = cedc46234c81a94626524d21847b27e5f59bbffb94b8de9bff323498c8c3d575
SIZE_BYTES = 4194621
```

Trazabilidad acumulativa:

```text
g7_thesis_claim_traceability_v0.3_D.csv
SHA256 = 924f6220e8114bce6f8465e8f2c403cc8e9ebe2a3506136dd4d0533820974828
TRACE_ROWS_INHERITED = 84
```

Recalcula ambos hashes antes de editar. Si no coinciden, STOP.

## Alcance exclusivo

Corrige únicamente **A035** en:

- el párrafo inmediato de `4.1.1. Resultados de curación, integridad y partición de las series` situado después de Tabla 10;
- las celdas de `Lectura` de las tres filas de partición de `Tabla 10`:
  - Banco histórico;
  - Conjunto de desarrollo;
  - Conjunto de evaluación.

No modifiques ninguna otra celda de Tabla 10.

No modifiques:

- 3.8 ni ninguna sección anterior;
- 4.1.2 ni Tabla 11;
- 4.1.3 ni posteriores;
- Figura 3 ni ninguna otra figura;
- listas preliminares;
- bibliografía;
- conclusiones;
- recomendaciones.

`A036` permanece **VERIFY / KEEP** y no requiere nueva verificación ni nuevo comentario salvo que detectes una alteración accidental de D; en ese caso STOP.

## Fuente científica vinculante

Usa exclusivamente para esta corrección:

```text
data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
blob = bcb02c9c3493235a6f80991158c5b24fa7c04510
```

Hechos congelados:

```text
ANALYSIS_UNIT = SERIE
GROUPING_FIELD = DECLARACION / DAM
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
FULL_ASSIGNMENT = 4106
CROSS_SPLIT_DAM_OVERLAP = 0
CROSS_SPLIT_ID_UNICO_OVERLAP = 0
EVAL_CASES_WITH_HISTORICAL_SUPPORT = 1056 / 1056
EVAL_CODES_WITH_HISTORICAL_SUPPORT = 42 / 42
SPLIT = DAM-DISJOINT v0.2
```

No recalcules ninguna cifra.

## Corrección obligatoria 1 — párrafo de 4.1.1

El estado D ya contiene cifras correctas de series y NANDINA, pero solo declara ausencia de solapamiento de `id_unico`. Corrige el fragmento mínimo para que el resultado final haga explícito que:

1. la partición final v0.2 se materializó mediante asignación explícita por DAM, manteniendo cada DAM íntegramente en una sola partición;
2. histórico, desarrollo y evaluación reúnen respectivamente `28`, `6` y `67` DAM;
3. no hubo solapamiento de DAM ni de `id_unico` entre las tres particiones;
4. esta condición corresponde al benchmark interno y no implica muestreo probabilístico ni validez externa.

No conviertas el resultado en una explicación extensa del método. El procedimiento ya está descrito en el Capítulo 3.

Mantén intactas las cifras correctas ya introducidas en D:

```text
2950 / 100 / 1056 series
66 / 9 / 42 NANDINA
```

## Corrección obligatoria 2 — Tabla 10

Conserva el objeto, número, título, estructura, bordes, anchos y todas las filas existentes.

Modifica únicamente las celdas `Lectura` de las tres particiones para incorporar DAM + NANDINA:

```text
Banco histórico
Lectura vigente objetivo = 28 DAM; 66 códigos NANDINA distintos

Conjunto de desarrollo
Lectura vigente objetivo = 6 DAM; 9 códigos NANDINA distintos

Conjunto de evaluación
Lectura vigente objetivo = 67 DAM; 42 códigos NANDINA distintos
```

Puedes ajustar mínimamente la puntuación o sintaxis para que sea natural dentro de la tabla, pero no cambiar los valores ni añadir interpretación adicional.

No reconstruyas la Tabla 10.

## Convención de revisión

```text
ANTERIOR_MODIFICADO = amarillo + tachado + visible
NUEVO = amarillo + no tachado + visible
SIN_CAMBIO = normal
```

Aplica la convención únicamente a los cuatro cambios reales de R1:

- un cambio de párrafo;
- tres celdas de Tabla 10.

No vuelvas a marcar ni a comentar los nueve cambios ya heredados de Prompt121D.

No uses `w:del`.

## Comentarios

Añade exactamente **cuatro comentarios nuevos**, uno por cada cambio real de R1. Cada comentario debe contener íntegramente en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Los comentarios deben explicar que la corrección completa el reporte de la partición DAM-disjoint y no modifica los tamaños ya aprobados.

No introduzcas en prosa visible nombres de prompts, fichas, gates, commits, IDs de claims ni estados administrativos.

## Trazabilidad

Preserva byte-semánticamente las 84 filas heredadas de D, en el mismo orden.

Añade exactamente cuatro filas nuevas:

```text
G7F02-V03D-R1-001
G7F02-V03D-R1-002
G7F02-V03D-R1-003
G7F02-V03D-R1-004
```

Vinculación esperada:

```text
R1-001 = párrafo 4.1.1 / DAM-disjoint + 28/6/67 DAM + zero overlap
R1-002 = Tabla 10 / Banco histórico / 28 DAM + 66 NANDINA
R1-003 = Tabla 10 / Desarrollo / 6 DAM + 9 NANDINA
R1-004 = Tabla 10 / Evaluación / 67 DAM + 42 NANDINA
```

No agregues filas por verificaciones sin modificación.

## Integridad heredada de comentarios

La entrada tiene 176 comentarios correctamente anclados. Exige:

```text
INHERITED_COMMENT_COUNT = 176
INHERITED_COMMENT_TEXT_CHANGED = 0
INHERITED_ORPHAN_COMMENT_IDS = NONE
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
COMMENTS_418_426_UNCHANGED = true
```

Los cuatro comentarios nuevos también deben quedar anclados. Si cualquier comentario heredado cambia de texto o queda huérfano, STOP.

## Salidas

Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_D_R1.docx
g7_thesis_claim_traceability_v0.3_D_R1.csv
```

No generes V03 final.

## QA obligatorio

Reporta al menos:

```text
INPUT_DOCX_SHA256
OUTPUT_DOCX_SHA256
INPUT_TRACE_SHA256
OUTPUT_TRACE_SHA256
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
INHERITED_TRACE_ROWS = 84
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 4
INHERITED_COMMENT_COUNT = 176
COMMENTS_ADDED = 4
A035_DAM_COUNTS_REPORTED = true
A035_DAM_DISJOINT_REPORTED = true
A035_CROSS_SPLIT_DAM_OVERLAP_ZERO_REPORTED = true
A035_CROSS_SPLIT_ID_UNICO_OVERLAP_ZERO_PRESERVED = true
A036_VISIBLE_CHANGE = false
TABLE_11_CHANGED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
COMMENTS_418_426_UNCHANGED = true
```

Renderiza e inspecciona únicamente las páginas afectadas por 4.1.1 y Tabla 10, más una página de frontera antes y después. La frontera posterior debe permitir confirmar que 4.1.2 y Tabla 11 permanecen sin cambios.

## Prohibiciones

- No corregir otras secciones aunque observes oportunidades de mejora.
- No modificar 4.1.2 ni Tabla 11.
- No ejecutar 121E.
- No modificar figuras.
- No introducir nuevas métricas, inferencia, CI, valores p o referencias.
- No reinterpretar la ausencia de solapamiento como independencia estadística completa, representatividad probabilística o validez externa.
- No reabrir EXP12.

## Respuesta oficial

Publica:

```text
writing_prompts_tmp/121D_R1_RESPUESTA_CORREGIR_REPORTE_DAM_SPLIT_A035.md
```

en `codex/prompts-temporary` y detente con:

```text
PROMPT121D_R1_EXECUTION = COMPLETE
A035_DAM_COUNTS_REPORTED = true
A035_DAM_DISJOINT_REPORTED = true
A035_CROSS_SPLIT_DAM_OVERLAP_ZERO_REPORTED = true
A035_CROSS_SPLIT_ID_UNICO_OVERLAP_ZERO_PRESERVED = true
A036_VISIBLE_CHANGE = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
ALL_COMMENT_IDS_ANCHORED = true
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

No avances a 121E.