# Introduction B01 — Resume after exact DOCX access

## 1. Propósito

Reanuda exclusivamente `INTRODUCTION_B01 / Section 1 Introduction` después del bloqueo documentado en:

`article/responses/3_INTRODUCTION_B01_RESPONSE_V01.md@86f6e5ff5e6bc4c1dd24a38c9d897dd31dd8f59a`

y revisado por la IA Gestora en:

`article/reviews/3_INTRODUCTION_B01_BLOCKER_REVIEW_V01.md`.

Este prompt no abre un bloque nuevo y no sustituye las reglas científicas del prompt original. Su única función es permitir la reanudación segura cuando el DOCX acumulativo exacto de B06 haya sido proporcionado a la sesión activa.

## 2. Fuente de instrucciones científicas

Lee y aplica íntegramente el prompt original:

`article/prompts/3_INTRODUCTION_B01_PROVISIONAL.md@2880ae515431388f3736e647a9692a93e0f4fb4d`

Todas sus reglas de alcance, narrativa, citas, contribuciones, RQs, configurabilidad, estilo, fronteras científicas, QA y prohibiciones continúan vigentes salvo las precisiones de versionado establecidas en este prompt de reanudación.

## 3. Precondición obligatoria: DOCX exacto

Antes de redactar una sola oración, localiza en la sesión activa el DOCX proporcionado por el autor y calcula su SHA-256.

El único baseline aceptable es:

```text
APPROVED_B06_DOCX = ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx OR BYTE_IDENTICAL_LOCAL_RENAME
REQUIRED_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
INHERITED_COMMENTS = 36
TRACKED_CHANGES_EXPECTED = 0
```

Si el SHA-256 no coincide exactamente, detente. No edites el archivo, no reconstruyas desde Markdown y no uses un DOCX aproximado o una versión anterior.

En ese caso versiona exclusivamente:

`article/responses/3_INTRODUCTION_B01_RESPONSE_V02.md`

con el estado `BASELINE_DOCX_SHA256_MISMATCH`, y detente.

## 4. Baseline Markdown

Verifica además el master Markdown canónico:

`article/manuscript/ARTICLE_MASTER_V006.md`

Git blob gobernante:

`7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`

La redacción debe partir conceptualmente de este master y el DOCX exacto anterior. Related Work 2.1–2.6 debe preservarse sin cambios.

## 5. Reanudación de Introduction B01

Si ambos baselines pasan las verificaciones, ejecuta íntegramente las tareas científicas del prompt original.

Mantén como alcance exclusivo:

`SECTION_1_PROVISIONAL_ONLY`

No abras ni redactes Decision-support architecture, Experimental design, Results, Discussion, Conclusion, Abstract, Title, Keywords ni end matter.

Debe permanecer cierto:

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No presentes resultados del estudio, novelty absoluta, SOTA, ausencia universal de prior art, legal correctness ni generalización empírica fuera del testbed.

## 6. Versionado de artefactos tras la reanudación

La ejecución previa no creó artefactos científicos. Por tanto, la primera versión científica de Introduction conserva `V01`:

1. `article/sections/introduction/Introduction_B01_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.docx` — solo local, bajo D-021

La respuesta operativa debe ser `V02`, porque `V01` ya documenta el bloqueo inicial:

4. `article/responses/3_INTRODUCTION_B01_RESPONSE_V02.md`

No sobrescribas ni elimines `3_INTRODUCTION_B01_RESPONSE_V01.md`.

## 7. QA obligatorio

Aplica todos los controles del prompt original y registra expresamente en la respuesta V02:

- SHA-256 del baseline DOCX = `3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`;
- baseline MD blob = `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`;
- 36/36 comentarios heredados preservados;
- Related Work 2.1–2.6 preservado exactamente;
- número de citas nuevas y cobertura de comentarios;
- equivalencia EN–ES;
- RQ1–RQ4 presentes y semánticamente alineadas;
- ausencia de resultados, novelty, SOTA y universal-absence claims;
- integridad OOXML;
- cero tracked changes;
- render completo;
- SHA-256 final del DOCX candidato;
- Introduction como único contenido científico nuevo;
- secciones posteriores no modificadas.

## 8. Commit

Si la ejecución científica y el QA concluyen correctamente, crea un único commit semántico que añada exclusivamente:

- `article/sections/introduction/Introduction_B01_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
- `article/responses/3_INTRODUCTION_B01_RESPONSE_V02.md`

No subas el DOCX. No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, governance, masters canónicos, Related Work ni secciones posteriores.

## 9. Respuesta en chat

Conforme a D-022, después del commit responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_RESPONSE_V02.md@<commit_sha>`

Después, detente. La IA Gestora realizará la auditoría científica independiente antes de cualquier aprobación, integración o apertura de Decision-support architecture.