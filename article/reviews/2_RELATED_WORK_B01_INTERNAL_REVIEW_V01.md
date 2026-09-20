# Related Work B01 — Internal Review V01 / Revisión interna V01

## Español

```text
REVIEW_ID = RELATED_WORK_B01_INTERNAL_REVIEW_V01
REVIEW_DATE = 2026-09-19
BLOCK = RELATED_WORK_B01
SECTION = 2.1 Automated tariff classification and candidate retrieval
DELIVERY_COMMIT = 9a3acddeee01bd3c78f1b06306b8619a9ad5ccd6
INTERNAL_REVIEW = PASS
SCIENTIFIC_CONTENT = PASS
SOURCE_SUPPORT = PASS
KBS_EDITORIAL_FIT = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
DOCX_INTEGRITY = PASS
CITATION_COMMENT_COVERAGE = 8/8 / PASS
MATERIAL_CORRECTIONS_REQUIRED = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = RECEIVED
INTEGRATION = AUTHORIZED
```

### 1. Alcance y disciplina de entrega

Se verificó el commit de entrega contra su padre `6b32f09b4c4b7cc97eea164b122739f6d8d02184`. La IA de Redacción produjo exclusivamente los cuatro artefactos autorizados: bloque 2.1 bilingüe, master candidato Markdown, master candidato DOCX e informe de respuesta. No inició 2.2 ni otras secciones y no modificó gobernanza, literatura congelada, estado editorial ni Plan Maestro experimental.

### 2. Auditoría científica y bibliográfica

La subsección organiza la literatura por función de tarea —clasificación directa, representación/predicción jerárquica, recuperación/ranking de candidatos y validación/corrección— y no como inventario autor por autor. Las ocho citas fueron recontrastadas de forma independiente con sus full texts. El soporte es suficiente para los claims atribuidos a Ding et al. (2015), Luppes (2019), Ruder (2020), Anggoro et al. (2025), Lee et al. (2021), Stassin et al. (2023), Pain (2021) y Spichakova & Haav (2020).

La redacción conserva las fronteras gobernantes: no homogeneiza Top-k con accuracy de clasificación; distingue generación/ranking de candidatos de validación de un código ya asignado; no presenta evidencia documental como corrección jurídica; no declara novelty universal ni `FINAL_GAP`; no introduce resultados del estudio actual, H100, Chapter 87, corpus peruano, DAM ni el Top-3 fijo de la arquitectura propuesta.

No se identificaron errores científicos materiales ni afirmaciones que excedan el alcance de las fuentes.

### 3. Auditoría editorial KBS-34

La sección cumple la función narrativa prevista y mejora sustancialmente respecto del problema detectado en el antiguo Methods-first: la prosa es concreta, las transiciones son funcionales y la síntesis progresa por familias de tarea. El último párrafo prepara 2.2 sin anticipar el posicionamiento definitivo del artículo.

Se registran dos controles no bloqueantes para las siguientes subsecciones:

1. `has most often been framed` debe mantenerse como síntesis cualitativa del corpus revisado, no reutilizarse posteriormente como afirmación cuantitativa de prevalencia;
2. en Results/Methods futuros, `Top-k` deberá nombrarse con su métrica exacta; la presencia en el corte Top-k no sustituye métricas sensibles al orden como MRR.

Ninguno exige V02 de B01.

### 4. Auditoría independiente del Word

Se verificó el DOCX entregado de forma independiente:

```text
FINAL_DOCX_SHA256 = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
OOXML_ZIP_INTEGRITY = PASS
WORD_DOCUMENT_XML = PRESENT
COMMENTS_XML = PRESENT
COMMENT_RANGE_START = 8
COMMENT_RANGE_END = 8
COMMENT_REFERENCE = 8
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
RENDER = PASS / 16_OF_16_PAGES_INSPECTED
LAYOUT_DEFECTS = NONE
```

Los ocho comentarios están anclados a las ocho instancias de cita inglesas correspondientes. El texto visible fuera de 2.1 se preservó. El conteo inglés de 2.1 es 587 palabras, dentro del rango orientativo del prompt.

El cover interno conserva aún etiquetas heredadas de la base estructural (`Working Article Structure`). Esto es metadato de trabajo no científico y no invalida B01; deberá normalizarse mediante una operación controlada de master/formato, no mediante una reescritura científica de la subsección aprobada.

### 5. Dictamen y gate

El autor comunicó aprobación expresa de esta versión condicionada a la auditoría interna. Al resultar la auditoría `PASS`, la aprobación queda efectiva.

```text
RELATED_WORK_B01_V01 = APPROVED / FROZEN / READY_FOR_INTEGRATION
AUTHOR_APPROVAL = EFFECTIVE
BLOCK_REVISION_V02 = NOT_REQUIRED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
NEXT_ELIGIBLE_SECTION_AFTER_INTEGRATION = 2.2 Knowledge-enhanced retrieval and regulatory reasoning
```

---

## English

The delivery was independently audited against the governing prompt, frozen literature maps, primary full texts, KBS-34 editorial guide, and cumulative DOCX requirements. Scope discipline passed; all eight cited claims are supported by rechecked primary full texts; no present-study results, prohibited novelty/gap statements, or premature testbed details were introduced. The English/Spanish mirror is semantically equivalent.

The DOCX independently passed ZIP/OOXML integrity, eight-of-eight citation-comment anchors, zero tracked changes, full 16-page rendering, and visual inspection without layout defects. SHA-256 is `08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5`.

Two non-blocking watch items are recorded: the opening prevalence wording is qualitative rather than a frequency estimate, and future evaluation text must use exact metric names rather than treating all Top-k/rank-sensitive measures as interchangeable.

Because the author had already approved V01 subject to this audit, the PASS makes that approval effective. B01 requires no V02 and is eligible for canonical integration; Section 2.2 may open only after that integration.