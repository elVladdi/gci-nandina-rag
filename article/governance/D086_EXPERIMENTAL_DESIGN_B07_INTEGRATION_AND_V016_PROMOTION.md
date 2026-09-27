# D-086 — Integración B07 y promoción verificada de V016 / B07 integration and verified V016 promotion

## Español

```text
DECISION_ID = D-086
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-085
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
CANDIDATE_REVISION = V02
AUTHOR_DECISION = APPROVED
PROMOTION_VERDICT = PASS / BYTE_EXACT
ARTICLE_MASTER_V016 = CANONICAL / VERIFIED
B07_STATE = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_8 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Verificación de promoción

IA Gestora verificó directamente `article/manuscript/ARTICLE_MASTER_V016.md` en `article/main-manuscript` después de la materialización realizada por el autor.

```text
EXPECTED_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
OBSERVED_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
BLOB_IDENTITY = EXACT_MATCH
APPROVED_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
PROMOTION = BYTE_EXACT / PASS
```

La identidad exacta del Git blob confirma que V016 contiene exactamente los bytes del candidato Markdown B07 V02 aprobado y auditado. Por tanto, conserva el SHA-256 aprobado indicado arriba.

## 2. Master canónico

Desde esta decisión:

```text
CANONICAL_MASTER = ARTICLE_MASTER_V016
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
CANONICAL_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
CANONICAL_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CANONICAL_TRACKED_CHANGES = 0
```

## 3. Cierre de Experimental Design

Con la promoción verificada de V016, B07 / Section 4.8 queda integrado. B01–B07 y la totalidad de Section 4 — Experimental design quedan cerrados, aprobados, congelados e integrados.

La Section 4.8 integrada mantiene el foco exclusivo en el repositorio público `gci-nandina-rag-reproducibility`, sin presentar narrativamente el repositorio interno de desarrollo, y conserva las fronteras ya aprobadas sobre recursos materializados/planificados/restringidos, reproducción de referencia/replicación externa y configurabilidad/generalización.

## 4. Gate posterior

El cierre de Experimental Design no autoriza Results automáticamente.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_COMPLETE / RESULTS_GATE_PENDING
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_SEPARATE_RESULTS_GROUND_TRUTH_AND_AUTHORIZATION_GATE
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

No puede iniciarse redacción de Section 5 hasta que exista sincronización independiente del ground truth de resultados, revisión del contrato correspondiente y autorización editorial explícita.

---

## English

```text
DECISION_ID = D-086
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PROMOTION_VERDICT = PASS / BYTE_EXACT
ARTICLE_MASTER_V016 = CANONICAL / VERIFIED
B07_STATE = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The observed Git blob of `article/manuscript/ARTICLE_MASTER_V016.md` exactly matches the frozen approved B07 V02 candidate blob `e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc`. V016 is therefore the canonical verified Markdown master, and `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx` becomes the canonical cumulative Word master in local author custody. Experimental Design is fully integrated. Results remains closed pending a separate ground-truth and authorization gate.