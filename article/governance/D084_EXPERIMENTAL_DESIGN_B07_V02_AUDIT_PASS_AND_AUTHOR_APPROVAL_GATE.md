# D-084 — PASS de auditoría B07 V02 y reapertura de gate autoral / B07 V02 audit PASS and author approval gate

## Español

```text
DECISION_ID = D-084
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-083
AUTHOR_CORRECTION_DECISION = D-082
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
CANDIDATE_REVISION = V02
GESTORA_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_INTERNAL_REVIEW_V02.md@1a59ae7d81549f0c42c8d72d5f7fb1891258f7c6
GESTORA_VERDICT = PASS
B07_STATE = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN_FOR_B07_V02_ONLY
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión

La auditoría independiente de B07 V02 confirma que la corrección autoral B07-C01 fue ejecutada de forma estrecha y completa. Section 4.8 ya no presenta ni menciona narrativamente el repositorio interno de desarrollo experimental. La prosa abre directamente con el repositorio público `gci-nandina-rag-reproducibility` y conserva las fronteras científicas ya aprobadas.

B07 V02 pasa exclusivamente a aprobación del autor. Esta decisión no equivale a aprobación autoral, integración ni promoción de master.

## 2. Candidatos exactos sometidos al autor

```text
APPROVAL_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
APPROVAL_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
APPROVAL_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

APPROVAL_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
APPROVAL_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
VISUAL_QA = PASS
```

El master canónico continúa siendo `ARTICLE_MASTER_V015.md` y el Word canónico continúa siendo `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx` hasta una eventual aprobación autoral de B07 V02 y posterior promoción verificada.

## 3. Estado científico aprobado para revisión autoral

Section 4.8 V02:

- se concentra exclusivamente en el recurso público de reproducibilidad;
- distingue recursos materializados, planificados/no materializados y entradas restringidas/no redistribuidas;
- distingue reproducción de referencia de replicación externa;
- no equipara configurabilidad con generalización empírica;
- no afirma una release computacional completa ni reproducción one-command/fresh-clone;
- no afirma disponibilidad pública de datos administrativos restringidos;
- mantiene el recheck del estado público antes de submission.

El snapshot público continúa en HEAD `254831cd955103faa2517065a7eed7fb340bbccc`, tree `078a85255fa1f3234b4f7ed51ef2660b903d486e`.

## 4. Cumplimiento D-035

La entrega V02 mantiene la ruta timeout-safe exigida. Los candidatos acumulativos exactos fueron entregados como archivos reales al autor y no se observó Base64 manual, chunking, fragmentación o reensamblado.

```text
D035_TIMEOUT_SAFE_HANDOFF = PASS
D027_AUTHOR_CUSTODY = ESTABLISHED_FOR_B07_V02_CANDIDATES
```

## 5. Gate

```text
CURRENT_GATE = B07_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_B07_V02_OR_REQUEST_CHANGES
B07_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
TARGET_MASTER_IF_APPROVED = ARTICLE_MASTER_V016
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

La eventual aprobación de B07 V02 cerrará Section 4 — Experimental design en contenido, pero no abrirá Results automáticamente. V016 deberá materializarse y verificarse byte-exactamente antes de cualquier gate posterior.

---

## English

```text
DECISION_ID = D-084
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
CANDIDATE_REVISION = V02
GESTORA_VERDICT = PASS
B07_STATE = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN_FOR_B07_V02_ONLY
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The narrow author-requested B07-C01 correction passed independent audit. Section 4.8 now focuses directly on the public reproducibility package and contains no narrative reference to the internal experimental-development repository. The exact B07 V02 MD/DOCX candidates are placed before the author for approval.

```text
APPROVAL_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
APPROVAL_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
APPROVAL_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_RENDER = PASS / 51 OF 51 PAGES
D035_TIMEOUT_SAFE_HANDOFF = PASS
```

The canonical master remains V015 until explicit author approval and later byte-exact V016 promotion. Results and later sections remain unauthorized.
