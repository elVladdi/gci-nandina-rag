# D-092 — Sincronización de ground truth de Results B02 y frontera §5.2 / Results B02 ground-truth synchronization and §5.2 boundary

## Español

```text
DECISION_ID = D-092
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-091
PHASE = RESULTS
BLOCK = RESULTS_B02_SECTION_5_2
SECTION = 5.2 CANDIDATE_RETRIEVAL_PERFORMANCE
CANONICAL_MASTER = ARTICLE_MASTER_V017
RESULTS_B02 = GROUND_TRUTH_SYNCHRONIZED / PROMPT_PREPARATION_ALLOWED
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión

IA Gestora sincronizó independientemente el ground truth necesario para abrir exclusivamente Results B02 / Section 5.2 — Candidate retrieval performance. La sincronización usa el snapshot experimental congelado `db0d0ad0d8435921a7838db6720eaea86a263763` y el master canónico `ARTICLE_MASTER_V017.md`.

B02 reportará **desempeño descriptivo observado de candidate retrieval** sobre el mismo EVAL de 1,056 SERIE. No reportará todavía inferencia, intervalos de confianza, disposición HE2, sensibilidades, evidencia documental, explicación ni Discussion.

## 2. Fuentes primarias congeladas

```text
DEVELOPMENT_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
EVAL_N = 1056

SOURCE_HIST = outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json
SOURCE_HIST_GIT_BLOB = a43893eca3dd756a1ff11935a9cf55afb728e8f4

SOURCE_FLAT = outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/normative_flat_metrics.json
SOURCE_FLAT_GIT_BLOB = 922ecbee8316ee36cd8a53d3ac52f79fac4cd3ed

SOURCE_HIER = outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json
SOURCE_HIER_GIT_BLOB = 780a005130d1ad68867b290b832c394f8f488a23

SOURCE_D1A = outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_metrics.json
SOURCE_D1A_GIT_BLOB = 73e062b927d059a9f4e52caab7b785eafb6f2e01
```

Los cuatro artefactos usan el EVAL v0.2 de 1,056 casos. Los comparadores normativos y D1a son **comparadores de evaluación**; no sustituyen la fuente de candidatos del flujo primario del framework.

## 3. Ground truth descriptivo de early ranking

Las métricas autorizadas para comparación descriptiva en B02 son Top-1, Top-3, Top-5, Top-10, MRR@100 y Top-50 suplementario.

| Método | Top-1 | Top-3 | Top-5 | Top-10 | Top-50 | MRR@100 |
|---|---:|---:|---:|---:|---:|---:|
| Historical BM25 H100 | 538/1056 = 0.509469696969697 | 709/1056 = 0.6714015151515151 | 806/1056 = 0.7632575757575758 | 941/1056 = 0.8910984848484849 | 1047/1056 = 0.9914772727272727 | 0.6297077493524843 |
| Flat normative BM25 | 29/1056 = 0.027462121212121212 | 54/1056 = 0.05113636363636364 | 65/1056 = 0.061553030303030304 | 69/1056 = 0.06534090909090909 | 74/1056 = 0.07007575757575757 | 0.04229731726741296 |
| Hierarchical normative BM25 | 28/1056 = 0.026515151515151516 | 55/1056 = 0.052083333333333336 | 66/1056 = 0.0625 | 69/1056 = 0.06534090909090909 | 96/1056 = 0.09090909090909091 | 0.041971783226435376 |
| D1a Text2Trade-inspired MNRL | 1/1056 = 0.000946969696969697 | 11/1056 = 0.010416666666666666 | 54/1056 = 0.05113636363636364 | 188/1056 = 0.17803030303030304 | 331/1056 = 0.3134469696969697 | 0.038087139731859634 |

En prosa pueden redondearse los porcentajes a dos decimales, preservando conteos y denominadores cuando se presenten.

Interpretación autorizada: en este EVAL fijo, la recuperación histórica mostró los mayores valores observados entre estas cuatro familias en Top-1, Top-3, Top-5, Top-10, Top-50 y MRR@100. Esta es una **comparación descriptiva observada**; no sustituye la inferencia de §5.6.

Top-50 es suplementario y no debe tratarse como parte de la familia inferencial primaria de cinco métricas.

## 4. Deep coverage descriptivo autorizado

Para el comparador jerárquico corregido:

```text
EXACT_RECALL_AT_100 = 107/1056 = 0.10132575757575757
EXACT_RECALL_AT_200 = 321/1056 = 0.3039772727272727
POOL_RECALL_AT_200 = 321/1056 = 0.3039772727272727
```

B02 puede reportar estos valores como cobertura exacta observada a mayor profundidad. **No** debe reportar todavía la diferencia inferencial `Recall@200 - Recall@100`, su intervalo de confianza ni la disposición HE2_B; todo ello pertenece a §5.6.

## 5. Claims y límites

```text
C04 = AUTHORIZED
C05 = AUTHORIZED
C28 = ELIGIBLE_BUT_NOT_FOR_B02_DISPOSITION
C16 = PROHIBITED
C18 = PROHIBITED
```

B02 no puede convertir retrieval en `overall classification accuracy`, corrección normativa o corrección jurídica. Tampoco puede afirmar SOTA, superioridad cross-study, generalización fuera de Chapter 87, causalidad, significancia o desempeño operacional.

## 6. Exclusiones de B02

No incluir en §5.2:

- intervalos de confianza, bootstrap o p-values;
- diferencias inferenciales historical-minus-comparator;
- `HE2 = SUPPORTED` o cualquier disposición de hipótesis;
- EXP11A, EXP11B, Attempt06 como sensibilidad, EXP12 o HE5;
- candidate pools Phase E; se reservarán para su bloque descriptivo/sensibilidad si posteriormente se autoriza;
- asociación/cobertura normativa del Top-3;
- resultados de explicación o LLM-as-judge;
- literatura o comparación cross-study;
- interpretación de Discussion.

## 7. Baselines acumulativos obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V017.md
BASELINE_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
BASELINE_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
BASELINE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

El DOCX debe editarse directamente desde el binario exacto; no se reconstruye desde Markdown. D-035 continúa vinculante.

## 8. Gate

```text
CURRENT_GATE = RESULTS_B02_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = CREATE_AND_REVIEW_RESULTS_B02_PROMPT
RESULTS_B02 = NOT_YET_AUTHORIZED_FOR_EXECUTION
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

D-092 freezes the descriptive ground truth for Results B02 / Section 5.2. B02 may report observed early-ranking performance for historical BM25 H100, corrected flat normative BM25, corrected hierarchical normative BM25, and D1a Text2Trade-inspired MNRL on the common 1,056-case EVAL using Top-1/3/5/10, MRR@100, and supplementary Top-50. It may also report hierarchical exact Recall@100 and Recall@200/Pool@200 descriptively. Inferential differences, confidence intervals, HE2 dispositions, sensitivity analyses, documentary evidence, explanation results, literature comparison, and Discussion remain outside B02.