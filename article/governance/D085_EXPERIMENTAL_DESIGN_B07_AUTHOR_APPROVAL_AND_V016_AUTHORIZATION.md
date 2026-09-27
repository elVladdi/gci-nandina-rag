# D-085 — Aprobación autoral B07 V02 y autorización de V016 / B07 V02 author approval and V016 authorization

## Español

```text
DECISION_ID = D-085
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-084
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
CANDIDATE_REVISION = V02
AUTHOR_DECISION = APPROVED
B07_STATE = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_8 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
TARGET_MASTER = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión

El autor aprueba explícitamente B07 V02 / Section 4.8 después de la corrección B07-C01 y del `PASS` de auditoría independiente registrado en D-084.

B07 V02 queda cerrado, aprobado y congelado. Se autoriza exclusivamente la promoción byte-exacta del candidato Markdown aprobado a `article/manuscript/ARTICLE_MASTER_V016.md`.

Esta decisión no materializa por sí sola V016 y no autoriza Results. V016 deberá ser subida sin modificación y posteriormente verificada por IA Gestora antes de convertirse en master canónico.

## 2. Artefactos exactos aprobados

```text
APPROVED_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
APPROVED_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
APPROVED_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

APPROVED_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
APPROVED_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
```

El DOCX aprobado permanece bajo custodia local del autor y será el Word acumulativo canónico una vez verificada la promoción de V016.

## 3. Contenido congelado de B07

Section 4.8 queda congelada con estas fronteras:

- foco directo en el repositorio público `gci-nandina-rag-reproducibility`;
- ninguna mención narrativa al repositorio interno de desarrollo experimental;
- separación entre recursos materializados, planificados/no materializados y entradas restringidas/no redistribuidas;
- separación entre reproducción de referencia y replicación externa;
- configurabilidad no equivale a generalización empírica;
- no se afirma una release computacional completa ni reproducción one-command/fresh-clone;
- el estado público deberá re-verificarse antes del freeze final/submission.

## 4. Gate de promoción

```text
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V015
AUTHORIZED_PROMOTION_SOURCE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
AUTHORIZED_PROMOTION_TARGET = article/manuscript/ARTICLE_MASTER_V016.md
EXPECTED_TARGET_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
EXPECTED_TARGET_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
V016_STATUS = AUTHORIZED / PENDING_MATERIALIZATION_AND_VERIFICATION
B07_INTEGRATION = PENDING_BYTE_EXACT_PROMOTION
RESULTS = NOT_AUTHORIZED
```

La siguiente acción es del autor: subir el Markdown aprobado sin modificación como `article/manuscript/ARTICLE_MASTER_V016.md`. Tras ello, IA Gestora verificará la identidad byte-exacta y solo entonces cerrará la integración de Experimental Design y evaluará el gate posterior.

---

## English

```text
DECISION_ID = D-085
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
CANDIDATE_REVISION = V02
AUTHOR_DECISION = APPROVED
B07_STATE = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
TARGET_MASTER = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The author explicitly approves B07 V02 after the B07-C01 correction and the independent audit PASS recorded in D-084. The exact approved Markdown candidate is authorized for byte-exact promotion to `article/manuscript/ARTICLE_MASTER_V016.md`.

```text
APPROVED_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
APPROVED_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
APPROVED_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

V015 remains canonical until V016 is materialized and independently verified. Results and later sections remain unauthorized.