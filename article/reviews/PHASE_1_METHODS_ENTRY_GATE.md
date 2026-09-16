# Gate de entrada Fase 1 — Methods / Phase 1 Entry Gate — Methods

## Español

### 1. Estado de entrada

```text
ARTICLE_SNAPSHOT_AT_GATE = b6a33e187fc5cbd2eec6fa68a6a99bc7ff4b5f74
SRC03_LIVE_BRANCH_HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
PHASE_0 = CLOSED / APPROVED
0C = CLOSED / APPROVED / FROZEN
0D = CLOSED / APPROVED / FROZEN
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`; `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; y el `SRC-03` vivo en `docs/plan-maestro-temporal-2026-08-31`.

### 2. Verificación del estado experimental vivo

El `SRC-03` vivo en el snapshot `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6` establece:

```text
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
GROUP3 = NOT_STARTED
```

Por tanto, no existen cierres vigentes de Grupo 3A/3B en este corte. HE2/HE5 y la inferencia final asociada a Grupo 3 permanecen pendientes. Esto no bloquea `Methods B01`, porque B01 se limita a diseño, alcance y unidades y no reporta resultados ni inferencias de Grupo 3.

### 3. Bloque autorizado

```text
PHASE_1 = OPENED
METHODS_B01 = READY_FOR_DRAFTING
METHODS_B01_TITLE = Design, scope, and units
MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY
OTHER_METHODS_BLOCKS = NOT_AUTHORIZED_YET
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

`Methods B01` puede establecer exclusivamente:

- diseño como piloto experimental aplicado y offline;
- alcance evaluado NANDINA en el ámbito congelado de Clase/Capítulo 87;
- carácter de apoyo a decisión, no vinculante;
- separación funcional entre recuperación histórica, recuperación normativa y LLM local;
- unidad de observación/análisis: SERIE de DAM;
- unidad de agrupamiento/dependencia: DAM;
- unidad de consulta: SERIE / descripción comercial normalizada;
- unidad de salida: ranking histórico Top-k y Top-3 fijo;
- revisión experta fuera del flujo automático;
- límites de alcance necesarios para impedir generalización o corrección jurídica no demostradas.

### 4. Exclusiones del bloque

B01 no puede contener resultados, métricas, cifras H100, resultados EXP-11A/11B/12/Grupo 3, inferencia estadística, relaciones causales, novelty final, gap final, corrección jurídica, accuracy global del sistema, generalización empírica fuera del alcance evaluado, ni detalle técnico reservado a Methods 3.2–3.9.

Los claims principales utilizables son `C01`, `C02` y `C03`; `C07` puede utilizarse solo como principio metodológico de agrupamiento/dependencia, sin anticipar resultados inferenciales. Los claims prohibidos y condicionales de la matriz permanecen sin cambios.

### 5. Dictamen

```text
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ARTIFACT = article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### 1. Entry state

```text
ARTICLE_SNAPSHOT_AT_GATE = b6a33e187fc5cbd2eec6fa68a6a99bc7ff4b5f74
SRC03_LIVE_BRANCH_HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
PHASE_0 = CLOSED / APPROVED
0C = CLOSED / APPROVED / FROZEN
0D = CLOSED / APPROVED / FROZEN
MWDP_VERSION = MWDP_V1.0
MWDP_STATE = FROZEN
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

**FILES READ:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`; `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; and the living `SRC-03` on `docs/plan-maestro-temporal-2026-08-31`.

### 2. Living experimental-state check

Living `SRC-03` at snapshot `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6` states:

```text
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
GROUP3 = NOT_STARTED
```

Therefore, no current Group-3A/3B closures exist at this cutoff. HE2/HE5 and final Group-3 inference remain pending. This does not block `Methods B01`, because B01 is limited to design, scope, and units and does not report Group-3 results or inference.

### 3. Authorized block

```text
PHASE_1 = OPENED
METHODS_B01 = READY_FOR_DRAFTING
METHODS_B01_TITLE = Design, scope, and units
MANUSCRIPT_DRAFTING = AUTHORIZED_FOR_METHODS_B01_ONLY
OTHER_METHODS_BLOCKS = NOT_AUTHORIZED_YET
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

B01 may establish only the applied offline experimental-pilot design; the frozen NANDINA Class/Chapter-87 evaluation scope; non-binding decision-support status; functional separation of historical retrieval, normative retrieval, and the local LLM; the SERIE observation/analysis unit; DAM grouping/dependence unit; SERIE/normalized-commercial-description query unit; historical Top-k/fixed-Top-3 output unit; expert review outside the automated flow; and scope boundaries needed to prevent unsupported generalization or legal-correctness claims.

### 4. Block exclusions

B01 must not contain results, metrics, H100 figures, EXP-11A/11B/12/Group-3 results, statistical inference, causal claims, final novelty, final gap, legal correctness, overall system accuracy, empirical generalization beyond the evaluated scope, or technical detail reserved for Methods 3.2–3.9.

The main usable claims are `C01`, `C02`, and `C03`; `C07` may be used only as a methodological grouping/dependence principle without anticipating inferential results. All conditional and prohibited claims remain unchanged.

### 5. Verdict

```text
PHASE_1_METHODS_ENTRY_GATE = PASS
METHODS_B01 = READY_FOR_DRAFTING
NEXT_ACTOR = DRAFTING_AI
NEXT_ARTIFACT = article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
