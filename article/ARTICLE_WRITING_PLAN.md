# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.6
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-076
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V014.md
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = AUTHOR_APPROVAL_B06_V02
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B06 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
SECTION_4_7 = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN_FOR_B06_V02_ONLY
B06_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política acumulativa

`ARTICLE_MASTER_V014.md` permanece como master Markdown canónico verificado. El Word acumulativo canónico sigue siendo `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx` bajo custodia local del autor.

MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` permanecen vinculantes. No se reconstruyen masters acumulativos, no se sustituyen baselines exactos y un `PASS` de IA Gestora no equivale a aprobación autoral ni integración.

## 2. Estructura congelada de Experimental Design

```text
4.1 Experimental setting and scope
4.2 Historical data and experimental dataset construction
  4.2.1 Source and data collection
  4.2.2 Processing and curation
  4.2.3 Partition construction and dataset composition
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

## 3. Estado de construcción

| Bloque | Estado |
|---|---|
| Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B02 / 4.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B03 / 4.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B04 / 4.5 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B05 / 4.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| ARTICLE_MASTER_V014 | CANONICAL / VERIFIED |
| B06 / 4.7 | DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL |
| 4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. B06 V01 y microgate correctivo

La ejecución inicial B06 V01 fue auditada en:

`article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V01.md@3d19fbb47fd48abe15520264eea3b29969084295` — `PASS WITH CORRECTIONS`.

D-074 restringió la corrección a B06-C01–B06-C04 y D-075 autorizó únicamente:

`article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547`.

## 5. B06 V02 — auditoría diferencial cerrada

Response recibida:

`article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md@8469a6aa83b85dc64486877106cc6f05115b1751`.

Section artifact:

`article/sections/experimental_design/Experimental_Design_B06_V02.md@b8d19af968cc9b3e0cc205a908a05a5c1549b4c4`.

Auditoría IA Gestora:

`article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V02.md@5f154e54faf5b59f301bbb07787616468304a04b` — `PASS`.

D-076 abre exclusivamente el gate de aprobación autoral de B06 V02.

### 5.1 Cierre científico

```text
B06-C01 = CLOSED / PASS
B06-C02 = CLOSED / PASS
B06-C03 = CLOSED / PASS
B06-C04 = CLOSED / PASS
RESULTS_LEAKAGE = NONE
HYPOTHESIS_DISPOSITION_LEAKAGE = NONE
SCIENTIFIC_SCOPE_EXPANDED = NO
EN_ES_EQUIVALENCE = PASS
```

La versión conserva SERIE como unidad de análisis, DAM como cluster inferencial, estimando ponderado por series, bootstrap pareado por DAM con 10.000 réplicas y seed 20263001, reglas de multiplicidad y Bonferroni congeladas, Top-50 suplementaria, contraste HE2_B separado, y estados descriptivos/no-estimables de sensibilidad/HE5. No hay p-values, resultados observados ni disposiciones HE2/HE5 en Methods.

### 5.2 Candidatos exactos sometidos al autor

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9

ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES
VISUAL_QA = PASS
```

El candidato DOCX deriva del B06 V01 exacto y conserva el paquete OOXML; únicamente `word/document.xml` cambió para incorporar los seis párrafos autorizados de Section 4.7 EN/ES.

## 6. Canonicalidad

B06 V02 todavía no está integrado. Hasta aprobación autoral explícita y posterior promoción gobernada:

```text
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
```

## 7. Gate inmediato

```text
CURRENT_GATE = AUTHOR_APPROVAL_B06_V02
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REQUEST_CHANGES_B06_V02
AUTHOR_APPROVAL_GATE = OPEN_FOR_B06_V02_ONLY
B06_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Si el autor aprueba B06 V02 sin cambios, corresponde un gate separado de integración/promoción. Solo después de verificar esa integración podrá evaluarse la apertura de Section 4.8 mediante su propio ground truth, prompt, revisión y autorización.

---

# English

## 1. Current cumulative state

`ARTICLE_MASTER_V014.md` remains the verified canonical Markdown master, and `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx` remains the canonical cumulative Word baseline in local author custody. B01–B05 are closed, approved, frozen, and integrated.

B06 V02 has completed the Managing-AI differential audit with `PASS`; it is not yet author-approved or integrated.

## 2. B06 V02 audit closure

The corrected response is:

`article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md@8469a6aa83b85dc64486877106cc6f05115b1751`.

The independent review is:

`article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V02.md@5f154e54faf5b59f301bbb07787616468304a04b` — `PASS`.

D-076 opens only the author-approval gate for B06 V02.

All four narrow corrections are closed. The corrected Methods prose preserves the frozen inferential design and the descriptive/not-estimable sensitivity boundaries without importing observed Results or final HE2/HE5 dispositions.

## 3. Exact candidates under author review

```text
CANDIDATE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANDIDATE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANDIDATE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES
VISUAL_QA = PASS
```

## 4. Canonicality and gate

The B06 V02 candidates do not become canonical until explicit author approval and a governed integration/promotion step. The current canonical master remains V014/B05.

```text
CURRENT_GATE = AUTHOR_APPROVAL_B06_V02
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REQUEST_CHANGES_B06_V02
AUTHOR_APPROVAL_GATE = OPEN_FOR_B06_V02_ONLY
B06_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
