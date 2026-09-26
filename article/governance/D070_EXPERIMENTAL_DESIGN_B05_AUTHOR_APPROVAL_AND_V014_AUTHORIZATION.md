# D-070 — Aprobación autoral de B05 y autorización de promoción a V014 / B05 author approval and V014 promotion authorization

## Español

```text
DECISION_ID = D-070
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-069
AUTHOR_DECISION = APPROVED
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 / 4.6.1–4.6.3
SECTION_TITLE = Evaluation framework and protocols
SECTION_STATE = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SCIENTIFIC_TECHNICAL_REVIEW = PASS
RESPONSE_METADATA_CORRECTION_REVIEW = PASS
AUTHOR_APPROVAL_GATE = SATISFIED
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V013
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
B05_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
B05_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
B05_CANDIDATE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CITATION_COMMENTS = 40 / PRESERVED
V014_PROMOTION = AUTHORIZED / PENDING_BYTE_EXACT_MATERIALIZATION_AND_VERIFICATION
B06 / SECTION_4_7 = NOT_AUTHORIZED_UNTIL_V014_INTEGRATION_CLOSE
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Decisión autoral

El autor aprobó expresamente B05 V01 / Section 4.6 después de:

- auditoría científica/técnica independiente de la IA Gestora;
- corrección documental de la response para registrar C14 como claim condicional utilizado bajo límites explícitos;
- revisión `PASS` del microgate de metadata;
- verificación de que no se modificaron el contenido científico ni los candidatos acumulativos Markdown/DOCX durante la corrección documental.

La aprobación autoral no altera las identidades ya auditadas de los candidatos B05.

### 2. Contenido congelado

Queda aprobado y congelado el contenido bilingüe de:

- 4.6 `Evaluation framework and protocols`;
- 4.6.1 `Candidate-retrieval evaluation`;
- 4.6.2 `Documentary-evidence evaluation`;
- 4.6.3 `Controlled-explanation evaluation`.

Se preservan las fronteras científicas:

- candidate retrieval ≠ overall classification accuracy;
- documentary association ≠ substantive normative/legal correctness;
- auditability ≠ legal correctness;
- automatic HE4 checks ≠ qualitative rubric;
- la modalidad cualitativa efectiva fue `AI_EXPERT_ROLE / LLM-as-judge`, con `HUMAN_SCORING = FALSE`;
- C14 es el único claim condicional usado y sus límites explícitos están satisfechos;
- resultados observados permanecen fuera de Methods.

### 3. Promoción autorizada

Se autoriza materializar el candidato Markdown aprobado, sin ninguna modificación, como:

`article/manuscript/ARTICLE_MASTER_V014.md`

La promoción solo puede declararse completada si el archivo materializado conserva exactamente:

```text
SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
```

Hasta completar esa verificación, `ARTICLE_MASTER_V013.md` sigue siendo el master canónico.

El DOCX aprobado permanece bajo custodia local del autor:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx`

SHA-256:

`b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2`.

### 4. Gate

```text
CURRENT_GATE = B05_V014_PROMOTION
NEXT_ACTOR = AUTHOR / IA_GESTORA
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V014
B05 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V013
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
B06 / SECTION_4_7 = NOT_AUTHORIZED_UNTIL_V014_INTEGRATION_CLOSE
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-070
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-069
AUTHOR_DECISION = APPROVED
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 / 4.6.1–4.6.3
SECTION_STATE = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SCIENTIFIC_TECHNICAL_REVIEW = PASS
RESPONSE_METADATA_CORRECTION_REVIEW = PASS
AUTHOR_APPROVAL_GATE = SATISFIED
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V013
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
B05_CANDIDATE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CITATION_COMMENTS = 40 / PRESERVED
V014_PROMOTION = AUTHORIZED / PENDING_BYTE_EXACT_MATERIALIZATION_AND_VERIFICATION
B06 / SECTION_4_7 = NOT_AUTHORIZED_UNTIL_V014_INTEGRATION_CLOSE
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The author explicitly approved B05 V01 / Section 4.6 after the independent scientific/technical review and the response-metadata corrective microgate both passed. The correction did not alter scientific manuscript content or either cumulative candidate.

The bilingual content of Sections 4.6 and 4.6.1–4.6.3 is therefore approved and frozen. The approved Markdown candidate may be materialized unchanged as `article/manuscript/ARTICLE_MASTER_V014.md`, provided its SHA-256 and Git blob match the frozen identities above. Until that verification is complete, V013 remains canonical.

The approved cumulative DOCX remains in local author custody with the frozen SHA-256 above. Section 4.7, Section 4.8, and Results remain closed until the V014 integration gate is completed.