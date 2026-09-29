# D-193 — Corrección de metadato de paginación del DOCX canónico / Canonical DOCX pagination metadata correction

## Español

```text
DECISION = D-193
PHASE = AUTHOR_FINALIZATION / GOVERNANCE_METADATA_CORRECTION
SCOPE = GOVERNANCE_METADATA_ONLY

PREVIOUS_DECISION = D-192
CANONICAL_MASTER = ARTICLE_MASTER_V036
CANONICAL_MASTER_MD_GIT_BLOB = c9dcbcc376cdb121d30dc2408756a6c95b569a90
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx
CANONICAL_MASTER_DOCX_SHA256 = d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d

STALE_METADATA =
CANONICAL_DOCX_PAGE_COUNT = 71

VERIFIED_METADATA =
CANONICAL_DOCX_PAGE_COUNT = 72

ARTICLE_CONTENT_CHANGED = NO
MARKDOWN_MASTER_CHANGED = NO
DOCX_BYTES_CHANGED = NO
SCIENTIFIC_CONTENT_CHANGED = NO
AUTHOR_APPROVAL_GATE = NOT_REQUIRED
GESTORA_TASK_STATUS = FINALIZED
FINAL_GAP = AUTHOR_OWNED_SUBMISSION_ASSEMBLY
```

### 1. Hallazgo

Después del cierre D-192, `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` conservaron por arrastre el valor de paginación del Word baseline anterior:

`CANONICAL_DOCX_PAGE_COUNT = 71`.

Ese valor no corresponde al DOCX canónico corregido de la declaración de IA.

### 2. Evidencia gobernada

D-192 y la auditoría independiente asociada
`article/reviews/12_END_MATTER_B02_GENERATIVE_AI_DECLARATION_INTERNAL_REVIEW_V02_C01.md`
registran para
`ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx`:

- SHA-256: `d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d`;
- tamaño: 111524 bytes;
- comentarios: 48;
- tracked changes: 0;
- páginas renderizadas: 72;
- render completo: PASS;
- QA visual: PASS, páginas 1–72.

Por tanto, el valor 71 en los dos archivos de gobernanza es un metadato obsoleto heredado y no una propiedad del artefacto canónico vigente.

### 3. Corrección

Se autoriza y ejecuta exclusivamente:

```text
ARTICLE_STATUS.md:
ARTICLE_WRITING_PLAN = V3.79 -> V3.80
LATEST_EDITORIAL_DECISION = D-192 -> D-193
CANONICAL_DOCX_PAGE_COUNT = 71 -> 72

ARTICLE_WRITING_PLAN.md:
PLAN_VERSION = V3.79 -> V3.80
LATEST_EDITORIAL_DECISION = D-192 -> D-193
CANONICAL_DOCX_PAGE_COUNT = 71 -> 72
```

No se modifica `ARTICLE_MASTER_V036.md`, el DOCX canónico, ninguna sección científica ni ningún texto de la declaración de IA.

### 4. Disposición

D-192 conserva íntegramente su autoridad como decisión de aprobación e integración de la declaración de IA V02. D-193 únicamente reconcilia el metadato de paginación de los registros de gobernanza con el artefacto ya auditado.

```text
AI_DISCLOSURE_STATUS = CLOSED / APPROVED / FROZEN / INTEGRATED
GESTORA_TASK_STATUS = FINALIZED
CURRENT_GATE = AUTHOR_OWNED_FINAL_ASSEMBLY
NEXT_ACTOR = AUTHOR
SUBMISSION_READY = NOT_ASSERTED
```

---

## English

D-193 corrects one stale governance metadata value inherited from the prior Word baseline.

D-192 and its independent Managing-AI review record the canonical corrected DOCX
`ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx`
as SHA-256
`d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d`,
111524 bytes, 48 comments, zero tracked changes, and 72 rendered pages with full render and visual-QA PASS.

Accordingly, the `CANONICAL_DOCX_PAGE_COUNT = 71` value remaining in `ARTICLE_STATUS.md` and `ARTICLE_WRITING_PLAN.md` is corrected to `72`. The plan version advances from V3.79 to V3.80 and the latest editorial decision becomes D-193.

No manuscript content, Markdown master bytes, DOCX bytes, scientific claims, or AI-disclosure wording are changed. D-192 remains the controlling approval/integration decision. The Managing-AI task remains finalized and the remaining submission assembly remains author-owned.
