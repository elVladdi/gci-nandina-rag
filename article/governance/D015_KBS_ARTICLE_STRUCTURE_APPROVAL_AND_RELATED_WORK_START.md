# D-015 — Aprobación de estructura KBS y apertura de Related Work / KBS Structure Approval and Related Work Start

## Español

```text
DECISION_ID = D-015
DECISION_DATE = 2026-09-19
AUTHOR_DECISION = RECEIVED
TARGET_JOURNAL = Knowledge-Based Systems
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_ID = KBS_ARTICLE_WORKING_STRUCTURE_V01
STRUCTURE_MD_PATH = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_MD_BLOB_SHA_AT_APPROVAL = a2deb23a7ef0281c63d5f1378e0628e85d671fd3
STRUCTURE_WORD_FILENAME = KBS_ARTICLE_WORKING_STRUCTURE_V01.docx
STRUCTURE_WORD_SHA256 = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
NEXT_DRAFTING_PHASE = RELATED_WORK
RELATED_WORK_B01 = AUTHORIZED
SCIENTIFIC_SCOPE = UNCHANGED
CLAIM_EVIDENCE_RULES = UNCHANGED
EXPERIMENTAL_GOVERNANCE = UNCHANGED
```

### Decisión

El autor aprueba expresamente la estructura completa contenida en `KBS_ARTICLE_WORKING_STRUCTURE_V01` y autoriza que se utilice como base acumulativa para la construcción del manuscrito. Desde esta decisión, la estructura deja de ser `WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN` y pasa a `AUTHOR_APPROVED / FROZEN_FOR_DRAFTING`.

La aprobación se refiere a la **estructura, orden narrativo, títulos/subtítulos y función asignada a cada sección**. No aprueba ningún texto científico previo de `Methods B01 V05`, que permanece en `HOLD / NOT APPROVED`, ni autoriza `V06`.

### Base acumulativa obligatoria

El Word exacto aprobado es `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`, SHA-256 `0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5`.

A partir de ahora:

1. cada bloque se redactará **dentro de esta estructura acumulativa**;
2. no se generarán Words independientes por sección;
3. la IA de Redacción deberá partir del Word acumulativo aprobado o, después de la primera integración, del último master acumulativo aprobado;
4. si el Word base exacto no está accesible en la sesión de la IA de Redacción, deberá detenerse y declarar `BASELINE_DOCX_ACCESS_REQUIRED`; no se autoriza reconstrucción silenciosa;
5. las notas editoriales solo se eliminan en la sección que se completa;
6. Part I en inglés y Part II en español deben conservar equivalencia semántica.

### Orden de redacción activado

Queda activado el orden definido por D-014 y `ARTICLE_WRITING_PLAN`:

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results autorizados → figures/tables → integración experimental pendiente → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

### Primer bloque autorizado

Se autoriza exclusivamente:

`Related Work B01 — Section 2.1 Automated tariff classification and candidate retrieval`

La autorización **no** incluye 2.2–2.6, Introduction, Decision-support architecture, Experimental design, Results ni ninguna corrección de Methods B01 V05.

El bloque 2.1 deberá sintetizar literatura por familias de tareas/enfoques y no por secuencia de autores. Debe distinguir clasificación directa, clasificación jerárquica, recuperación/ranking de códigos o precedentes y tareas de validación/corrección cuando resulten pertinentes. La subsección debe terminar con una síntesis que prepare 2.2, sin declarar novelty universal ni introducir prematuramente el testbed específico del presente estudio.

Los 34 artículos KBS continúan siendo **evidencia editorial**, no fuentes científicas automáticas. Las citas científicas deben provenir del corpus bibliográfico gobernado y cumplir re-recuperación full-text y comentarios de auditoría conforme a MWDP_V1.0.

### Bootstrap del master acumulativo

Como todavía no existe un master canónico aprobado bajo la nueva estructura, `Related Work B01 V01` utilizará el Word estructural aprobado como baseline y producirá un **master candidato acumulativo**. Solo después de aprobación expresa del autor del bloque podrá efectuarse la primera integración canónica bajo MWDP.

---

## English

```text
DECISION_ID = D-015
DECISION_DATE = 2026-09-19
AUTHOR_DECISION = RECEIVED
TARGET_JOURNAL = Knowledge-Based Systems
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_ID = KBS_ARTICLE_WORKING_STRUCTURE_V01
STRUCTURE_MD_PATH = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_MD_BLOB_SHA_AT_APPROVAL = a2deb23a7ef0281c63d5f1378e0628e85d671fd3
STRUCTURE_WORD_FILENAME = KBS_ARTICLE_WORKING_STRUCTURE_V01.docx
STRUCTURE_WORD_SHA256 = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
NEXT_DRAFTING_PHASE = RELATED_WORK
RELATED_WORK_B01 = AUTHORIZED
SCIENTIFIC_SCOPE = UNCHANGED
CLAIM_EVIDENCE_RULES = UNCHANGED
EXPERIMENTAL_GOVERNANCE = UNCHANGED
```

The author explicitly approves the complete `KBS_ARTICLE_WORKING_STRUCTURE_V01` as the cumulative manuscript structure. The approval covers section order, headings/subheadings, narrative placement, and section functions; it does not approve the rejected/held Methods B01 V05 prose.

The exact approved Word baseline is `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`, SHA-256 `0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5`. Every subsequent drafting block must be inserted into the cumulative baseline or the latest approved cumulative master. Silent reconstruction is prohibited; lack of baseline access requires `BASELINE_DOCX_ACCESS_REQUIRED`.

The first and only newly authorized drafting block is `Related Work B01 — Section 2.1 Automated tariff classification and candidate retrieval`. Sections 2.2–2.6 and all later manuscript sections remain unauthorized until the B01 gate is completed.