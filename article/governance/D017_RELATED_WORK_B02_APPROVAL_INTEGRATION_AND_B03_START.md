# D-017 — Aprobación e integración de Related Work B02 y apertura de B03 / Related Work B02 Approval, Integration, and B03 Start

## Español

```text
DECISION_ID = D-017
DECISION_DATE = 2026-09-19
AUTHOR_DECISION = RECEIVED
INTERNAL_REVIEW = PASS
BLOCK = RELATED_WORK_B02
BLOCK_REVISION = V01
SECTION = 2.2 Knowledge-enhanced retrieval and regulatory reasoning
DELIVERY_COMMIT = 5e58b5a45b1dcc50a4a324f38e5cc0c9746ef3dc
BLOCK_STATUS = APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V002
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V002.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V002.docx
CANONICAL_DOCX_SHA256 = ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e
CITATION_COMMENTS_TOTAL = 14
EXPERIMENTAL_REVIEW = NOT_REQUIRED
NEXT_BLOCK = RELATED_WORK_B03
NEXT_SECTION = 2.3 LLMs for classification, reasoning, and explanation
RELATED_WORK_B03 = AUTHORIZED
SECTIONS_2_4_TO_2_6 = NOT_AUTHORIZED
```

### Decisión

El autor aprobó expresamente `Related Work B02 V01` condicionado a la auditoría de la IA Gestora. La revisión independiente concluyó `PASS` sin correcciones materiales. La aprobación queda efectiva y B02 se congela e integra al master acumulativo.

La auditoría verificó de manera independiente las seis citas nuevas contra los full texts primarios y confirmó que los comentarios Word contienen pasajes reales y adecuados al claim. Los ocho comentarios heredados de 2.1 permanecen preservados, para un total de catorce.

### Master canónico

La versión canónica posterior a B02 es:

- `article/manuscript/ARTICLE_MASTER_V002.md`
- `article/manuscript/ARTICLE_MASTER_V002.docx`

El DOCX canónico es binariamente equivalente al candidato B02 aprobado y conserva los 14 comentarios de auditoría. SHA-256: `ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e`.

### Apertura de B03

Se autoriza exclusivamente `Related Work B03 — Section 2.3 LLMs for classification, reasoning, and explanation`.

B03 deberá partir de `ARTICLE_MASTER_V002.docx` y preservar exactamente 2.1, 2.2 y sus catorce comentarios. Su función será distinguir los papeles que los LLM y modelos relacionados desempeñan dentro del pipeline: clasificación generativa directa, transformer classifiers fine-tuned, LLM que decide o controla búsqueda/reranking, lector/razonador condicionado por retrieval y generador de explicación/rationale.

La subsección no describirá todavía la arquitectura del presente estudio ni afirmará que un LLM exclusivamente explicativo sea novedoso. Debe cerrar preparando 2.4 sobre grounding, explicabilidad y auditabilidad. `FINAL_GAP` y novelty universal continúan prohibidos.

### Controles heredados

- Wang et al. (2026) se mantiene como preprint salvo verificación posterior de publicación final.
- Visible evidence, citations, reasoning traces, path validity y rationale no equivalen automáticamente a formal auditability o legal correctness.
- `fine-tuned transformer classifier ≠ generative LLM classification`.
- `reranking/search control ≠ explanation-only generation`.

---

## English

The author approved Related Work B02 V01 subject to the Managing AI audit. Independent review passed with no material corrections, including six claim-to-primary-source checks and verification of the six new Word citation comments. The approval is therefore effective and B02 is approved, frozen, and integrated.

The new canonical cumulative master is `ARTICLE_MASTER_V002.md/.docx`, with DOCX SHA-256 `ffbaf15e59cbee922be5ddc70622e2da2f52110c712142f956479acea44e890e` and fourteen preserved citation-audit comments.

Only Related Work B03 / Section 2.3 is now authorized. It must distinguish direct generative LLM classification, fine-tuned transformer classification, LLM search/reranking/decision control, retrieval-conditioned reader/reasoner roles, and explanation/rationale generation. It must preserve Sections 2.1–2.2 exactly and stop before Section 2.4. Present-study architecture, final gap, and universal novelty remain unauthorized.