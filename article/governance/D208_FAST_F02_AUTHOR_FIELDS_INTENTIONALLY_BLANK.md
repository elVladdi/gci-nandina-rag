# D-208 — Cierre de campos administrativos de Autor como intencionalmente en blanco

## Español

```text
DECISION = D-208
PHASE = FAST_FINALIZATION / FAST_F02
PREVIOUS_DECISION = D-207

AUTHOR_INSTRUCTION =
LEAVE_AUTHOR_AND_RELATED_ADMINISTRATIVE_FIELDS_BLANK /
DO_NOT_DELAY_CONTENT_FINALIZATION

AUTHOR_FIELDS_DEFERRAL =
article/forms/FAST_F02_AUTHOR_FIELDS_DEFERRAL_V01.md@a5423c24c3afb6a24d7748dde32ed35afb41913e
AUTHOR_FIELDS_DEFERRAL_GIT_BLOB =
df4d52166687b9e3318a9b3aafd57341aad051ae

AUTHOR_METADATA_TASK = CLOSED / INTENTIONALLY_BLANK
CORRESPONDING_AUTHOR_FIELD = BLANK
CREDIT_FIELD = BLANK
FUNDING_FIELD = BLANK
COMPETING_INTERESTS_FIELD = BLANK
ACKNOWLEDGEMENTS_FIELD = BLANK

PREVIOUSLY_SUPPLIED_AUTHOR_FACTS =
GOVERNANCE_RECORD_ONLY / DO_NOT_INSERT_IN_FAST_F02

AI_DISCLOSURE =
PRESERVE_ALREADY_APPROVED_TEXT

FAST_F02_AUTHOR_FACTS_BLOCKER = NONE
FAST_F02_WRITING_PROMPT = ELIGIBLE_FOR_PREPARATION
```

## 1. Efecto de la instrucción del Autor

El Autor ordena no retrasar más el artículo por datos administrativos o declarativos de autoría que puede completar manualmente después.

Por tanto, el gate de hechos autorales abierto por D-207 se cierra sin requerir B1–B5 como condición de ejecución.

## 2. Campos que FAST-F02 debe dejar en blanco

FAST-F02 no debe insertar ni inferir:

- author/title-page metadata que todavía no esté materializado;
- corresponding-author designation;
- CRediT;
- Funding;
- Competing interests;
- Acknowledgements.

Si las secciones de End Matter ya existen con placeholders de drafting, Writing AI debe conservar el heading y eliminar el placeholder, dejando el cuerpo vacío.

Los datos previamente suministrados por el Autor se conservan únicamente en gobernanza y no se insertan en el manuscrito durante FAST-F02.

## 3. Declaración de IA

La declaración de uso de IA generativa ya aprobada y materializada no se borra ni se deja en blanco. No forma parte del gate administrativo reabierto y debe preservarse byte-equivalente en contenido salvo cambios mecánicos de formato.

## 4. Trabajo de contenido que continúa

FAST-F02 debe continuar sin demora con:

- Data availability;
- code and reproducibility resources;
- final References;
- Supplementary Material;
- bilingual semantic equivalence;
- cross-reference and package integrity dentro del scope de FAST-F02.

## 5. Gate

```text
CURRENT_GATE = FAST_F02_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
NEXT_ACTION = VERSION_AUDIT_AND_AUTHORIZE_SINGLE_FAST_F02_PROMPT

AUTHOR_ADMINISTRATIVE_TASK = CLOSED / INTENTIONALLY_BLANK
FAST_F02_WRITING_EXECUTION = NOT_AUTHORIZED_YET
AUTHOR_APPROVAL_GATE = NOT_OPEN
FAST_F03 = NOT_AUTHORIZED
```

---

## English

D-208 closes the FAST-F02 author-administrative-data task as intentionally blank by explicit Author instruction. Previously supplied author facts remain governance-only and are not inserted into the manuscript during FAST-F02.

The already approved generative-AI declaration remains unchanged. FAST-F02 may now proceed directly to one consolidated Writing-AI prompt for content-bearing End Matter, references, and supplementary material.
