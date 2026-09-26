# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.2
LATEST_EDITORIAL_DECISION = D-051
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V010
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
CANONICAL_MASTER_MD_SHA256 = 82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_SECTION_4_3_DRAFTING
SECTION_4_3 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Jerarquía científica gobernante

El objeto general continúa siendo un **framework configurable para apoyo auditable a la clasificación arancelaria**. La arquitectura de Section 3 es su núcleo técnico:

```text
commercial description
→ normalization
→ historical retrieval
→ historical Top-k ranking
→ fixed Top-3
→ candidate-specific documentary/normative evidence
→ evidence-context construction
→ local LLM
→ controlled explanation of the fixed Top-3
```

El ranking histórico genera y ordena candidatos. El Top-3 queda fijado antes de la etapa documental. La evidencia documental no altera composición ni orden de candidatos, y el LLM opera downstream para explicación controlada. La arquitectura apoya una decisión; no adjudica autónomamente una clasificación jurídica final.

NANDINA de ocho dígitos, Chapter 87 y el contexto administrativo peruano constituyen la instanciación empírica evaluada, no el alcance conceptual completo del framework. La configurabilidad para otros bancos históricos, espacios de clases, profundidades arancelarias o corpus compatibles no equivale a generalización de desempeño.

### B01 integrado

D-050 verificó la materialización exacta de `ARTICLE_MASTER_V010.md` y cerró Experimental Design B01. Quedaron integrados y congelados:

- los ajustes editoriales controlados en 3.5 y 3.7;
- 4.1 `Experimental setting and scope`;
- 4.2 y 4.2.1–4.2.3;
- el posicionamiento transversal framework vs. instanciación experimental.

### Gate B02 / Section 4.3

D-051 abre exclusivamente `4.3 Documentary corpus and evidence resource` después de una reconstrucción independiente del ground truth.

Hechos congelados para este gate:

```text
PRIMARY_EVIDENCE_RESOURCE = HIERARCHICAL_NANDINA_CORPUS_DERIVED_FROM_DECISION_885
PRIMARY_EVIDENCE_ASSOCIATION = EXACT_NANDINA8_CODE_LOOKUP
QUERY_BASED_NORMATIVE_RETRIEVAL_IN_PRIMARY_PHASE_F = false
DOCUMENTARY_RERANKING = false
CANDIDATE_INSERTION_OR_SUBSTITUTION = false
CORPUS_SCOPE = NANDINA_HIERARCHY_FROM_FROZEN_SOURCE
EMPIRICAL_CANDIDATE_SCOPE = CHAPTER_87_INSTANCE
DECISION_885_EFFECTIVE = 2022-01-01
DECISION_906_MODIFIES_885_EFFECTIVE = 2023-01-01
PRIMARY_PHASE_F_HE4_CORPUS_RETROACTIVELY_REPLACED_BY_906 = false
TEMPORAL_VERSION_MISMATCH_RELATIVE_TO_2026_CASES = DISCLOSE
ARANCEL_2022_IN_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
CLASSIFICATION_RESOLUTIONS_IN_PRIMARY_HE4_CONTEXT = NOT_ESTABLISHED / DO_NOT_CLAIM
```

La ruta primaria usada para la explicación asocia evidencia por lookup exacto del código NANDINA-8 de cada candidato ya fijado. La terminología arquitectónica genérica de retrieval no autoriza a describir esta instanciación como BM25/query-based normative search.

La fuente del recurso verificado es la NANDINA aprobada por la Comisión de la Comunidad Andina mediante Decision 885. Decision 906 modificó esa nomenclatura y entró en vigencia antes del escenario administrativo 2026; la ruta primaria no fue reescrita retroactivamente con esa versión. Esta es una frontera de versionado que debe declararse sin convertirla en una afirmación de incorrección de todos los códigos Chapter 87 ni anticipar resultados de la línea correctiva posterior.

### Fronteras científicas obligatorias

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.
- `FRAMEWORK_GENERAL_SCOPE ≠ NANDINA_CHAPTER87_TESTBED`.
- `ARCHITECTURE = TECHNICAL_CORE_OF_FRAMEWORK`.
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`.
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.

### Gate vigente

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_SECTION_4_3_DRAFTING
NEXT_ACTOR = DRAFTING_AI
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B02_DOCUMENTARY_CORPUS_EVIDENCE_RESOURCE.md
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V010.md
BASELINE_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V05.docx
BASELINE_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
AUTHORIZED_SCOPE = SECTION_4_3_ONLY_ENGLISH_PLUS_SPANISH_MIRROR
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_WRITING_PLAN = V3.2
LATEST_EDITORIAL_DECISION = D-051
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
CANONICAL_MASTER = ARTICLE_MASTER_V010
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
CURRENT_GATE = EXPERIMENTAL_DESIGN_B02_SECTION_4_3_DRAFTING
SECTION_4_3 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_4_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

B02 is limited to Section 4.3 in English and its Spanish semantic-control mirror. The verified primary evidence resource is the hierarchical NANDINA corpus derived from Andean Community Decision 885. In the primary integrated path, documentary evidence is associated through exact NANDINA-8 code lookup for each already fixed Top-3 candidate; the documentary stage does not rerank, insert, or substitute candidates.

Decision 906 modified Decision 885 and became effective before the 2026 administrative scenario. The primary Phase-F/HE4 path nevertheless consumed the frozen Decision-885-derived resource. This version boundary must be disclosed as a methodological limitation without converting it into a blanket claim that all Chapter-87 evidence was incorrect and without anticipating corrective robustness results.
