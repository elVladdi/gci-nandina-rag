# PROMPT121D — G7-F02 V03, BLOQUE D: RESULTADOS 4.1.1–4.1.2

## Rol y estado

Actúa como **IA de Redacción Científica**. Continúa acumulativamente desde el Bloque C aprobado. No eres CODEX y no debes ejecutar bloques posteriores.

```text
PROMPT121C_EXTERNAL_AUDIT = PASS
PROMPT121C_BLOCK_C = APPROVED
NEXT_BLOCK_121D_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría vinculante:

```text
writing_prompts_tmp/121C_AUDITORIA_EXTERNA_PASS.md
commit = 772ba073ea029332c5afe81dbbe75237d6ab74c0
```

## Entrada única

Usa exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_C.docx
SHA256 = 38b2b089a87b973a81be37108a2d303492de8a4a79a3acf99264750c1130deff
SIZE_BYTES = 4193389
```

Trazabilidad acumulativa:

```text
g7_thesis_claim_traceability_v0.3_C.csv
SHA256 = 1ed85863b6a588ef2ce80cbfa05d105f1792de17fead99d2c634fafa19296c1f
TRACE_ROWS_INHERITED = 75
```

Recalcula ambos hashes. Si no coinciden, STOP.

## Alcance exclusivo

Ejecuta solo las filas del plan vinculante:

```text
A035
A036
```

Fuente del plan:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
```

Puedes modificar únicamente:

- `4.1.1. Resultados de curación, integridad y partición de las series`;
- `Tabla 10`;
- `4.1.2. Resultados de estructuración y auditoría del corpus normativo`;
- `Tabla 11`, **solo si la verificación de la fuente primaria confirma una discrepancia real**.

No modifiques:

- 3.8 ni ninguna sección anterior;
- 4.1.3 ni posteriores;
- Figura 3;
- Figuras 4–12;
- listas preliminares;
- bibliografía;
- conclusiones;
- recomendaciones.

La Figura 3 permanece `KEEP`; no requiere comentario si no cambia.

## Fuentes científicas obligatorias

Lee primero:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.md
docs/writing/group7/g7_writing_source_freeze_v0.1.json
```

Sigue las rutas primarias congeladas que el JSON asigna a población, split, curación y corpus normativo. El source freeze es contrato de precedencia, no sustituto de las fuentes primarias.

Para números de resultados utiliza las fuentes primarias y, cuando corresponda, las presentaciones canónicas de Grupo 5. No recalcules métricas ni reconstruyas resultados por inferencia propia.

## Hechos vinculantes para 4.1.1

El resultado final de partición es v0.2 y debe reemplazar el estado legacy del baseline:

```text
CURATED_TOTAL = 4106 series
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM when applicable
SPLIT = DAM-DISJOINT v0.2
CROSS_SPLIT_DAM_OVERLAP = 0
CROSS_SPLIT_ID_UNICO_OVERLAP = 0
```

Preserva los conteos de curación que continúen vigentes únicamente si las fuentes primarias los confirman. No sustituyas los resultados de curación por números deducidos de la diferencia entre conjuntos.

### Tabla 10

- Conserva el objeto y número `Tabla 10`.
- Actualiza por celda/fila, no reconstruyas la tabla completa salvo imposibilidad estructural demostrada.
- Elimina del estado vigente los tamaños legacy `3 000 / 100 / 1 006`.
- La lectura de cada fila debe distinguir curación de partición final.
- No presentes la separación DAM-disjoint como muestreo probabilístico ni como validez externa.

## Regla para 4.1.2 y Tabla 11

`A036` es una **verificación de fuente**, no una autorización automática para modificar.

Antes de tocar una cifra del corpus:

1. identifica en el source freeze la fuente primaria congelada del corpus normativo;
2. verifica los conteos del texto y de Tabla 11 contra esa fuente;
3. si coinciden, deja 4.1.2 y Tabla 11 sin cambios visibles y **no agregues comentario ni fila de trazabilidad**;
4. si existe una discrepancia confirmada, modifica únicamente el fragmento/celda afectado, registra la fuente exacta y explica el cambio en un comentario.

Prohibido actualizar el corpus por memoria, por coherencia aparente o a partir de cifras de otra etapa.

## Reglas de redacción

- El Capítulo 4 reporta resultados, no vuelve a explicar extensamente el método.
- Evita repetir en prosa todos los valores ya visibles en Tabla 10/11.
- Mantén lenguaje de tesis, no lenguaje de gobernanza interna.
- No introduzcas nueva ciencia, inferencia, métricas, CI, valores p ni referencias.
- No conviertas trazabilidad o estructuración del corpus en corrección jurídica.
- No conviertas la ausencia de solapamiento en prueba de generalización externa.

## Convención de revisión

```text
ANTERIOR_MODIFICADO = amarillo + tachado + visible
NUEVO = amarillo + no tachado + visible
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

No introduzcas en prosa visible nombres de fichas, prompts, gates, commits, claim IDs ni estados administrativos.

## Trazabilidad

Preserva byte-semánticamente las 75 filas heredadas. Añade solo filas por cambios reales del Bloque D:

```text
G7F02-V03D-001 ...
```

No generes fila por la verificación de Tabla 11 si no existe modificación visible.

## Integridad heredada de comentarios

La entrada tiene 167 comentarios correctamente anclados. Al cerrar exige:

```text
INHERITED_COMMENT_COUNT = 167
INHERITED_ORPHAN_COMMENT_IDS = NONE
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
```

Preserva también sin cambios los comentarios 385–417 heredados de 121C.

Si cualquier comentario heredado queda huérfano o cambia de texto, STOP y no continúes.

## Salidas

```text
Molleapasa_gv_G7F02_REVIEW_V03_D.docx
g7_thesis_claim_traceability_v0.3_D.csv
```

No generes V03 final.

## QA obligatorio localizado

Reporta al menos:

```text
INPUT_DOCX_SHA256
OUTPUT_DOCX_SHA256
INPUT_TRACE_SHA256
OUTPUT_TRACE_SHA256
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
INHERITED_TRACE_ROWS = 75
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED
A035_APPLIED = true
A036_SOURCE_VERIFICATION = PASS
A036_VISIBLE_CHANGE = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
```

Renderiza e inspecciona solo las páginas afectadas por 4.1.1–4.1.2 y una página de frontera antes/después. No renderices el documento completo salvo necesidad técnica.

## Separación de actores para figuras

Este bloque **no ejecuta trabajo científico-visual**. Las actualizaciones de las Figuras 4–6 del plan (`A039`, `A040`, `A043`) quedan diferidas para un bloque posterior bajo la **IA Diseñadora y Auditora de Figuras Científicas**, utilizando exclusivamente los artefactos G6 ya aprobados. No regeneres ni reemplaces figuras aquí.

## Prohibiciones

No ejecutes 4.1.3 ni posteriores. No ejecutes `A037`–`A043`. No ejecutes 121E ni ningún bloque posterior.

No modifiques Figura 3 ni ninguna otra figura.

No introduzcas nuevos resultados, nuevos p-values, nuevos intervalos, nuevas referencias, decisiones de hipótesis, generalización externa ni corrección jurídica.

No reabras EXP12.

## Respuesta oficial

Publica:

```text
writing_prompts_tmp/121D_RESPUESTA_G7_F02_V03_BLOQUE_D_RESULTADOS_4_1_1_4_1_2.md
```

en `codex/prompts-temporary` y detente con:

```text
PROMPT121D_EXECUTION = COMPLETE
A035_APPLIED = true
A036_SOURCE_VERIFICATION = PASS
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
ALL_COMMENT_IDS_ANCHORED = true
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```
