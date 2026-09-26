# D-054 — Experimental Design B02 V02 author approval and V011 authorization

## Español

```text
DECISION_ID = D-054
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B02
PARENT_DECISION = D-053
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B02_V02_NARROW_COHERENCE_CORRECTION_INTERNAL_REVIEW_V01.md@5e87dc19d8ee74fb2e9ebbe079b074e513135b13
AUTHOR_DECISION = APPROVED
SCIENTIFIC_REVIEW = PASS
NARROW_COHERENCE_CORRECTION_REVIEW = PASS
DOCX_QA = PASS
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
APPROVED_MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md
APPROVED_MASTER_CANDIDATE_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
APPROVED_MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_MASTER_CANDIDATE_DOCX_SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
CANONICAL_CITATION_COMMENTS_AFTER_B02 = 40
TRACKED_CHANGES = 0
ARTICLE_MASTER_V011 = AUTHORIZED / NOT_YET_MATERIALIZED
SECTION_4_4 = ELIGIBLE_AFTER_V011_INTEGRATION / NOT_YET_AUTHORIZED
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Decisión autoral

El autor aprobó expresamente `Experimental Design B02 V02` después del PASS independiente de la IA Gestora. La aprobación comprende Section 4.3 y las correcciones estrechas de coherencia autorizadas por D-053.

Quedan aprobados y congelados para integración:

- Section 4.3 `Documentary corpus and evidence resource`;
- la identificación del recurso jerárquico NANDINA derivado de Decision 885;
- la asociación documental mediante lookup exacto NANDINA-8 para cada candidato del Top-3 ya fijado;
- la ausencia de query-based normative retrieval, score fusion, reranking, inserción o sustitución de candidatos en la ruta primaria;
- la invariabilidad del Top-3 downstream;
- la divulgación de la frontera temporal/versionado frente a Decision 906;
- la separación conceptual entre contexto administrativo peruano y recurso documental andino;
- la actualización acumulativa del rótulo `KBS_ARTICLE_WORKING_STRUCTURE_V01` a `KBS_ARTICLE_WORKING_STRUCTURE_V02`.

La aprobación no abre contenido científico de Section 4.4 ni posteriores.

### 2. Artefactos aprobados

```text
CUMULATIVE_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md
SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f

CUMULATIVE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx
SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
```

La identidad de ambos artefactos fue verificada independientemente en la auditoría diferencial previa. La aprobación autoral preserva exactamente esos artefactos y no autoriza regeneración, normalización ni reescritura.

### 3. Integración y promoción

Se autoriza materializar, sin modificación de contenido, el Markdown acumulativo exacto aprobado como:

`article/manuscript/ARTICLE_MASTER_V011.md`

La integración solo podrá declararse completada después de verificar la identidad exacta del artefacto materializado contra el SHA-256 aprobado y registrar el Git blob resultante. D-023, D-032 y D-035 permanecen vinculantes: no se autoriza Base64 manual, fragmentación, chunking, recomposición, reconstrucción desde DOCX ni regeneración del Markdown.

El DOCX aprobado permanece bajo custodia local efectiva del autor conforme a D-021/D-027 y se convierte en el próximo baseline acumulativo únicamente después de la verificación de integración.

### 4. Gate posterior

La aprobación autoral autoriza la integración, pero no la sustituye.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_V011_CANONICAL_INTEGRATION
NEXT_ACTOR = IA_GESTORA / TECHNICAL_INTEGRATION_ONLY
SECTION_4_4 = ELIGIBLE_AFTER_INTEGRATION / NOT_AUTHORIZED
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Después de verificar V011, la IA Gestora deberá emitir una decisión separada de integración. Solo entonces podrá evaluar la apertura del siguiente bloque atómico elegible bajo la estructura y el estado experimental vigentes.

---

## English

```text
DECISION_ID = D-054
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B02
PARENT_DECISION = D-053
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B02_V02_NARROW_COHERENCE_CORRECTION_INTERNAL_REVIEW_V01.md@5e87dc19d8ee74fb2e9ebbe079b074e513135b13
AUTHOR_DECISION = APPROVED
SCIENTIFIC_REVIEW = PASS
NARROW_COHERENCE_CORRECTION_REVIEW = PASS
DOCX_QA = PASS
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
APPROVED_MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md
APPROVED_MASTER_CANDIDATE_MD_SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f
APPROVED_MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_MASTER_CANDIDATE_DOCX_SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
CANONICAL_CITATION_COMMENTS_AFTER_B02 = 40
TRACKED_CHANGES = 0
ARTICLE_MASTER_V011 = AUTHORIZED / NOT_YET_MATERIALIZED
SECTION_4_4 = ELIGIBLE_AFTER_V011_INTEGRATION / NOT_YET_AUTHORIZED
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Author decision

The author expressly approved `Experimental Design B02 V02` after the independent PASS issued by the IA Gestora. The approval covers Section 4.3 and the narrow coherence corrections authorized by D-053.

The following are approved and frozen for integration: Section 4.3; the hierarchical NANDINA resource derived from Decision 885; exact NANDINA-8 lookup for each already-fixed Top-3 candidate; the absence of query-based normative retrieval, score fusion, reranking, candidate insertion, or substitution in the primary path; downstream Top-3 invariance; disclosure of the temporal/version boundary relative to Decision 906; the distinction between the Peruvian administrative context and the Andean documentary resource; and the cumulative update from `KBS_ARTICLE_WORKING_STRUCTURE_V01` to `KBS_ARTICLE_WORKING_STRUCTURE_V02`.

This approval does not authorize scientific content for Section 4.4 or any later section.

### 2. Approved artifacts

```text
CUMULATIVE_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.md
SHA256 = ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f

CUMULATIVE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx
SHA256 = d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf
CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
```

The identity of both artifacts was independently verified in the preceding differential review. Author approval preserves those exact artifacts and does not authorize regeneration, normalization, or rewriting.

### 3. Integration and promotion

The exact approved cumulative Markdown is authorized for materialization, without content modification, as:

`article/manuscript/ARTICLE_MASTER_V011.md`

Integration may only be declared complete after exact artifact identity is verified against the approved SHA-256 and the resulting Git blob is recorded. D-023, D-032, and D-035 remain binding: manual Base64, fragmentation, chunking, recomposition, reconstruction from DOCX, and Markdown regeneration are prohibited.

The approved DOCX remains under effective local author custody under D-021/D-027 and becomes the next cumulative baseline only after integration verification.

### 4. Subsequent gate

Author approval authorizes integration but does not replace it.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_V011_CANONICAL_INTEGRATION
NEXT_ACTOR = IA_GESTORA / TECHNICAL_INTEGRATION_ONLY
SECTION_4_4 = ELIGIBLE_AFTER_INTEGRATION / NOT_AUTHORIZED
SECTION_4_5_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

After V011 is verified, the IA Gestora must issue a separate integration decision. Only then may the next eligible atomic block be evaluated for opening under the governing structure and current experimental state.