# D-068 — Experimental Design B05 / Section 4.6 execution authorization

## Español

```text
DECISION_ID = D-068
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-067
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 Evaluation framework and protocols
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99
PROMPT_GIT_BLOB = 55108c6628da436c601b8a69a8397c32b2c0589d
PROMPT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_PROMPT_INTERNAL_REVIEW_V01.md@03d70a8f891b98956fd69f39a972497e6eec8886
PROMPT_REVIEW_RESULT = PASS
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
SECTION_4_6 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B05_V01_ONLY
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Autorización

La sincronización de ground truth B05 quedó registrada en D-067. El prompt atómico B05 V01 fue materializado y sometido a revisión interna independiente. La revisión emitió `PASS` sin correcciones.

Se autoriza exclusivamente la ejecución de:

`article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99`

sobre los baselines exactos congelados.

### 2. Alcance

La autorización cubre únicamente:

- 4.6 Evaluation framework and protocols;
- 4.6.1 Candidate-retrieval evaluation;
- 4.6.2 Documentary-evidence evaluation;
- 4.6.3 Controlled-explanation evaluation;
- sus espejos españoles;
- generación del master Markdown candidato acumulativo B05 V01;
- generación y handoff del DOCX candidato acumulativo B05 V01.

No se autoriza 4.7, 4.8, Results, Discussion, Conclusion, Abstract, Title ni Keywords.

### 3. Baselines vinculantes

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
BASELINE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx
BASELINE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
PRIOR_CITATION_COMMENTS = 40 / PRESERVE
```

Si el DOCX exacto no está disponible, la ejecución debe bloquearse. No se permite reconstrucción.

### 4. Gate de salida

La entrega vuelve a la IA Gestora para auditoría independiente. El PASS de Redacción no abre el gate autoral ni B06.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-068
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-067
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 Evaluation framework and protocols
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99
PROMPT_GIT_BLOB = 55108c6628da436c601b8a69a8397c32b2c0589d
PROMPT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_PROMPT_INTERNAL_REVIEW_V01.md@03d70a8f891b98956fd69f39a972497e6eec8886
PROMPT_REVIEW_RESULT = PASS
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
SECTION_4_6 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B05_V01_ONLY
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

D-067 completed the B05 ground-truth synchronization. The atomic B05 V01 prompt was then materialized and independently audited with `PASS`. Execution of that exact prompt is therefore authorized against canonical V013 and the exact B04 V02 cumulative DOCX baseline.

Authorization is limited to Section 4.6 and Sections 4.6.1–4.6.3 in English and Spanish, plus the cumulative Markdown/DOCX B05 V01 candidates. Section 4.7, Section 4.8, Results, Discussion, Conclusion, Abstract, Title, and Keywords remain closed.

The resulting B05 delivery must return to the Managing AI for independent audit; it does not open author approval or B06 automatically.