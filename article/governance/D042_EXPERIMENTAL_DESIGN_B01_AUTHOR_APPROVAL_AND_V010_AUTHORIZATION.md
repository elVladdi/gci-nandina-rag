# D-042 — Experimental Design B01 author approval and V010 authorization

## Español

```text
DECISION_ID = D-042
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-041
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B01_CORRECTION_INTERNAL_REVIEW_V01.md@04980afc3e4a8544e80d9060da7f5fd38f3a32ab
AUTHOR_DECISION = APPROVED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / READY_FOR_INTEGRATION
AUTHORIZED_SCOPE = SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
APPROVED_MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md
APPROVED_MASTER_CANDIDATE_MD_SHA256 = bdcbbd474d467e978777e031ae568b3fb5d089c32606289f0818ea852a4d4c44
EXPECTED_ARTICLE_MASTER_V010_GIT_BLOB = 2b409a22355b2268f9c71cc8efca5ceb93c19b37
APPROVED_MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_MASTER_CANDIDATE_DOCX_SHA256 = 53c23c6f951aa8d76ea647fe97105cddd43883c3b3b93e6850ea8eaf861053b2
CANONICAL_CITATION_COMMENTS_AFTER_B01 = 40
TRACKED_CHANGES = 0
ARTICLE_MASTER_V010 = AUTHORIZED / NOT_YET_MATERIALIZED
EXPERIMENTAL_DESIGN_B02 = ELIGIBLE_AFTER_V010_INTEGRATION / NOT_YET_AUTHORIZED
SECTION_4_3_AND_LATER = NOT_YET_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El autor aprobó expresamente Experimental Design B01 después del `PASS` científico y de la corrección estructural menor verificada. La versión aprobada comprende exclusivamente 4.1 y 4.2.1–4.2.4 y queda congelada para integración.

Se autoriza materializar el Markdown acumulativo aprobado, sin modificación de contenido, como `article/manuscript/ARTICLE_MASTER_V010.md`. La integración solo se considerará completada cuando GitHub reporte el Git blob esperado `2b409a22355b2268f9c71cc8efca5ceb93c19b37` para ese archivo.

El DOCX aprobado permanece bajo custodia local efectiva del autor conforme a D-021/D-027. No debe reconstruirse desde Markdown ni modificarse durante la integración.

D-035 continúa vigente: dado el antecedente de timeout para masters acumulativos grandes, no se autoriza reintentar la transferencia directa del Markdown grande mediante el conector ni utilizar Base64 manual, fragmentación, chunking, recomposición o archivos auxiliares como workaround. Si la materialización exacta requiere intervención del autor, se utilizará el handoff exacto del archivo ya aprobado.

La aprobación de B01 no abre por sí sola 4.3 ni Experimental Design B02. Una vez integrada y verificada V010, la IA Gestora debe continuar automáticamente con la reconciliación y apertura del siguiente bloque elegible.

---

## English

The author explicitly approved Experimental Design B01 after scientific PASS and verified removal of the single stale Spanish placeholder. The approved cumulative Markdown is `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.md`, SHA-256 `bdcbbd474d467e978777e031ae568b3fb5d089c32606289f0818ea852a4d4c44`; its expected Git blob is `2b409a22355b2268f9c71cc8efca5ceb93c19b37`. The approved DOCX is `ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V02.docx`, SHA-256 `53c23c6f951aa8d76ea647fe97105cddd43883c3b3b93e6850ea8eaf861053b2`, under local author custody. `ARTICLE_MASTER_V010` is authorized but not yet materialized. Experimental Design B02 remains closed until exact V010 integration is verified.