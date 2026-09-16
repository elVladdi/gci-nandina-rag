# Fase 1 — Methods B01 — Informe de ejecución V01

## Español

### 1. Onboarding y estado operativo

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`); `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`; `SRC-03` vivo; y `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md`.

**FASE ACTIVA:** `PHASE_1 = OPENED`.

**ESTADO DEL BLOQUE ASIGNADO:** `METHODS_B01 = READY_FOR_DRAFTING`.

**REDACCIÓN AUTORIZADA:** SÍ, exclusivamente `Methods B01 — Design, scope, and units`.

**DECISIONES CONGELADAS RELEVANTES:** separación funcional entre recuperación histórica, recuperación normativa y LLM local; Top-3 fijo antes de generación; SERIE como unidad de análisis; DAM como unidad de agrupamiento cuando existe dependencia; piloto offline y no vinculante; alcance empírico en Capítulo 87; configurabilidad arquitectónica distinta de generalización empírica; `MWDP_V1.0` como protocolo acumulativo obligatorio.

**CLAIMS AUTORIZADOS RELEVANTES:** `C01`, `C02`, `C03` y `C07` exclusivamente como principio metodológico de agrupamiento/dependencia.

**CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:** no se utilizaron `C09`, `C10`, `C11`, `C12`, `C13`, `C16`, `C18`, `C20` ni resultados/inferencias de Grupo 3. `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`.

**FUENTES EXTERNAS QUE DEBEN VERIFICARSE:** ninguna. B01 se sustenta íntegramente en las fuentes metodológicas gobernantes y no incorpora literatura externa.

**BLOQUEOS O CONTRADICCIONES DETECTADOS:** `ARTICLE_STATUS.md` y `PHASE_1_METHODS_ENTRY_GATE.md` indican que el `SRC-03` vivo registra cierres de Grupo 3A/3B, mientras que el `SRC-03` efectivamente leído en `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6` conserva `GROUP3 = NOT_STARTED` y `G3-F01` como ficha prospectiva no autorizada. La discrepancia no se reconcilió ni se usó para redactar B01. Es no bloqueante para este bloque porque B01 no utiliza resultados ni inferencias de Grupo 3.

### 2. Snapshots realmente leídos

- `article/main-manuscript HEAD: 3e2fe0e97d5c5fa132e2465f6091cd5b55277380`
- `article/START_HERE.md: e7ac1dd0de37e9cf78e0b7bb3a720dbde69561be`
- `article/README.md: 8b11aed826d8c4985814f62e61a6554b8d77fa4a`
- `article/ARTICLE_STATUS.md: abdf2ca7d165836cd26c6513e1522c6307cd67b6`
- `article/ARTICLE_WRITING_PLAN.md: e69da61e52d8dbb4c74f6e4a210ec5d06387e767`
- `article/DECISIONS.md: 895992ce2c13819b7ebeb69234d118654a714dea`
- `article/SOURCE_REGISTRY.md: d32fa718933b97c0a1b95ff528b1cbd74cc7f44c`
- `article/CLAIM_EVIDENCE_MATRIX.md: ceaa754ef0012862f4952b378dd4a12dfb6e33f7`
- `article/STYLE_GUIDE.md: cac5c562a30da80db61da7a335381f21741f2d69`
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md: 34fbf6c8d905da6934cc518fba0c4cc9d4cc1b7e`
- `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md: 2cbaa9e809fd067d1c8e40e97e23480ba3ee6d05`
- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md: 52c45948bbc085a25faf4df850ae15e6ca682d17`
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md: 21bc5de58af3ea0f5429f1f11da130762185f779`
- `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md: 3df54c517de4263659d62bb3a6f8e2afa34e319f`
- `SRC-03 branch HEAD: f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`
- `SRC-03 Plan Maestro blob: adcd9be3aaa9c13929575d6f348fa6f9693bccbf`
- `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md: cf2004bdb5824535cbab0a5ccefedaab2f3b6bc6`

### 3. Alcance de la redacción ejecutada

Se redactó únicamente la subsección `3.1 Design, scope, and units`. El texto define el carácter aplicado y offline del piloto, su alcance en Capítulo 87, su condición no vinculante de apoyo a decisión, la revisión experta fuera del flujo automático, la separación funcional entre las tres capas del sistema y las unidades de análisis, agrupamiento, consulta y salida. No se incorporaron resultados, métricas, cifras experimentales, inferencia estadística, causalidad, novelty, gap final, detalle técnico reservado a Methods 3.2–3.9 ni literatura externa.

### 4. Artefactos generados

- `article/sections/methods/Methods_B01_V01.md` — bloque independiente bilingüe.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md` — primer master acumulativo candidato, que contiene únicamente B01.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.docx` — Word acumulativo candidato bilingüe, editable y de layout neutral/reversible.
- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V01.md` — este informe de ejecución.

La creación del master se clasifica como `INITIAL_MASTER_CANDIDATE_INITIALIZATION`. No se creó ningún `ARTICLE_MASTER_V001.*`.

### 5. QA MWDP

- No se utilizaron citas externas: `CITATION_COMMENT_COVERAGE = 0/0`.
- No existen referencias que requieran `ACCESS_RECHECK_REQUIRED`.
- La versión inglesa y el espejo español se verificaron para conservar alcance, fuerza epistémica, arquitectura, unidades y límites.
- El Word se generó sin maquetación KBS supuesta, sin Mendeley y sin campos bibliográficos simulados.
- El conteo del texto principal inglés de B01 es `264` palabras, excluyendo headings y metadatos.

### 6. Checklist obligatorio

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V01
SOURCE_SNAPSHOT(S) = [3e2fe0e97d5c5fa132e2465f6091cd5b55277380; e7ac1dd0de37e9cf78e0b7bb3a720dbde69561be; 8b11aed826d8c4985814f62e61a6554b8d77fa4a; abdf2ca7d165836cd26c6513e1522c6307cd67b6; e69da61e52d8dbb4c74f6e4a210ec5d06387e767; 895992ce2c13819b7ebeb69234d118654a714dea; d32fa718933b97c0a1b95ff528b1cbd74cc7f44c; ceaa754ef0012862f4952b378dd4a12dfb6e33f7; cac5c562a30da80db61da7a335381f21741f2d69; 34fbf6c8d905da6934cc518fba0c4cc9d4cc1b7e; 2cbaa9e809fd067d1c8e40e97e23480ba3ee6d05; 52c45948bbc085a25faf4df850ae15e6ca682d17; 21bc5de58af3ea0f5429f1f11da130762185f779; 3df54c517de4263659d62bb3a6f8e2afa34e319f; f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6; adcd9be3aaa9c13929575d6f348fa6f9693bccbf; cf2004bdb5824535cbab0a5ccefedaab2f3b6bc6]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md + .docx
MASTER_INITIALIZATION = INITIAL_MASTER_CANDIDATE_INITIALIZATION
ENGLISH_MAIN_TEXT_WORD_COUNT = 264
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = DRAFTING / AWAITING_INTERNAL_REVIEW
```

---

## English

### 1. Onboarding and operational state

**FILES READ:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`); `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`; the living `SRC-03`; and `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md`.

**ACTIVE PHASE:** `PHASE_1 = OPENED`.

**ASSIGNED BLOCK STATUS:** `METHODS_B01 = READY_FOR_DRAFTING`.

**DRAFTING AUTHORIZED:** YES, exclusively for `Methods B01 — Design, scope, and units`.

**RELEVANT FROZEN DECISIONS:** functional separation among historical retrieval, normative retrieval, and the local LLM; fixed Top-3 before generation; SERIES as analysis unit; DAM as grouping unit when dependence exists; offline, non-binding pilot; Chapter-87 empirical scope; architectural configurability distinct from empirical generalization; and `MWDP_V1.0` as the binding cumulative protocol.

**RELEVANT AUTHORIZED CLAIMS:** `C01`, `C02`, `C03`, and `C07` only as a methodological grouping/dependence principle.

**RELEVANT PROHIBITED OR PENDING CLAIMS:** `C09`, `C10`, `C11`, `C12`, `C13`, `C16`, `C18`, `C20`, and Group-3 results/inferences were not used. `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`.

**EXTERNAL SOURCES REQUIRING VERIFICATION:** none. B01 is fully supported by governing methodological sources and introduces no external literature.

**BLOCKERS OR CONTRADICTIONS DETECTED:** `ARTICLE_STATUS.md` and `PHASE_1_METHODS_ENTRY_GATE.md` state that the living `SRC-03` records Group-3A/3B closures, whereas the `SRC-03` actually read at `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6` retains `GROUP3 = NOT_STARTED` and `G3-F01` as a prospective, unauthorized record. The discrepancy was neither reconciled nor used in B01. It is non-blocking for this block because B01 uses no Group-3 result or inference.

### 2. Source snapshots actually read

- `article/main-manuscript HEAD: 3e2fe0e97d5c5fa132e2465f6091cd5b55277380`
- `article/START_HERE.md: e7ac1dd0de37e9cf78e0b7bb3a720dbde69561be`
- `article/README.md: 8b11aed826d8c4985814f62e61a6554b8d77fa4a`
- `article/ARTICLE_STATUS.md: abdf2ca7d165836cd26c6513e1522c6307cd67b6`
- `article/ARTICLE_WRITING_PLAN.md: e69da61e52d8dbb4c74f6e4a210ec5d06387e767`
- `article/DECISIONS.md: 895992ce2c13819b7ebeb69234d118654a714dea`
- `article/SOURCE_REGISTRY.md: d32fa718933b97c0a1b95ff528b1cbd74cc7f44c`
- `article/CLAIM_EVIDENCE_MATRIX.md: ceaa754ef0012862f4952b378dd4a12dfb6e33f7`
- `article/STYLE_GUIDE.md: cac5c562a30da80db61da7a335381f21741f2d69`
- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md: 34fbf6c8d905da6934cc518fba0c4cc9d4cc1b7e`
- `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md: 2cbaa9e809fd067d1c8e40e97e23480ba3ee6d05`
- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md: 52c45948bbc085a25faf4df850ae15e6ca682d17`
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md: 21bc5de58af3ea0f5429f1f11da130762185f779`
- `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md: 3df54c517de4263659d62bb3a6f8e2afa34e319f`
- `SRC-03 branch HEAD: f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`
- `SRC-03 Plan Maestro blob: adcd9be3aaa9c13929575d6f348fa6f9693bccbf`
- `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS.md: cf2004bdb5824535cbab0a5ccefedaab2f3b6bc6`

### 3. Drafting scope executed

Only subsection `3.1 Design, scope, and units` was drafted. The text defines the applied offline pilot, Chapter-87 scope, non-binding decision-support status, expert review outside the automated flow, the functional separation among the system layers, and the analysis, grouping, query, and output units. No results, metrics, experimental figures, statistical inference, causal language, novelty, final gap, technical detail reserved for Methods 3.2–3.9, or external literature were introduced.

### 4. Generated artifacts

- `article/sections/methods/Methods_B01_V01.md` — independent bilingual block.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md` — first cumulative candidate master containing only B01.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.docx` — bilingual, editable, neutral/reversible cumulative candidate Word master.
- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V01.md` — this execution report.

Master creation is classified as `INITIAL_MASTER_CANDIDATE_INITIALIZATION`. No `ARTICLE_MASTER_V001.*` artifact was created.

### 5. MWDP QA

- No external citations were used: `CITATION_COMMENT_COVERAGE = 0/0`.
- No reference requires `ACCESS_RECHECK_REQUIRED`.
- English and Spanish were checked for equivalent scope, epistemic strength, architecture, units, and boundaries.
- The Word candidate was generated without assumed KBS typesetting, Mendeley, or simulated bibliography fields.
- The English B01 main-text count is `264` words, excluding headings and metadata.

### 6. Mandatory checklist

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V01
SOURCE_SNAPSHOT(S) = [3e2fe0e97d5c5fa132e2465f6091cd5b55277380; e7ac1dd0de37e9cf78e0b7bb3a720dbde69561be; 8b11aed826d8c4985814f62e61a6554b8d77fa4a; abdf2ca7d165836cd26c6513e1522c6307cd67b6; e69da61e52d8dbb4c74f6e4a210ec5d06387e767; 895992ce2c13819b7ebeb69234d118654a714dea; d32fa718933b97c0a1b95ff528b1cbd74cc7f44c; ceaa754ef0012862f4952b378dd4a12dfb6e33f7; cac5c562a30da80db61da7a335381f21741f2d69; 34fbf6c8d905da6934cc518fba0c4cc9d4cc1b7e; 2cbaa9e809fd067d1c8e40e97e23480ba3ee6d05; 52c45948bbc085a25faf4df850ae15e6ca682d17; 21bc5de58af3ea0f5429f1f11da130762185f779; 3df54c517de4263659d62bb3a6f8e2afa34e319f; f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6; adcd9be3aaa9c13929575d6f348fa6f9693bccbf; cf2004bdb5824535cbab0a5ccefedaab2f3b6bc6]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md + .docx
MASTER_INITIALIZATION = INITIAL_MASTER_CANDIDATE_INITIALIZATION
ENGLISH_MAIN_TEXT_WORD_COUNT = 264
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = DRAFTING / AWAITING_INTERNAL_REVIEW
```
