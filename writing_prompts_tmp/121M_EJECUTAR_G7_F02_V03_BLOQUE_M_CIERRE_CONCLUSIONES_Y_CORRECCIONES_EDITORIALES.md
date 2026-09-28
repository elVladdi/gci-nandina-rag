# PROMPT121M — G7-F02 V03, BLOQUE M: cierre de conclusiones, recomendaciones y correcciones editoriales finales

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. Este bloque está autorizado únicamente después del PASS externo de 121L-R1.

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/121L_R1_AUDITORIA_EXTERNA_PASS.md
commit = 0006260f4c05fab925d731488aa103a04888ef21

writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
commit = 583138f94646b1e84de1c28f32342e59f82988a3
```

Ejecuta exclusivamente las acciones pendientes enumeradas en este prompt. **No reejecutes A073–A079. No ejecutes G7-F03 ni ningún bloque posterior.**

---

## 1. Entradas exactas

Trabaja exclusivamente sobre los artefactos L-R1 aprobados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_L_R1.docx
SHA256 = 262a7621bd7e426e8c9c2da3bf73812a9c55ccfd40b45673999b9d6999cdba49
SIZE = 4686010

g7_thesis_claim_traceability_v0.3_L_R1.csv
SHA256 = d6d27bf608f141ff490fa2c91f73d3e28c0637e5a94107abd0aae64f6362d5ee
SIZE = 123152
ROWS = 128
```

Verifica hash, tamaño y filas antes de editar. Si no coinciden, devuelve `STOPPED_PRECONDITION` y no modifiques nada.

Estado estructural heredado obligatorio:

```text
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
COMMENT_COUNT = 217
ALL_NONEMPTY_COMMENT_IDS_ANCHORED = true
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TRACE_ROWS = 128
A073_A079_ALREADY_APPLIED = true
```

No reconstruyas el documento desde K, L, baseline ni ninguna versión anterior.

---

## 2. Alcance EXCLUSIVO de 121M

Ejecuta exactamente estas ocho acciones pendientes del plan:

```text
A068 = Conclusiones
A069 = Recomendaciones
A070 = Lista de Tablas
A071 = Lista de Figuras / verificación sin cambio
A072 = Índice/campos automáticos / verificación sin cambio
A080 = 4.1.8, referencia Tabla 21 -> Tabla 20
A081 = 4.2, referencia Tabla 10 -> Tabla 9
A082 = 4.3.5, referencia Tabla 24 -> Tabla 23
```

Las acciones A073–A079 ya fueron ejecutadas y trazadas en bloques anteriores. **No las vuelvas a tocar ni añadas filas nuevas para ellas.**

No modifiques Capítulos 1–3 ni 4.1–4.3 fuera de los tres reemplazos inline A080–A082.

---

## 3. Contrato editorial REVIEW V03

Se mantiene íntegramente el contrato de revisión:

- texto legacy reemplazado: **amarillo + tachado + visible**;
- texto nuevo: **amarillo + no tachado**;
- texto sin cambios: formato normal;
- no usar `w:del` ni `w:ins`;
- no borrar físicamente texto legacy;
- edición mínima: fragmento → celda → fila → párrafo, solo según lo autorizado;
- no reconstruir tablas, figuras, índices o secciones completas si basta una modificación localizada;
- no introducir IDs internos, nombres de prompts, gates, commits, acciones Axxx ni estados administrativos en la tesis visible;
- no añadir bibliografía ni referencias nuevas;
- no crear ciencia, métricas, inferencia, p-values, CI ni resultados no existentes;
- conservar la numeración de Figuras 1–12 durante REVIEW V03;
- no aceptar ni limpiar cambios: esta sigue siendo una copia de revisión.

Cada comentario nuevo debe estar íntegramente en español y contener exactamente estos seis apartados, en este orden:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

---

# 4. A068 — CONCLUSIONES

## 4.1. Regla científica

Conserva el encabezado `CONCLUSIONES` y la estructura de ocho párrafos conclusivos. Los ocho párrafos actuales dependen en distinta medida de ciencia superseded; sustitúyelos por versiones científicamente vigentes sin agregar referencias bibliográficas.

La nueva redacción debe ser natural, conclusiva y coherente con el tono del baseline. No debe incluir rutas, hashes, nombres de artefactos ni códigos de gobernanza.

### Estado científico vinculante

```text
BENCHMARK = 1056 series / 67 DAM / 42 NANDINA / Capítulo 87 / offline
HISTORICAL_BANK = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM / 9 NANDINA
CURATED_TOTAL = 4106 series
NORMATIVE_HIERARCHICAL_DOCUMENTS = 7648

HISTORICAL_TOP1 = 0.5095
HISTORICAL_TOP3 = 0.6714
HISTORICAL_TOP5 = 0.7633
HISTORICAL_TOP10 = 0.8911
HISTORICAL_TOP50 = 0.9915
HISTORICAL_MRR100 = 0.6297

HE2 = SUPPORTED
HE2_PRIMARY = 15 paired contrasts, bilateral CI 99 %, all above zero
HE2_DEEP = Recall@200 - Recall@100 hierarchical, bilateral CI 95 %, above zero
P_VALUES = NONE

INTEGRATION_RANKING_INVARIANT = 1056/1056
TRACE_HISTORICAL = 3168/3168 candidate positions
TRACE_NORMATIVE = 3168/3168 candidate positions
CANDIDATES_INSERTED_OR_REMOVED_BY_NORMATIVE_EVIDENCE = 0
HE3 = SUPPORTED

RERANKER_SAMPLE = 20
RERANKER_REFERENCE_IN_POOL = 19
RERANKER_REFERENCE_OUTSIDE_POOL = 1
RERANKER_TOP1_BEFORE_AFTER = 0.5000 / 0.5000
RERANKER_TOP3_BEFORE_AFTER = 0.6500 / 0.6500
RERANKER_TOP5_BEFORE_AFTER = 0.8000 / 0.8000
RERANKER_MRR_BEFORE_AFTER = 0.6326 / 0.6326
RERANKER_POSITIVE_NOCHANGE_NEGATIVE = 0 / 19 / 0
RERANKER_INTERPRETATION = DIAGNOSTIC_ONLY / NO_AGGREGATE_IMPROVEMENT / NO_AGGREGATE_DETERIORATION

HE4_TOP3_ORDER_PRESERVED = 50/50
HE4_TRACEABILITY_COMPLETE = 50/50
HE4_GENERIC_NORM_WARNING_CONFORMANT = 41/50
HE4_GENERIC_NORM_WARNING_MISSING = 9/50
HE4_AUDITABLE = 28/50
HE4_NON_AUDITABLE = 22/50
HE4_SEVERE_VIOLATIONS = 0/50
HE4_EVALUATOR = independent AI under expert role
HE4_HUMAN_SCORING = none
HE4 = PARTIALLY_SUPPORTED

HE5 = INCONCLUSIVE
HE1 = NO_FORMAL_DISPOSITION_FOUND
HG = NO_FORMAL_DISPOSITION_FOUND
```

### Guardrails obligatorios

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
EXP11A != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
ATTEMPT06 != GLOBAL_ZERO_IMPACT
```

No afirmar:

- reproducibilidad completa, total o absoluta;
- validación externa;
- corrección jurídica;
- clasificación oficial;
- evaluación humana de HE4;
- que ausencia de violaciones graves implique corrección;
- que 50/50 estructural equivalga a 28/50 cualitativo;
- que el reranker sea globalmente nulo fuera de la muestra diagnóstica;
- que HE1 o la hipótesis general tengan dictamen terminal.

## 4.2. Redacción objetivo de las ocho conclusiones

Puedes ajustar conectores y sintaxis al estilo nativo, pero **no cambiar el contenido científico**.

### Conclusión 1

```text
El objetivo general se evaluó dentro del alcance experimental definido mediante una arquitectura que separó tres funciones: la recuperación histórica ordenó candidatos, el corpus normativo aportó evidencia identificable y el LLM local explicó un Top-3 fijo sin modificarlo. El piloto produjo salidas con trazabilidad y controles estructurales de revisión, pero la auditabilidad cualitativa fue heterogénea y no equivale a clasificación oficial ni a validación jurídica.
```

### Conclusión 2

```text
La preparación de la información convirtió registros administrativos y documentos normativos en artefactos consultables y trazables. El conjunto curado reunió 4 106 series y la partición final mantuvo 2 950 series en el banco histórico, 100 en desarrollo y 1 056 en evaluación, sin solapamiento de DAM ni de identificadores entre particiones; además, se conservaron 7 648 documentos normativos jerárquicos con metadatos y advertencias de calidad. La trazabilidad y el versionamiento permiten reconstruir una parte sustancial del procedimiento, aunque persisten activos locales o restringidos y ejecuciones no reproducibles exactamente a nivel de bytes; por ello, no se afirma reproducibilidad completa ni se deriva una decisión terminal para HE1.
```

### Conclusión 3

```text
La recuperación histórica presentó el mejor desempeño de ranking temprano entre las configuraciones comparadas dentro del benchmark interno. Sobre 1 056 series alcanzó Top-1 de 0,5095, Top-3 de 0,6714, Top-5 de 0,7633, Top-10 de 0,8911, Top-50 de 0,9915 y MRR@100 de 0,6297. La evidencia primaria de HE2 se apoyó en quince contrastes pareados con intervalos bilaterales del 99 % por encima de cero, sin valores p. Esta superioridad se limita a la función de recuperación histórica evaluada y no representa exactitud global del sistema ni validez externa.
```

### Conclusión 4

```text
La recuperación normativa mostró un desempeño temprano inferior al del ranking histórico en los comparadores corregidos, mientras que la representación jerárquica amplió la cobertura en profundidades mayores; el contraste Recall@200 menos Recall@100 presentó un intervalo bilateral del 95 % por encima de cero. Su contribución principal en la arquitectura final fue documental: aportar evidencia identificable para candidatos ya ordenados. En este alcance, HE2 quedó respaldada, sin que la evidencia normativa pueda interpretarse como garantía de corrección jurídica.
```

### Conclusión 5

```text
La integración histórica–normativa conservó el ranking histórico en 1 056 de 1 056 casos y no insertó ni eliminó candidatos. Para las 3 168 posiciones del Top-3 se mantuvo trazabilidad completa tanto hacia el precedente histórico como hacia el documento normativo asociado. La evidencia normativa añadió contexto revisable sin reordenar los candidatos; esta separación funcional respalda HE3 y mantiene al ranking histórico como mecanismo principal de ordenamiento.
```

### Conclusión 6

```text
El reordenamiento con LLM se mantuvo como una prueba diagnóstica independiente sobre 20 casos. La referencia estuvo presente en el pool en 19 casos y ausente en uno; entre los casos recuperables no hubo variaciones positivas ni negativas de posición y las métricas agregadas permanecieron iguales antes y después: Top-1 de 0,5000, Top-3 de 0,6500, Top-5 de 0,8000 y MRR de 0,6326. Este resultado describe únicamente la muestra observada y no justifica atribuir al LLM una mejora del ranking ni generalizar un efecto nulo fuera del diagnóstico ejecutado.
```

### Conclusión 7

```text
El LLM restringido al Top-3 cumplió los controles estructurales de preservación del ranking y trazabilidad en las 50 fichas evaluadas, pero la revisión cualitativa mostró una calidad de auditabilidad más limitada. La advertencia ante normativa genérica fue conforme en 41 de 50 fichas; 28 de 50 fueron calificadas como auditables y 22 de 50 como no auditables, sin violaciones graves observadas. La evaluación cualitativa fue realizada por una inteligencia artificial independiente bajo un rol experto y no incluyó puntuación humana. En consecuencia, HE4 quedó parcialmente respaldada y la auditabilidad no se equipara con corrección de clasificación ni validez jurídica.
```

### Conclusión 8

```text
Los límites del piloto impiden cerrar de forma confirmatoria todos los componentes previstos. La calidad descriptiva no fue operacionalizada prospectivamente, la proximidad jerárquica y el soporte histórico permanecen descriptivos, las sensibilidades de tamaño y composición no identifican efectos causales aislados, y el análisis de diversidad se cerró sin ejecutar recuperación, por lo que su efecto no es estimable. HE5 permanece inconclusa; HE2 y HE3 están respaldadas, HE4 parcialmente respaldada y no se localizó una disposición formal terminal para HE1 ni para la hipótesis general. Estas conclusiones se restringen al benchmark offline interno del Capítulo 87 y no autorizan generalización automática a otras clases, aduanas, periodos o condiciones operativas.
```

### Marcado

Para cada uno de los ocho párrafos:

1. conserva el párrafo legacy visible;
2. marca el contenido legacy reemplazado como amarillo + tachado;
3. añade inmediatamente el nuevo contenido como amarillo, no tachado;
4. conserva el número de párrafos y la posición del bloque bajo `CONCLUSIONES`.

### Comentario A068

Añade **un solo comentario Word**, ID esperado `468`, que documente A068 y quede anclado al nuevo bloque conclusivo. Puede abarcar el bloque de conclusiones modificado o anclarse al primer párrafo nuevo siempre que describa de forma inequívoca el conjunto de ocho conclusiones actualizadas.

---

# 5. A069 — RECOMENDACIONES

La revisión externa previa del texto actual determinó que las recomendaciones vigentes son prospectivas y ya están formuladas con límites adecuados.

Por tanto:

```text
A069_STATUS = VERIFIED_NO_CHANGE
VISIBLE_CHANGE = false
COMMENT_REQUIRED = false
```

No modifiques el encabezado `RECOMENDACIONES` ni ninguno de sus seis párrafos actuales.

Registra A069 en trazabilidad como verificado sin cambio.

---

# 6. A070 — LISTA DE TABLAS

La Lista de Tablas contiene actualmente 24 entradas, pero omite Tabla 3 y mantiene una secuencia desplazada `Tabla 4 ... Tabla 25`.

No cambies la cantidad de párrafos ni los números de página. Corrige exclusivamente las etiquetas numéricas de las 22 entradas afectadas:

```text
Tabla 4  -> Tabla 3
Tabla 5  -> Tabla 4
Tabla 6  -> Tabla 5
...
Tabla 24 -> Tabla 23
Tabla 25 -> Tabla 24
```

Las entradas `Tabla 1` y `Tabla 2` permanecen intactas.

Resultado visible de la lista:

```text
Tabla 1
Tabla 2
Tabla 3
...
Tabla 24
```

sin Tabla 25.

### Marcado A070

En cada entrada afectada, marca únicamente la etiqueta legacy (`Tabla N`) como amarillo + tachado y añade inmediatamente la etiqueta corregida como amarillo no tachado. Preserva guías, tabulaciones y número de página.

Añade un solo comentario Word, ID esperado `469`, anclado a la primera entrada corregida y describiendo la corrección secuencial completa de la Lista de Tablas.

No modifiques números de tablas dentro del cuerpo de la tesis.

---

# 7. A071 — LISTA DE FIGURAS

```text
A071_STATUS = VERIFIED_NO_CHANGE
```

Verifica que la Lista de Figuras conserve exactamente `Figura 1` a `Figura 12` y sus páginas actuales. No renumeres figuras durante REVIEW V03.

No añadas comentario Word.

---

# 8. A072 — ÍNDICE / CAMPOS AUTOMÁTICOS

```text
A072_STATUS = VERIFIED_NO_CHANGE
```

No actualices el Índice general, campos automáticos, numeración de páginas, TOC, List of Figures, campos `SEQ Figura`, encabezados ni pies. No materialices ni recalcules campos.

La única modificación preliminar autorizada en 121M es A070 sobre las etiquetas visibles de la Lista de Tablas.

No añadas comentario Word.

---

# 9. A080 — referencia en 4.1.8

Localiza exclusivamente la frase legacy previa a Tabla 20:

```text
La Tabla 21 resume los hallazgos...
```

Cambia solo el token de referencia:

```text
Tabla 21 -> Tabla 20
```

Preserva todo el resto del párrafo.

Marcado: `Tabla 21` amarillo + tachado; `Tabla 20` amarillo sin tachado.

Añade comentario Word ID esperado `470`.

---

# 10. A081 — referencia en 4.2

Localiza exclusivamente la introducción a la contrastación que contiene:

```text
criterios operacionales definidos en la Tabla 10
```

Cambia solo:

```text
Tabla 10 -> Tabla 9
```

Preserva el resto del párrafo y las disposiciones científicas vigentes ya incorporadas.

Marcado: `Tabla 10` amarillo + tachado; `Tabla 9` amarillo sin tachado.

Añade comentario Word ID esperado `471`.

---

# 11. A082 — referencia en 4.3.5

Localiza exclusivamente la frase:

```text
La Tabla 24 resume las principales convergencias y diferencias.
```

Cambia solo:

```text
Tabla 24 -> Tabla 23
```

Preserva todo el resto del párrafo y no modifiques nuevamente la Tabla 23.

Marcado: `Tabla 24` amarillo + tachado; `Tabla 23` amarillo sin tachado.

Añade comentario Word ID esperado `472`.

---

# 12. A073–A079 — prohibición de reejecución

Estas acciones ya están aplicadas y trazadas en L-R1:

```text
A073 trace = G7F02-V03A-011
A074 trace = G7F02-V03A-012
A075 trace = G7F02-V03B-024
A076 trace = G7F02-V03C-003
A077 trace = G7F02-V03C-024
A078 trace = G7F02-V03E-002
A079 trace = G7F02-V03E-006
```

No vuelvas a editar esos loci, no añadas nuevas filas de trazabilidad y no dupliques comentarios.

---

# 13. Trazabilidad CSV

Parte del CSV L-R1 de 128 filas y conserva las 128 filas heredadas como **prefijo byte-idéntico**.

Añade exactamente ocho filas nuevas, una por cada acción de este bloque, en este orden:

```text
G7F02-V03M-001 -> A068 -> APPLIED
G7F02-V03M-002 -> A069 -> VERIFIED_NO_CHANGE
G7F02-V03M-003 -> A070 -> APPLIED
G7F02-V03M-004 -> A071 -> VERIFIED_NO_CHANGE
G7F02-V03M-005 -> A072 -> VERIFIED_NO_CHANGE
G7F02-V03M-006 -> A080 -> APPLIED
G7F02-V03M-007 -> A081 -> APPLIED
G7F02-V03M-008 -> A082 -> APPLIED
```

Resultado obligatorio:

```text
INHERITED_TRACE_ROWS = 128
NEW_TRACE_ROWS_ADDED = 8
TOTAL_TRACE_ROWS = 136
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true
```

Para acciones `VERIFIED_NO_CHANGE`, registra que la verificación fue realizada y que no hubo cambio visible ni comentario Word.

No modifiques ninguna fila heredada.

---

# 14. Comentarios Word

Estado de entrada:

```text
INHERITED_COMMENT_COUNT = 217
```

Añade exactamente cinco comentarios nuevos:

```text
468 -> A068
469 -> A070
470 -> A080
471 -> A081
472 -> A082
```

No añadas comentario para A069, A071 ni A072.

Resultado esperado:

```text
COMMENTS_ADDED = 5
TOTAL_COMMENT_COUNT = 222
ALL_NONEMPTY_COMMENT_IDS_ANCHORED = true
ALL_217_INHERITED_COMMENTS_UNCHANGED = true
```

No modifiques contenido, metadatos ni anclajes de los 217 comentarios heredados.

---

# 15. Invariantes OOXML y de alcance

Después de ejecutar 121M debe cumplirse:

```text
TABLE_OBJECT_COUNT = 24
TABLES_1_TO_24_OBJECT_IDENTITY_PRESERVED = true
TABLE_23_UNCHANGED_FROM_L_R1 = true
TABLE_24_UNCHANGED_FROM_L_R1 = true
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
ALL_MEDIA_BINARIES_UNCHANGED = true
FIGURE_1_TO_12_BINARIES_UNCHANGED = true
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
NEW_REFERENCES_BIBLIOGRAPHIC = 0
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
A073_A079_REEXECUTED = false
G7_F03_EXECUTED = false
```

No modifiques tablas ni figuras para resolver A068–A082. A070 actúa únicamente sobre la Lista de Tablas preliminar; A080–A082 son reemplazos inline de referencias.

---

# 16. QA visual y estructural

Renderiza el DOCX resultante y revisa al menos:

1. **Lista de Tablas**: secuencia visible 1–24, sin 25; page numbers preservados; no overflow ni desalineación.
2. **4.1.8 / A080**: referencia corregida hacia Tabla 20 y continuidad con Tabla 20.
3. **4.2 / A081**: referencia corregida hacia Tabla 9; no alteración de Tabla 21 ni de la ciencia ya aprobada.
4. **4.3.5 / A082**: referencia corregida hacia Tabla 23; Tabla 23 intacta.
5. **CONCLUSIONES**: ocho conclusiones legibles, legacy amarillo+tachado y nuevo amarillo sin tachado; sin pérdida de párrafos, clipping o solapamiento.
6. **RECOMENDACIONES**: byte/OOXML visible sin cambios respecto de L-R1.
7. límite `RECOMENDACIONES -> REFERENCIAS BIBLIOGRÁFICAS`: sin alteraciones de bibliografía.

Verifica también:

```text
LIST_OF_TABLES_VISIBLE_SEQUENCE = 1..24
LIST_OF_FIGURES_VISIBLE_SEQUENCE = 1..12
CONCLUSIONS_PARAGRAPH_COUNT = 8
RECOMMENDATIONS_VISIBLE_UNCHANGED = true
A080_REFERENCE_CORRECT = true
A081_REFERENCE_CORRECT = true
A082_REFERENCE_CORRECT = true
```

---

# 17. Salidas obligatorias

No sobrescribas L-R1. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_M.docx
g7_thesis_claim_traceability_v0.3_M.csv
```

Calcula y reporta SHA-256 y tamaño de ambos; reporta filas del CSV.

Publica respuesta oficial en:

```text
writing_prompts_tmp/121M_RESPUESTA_G7_F02_V03_BLOQUE_M_CIERRE_CONCLUSIONES_Y_CORRECCIONES_EDITORIALES.md
```

La respuesta debe reportar como mínimo:

```text
PROMPT121M_EXECUTION = COMPLETE | REVISION_REQUIRED | STOPPED_PRECONDITION
A068_APPLIED = true|false
A069_STATUS = VERIFIED_NO_CHANGE | CHANGED
A070_APPLIED = true|false
A071_STATUS = VERIFIED_NO_CHANGE
A072_STATUS = VERIFIED_NO_CHANGE
A080_APPLIED = true|false
A081_APPLIED = true|false
A082_APPLIED = true|false
A073_A079_REEXECUTED = false
INHERITED_TRACE_ROWS = 128
NEW_TRACE_ROWS_ADDED = 8
TOTAL_TRACE_ROWS = 136
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true|false
INHERITED_COMMENT_COUNT = 217
COMMENTS_ADDED = 5
TOTAL_COMMENT_COUNT = 222
ALL_NONEMPTY_COMMENT_IDS_ANCHORED = true|false
ALL_217_INHERITED_COMMENTS_UNCHANGED = true|false
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
LIST_OF_TABLES_VISIBLE_SEQUENCE = 1..24 | FAIL
LIST_OF_FIGURES_VISIBLE_SEQUENCE = 1..12 | FAIL
CONCLUSIONS_PARAGRAPH_COUNT = 8
RECOMMENDATIONS_VISIBLE_UNCHANGED = true|false
A080_REFERENCE_CORRECT = true|false
A081_REFERENCE_CORRECT = true|false
A082_REFERENCE_CORRECT = true|false
NEW_REFERENCES = 0
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
G7_F03_EXECUTED = false
LOCAL_VISUAL_REVIEW = PASS|FAIL
DOCX_M_SHA256 = <hash>
DOCX_M_SIZE = <bytes>
CSV_M_SHA256 = <hash>
CSV_M_SIZE = <bytes>
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

---

# 18. Parada obligatoria

Al finalizar, detente para auditoría externa.

No ejecutes G7-F03 ni ningún bloque posterior.
