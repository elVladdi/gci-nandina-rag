# D-069 — Experimental Design B05 V01 PASS and author-approval gate

## Español

```text
DECISION_ID = D-069
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 Evaluation framework and protocols
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99
EXECUTION_RESPONSE_V01 = article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md@ee7cd01b652d85791c84eeb26398b224038074ca
EXECUTION_RESPONSE_V02 = article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V02.md@9e9546a9d052c1fc1145bf42d37f53e7bcd0ba84
PRIMARY_INTERNAL_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_INTERNAL_REVIEW_V01.md@bad6a978ef0a6e70c6db675cf77ff8bf7f2942cf
METADATA_CORRECTION_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B05_RESPONSE_METADATA_CORRECTION_REVIEW_V01.md@f8e611bc359bd9c408595907355b755bf82c602f
METADATA_CORRECTION_REVIEW_RESULT = PASS
BASELINE_CANONICAL_MASTER = ARTICLE_MASTER_V013
B05_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md / LOCAL_AUTHOR_CUSTODY
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
B05_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
B05_CANDIDATE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
SCIENTIFIC_CONTENT = PASS
CLAIM_EVIDENCE = PASS
DOCX_TECHNICAL_AUDIT = PASS
RESPONSE_METADATA = PASS
EXPERIMENTAL_DESIGN_B05 = PASS / PENDING_AUTHOR_APPROVAL
SECTION_4_6 = PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
INTEGRATION = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Base de la decisión

La revisión científica/técnica primaria de B05 concluyó que Section 4.6 y los candidatos acumulativos Markdown/DOCX eran correctos, pero detectó una única inconsistencia documental en la response V01: el autocontrol omitía C14 como claim condicional utilizado bajo límites explícitos.

La IA de Redacción ejecutó el microgate de metadata sin modificar el artefacto científico ni los candidatos acumulativos. La response V02 registra C14 correctamente en español e inglés, mantiene las limitaciones de auditabilidad y de modalidad del evaluador, y conserva las identidades previamente auditadas de los candidatos.

La revisión independiente del microgate emitió `PASS`.

### 2. Estado científico de B05

Section 4.6 queda científicamente y técnicamente apta para decisión autoral. En particular:

- RQ1 permanece limitado a candidate retrieval;
- RQ2 permanece limitado a documentary coverage/association/traceability sobre el Top-3 fijo;
- RQ3 separa controles automáticos y rúbrica cualitativa;
- la modalidad HE4 ejecutada permanece declarada como `AI_EXPERT_ROLE / LLM-as-judge`, con `HUMAN_SCORING = FALSE`;
- C14 se usa únicamente con los límites explícitos requeridos;
- candidate retrieval no se presenta como accuracy global;
- documentary association no se presenta como substantive normative/legal correctness;
- auditability no se presenta como legal correctness;
- no se incorporaron valores observados de Results ni inferencia de Section 4.7.

### 3. Gate autoral

Se abre exclusivamente el gate de aprobación del autor sobre B05 V01 / Section 4.6 y sus candidatos acumulativos exactos.

La aprobación no se presume. Hasta que el autor emita una decisión expresa:

- `ARTICLE_MASTER_V013.md` sigue siendo el master canónico;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md` sigue siendo candidato local;
- el DOCX B05 V01 permanece bajo custodia local;
- no se materializa `ARTICLE_MASTER_V014.md`;
- B06/Section 4.7, Section 4.8 y Results continúan cerrados.

Si el autor aprueba B05, la IA Gestora deberá registrar esa aprobación en una decisión separada y autorizar únicamente la promoción byte-exacta del candidato Markdown aprobado a `article/manuscript/ARTICLE_MASTER_V014.md`, seguida de verificación de identidad e integración técnica antes de preparar B06.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
EXPECTED_DECISION = APPROVE / REQUEST_CORRECTION
AUTHOR_APPROVAL_GATE = OPEN
INTEGRATION = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-069
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 Evaluation framework and protocols
SCIENTIFIC_CONTENT = PASS
CLAIM_EVIDENCE = PASS
DOCX_TECHNICAL_AUDIT = PASS
RESPONSE_METADATA = PASS
EXPERIMENTAL_DESIGN_B05 = PASS / PENDING_AUTHOR_APPROVAL
SECTION_4_6 = PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
INTEGRATION = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The B05 scientific/technical review had already passed the manuscript section and cumulative Markdown/DOCX candidates, with one blocking response-metadata defect. Response V02 corrects that defect by explicitly identifying C14 as the sole conditional claim used under satisfied limitations, without changing manuscript science or the cumulative candidate artifacts. Independent review of that microgate passed.

The author-approval gate is therefore open. Canonical V013 remains in force and no V014 promotion or B06 drafting is authorized until explicit author approval is received and subsequently recorded.