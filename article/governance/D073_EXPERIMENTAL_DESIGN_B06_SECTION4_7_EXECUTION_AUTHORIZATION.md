# D-073 — Autorización de ejecución B06 / Section 4.7 / B06 Section 4.7 execution authorization

## Español

```text
DECISION_ID = D-073
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-072
BLOCK = EXPERIMENTAL_DESIGN_B06
SECTION = 4.7
SECTION_TITLE = Statistical and robustness analysis
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
AUTHORIZED_PROMPT_GIT_BLOB = 23159f8e85210c78ccfbb2acec4f5b560e83b984
PROMPT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_PROMPT_INTERNAL_REVIEW_V01.md@1ca287f50580c4c023abf959bb47546bf22e3057
PROMPT_REVIEW_RESULT = PASS
B06_SECTION_4_7 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B06_V01_ONLY
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisión

Se autoriza a la IA de Redacción a ejecutar exclusivamente B06 / Section 4.7 mediante el prompt auditado indicado arriba. La autorización no permite alterar Sections 1–4.6, redactar Section 4.8 ni introducir Results.

La IA de Redacción debe usar el master V014 y el DOCX B05 V01 exactos, verificar fuentes vivas y detenerse ante drift material. Debe preservar la separación Methods/Results, los límites de inferencia y sensibilidad de D-072, y el contrato MWDP completo.

La salida válida del bloque es `EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT`. No existe gate autoral hasta después de la auditoría independiente de la entrega B06.

---

## English

```text
DECISION_ID = D-073
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-072
BLOCK = EXPERIMENTAL_DESIGN_B06
SECTION = 4.7
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
AUTHORIZED_PROMPT_GIT_BLOB = 23159f8e85210c78ccfbb2acec4f5b560e83b984
PROMPT_REVIEW_RESULT = PASS
B06_SECTION_4_7 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B06_V01_ONLY
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

The Drafting AI is authorized to execute only B06 / Section 4.7 under the independently reviewed prompt. Exact V014 and B05 V01 DOCX baselines are mandatory. Sections 1–4.6 are frozen, Section 4.8 and Results remain closed, and all D-072 inferential/sensitivity boundaries plus MWDP remain binding.