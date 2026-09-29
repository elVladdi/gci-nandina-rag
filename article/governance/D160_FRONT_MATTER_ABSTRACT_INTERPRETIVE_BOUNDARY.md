# D-160 — Front matter Abstract interpretive boundary

## Español

```text
DECISION = D-160
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B01_ABSTRACT
CANONICAL_MASTER = ARTICLE_MASTER_V031
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V031.md
CANONICAL_MASTER_MD_SHA256 = 6f05e9e3b8a480fb24c46f5984214900cb8d77bfb203589b179da15aff059300
CANONICAL_MASTER_MD_GIT_BLOB = a8bfdcd30d1ec205c486102d991c37085f307b8c
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_CONCLUSION_B01_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = d561a0f25eca77ea234f9a0684786b57f8969436c8db1481cabbcc6db0f0792d
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0
CANONICAL_DOCX_PAGE_COUNT = 71
PRIMARY_INPUTS = INTRODUCTION; ARCHITECTURE; EXPERIMENTAL_DESIGN; RESULTS; DISCUSSION; CONCLUSION
NEW_LITERATURE = PROHIBITED
NEW_CITATIONS = PROHIBITED
NEW_RESULTS = PROHIBITED
NEW_CALCULATIONS = PROHIBITED
NEW_INFERENCE = PROHIBITED
TITLE = PRESERVE_PLACEHOLDER
ABSTRACT = DRAFT_EN_AND_ES
KEYWORDS = PRESERVE_PLACEHOLDER
END_MATTER = PRESERVE
FINAL_GAP = NOT_DEFINED
NOVELTY_CLAIM = PROHIBITED
SOTA_OR_SUPERIORITY_CLAIM = PROHIBITED
EXTERNAL_GENERALIZATION = PROHIBITED
LEGAL_CORRECTNESS = PROHIBITED
DEPLOYMENT_READINESS = PROHIBITED
HUMAN_EXPERT_VALIDATION = PROHIBITED
ABSTRACT_FUNCTION = PROBLEM_AND_LIMITATION -> PROPOSAL_AND_AUTHORITY_BOUNDARIES -> EVALUATION_AND_MAIN_EVIDENCE -> BOUNDED_INTERPRETATION
TARGET_ENGLISH_WORD_COUNT = APPROX_200_250
```

### Objeto científico

El Abstract debe condensar el artículo completo como una unidad autosuficiente y reader-facing. Debe seguir las convenciones observadas en KBS: problema/contexto inmediato, limitación concreta, propuesta, evaluación/evidencia e interpretación delimitada. No debe funcionar como introducción abreviada ni como inventario de métricas.

El lector debe poder entender el problema sin conocer NANDINA de antemano y distinguir la función de las tres etapas principales: historical candidate retrieval fija el ranking y el Top-3; candidate-specific documentary association añade evidencia sin reordenar; y el local LLM genera únicamente la explicación del conjunto ya fijado.

### Contenido autorizado

El Abstract puede sintetizar, con economía, que:

1. el problema metodológico es que mezclar autoridad entre candidate selection, documentary evidence y generation dificulta atribuir y evaluar qué componente produjo cada salida;
2. el framework separa esas autoridades: historical retrieval fija el Top-3 antes de las etapas documental y generativa;
3. el piloto offline evalúa por separado candidate retrieval, documentary association y controlled explanation en un testbed de Chapter 87 / NANDINA-8;
4. como evidencia principal de candidate retrieval, puede informarse Top-1 = 50.95% y/o Top-3 = 67.14%; MRR@100 = 0.6297 es opcional si mejora la síntesis;
5. exact documentary association estuvo disponible para 3,168/3,168 candidate slots y la membresía/orden del Top-3 se preservó en 1,056/1,056 casos;
6. en la muestra de explicación, Top-3 y orden se preservaron en 50/50 y 28/50 (56.0%) cumplieron el criterio cualitativo predefinido de auditabilidad bajo evaluación LLM-as-judge;
7. la implicación autorizada es que separar autoridad y preservar provenance hace inspeccionables ranking, documentary evidence y generated explanation como salidas diferenciadas;
8. los resultados están delimitados al benchmark offline evaluado y no establecen overall classification accuracy, substantive normative/legal correctness, human expert validation, external generalization ni deployment readiness.

### Prioridad de cifras

El Abstract debe usar solo las cifras que materialmente sostengan el argumento central. Preferencia:

```text
PRIMARY_CANDIDATE_METRIC = TOP3_67_14_PERCENT
OPTIONAL_CANDIDATE_METRIC = TOP1_50_95_PERCENT
OPTIONAL_MRR = 0_6297
DOCUMENTARY_ASSOCIATION = 3168_OF_3168
RANKING_INVARIANCE = 1056_OF_1056
EXPLANATION_AUDITABILITY = 28_OF_50_56_PERCENT
```

No incluir intervalos de confianza, p-values, métricas de comparadores, sensibilidad detallada, buckets de soporte, cifras de near-duplicates ni inventarios de robustness salvo que fueran indispensables para evitar una interpretación incorrecta. En principio deben quedar fuera por economía.

### Terminología y límites vinculantes

Preservar:

```text
ARCHITECTURE = TECHNICAL_CORE_OF_FRAMEWORK
HISTORICAL_RETRIEVAL = ONLY_PRIMARY_CANDIDATE_RANKING_AUTHORITY
FIXED_TOP3 = ESTABLISHED_BEFORE_DOCUMENTARY_AND_GENERATIVE_STAGES
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
LLM_AS_JUDGE != HUMAN_EXPERT_VALIDATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
REINSTANTIATION != DEPLOYMENT_READINESS
CHAPTER87_RESULTS = NOT_TRANSFERABLE_BY_ASSUMPTION
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No usar `novel`, `first`, `state of the art`, `superior`, `best`, `validated for deployment`, `legally correct`, `human validated`, `generalizable`, `robust across jurisdictions` ni equivalentes.

### Prosa y estructura

El Abstract inglés debe tener aproximadamente 200–250 palabras, preferentemente un único párrafo continuo, sin citas. El espejo español debe ser natural y semánticamente equivalente. Debe usar prosa concreta, evitar códigos internos y no mencionar IDs de decisiones, prompts, gates, hashes, commits, nombres internos de experimentos o artefactos de gobernanza.

El nombre `H100` no es necesario en Abstract; si se informa el resultado histórico, preferir formulación reader-facing como `historical BM25 over the full historical bank`.

### Gate

```text
CURRENT_GATE = FRONT_MATTER_B01_ABSTRACT_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = CREATE_REVIEW_AND_AUTHORIZE_ABSTRACT_B01_PROMPT
TITLE = NOT_AUTHORIZED
ABSTRACT = BOUNDED_FOR_PROMPT_PREPARATION
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

D-160 bounds the final Abstract to a concise KBS-style sequence of problem/limitation, proposal with explicit authority separation, evaluation/main evidence, and bounded interpretation. It must be understandable without prior NANDINA knowledge, use only already integrated evidence, introduce no citations or new claims, and keep candidate retrieval, documentary association, and controlled explanation distinct. Title, Keywords, end matter, FINAL_GAP, and novelty remain outside this block.
