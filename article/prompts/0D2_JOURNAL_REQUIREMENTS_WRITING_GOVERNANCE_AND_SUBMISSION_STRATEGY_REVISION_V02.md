# 0D-2 — Revisión V02 / 0D-2 Revision V02

## Español

Actúa exclusivamente como **IA de Redacción y análisis científico-editorial** para corregir la respuesta 0D-2 V01.

No redactes ninguna sección del manuscrito. No abras Fase 1. No modifiques Plan Maestro, claims experimentales ni literatura congelada.

### Base obligatoria

Trabaja sobre:

- `article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md`;
- `article/reviews/0D2_INTERNAL_REVIEW.md`;
- `article/reviews/0D2_AUTHOR_DECISION_DOCX_LANGUAGE_LAYOUT.md`;
- el prompt original `article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY.md`;
- artefactos gobernantes citados por el prompt original.

Preserva todo lo aprobado en V01 y corrige **únicamente** 0D2-M01 a 0D2-M04.

### 0D2-M01 — Requisitos KBS aún no suficientemente cerrados

Debes distinguir expresamente:

```text
KBS_REQUIREMENTS_VERIFIED_FROM_PRIMARY
KBS_REQUIREMENTS_UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT
KBS_REQUIREMENTS_DEFERABLE_WITHOUT_REWRITE_RISK
```

Vuelve a intentar verificación web vigente y prioriza fuentes oficiales/primarias. No promociones reproducciones de terceros a autoridad normativa.

Si un requisito KBS capaz de afectar longitud, formato inicial o arquitectura permanece no verificado, debes hacer una de dos cosas:

1. fijar una política interna conservadora que elimine de forma explícita el riesgo de reescritura científica; o
2. clasificarlo como `UNVERIFIED_BLOCKING` y recomendar `PRE_DRAFTING_GATE_RECOMMENDATION = BLOCKED`.

En particular:

- justifica explícitamente si un Word neutral puede migrarse posteriormente al formato KBS sin reescritura científica;
- establece una disciplina de extensión conservadora desde Fase 1 para minimizar riesgo de compresión tardía;
- no atribuyas a KBS un límite de páginas ni modelo de revisión que no hayas confirmado en fuente primaria accesible.

### 0D2-M02 — Layout lingüístico del Word resuelto por decisión del autor

La decisión del autor ya está formalizada en:

`article/reviews/0D2_AUTHOR_DECISION_DOCX_LANGUAGE_LAYOUT.md`

Debes aplicar obligatoriamente:

```text
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
AUTHOR_DECISION = APPROVED
```

Por tanto:

- el `.docx` maestro interno será bilingüe;
- la parte inglesa será el manuscrito científico destinado a publicación;
- la parte española será el espejo de control semántico para facilitar la revisión del autor;
- ambas partes deberán conservar equivalencia semántica;
- los comentarios de auditoría de citas se anclarán a las citas de la parte inglesa;
- la parte española interna será retirada únicamente mediante un gate editorial explícito al preparar el paquete final de submission, sin alterar el contenido científico aprobado.

No presentes esta cuestión como pendiente ni vuelvas a ofrecer opciones A/B salvo que exista una nueva instrucción expresa del autor.

### 0D2-M03 — Separar APA 7 del Word respecto de Markdown

Fija explícitamente:

```text
WORD = PROVISIONAL_APA7_PRESENTATION_LAYER
MARKDOWN = SOURCE_TRACEABILITY_LAYER_NOT_APA7_FORMATTING_AUTHORITY
```

Markdown puede usar identificadores estables de fuente/cita y placeholders legibles necesarios para mantener el significado, pero no debe convertirse en una segunda autoridad de formato APA 7.

La conversión final mediante Mendeley sigue siendo responsabilidad del autor y se realiza solo en Word al final.

### 0D2-M04 — Separar revisionado e integración del master

Adopta una convención no ambigua con contadores separados. Debe distinguir como mínimo:

```text
BLOCK_REVISION
MASTER_INTEGRATION
MASTER_CANDIDATE_REVISION
```

Ejemplo admisible:

```text
P01_METHODS_B01_V01.md
P01_METHODS_B01_V02.md
ARTICLE_MASTER_V001_CANDIDATE_R01.md/.docx
ARTICLE_MASTER_V001_CANDIDATE_R02.md/.docx
ARTICLE_MASTER_APPROVED_V001.md/.docx
ARTICLE_MASTER_V002_CANDIDATE_R01.md/.docx
```

Solo la integración aprobada avanza `MASTER_V00N`.

### Restricciones preservadas

No cambies:

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
```

No reabras 0B ni declares novelty.

### Artefacto único

Crea únicamente:

`article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V02.md`

Debe ser bilingüe ES/EN con equivalencia semántica. No modifiques ningún otro archivo.

### Cierre obligatorio

Finaliza con:

```text
0D2_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
0D2_M01 = ADDRESSED
0D2_M02 = ADDRESSED_BY_AUTHOR_DECISION
0D2_M03 = ADDRESSED
0D2_M04 = ADDRESSED
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
KBS_TEMPLATE_STATUS = <valor>
KBS_ARTICLE_TYPE_STATUS = <valor>
KBS_REFERENCE_STYLE_STATUS = <valor>
ARTICLE_ARCHITECTURE_STATUS = <valor>
WRITING_POLICY_STATUS = <valor>
CLAIM_EVIDENCE_PROTOCOL_STATUS = <valor>
MD_DOCX_WORKFLOW_STATUS = <valor>
WORD_CITATION_COMMENT_PROTOCOL_STATUS = <valor>
DOCX_LANGUAGE_LAYOUT = DOCX_BILINGUAL_INTERNAL_MASTER
JOURNAL_CASCADE_STATUS = <valor>
PRE_DRAFTING_GATE_RECOMMENDATION = PASS | PASS_WITH_CORRECTIONS | BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
PHASE_1 = NOT_OPENED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

Commit sugerido:

`article: correct 0D2 pre-drafting governance response v02`

En el chat informa únicamente commit SHA, ruta y estado `COMPLETED_PENDING_EDITORIAL_REVIEW`.

---

## English

Act exclusively as the Writing/scientific-editorial analysis AI to correct 0D-2 V01. Do not draft manuscript sections or open Phase 1.

Use V01, `article/reviews/0D2_INTERNAL_REVIEW.md`, `article/reviews/0D2_AUTHOR_DECISION_DOCX_LANGUAGE_LAYOUT.md`, the original 0D-2 prompt, and its governing artifacts. Preserve all accepted V01 content and correct only 0D2-M01 through 0D2-M04.

For M01, distinguish primary-verified requirements, unverified but potentially rewrite-relevant requirements, and deferable requirements. Reattempt current official-source verification. Any unverified requirement capable of affecting length, initial format, or architecture must either be neutralized by an explicit conservative internal policy or become `UNVERIFIED_BLOCKING` with a `BLOCKED` pre-drafting recommendation. Do not promote third-party reproductions to official authority.

For M02, the author has expressly selected `DOCX_BILINGUAL_INTERNAL_MASTER`. Apply this decision as closed: English is the publication manuscript, Spanish is the internal semantic-control mirror, both remain semantically equivalent, citation-audit comments are anchored to the English part, and the Spanish internal mirror is removed only through an explicit final-submission gate without changing approved scientific content.

For M03, establish Word as the provisional APA-7 presentation layer and Markdown as the stable source-traceability layer rather than a second APA-7 formatting authority.

For M04, separate block revision, master integration, and candidate-master revision counters. Only an approved integration advances the canonical master version number.

Create only:

`article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V02.md`

Preserve all frozen scientific states, targets, RQs, Group-3 and EXP-11B constraints, final-gap and novelty states. Finish with the required status block. Modify no other file.
