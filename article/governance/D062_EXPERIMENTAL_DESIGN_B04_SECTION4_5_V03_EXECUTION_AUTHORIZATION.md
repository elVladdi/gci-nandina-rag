# D-062 — Autorización de ejecución B04 / Section 4.5 bajo Prompt V03 / B04 Section 4.5 execution authorization under Prompt V03

## Español

```text
DECISION_ID = D-062
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-061
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_PROMPT_V03_INTERNAL_REVIEW_V01.md@f19f2005d6de7b83b649677a7d29ca384765b54b
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
AUTHORIZED_PROMPT_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION
B04_PROMPT_V03 = PASS / ACTIVE / AUTHORIZED
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V03_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Base de autorización

D-061 exigió sincronizar los controles vivos y materializar un Prompt B04 V03 con el orden exacto de onboarding de `START_HERE.md`, preservando todo el alcance científico y las obligaciones acumulativas válidas de V02.

`ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` fueron sincronizados a V012/B04. El Prompt V03 fue materializado y posteriormente auditado por la IA Gestora con `VERDICT = PASS`.

### 2. Alcance autorizado

Se autoriza a la IA de Redacción a ejecutar exclusivamente:

- Part I: `4.5 Experimental system configuration and execution`;
- Part II: `4.5 Configuración y ejecución experimental`;
- bloque B04 versionado;
- master Markdown acumulativo candidato derivado de V012;
- master DOCX acumulativo candidato derivado exclusivamente del DOCX B03 exacto;
- response versionada bilingüe.

No se autoriza 4.6, 4.7, 4.8 ni Results.

### 3. Condiciones vinculantes

La ejecución válida debe usar exclusivamente Prompt V03. V01/V02 no son contratos de ejecución aceptables.

El DOCX B03 exacto debe ser proporcionado por el autor y verificar SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`. Si no está disponible o no coincide, la IA de Redacción debe bloquearse y no reconstruir el Word.

La IA de Redacción debe consultar SRC-03 y `main` vivos, re-verificar los hechos metodológicos contra artefactos primarios y registrar cualquier drift material. No puede usar los valores precargados del prompt como sustituto de esa verificación.

### 4. Gate de salida

La ejecución B04 vuelve obligatoriamente a la IA Gestora para auditoría independiente. La IA de Redacción no aprueba ni integra B04.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
NEXT_ACTOR = IA_REDACCION
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-062
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-061
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_PROMPT_V03_INTERNAL_REVIEW_V01.md@f19f2005d6de7b83b649677a7d29ca384765b54b
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
AUTHORIZED_PROMPT_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION
B04_PROMPT_V03 = PASS / ACTIVE / AUTHORIZED
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V03_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Authorization basis

D-061 required synchronization of the live controls and materialization of a B04 Prompt V03 with the exact `START_HERE.md` onboarding sequence while preserving all scientifically and procedurally valid V02 requirements.

`ARTICLE_STATUS.md` and `ARTICLE_WRITING_PLAN.md` were synchronized to V012/B04. Prompt V03 was materialized and then independently audited by the Managing AI with `VERDICT = PASS`.

### 2. Authorized scope

The Drafting AI is authorized to execute only:

- Part I: `4.5 Experimental system configuration and execution`;
- Part II: `4.5 Configuración y ejecución experimental`;
- the versioned B04 block;
- a cumulative candidate Markdown master derived from V012;
- a cumulative candidate DOCX master derived only from the exact B03 DOCX;
- the bilingual versioned response.

Sections 4.6, 4.7, 4.8, and Results remain unauthorized.

### 3. Binding conditions

A valid execution must use Prompt V03 only. V01/V02 are not acceptable execution contracts.

The exact B03 DOCX must be supplied by the author and verify SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`. If unavailable or mismatched, the Drafting AI must block and must not reconstruct Word.

The Drafting AI must consult live SRC-03 and `main`, re-verify methodological facts against primary artifacts, and record any material drift. Preloaded values in the prompt do not substitute for live verification.

### 4. Exit gate

B04 execution must return to the Managing AI for independent audit. The Drafting AI may neither approve nor integrate B04.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
NEXT_ACTOR = DRAFTING_AI
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```