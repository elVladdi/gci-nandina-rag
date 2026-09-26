# D-064 — Experimental Design B04 V02 differential PASS and author-approval gate

## Español

```text
DECISION_ID = D-064
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-063
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
CANDIDATE_REVISION = V02
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54
B04_V02_DIFFERENTIAL_AUDIT = PASS
CORRECTION_REQUIRED = NO
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL_GATE = OPEN
INTEGRATION = NOT_AUTHORIZED_UNTIL_EXPRESS_AUTHOR_APPROVAL
B05 = NOT_AUTHORIZED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

La auditoría diferencial independiente de la IA Gestora verificó que B04 V02 ejecuta exclusivamente B04-C01 y B04-C02 en inglés y español, sin mutaciones no autorizadas en el master Markdown ni en el DOCX acumulativo.

Artefactos candidatos verificados:

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B04_V02.md@bf85389070b583213a062421ee0adcd2e3e349ab
SECTION_ARTIFACT_GIT_BLOB = fa6e9325a5acd6bf480cdbe90a467855cf877f1d
MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md / LOCAL_AUTHOR_CUSTODY
MASTER_CANDIDATE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
MASTER_CANDIDATE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
MASTER_CANDIDATE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CITATION_COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

El master canónico sigue siendo `ARTICLE_MASTER_V012` porque la aprobación autoral es un gate separado del PASS técnico/editorial. La IA Gestora no puede promover V02 ni abrir B05 antes de que el autor apruebe expresamente B04 V02.

La diferencia de paginación DOCX de 44 a 45 páginas se acepta como consecuencia de reflujo de las sustituciones autorizadas y no como incorporación de contenido adicional.

El `ARTICLE_WRITING_PLAN.md` V3.4 contiene todavía texto operativo previo a D-063. Hasta su sincronización, D-064 y `ARTICLE_STATUS.md` tienen precedencia para el gate vigente. Este drift es editorial y no afecta el contenido científico ni la validez del candidato B04 V02; debe eliminarse antes de autorizar B05.

### Gate vigente

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
AUTHOR_ACTION = APPROVE_OR_REJECT_B04_V02
CANONICAL_MASTER = ARTICLE_MASTER_V012
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-064
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-063
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
CANDIDATE_REVISION = V02
GOVERNING_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_NARROW_PRECISION_CORRECTION_DIFFERENTIAL_REVIEW_V01.md@1cb3e2c865d44bbffb2481185ded6df8bf9abc54
B04_V02_DIFFERENTIAL_AUDIT = PASS
CORRECTION_REQUIRED = NO
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL_GATE = OPEN
INTEGRATION = NOT_AUTHORIZED_UNTIL_EXPRESS_AUTHOR_APPROVAL
B05 = NOT_AUTHORIZED
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

The independent Managing-AI differential audit verified that B04 V02 implements only B04-C01 and B04-C02 in English and Spanish, with no unauthorized mutation of the cumulative Markdown or DOCX candidate.

Verified candidate identities are the V02 section artifact at `bf85389070b583213a062421ee0adcd2e3e349ab`, Markdown SHA-256 `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43` / Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`, and DOCX SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`. All 40 inherited citation comments are preserved and tracked changes remain zero.

`ARTICLE_MASTER_V012` remains canonical because author approval is separate from technical/editorial PASS. B04 V02 may not be promoted and B05 may not be opened until the author expressly approves the candidate.

The DOCX page-count increase from 44 to 45 is accepted as layout reflow from the authorized wording, not additional content.

`ARTICLE_WRITING_PLAN.md` V3.4 still contains pre-D-063 operational text. Until synchronized, D-064 and `ARTICLE_STATUS.md` govern the current gate. This editorial drift does not affect B04 V02 scientific validity, but it must be removed before B05 authorization.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
AUTHOR_ACTION = APPROVE_OR_REJECT_B04_V02
CANONICAL_MASTER = ARTICLE_MASTER_V012
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
