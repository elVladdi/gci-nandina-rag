# D-077 — Aprobación autoral de B06 y autorización de promoción V015 / B06 author approval and V015 promotion authorization

## Español

```text
DECISION_ID = D-077
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-076
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
CANDIDATE_REVISION = V02
AUTHOR_DECISION = APPROVED
B06_STATE = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V015
INTEGRATION = AUTHORIZED / PENDING_BYTE_EXACT_MATERIALIZATION_AND_VERIFICATION
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión

El autor aprobó explícitamente B06 V02 / Section 4.7 sin solicitar cambios adicionales. Se cierra el gate autoral abierto por D-076 y se autoriza la promoción gobernada del candidato Markdown aprobado a `article/manuscript/ARTICLE_MASTER_V015.md`.

La aprobación no equivale todavía a integración materializada: la promoción debe conservar identidad byte-exacta y ser verificada después de que V015 exista en GitHub.

## 2. Candidatos aprobados y congelados

```text
APPROVED_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
APPROVED_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
APPROVED_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9

APPROVED_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
APPROVED_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES
VISUAL_QA = PASS
```

Estas identidades quedan congeladas. Cualquier modificación posterior requeriría una nueva revisión y una nueva aprobación antes de integración.

## 3. Estado científico aprobado

La aprobación autoral ratifica el bloque auditado por IA Gestora en `PASS`:

```text
B06-C01 = CLOSED / PASS
B06-C02 = CLOSED / PASS
B06-C03 = CLOSED / PASS
B06-C04 = CLOSED / PASS
RESULTS_LEAKAGE = NONE
HYPOTHESIS_DISPOSITION_LEAKAGE = NONE
SCIENTIFIC_SCOPE_EXPANDED = NO
EN_ES_EQUIVALENCE = PASS
MD_DOCX_CONTINUITY = PASS
OOXML_INTEGRITY = PASS
```

Section 4.7 conserva SERIE como unidad de análisis, DAM como cluster inferencial, estimando ponderado por series, bootstrap pareado por DAM con 10.000 réplicas y seed 20263001, la matriz común `10000 × 67`, las reglas de multiplicidad y Bonferroni, Top-50 suplementaria con IC 95%, el contraste HE2_B separado y los límites descriptivos/no estimables congelados.

## 4. Promoción autorizada

La única promoción autorizada es:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
TARGET = article/manuscript/ARTICLE_MASTER_V015.md
EXPECTED_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
EXPECTED_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
```

Hasta verificar esas identidades en el archivo materializado, `ARTICLE_MASTER_V014.md` permanece como master Markdown canónico.

El DOCX aprobado no se sube al repositorio; permanece bajo custodia local del autor y será el baseline Word acumulativo después de la promoción verificada de V015.

## 5. Gate

```text
CURRENT_GATE = B06_V015_PROMOTION_PENDING
NEXT_ACTOR = AUTHOR / REPOSITORY_MATERIALIZATION
NEXT_ACTION = MATERIALIZE_APPROVED_B06_V02_MD_AS_ARTICLE_MASTER_V015_AND_RETURN_FOR_VERIFICATION
AUTHOR_APPROVAL_GATE = SATISFIED
B06 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Section 4.8 no se abre por esta decisión. Su eventual apertura exige, después de la verificación de V015, ground truth propio, prompt, revisión independiente y autorización.

---

## English

```text
DECISION_ID = D-077
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-076
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
CANDIDATE_REVISION = V02
AUTHOR_DECISION = APPROVED
B06_STATE = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V015
INTEGRATION = AUTHORIZED / PENDING_BYTE_EXACT_MATERIALIZATION_AND_VERIFICATION
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The author explicitly approved B06 V02 / Section 4.7 without further changes. D-077 closes the author gate opened by D-076 and authorizes governed promotion of the exact approved Markdown candidate to `article/manuscript/ARTICLE_MASTER_V015.md`.

The approved identities are frozen:

```text
APPROVED_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
APPROVED_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
APPROVED_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

Promotion is authorized only if `ARTICLE_MASTER_V015.md` is materialized byte-exactly with the expected SHA-256 and Git blob above. Until that verification occurs, V014 remains canonical. The approved DOCX remains under local author custody and becomes the cumulative Word baseline only after V015 promotion is verified.

D-077 does not authorize Section 4.8, Results, Discussion, or Conclusion. Section 4.8 requires its own ground-truth synchronization, drafting contract, review, and authorization after V015 is verified.
