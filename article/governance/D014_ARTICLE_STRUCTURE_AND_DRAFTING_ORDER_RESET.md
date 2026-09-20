# D-014 — Reset de estructura del artículo y orden de redacción / Article Structure and Drafting-Order Reset

## Español

```text
DECISION_ID = D-014
DECISION_DATE = 2026-09-19
AUTHOR_DECISION = RECEIVED
TARGET_JOURNAL = Knowledge-Based Systems
EDITORIAL_BASIS = KBS_EWG_34_V01
V05_AUTHOR_APPROVAL = NOT_GRANTED
V05_STATUS = HOLD / NOT_APPROVED
V06 = NOT_AUTHORIZED
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
LEGACY_0D_SECTION_ARCHITECTURE = SUPERSEDED_BY_CONTROLLED_AMENDMENT_FOR_STRUCTURE_ONLY
SCIENTIFIC_SCOPE = UNCHANGED
CLAIM_EVIDENCE_RULES = UNCHANGED
EXPERIMENTAL_GOVERNANCE = UNCHANGED
NEW_STRUCTURE_STATUS = WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN
```

### Decisión

El autor no aprueba todavía `Methods B01 V05`. Las razones editoriales registradas son: falta de fluidez, persistencia de abstracciones, apertura mediante una formulación que sugiere prematuramente que se ha desarrollado “the method”, y aparición demasiado temprana del alcance experimental específico —incluidos NANDINA, Chapter/Class 87 y el corpus utilizado— antes de que el lector comprenda la arquitectura general y su posicionamiento científico.

A la luz de la guía empírica KBS-34 ya aprobada, se autoriza un **reset controlado de la estructura editorial y del orden de redacción**. El orden previo `Methods → Related Work → ... → Introduction` queda supersedido. Este cambio no modifica el diseño experimental, los claims autorizados, las fronteras epistemológicas, las RQ vigentes ni la gobernanza del Plan Maestro experimental.

### Principio estructural nuevo

El artículo debe separar explícitamente tres niveles narrativos:

1. **problema y posicionamiento científico**;
2. **arquitectura general de apoyo a decisiones**;
3. **instanciación y evaluación experimental específica**.

La arquitectura general debe explicarse antes de introducir el testbed experimental concreto. NANDINA, el alcance de Chapter/Class 87, los datasets versionados y el corpus documental concreto pertenecen principalmente a la sección de diseño experimental, no a la apertura de la arquitectura.

### Arquitectura de trabajo autorizada

La nueva estructura de trabajo es:

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

`Limitations` se integra provisionalmente como subsección final de `Discussion`, salvo que la redacción definitiva justifique elevarla a sección principal.

La estructura detallada se versiona en:

`article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`

El Word editable entregado al autor usa la misma estructura y funcionará como base acumulativa para las versiones posteriores del manuscrito. La estructura exacta permanece `WORKING / AUTHOR_EDITABLE`; no queda `FROZEN` hasta que el autor termine de revisarla y la apruebe expresamente.

### Nuevo orden de redacción

Una vez aprobada la estructura de trabajo, el orden operativo será:

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results disponibles/autorizados → figures/tables → integración de resultados pendientes → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title → adaptación final KBS`.

Este orden de redacción es una decisión de gobernanza del proyecto; no se presenta como una inferencia acerca del orden en que los autores de los 34 artículos KBS redactaron sus manuscritos.

### Gate

Hasta que la estructura sea aprobada por el autor:

```text
METHODS_B01_V05 = HOLD / NOT_APPROVED
METHODS_B01_V06 = NOT_AUTHORIZED
B02_LEGACY_SEQUENCE = NOT_AUTHORIZED
NEW_MANUSCRIPT_SECTION_DRAFTING = NOT_AUTHORIZED
NEXT_ACTOR = AUTHOR
NEXT_ACTION = REVIEW_AND_EDIT_WORKING_STRUCTURE_V01
```

---

## English

```text
DECISION_ID = D-014
DECISION_DATE = 2026-09-19
AUTHOR_DECISION = RECEIVED
TARGET_JOURNAL = Knowledge-Based Systems
EDITORIAL_BASIS = KBS_EWG_34_V01
V05_AUTHOR_APPROVAL = NOT_GRANTED
V05_STATUS = HOLD / NOT_APPROVED
V06 = NOT_AUTHORIZED
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
LEGACY_0D_SECTION_ARCHITECTURE = SUPERSEDED_BY_CONTROLLED_AMENDMENT_FOR_STRUCTURE_ONLY
SCIENTIFIC_SCOPE = UNCHANGED
CLAIM_EVIDENCE_RULES = UNCHANGED
EXPERIMENTAL_GOVERNANCE = UNCHANGED
NEW_STRUCTURE_STATUS = WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN
```

The author has not approved `Methods B01 V05`. The registered editorial concerns are limited fluency, remaining abstraction, an opening formulation that prematurely suggests the development of “the method,” and premature introduction of the specific experimental scope before the reader understands the general architecture and scientific positioning.

A controlled reset of the article structure and drafting order is therefore authorized under the approved KBS-34 empirical writing guide. The former `Methods-first` drafting sequence is superseded. Scientific scope, authorized claims, Research Questions, experimental design, and experimental governance remain unchanged.

The new working architecture is `Introduction → Related work → Decision-support architecture → Experimental design → Results → Discussion → Conclusion → KBS end matter`. The detailed working structure is versioned in `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md` and remains author-editable until explicitly frozen.

After structure approval, the operational drafting order becomes `Related Work → provisional Introduction → Decision-support architecture → Experimental design → authorized Results → figures/tables → pending-result integration → final Results → Discussion + Limitations → Conclusion → Abstract → Title → final KBS adaptation`.
