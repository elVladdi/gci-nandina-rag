# 0B-05C — Revisión interna / Internal Review

## Español

### Dictamen

`0B-05C_INTERNAL_REVIEW = PASS WITH CORRECTIONS`

La revisión científica/editorial independiente confirma el núcleo del entregable 0B-05C, pero mantiene el bloque abierto porque se activó un gate experimental.

Estados verificados:

- `SOURCE_VERSION_DRIFT = PRESENT`.
- `SCOPE_OVERLAP = CONFIRMED`.
- `RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25`.
- `EXPERIMENTAL_METRIC_IMPACT = NOT_DETERMINED`.
- `EXPERIMENTAL_REVIEW = REQUIRED`.
- `TRIGGER = EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`.
- `AUTHOR_APPROVAL = NOT_REQUESTED`.
- `FREEZE = NOT_PERFORMED`.
- `NEXT_BLOCK_AUTHORIZED = NO`.
- `MANUSCRIPT_DRAFTING_AUTHORIZED = NO`.

### Hallazgo material

La revisión confirmó que el snapshot normativo experimental conserva textos derivados de la Decisión 885 pese a la existencia de la Decisión 906 vigente, con solapamiento material dentro del Capítulo 87.

Además, se verificó un solapamiento directo en output de retrieval: `87044110` aparece en `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, caso `DA-EVAL-V02-00060`, `candidate_rank = 100`, `candidate_doc_id = NANDINA_87044110`, con la descripción proveniente del snapshot Decisión 885.

No se identificó `87045110` en el mismo output plano Top-100. La ausencia de ambos códigos entre labels EVAL o candidatos del ranking histórico no elimina el drift normativo y no autoriza inferir impacto métrico cero.

Debe mantenerse estrictamente:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

### Correcciones obligatorias C1–C6

- **C1 — material:** incorporar el overlap observado de `87044110` en `normative_results.csv`, caso `DA-EVAL-V02-00060`, rank 100.
- **C2 — cadena de artefactos:** EV-03 ejecutó sobre `data/processed/corpus_rag_v1_index.jsonl`; EV-04 sobre `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`. No confundir fuente ancestral con input efectivo del experimento.
- **C3 — estados:** ausencia en labels EVAL o candidatos históricos es una intersección negativa, no `NO_DRIFT_IDENTIFIED`.
- **C4 — modificaciones nacionales:** limitar cualquier conclusión a los instrumentos nacionales efectivamente auditados; no convertir esa revisión en prueba universal de inexistencia de otras normas.
- **C5 — DESPA-PG.01:** corregir la precisión temporal de la RS 079-2026/SUNAT; la vigencia general y la disposición específica no deben fusionarse ni transformarse artificialmente en impacto experimental.
- **C6 — frontera de impacto:** la aparición de `87044110` en rank 100 no demuestra por sí sola cambios de Top-k, Recall, MRR, cobertura, integración, HE4 u otras métricas.

### Gate

La siguiente acción obligatoria es revisión de la IA experimental. Esta revisión debe determinar la materialidad sobre EV-03, EV-04 y solo si la trazabilidad lo demuestra sobre componentes downstream, preservando íntegramente el snapshot experimental original.

El editor científico no modifica el Plan Maestro. Su autoridad permanece exclusivamente en la IA experimental conforme a la gobernanza vigente.

`NO AVANZAR` a 0B-06, 0C, 0D ni manuscrito hasta recibir el dictamen experimental, corregir 0B-05C si corresponde y completar nuevamente el gate editorial.

---

## English

### Decision

`0B-05C_INTERNAL_REVIEW = PASS WITH CORRECTIONS`

The independent scientific/editorial review confirms the core of the 0B-05C deliverable, but keeps the block open because an experimental gate has been triggered.

Verified states:

- `SOURCE_VERSION_DRIFT = PRESENT`.
- `SCOPE_OVERLAP = CONFIRMED`.
- `RETRIEVAL_OUTPUT_OVERLAP = CONFIRMED_FOR_87044110_FLAT_BM25`.
- `EXPERIMENTAL_METRIC_IMPACT = NOT_DETERMINED`.
- `EXPERIMENTAL_REVIEW = REQUIRED`.
- `TRIGGER = EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`.
- `AUTHOR_APPROVAL = NOT_REQUESTED`.
- `FREEZE = NOT_PERFORMED`.
- `NEXT_BLOCK_AUTHORIZED = NO`.
- `MANUSCRIPT_DRAFTING_AUTHORIZED = NO`.

### Material finding

The review confirmed that the experimental normative snapshot preserves Decision-885-derived text despite the existence of effective Decision 906, with material scope overlap inside Chapter 87.

A direct retrieval-output overlap was also verified: `87044110` appears in `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_results.csv`, case `DA-EVAL-V02-00060`, `candidate_rank = 100`, `candidate_doc_id = NANDINA_87044110`, using the description from the Decision 885 snapshot.

`87045110` was not identified in the same flat Top-100 output. The absence of both codes from EVAL labels or historical-ranking candidates does not remove the normative drift and does not authorize an inference of zero metric impact.

The following separation must remain strict:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

### Mandatory corrections C1–C6

- **C1 — material:** add the observed `87044110` overlap in `normative_results.csv`, case `DA-EVAL-V02-00060`, rank 100.
- **C2 — artifact chain:** EV-03 ran on `data/processed/corpus_rag_v1_index.jsonl`; EV-04 ran on `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`. Do not confuse an ancestral source with the effective experimental input.
- **C3 — states:** absence from EVAL labels or historical candidates is a negative intersection result, not `NO_DRIFT_IDENTIFIED`.
- **C4 — national amendments:** constrain conclusions to the national instruments actually audited; do not turn that review into universal evidence that no other relevant instrument exists.
- **C5 — DESPA-PG.01:** correct the temporal precision concerning RS 079-2026/SUNAT; general effectiveness and the specific provision must not be merged or artificially converted into experimental impact.
- **C6 — impact boundary:** the presence of `87044110` at rank 100 does not by itself demonstrate changes in Top-k, Recall, MRR, coverage, integration, HE4, or any other metric.

### Gate

The next mandatory action is experimental-AI review. That review must determine materiality for EV-03, EV-04 and only where traceability demonstrates it, downstream components, while preserving the original experimental snapshot intact.

The scientific editor does not modify the Master Plan. Authority over the Master Plan remains exclusively with the experimental AI under the current governance.

`DO NOT ADVANCE` to 0B-06, 0C, 0D, or manuscript drafting until the experimental decision is received, 0B-05C is corrected if required, and the editorial gate is completed again.
