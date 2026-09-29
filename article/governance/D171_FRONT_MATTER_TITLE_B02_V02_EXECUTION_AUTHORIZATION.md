# D-171 — Front matter B02 / Final Title V02 execution authorization

## Español

```text
DECISION = D-171
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE

EDITORIAL_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_KBS_CORPUS_EDITORIAL_REVIEW_V01.md@6e0043e394d3bd996f13d0ec7bd8f8983df5fc71
EDITORIAL_REVIEW_GIT_BLOB =
99e1a51de0eab71159fdfe843bd7c0a9794d6002

EDITORIAL_DECISION = D-170

PROMPT = article/prompts/10_FRONT_MATTER_B02_TITLE_V02.md
PROMPT_COMMIT = 1e91b5540ea2abda6e202afb54bde3363469881d
PROMPT_GIT_BLOB = 8a86f760bf7353222e5610312b11525ec5793385

PROMPT_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_PROMPT_INTERNAL_REVIEW_V02.md@176029244c65e1a26486fa13b7699dde8dcc5cf6
PROMPT_REVIEW_GIT_BLOB = ad03b75295e6265d60656774e294c92d9a2f036f
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
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support

TITLE_ES_EXACT =
Separación del ranking de candidatos, la evidencia documental y la explicación en el apoyo a la decisión de clasificación arancelaria

TITLE_B02_V02_EXECUTION = AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED

EXPECTED_EXIT = FRONT_MATTER_B02_TITLE_V02_COMPLETED_PENDING_GESTORA_AUDIT
```

### Autorización

Se autoriza exclusivamente la ejecución de:

`article/prompts/10_FRONT_MATTER_B02_TITLE_V02.md`

La IA de Redacción debe materializar exactamente los títulos EN/ES fijados por D-170. No debe generar ni seleccionar alternativas.

Debe trabajar sobre V032 y sobre el Word acumulativo aprobado después del Abstract. El candidato Title V01 no es baseline porque nunca recibió aprobación autoral ni promoción canónica.

La única mutación autorizada es Title/Título.

Se preservan:

- Abstract/Resumen;
- Keywords/Palabras clave placeholders;
- Sections 1–7;
- end matter;
- comentarios y anclajes;
- cero tracked changes.

### Gate

```text
CURRENT_GATE = FRONT_MATTER_B02_TITLE_V02_EXECUTION
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_TITLE_B02_V02_ONLY
ACTIVE_AUTHORIZATION = D-171

PROMPT = article/prompts/10_FRONT_MATTER_B02_TITLE_V02.md
PROMPT_GIT_BLOB = 8a86f760bf7353222e5610312b11525ec5793385

INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
INPUT_MASTER_MD_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx
INPUT_MASTER_DOCX_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156

AUTHOR_APPROVAL_GATE = NOT_OPEN
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED

EXPECTED_EXIT = FRONT_MATTER_B02_TITLE_V02_COMPLETED_PENDING_GESTORA_AUDIT
```

---

## English

D-171 authorizes only Title B02 V02. The Writing AI must materialize the exact English and Spanish titles fixed by the full accepted-KBS-corpus editorial audit and D-170. Canonical V032 and the approved Abstract cumulative Word file remain the baselines. Only Title/Título may change. Keywords and end matter remain unauthorized.
