# D-033 — Introduction B01 integration and ARTICLE_MASTER_V007 promotion

```text
DECISION_ID = D-033
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
BLOCK = INTRODUCTION_B01
AUTHOR_APPROVAL = RECEIVED / PRESERVED
SCIENTIFIC_REVIEW = PASS
TECHNICAL_CLOSURE = PASS
INTRODUCTION_B01_V02 = APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
CANONICAL_CITATION_COMMENTS = 40
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Base de la decisión

Introduction B01 V02 fue auditada científicamente con `PASS`, aprobada expresamente por el autor y congelada por D-031. El bloqueo posterior era exclusivamente técnico: los Markdown exactos aprobados no habían podido materializarse en GitHub.

D-032 autorizó su handoff exacto al autor. La respuesta `article/responses/3_INTRODUCTION_B01_EXACT_MARKDOWN_HANDOFF_RESPONSE_V01.md@af4c0b96436e5b3a310499266b82bf5b377154a6` registró la entrega de ambos archivos. La IA Gestora verificó los dos SHA-256 recibidos y los materializó sin reconstrucción en `de2c1f2b766a626552616ea55be29d66a75203b1`.

La revisión de materialización confirma identidad exacta de:

- `article/sections/introduction/Introduction_B01_V02.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md`.

## 2. Integración canónica

Se autoriza promover, sin cambio de contenido, el blob Git `436e0522db0ac348efaed86f4e53a7e6db372471` a:

`article/manuscript/ARTICLE_MASTER_V007.md`

El DOCX aprobado correspondiente queda como nuevo baseline acumulativo bajo custodia local del autor:

`ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx`

SHA-256:

`d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c`

Introduction B01 V02 pasa a `APPROVED / FROZEN / INTEGRATED`. Related Work 2.1–2.6 conserva su estado previo sin modificación.

## 3. Gate posterior

Esta decisión **no abre todavía** `Decision-support architecture`.

El autor solicitó revisar expresamente la relación entre el Plan Maestro experimental, Grupo 6 y Grupo 7 antes de continuar con la siguiente sección. En consecuencia, la apertura de Architecture requiere una decisión editorial separada después de esa reconciliación. Esto no reabre Introduction ni invalida V007.

```text
CURRENT_GATE = PRE_ARCHITECTURE_G6_G7_GOVERNANCE_RECONCILIATION
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
