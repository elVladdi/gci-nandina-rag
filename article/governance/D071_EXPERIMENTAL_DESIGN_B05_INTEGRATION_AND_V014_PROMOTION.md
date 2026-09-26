# D-071 — Integración de B05 y promoción verificada a V014 / B05 integration and verified V014 promotion

## Español

```text
DECISION_ID = D-071
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-070
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 / 4.6.1–4.6.3
AUTHOR_APPROVAL = SATISFIED
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
MATERIALIZED_MASTER = article/manuscript/ARTICLE_MASTER_V014.md
MATERIALIZED_MASTER_GIT_BLOB_OBSERVED = 20105abb745e382b923e4eb43d9a771a722df9e3
BYTE_EXACT_PROMOTION = PASS
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CITATION_COMMENTS = 40 / PRESERVED
B05_SECTION_4_6 = CLOSED / APPROVED / FROZEN / INTEGRATED
B06_SECTION_4_7 = ELIGIBLE_FOR_GROUND_TRUTH_SYNC / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Verificación

La IA Gestora recuperó `article/manuscript/ARTICLE_MASTER_V014.md` desde la rama `article/main-manuscript`. El Git blob observado es exactamente `20105abb745e382b923e4eb43d9a771a722df9e3`, igual al blob esperado del candidato B05 V01 previamente auditado y aprobado. La identidad Git exacta prueba que los bytes materializados son los bytes del candidato aprobado; por tanto conserva también el SHA-256 auditado `e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97`.

No se realizó reescritura, normalización ni reconstrucción durante la promoción.

### Cierre

B05 / Section 4.6 queda cerrado, aprobado, congelado e integrado. `ARTICLE_MASTER_V014.md` pasa a ser el master Markdown canónico y `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx` pasa a ser el baseline Word acumulativo canónico bajo custodia local del autor.

El cierre técnico habilita únicamente la preparación editorial de B06 / Section 4.7. No autoriza por sí mismo redacción de 4.7, 4.8 ni Results.

---

## English

```text
DECISION_ID = D-071
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-070
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 / 4.6.1–4.6.3
AUTHOR_APPROVAL = SATISFIED
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
MATERIALIZED_MASTER = article/manuscript/ARTICLE_MASTER_V014.md
MATERIALIZED_MASTER_GIT_BLOB_OBSERVED = 20105abb745e382b923e4eb43d9a771a722df9e3
BYTE_EXACT_PROMOTION = PASS
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CITATION_COMMENTS = 40 / PRESERVED
B05_SECTION_4_6 = CLOSED / APPROVED / FROZEN / INTEGRATED
B06_SECTION_4_7 = ELIGIBLE_FOR_GROUND_TRUTH_SYNC / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The Managing AI retrieved `ARTICLE_MASTER_V014.md` from `article/main-manuscript` and observed Git blob `20105abb745e382b923e4eb43d9a771a722df9e3`, exactly matching the previously audited and author-approved B05 candidate. This exact Git-object identity establishes byte-exact promotion and therefore preserves the audited SHA-256.

B05 / Section 4.6 is now closed, approved, frozen, and integrated. V014 is the canonical Markdown master and the B05 V01 cumulative DOCX is the canonical Word baseline under local author custody. Only B06 ground-truth preparation is enabled; Section 4.7 drafting, Section 4.8, and Results remain unauthorized until separately gated.