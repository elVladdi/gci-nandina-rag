# D-104 — Results B04 ground-truth synchronization and Section 5.4 boundary

## Español

```text
DECISION = D-104
PHASE = RESULTS
BLOCK = RESULTS_B04_SECTION_5_4
SECTION = 5.4 CONTROLLED EXPLANATION QUALITY
RQ = RQ3
CANONICAL_MASTER = ARTICLE_MASTER_V019
GROUND_TRUTH = SYNCHRONIZED
PROMPT_PREPARATION = ALLOWED
DRAFTING = NOT_YET_AUTHORIZED
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Baseline editorial

```text
MASTER_MD = article/manuscript/ARTICLE_MASTER_V019.md
MASTER_MD_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
MASTER_MD_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e

MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
MASTER_DOCX_SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
PAGE_COUNT = 54
```

### 2. Snapshot experimental y fuentes congeladas

B04 consume exclusivamente el siguiente corte experimental:

```text
EXPERIMENTAL_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
HE4_DIRECTORY = outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2
CASES = 50
CANDIDATE_SLOTS = 150
```

Fuentes primarias vinculantes:

```text
he4_automatic_validation_metrics_v0.2.json
GIT_BLOB = a8adfe08da2b6b0052205fdb8650d9c86e8c5b82

he4_qualitative_metrics_v0.2.json
GIT_BLOB = 843e1edd17a023f6c3d6f0b5235dd3fba86369c1

he4_qualitative_findings_v0.2.md
GIT_BLOB = 4b9dd1b3079235b2c54d5777fc788f0e98b27e32

he4_he4_joint_jk_assessment_v0.2.json
GIT_BLOB = b617b4f397d0ffb4f8882ddda06790b1c539543e

he4_top3_invariance_v0.2.json
GIT_BLOB = 8ddc1703fb267e28b4301c13602f62b494846921

he4_traceability_validation_v0.2.json
GIT_BLOB = 580214070ac4c9aac1f10e4452614bc41b39d9a0

he4_label_leakage_audit_v0.2.json
GIT_BLOB = 2d078f7742806a95ab7f4004c1c140287510e8b4

gate_j_interpretation_v0.2.json
GIT_BLOB = 652610251f09ba841e7eff7598b399b8b745eec2

gate_k_qualitative_evaluation_manifest_v0.2.json
GIT_BLOB = 28963380bdcc22932d08591a709059f6fa00263b
```

No sustituir estas fuentes por outputs históricos, prompts, literatura o inferencia propia.

### 3. Ground truth — capa automática/estructural

La evaluación automática se aplicó a 50 casos / 150 candidate slots.

Resultados válidos:

```text
TOP3_ORDER_PRESERVATION = 50/50 = 100%
CANDIDATE_SET_CLOSURE = 50/50 = 100%
MISSING_CANDIDATE_FREE = 50/50 = 100%
DUPLICATE_CANDIDATE_FREE = 50/50 = 100%
EXTERNAL_CODE_FREE = 50/50 = 100%
RANK_CONSISTENCY = 50/50 = 100%
TRACEABILITY_COMPLETENESS = 50/50 = 100%
HISTORICAL_REFERENCE_VALIDITY = 50/50 = 100%
NORMATIVE_REFERENCE_VALIDITY = 50/50 = 100%
COMPARISON_PRESENCE = 50/50 = 100%
EXPLICIT_LABEL_LEAKAGE_FREE = 50/50 = 100%
RAW_JSON_PARSE = 50/50 = 100%

SLOT_CANDIDATE_CODE_VALID = 150/150 = 100%
SLOT_HISTORICAL_REFERENCE_VALID = 150/150 = 100%
SLOT_NORMATIVE_REFERENCE_VALID = 150/150 = 100%
SLOT_RANK_CONSISTENT = 150/150 = 100%
```

Sin embargo:

```text
AUTOMATIC_VALIDATION_PASS = NOT_APPLICABLE
REASON = no pre-generation per-case PASS/FAIL rule existed in the frozen schema or historical validator
SCHEMA_COMPLIANCE = 0/50
REQUIRED_FIELDS_COMPLETENESS = 0/50
```

La tasa 0/50 de schema compliance no puede narrarse como fracaso general de las explicaciones. La microauditoría congelada clasifica el problema como `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`: el schema v0.2 exigía `advertencias_globales`, pero el prompt v0.2 no incluía ese campo en su estructura de salida. Los 50 casos fallaban únicamente por ese campo y se registraron cero otros errores de schema.

El control de advertencia normativa genérica fue satisfecho en 41/50 casos; nueve casos quedaron bajo `MISSING_GENERIC_NORMATIVE_WARNING`.

### 4. Ground truth — capa cualitativa

La capa cualitativa utilizó la regla congelada de caso auditable: total ≥12/16 y ninguna hard violation.

```text
AUDITABLE_CASES = 28/50 = 56.0%
NON_AUDITABLE_CASES = 22/50 = 44.0%
TOTAL_SCORE_MEAN = 11.72/16
TOTAL_SCORE_MEDIAN = 12/16
TOTAL_SCORE_RANGE = 6–15
HARD_VIOLATIONS = 0/50
```

Puntuaciones por dimensión (0–2):

```text
TRACEABILITY = mean 2.00 / median 2.0
VERIFIABILITY = mean 0.54 / median 1.0
HISTORICAL_NORMATIVE_SEPARATION = mean 1.04 / median 1.0
CONCLUSION_PRUDENCE = mean 1.78 / median 2.0
FIXED_TOP3_CONSISTENCY = mean 1.96 / median 2.0
GENERIC_NORMATIVE_EVIDENCE_DETECTION = mean 1.68 / median 2.0
CANDIDATE_COMPARISON = mean 1.46 / median 1.0
UTILITY_FOR_HUMAN_AUDIT = mean 1.26 / median 1.0
```

Estas cifras deben presentarse como puntuaciones bajo la rúbrica congelada, no como mediciones de corrección jurídica o validación experta humana.

### 5. Modalidad real del evaluador

El protocolo previo había preparado revisión `HUMAN/MANUAL REVIEW`, pero la ejecución cualitativa real fue:

```text
EVALUATOR_IDENTIFIER = independent_ai_reviewer_01
EVALUATOR_MODALITY = AI_EXPERT_ROLE
LLM_AS_JUDGE = TRUE
HUMAN_SCORING = FALSE
METHODOLOGICAL_DEVIATION = EVALUATOR_MODALITY_DEVIATION
GROUND_TRUTH_EXPOSED = FALSE
REFERENCE_RANK_EXPOSED = FALSE
BUCKET_EXPOSED = FALSE
EXTERNAL_EVIDENCE_USED = FALSE
WEB_USED = FALSE
RETRIEVAL_USED = FALSE
```

La etiqueta de referencia tampoco fue expuesta al LLM explicador ni utilizada para Top-3, contexto o evidencia; sí fue utilizada en el diseño de la muestra de evaluación. Esto no equivale a afirmar ausencia total de leakage en todo el estudio ni independencia estadística.

### 6. Resultado conjunto y límites

El cierre experimental registra:

```text
HE4_GLOBAL = PARTIALLY SUPPORTED
GATE_J = APPROVED WITH PROTOCOL/SPECIFICATION LIMITATION
GATE_K = APPROVED WITH EVALUATOR-MODALITY LIMITATION
```

La lectura permitida es que los 50 casos conservaron controles estructurales de Top-3 y trazabilidad, mientras 28/50 alcanzaron el criterio cualitativo de caso auditable bajo la rúbrica congelada aplicada por un evaluador AI en rol experto. Son objetos distintos y no intercambiables.

Queda prohibido inferir de estos resultados:

- corrección jurídica o normativa sustantiva;
- validación humana experta;
- fidelidad causal de la explicación respecto del ranking histórico;
- accuracy de clasificación del sistema completo;
- generalización fuera del testbed;
- una tasa binaria retrospectiva `automatic_validation_pass` por caso;
- significancia estadística o causalidad a partir de las comparaciones descriptivas.

### 7. Función narrativa de §5.4

§5.4 debe responder RQ3 mediante dos capas claramente separadas:

1. controles automáticos/estructurales de preservación, referencias y trazabilidad;
2. evaluación cualitativa de 50 casos bajo la rúbrica congelada y su modalidad real de evaluador.

Debe reportar tanto las fortalezas como las limitaciones observadas. En particular, no ocultar la baja verificabilidad media (0.54), la separación histórico/normativa media (1.04), la tasa auditable 56%, el mismatch prompt-schema ni la desviación de modalidad del evaluador.

El dictamen interno `PARTIALLY SUPPORTED` puede registrarse en gobernanza y, si se usa en el manuscrito, debe traducirse a lenguaje científico funcional en lugar de abrir con el identificador interno HE4.

### 8. Claims y gate

C13 continúa `PROHIBITED` y C14 permanece `CONDITIONAL` como claim paraguas. Antes de autorizar drafting, la matriz claim–evidencia debe registrar claims numéricos específicos de B04 como `AUTHORIZED` con los límites anteriores.

```text
RESULTS_B04_GROUND_TRUTH = SYNCHRONIZED
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = REGISTER_B04_CLAIMS / PREPARE_AND_AUDIT_B04_PROMPT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B05_PLUS = NOT_AUTHORIZED
```

---

## English

Results B04 / Section 5.4 ground truth is synchronized to the frozen HE4 artifacts at `main@db0d0ad0d8435921a7838db6720eaea86a263763`. The automatic layer preserves the fixed Top-3, rank, traceability, and valid references for all 50 cases, but no retrospective per-case automatic pass rate is permitted. Frozen schema compliance is 0/50 because of a documented prompt–schema mismatch involving `advertencias_globales`, not because of 50 independent substantive explanation failures. The qualitative layer marks 28/50 cases auditable under the frozen ≥12/16/no-hard-violation rule; mean total is 11.72, median 12, range 6–15, and hard violations are 0. Qualitative scoring was performed by an independent AI reviewer in expert role, not by human scorers. These results support bounded claims about structure, traceability, rubric conformity, and audit-oriented utility only; they do not establish legal correctness, human expert validation, overall classification accuracy, or empirical generalization.