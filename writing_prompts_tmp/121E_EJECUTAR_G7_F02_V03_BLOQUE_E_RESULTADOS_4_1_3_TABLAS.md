# PROMPT121E — G7-F02 V03, BLOQUE E: RESULTADOS 4.1.3 Y TABLAS 12–13

## Rol y estado

Actúa como **IA de Redacción Científica**. Continúa acumulativamente desde el Bloque D_R1 aprobado. No eres CODEX, no eres la IA Experimental y no debes ejecutar bloques posteriores.

```text
PROMPT121D_R1_EXTERNAL_AUDIT = PASS
PROMPT121D_BLOCK_D = PASS / APPROVED_FOR_CONTINUATION
NEXT_BLOCK_121E_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría vinculante:

```text
writing_prompts_tmp/121D_R1_AUDITORIA_EXTERNA_PASS.md
commit = ebec160ae8667099363e65d606612599df223e01
```

## Entrada única

Usa exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_D_R1.docx
SHA256 = 5b9a1d59e1e459f2772410d268029b976a552c59629c789c90ebfbfa160fca4b
SIZE_BYTES = 4195516
```

Trazabilidad acumulativa:

```text
g7_thesis_claim_traceability_v0.3_D_R1.csv
SHA256 = 82582814e17a4e535c6f79d30d7629cc88076d51962adc4b316cc79954d8559d
SIZE_BYTES = 77788
TRACE_ROWS_INHERITED = 88
```

Recalcula ambos hashes antes de editar. Si cualquiera no coincide exactamente, STOP.

## Alcance exclusivo

Ejecuta solo:

```text
A037
A038
A078
A079
```

del plan vinculante:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
```

Puedes modificar únicamente:

- `4.1.3. Resultados de la recuperación normativa`;
- `Tabla 12`;
- `Tabla 13`;
- los párrafos de síntesis inmediatamente asociados a esas dos tablas.

Las correcciones A078 y A079 forman parte de este mismo alcance:

```text
A078: primera referencia `Tabla 13` -> `Tabla 12`
A079: referencia posterior `Los valores de la Tabla 13...` -> `Tabla 12`, si esa oración se conserva; si el párrafo se reescribe por A037, la nueva redacción debe apuntar correctamente a Tabla 12.
```

### Fuera de alcance

No modifiques:

- 4.1.2 ni Tabla 11;
- 4.1.4 ni Tabla 14;
- Figura 3;
- Figura 4;
- Figura 5;
- ninguna otra figura;
- ninguna sección anterior a 4.1.3 ni posterior a su frontera con 4.1.4;
- listas preliminares;
- bibliografía;
- conclusiones;
- recomendaciones.

**A039 y A040 no se ejecutan en este prompt.** Las Figuras 4 y 5 requieren el flujo específico de la **IA Diseñadora y Auditora de Figuras Científicas** y se tratarán en un bloque separado después de la auditoría externa de 121E. No regeneres, sustituyas, edites, recortes ni reubiques imágenes en esta ejecución.

## Fuentes científicas vinculantes

Lee primero el source freeze de G7-F01 y sigue su precedencia. Para este bloque, los artefactos numéricos de presentación son:

```text
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
blob = cb68583ee2260e4455796bac99ad90995ca7ef92

outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
blob = 359e4e19b5ef1d44983c03039162209293b2a44c

outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
```

Fuentes primarias de los tres comparadores de ranking temprano:

```text
outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/normative_flat_metrics.json
blob = 922ecbee8316ee36cd8a53d3ac52f79fac4cd3ed

outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json
blob = 780a005130d1ad68867b290b832c394f8f488a23

outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_metrics.json
blob = 73e062b927d059a9f4e52caab7b785eafb6f2e01
```

No uses cifras del baseline cuando contradigan estos artefactos. No recalcules métricas, intervalos ni contrastes.

## Marco científico congelado

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION when applicable
EVAL = 1056 series / 67 DAM / 42 NANDINA
HE2 = SUPPORTED
P_VALUES = NONE
EARLY_RANKING_PRIMARY_CI = 99% ON PAIRED HISTORICAL_MINUS_COMPARATOR DIFFERENCES ONLY
HIERARCHICAL_DEEP_COVERAGE_CI = 95% ON RECALL@200_MINUS_RECALL@100 ONLY
ARM_LEVEL_CI_AUTHORIZED = false
PHASE_E_COVERAGE = DESCRIPTIVE_ONLY / NO_CI / NO_P_VALUES
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
```

Los contrastes son no causales y se limitan al benchmark interno.

---

# A037 — 4.1.3 y Tabla 12

## 1. Corrección del párrafo introductorio

El estado visible actual es obsoleto: menciona cuatro configuraciones, `1 006` consultas y una referencia incorrecta a Tabla 13.

Actualiza el fragmento mínimo para describir los **tres comparadores corregidos de ranking temprano** aplicados sobre `1 056` series de evaluación:

1. comparador normativo BM25 plano;
2. comparador normativo BM25 jerárquico;
3. recuperador denso entrenado con MNRL, sin Monte Carlo dropout.

En prosa visible:

- no escribas `Attempt06`;
- no escribas `EV03` ni `EV04`;
- no uses `D1a` salvo que se defina expresamente como identificador técnico; **preferencia vinculante para esta tesis: omitir D1a y usar “recuperador denso entrenado con MNRL”**;
- no denomines al tercer brazo simplemente “Text2Trade”, porque el artefacto ejecutado es un recuperador inspirado en ese enfoque y no una reproducción literal completa de Text2Trade.

La frase que introduce el ranking temprano debe remitir a **Tabla 12**, no Tabla 13.

## 2. Tabla 12 — estructura objetivo

Conserva el mismo objeto `Tabla 12`; no lo dupliques ni crees otro objeto de tabla.

Título corporal: conserva el título si sigue siendo natural:

```text
Comparación del desempeño de las estrategias de recuperación normativa
```

Adapta la tabla in-place para presentar exclusivamente los valores observados de las cinco métricas primarias de ranking temprano en los tres comparadores corregidos.

Estructura recomendada:

```text
Método | Top-1 | Top-3 | Top-5 | Top-10 | MRR@100 | Función
```

Valores vinculantes, con redondeo de presentación a cuatro decimales:

```text
BM25 normativo plano
Top-1   = 0,0275
Top-3   = 0,0511
Top-5   = 0,0616
Top-10  = 0,0653
MRR@100 = 0,0423
Función = comparador normativo léxico

BM25 normativo jerárquico
Top-1   = 0,0265
Top-3   = 0,0521
Top-5   = 0,0625
Top-10  = 0,0653
MRR@100 = 0,0420
Función = comparador normativo jerárquico

Recuperador denso entrenado con MNRL
Top-1   = 0,0009
Top-3   = 0,0104
Top-5   = 0,0511
Top-10  = 0,1780
MRR@100 = 0,0381
Función = comparador denso
```

No incluyas en Tabla 12:

- valores legacy de `1 006` casos;
- `Recall@100` como sustituto de una de las cinco métricas primarias;
- la antigua fila `BM25 dual protegido`;
- intervalos de confianza por brazo;
- p-values;
- significancia;
- métricas históricas como una cuarta fila normativa.

### Nota obligatoria de Tabla 12

La nota debe dejar claro, en lenguaje de tesis, que:

- los valores son observados sobre 1 056 series del benchmark interno;
- no existen CI por brazo autorizados;
- la inferencia primaria de HE2 compara de forma pareada el ranking histórico con cada comparador y los intervalos congelados corresponden a esas **diferencias pareadas**, no a los valores absolutos mostrados en la tabla.

No vuelques los quince intervalos dentro de Tabla 12.

## 3. Síntesis asociada a Tabla 12

Reescribe únicamente lo necesario para eliminar los resultados provisionales/legacy actualmente visibles.

La síntesis debe comunicar, sin repetir todas las celdas, que:

- los tres comparadores corregidos presentan valores observados de ranking temprano sustancialmente inferiores al ranking histórico en el benchmark interno;
- la conclusión inferencial autorizada se basa en los quince contrastes pareados con CI congelados de 99%, no en una inspección visual de valores absolutos;
- no se calcularon p-values;
- esta superioridad del recuperador histórico corresponde a la función de ranking y **no equivale a exactitud global del framework RAG ni a corrección jurídica**.

Puedes mencionar uno o dos valores ilustrativos si mejoran la lectura, pero no reproduzcas la tabla completa en prosa.

---

# A038 — Tabla 13 y cobertura profunda/descriptiva

## 1. Contraste primario de cobertura profunda

Antes de la tabla descriptiva, la prosa debe registrar el contraste primario vigente del recuperador jerárquico corregido:

```text
Recall@100 = 0.10132575757575757
Recall@200 = 0.3039772727272727
DIFFERENCE Recall@200 - Recall@100 = 0.20265151515151514
FROZEN_95_CI = [0.06676310583580614, 0.34160130792395144]
N = 1056 series
DAM = 67
P_VALUES = NONE
```

En presentación a cuatro decimales:

```text
Recall@100 = 0,1013
Recall@200 = 0,3040
Diferencia = 0,2027
IC 95% = [0,0668; 0,3416]
```

Este es **un único contraste primario**. No presentes `Pool@200` como una segunda evidencia confirmatoria independiente.

## 2. Tabla 13 — estructura objetivo

Conserva el mismo objeto `Tabla 13` y adapta su estructura in-place. No dupliques la tabla.

La tabla debe dejar de mostrar las métricas jerárquicas legacy `Partida@100 / HS-6@100 / Clase@100` y la antigua unión diagnóstica como rendimiento ordinario.

Usa la tabla para mostrar la **cobertura exacta NANDINA descriptiva** de las cinco variantes congeladas en profundidades 50, 100 y 200.

Estructura recomendada:

```text
Variante | Cobertura@50 | Cobertura@100 | Cobertura@200 | Rol
```

Valores vinculantes, redondeados a cuatro decimales:

```text
Solo jerárquico
0,0909 | 0,1013 | 0,3040 | Variante descriptiva predefinida

Solo dual
0,0919 | 0,1004 | 0,2661 | Variante descriptiva predefinida

Jerárquico con prioridad para los primeros 100 candidatos
0,0909 | 0,1013 | 0,2652 | Variante descriptiva predefinida

Jerárquico 80 + backfill dual 20
0,0909 | 0,1013 | 0,3040 | Variante descriptiva predefinida

Jerárquico 70 + backfill dual 30
0,0909 | 0,1023 | 0,3040 | Contexto descriptivo adicional
```

Los nombres pueden recibir un ajuste mínimo de estilo para caber en la tabla, siempre que no cambie su semántica. No muestres los identificadores internos `hierarchical_only`, `dual_only`, `hierarchical_first_100`, `hierarchical_80_dual_backfill_20` o `hierarchical_70_dual_backfill_30` en prosa visible salvo que sea estrictamente necesario para reproducibilidad; si se necesitan, déjalos solo en comentario o trazabilidad.

### Nota obligatoria de Tabla 13

Debe indicar que:

- todas las proporciones usan el benchmark de 1 056 series;
- son resultados **descriptivos**;
- no tienen CI ni p-values;
- no se realizaron contrastes inferenciales entre variantes;
- la variante 70/30 se presenta únicamente como contexto descriptivo adicional y no fue seleccionada por favorabilidad;
- la unión diagnóstica de jerárquico y dual representa un techo de cobertura y queda excluida de la tabla de rendimiento ordinario.

No utilices el nombre interno `Phase E` en prosa visible.

## 3. Síntesis asociada a Tabla 13

Elimina/reemplaza la prosa legacy que actualmente declara como “mejor pool” una configuración por 0,3489/0,6292 o usa la unión diagnóstica 0,3658/0,6392 como comparación ordinaria.

La nueva síntesis debe limitarse a describir el patrón congelado:

- a profundidad 50, las cinco coberturas exactas están alrededor de 0,091;
- a profundidad 100, se sitúan aproximadamente entre 0,1004 y 0,1023;
- a profundidad 200, se sitúan entre 0,2652 y 0,3040;
- las variantes predefinidas y la variante 70/30 son contexto descriptivo y **no autorizan un ranking de favorabilidad ni una conclusión inferencial entre variantes**.

No presentes la diferencia entre variantes como evidencia de significancia ni como efecto causal.

---

## Convención de revisión visible

```text
ANTERIOR_MODIFICADO = amarillo + tachado + visible
NUEVO = amarillo + no tachado + visible
SIN_CAMBIO = normal
```

- Modifica el fragmento mínimo posible.
- En reescrituras de párrafos cuya semántica legacy deba sustituirse materialmente, conserva el párrafo anterior visible y marcado y coloca el nuevo párrafo inmediatamente después, conforme a Prompt120.
- Para Tabla 12 y Tabla 13, conserva cada objeto de tabla y modifica su contenido/estructura in-place.
- No uses `w:del`.
- No dupliques tablas.

## Comentarios Word

Añade comentarios únicamente a cambios reales. Cada comentario debe contener exactamente estos seis encabezados en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Para cambios estructurales de Tabla 12 o Tabla 13 puedes usar un comentario por fila/celda materialmente modificada o por unidad estructural coherente, pero cada comentario debe quedar anclado a texto realmente modificado y permitir reconstruir qué cambió.

No agregues comentarios a Figuras 4–5 porque permanecen sin modificación en este bloque.

## Trazabilidad

Preserva byte-semánticamente las 88 filas heredadas de D_R1, en el mismo orden.

Añade únicamente filas por cambios reales de 121E, con identificadores:

```text
G7F02-V03E-001 ...
```

Debe existir trazabilidad suficiente para distinguir:

- actualización del párrafo introductorio y A078;
- Tabla 12;
- síntesis posterior a Tabla 12 y A079;
- contraste primario de cobertura profunda;
- Tabla 13;
- síntesis posterior a Tabla 13.

No agregues filas por verificar elementos que no cambian.

## Integridad heredada

La entrada aprobada tiene:

```text
TOTAL_TABLE_OBJECT_COUNT = 24
INHERITED_COMMENT_COUNT = 180
INHERITED_TRACE_ROWS = 88
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
COMMENTS_418_430_UNCHANGED = true
```

Exige al cierre:

```text
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
INHERITED_TRACE_ROWS_CHANGED = 0
INHERITED_COMMENT_TEXT_CHANGED = 0
INHERITED_ORPHAN_COMMENT_IDS = NONE
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
COMMENTS_418_430_UNCHANGED = true
```

Si cualquier comentario heredado cambia de texto o queda huérfano, STOP.

## Salidas

Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E.docx
g7_thesis_claim_traceability_v0.3_E.csv
```

No generes una V03 final ni una copia limpia.

## QA obligatorio

Reporta al menos:

```text
INPUT_DOCX_SHA256
OUTPUT_DOCX_SHA256
INPUT_TRACE_SHA256
OUTPUT_TRACE_SHA256
TOTAL_TABLE_OBJECT_COUNT = 24
TRACKED_DELETION_COUNT = 0
INHERITED_TRACE_ROWS = 88
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED
INHERITED_COMMENT_COUNT = 180
COMMENTS_ADDED
A037_APPLIED = true
A038_APPLIED = true
A078_APPLIED = true
A079_APPLIED = true
TABLE_12_UPDATED_IN_PLACE = true
TABLE_13_UPDATED_IN_PLACE = true
FIGURE_4_CHANGED = false
FIGURE_5_CHANGED = false
A039_EXECUTED = false
A040_EXECUTED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_230_ANCHORED = true
COMMENT_384_UNCHANGED = true
COMMENTS_418_430_UNCHANGED = true
```

Renderiza e inspecciona únicamente 4.1.3 y una página de frontera antes y después. La frontera posterior debe confirmar que `4.1.4` y `Tabla 14` permanecen sin cambios. Verifica específicamente que Tabla 12 y Tabla 13 no presenten clipping, overflow, filas cortadas ni texto ilegible después de adaptar su estructura.

## Prohibiciones científicas y editoriales

- No ejecutar A039 ni A040.
- No modificar Figuras 4–5.
- No ejecutar 4.1.4 ni A041–A043.
- No crear nuevas tablas.
- No crear nuevas figuras.
- No usar resultados superseded del baseline.
- No recalcular métricas o intervalos.
- No crear CI por brazo.
- No calcular p-values.
- No convertir la cobertura descriptiva en evidencia confirmatoria.
- No seleccionar o describir variantes por favorabilidad.
- No presentar la unión diagnóstica como rendimiento ordinario.
- No inferir exactitud global del RAG a partir de superioridad del ranking histórico.
- No inferir corrección jurídica.
- No introducir nuevas referencias.
- No reabrir EXP12.

## Respuesta oficial

Publica:

```text
writing_prompts_tmp/121E_RESPUESTA_G7_F02_V03_BLOQUE_E_RESULTADOS_4_1_3_TABLAS.md
```

en `codex/prompts-temporary` y detente con:

```text
PROMPT121E_EXECUTION = COMPLETE
A037_APPLIED = true
A038_APPLIED = true
A078_APPLIED = true
A079_APPLIED = true
TABLE_12_UPDATED_IN_PLACE = true
TABLE_13_UPDATED_IN_PLACE = true
FIGURE_4_CHANGED = false
FIGURE_5_CHANGED = false
A039_EXECUTED = false
A040_EXECUTED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
ALL_COMMENT_IDS_ANCHORED = true
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

No avances al bloque científico-visual ni a 4.1.4.