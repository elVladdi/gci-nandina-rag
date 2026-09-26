# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-066
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política acumulativa

El artículo se construye sobre masters acumulativos. Cada bloque parte del master canónico vigente y solo se integra después de superar auditorías aplicables, correcciones, aprobación autoral cuando corresponda y promoción técnica exacta.

Permanecen vinculantes MWDP v1.0, SPCCR, las decisiones activas, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, la guía empírica KBS y las fuentes experimentales gobernantes.

Fronteras científicas permanentes:

- framework general configurable ≠ testbed NANDINA/Capítulo 87;
- recuperación histórica = generación/ranking principal de candidatos;
- Top-3 fijado antes de evidencia documental y generación;
- evidencia documental/normativa = evidencia específica por candidato, no reranking;
- LLM local = explicación controlada downstream, no clasificador autónomo;
- `candidate retrieval ≠ overall classification accuracy`;
- `normative association ≠ substantive normative correctness`;
- `auditability ≠ legal correctness`;
- `configurability ≠ empirical generalization`;
- SERIE = unidad primaria de análisis; DAM/declaración = unidad de agrupamiento cuando la dependencia importa;
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`;
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`;
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`;
- `FINAL_GAP = NOT_DEFINED`;
- `NOVELTY = NOT_DECLARED`.

## 2. Estructura congelada de Experimental Design

```text
4.1 Experimental setting and scope
4.2 Historical data and experimental dataset construction
  4.2.1 Source and data collection
  4.2.2 Processing and curation
  4.2.3 Partition construction and dataset composition
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

## 3. Continuidad Markdown/DOCX

Master Markdown canónico:

`article/manuscript/ARTICLE_MASTER_V013.md`

- SHA-256 aprobado: `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43`;
- Git blob verificado: `06beaa052e2f1bcc630647040762fe78d3838a62`.

Baseline Word acumulativo:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx`

- SHA-256: `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`;
- custodia local del autor;
- 40 comentarios/anclajes heredados;
- tracked changes = 0.

D-021/D-027/D-035 permanecen vinculantes. El DOCX no puede reconstruirse desde Markdown ni desde un Word anterior.

## 4. Estado de bloques

| Bloque | Estado |
|---|---|
| Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B02 / 4.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B03 / 4.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B04 / 4.5 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| ARTICLE_MASTER_V013 | CANONICAL / VERIFIED |
| B05 / 4.6 | ELIGIBLE / GROUND-TRUTH SYNC + PROMPT PREPARATION |
| 4.7–4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 5. Fase activa — B05 / Section 4.6

La función narrativa está congelada por Structure V02:

`Mapear RQ → función del sistema → salida → unidad de evaluación → métrica/protocolo → interpretación permitida`, separando estrictamente:

1. `4.6.1 Candidate-retrieval evaluation`;
2. `4.6.2 Documentary-evidence evaluation`;
3. `4.6.3 Controlled-explanation evaluation`.

B05 describe **protocolos de evaluación**, no resultados. Los valores observados, conclusiones HE2/HE5 y comparaciones finales pertenecen a Results/Discussion. Los procedimientos inferenciales y de robustez pertenecen a 4.7 salvo que una referencia mínima sea necesaria para delimitar 4.6.

### 5.1 Fuentes experimentales mínimas para el contrato B05

El prompt B05 deberá obligar a verificar directamente en `main` y SRC-03, como mínimo:

- `docs/analysis/group3/g3_analytical_contract_v0.1.md` para unidades, métricas, familias y límites interpretativos;
- outputs congelados de historical retrieval y las familias normativas comparables solo para verificar cómo se materializan las métricas, sin narrar sus valores;
- `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/` para el protocolo de cobertura/trazabilidad documental;
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_scoring_guide_v0.2.md` y los manifests J/K para controles automáticos, rúbrica cualitativa, unidad muestral y limitación de modalidad del evaluador;
- cualquier fuente adicional necesaria para sustentar claims específicos.

### 5.2 Límites que debe imponer B05

- Candidate retrieval: métricas autorizadas y unidad de evaluación; no llamar a esto accuracy global.
- Documentary evidence: cobertura/asociación/trazabilidad; no convertir cobertura en corrección jurídica o normativa sustantiva.
- Controlled explanation: separar controles automáticos estructurales de la evaluación cualitativa; explicitar la rúbrica congelada y la modalidad efectiva del evaluador cuando sea metodológicamente relevante; no afirmar validación humana si no ocurrió.
- No introducir resultados numéricos observados en 4.6 salvo tamaños/configuración imprescindibles para describir el protocolo y ya pertenecientes a Methods.
- No ejecutar inferencia ni sensibilidad en 4.6; 4.7 permanece cerrado.

## 6. Concurrencia experimental observada

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
GROUP3 = CLOSED / APPROVED
GROUP4 = CLOSED / APPROVED
GROUP5 = CLOSED / APPROVED
GROUP6 = CLOSED / APPROVED
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

El estado de Grupo 7 es un flujo externo de redacción de tesis y no modifica automáticamente el gate editorial del artículo.

## 7. Gate inmediato

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = MATERIALIZE_AND_AUDIT_B05_ATOMIC_PROMPT
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx
BASELINE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Cumulative policy

The article uses cumulative masters. V013 is the current canonical Markdown master, verified by Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`. The cumulative Word baseline is the approved B04 V02 DOCX in local author custody, SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`, with 40 inherited comments and zero tracked changes.

B01–B04 are closed, approved, frozen, and integrated. B05/Section 4.6 is the next eligible block but is not yet authorized for drafting. Sections 4.7–4.8 and Results remain closed.

## 2. B05 function

Section 4.6 must map `RQ → system function → output → evaluation unit → metric/protocol → permitted interpretation` while keeping candidate retrieval, documentary evidence, and controlled explanation evaluation strictly separate. It describes protocols rather than observed results; inferential/robustness procedures remain primarily in Section 4.7.

The B05 contract must bind the Drafting AI to the frozen analytical contract, primary evaluation artifacts, documentary-integration coverage/traceability artifacts, and the frozen HE4 automatic/qualitative evaluation protocol. It must preserve the boundaries that candidate retrieval is not global classification accuracy, documentary association is not substantive legal correctness, and explanation auditability is not legal correctness.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
NEXT_ACTOR = MANAGING_AI
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```