# D-018 — Aprobación e integración de Related Work B03 y apertura de B04 / Related Work B03 Approval, Integration, and B04 Start

## Español

```text
DECISION_ID = D-018
DECISION_DATE = 2026-09-20
AUTHOR_DECISION = RECEIVED
INTERNAL_REVIEW = PASS
BLOCK = RELATED_WORK_B03
BLOCK_REVISION = V01
SECTION = 2.3 LLMs for classification, reasoning, and explanation
DELIVERY_COMMIT = 17802e2c10de072524acf3655d6ee8ad0b0aa892
BLOCK_STATUS = APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V003
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V003.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V003.docx
CANONICAL_DOCX_SHA256 = f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7
CITATION_COMMENTS_TOTAL = 19
EXPERIMENTAL_REVIEW = NOT_REQUIRED
NEXT_BLOCK = RELATED_WORK_B04
NEXT_SECTION = 2.4 Evidence grounding, explainability, and auditability
RELATED_WORK_B04 = AUTHORIZED
SECTIONS_2_5_TO_2_6 = NOT_AUTHORIZED
```

### Decisión

El autor aprobó expresamente `Related Work B03 V01` condicionado a la auditoría de la IA Gestora. La revisión independiente concluyó `PASS` sin correcciones materiales. La aprobación queda efectiva y B03 se congela e integra al master acumulativo.

La auditoría verificó la función científica y editorial de 2.3, la correspondencia claim–fuente de las cinco citas nuevas contra los full texts primarios, la adecuación de los cinco comentarios Word nuevos, la preservación de los catorce comentarios heredados y la equivalencia EN–ES. El candidato aprobado contiene diecinueve comentarios de auditoría de citas y no contiene tracked changes.

Entre el commit semántico de B03 y el HEAD inspeccionado antes de esta integración existen commits posteriores que modifican únicamente `ARTICLE_STATUS.md`, `CLAIM_EVIDENCE_MATRIX.md` y `SOURCE_REGISTRY.md`; no modifican los cuatro artefactos de la entrega B03. Por tanto, el candidato aprobado permanece íntegro para promoción canónica.

### Master canónico

La versión canónica posterior a B03 es:

- `article/manuscript/ARTICLE_MASTER_V003.md`
- `article/manuscript/ARTICLE_MASTER_V003.docx`

Ambos se promueven byte-for-byte desde el candidato B03 aprobado. El DOCX canónico conserva los 19 comentarios de auditoría y mantiene SHA-256 `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`.

### Apertura de B04

Se autoriza exclusivamente `Related Work B04 — Section 2.4 Evidence grounding, explainability, and auditability`.

B04 deberá partir de `ARTICLE_MASTER_V003.docx` y preservar exactamente 2.1–2.3 y sus diecinueve comentarios. Su función es sintetizar cómo la literatura relaciona outputs con evidencia recuperada, explicaciones, atribución/procedencia y mecanismos de auditoría, manteniendo separadas las propiedades que responden a preguntas distintas.

La subsección deberá distinguir, cuando las fuentes lo soporten, entre evidencia visible y soporte real del claim; explicación y faithfulness; provenance/traceability y auditability; lifecycle audit y output-level auditability; autoridad/actualidad documental y corrección sustantiva o jurídica. No describirá todavía la arquitectura del presente estudio, HE4, resultados propios, `FINAL_GAP` ni novelty.

B04 debe cerrar preparando 2.5 sobre reproducibilidad y evaluación, sin desarrollarla.

### Controles heredados

- `VISIBLE_EVIDENCE / CITATION ≠ CLAIM_SUPPORT ≠ FORMAL_AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `RATIONALE / REASONING_TRACE ≠ FAITHFULNESS GUARANTEE`.
- `PROVENANCE / LINEAGE ≠ SUBSTANTIVE_CORRECTNESS`.
- `LIFECYCLE_AUDIT ≠ FORMAL_OUTPUT_LEVEL_AUDITABILITY`.
- `OFFICIAL_SOURCE / DOCUMENT_AUTHORITY ≠ CORRECT_LEGAL_INTERPRETATION`.
- `DOCUMENT_CURRENCY / TRACEABILITY ≠ LEGAL_VALIDITY_OF_THE_MODEL_OUTPUT`.
- La reproducibilidad detallada, documentación de datasets y evaluación experimental pertenecen principalmente a 2.5; B04 puede usarlos solo para delimitar conceptos próximos.

---

## English

The author approved Related Work B03 V01 subject to the Managing AI audit. Independent review passed with no material corrections, including five claim-to-primary-source checks, verification of five new Word citation comments, preservation of all fourteen prior comments, bilingual equivalence, OOXML integrity, zero tracked changes, and full-document rendering. B03 is therefore approved, frozen, and integrated.

The new canonical cumulative master is `ARTICLE_MASTER_V003.md/.docx`. It is promoted byte-for-byte from the approved B03 candidate; the DOCX retains nineteen citation-audit comments and SHA-256 `f211e294f9da1241d899c4f4d52b3752b494cbf5e5323a09fc86431e4d4b3ec7`.

Only Related Work B04 / Section 2.4 is now authorized. It must distinguish visible evidence from actual claim support, explanation from faithfulness, provenance/traceability from auditability, lifecycle audit from output-level auditability, and documentary authority/currency from substantive or legal correctness. Sections 2.1–2.3 and all nineteen comments must remain unchanged. Present-study architecture, HE4, experimental results, final gap, and novelty remain unauthorized.