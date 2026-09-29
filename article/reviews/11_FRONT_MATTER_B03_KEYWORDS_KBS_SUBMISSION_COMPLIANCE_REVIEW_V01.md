# Post-approval compliance review — Front matter B03 / Keywords against current KBS author guidance

## Español

```text
REVIEW_TYPE = TARGET_JOURNAL_SUBMISSION_COMPLIANCE_AUDIT
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B03_KEYWORDS
TARGET_JOURNAL = Knowledge-Based Systems
AUDIT_DATE = 2026-09-29

CANONICAL_MASTER = ARTICLE_MASTER_V034
CANONICAL_MASTER_GIT_BLOB = 0d24b1e46ed3d6a189c5ffdcfaac97e9670fa684

CURRENT_KEYWORDS_VERSION = B03_V01
CURRENT_KEYWORD_COUNT = 7
AUTHOR_APPROVAL = YES
CANONICAL_PROMOTION = YES

VERDICT = REVISE_KEYWORDS_TO_V02
REASON = CURRENT_ELSEVIER_AUTHOR_GUIDANCE_MAXIMUM_6_KEYWORDS
```

### 1. Hallazgo de cumplimiento

Durante la auditoría de transición desde Front Matter hacia End Matter se revalidaron las instrucciones editoriales actuales de Elsevier aplicables al paquete de sumisión.

La guía actual de autor de Elsevier usada por el flujo de *Your Paper Your Way* establece para Keywords:

- máximo de 6 keywords inmediatamente después del Abstract;
- American spelling;
- evitar términos excesivamente generales;
- evitar plurales cuando sea posible;
- evitar múltiples conceptos en una misma keyword, ejemplificando construcciones con `and` / `of`.

Fuentes verificadas el 2026-09-29:

- https://www-prod.elsevier.com/subject/next/guide-for-authors
- https://www.elsevier.com/subject/next/guide-for-authors
- página oficial de Knowledge-Based Systems en Elsevier/ScienceDirect, que remite al Guide for Authors del journal.

La lista B03 V01 aprobada contiene siete keywords:

```text
1. Knowledge-based decision support
2. Tariff classification
3. Harmonized System
4. Information retrieval
5. Documentary evidence
6. Large language models
7. Provenance and traceability
```

Por tanto:

```text
B03_V01_SCIENTIFIC_FIT = PASS
B03_V01_AUTHOR_APPROVAL = VALID
B03_V01_CANONICAL_PROMOTION = VALID
B03_V01_SUBMISSION_KEYWORD_COUNT_COMPLIANCE = FAIL
```

### 2. Segunda observación de estilo de keyword

`Provenance and traceability` combina dos conceptos mediante `and`.

Aunque ambos están sustentados por el manuscrito, la forma no es óptima bajo la guía vigente. `Provenance` conserva el concepto más directamente indexable y ya cubre la propiedad transversal de lineage/origin sin convertirla en una afirmación de correctness.

`Large language models` se normaliza a singular:

`Large language model`

para respetar la preferencia editorial contra plurales innecesarios.

### 3. Selección V02

Se fija una lista de seis keywords:

```text
KEYWORDS_EN_V02 =
Knowledge-based decision support; Tariff classification; Harmonized System; Information retrieval; Large language model; Provenance

KEYWORDS_ES_V02 =
Apoyo a la decisión basado en conocimiento; Clasificación arancelaria; Sistema Armonizado; Recuperación de información; Modelo de lenguaje grande; Procedencia
```

### 4. Criterio de reducción

Se elimina `Documentary evidence` de la lista de keywords, no del manuscrito ni del Title.

Razones:

1. la guía obliga a reducir de siete a seis;
2. `Documentary Evidence` ya está explicitado literalmente en el Title aprobado;
3. la guía editorial general de Elsevier recomienda evitar redundancia innecesaria con términos ya presentes en el Title;
4. su función científica sigue visible en Title, Abstract, Architecture, Results, Discussion y Conclusion;
5. las seis keywords restantes aportan una combinación más eficiente de identidad científica, dominio, taxonomía aduanera, familia de recuperación, familia generativa y provenance.

No se modifica el alcance científico.

### 5. Estado de V034

V034 permanece como master canónico porque fue promovido byte-exactamente después de aprobación autoral.

Sin embargo, el cierre de Front Matter declarado en D-183 queda reabierto únicamente para Keywords debido al hallazgo de compliance posterior.

```text
V034_CANONICAL_STATUS = RETAINED
D183_PROMOTION_VERIFICATION = RETAINED_PASS
D183_FRONT_MATTER_FINALIZATION = SUPERSEDED_FOR_KEYWORDS_COMPLIANCE_ONLY

TITLE = REMAINS_CLOSED / APPROVED / FROZEN / INTEGRATED
ABSTRACT = REMAINS_CLOSED / APPROVED / FROZEN / INTEGRATED
KEYWORDS = REOPENED / V02_REQUIRED
END_MATTER = HOLD
```

### 6. Veredicto

```text
KEYWORDS_B03_V02_REQUIRED = YES

TARGET_KEYWORDS_EN_V02 =
Knowledge-based decision support; Tariff classification; Harmonized System; Information retrieval; Large language model; Provenance

TARGET_KEYWORDS_ES_V02 =
Apoyo a la decisión basado en conocimiento; Clasificación arancelaria; Sistema Armonizado; Recuperación de información; Modelo de lenguaje grande; Procedencia

CANONICAL_MASTER = ARTICLE_MASTER_V034
END_MATTER_FINALIZATION = NOT_AUTHORIZED_UNTIL_KEYWORDS_V02_APPROVED_AND_INTEGRATED
```

---

## English

A post-approval submission-compliance audit found that the current Elsevier author guidance limits the keyword list to a maximum of six terms and advises avoiding unnecessary plurals and multi-concept keywords.

The author-approved B03 V01 list remains scientifically valid and its byte-exact V034 promotion remains valid as the current canonical master. However, its seven-keyword list is not submission-compliant.

B03 V02 is therefore required. The new fixed list contains six terms, changes `Large language models` to singular, reduces `Provenance and traceability` to `Provenance`, and removes `Documentary evidence` because that concept remains explicitly represented in the approved title and throughout the manuscript.

Title and Abstract remain frozen. End Matter stays on hold until the corrected Keywords V02 is approved and integrated.
