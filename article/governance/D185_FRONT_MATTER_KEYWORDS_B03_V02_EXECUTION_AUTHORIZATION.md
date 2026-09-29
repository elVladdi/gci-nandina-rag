# D-185 — Front matter B03 / Final Keywords V02 execution authorization

## Español

```text
DECISION = D-185
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B03_KEYWORDS

COMPLIANCE_REVIEW =
article/reviews/11_FRONT_MATTER_B03_KEYWORDS_KBS_SUBMISSION_COMPLIANCE_REVIEW_V01.md@cf3ceb70d6dc109e47cc80b1bf3b8b58f0c3a5ca
COMPLIANCE_REVIEW_GIT_BLOB =
b0f816647b041e7ece171cefb41d6ebd0bbf128a

EDITORIAL_DECISION = D-184

PROMPT = article/prompts/11_FRONT_MATTER_B03_KEYWORDS_V02.md
PROMPT_COMMIT = 3bc3c90f16d4f26543b4ca1d96c3b9c9358f4424
PROMPT_GIT_BLOB = 8ae3ee8adb089e3fc998c758b3e7eae85bc40b9d

PROMPT_REVIEW =
article/reviews/11_FRONT_MATTER_B03_KEYWORDS_PROMPT_INTERNAL_REVIEW_V02.md@6f68b1c46bcd8855ed4c318cdb83bc14f45e02e4
PROMPT_REVIEW_GIT_BLOB = 679b7384f7b2b9c8a93a2624046ac932596fb961
PROMPT_REVIEW_RESULT = PASS

CANONICAL_MASTER = ARTICLE_MASTER_V034
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V034.md
CANONICAL_MASTER_MD_SHA256 = 37994390a1be96d6c37bceb6536ea367b0918872b63180e2f5531ba32856f6ca
CANONICAL_MASTER_MD_GIT_BLOB = 0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684

CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 8e31acd688e0e7b52a8f132ed12f342178c75daf9bfe1dbb4d8c44137f317b84
CANONICAL_MASTER_DOCX_SIZE_BYTES = 110943
CANONICAL_MASTER_DOCX_COMMENTS = 48
CANONICAL_MASTER_DOCX_TRACKED_CHANGES = 0
CANONICAL_MASTER_DOCX_PAGE_COUNT = 71

KEYWORDS_EN_EXACT =
Knowledge-based decision support; Tariff classification; Harmonized System; Information retrieval; Large language model; Provenance

KEYWORDS_ES_EXACT =
Apoyo a la decisión basado en conocimiento; Clasificación arancelaria; Sistema Armonizado; Recuperación de información; Modelo de lenguaje grande; Procedencia

KEYWORDS_B03_V02_EXECUTION = AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
END_MATTER_FINALIZATION = NOT_AUTHORIZED

EXPECTED_EXIT =
FRONT_MATTER_B03_KEYWORDS_V02_COMPLETED_PENDING_GESTORA_AUDIT
```

### Autorización

Se autoriza exclusivamente la ejecución de:

`article/prompts/11_FRONT_MATTER_B03_KEYWORDS_V02.md`

La IA de Redacción debe materializar exactamente seis Keywords/Palabras clave, sin generar alternativas.

Debe trabajar sobre V034 y sobre el Word acumulativo aprobado después de Keywords B03 V01.

La única mutación autorizada es la sustitución de las líneas Keywords/Palabras clave.

Title/Título, Abstract/Resumen, Sections 1–7 y End Matter permanecen congelados.

### Gate

```text
CURRENT_DRAFTING_PHASE = FRONT_MATTER / KEYWORDS
CURRENT_GATE = FRONT_MATTER_B03_KEYWORDS_V02_EXECUTION
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_KEYWORDS_B03_V02_ONLY
ACTIVE_AUTHORIZATION = D-185

PROMPT = article/prompts/11_FRONT_MATTER_B03_KEYWORDS_V02.md
PROMPT_GIT_BLOB = 8ae3ee8adb089e3fc998c758b3e7eae85bc40b9d

INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V034.md
INPUT_MASTER_MD_GIT_BLOB = 0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684

INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_KEYWORDS_B03_V01.docx
INPUT_MASTER_DOCX_SHA256 =
8e31acd688e0e7b52a8f132ed12f342178c75daf9bfe1dbb4d8c44137f317b84

AUTHOR_APPROVAL_GATE = NOT_OPEN
END_MATTER_FINALIZATION = NOT_AUTHORIZED

EXPECTED_EXIT =
FRONT_MATTER_B03_KEYWORDS_V02_COMPLETED_PENDING_GESTORA_AUDIT
```

---

## English

D-185 authorizes only Keywords B03 V02.

The Writing AI must materialize the exact six English and Spanish keywords fixed by D-184. Canonical V034 and the approved Keywords B03 V01 cumulative Word file are the baselines.

Only Keywords/Palabras clave may change. Title, Abstract, Sections 1–7, and End Matter remain frozen.
