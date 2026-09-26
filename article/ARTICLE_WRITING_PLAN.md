# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-065
CANONICAL_MASTER = ARTICLE_MASTER_V012
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V013
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V013_CANONICAL_INTEGRATION
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_5 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_6 = ELIGIBLE_AFTER_V013_INTEGRATION_AND_GROUND_TRUTH_SYNC / NOT_AUTHORIZED
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política científica y editorial acumulativa

El artículo se construye mediante masters acumulativos. Cada bloque parte del último master canónico y solo puede convertirse en estado de referencia después de auditoría independiente, correcciones aplicables, aprobación autoral cuando corresponda e integración técnica exacta.

Permanecen vinculantes MWDP v1.0, SPCCR, las decisiones activas, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, la guía empírica KBS y las fuentes experimentales gobernantes.

Fronteras obligatorias:

- el objeto general es un framework configurable para apoyo auditable a la clasificación arancelaria;
- Section 3 es su núcleo técnico;
- recuperación histórica = generación/ranking de candidatos;
- Top-3 fijado antes de evidencia documental y generación;
- evidencia normativa/documental = asociación de evidencia, no reranking;
- LLM local = explicación controlada downstream, no clasificador autónomo;
- `candidate retrieval ≠ overall classification accuracy`;
- `normative association ≠ substantive normative correctness`;
- `auditability ≠ legal correctness`;
- `configurability ≠ empirical generalization`;
- SERIE = unidad de análisis; DAM/declaración = unidad de agrupamiento cuando la dependencia es relevante;
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`;
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`;
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`;
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED`.

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

## 3. Política de continuidad Markdown/DOCX

Master Markdown canónico actual, hasta cierre técnico de V013:

`article/manuscript/ARTICLE_MASTER_V012.md`

SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f` is NOT applicable; the correct V012 SHA is `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78` and Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`.

Approved B04 V02 cumulative candidate:

- Markdown: `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.md`;
- SHA-256: `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43`;
- expected Git blob: `06beaa052e2f1bcc630647040762fe78d3838a62`;
- DOCX: `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx`;
- DOCX SHA-256: `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`;
- citation comments: 40 preserved;
- tracked changes: 0.

D-021/D-027/D-035 remain binding. The DOCX remains under local author custody and must not be reconstructed from Markdown or from an earlier Word file.

## 4. Estado de bloques

| Bloque | Estado |
|---|---|
| Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B02 / 4.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B03 / 4.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B04 / 4.5 | CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION |
| ARTICLE_MASTER_V013 | AUTHORIZED / NOT_YET_VERIFIED_AS_MATERIALIZED |
| B05 / 4.6 | ELIGIBLE AFTER V013 + LIVE GROUND-TRUTH SYNC / NOT AUTHORIZED |
| 4.7–4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 5. Cierre de B04

B04 V01 fue ejecutado bajo el contrato V03. La auditoría de Gestora detectó únicamente dos problemas estrechos de precisión, B04-C01 y B04-C02. D-063 autorizó su corrección literal y B04 V02 la ejecutó sin otras mutaciones. La revisión diferencial V01 emitió PASS. D-064 abrió el gate de aprobación autoral y el autor aprobó expresamente B04 V02. D-065 congela Section 4.5 y autoriza la promoción byte-exacta del candidato a `ARTICLE_MASTER_V013.md`.

No se reabre contenido B01–B04 durante la promoción.

## 6. Siguiente bloque: B05 / Section 4.6

B05 no se abre todavía. Antes deben cumplirse tres condiciones:

1. materializar y verificar `ARTICLE_MASTER_V013.md` con el blob exacto `06beaa052e2f1bcc630647040762fe78d3838a62`;
2. reconstruir el estado vivo de SRC-03 y `main` relevante a los protocolos de evaluación;
3. emitir y auditar un prompt atómico específico para Section 4.6 que cubra 4.6, 4.6.1, 4.6.2 y 4.6.3 sin anticipar Results ni invadir 4.7.

El futuro contrato B05 deberá mapear explícitamente `RQ → función del sistema → salida → unidad de evaluación → métrica/protocolo → interpretación permitida` y mantener separadas la evaluación de candidate retrieval, documentary evidence y controlled explanation.

## 7. Gate inmediato

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V013_CANONICAL_INTEGRATION
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V013
TARGET_PATH = article/manuscript/ARTICLE_MASTER_V013.md
EXPECTED_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
EXPECTED_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V012
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Cumulative scientific/editorial policy

The article uses cumulative masters. Each block starts from the latest canonical master and becomes the reference state only after independent audit, applicable corrections, author approval where required, and exact technical integration.

MWDP v1.0, SPCCR, active decisions, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, the KBS empirical guide, and governing experimental sources remain binding. The functional separation among historical candidate ranking, fixed Top-3, documentary evidence, and downstream controlled explanation remains mandatory, as do all frozen interpretation boundaries and the `FINAL_GAP = NOT_DEFINED` / `NOVELTY = NOT_DECLARED` constraints.

## 2. Experimental Design structure

Section 4 remains frozen as 4.1 setting/scope, 4.2 historical data/dataset construction, 4.3 documentary corpus, 4.4 partition validity, 4.5 experimental system configuration/execution, 4.6 evaluation framework/protocols with three functional subsections, 4.7 statistical/robustness analysis, and 4.8 reproducibility resources.

## 3. Markdown/DOCX continuity

Until V013 promotion closes, `ARTICLE_MASTER_V012.md` remains canonical at SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`, blob `dfea73f5f462fc65cf98347f796deadc6da58455`.

The author-approved B04 V02 cumulative candidates are Markdown SHA-256 `2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43`, expected Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`, and DOCX SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`. The Word file remains in local author custody with 40 inherited citation comments and zero tracked changes.

## 4. Block state

B01–B03 are closed, approved, frozen, and integrated. B04/4.5 is closed, approved, frozen, and ready for integration. V013 is authorized but not yet verified as materialized. B05/4.6 is eligible only after V013 integration and live ground-truth synchronization; 4.7–4.8 and Results remain unauthorized.

## 5. Immediate gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_V013_CANONICAL_INTEGRATION
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V013
TARGET_PATH = article/manuscript/ARTICLE_MASTER_V013.md
EXPECTED_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
EXPECTED_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V012
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```