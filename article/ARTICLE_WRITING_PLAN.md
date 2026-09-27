# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.13
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-086
CANONICAL_MASTER = ARTICLE_MASTER_V016
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
CANONICAL_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
CANONICAL_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = POST_EXPERIMENTAL_DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_COMPLETE / RESULTS_GATE_PENDING
EXPERIMENTAL_DESIGN_B01_TO_B07 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_8 = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V016.md` es el master Markdown canónico verificado. La promoción desde el candidato B07 V02 aprobado fue byte-exacta: Git blob observado y esperado `e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc`, SHA-256 aprobado `3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5`.

El Word acumulativo canónico es `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx`, SHA-256 `c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de`, bajo custodia local del autor, con 40 comentarios preservados y 0 tracked changes.

## 2. Cierre de Experimental Design

B01–B07 y toda Section 4 — Experimental design están cerrados, aprobados, congelados e integrados.

La estructura congelada completada es:

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

B07 / §4.8 queda integrado con foco directo en el repositorio público `gci-nandina-rag-reproducibility`; no presenta narrativamente el repositorio interno de desarrollo y mantiene las fronteras entre recursos materializados, planificados y restringidos, reproducción de referencia y replicación externa, y configurabilidad frente a generalización empírica.

## 3. Identidades de cierre

```text
ARTICLE_MASTER_V016.md
SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

Decisión de integración:

`article/governance/D086_EXPERIMENTAL_DESIGN_B07_INTEGRATION_AND_V016_PROMOTION.md@58febd57d6384241c2253f9101a869792f23e139`.

## 4. Fase siguiente

El cierre de Experimental Design no abre Results por inferencia.

Antes de cualquier redacción de Section 5, IA Gestora debe sincronizar de manera independiente el ground truth de resultados y definir qué resultados, comparaciones, inferencias, sensibilidades y límites están autorizados para el manuscrito. Ese trabajo deberá producir su propio contrato/prompt, revisión y autorización.

```text
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_SEPARATE_RESULTS_GROUND_TRUTH_AND_AUTHORIZATION_GATE
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
BASELINE_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
BASELINE_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
RESULTS = NOT_AUTHORIZED
```

No se autoriza todavía Section 5, Discussion, Conclusion, definición del final gap ni declaración de novelty.

---

# English

## 1. Current cumulative state

`ARTICLE_MASTER_V016.md` is the verified canonical Markdown master. `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx` is the canonical cumulative Word master in local author custody. Experimental Design B01–B07 and all of Section 4 are closed, approved, frozen, and integrated.

```text
CANONICAL_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
CANONICAL_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
CANONICAL_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

## 2. Next gate

Results is not opened automatically by completion of Experimental Design. A separate Managing-AI ground-truth synchronization, drafting contract, review, and explicit authorization are required before Section 5 drafting begins.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_COMPLETE / RESULTS_GATE_PENDING
NEXT_ACTOR = IA_GESTORA
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```