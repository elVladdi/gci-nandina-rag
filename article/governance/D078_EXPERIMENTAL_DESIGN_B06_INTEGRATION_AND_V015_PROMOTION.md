# D-078 — Integración de B06 y promoción verificada a V015 / B06 integration and verified V015 promotion

## Español

```text
DECISION_ID = D-078
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-077
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
AUTHOR_APPROVAL = SATISFIED
PROMOTED_MASTER = article/manuscript/ARTICLE_MASTER_V015.md
EXPECTED_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
OBSERVED_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
EXPECTED_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
PROMOTION_VERIFICATION = PASS / BYTE_EXACT_BY_GIT_BLOB_IDENTITY
B06_STATE = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
SECTION_4_8 = NOT_YET_AUTHORIZED_BY_THIS_DECISION
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Verificación de promoción

Se verificó directamente `article/manuscript/ARTICLE_MASTER_V015.md` en `article/main-manuscript`. El Git blob observado `e9a17899ccbcb9971e6dfb5002f908e17a0441d9` coincide exactamente con el Git blob congelado del candidato B06 V02 aprobado por el autor. La identidad de Git blob demuestra identidad byte-exacta del contenido almacenado; por ello se conserva el SHA-256 previamente auditado `b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c`.

No se detectó sustitución, edición posterior ni materialización divergente.

## 2. Cierre de B06

B06 / Section 4.7 queda cerrado, aprobado, congelado e integrado. Sus decisiones científicas y límites permanecen fijados por D-072–D-077 y por la auditoría `PASS` de B06 V02.

El baseline Word acumulativo pasa a ser el binario B06 V02 exacto, bajo custodia local del autor:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

## 3. Canonicalidad

Desde esta decisión:

```text
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V015.md
CANONICAL_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
```

`ARTICLE_MASTER_V014.md` deja de ser el master canónico vigente, aunque permanece como versión histórica trazable.

## 4. Gate posterior

D-078 no redacta ni autoriza por sí misma Section 4.8. El siguiente bloque solo puede abrirse tras sincronizar su ground truth con el estado real del repositorio de reproducibilidad y distinguir con precisión entre recursos ya materializados y recursos todavía planificados.

Results, Discussion y Conclusion permanecen cerrados.

---

## English

```text
DECISION_ID = D-078
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-077
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
PROMOTION_VERIFICATION = PASS / BYTE_EXACT_BY_GIT_BLOB_IDENTITY
B06_STATE = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
SECTION_4_8 = NOT_YET_AUTHORIZED_BY_THIS_DECISION
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The materialized `ARTICLE_MASTER_V015.md` was directly verified on the article branch. Its observed Git blob exactly matches the frozen Git blob of the author-approved B06 V02 candidate. B06 / Section 4.7 is therefore closed, approved, frozen, and integrated, and V015 becomes the canonical Markdown master.

The exact B06 V02 DOCX remains in local author custody and becomes the canonical cumulative Word baseline. Section 4.8 requires a separate ground-truth synchronization and authorization. Results, Discussion, and Conclusion remain closed.