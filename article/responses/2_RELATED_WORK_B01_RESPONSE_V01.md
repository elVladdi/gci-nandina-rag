# Related Work B01 — Execution report V01 / Informe de ejecución V01

## Español

### 1. Alcance ejecutado

Se ejecutó exclusivamente `RELATED_WORK_B01 — Section 2.1 Automated tariff classification and candidate retrieval` sobre la estructura acumulativa aprobada. No se redactaron ni modificaron científicamente 2.2–2.6, Introduction, Decision-support architecture, Experimental design, Results ni Methods B01 V06.

El baseline binario proporcionado en la sesión fue `KBS_ARTICLE_WORKING_STRUCTURE_V01(1).docx`. El sufijo de adjunto no se interpretó como versión científica distinta: su SHA-256 coincide exactamente con el baseline aprobado `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`.

### 2. Fuentes y verificación full-text

Las ocho referencias citadas en 2.1 fueron recuperadas nuevamente a texto completo desde los PDF disponibles en la sesión, verificadas por identidad y contrastadas contra las matrices congeladas 0B-01/0B-02. Para cada instancia de cita se localizó un pasaje original de respaldo y se incorporó un comentario Word anclado exactamente a la cita inglesa.

`0B04A` se utilizó como control metodológico de terminología —clasificación, candidate retrieval/ranking y métricas no intercambiables—, sin introducir sus fundamentos IR generales como citas científicas innecesarias en 2.1.

### 3. QA científico-editorial

La subsección se organizó por familias de tarea y no por secuencia de autores: clasificación directa → representación y predicción jerárquica por etapas → retrieval/ranking de candidatos → validation/correction → síntesis de transición hacia 2.2.

No se introdujeron claims del estudio actual, resultados experimentales propios, H100, Chapter 87, corpus peruano, DAM, Top-3 fijo de la arquitectura propuesta, novelty universal ni `FINAL_GAP`.

La sección diferencia explícitamente:

- `direct classification` de `candidate retrieval/ranking`;
- Top-k/ranking de classification accuracy;
- predicción desde una descripción sin código de validation/correction de un código previamente asignado;
- conocimiento documental que participa en una decisión de clasificación de retrieval utilizado como función de apoyo, dejando la discusión de conocimiento/regulación para 2.2.

### 4. QA del Word acumulativo

El `.docx` final se obtuvo editando una copia del baseline binario exacto, no reconstruyéndolo. Solo se sustituyeron la nota/placeholder de 2.1 en la Parte I y el placeholder de 2.1 en la Parte II. El texto visible fuera de esos cuerpos fue comparado programáticamente con el baseline y permaneció idéntico.

Se verificó:

- ZIP/OOXML íntegro;
- `word/document.xml` presente;
- ocho comentarios Word y ocho anclajes start/end/reference;
- cero tracked changes;
- render completo de 16 páginas con LibreOffice;
- equivalencia visual pixel a pixel entre el paquete candidato previo a normalización OOXML y el paquete final compacto;
- inspección visual de las 16 páginas sin clipping, solapamientos ni ruptura de layout;
- equivalencia visible Markdown–DOCX para 2.1;
- equivalencia semántica EN–ES.

### 5. Checklist

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
STRUCTURE_DECISION = D-015
BLOCK = RELATED_WORK_B01
BLOCK_REVISION = V01
SECTION = 2.1
BASELINE_DOCX_SHA256_EXPECTED = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
BASELINE_DOCX_SHA256_VERIFIED = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5 / PASS
SOURCE_SNAPSHOT(S) = [article/main-manuscript@6b32f09b4c4b7cc97eea164b122739f6d8d02184; KBS_STRUCTURE_MD=7f772ffbbf1b25bfd3e4e8ed255c15b4c4504145; 0B01=644483ac6bed8c3a5df572a2ab53db698568e2fe; 0B04A=6c8bbf48fd64aac87b54374a8c9af8ce7b1945f0; 0B02=55636236193afbd523609f8b0ccee987035d35ef; PROMPT=37c6ef12dcb5c5076e1685384ddfd4185888b57b]
FULLTEXTS_RETRIEVED = [REF-007 Ding et al. 2015 SHA256=27dc3898184bbbd37a7c45a0448ab0deade04c731e48e449ddb7395cce4ccfbb; REF-013 Luppes 2019 SHA256=314a0faf6614089d15b5d20b5460d6c1a5b5bee9f5d27ad0dc78ccf54bde78b8; REF-005 Ruder 2020 SHA256=2ac1debae882ae0ac3f817f22928b8a290dfd9a79189505d197cb79d184e1940; REF-024 Anggoro et al. 2025 SHA256=c75ced226933c0c4b82d18f0f16b5d1e219c6864c003ec485afcda4ee2124137; REF-012 Lee et al. 2021 SHA256=2d6989ffcd04ee8f3436df7d828fe89e47cd56db4cf697d7a3be9abd267137d6; REF-011 Stassin et al. 2023 SHA256=f9edb4bfdb57a91347d35c44a20da32285b087277b096485043527c0b6bb2f9e; REF-019 Pain 2021 SHA256=7132f90ac656b670bba8943c8d13203c51764271a974a76bfdd199adde83968c; REF-004 Spichakova & Haav 2020 SHA256=505f484b82cf466943947232022365b753e6ad6b4f10334fc0bfc8f6f3ba4031]
AUTHORIZED_CLAIMS_USED = NONE_FROM_PROJECT_CLAIM_EVIDENCE_MATRIX / LITERATURE_CLAIMS_VERIFIED_FROM_PRIMARY_FULLTEXT
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 8/8
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_PROSE_QA = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
MASTER_CANDIDATE_MD = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B01_V01.md
MASTER_CANDIDATE_DOCX = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B01_V01.docx
DOCX_OOXML_INTEGRITY = PASS
DOCX_DOCUMENT_XML = PRESENT
DOCX_COMMENTS = 8
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS / 16_OF_16_PAGES_VISUALLY_INSPECTED
MD_DOCX_EQUIVALENCE = PASS
OTHER_SECTIONS_VISIBLE_TEXT_PRESERVATION = PASS
ENGLISH_SECTION_2_1_WORD_COUNT = 587
FINAL_DOCX_SHA256 = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```

---

## English

### 1. Executed scope

Only `RELATED_WORK_B01 — Section 2.1 Automated tariff classification and candidate retrieval` was drafted within the approved cumulative structure. Sections 2.2–2.6, Introduction, Decision-support architecture, Experimental design, Results, and Methods B01 V06 were not drafted or scientifically modified.

The session baseline file was named `KBS_ARTICLE_WORKING_STRUCTURE_V01(1).docx`. The attachment suffix was not treated as a scientific version change because its SHA-256 exactly matches the approved `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx` baseline.

### 2. Full-text verification

All eight references cited in Section 2.1 were re-retrieved at full-text level from the PDFs available in the active session, identity-checked, and cross-checked against the frozen 0B-01/0B-02 maps. Each English citation instance has a Word comment anchored exactly to that citation containing the source identity, an exact supporting passage, Spanish translation, semantic justification, and scope limitation.

The frozen 0B04A artifact was used as a methodological terminology control—particularly to keep classification, candidate retrieval/ranking, and heterogeneous metrics distinct—without adding unnecessary generic IR citations to Section 2.1.

### 3. Scientific/editorial QA

The subsection is organized by task family rather than author chronology: direct classification → representation and staged hierarchical prediction → candidate retrieval/ranking → validation/correction → transition toward Section 2.2.

No present-study results, H100, Chapter 87, Peruvian corpus, DAM partitioning, proposed fixed Top-3 architecture, universal novelty, or `FINAL_GAP` claims were introduced.

### 4. Cumulative Word QA

The final DOCX was produced by editing a copy of the exact binary baseline rather than rebuilding the document. Only the English Section-2.1 drafting note/placeholder and the Spanish Section-2.1 placeholder were replaced. Visible text outside those bodies was programmatically compared with the baseline and remained identical.

OOXML ZIP integrity, `word/document.xml`, eight citation comments and anchors, zero tracked changes, 16-page rendering, pixel-identical visual equivalence before/after OOXML package normalization, visual inspection of all rendered pages, Markdown–DOCX equivalence for Section 2.1, and English–Spanish semantic equivalence all passed.

### 5. Delivery state

```text
PROTOCOL_READ = MWDP_V1.0
KBS_GUIDE_READ = KBS_EWG_34_V01
STRUCTURE_DECISION = D-015
BLOCK = RELATED_WORK_B01
BLOCK_REVISION = V01
SECTION = 2.1
BASELINE_DOCX_SHA256_VERIFIED = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5 / PASS
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 8/8
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_PROSE_QA = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
DOCX_OOXML_INTEGRITY = PASS
DOCX_RENDER = PASS
MD_DOCX_EQUIVALENCE = PASS
ENGLISH_SECTION_2_1_WORD_COUNT = 587
FINAL_DOCX_SHA256 = 08d8ce916452c71a504aa2a0e23d65d68aafe556d818bbf13fa82422a133bfc5
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = COMPLETED / AWAITING_INTERNAL_REVIEW
```
