# D-174 — Front matter B02 / Final Title V03 execution authorization

## Español

```text
DECISION = D-174
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE

KBS_IDENTITY_EDITORIAL_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_KBS_IDENTITY_EDITORIAL_REVIEW_V01.md@8bbc263e0a17972d9a04e73c0ac091e416594511
KBS_IDENTITY_EDITORIAL_REVIEW_GIT_BLOB =
ba9aed182dc806c6f3407e448202909a44d32cb8

EDITORIAL_DECISION = D-173

PROMPT = article/prompts/10_FRONT_MATTER_B02_TITLE_V03.md
PROMPT_COMMIT = b7e1eabf34bee4bea81e3e0cd0e34680bfcb0ee1
PROMPT_GIT_BLOB = f9c1231f9487bd660b9e01355dce0e343261f3e9

PROMPT_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_PROMPT_INTERNAL_REVIEW_V03.md@9ad4a0b51c099e879262d52e2159642aec6df754
PROMPT_REVIEW_GIT_BLOB = b011674bb4bfd599851f9a529bf1b176c6977d72
PROMPT_REVIEW_RESULT = PASS

CANONICAL_MASTER = ARTICLE_MASTER_V032
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
CANONICAL_MASTER_MD_SHA256 = 0fcf9c2676add5128f86efc50788335bc435077bedbd7a8aedbf73f8f1549f64
CANONICAL_MASTER_MD_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156
CANONICAL_MASTER_DOCX_SIZE_BYTES = 111028
CANONICAL_MASTER_DOCX_COMMENTS = 48
CANONICAL_MASTER_DOCX_TRACKED_CHANGES = 0
CANONICAL_MASTER_DOCX_PAGE_COUNT = 71

TITLE_EN_EXACT =
Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

TITLE_ES_EXACT =
Arquitectura basada en conocimiento para el apoyo a la decisión en clasificación arancelaria: separación del ranking de candidatos, la evidencia documental y la explicación

TITLE_B02_V03_EXECUTION = AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED

EXPECTED_EXIT = FRONT_MATTER_B02_TITLE_V03_COMPLETED_PENDING_GESTORA_AUDIT
```

### Autorización

Se autoriza exclusivamente la ejecución de:

`article/prompts/10_FRONT_MATTER_B02_TITLE_V03.md`

La IA de Redacción debe materializar exactamente los títulos EN/ES fijados por D-173. No debe generar ni seleccionar alternativas.

`Knowledge-Based` caracteriza el sistema de apoyo a decisiones como conjunto y no transfiere autoridad de ranking al corpus documental o al LLM.

Debe trabajar sobre V032 y sobre el Word acumulativo aprobado después del Abstract. Ningún candidato Title V01/V02 es baseline porque ninguno recibió aprobación autoral ni promoción canónica.

La única mutación autorizada es Title/Título.

### Gate

```text
CURRENT_GATE = FRONT_MATTER_B02_TITLE_V03_EXECUTION
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_TITLE_B02_V03_ONLY
ACTIVE_AUTHORIZATION = D-174

PROMPT = article/prompts/10_FRONT_MATTER_B02_TITLE_V03.md
PROMPT_GIT_BLOB = f9c1231f9487bd660b9e01355dce0e343261f3e9

INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
INPUT_MASTER_MD_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx
INPUT_MASTER_DOCX_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156

AUTHOR_APPROVAL_GATE = NOT_OPEN
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED

EXPECTED_EXIT = FRONT_MATTER_B02_TITLE_V03_COMPLETED_PENDING_GESTORA_AUDIT
```

---

## English

D-174 authorizes only Title B02 V03. The Writing AI must materialize the exact English and Spanish titles fixed by D-173. "Knowledge-Based" is a system-level characterization only; historical retrieval remains the sole ranking authority, documentary knowledge is attached downstream, and the LLM remains explanation-only.

Canonical V032 and the approved Abstract cumulative Word file remain the baselines. Only Title/Título may change. Keywords and end matter remain unauthorized.
