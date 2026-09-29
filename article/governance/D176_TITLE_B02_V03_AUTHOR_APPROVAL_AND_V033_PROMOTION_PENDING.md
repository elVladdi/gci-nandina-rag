# D-176 — Title B02 V03 author approval recorded; V033 materialization required

## Español

```text
DECISION = D-176
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE_V03

AUTHOR_DECISION = APPROVED
AUTHOR_APPROVAL_RECEIVED = YES
AUTHOR_APPROVAL_SCOPE = EXACT_TITLE_B02_V03_CANDIDATE_ONLY

APPROVED_TITLE_EN =
Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

APPROVED_TITLE_ES =
Arquitectura basada en conocimiento para el apoyo a la decisión en clasificación arancelaria: separación del ranking de candidatos, la evidencia documental y la explicación

APPROVED_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_TITLE_B02_V03.md
APPROVED_CANDIDATE_MD_SHA256 = bf90c8b10891d401aa34f7553248f30578c1e4b98bef0bcbf32ec1da4446c9f1
APPROVED_CANDIDATE_MD_EXPECTED_GIT_BLOB = 9b87c71290126f5223c6e4a252f95b5d64f71f49

APPROVED_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_TITLE_B02_V03.docx
APPROVED_CANDIDATE_DOCX_SHA256 = 1451c7c2d9a013603c749a7ad0730ea450f76700ff853b6d96d9d1f865882ed1
APPROVED_CANDIDATE_DOCX_SIZE_BYTES = 110921
APPROVED_CANDIDATE_DOCX_COMMENTS = 48
APPROVED_CANDIDATE_DOCX_TRACKED_CHANGES = 0
APPROVED_CANDIDATE_DOCX_PAGE_COUNT = 71

PRE_APPROVAL_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_INTERNAL_REVIEW_V03.md@7a0b0ffe8d6e3b905abb72642d41414ffcffd337
PRE_APPROVAL_REVIEW_GIT_BLOB = 672edc20d6eb9c0300485a3721315cba0b3bcdfd
PRE_APPROVAL_REVIEW_RESULT = PASS

PREVIOUS_GATE_DECISION = D-175
D175_GATE_RESULT = AUTHOR_APPROVED

CANONICAL_MASTER_BEFORE_PROMOTION = ARTICLE_MASTER_V032
CANONICAL_PROMOTION_STATUS = PENDING_MATERIALIZATION_AND_BYTE_EXACT_VERIFICATION

TARGET_MASTER = article/manuscript/ARTICLE_MASTER_V033.md
TARGET_MASTER_EXPECTED_GIT_BLOB = 9b87c71290126f5223c6e4a252f95b5d64f71f49

TITLE_B02_STATUS = AUTHOR_APPROVED / PENDING_V033_PROMOTION_VERIFICATION
KEYWORDS = NOT_AUTHORIZED_UNTIL_V033_VERIFIED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Decisión del autor

El autor aprueba explícitamente el candidato exacto Title B02 V03 que pasó D-175.

La aprobación cubre únicamente el candidato identificado por SHA-256 y Git blob esperados en esta decisión. No autoriza una reformulación, una regeneración del título ni la promoción de V01/V02.

### 2. Efecto de la aprobación

La aprobación autoral satisface el gate sustantivo de Title/Título, pero la integración canónica no se declara todavía.

Se requiere materializar el Markdown aprobado exactamente como:

`article/manuscript/ARTICLE_MASTER_V033.md`

y verificar:

```text
EXPECTED_GIT_BLOB =
9b87c71290126f5223c6e4a252f95b5d64f71f49
```

Hasta que esa identidad no sea verificada:

```text
CANONICAL_MASTER = ARTICLE_MASTER_V032
TITLE_B02_INTEGRATED = NO
KEYWORDS = NOT_AUTHORIZED
```

### 3. Word acumulativo

El Word aprobado para la siguiente etapa queda identificado como:

`ARTICLE_MASTER_CANDIDATE_TITLE_B02_V03.docx`

```text
SHA256 = 1451c7c2d9a013603c749a7ad0730ea450f76700ff853b6d96d9d1f865882ed1
SIZE_BYTES = 110921
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 71
```

Su condición de Word canónico acumulativo será efectiva después de la verificación de promoción de V033.

### 4. Gate

```text
CURRENT_GATE = FRONT_MATTER_B02_TITLE_V03_PROMOTION_VERIFICATION
NEXT_ACTOR = AUTHOR / IA_GESTORA
NEXT_ACTION = MATERIALIZE_AND_VERIFY_EXACT_V033

CANONICAL_MASTER = ARTICLE_MASTER_V032
TARGET_MASTER = ARTICLE_MASTER_V033
TARGET_MASTER_EXPECTED_GIT_BLOB = 9b87c71290126f5223c6e4a252f95b5d64f71f49

AUTHOR_APPROVAL_GATE = CLOSED / APPROVED
TITLE = AUTHOR_APPROVED / PENDING_V033_PROMOTION_VERIFICATION

KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

D-176 records explicit author approval of the exact Title B02 V03 candidate.

The substantive author-approval gate is closed as approved, but canonical integration remains pending until the exact approved Markdown is materialized as `article/manuscript/ARTICLE_MASTER_V033.md` and independently verified to have Git blob `9b87c71290126f5223c6e4a252f95b5d64f71f49`.

Until that verification, V032 remains canonical and Keywords/end matter remain unauthorized. The approved cumulative Word candidate is identified by SHA-256 `1451c7c2d9a013603c749a7ad0730ea450f76700ff853b6d96d9d1f865882ed1`.
