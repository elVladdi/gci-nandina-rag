# Related Work B02 — Execution report V01 / Informe de ejecución V01

## Español

### 1. Alcance ejecutado

Se ejecutó exclusivamente `RELATED_WORK_B02 — Section 2.2 Knowledge-enhanced retrieval and regulatory reasoning` sobre el master canónico acumulativo `ARTICLE_MASTER_V001`. No se redactaron ni modificaron científicamente 2.3–2.6, Introduction, Decision-support architecture, Experimental design, Results ni Methods B01 V06.

El baseline binario utilizado fue el master canónico exacto con SHA-256 `08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5`. La sección 2.1 y sus ocho comentarios de auditoría se preservaron antes de insertar 2.2.

### 2. Fuentes científicas re-recuperadas y uso claim-level

Se re-recuperaron y verificaron a texto completo, en la sesión activa, las seis fuentes finalmente citadas:

- `REF-006` — Qi et al. (2025), *Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities*;
- `REF-012` — Lee et al. (2021), *Classification of Goods Using Text Descriptions With Sentences Retrieval*;
- `REF-018` — Lee et al. (2023), *Explainable Product Classification for Customs*;
- `REF-015` — Wang et al. (2026), *Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification*;
- `REF-041` — Lewis et al. (2020), *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*;
- `REF-038` — Ma et al. (2023), *Query Rewriting for Retrieval-Augmented Large Language Models*.

Cada referencia se usó solo para la función que su full text respalda: structured knowledge dentro de la predicción; sentence retrieval que alimenta una predicción posterior; evidence retrieval posterior a la predicción de candidatos; búsqueda jerárquica en la que candidatos/evidencia intervienen en el siguiente salto; RAG como generación condicionada por documentos recuperados; y query rewriting como transformación anterior al retrieval.

No se promovieron claims secundarios atribuidos por esos trabajos a WCO u otras terceras fuentes.

### 3. Síntesis científica y límites preservados

La subsección se organizó por función del conocimiento externo, no paper por paper:

`structured knowledge in prediction → retrieved documents as decision context → candidate-specific supporting evidence → regulation-/hierarchy-driven search → RAG → query transformation → synthesis and transition to 2.3`.

Se conservaron explícitamente las fronteras gobernantes entre code/sentence/precedent/evidence retrieval, entre knowledge used to decide y documentary support, y entre retrieved passages, evidence attribution, grounding, auditability y substantive/legal correctness.

No se introdujeron la arquitectura del estudio actual, Top-3 fijo, resultados propios, NANDINA/Chapter 87, H100, DAM, corpus peruano, claims de novelty universal ni `FINAL_GAP`.

### 4. Preservación acumulativa y QA del Word

El `.docx` final fue producido mediante edición OOXML localizada sobre una copia del baseline binario exacto, sin reconstrucción del documento. Solo se sustituyeron la nota/placeholder de 2.2 en la Parte I y el placeholder de 2.2 en la Parte II.

La preservación de 2.1 se verificó en dos niveles:

1. los bloques XML completos de 2.1 inglesa y española son byte-idénticos entre baseline y candidato;
2. los comentarios de auditoría `0–7`, sus textos, IDs y anclajes permanecen sin modificación (`8/8`).

Para 2.2 se añadieron seis nuevos comentarios Word (`IDs 8–13`), cada uno anclado exactamente a su instancia de cita inglesa. El total del documento es de 14 comentarios.

También se verificó:

- ZIP/OOXML íntegro y XML parseable;
- cero tracked changes;
- texto visible fuera de 2.2 preservado;
- equivalencia Markdown–DOCX de 2.2;
- equivalencia semántica EN–ES;
- render completo de 19 páginas;
- inspección visual de las 19 páginas, sin clipping, solapamientos, pérdida de glifos ni ruptura de layout.

### 5. Checklist obligatorio

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
BLOCK = RELATED_WORK_B02
BLOCK_REVISION = V01
SECTION = 2.2
BASELINE_MASTER = ARTICLE_MASTER_V001
BASELINE_DOCX_SHA256_EXPECTED = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
BASELINE_DOCX_SHA256_VERIFIED = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5 / PASS
SOURCE_SNAPSHOT(S) = [article/main-manuscript@674f55c8573c78cdc01f7eca2b5150b3070fcfb9; ARTICLE_MASTER_V001_MD=14e7e4e0a0a5080c096bfecd5ce2cd104e0a780c; D016=34adc5384de8c1174d38fe73189b9cc5785fadd4; 0B02=55636236193afbd523609f8b0ccee987035d35ef; 0B03B=1bb70fdc93bafb8c883a0383ec2e67fe652cfab2; 0B04B=cde65f51d2959f90c321458cd8fa50073d1ba056; PROMPT=b1a7c338cca4aeab8c2e90e0717bfffe654484ae]
FULLTEXTS_RETRIEVED = [REF-006 Qi et al. 2025; REF-012 Lee et al. 2021; REF-018 Lee et al. 2023; REF-015 Wang et al. 2026; REF-041 Lewis et al. 2020; REF-038 Ma et al. 2023]
AUTHORIZED_CLAIMS_USED = NONE_FROM_PROJECT_CLAIM_EVIDENCE_MATRIX / LITERATURE_CLAIMS_VERIFIED_FROM_PRIMARY_FULLTEXT
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
PRIOR_2_1_TEXT_PRESERVED = PASS
PRIOR_2_1_CITATION_COMMENTS_PRESERVED = 8/8
NEW_CITATION_COMMENT_COVERAGE = 6/6
TOTAL_CITATION_COMMENT_COUNT = 14
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_PROSE_QA = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
MASTER_CANDIDATE_MD = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B02_V01.md
MASTER_CANDIDATE_DOCX = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B02_V01.docx
DOCX_OOXML_INTEGRITY = PASS
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS / 19_OF_19_PAGES_VISUALLY_INSPECTED
MD_DOCX_EQUIVALENCE = PASS
ENGLISH_SECTION_2_2_WORD_COUNT = 788
FINAL_DOCX_SHA256 = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```

### 6. Observación documental no bloqueante

`ARTICLE_WRITING_PLAN.md` conserva una línea histórica que todavía identifica B01/2.1 como bloque autorizado. No se modificó. El gate vigente para B02 está definido de forma posterior y específica por `ARTICLE_STATUS.md`, D-016 y el prompt B02 ejecutado.

---

## English

### 1. Executed scope

Only `RELATED_WORK_B02 — Section 2.2 Knowledge-enhanced retrieval and regulatory reasoning` was drafted on top of the canonical cumulative `ARTICLE_MASTER_V001`. Sections 2.3–2.6, Introduction, Decision-support architecture, Experimental design, Results, and Methods B01 V06 were not drafted or scientifically modified.

The exact canonical DOCX baseline was verified at SHA-256 `08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5`. Approved Section 2.1 and its eight citation-audit comments were preserved before Section 2.2 was inserted.

### 2. Full-text verification and claim-level use

Six cited sources were re-retrieved and checked at full-text level during the active session: REF-006, REF-012, REF-018, REF-015, REF-041, and REF-038. Each was used only for the function supported by its primary text: structured knowledge inside prediction; sentence retrieval feeding a later prediction; candidate-specific evidence retrieval after prediction; regulation-aware hierarchical search; retrieval-conditioned generation; and query rewriting before retrieval.

No secondary WCO or other third-party claims inherited through these papers were promoted to manuscript facts.

### 3. Scientific synthesis

The subsection is organized by the function played by external knowledge rather than by author chronology. It preserves the distinctions among code/sentence/precedent/evidence retrieval; knowledge used to decide versus documentary support; and retrieved passages, attribution, grounding, auditability, and substantive/legal correctness.

No present-study architecture, fixed Top-3, experimental findings, NANDINA/Chapter 87, H100, DAM, Peruvian corpus, universal novelty, or final-gap claims were introduced.

### 4. Cumulative Word preservation and QA

The final DOCX was produced through localized OOXML editing of the exact baseline, not by reconstructing the document. Only the English and Spanish Section-2.2 placeholders were replaced.

The complete English and Spanish Section-2.1 XML blocks remain byte-identical to the baseline. The eight pre-existing citation comments retain the same IDs, text, and anchors. Six new comments were added to the six English citation instances, for 14 total comments.

OOXML integrity, zero tracked changes, visible-text preservation outside Section 2.2, Markdown–DOCX equivalence, EN–ES semantic equivalence, 19-page rendering, and visual inspection of all 19 pages passed.

### 5. Delivery state

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
BLOCK = RELATED_WORK_B02
BLOCK_REVISION = V01
SECTION = 2.2
BASELINE_MASTER = ARTICLE_MASTER_V001
BASELINE_DOCX_SHA256_VERIFIED = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5 / PASS
ACCESS_RECHECK_REQUIRED = NONE
PRIOR_2_1_TEXT_PRESERVED = PASS
PRIOR_2_1_CITATION_COMMENTS_PRESERVED = 8/8
NEW_CITATION_COMMENT_COVERAGE = 6/6
TOTAL_CITATION_COMMENT_COUNT = 14
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_PROSE_QA = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
DOCX_OOXML_INTEGRITY = PASS
DOCX_RENDER = PASS / 19_OF_19_PAGES_VISUALLY_INSPECTED
MD_DOCX_EQUIVALENCE = PASS
ENGLISH_SECTION_2_2_WORD_COUNT = 788
FINAL_DOCX_SHA256 = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```
