# Introduction B01 — V02 minor corrections after internal review

## 1. Objective único

Corrige exclusivamente `INTRODUCTION_B01` conforme a:

`article/reviews/3_INTRODUCTION_B01_INTERNAL_REVIEW_V01.md@ea7f8b3e0226fabcbbd4c503a1e12690bbbca9f6`

No reescribas la Introduction desde cero. No abras ni redactes Decision-support architecture, Experimental design, Results, Discussion ni ninguna sección posterior.

Esta ejecución tiene exactamente tres correcciones obligatorias: B01-C01, B01-C02 y B01-C03. Todo contenido científico de V01 que no esté afectado por ellas debe conservarse.

## 2. Estado de entrada

La revisión interna determinó:

```text
INTRODUCTION_B01_V01 = PASS_WITH_MINOR_MANDATORY_CORRECTIONS
SOURCE_SUPPORT = PASS / 4_OF_4
DOCX_TECHNICAL_QA = PASS
RELATED_WORK_PRESERVATION = PASS
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_BLOCK = NOT_AUTHORIZED
```

El commit V03 `7125a0df89c575f7edc358c58809249d055a9cd9` contiene solamente la respuesta operativa porque el cierre Markdown quedó técnicamente incompleto. No intentes reconstruir retrospectivamente un supuesto master V01 idéntico ni hagas commits auxiliares para backfill. Esta V02 debe producir una entrega científica completa y versionada.

## 3. Baselines obligatorios

### Markdown canónico acumulativo

```text
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V006.md
CANONICAL_MASTER_MD_GIT_BLOB = 7d3c7a71cd6578ffc0b93df80ea12e4172833a1a
```

El master candidato V02 debe construirse desde este Markdown canónico reemplazando exclusivamente el placeholder de Introduction en Part I y Part II por la Introduction V02 corregida. Related Work 2.1–2.6 y todo contenido posterior deben conservarse exactamente.

### DOCX candidato V01 entregado al autor

Trabaja sobre el DOCX científico V01 ya entregado, auditado por la IA Gestora:

```text
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V01.docx OR BYTE_IDENTICAL_LOCAL_RENAME
BASELINE_DOCX_SHA256 = 1dd91002c99757f1aa3ed876efba118c5286be60c7d625739913b2b871cb1781
BASELINE_COMMENTS = 40
BASELINE_TRACKED_CHANGES = 0
```

Antes de editar una sola oración, calcula SHA-256. Si no coincide exactamente, detente con `INTRO_B01_V01_DOCX_ACCESS_REQUIRED_OR_HASH_MISMATCH`.

No vuelvas al B06 para reconstruir el DOCX V02. El baseline operativo para estas correcciones es el candidato Introduction V01 exacto.

## 4. Contenido científico que debe preservarse

Preserva sin cambios sustantivos:

- la apertura concreta del problema;
- los cuatro antecedentes citados y sus claims;
- la limitación basada en separación operacional/evaluativa;
- la arquitectura de alto nivel: historical retrieval → ranking/fixed Top-3 → normative retrieval sin reranking → local LLM explanation-only;
- la frontera documentary evidence ≠ legal correctness;
- las tres contribuciones en su contenido científico;
- la frontera configurability/re-instantiation ≠ empirical generalization;
- el testbed después de propuesta/contribuciones;
- RQ1–RQ4 exactamente en su objeto;
- el roadmap;
- `FINAL_GAP = NOT_DEFINED`;
- `NOVELTY = NOT_DECLARED`.

No agregues ni elimines citas. Las cuatro citas nuevas de V01 ya pasaron auditoría independiente.

## 5. B01-C01 — Concretar el párrafo de contribuciones

La V01 comprime las tres contribuciones en una oración excesivamente larga y abstracta que comienza con:

`It formalizes an architectural-methodological separation...`

Reformula únicamente ese párrafo para cumplir SPCCR.

### Requisitos semánticos obligatorios

La redacción debe conservar tres contribuciones y hacer visible qué componente hace qué:

1. **Arquitectura/procedimiento:** la recuperación histórica genera y ordena candidatos y fija el Top-3; la recuperación normativa solo asocia evidencia después de fijado el ranking; el LLM local solo genera la explicación del Top-3 fijo y no modifica candidatos ni orden.
2. **Evaluación:** candidate retrieval, documentary association y controlled explanation se evalúan como salidas distintas; cuando la estructura de una DAM introduce dependencia, la evaluación conserva el agrupamiento por DAM.
3. **Reproducibilidad/reinstanciación:** el procedimiento documenta interfaces y recursos que permiten sustituir el banco histórico etiquetado, el espacio objetivo de clases y un corpus documental compatible, sin inferir transferencia de desempeño.

### Requisitos de prosa

- no comprimir las tres contribuciones en una sola oración larga;
- preferir sujeto/componente + verbo + objeto + restricción;
- eliminar acumulaciones como `architectural-methodological separation`, `non-overlapping roles` y `explicit modification limits` cuando puedan sustituirse por acciones concretas;
- no introducir `novel`, `first`, `unique`, `unprecedented` ni equivalentes;
- el espejo español debe conservar la misma carga epistémica y ser natural, no literal rígido.

## 6. B01-C02 — Terminología del testbed

En el párrafo del contexto empírico, sustituye la construcción ambigua:

`NANDINA/HS subheading recommendation`

por la terminología estable:

`NANDINA subheading recommendation`

Mantén la delimitación `Class/Chapter 87` conforme al ground truth documental si permanece en esa oración.

En español conserva `recomendación de subpartidas NANDINA`.

No cambies ninguna otra propiedad del testbed.

## 7. B01-C03 — QA SPCCR obligatorio

Después de aplicar las dos correcciones de prosa, ejecuta y registra explícitamente:

```text
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

Si cualquiera falla, revisa antes de entregar.

## 8. Controles que deben permanecer PASS

```text
PRIMARY_SOURCE_SUPPORT = PASS / 4_OF_4 / NO_CLAIM_CHANGE
INTRODUCTION_NEW_ENGLISH_CITATIONS = 4
INTRODUCTION_CITATION_COMMENT_COVERAGE = 4_OF_4
TOTAL_CITATION_COMMENT_COUNT = 40
INHERITED_COMMENTS = 40_OF_40 / PRESERVE_EXACTLY
RELATED_WORK_2_1_TO_2_6 = PRESERVE_EXACTLY
RQ1_TO_RQ4 = PRESENT / SEMANTICALLY_ALIGNED
STUDY_RESULTS_IN_INTRODUCTION = ABSENT
NOVELTY_SOTA_UNIVERSAL_ABSENCE_CLAIMS = ABSENT
UNEVALUATED_EMPIRICAL_GENERALIZATION = ABSENT
LEGAL_CORRECTNESS_OVERCLAIM = ABSENT
DECISION_SUPPORT_ARCHITECTURE = NOT_AUTHORIZED / NOT_DRAFTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Las correcciones no afectan frases citadas. Por tanto, los 40 comentarios del DOCX deben preservarse exactamente; no recrees ni añadas comentarios.

## 9. QA DOCX

Verifica al final:

- SHA-256 del baseline V01 exacto antes de editar;
- 40/40 comentarios preservados;
- cero tracked changes;
- integridad OOXML;
- Related Work 2.1–2.6 sin cambios;
- secciones posteriores sin cambios;
- Introduction como único contenido científico editado;
- equivalencia EN–ES;
- render completo e inspección visual sin clipping, overlap, truncation o content loss;
- SHA-256 final del DOCX V02.

Entrega efectivamente al autor el DOCX V02 antes de declarar `AUTHOR_HANDOFF = COMPLETED`.

## 10. Artefactos de salida

Genera exactamente:

1. `article/sections/introduction/Introduction_B01_V02.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md`
3. `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx` — local, entregado al autor; no subir a GitHub
4. `article/responses/3_INTRODUCTION_B01_RESPONSE_V04.md`

Los dos Markdown científicos deben contener Part I English y Part II Spanish semantic-control mirror según el master acumulativo vigente.

No promuevas `ARTICLE_MASTER_V007`.

## 11. Commit obligatorio

Después del QA, crea **un solo commit semántico** que añada exclusivamente:

- `article/sections/introduction/Introduction_B01_V02.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.md`;
- `article/responses/3_INTRODUCTION_B01_RESPONSE_V04.md`.

No subas el DOCX.

No modifiques:

- `ARTICLE_STATUS.md`;
- `ARTICLE_WRITING_PLAN.md`;
- governance;
- `ARTICLE_MASTER_V006.md`;
- Related Work;
- Architecture ni secciones posteriores.

Si el conector vuelve a impedir transferir el master Markdown completo, detente sin crear placeholders, archivos parciales, commits auxiliares ni force-push y registra el bloqueo en V04. No declares entrega completa.

## 12. Respuesta final de chat

Después del commit exitoso, responde únicamente:

`RESPONSE_VERSIONED_IN_GITHUB = article/responses/3_INTRODUCTION_B01_RESPONSE_V04.md@<commit_sha>`

Después detente. La IA Gestora realizará una nueva auditoría. La aprobación del autor y la apertura de Decision-support architecture continúan prohibidas hasta ese dictamen.
