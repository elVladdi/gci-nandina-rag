# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**.
- `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- `0C — Gap, contribución y Research Questions`: **`CLOSED / APPROVED`**.
- `0C`: **`APPROVED / FROZEN`**.
- `0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL`.
- `RQ1 = RETAINED`.
- `RQ2 = RETAINED`.
- `RQ3 = RETAINED_WITH_HE4_LIMITATIONS`.
- `RQ4 = RETAINED_CONDITIONAL_ON_GROUP3`.
- `0D-1 — Arquitectura editorial y journal fit`: **`INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`**.
- `0D_V02_INTERNAL_REVIEW = PASS`.
- `0D_M01 = CLOSED`.
- `0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío`: **`READY_FOR_DRAFTING`**.
- `0D2_ENTRY_GATE = PASS / OPENED`.
- `PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems`.
- `ALTERNATIVE_TARGET_1 = Expert Systems with Applications`.
- `ALTERNATIVE_TARGET_2 = Information Processing & Management`.
- `TARGET_JOURNAL = PENDING_0D2_AND_AUTHOR_APPROVAL`.
- `PHASE_0_GATE_RECOMMENDATION = PASS_WITH_CORRECTIONS` de 0D-1, todavía no cerrado.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW`.
- `FREEZE_0D = NOT_AUTHORIZED`.
- `PHASE_1 = BLOCKED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED_FOR_GAP`; búsqueda web autorizada en 0D-2 únicamente para requisitos editoriales vigentes, plantilla/formato oficial, políticas y estrategia de fit/cascada de revistas.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_0D2_ENTRY`.

### Gobernanza vigente

Gobiernan, entre otros:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- freezes `0B-01` a `0B-06`;
- `article/reviews/0B_PHASE_CLOSURE.md`;
- `article/reviews/0C_AUTHOR_APPROVAL.md`;
- `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
- `article/reviews/0C_PHASE_CLOSURE.md`;
- `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`;
- `article/reviews/0D_V02_INTERNAL_REVIEW.md`;
- `article/reviews/0D2_ENTRY_GATE.md`;
- `article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/STYLE_GUIDE.md`.

La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados editoriales, gates, claims y auditoría editorial. La IA de Redacción ejecuta prompts cerrados versionados y, una vez abierta Fase 1, será responsable de generar y actualizar los artefactos del manuscrito `.md` y `.docx` conforme al protocolo que se cierre en 0D-2.

### Estado experimental relevante

El snapshot experimental consumido por 0D permanece en solo lectura:

```text
SRC-03 branch = docs/plan-maestro-temporal-2026-08-31
SRC-03 HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
SRC-03 blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
GROUP3 = NEXT / NOT_STARTED
```

Se mantiene:

```text
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
```

0D-2 no puede resolver estas dependencias experimentales por inferencia.

### Posicionamiento científico preservado

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Se mantienen las fronteras:

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`;
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`;
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`;
- `JOURNAL_FIT ≠ NOVELTY_PROOF`;
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`;
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`;
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`;
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.

### Motivo de apertura de 0D-2

La aprobación del autor y el freeze de 0D se aplazan porque, antes de iniciar Methods, deben cerrarse requisitos capaces de provocar reescritura:

1. tipo de artículo exacto para KBS;
2. plantilla/formato oficial de submission;
3. estructura/secciones compatibles;
4. límites y requisitos formales relevantes desde el primer borrador;
5. estilo bibliográfico final de KBS;
6. política maestra de escritura científica;
7. protocolo anti-error, anti-alucinación y anti-overclaiming;
8. contrato operativo claim–evidence;
9. workflow acumulativo `.md` + `.docx`;
10. Word provisional con citas/referencias APA 7 y gestión final del autor mediante Mendeley;
11. comentario obligatorio anclado a cada cita del Word con fuente/revista, autores, afirmación original, traducción al español y justificación de respaldo;
12. estrategia editorial y cascada A/B/C para minimizar reescritura tras eventual rechazo.

### Autoridad sobre los entregables de manuscrito

Regla fijada por el autor para formalización en 0D-2:

- la **IA de Redacción** generará y actualizará el `.md` de cada bloque, el `.md` maestro acumulativo y el `.docx` maestro acumulativo;
- cada entrega será candidata hasta superar las auditorías aplicables y aprobación del autor;
- el Word se actualizará sobre la última versión aprobada y no se reconstruirá desde cero, salvo creación inicial a partir del formato/plantilla oficialmente adoptado;
- la IA Gestora, la IA Experimental y el autor auditan conforme a sus competencias;
- el autor gestionará Mendeley al final;
- durante la redacción, las citas/referencias provisionales del Word se expresarán en APA 7;
- cada cita en Word llevará un comentario específico de auditoría afirmación–cita–fuente.

### Gate vigente

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2_ENTRY_GATE = PASS / OPENED
0D2 = READY_FOR_DRAFTING
NEXT_ACTOR = IA_DE_REDACCION
PROMPT = article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY.md
EXPECTED_RESPONSE = article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

---

## English

### Overall state

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: `CLOSED / APPROVED`.
- Phase 0B: `CLOSED / APPROVED`; 0B-01 through 0B-06 are `APPROVED / FROZEN`.
- Phase 0C: `CLOSED / APPROVED`; 0C is `APPROVED / FROZEN`.
- `0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN`.
- `0D_V02_INTERNAL_REVIEW = PASS` and `0D_M01 = CLOSED`.
- `0D2_ENTRY_GATE = PASS / OPENED`.
- `0D2 = READY_FOR_DRAFTING`.
- `PRIMARY_TARGET_RECOMMENDATION = Knowledge-Based Systems`.
- `ALTERNATIVE_TARGET_1 = Expert Systems with Applications`.
- `ALTERNATIVE_TARGET_2 = Information Processing & Management`.
- Final target selection is deferred until 0D-2 review and author approval.
- `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`.
- `AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW`.
- `FREEZE_0D = NOT_AUTHORIZED`.
- `PHASE_1 = BLOCKED` and `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.

0D-2 was opened because journal-specific requirements, manuscript template/format, final reference style, definitive section architecture, writing and claim-control rules, cumulative Markdown/Word workflow, citation-level Word comments, and the A/B/C journal cascade must be closed before drafting to minimize avoidable rewriting.

The Drafting AI will own generation and updating of manuscript `.md` and `.docx` artifacts after Phase 1 opens. The Managing AI, Experimental AI, and author will audit within their respective scopes. During drafting, the Word version will use provisional APA-7 citations/references; final Mendeley management will be performed by the author. Every Word citation will carry a citation-anchored audit comment with source/journal, authors, exact sufficient original-language supporting statement, Spanish translation, and support justification.

All frozen scientific boundaries remain unchanged, including the prohibition on using EXP-11B before C10/C11 reconciliation and on closing RQ4/HE2/HE5 before Group 3.

### Current gate

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D1 = INTERNAL_REVIEW_COMPLETE / NOT_FROZEN
0D2_ENTRY_GATE = PASS / OPENED
0D2 = READY_FOR_DRAFTING
NEXT_ACTOR = WRITING_AI
PROMPT = article/prompts/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY.md
EXPECTED_RESPONSE = article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = DEFERRED_UNTIL_0D2_REVIEW
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```
