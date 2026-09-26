# PROMPT121E — Auditoría externa independiente

```text
PROMPT121E_EXTERNAL_AUDIT = PASS
PROMPT121E_BLOCK_E = PASS / APPROVED_FOR_CONTINUATION
A037 = VERIFIED / COMPLETE
A038 = VERIFIED / COMPLETE
A078 = VERIFIED / COMPLETE
A079 = VERIFIED / COMPLETE
SCIENTIFIC_CORRECTION_REQUIRED = false
TEXT_TABLE_RERUN_REQUIRED = false
A039_A040_STATUS = PENDING_SCIENTIFIC_VISUAL_WORKFLOW
121F_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## 1. Artefactos auditados

Se auditó independientemente `PROMPT121E` contra el prompt autorizado, el DOCX entregado, la trazabilidad acumulativa, el source freeze G7-F01, las fuentes numéricas canónicas de G5 y los artefactos primarios de los comparadores.

```text
Molleapasa_gv_G7F02_REVIEW_V03_E.docx
SHA256 = f6eb5a9f4db80faa36306df64ec51ddd865df2a081d69f65ca6a3e063ec2b7ba
SIZE_BYTES = 4199560

g7_thesis_claim_traceability_v0.3_E.csv
SHA256 = c8bd644af8b660269f6bb7ea6f7cebf615ad9a3d23a42ac9a2814949ae8be05f
SIZE_BYTES = 87358
TRACE_ROWS = 99
```

Los hashes y tamaños fueron recalculados sobre los binarios entregados y coinciden exactamente con la respuesta oficial.

## 2. Precondición G7-F01

Se verificó la identidad de los dos artefactos aprobados del source freeze:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.md
blob = feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430

docs/writing/group7/g7_writing_source_freeze_v0.1.json
blob = 776fcb52e8ada9967504001b897c75b4108bfb63
artifact_id = G7_F01_WRITING_SOURCE_FREEZE_v0.1
```

La detención previa de 121E fue correcta y la reanudación posterior satisfizo la precondición sin modificar los artefactos de entrada antes de la verificación.

## 3. A037 / A078 / A079 — 4.1.3 y Tabla 12

El contenido vigente de 4.1.3 describe correctamente los tres comparadores corregidos sobre 1 056 series:

- BM25 normativo plano;
- BM25 normativo jerárquico;
- recuperador denso entrenado con MNRL, sin Monte Carlo dropout.

La referencia introductoria apunta a Tabla 12. La antigua referencia a Tabla 13 queda únicamente como material legacy tachado de la copia de revisión.

La Tabla 12 conserva el mismo objeto y su contenido vigente presenta exactamente:

```text
Método | Top-1 | Top-3 | Top-5 | Top-10 | MRR@100 | Función

BM25 normativo plano
0,0275 | 0,0511 | 0,0616 | 0,0653 | 0,0423 | comparador normativo léxico

Recuperador denso entrenado con MNRL
0,0009 | 0,0104 | 0,0511 | 0,1780 | 0,0381 | comparador denso

BM25 normativo jerárquico
0,0265 | 0,0521 | 0,0625 | 0,0653 | 0,0420 | comparador normativo jerárquico
```

Estos valores coinciden con `g5_main_01_he2a_primary_early_ranking.csv` y con los artefactos primarios de cada comparador. No se incorporaron CI por brazo ni valores p. La nota distingue correctamente los valores absolutos observados de los quince contrastes pareados `histórico − comparador`, cuyos IC congelados son de 99%.

La síntesis autorizada queda correctamente limitada al benchmark interno y a la función de ranking; no convierte la superioridad del recuperador histórico en exactitud global del framework RAG ni en corrección jurídica.

## 4. A038 — cobertura profunda y Tabla 13

La prosa registra correctamente el único contraste primario de cobertura profunda:

```text
Recall@100 = 0,1013
Recall@200 = 0,3040
Diferencia = 0,2027
IC 95% = [0,0668; 0,3416]
N = 1 056 series
DAM = 67
P_VALUES = NONE
```

Pool@200 no se presenta como segunda evidencia confirmatoria.

La Tabla 13 conserva el mismo objeto y el contenido vigente muestra las cinco variantes descriptivas previstas:

```text
Solo jerárquico                                  0,0909 | 0,1013 | 0,3040
Solo dual                                        0,0919 | 0,1004 | 0,2661
Jerárquico con prioridad para los primeros 100   0,0909 | 0,1013 | 0,2652
Jerárquico 80 + backfill dual 20                 0,0909 | 0,1013 | 0,3040
Jerárquico 70 + backfill dual 30                 0,0909 | 0,1023 | 0,3040
```

La variante 70/30 queda explícitamente como contexto descriptivo adicional. La unión diagnóstica queda excluida del rendimiento ordinario y se describe solo como techo de cobertura. No hay CI, p-values, contrastes inferenciales entre variantes, ranking de favorabilidad ni interpretación causal.

## 5. Trazabilidad, comentarios e integridad OOXML

La auditoría confirmó:

```text
INHERITED_TRACE_ROWS = 88
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED = 11
NEW_TRACE_IDS = G7F02-V03E-001 .. G7F02-V03E-011
TOTAL_TRACE_ROWS = 99

TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0

INHERITED_COMMENT_COUNT = 180
COMMENTS_ADDED = 9
TOTAL_COMMENT_COUNT = 189
COMMENT_RANGE_START = 189
COMMENT_RANGE_END = 189
COMMENT_REFERENCE = 189
ORPHAN_COMMENT_IDS = NONE
DUPLICATE_COMMENT_IDS = NONE
NEW_COMMENT_IDS = 431..439
```

Los nueve comentarios nuevos están íntegramente en español, corresponden a cambios reales y contienen los seis apartados exigidos: cambio exacto, motivo, evidencia concreta, fuente gobernante, efecto en la tesis y límite de interpretación.

La convención de revisión se mantiene: contenido anterior modificado visible en amarillo y tachado; contenido nuevo en amarillo; ningún `w:del`.

## 6. Confinamiento de alcance

La comparación estructural de D_R1 contra E confirmó que solo cambiaron:

```text
word/document.xml
word/comments.xml
```

El cuerpo anterior a 4.1.3 permanece idéntico. El cuerpo desde la cabecera 4.1.4 en adelante permanece idéntico. Por tanto:

```text
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
FIGURE_4_CHANGED = false
FIGURE_5_CHANGED = false
TABLE_14_CHANGED = false
A039_EXECUTED = false
A040_EXECUTED = false
```

## 7. Revisión visual localizada

Se renderizó el DOCX y se revisó el bloque 4.1.3 junto con sus fronteras. Las Tablas 12 y 13 son legibles y no presentan clipping, overflow ni filas cortadas. La densidad visual producida por texto antiguo tachado y texto nuevo resaltado corresponde deliberadamente a la convención de copia de revisión y no debe trasladarse a la futura copia limpia.

Las Figuras 4 y 5 continúan mostrando el estado legacy inmediatamente después de 4.1.3. Esto no constituye incumplimiento de 121E porque A039/A040 estaban expresamente fuera de alcance; sí constituye una dependencia pendiente que debe resolverse antes de continuar con el siguiente bloque sustantivo.

## 8. Dictamen y siguiente actor

```text
PROMPT121E_EXTERNAL_AUDIT = PASS
PROMPT121E_BLOCK_E = PASS / APPROVED_FOR_CONTINUATION
A037 = VERIFIED / COMPLETE
A038 = VERIFIED / COMPLETE
A078 = VERIFIED / COMPLETE
A079 = VERIFIED / COMPLETE
SCIENTIFIC_CORRECTION_REQUIRED = false
TEXT_TABLE_RERUN_REQUIRED = false
A039_A040_STATUS = PENDING_SCIENTIFIC_VISUAL_WORKFLOW
NEXT_ACTOR = IA_DISENADORA_Y_AUDITORA_DE_FIGURAS_CIENTIFICAS
121F_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

La aprobación corresponde exclusivamente al Bloque E textual/tabular. No constituye aprobación global de G7-F02. Antes de 121F deben reconciliarse las Figuras 4 y 5 con las Tablas 12 y 13 mediante el flujo científico-visual gobernado por G6.