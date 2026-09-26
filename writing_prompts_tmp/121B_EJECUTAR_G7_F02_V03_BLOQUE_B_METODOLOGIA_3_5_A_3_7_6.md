# PROMPT121B — G7-F02 V03, BLOQUE B: METODOLOGÍA 3.5–3.7.6

## Rol

Actúa como **IA de Redacción Científica**. Continúa de forma acumulativa la REVIEW V03 aprobada en el Bloque A. No reconstruyas la tesis desde el baseline y no uses V01/V02.

## Estado vinculante

```text
PROMPT121A_R1_EXTERNAL_AUDIT = PASS
PROMPT121A_BLOCK_A = APPROVED
NEXT_BLOCK_121B_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

La auditoría externa está versionada en:

```text
writing_prompts_tmp/121A_R1_AUDITORIA_EXTERNA_PASS.md
```

## Entrada acumulativa única

Parte exclusivamente de:

```text
Molleapasa_gv_G7F02_REVIEW_V03_A_R1.docx
SHA256 = c6ab7325068fbeb76e283b543da372c09f114bcaca57094afae61681f419ed90
SIZE_BYTES = 4170741
```

y de su trazabilidad acumulada:

```text
g7_thesis_claim_traceability_v0.3_A_R1.csv
SHA256 = c104eb43d7bf61e2a2653ae8cf1f41fb964341f3347a5c2b94e4ec17b5aba97a
SIZE_BYTES = 8310
TRACE_ROWS_INHERITED = 14
```

Recalcula ambos SHA-256 antes de editar. Si cualquiera no coincide exactamente, **STOP**.

No uses como fuente de redacción:
- V01;
- V02;
- `Molleapasa_gv_G7F02_REVIEW_V03_A.docx` anterior a R1;
- ninguna copia alternativa de la tesis.

## Plan vinculante

Ejecuta exclusivamente las filas siguientes de la Matriz A de:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
commit = 583138f94646b1e84de1c28f32342e59f82988a3
```

```text
A016
A017
A018
A019
A020
A021
A022
A023
A024
A025
A075
```

Nada más.

## Alcance EXCLUSIVO

Puedes modificar únicamente:

- **3.5. Tamaño de muestra**;
- **Tabla 4**;
- **3.6. Selección de muestra**;
- **Tabla 5**;
- el texto introductorio de **3.7** y **Tabla 6**, solo donde A020 requiera actualización;
- **3.7.1**, únicamente para verificar A021; no modificar si no existe una discrepancia primaria confirmada;
- **3.7.3**, únicamente si A022 identifica una obsolescencia terminológica confirmada por fuente primaria;
- **3.7.4. Curación, validación y partición**;
- **3.7.5. Instrumentos computacionales y artefactos generados** y **Tabla 7**, solo en filas/celdas materialmente obsoletas;
- **3.7.6. Registro experimental y condiciones de ejecución**;
- **A075**: referencia `Tabla 8` → `Tabla 7` en 3.7.5.

### Fuera de alcance

NO modifiques:

- 3.1–3.4, incluido todo el Bloque A/R1 ya aprobado;
- 3.7.2 salvo que sea estrictamente necesario para conservar continuidad tipográfica, sin cambio semántico;
- 3.7.7 en adelante;
- Capítulo 4;
- conclusiones o recomendaciones;
- Lista de Tablas;
- Lista de Figuras;
- ninguna figura;
- A076–A082;
- referencias bibliográficas.

## Fuentes científicas primarias para este bloque

### Partición final v0.2

Gobiernan:

```text
data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
src/configs/data_aduanas_split_clase87_v0.2.json
src/evaluation/group_split_by_dam.py
```

Hechos que deben quedar consistentes:

```text
UNIT_OF_ANALYSIS = SERIE
GROUPING_FIELD = DECLARACION / DAM
TOTAL_CURATED_SERIES = 4106
HISTORICAL = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
EVAL = 1056 series / 67 DAM / 42 NANDINA
DAM_OVERLAP_BETWEEN_SPLITS = 0
ID_UNICO_OVERLAP_BETWEEN_SPLITS = 0
FULL_ASSIGNMENT = true
SEED_METADATA = 2026
FINAL_SPLIT_REPRODUCTION = EXPLICIT_DAM_ASSIGNMENT
FINAL_SPLIT_HEURISTIC_SEARCH = false
MODEL_METRIC_SELECTION = false
```

La versión final se reproduce mediante listas explícitas de DAM; no describas la estratificación proporcional por NANDINA como la regla final vigente de partición.

Los artefactos finales son:

```text
data/processed/data_aduanas_historico_clase87_v0.2.csv
data/processed/data_aduanas_devset_clase87_v0.2.csv
data/processed/data_aduanas_evalset_clase87_v0.2.csv
data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
outputs/audits/data_aduanas_splits_clase87_v0.2/
```

### Inferencia interna HE2

Gobiernan:

```text
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
outputs/analysis/group3/g3_inferential_results_v0.1.json
```

Preserva:

```text
ANALYSIS_UNIT = SERIE
DEPENDENCY_GROUP = DAM
BOOTSTRAP_REPLICATES = 10000
PRIMARY_HE2_A_CONTRASTS = 15
PRIMARY_HE2_A_CI = 99%
PRIMARY_HE2_B_CONTRAST = Recall@200 - Recall@100
PRIMARY_HE2_B_CI = 95%
P_VALUES = none
SCOPE = fixed internal Chapter-87 benchmark
EXTERNAL_POPULATION_INFERENCE = not authorized
```

No repitas innecesariamente todo el detalle ya incorporado en 3.2.2. En 3.5 basta con eliminar la contradicción entre **muestreo no probabilístico** e **inferencia interna** y remitir, cuando sea natural, al procedimiento analítico descrito en el diseño/análisis.

### Reproducibilidad

Gobiernan:

```text
outputs/audits/g2a_reproducibility_v0.1/gate_g2a_reproducibility_manifest_v0.1.json
outputs/audits/group2b_reproducibility_readiness_v0.2.json
outputs/audits/group2b_reproducibility_closure_v0.1.json
```

La redacción debe comunicar **reproducibilidad con limitaciones documentadas**, no “reproducibilidad completa” ni “reproducibilidad total”. Entre las limitaciones documentadas se encuentran activos locales no versionados o ligados por hash, componentes históricos no recuperables, información histórica incompleta del entorno y elementos de LLM/evaluación por IA que no son byte-exactamente reproducibles. Esto constituye evidencia de reproducibilidad y trazabilidad, **no una disposición formal de HE1**.

## Reglas por sección

### A016 — 3.5 Tamaño de muestra

Corrige la contradicción actual.

Debe quedar claro que:

1. no se calculó un tamaño muestral probabilístico para estimar una población externa;
2. el marco curado contiene 4 106 series;
3. la partición final es 2 950 / 100 / 1 056;
4. el conjunto final de evaluación contiene 67 DAM y 42 subpartidas NANDINA;
5. el carácter no probabilístico del conjunto **no significa ausencia de toda inferencia estadística**: HE2 utiliza remuestreo pareado por conglomerados de DAM para cuantificar incertidumbre dentro del benchmark interno;
6. no se autoriza generalización poblacional externa.

Actualiza también las menciones posteriores en 3.5 que todavía digan `1 006` cuando se refieran al conjunto final de evaluación.

### A017 — Tabla 4

Conserva el **mismo objeto de Tabla 4** y su estructura editorial. No agregues una segunda tabla.

Mantén 4 232 como conjunto inicial y 4 106 como conjunto curado total.

Actualiza:

```text
Banco histórico: 3000 -> 2950
Desarrollo: 100 -> 100
Evaluación: 1006 -> 1056
```

Cuando sea necesario para evitar ambigüedad, incorpora los conteos de DAM/NANDINA dentro de las celdas existentes de función/descripción, sin crear columnas nuevas:

```text
Histórico: 28 DAM / 66 NANDINA
Desarrollo: 6 DAM / 9 NANDINA
Evaluación: 67 DAM / 42 NANDINA
```

No alteres las submuestras de 20 y 50 salvo que una fuente primaria gobernante demuestre una discrepancia; en caso de conflicto, STOP.

### A018 — 3.6 Selección de muestra

Preserva los criterios administrativos, temporales, temáticos y de calidad que continúan vigentes.

Corrige únicamente la parte referente a la partición final:

- no describir la estratificación proporcional por NANDINA como regla final;
- indicar que cada DAM quedó íntegramente asignada a una sola partición;
- indicar ausencia de solapamiento de DAM e identificadores entre particiones;
- explicar que la configuración final se materializó mediante asignaciones explícitas de DAM, reproducibles sin reoptimización;
- la semilla 2026 puede conservarse como metadato de la configuración, pero no presentarse como mecanismo suficiente para recrear el split final;
- corregir los conteos de cobertura por subpartida cuando el texto todavía diga 69 para el banco histórico o 62 para evaluación: los valores finales son 66 y 42 respectivamente;
- corregir 3000/100/1006 a 2950/100/1056 en cualquier descripción de la partición final dentro de 3.6.

No conviertas esta partición en una muestra probabilística.

### A019 — Tabla 5

Mantén el mismo objeto de Tabla 5.

Actualiza solo las celdas de **Partición** e **Independencia** necesarias para representar:

- agrupación/asignación por DAM;
- cero solapamiento de DAM entre histórico, desarrollo y evaluación;
- cero solapamiento de identificadores;
- finalidad: evitar dependencia/fuga entre series de una misma declaración y entre particiones.

No reconstruyas la tabla.

### A020 — 3.7 y Tabla 6

Mantén las técnicas de recolección que siguen siendo válidas.

En la fila de curación/partición de Tabla 6 actualiza únicamente condiciones y producto para que el estado final sea v0.2 y DAM-disjoint. No presentes los artefactos v0.1 como salida final del experimento.

No modifiques filas de acopio, análisis documental o normalización si siguen siendo correctas.

### A021 — 3.7.1

**VERIFY / KEEP.**

Comprueba las afirmaciones contra las fuentes primarias de corpus. Si no existe una discrepancia material confirmada, no modifiques la sección y no agregues comentario.

Si descubres una discrepancia científica material que no esté prevista por Prompt119, STOP y repórtala; no improvises.

### A022 — 3.7.3

**TERMINOLOGY_ONLY.**

No reescribas la normalización. Solo modifica un término si una fuente primaria demuestra que quedó obsoleto. Si no, conserva la sección sin comentario.

### A023 — 3.7.4 Curación, validación y partición

Distingue dos funciones que el baseline mezcla:

1. la curación/validación que produjo el conjunto curado de 4 106 series;
2. la materialización posterior de la partición final v0.2 agrupada por DAM.

Preserva las reglas válidas de campos obligatorios, NANDINA de ocho dígitos, coherencia jerárquica, parseo y política de duplicados.

Reemplaza solamente la parte de partición final por el procedimiento vigente:

```text
src/evaluation/group_split_by_dam.py
config = src/configs/data_aduanas_split_clase87_v0.2.json
```

El script materializa la composición aprobada desde asignaciones explícitas de DAM; no realiza una nueva búsqueda, optimización ni selección por métricas del modelo.

Actualiza los productos finales a 2 950 / 100 / 1 056 y documenta cero solapamiento de DAM e `id_unico`.

No atribuyas retrospectivamente a `build_data_aduanas_splits.py` la materialización del split final v0.2. Ese script puede permanecer citado únicamente para las operaciones históricas de curación que realmente ejecutó.

### A024 — 3.7.5 y Tabla 7

Mantén el mismo objeto de Tabla 7.

En la fila **Curación y partición**, actualiza de manera mínima el instrumento y los artefactos para distinguir la curación previa de la partición final v0.2. Debe quedar identificable, cuando corresponda:

```text
src/evaluation/build_data_aduanas_splits.py
src/evaluation/group_split_by_dam.py
src/configs/data_aduanas_split_clase87_v0.2.json
```

y como artefactos finales:

```text
data_aduanas_historico_clase87_v0.2.csv
data_aduanas_devset_clase87_v0.2.csv
data_aduanas_evalset_clase87_v0.2.csv
data_aduanas_splits_clase87_v0.2_metadata.json
```

No actualices otras filas de Tabla 7 salvo discrepancia primaria confirmada y ya autorizada por A024. Si aparece una discrepancia no prevista, STOP.

### A025 — 3.7.6 Registro experimental y condiciones de ejecución

Mantén las condiciones válidas del LLM local, temperatura cero y ausencia de APIs remotas si siguen respaldadas.

Actualiza el párrafo de reproducibilidad para reflejar la auditoría vigente con lenguaje académico natural:

- existe trazabilidad/versionamiento suficiente para reconstruir una parte sustancial del procedimiento y verificar identidades de numerosos artefactos;
- el cierre de reproducibilidad conserva limitaciones documentadas no bloqueantes;
- existen activos locales o ligados por hash y componentes históricos no recuperables/entorno incompleto;
- algunas ejecuciones con LLM/evaluación por IA no son byte-exactamente reproducibles;
- no afirmar “reproducibilidad completa” ni “reproducibilidad total”;
- no derivar de este estado una decisión formal de HE1.

No uses nombres internos de grupos, gates o estados administrativos en la prosa visible.

### A075 — referencia cruzada

En 3.7.5 corrige exclusivamente:

```text
La Tabla 8 relaciona...
```

a:

```text
La Tabla 7 relaciona...
```

No renumeres la Tabla 7.

## Convención de revisión visible

Preserva exactamente la convención aprobada:

```text
TEXTO_ANTERIOR_MODIFICADO = AMARILLO + TACHADO + VISIBLE
TEXTO_NUEVO = AMARILLO + NO_TACHADO + VISIBLE
TEXTO_SIN_CAMBIO = NORMAL
```

Reglas:

- fragmento mínimo primero;
- no taches una celda o párrafo completo si cambia solo una cifra/frase;
- `PARAGRAPH_REWRITE_MINIMAL` permite párrafo completo solo cuando la mayor parte de la semántica de ese párrafo está obsoleta;
- no uses `w:del`;
- no elimines silenciosamente texto del baseline;
- no dupliques tablas.

## Comentarios Word

Añade comentarios únicamente donde exista cambio real.

Cada comentario nuevo debe estar íntegramente en español y contener exactamente:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

No comentes A021/A022 si no hay cambio visible.

No filtres a la prosa visible identificadores de gobernanza como G1–G8, Group2, G3-Fxx, Prompt119, Prompt121B, source freeze, claim IDs, gates, estados de aprobación, códigos internos de auditoría o nombres equivalentes.

Los paths técnicos reales pueden aparecer en 3.7.5 cuando son instrumentos/artefactos genuinos de reproducibilidad científica.

## Trazabilidad acumulativa

Parte del CSV A_R1 de 14 filas y **preserva esas 14 filas sin modificación**.

Añade filas nuevas únicamente para cambios efectivamente aplicados en este Bloque B, con IDs nuevos no colisionantes del tipo:

```text
G7F02-V03B-001
G7F02-V03B-002
...
```

No crees filas para verificaciones `KEEP` sin cambio.

Salida acumulativa:

```text
g7_thesis_claim_traceability_v0.3_B.csv
```

## Salida DOCX acumulativa

Genera:

```text
Molleapasa_gv_G7F02_REVIEW_V03_B.docx
```

Debe contener intactas las correcciones ya aprobadas del Bloque A/R1 y sumar únicamente las modificaciones del Bloque B.

No generes todavía la V03 final.

## QA estructural del bloque

Verifica y reporta al menos:

```text
INPUT_DOCX_SHA256
OUTPUT_DOCX_SHA256
INPUT_TRACE_SHA256
OUTPUT_TRACE_SHA256
DOCX_ZIP_INTEGRITY
ZIP_ENTRY_SET_PRESERVED
TOTAL_TABLE_OBJECT_COUNT = 24
TABLE_OBJECT_COUNT_DELTA = 0
TRACKED_DELETION_COUNT = 0
INHERITED_TRACE_ROWS = 14
INHERITED_TRACE_ROWS_CHANGED = 0
NEW_TRACE_ROWS_ADDED
A075_APPLIED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
BASELINE_BLOCK_A_CONTENT_PRESERVED = true
```

Comprueba además:

- ninguna modificación en 3.1–3.4;
- ninguna modificación en 3.7.7 en adelante;
- ninguna figura modificada;
- Listas de Tablas/Figuras sin cambios;
- Tabla 4–7 siguen siendo cuatro objetos existentes, no copias;
- 4 232 y 4 106 se preservan donde corresponden;
- 2 950 / 100 / 1 056 se usan como partición final;
- 28/6/67 DAM y 66/9/42 NANDINA son consistentes donde se reporten;
- 0 solapamiento de DAM entre particiones;
- no permanece 3 000/100/1 006 como descripción de la partición final dentro de 3.5–3.7.6;
- no permanece 69/62 como conteo final de códigos histórico/evaluación dentro de 3.6;
- `Tabla 8` no permanece como referencia a la tabla de instrumentos de 3.7.5;
- no se afirma ausencia absoluta de inferencia estadística;
- no aparece “reproducibilidad completa” ni “reproducibilidad total”;
- 0 términos de gobernanza interna introducidos en prosa visible.

## QA visual localizado

Renderiza el DOCX resultante e inspecciona **todas las páginas afectadas por 3.5–3.7.6**, incluyendo cualquier página que se desplace por los cambios. No es necesario auditar visualmente todo el documento en este bloque modular.

Revisa específicamente:

- clipping/desbordes;
- tablas 4–7 legibles y sin duplicación;
- bordes/anchos preservados;
- texto anterior y nuevo comparables;
- amarillo limitado al cambio real;
- saltos de página razonables;
- ausencia de páginas vacías inesperadas dentro del rango afectado.

## Prohibiciones científicas

No introduzcas:

- nueva inferencia;
- nuevos intervalos;
- nuevos valores p;
- nuevas métricas;
- nuevas referencias;
- una disposición formal para HE1;
- generalización externa;
- corrección jurídica de la clasificación;
- reapertura de EXP12.

No modifiques resultados de HE2–HE5 en este bloque.

## Respuesta

Publica:

```text
writing_prompts_tmp/121B_RESPUESTA_G7_F02_V03_BLOQUE_B.md
```

en la rama:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT121B_EXECUTION
INPUT_DOCX_SHA256
OUTPUT_DOCX_SHA256
OUTPUT_DOCX_SIZE_BYTES
INPUT_TRACE_SHA256
OUTPUT_TRACE_SHA256
OUTPUT_TRACE_SIZE_BYTES
SECTIONS_MODIFIED
TABLES_MODIFIED
A075_APPLIED
COMMENTS_ADDED
TRACE_ROWS_INHERITED
TRACE_ROWS_ADDED
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS
OUT_OF_SCOPE_COMMENT_MODIFICATIONS
TRACKED_DELETION_COUNT
LOCAL_VISUAL_REVIEW
G7_F02_STATE
G7_F03_AUTHORIZED
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Terminal esperado:

```text
PROMPT121B_EXECUTION = COMPLETE
A075_APPLIED = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
TRACKED_DELETION_COUNT = 0
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
NEXT_BLOCK = PENDING_EXTERNAL_AUDIT
```

Detente. No ejecutes el siguiente bloque hasta auditoría externa de la IA Experimental.
