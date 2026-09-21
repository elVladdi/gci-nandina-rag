# D025 — Related Work B06 approval, integration, and Introduction start

## Español

### Estado

```text
DECISION = D-025
RELATED_WORK_B06_V01 = APPROVED / FROZEN / INTEGRATED
RELATED_WORK = CLOSED / APPROVED / FROZEN
B06_DELIVERY_COMMIT = f8756f5ed6ebed98a567186035082db96b618032
B06_INTERNAL_REVIEW_V01 = PASS
B06_INTERNAL_REVIEW_V02 = PASS / TECHNICAL_PAGE_COUNT_CORRECTION_ONLY
B06_AUTHOR_APPROVAL = RECEIVED
CANONICAL_MASTER_MD = ARTICLE_MASTER_V006.md
CANONICAL_MASTER_MD_GIT_BLOB = 7d3c7a71cd6578ffc0b93df80ea12e4172833a1a
CANONICAL_MASTER_DOCX = LOCAL_AUTHOR_CUSTODY / D021
CANONICAL_MASTER_DOCX_SOURCE_FILENAME = ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx
CANONICAL_MASTER_DOCX_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
CANONICAL_CITATION_COMMENTS = 36
INTRODUCTION_B01 = AUTHORIZED / ACTIVE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Base de la decisión

Related Work B06 V01 fue ejecutado en `f8756f5ed6ebed98a567186035082db96b618032`, auditado independientemente por la IA Gestora y aprobado expresamente por el autor. La revisión concluyó `PASS` para soporte de fuentes primarias, control de alcance, posicionamiento, equivalencia EN–ES y prosa KBS/SPCCR.

La revisión V01 contenía una única transcripción técnica incorrecta en el conteo de páginas renderizadas del DOCX. `2_RELATED_WORK_B06_INTERNAL_REVIEW_V02.md` corrige el campo a `PASS / 28_OF_28_PAGES`, en concordancia con la respuesta de ejecución. El dictamen científico permanece sin cambios.

### 2. Promoción del master

El Markdown acumulativo aprobado de B06 se promueve sin cambios a:

`article/manuscript/ARTICLE_MASTER_V006.md`

La promoción reutiliza exactamente el blob Git del candidato B06:

`7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`

Conforme a D-021, el DOCX aprobado permanece bajo custodia local del autor:

`ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx`

SHA-256 gobernante:

`3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`

El binario reporta 36 comentarios de auditoría, cero tracked changes, integridad OOXML `PASS` y render `28/28 PASS`. Puede renombrarse localmente como `ARTICLE_MASTER_V006.docx` únicamente si permanece byte-for-byte idéntico.

### 3. Cierre de Related Work

Quedan aprobadas, congeladas e integradas las Sections 2.1–2.6. El cierre conserva las fronteras científicas acumuladas, en particular:

- `candidate retrieval ≠ overall classification accuracy`;
- `normative association ≠ substantive/legal correctness`;
- `auditability ≠ legal correctness`;
- `configurability/replicability ≠ empirical generalization`;
- diferencia arquitectónica ≠ novelty por sí misma.

El posicionamiento final de Related Work reconoce prior art parcial y cercano. `FINAL_GAP` continúa `NOT_DEFINED` y `NOVELTY` continúa `NOT_DECLARED`.

### 4. Apertura de Introduction B01

Se cumple el gate definido en el Writing Plan: Related Work está suficientemente estable y las RQs/contribución provisional están autorizadas por 0C. Se autoriza exclusivamente una **Introduction provisional**.

La Introduction debe seguir este orden narrativo:

`problema concreto → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones acotadas → contexto de evaluación → RQs → roadmap`.

La propuesta debe explicar de manera concreta que:

1. la recuperación histórica fija el ranking y un Top-3;
2. la recuperación normativa documenta esos candidatos sin modificarlos;
3. un LLM local downstream produce explicación sin autoridad para insertar, eliminar, sustituir, reordenar ni retroalimentar la clasificación;
4. las funciones se evalúan por separado y la partición respeta DAM cuando existe dependencia.

La Introduction puede presentar la arquitectura como **configurable/replicable** respecto del banco histórico, espacio de clases y corpus documental, pero no puede transformar esa propiedad en evidencia de generalización empírica.

### 5. Límites del bloque

Introduction B01 no está autorizada a:

- declarar `first`, `novel`, `unique`, `unprecedented` o ausencia universal de prior art;
- declarar SOTA o superioridad cross-study;
- presentar resultados o cifras de desempeño del estudio;
- convertir la contribución provisional de 0C en novelty final;
- convertir evidencia normativa o explicaciones trazables en legal correctness;
- abrir Decision-support architecture, Experimental design, Results, Discussion o Conclusion;
- reescribir Related Work 2.1–2.6.

El testbed específico debe aparecer solo después de que la propuesta y contribuciones sean comprensibles. No debe definir el alcance conceptual de la arquitectura.

---

## English

Related Work B06 V01 passed independent review and explicit author approval. Sections 2.1–2.6 are now closed, approved, frozen, and integrated. The cumulative Markdown is promoted unchanged to `ARTICLE_MASTER_V006.md` by reusing Git blob `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`. Under D-021, the approved cumulative DOCX remains in author-local custody with SHA-256 `3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0` and 36 citation-audit comments.

The V02 internal review corrects only a page-count transcription in V01: the execution report records a complete `28/28` render inspection. The scientific `PASS` is unchanged.

Introduction B01 is now the only authorized drafting scope. It must move from the concrete decision-support problem to the verified limitation, high-level proposal, bounded contributions, evaluation context, final retained RQs, and roadmap. It must make the separation between historical ranking, post-ranking normative evidence, and explanation-only local generation explicit without declaring absolute novelty or empirical generalization. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain unchanged.
