# Introduction B01 — Resume after exact B06 DOCX access

## 1. Propósito

Reanuda exclusivamente `INTRODUCTION_B01 / Section 1 Introduction` después de las dos detenciones correctamente documentadas:

- `article/responses/3_INTRODUCTION_B01_RESPONSE_V01.md@86f6e5ff5e6bc4c1dd24a38c9d897dd31dd8f59a` — baseline DOCX no disponible;
- `article/responses/3_INTRODUCTION_B01_RESPONSE_V02.md@bd10f0576dedbda23fb4966a437e10dce5e1c78b` — DOCX proporcionado corresponde a B05 y no al baseline B06.

Revisa además:

- `article/reviews/3_INTRODUCTION_B01_BLOCKER_REVIEW_V01.md`;
- `article/reviews/3_INTRODUCTION_B01_BLOCKER_REVIEW_V02.md`.

Este prompt no abre un bloque nuevo. Introduction B01 continúa siendo el único bloque autorizado.

## 2. Fuente científica gobernante

Lee y aplica íntegramente:

`article/prompts/3_INTRODUCTION_B01_PROVISIONAL.md@2880ae515431388f3736e647a9692a93e0f4fb4d`

Todas sus reglas científicas, narrativas, bibliográficas, terminológicas, de estilo, QA y alcance permanecen vigentes.

## 3. Gate binario obligatorio

Antes de redactar una sola oración, localiza el DOCX proporcionado por el autor y calcula SHA-256.

El único baseline aceptable es:

```text
APPROVED_B06_DOCX = ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx OR BYTE_IDENTICAL_LOCAL_RENAME
REQUIRED_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
INHERITED_COMMENTS = 36
TRACKED_CHANGES_EXPECTED = 0
```

No aceptes el SHA-256 de B05:

`042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`

Si el archivo falta o el SHA-256 no coincide exactamente, detente sin redactar y versiona exclusivamente:

`article/responses/3_INTRODUCTION_B01_RESPONSE_V03.md`

con el estado aplicable (`BASELINE_DOCX_ACCESS_REQUIRED` o `BASELINE_DOCX_SHA256_MISMATCH`).

No reconstruyas el Word desde Markdown y no continúes con un baseline anterior.

## 4. Baseline Markdown

Verifica:

```text
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V006.md
REQUIRED_GIT_BLOB = 7d3c7a71cd6578ffc0b93df80ea12e4172833a1a
```

Related Work 2.1–2.6 debe preservarse exactamente.

## 5. Ejecución científica

Si ambos baselines pasan, ejecuta íntegramente Introduction B01 según el prompt original.

Mantén:

```text
AUTHORIZED_SCOPE = SECTION_1_PROVISIONAL_ONLY
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No abras Decision-support architecture, Experimental design, Results, Discussion, Conclusion, Abstract, Title, Keywords ni end matter.

No presentes resultados del estudio, SOTA, novelty absoluta, ausencia universal de prior art, legal correctness ni generalización empírica fuera del testbed.

## 6. Artefactos

Como aún no existe una versión científica de Introduction, conserva:

1. `article/sections/introduction/Introduction_B01_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.docx` — solo local bajo D-021

La respuesta operativa será ahora:

4. `article/responses/3_INTRODUCTION_B01_RESPONSE_V03.md`

No sobrescribas V01 ni V02.

## 7. QA obligatorio

Además de todo el QA del prompt original, registra expresamente:

- baseline DOCX SHA-256 exacto = `3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`;
- baseline MD blob exacto = `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`;
- 36/36 comentarios heredados preservados;
- Related Work 2.1–2.6 preservado exactamente;
- número de nuevas citas y cobertura de comentarios;
- equivalencia EN–ES;
- RQ1–RQ4 presentes y alineadas;
- ausencia de resultados, novelty, SOTA y universal-absence claims;
- OOXML `PASS`;
- tracked changes = 0;
- render completo;
- SHA-256 final del DOCX candidato;
- Introduction como único contenido científico nuevo;
- secciones posteriores sin cambios.

## 8. Commit

Si ejecución y QA pasan, crea un único commit semántico que añada exclusivamente:

- `article/sections/introduction/Introduction_B01_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
- `article/responses/3_INTRODUCTION_B01_RESPONSE_V03.md`

No subas el DOCX. No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, governance, masters canónicos, Related Work ni secciones posteriores.

## 9. Respuesta en chat

Conforme a D-022, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_RESPONSE_V03.md@<commit_sha>`

Después, detente. La IA Gestora realizará auditoría científica independiente antes de cualquier aprobación, integración o apertura del siguiente bloque.