# D-067 — Experimental Design B05 / Section 4.6 ground-truth synchronization

## Español

```text
DECISION_ID = D-067
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-066
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 Evaluation framework and protocols
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
SRC03_HEAD_OBSERVED = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_OBSERVED = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
GROUND_TRUTH_SYNC = PASS
B05_PROMPT = REQUIRED / NOT_YET_AUDITED
SECTION_4_6 = READY_FOR_ATOMIC_PROMPT / NOT_YET_EXECUTABLE
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Función congelada de Section 4.6

La estructura aprobada exige mapear `RQ → función del sistema → salida → unidad de evaluación → métrica/protocolo → interpretación permitida` manteniendo tres objetos distintos:

1. `4.6.1 Candidate-retrieval evaluation`;
2. `4.6.2 Documentary-evidence evaluation`;
3. `4.6.3 Controlled-explanation evaluation`.

Section 4.6 describe **cómo se evalúa** cada función. Los valores observados y conclusiones experimentales pertenecen a Results. Los procedimientos inferenciales, de sensibilidad y robustez se desarrollan en Section 4.7.

### 2. Sincronización de candidate retrieval

El contrato analítico congelado `docs/analysis/group3/g3_analytical_contract_v0.1.md` confirma:

- SERIE como unidad primaria de análisis;
- DAM/declaración como unidad de dependencia cuando corresponde;
- EVAL v0.2 fijo de 1,056 series;
- para HE2_A: Top-1, Top-3, Top-5, Top-10 y MRR@100 como métricas primarias; Top-50 es suplementaria;
- comparación elegible de historical retrieval contra las familias normativas corregidas flat, hierarchical y D1a, sin transformar candidate retrieval en accuracy global;
- HE2_B/deep coverage es un objeto distinto de early-ranking performance;
- candidate-pool variants de Phase E son descriptivas y no equivalen a ranking principal;
- EXP11A es sensibilidad descriptiva tamaño/composición; EXP11B es descriptivo; EXP12 no es estimable.

La mecánica inferencial DAM-cluster-aware pertenece principalmente a 4.7 y no debe desarrollarse anticipadamente en 4.6.

### 3. Sincronización de documentary evidence

`outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json` confirma que la evaluación documental parte del Top-3 histórico fijo, con tres candidate slots por caso, y que la asociación primaria usa lookup directo por NANDINA-8. El label de evaluación no participa en selección de candidatos, precedentes, evidencia, orden ni fallback.

Las dimensiones protocolarias elegibles incluyen, según los artefactos de integración:

- disponibilidad/cobertura de evidencia exacta por candidato;
- disponibilidad de contexto jerárquico cuando corresponda;
- cobertura del precedente histórico;
- trazabilidad candidato–precedente–evidencia;
- invariancia del ranking/Top-3 después de la asociación documental.

Los valores observados de cobertura e invariancia —incluidos conteos como 3,168 candidate slots y tasas empíricas— son Results y no deben narrarse como resultados en 4.6. La cobertura o asociación documental no demuestra corrección normativa o jurídica sustantiva.

### 4. Sincronización de controlled explanation

La evaluación HE4 tiene dos capas que deben permanecer separadas metodológicamente:

**A. Controles automáticos estructurales y de trazabilidad.** El Gate J verifica propiedades tales como preservación del Top-3/orden, ausencia de códigos externos o duplicados, validez de referencias histórica/normativa, trazabilidad, presencia de comparación, parseo/estructura y ausencia de leakage explícito. No existió una regla congelada única de PASS/FAIL por caso para `automatic_validation_pass`; por tanto no debe inventarse retrospectivamente.

**B. Evaluación cualitativa congelada.** La guía `he4_qualitative_scoring_guide_v0.2.md` define ocho dimensiones con puntuación 0–2: trazabilidad, verificabilidad, separación histórico/normativo, prudencia de conclusión, consistencia con Top-3 fijo, detección de evidencia normativa genérica, comparación entre candidatos y utilidad para auditoría humana. Una ficha se considera auditable con total `>=12/16` y ausencia de hard violation.

Hard constraints congelados: preservación exacta del Top-3 y su orden, ausencia de códigos externos, ausencia de clasificación oficial/categórica, conclusión como apoyo documental para revisión experta y JSON estricto en el artefacto técnico. `advertencias_globales` queda excluido del scoring por el mismatch prompt-schema congelado.

La muestra HE4 consta de 50 casos seleccionados determinísticamente mediante estratificación por bucket de soporte, conteo de soporte, rank exacto y `case_id`, con seed 2026. Su composición congelada es 10 `difficult_low_support`, 15 `rank_1`, 15 `rank_2_3` y 10 `rank_4_10`.

La modalidad efectiva del evaluador fue `AI_EXPERT_ROLE / LLM-as-judge`, no revisión humana. El manifiesto K registra desviación respecto de la modalidad originalmente prevista `HUMAN/MANUAL REVIEW`; ground truth, reference rank y bucket no fueron expuestos al evaluador, no se usó evidencia externa ni web. Esta limitación de modalidad debe quedar explícita en Methods cuando se describa el protocolo real.

### 5. Research questions del artículo

El master canónico V013 fija cuatro RQ:

- RQ1: desempeño de candidate retrieval histórico bajo particiones disjuntas por DAM;
- RQ2: grado en que evidencia normativa identificable puede asociarse a cada candidato del Top-3 fijo sin alterar el orden;
- RQ3: grado en que el LLM local restringido al Top-3 preserva candidatos/orden y produce explicaciones estructuradas vinculadas a evidencia identificable;
- RQ4: límites de validez por dependencia intra-DAM, near-duplicates, composición histórica y drift normativo.

B05 desarrolla principalmente los protocolos RQ1–RQ3. RQ4 se conecta con controles ya descritos en 4.4 y con análisis/robustez de 4.7; no debe duplicarse ni anticiparse en 4.6.

### 6. Gate

La sincronización no autoriza todavía la redacción. Debe materializarse un prompt B05 bilingüe, autosuficiente y sometido a revisión interna antes de abrir el gate de ejecución.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_PROMPT_MATERIALIZATION_AND_AUDIT
NEXT_ACTOR = IA_GESTORA
SECTION_4_6 = READY_FOR_ATOMIC_PROMPT / NOT_YET_EXECUTABLE
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-067
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-066
BLOCK = EXPERIMENTAL_DESIGN_B05
SECTION = 4.6 Evaluation framework and protocols
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
SRC03_HEAD_OBSERVED = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_OBSERVED = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
GROUND_TRUTH_SYNC = PASS
B05_PROMPT = REQUIRED / NOT_YET_AUDITED
SECTION_4_6 = READY_FOR_ATOMIC_PROMPT / NOT_YET_EXECUTABLE
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The frozen Section-4.6 function is to map each research question to system function, output, evaluation unit, metric/protocol, and permitted interpretation while keeping candidate retrieval, documentary evidence, and controlled explanation distinct.

For candidate retrieval, the frozen Group-3 contract uses SERIE as the primary analysis unit and defines Top-1, Top-3, Top-5, Top-10, and MRR@100 as primary HE2_A metrics, with Top-50 supplementary. Deep coverage is a separate object; inferential and robustness procedures belong primarily in Section 4.7.

For documentary evidence, Phase F evaluates association from an already fixed historical Top-3 through direct NANDINA-8 lookup, with candidate-level evidence/context, historical-precedent linkage, traceability, and ranking invariance as protocol dimensions. Coverage is not substantive normative/legal correctness, and observed rates belong to Results.

For controlled explanation, the actual protocol separates automatic structural/traceability checks from an eight-dimension qualitative rubric scored 0–2. Auditability requires at least 12/16 with no hard violation. The qualitative sample has 50 deterministically selected cases. The effective evaluator modality was an independent AI expert / LLM-as-judge rather than the originally planned human/manual modality; this methodological deviation must be stated and bounded. No ground truth, reference rank, external evidence, or web information was exposed to that evaluator.

The canonical RQs map RQ1 to candidate retrieval, RQ2 to documentary association, RQ3 to controlled explanation, and RQ4 chiefly to validity/robustness controls already distributed across Sections 4.4 and 4.7. Drafting remains closed until the B05 prompt is materialized and independently audited.