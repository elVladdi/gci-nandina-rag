# Methods B01 — Revisión interna V05 / Internal Review V05

## Español

### Dictamen

```text
REVIEW_ID = METHODS_B01_INTERNAL_REVIEW_V05
DELIVERY_COMMIT = 1e5c6fe2fc89b9f819b0555478bcca179c3a1bc3
KBS_GUIDE = KBS_EWG_34_V01
GUIDE_APPROVAL = D-013
METHODS_B01_V05_INTERNAL_REVIEW = PASS
SCIENTIFIC_CONTENT_REVIEW = PASS / PREVIOUS_PASS_RETAINED
KBS_EDITORIAL_FIT = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
B01_M09 = CLOSED
B01_M10 = CLOSED
B01_M11 = CLOSED
B01_M12 = CLOSED
B01_M13 = CLOSED
AUTHOR_REVIEW_READY = YES
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### 1. Alcance de la auditoría

Se auditó independientemente la entrega V05 de `Methods B01 — 3.1 Design, scope, and units` contra el protocolo vigente, la Claim–Evidence Matrix, la guía empírica KBS-34 aprobada mediante D-013, la reauditoría editorial V03 y el alcance científico previamente validado.

El commit de entrega `1e5c6fe2fc89b9f819b0555478bcca179c3a1bc3` modifica exclusivamente los cuatro artefactos autorizados para V05:

1. `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V05.md`;
2. `article/sections/methods/Methods_B01_V05.md`;
3. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.md`;
4. `article/manuscript/ARTICLE_MASTER_CANDIDATE_V05.docx`.

No se detectó avance a B02 ni modificación de gobernanza, matrices científicas, revisiones previas o Plan Maestro.

### 2. Auditoría científica y de claims

La V05 conserva el alcance científico validado en V03 y utiliza únicamente los claims autorizados `[C01, C02, C03, C07, C15]`:

- la recuperación histórica genera y ordena candidatos y fija el Top-3 antes de la recuperación normativa;
- la recuperación normativa aporta evidencia para candidatos ya fijados y no cambia el ranking;
- el LLM local opera después de la recuperación y su salida no retroalimenta la selección o ranking;
- la DAM se conserva como unidad de agrupamiento cuando la dependencia entre series es metodológicamente relevante;
- la configurabilidad se presenta como propiedad de diseño/replicación, no como generalización empírica.

No se introducen resultados de Grupo 3, métricas, causalidad, novelty final, superioridad, clasificación jurídicamente vinculante ni generalización fuera del piloto evaluado.

### 3. Auditoría editorial KBS-34

#### B01-M10 — CLOSED

El primer párrafo ya no enumera exhaustivamente todas las prohibiciones finas del LLM. Mantiene únicamente las invariantes necesarias para comprender el flujo en 3.1: Top-3 fijado antes de evidencia normativa, evidencia sin reranking y ausencia de feedback del LLM al ranking. La descripción sigue una secuencia operacional clara.

#### B01-M11 — CLOSED

La prosa abandona el tono dominante de especificación/gobernanza. `functional contract` se utiliza una sola vez y solo después de describir operaciones observables. Predominan relaciones concretas de entrada–operación–salida y agentes identificables.

#### B01-M12 — CLOSED

La configurabilidad queda acompañada por precondiciones explícitas: banco histórico etiquetado alineado con el universo de clases, universo objetivo definido, corpus documental/normativo compatible e interfaces coherentes de representación e identificación. Además, se excluyen explícitamente la interoperabilidad automática y la transferencia del desempeño empírico.

#### B01-M13 — CLOSED

La frontera experimental se formula en términos concretos: piloto offline de NANDINA Chapter 87 y versiones específicas de los datos históricos, corpus documental y configuración utilizadas en ese piloto. Se eliminó la enumeración abstracta de categorías de alcance de V03.

### 4. Unidades y secuencia metodológica

La subsección conserva de forma clara:

- método general antes del testbed;
- consulta = descripción comercial normalizada de una serie;
- recuperación histórica → Top-k → Top-3 histórico fijo;
- recuperación normativa posterior para esos candidatos;
- LLM local posterior para explicación controlada;
- ranking, evidencia y explicación como funciones diferenciadas;
- serie = unidad de observación y análisis;
- DAM = unidad de agrupamiento cuando corresponda por dependencia;
- NANDINA Chapter 87 = instancia experimental evaluada, no alcance conceptual completo.

### 5. Equivalencia bilingüe

La parte española preserva el mismo alcance, grado de certeza, secuencia funcional, límites de configurabilidad, unidad analítica y frontera experimental que la versión inglesa.

```text
EN_ES_SEMANTIC_EQUIVALENCE = PASS
```

No se considera material la permanencia de términos técnicos ingleses de uso interno como `Methods` o `pipeline` en el espejo español; no altera contenido científico ni requiere una nueva revisión.

### 6. Auditoría técnica del DOCX — B01-M09

Se verificó independientemente el archivo Word entregado y se obtuvo:

```text
DOCX_SHA256 = 77c8cb0121f50ff51507c59d32f4a66f32e198143777285a4d5b7cb62013ba76
DOCX_ZIP_INTEGRITY = PASS
DOCX_DOCUMENT_XML = PRESENT
DOCX_COMMENTS = 0
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS
RENDERED_PAGES = 2
MD_DOCX_VISIBLE_TEXT_EQUIVALENCE = PASS
```

El SHA-256 verificado coincide con el reportado por la IA de Redacción. El paquete OOXML abre correctamente, contiene `word/document.xml`, no contiene comentarios ni revisiones rastreadas y se renderiza sin errores. La página 1 contiene el master inglés y la página 2 el espejo español, sin defectos visibles de maquetación que bloqueen la revisión.

Por tanto, `B01-M09` queda cerrada.

### 7. Estado experimental observado, sin consumo de resultados

Durante esta auditoría se verificó que la rama viva del Plan Maestro se encuentra en:

```text
SRC03_LIVE_HEAD = 96cccb9a61f42ab97b1eba607524e33f992740f6
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
NEXT_ELIGIBLE_FICHA = G3-F04
G3_F04 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

V05 no utiliza ningún resultado, métrica o inferencia de Grupo 3, por lo que este avance experimental no activa revisión experimental del bloque 3.1.

### 8. Gate

```text
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
METHODS_B01_V05_INTERNAL_REVIEW = PASS
AUTHOR_REVIEW_READY = YES
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
NEXT_ACTOR = AUTHOR
```

El `PASS` interno no equivale a aprobación del autor, integración canónica ni freeze. B02 permanece bloqueado hasta la decisión expresa del autor sobre V05 y el cierre editorial correspondiente.

---

## English

### Verdict

```text
REVIEW_ID = METHODS_B01_INTERNAL_REVIEW_V05
DELIVERY_COMMIT = 1e5c6fe2fc89b9f819b0555478bcca179c3a1bc3
KBS_GUIDE = KBS_EWG_34_V01
GUIDE_APPROVAL = D-013
METHODS_B01_V05_INTERNAL_REVIEW = PASS
SCIENTIFIC_CONTENT_REVIEW = PASS / PREVIOUS_PASS_RETAINED
KBS_EDITORIAL_FIT = PASS
MATERIAL_SCIENTIFIC_ERRORS = 0
B01_M09 = CLOSED
B01_M10 = CLOSED
B01_M11 = CLOSED
B01_M12 = CLOSED
B01_M13 = CLOSED
AUTHOR_REVIEW_READY = YES
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

The V05 delivery was independently audited against the current protocol, Claim–Evidence Matrix, the author-approved KBS-34 empirical writing guide, the V03 KBS editorial reaudit, and the previously validated scientific scope.

The delivery commit changes only the four authorized V05 artifacts and does not advance B02 or modify governance, scientific matrices, prior reviews, or the experimental Master Plan.

The scientific scope remains bounded to claims C01, C02, C03, C07, and C15. Historical retrieval generates/ranks candidates and fixes the Top-3 before normative retrieval; normative retrieval supplies evidence without changing the ranking; the local LLM operates downstream and does not feed generated output back into candidate selection or ranking; DAM remains the grouping unit when dependence is methodologically relevant; and configurability is stated only as a bounded design/replication property rather than empirical generalization.

The KBS-specific corrections B01-M10 through B01-M13 are closed. The opening architecture overview is less dense, `functional contract` is used only after observable operations are explained, configurability is tied to explicit resource/interface preconditions, and the empirical boundary is stated concretely as the Chapter 87 offline pilot and the specific data/corpus/configuration versions used in that pilot.

The English and Spanish versions are semantically equivalent. Minor internal lexical carryover such as `Methods` or `pipeline` in the Spanish mirror is non-material and does not warrant another revision.

The DOCX was independently verified with SHA-256 `77c8cb0121f50ff51507c59d32f4a66f32e198143777285a4d5b7cb62013ba76`. ZIP/OOXML integrity passes, `word/document.xml` is present, comments and tracked changes are absent, the file renders successfully as two pages, and visible text matches the Markdown candidate. B01-M09 is therefore closed.

The live experimental Master Plan was observed at `96cccb9a61f42ab97b1eba607524e33f992740f6`, with Group 3 in progress through integrated G3-F03 and G3-F04 eligible but not authorized/executed. V05 consumes no Group 3 result, metric, or inference, so no experimental-review trigger is present for this Methods 3.1 review.

```text
METHODS_B01 = READY_FOR_AUTHOR_REVIEW
METHODS_B01_V05_INTERNAL_REVIEW = PASS
AUTHOR_REVIEW_READY = YES
AUTHOR_APPROVAL_METHODS_B01_V05 = PENDING
MASTER_INTEGRATION = NOT_AUTHORIZED
B02 = NOT_AUTHORIZED
NEXT_ACTOR = AUTHOR
```

Internal PASS does not constitute author approval, canonical integration, or freeze. B02 remains blocked pending the author's explicit decision on V05.