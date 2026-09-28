# D-099 — Results B03 ground-truth synchronization and Section 5.3 boundary

## Español

```text
DECISION = D-099
BLOCK = RESULTS_B03_SECTION_5_3
SECTION = 5.3 DOCUMENTARY EVIDENCE RETRIEVAL
ROLE = IA_GESTORA
CANONICAL_MASTER = ARTICLE_MASTER_V018
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
GROUND_TRUTH_SYNC = PASS
DRAFTING_AUTHORIZATION = NOT_YET_GRANTED_BY_THIS_DECISION
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Función científica del bloque

Results B03 / §5.3 debe responder exclusivamente a RQ2: **en qué medida puede asociarse evidencia normativa/documental identificable a cada candidato del Top-3 histórico fijo sin alterar la composición ni el orden del ranking histórico**.

El objeto de resultado es la **asociación/cobertura documental y su trazabilidad sobre candidatos ya fijados**, no la exactitud de clasificación ni la corrección jurídica del candidato.

### 2. Snapshot y fuentes congeladas

IA Gestora reconsultó directamente en el snapshot experimental congelado:

```text
EXPERIMENTAL_REPOSITORY = elVladdi/gci-nandina-rag
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
EXPERIMENT = EXP-04-F / historical_normative_integration_data_aduanas_clase87_v0.2
```

Fuentes primarias congeladas:

```text
SOURCE_METRICS = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_metrics.json
SOURCE_METRICS_GIT_BLOB = 3fddeba15d080468001b1a855749ab23b1f0f0fb

SOURCE_EVIDENCE_COVERAGE = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_evidence_coverage.json
SOURCE_EVIDENCE_COVERAGE_GIT_BLOB = f8a746933655864cda005f14b41938ae750ec9e5

SOURCE_RANKING_INVARIANCE = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_ranking_invariance.json
SOURCE_RANKING_INVARIANCE_GIT_BLOB = b295b399d80eee5fb21d1fd582cccae9afef4bdd

SOURCE_LABEL_LEAKAGE = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_label_leakage_audit.json
SOURCE_LABEL_LEAKAGE_GIT_BLOB = cad4b3c5daee8988ecd56a38d6150d98cdd96d94

SOURCE_COMPATIBILITY = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_compatibility.json
SOURCE_COMPATIBILITY_GIT_BLOB = 1d9070daea5875f47d9a10cbe714880fc9a06bf2

SOURCE_MISSING_EXACT = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_missing_exact_evidence.csv
SOURCE_MISSING_EXACT_GIT_BLOB = 7fe49b33b908f7d54b64ddbf03af8cb39c131c5b
```

El archivo de missing exact evidence contiene solo su encabezado, coherente con ausencia de slots sin asociación exacta en esta ejecución.

### 3. Ground truth numérico congelado

Unidad principal de esta etapa: **candidate slot** dentro del Top-3 histórico fijo.

```text
EVAL_CASES = 1056
CANDIDATES_PER_CASE = 3
CANDIDATE_SLOTS = 3168
EXACTLY_THREE_HISTORICAL_CANDIDATES_PER_CASE = TRUE
```

#### 3.1 Evidencia exacta de candidato

```text
EXACT_NANDINA8_EVIDENCE = 3168 / 3168 = 100.00%
CASE_ALL_TOP3_EXACT_EVIDENCE = 1056 / 1056 = 100.00%

RANK_1_EXACT_EVIDENCE = 1056 / 1056 = 100.00%
RANK_2_EXACT_EVIDENCE = 1056 / 1056 = 100.00%
RANK_3_EXACT_EVIDENCE = 1056 / 1056 = 100.00%
```

La cobertura exacta fue 100% tanto en los 709 casos donde el código de referencia estaba en el Top-3 histórico como en los 347 casos donde no estaba; este desglose puede usarse solo si mejora la claridad y no debe interpretarse como corrección del candidato.

#### 3.2 Contexto jerárquico y trazabilidad

```text
HS6_CONTEXT = 2168 / 3168 = 68.434343...% ≈ 68.43%
HS4_CONTEXT = 3168 / 3168 = 100.00%
CHAPTER_CONTEXT = 3168 / 3168 = 100.00%
HISTORICAL_PRECEDENT_COVERAGE = 3168 / 3168 = 100.00%
TRACEABILITY_COMPLETE = 3168 / 3168 = 100.00%
```

`HS6_CONTEXT` es contexto padre disponible y no debe confundirse con exact evidence a ocho dígitos. El resultado exacto NANDINA-8 permanece 3168/3168.

#### 3.3 Invariancia del ranking histórico

```text
RANKING_INVARIANCE_CASES = 1056 / 1056 = 100.00%
HISTORICAL_RANK_INVARIANCE_RATE = 1.0
TOP3_INVARIANCE_RATE = 1.0
TOP1_UNCHANGED = TRUE
TOP3_UNCHANGED = TRUE
POSITIONS_UNCHANGED = TRUE
HISTORICAL_SCORES_UNCHANGED = TRUE
NO_NEW_CANDIDATE_INSERTED = TRUE
NO_CANDIDATE_REMOVED = TRUE
NORMATIVE_SCORE_AFFECTS_ORDER = FALSE
```

Los hashes del resultado histórico antes y después de la integración normativa fueron idénticos (`c350b63e0180a4c28573d2626c76d030308913b690c524d2d62ea439cf34a6c8`).

#### 3.4 Control de uso de etiqueta

El audit de leakage congelado registra:

```text
LABEL_USED_FOR_CANDIDATE_SELECTION = FALSE
LABEL_USED_FOR_PRECEDENT_SELECTION = FALSE
LABEL_USED_FOR_EVIDENCE_SELECTION = FALSE
LABEL_USED_FOR_ORDER_OR_FALLBACK = FALSE
LABELS_ONLY_USED_AFTER_CONSTRUCTION_FOR_METRICS = TRUE
PASS = TRUE
```

Este control puede reportarse de forma breve como propiedad de construcción/validación; no debe convertirse en una afirmación de independencia estadística o de corrección sustantiva.

### 4. Límites interpretativos obligatorios

Los resultados anteriores autorizan afirmaciones de **coverage, association, provenance/traceability e invariance** dentro de la ejecución congelada. No autorizan:

- afirmar que 100% de cobertura implica 100% de corrección normativa;
- afirmar legal correctness, official classification, substantive normative correctness o equivalentes;
- afirmar que la evidencia recuperada/identificada es suficiente para resolver jurídicamente cada caso;
- reinterpretar HS6/HS4/chapter context como exact evidence a NANDINA-8;
- afirmar desempeño operacional fuera del benchmark offline;
- generalizar empíricamente fuera de Chapter 87;
- omitir la frontera temporal del corpus: la ejecución primaria utilizó el corpus congelado derivado de Decisión 885, mientras que el drift respecto de Decisión 906 ya está documentado en Methods/Validity y se tratará en sensibilidad/Discussion cuando corresponda.

Permanece vinculante:

```text
C12 = PROHIBITED / ASSOCIATION DOES NOT ESTABLISH SUBSTANTIVE NORMATIVE CORRECTNESS
C18 = PROHIBITED / NO LEGALLY BINDING CLASSIFICATION
C21 = AUTHORIZED WITH LIMITS / DOCUMENTARY CORPUS DRIFT
```

### 5. Frontera editorial de §5.3

B03 puede contener únicamente:

1. cobertura exacta a nivel de candidate slot y case-level Top-3;
2. disponibilidad de contexto jerárquico HS6/HS4/chapter;
3. cobertura del precedente histórico y trazabilidad completa;
4. invariancia de composición/orden/scores del ranking histórico tras la asociación documental;
5. control breve de ausencia de uso de la etiqueta en selección/asociación, si mejora la lectura;
6. una oración explícita que delimite association/coverage frente a substantive/legal correctness.

No pertenecen a B03:

- calidad de explicación o HE4;
- LLM-as-judge;
- inferencia, bootstrap, CI, p-values o HE2;
- sensibilidades EXP11A/EXP11B/0B-05C;
- HE5;
- comparación con literatura;
- Discussion;
- novelty/final gap.

### 6. Claims nuevos que deben registrarse antes de redacción

D-099 habilita la incorporación a `CLAIM_EVIDENCE_MATRIX.md` de los siguientes claims acotados:

```text
C30 = exact documentary association coverage 3168/3168 candidate slots and 1056/1056 cases with 3/3 exact Top-3 evidence / AUTHORIZED
C31 = historical-precedent coverage and complete candidate-level traceability 3168/3168 / AUTHORIZED
C32 = historical ranking and fixed Top-3 invariant in 1056/1056 cases after documentary association / AUTHORIZED
C33 = hierarchical context coverage HS6 2168/3168, HS4 3168/3168, chapter 3168/3168 / AUTHORIZED
C34 = frozen construction audit used no reference label for candidate, precedent, evidence, order, or fallback decisions / AUTHORIZED
```

Todos quedan subordinados a C12/C18/C21 y al alcance offline Chapter-87.

### 7. Exit

```text
RESULTS_B03_GROUND_TRUTH = SYNCHRONIZED
CLAIM_MATRIX_UPDATE = REQUIRED_BEFORE_DRAFTING_AUTHORIZATION
B03_PROMPT = NOT_YET_AUTHORIZED_BY_THIS_DECISION
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

D-099 synchronizes Results B03 / Section 5.3 ground truth against frozen EXP-04-F artifacts at development snapshot `db0d0ad0d8435921a7838db6720eaea86a263763`. Across 1,056 evaluation cases and 3,168 fixed historical Top-3 candidate slots, exact NANDINA-8 documentary association, historical-precedent coverage, and complete traceability were 100%; all cases had exact evidence for all three slots. HS6 parent context was available for 2,168/3,168 slots (68.43%), while HS4 and chapter context were available for all slots. Historical ranking/Top-3 membership, positions, scores, and candidate composition remained invariant in all 1,056 cases. The construction audit recorded no reference-label use for candidate, precedent, evidence, ordering, or fallback decisions. These results measure association, coverage, traceability, and invariance only; they do not establish substantive normative or legal correctness. New bounded claims C30-C34 must be registered before drafting authorization.