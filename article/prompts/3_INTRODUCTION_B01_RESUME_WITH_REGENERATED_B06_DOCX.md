# Introduction B01 — Reanudación con baseline B06 regenerado y auditado

## 1. Objetivo único

Reanuda y ejecuta exclusivamente `INTRODUCTION_B01 / Section 1 Introduction` como primera versión científica provisional.

La recuperación técnica del DOCX B06 ya concluyó. No vuelvas a regenerar B06, no reabras Related Work y no ejecutes ninguna sección posterior.

## 2. Gobernanza de reanudación

Lee y aplica obligatoriamente:

- `article/prompts/3_INTRODUCTION_B01_PROVISIONAL.md@2880ae515431388f3736e647a9692a93e0f4fb4d` como fuente completa de las instrucciones científicas de Introduction B01;
- `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`;
- `article/governance/D028_CONTROLLED_REGENERATION_OF_LOST_B06_DOCX.md`;
- `article/governance/D029_REGENERATED_B06_DOCX_ACCEPTANCE_AND_INTRODUCTION_B01_RESUME.md`;
- `article/reviews/3_INTRODUCTION_B01_B06_DOCX_REGENERATION_INTERNAL_REVIEW_V01.md@063dd87c6889e91cefe2b69102180d8cd2f092e1`.

D-029 sustituye exclusivamente los campos antiguos de identidad/custodia del DOCX B06 que todavía puedan aparecer en `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, D-025 o prompts anteriores. No altera ninguna frontera científica.

## 3. Baselines obligatorios

### Markdown canónico

```text
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V006.md
CANONICAL_MASTER_MD_GIT_BLOB = 7d3c7a71cd6578ffc0b93df80ea12e4172833a1a
```

Verifica el blob antes de redactar.

### DOCX acumulativo gobernante

El único Word autorizado como baseline es el archivo entregado al autor y aceptado por D-029:

```text
GOVERNING_B06_DOCX = ARTICLE_MASTER_B06_REGENERATED_V01.docx OR BYTE_IDENTICAL_LOCAL_RENAME
REQUIRED_SHA256 = 7050cf9fee27687c7b9ed66d0ee110ef38b7aca1671868aaf3065fe50432377b
INHERITED_COMMENTS = 36
TRACKED_CHANGES_EXPECTED = 0
```

Antes de redactar una sola oración, calcula SHA-256. Si no coincide exactamente, detente y no modifiques el archivo.

El hash `3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0` corresponde al B06 original perdido y **no debe utilizarse como baseline activo**.

## 4. Alcance científico

Si ambos baselines pasan, ejecuta íntegramente las reglas científicas del prompt original `3_INTRODUCTION_B01_PROVISIONAL.md`.

Mantén como alcance exclusivo:

`SECTION_1_PROVISIONAL_ONLY`

La Introduction debe seguir:

`problema concreto → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones acotadas → contexto de evaluación → RQs → roadmap`

Debe hacer explícito, con lenguaje concreto, que:

1. la recuperación histórica genera y ordena candidatos;
2. ranking y Top-3 quedan fijados antes de la recuperación normativa;
3. la recuperación normativa asocia evidencia a esos candidatos sin insertarlos, eliminarlos, sustituirlos ni reordenarlos;
4. el LLM local downstream produce explicación sin modificar candidatos ni retroalimentar la clasificación;
5. ranking, asociación documental y explicación son salidas diferentes y se evalúan por función;
6. las particiones respetan DAM cuando existe dependencia;
7. banco histórico, espacio de clases y corpus documental son configurables/reinstanciables, sin convertir configurabilidad en generalización empírica.

Presenta RQ1–RQ4 conforme al prompt original y a 0C, sin códigos internos.

## 5. Fronteras obligatorias

Debe permanecer cierto:

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Queda prohibido:

- `first`, `novel`, `unique`, `unprecedented` o equivalentes;
- ausencia universal de prior art;
- SOTA o superioridad cross-study;
- resultados, porcentajes, p-values o conclusiones empíricas del presente estudio;
- legal/substantive correctness derivada de evidencia o explicación;
- generalización empírica derivada de configurabilidad/reproducibilidad;
- abrir o redactar Decision-support architecture, Experimental design, Results, Discussion, Conclusion, Abstract, Title, Keywords o end matter.

Related Work 2.1–2.6 debe permanecer preservado.

## 6. Versionado de salida

Los intentos V01 y V02 de respuesta documentaron blockers y no produjeron prosa científica de Introduction. Por ello:

### Primera versión científica de Introduction

1. `article/sections/introduction/Introduction_B01_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.docx` — archivo local que DEBE entregarse efectivamente al autor conforme a D-027

### Respuesta operativa

4. `article/responses/3_INTRODUCTION_B01_RESPONSE_V03.md`

No sobrescribas V01 ni V02 de las respuestas anteriores.

## 7. QA obligatorio

Registra en la respuesta V03, como mínimo:

- baseline MD blob exacto = `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`;
- baseline DOCX SHA-256 exacto = `7050cf9fee27687c7b9ed66d0ee110ef38b7aca1671868aaf3065fe50432377b`;
- 36/36 comentarios heredados preservados;
- Related Work 2.1–2.6 preservado exactamente;
- número de citas nuevas de Introduction y cobertura de comentarios;
- equivalencia semántica EN–ES;
- RQ1–RQ4 presentes y semánticamente alineadas;
- ausencia de resultados, novelty, SOTA y universal-absence claims;
- ausencia de generalización empírica no evaluada;
- cero tracked changes;
- integridad OOXML;
- render completo e inspección visual;
- SHA-256 final del candidato DOCX;
- entrega efectiva del candidato DOCX al autor;
- Introduction como único contenido científico nuevo;
- secciones posteriores no modificadas;
- `FINAL_GAP = NOT_DEFINED`;
- `NOVELTY = NOT_DECLARED`.

## 8. Commit

Si la ejecución y el QA concluyen correctamente, crea un único commit semántico que añada exclusivamente:

- `article/sections/introduction/Introduction_B01_V01.md`
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.md`
- `article/responses/3_INTRODUCTION_B01_RESPONSE_V03.md`

No subas el DOCX a GitHub. No modifiques `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, governance, el master canónico, Related Work ni ninguna sección posterior.

## 9. Entrega al autor y respuesta de chat

Conforme a D-027, entrega primero `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.docx` al autor mediante archivo descargable en la sesión y registra su SHA-256.

Después del commit, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_RESPONSE_V03.md@<commit_sha>`

Después, detente. La IA Gestora realizará auditoría científica independiente. No promuevas `ARTICLE_MASTER_V007` ni abras Decision-support architecture.