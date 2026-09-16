# Fase 1 — Methods B01 — Informe de revisión V02

## Español

### 1. Onboarding y estado operativo

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`, íntegro); `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`; `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V01.md`; `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V01.md`; `article/sections/methods/Methods_B01_V01.md`; `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md`; el `SRC-03` vivo; y `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V02.md`.

**FASE ACTIVA:** `PHASE_1 = OPENED`.

**ESTADO DEL BLOQUE ASIGNADO:** `METHODS_B01 = REVISION_REQUIRED`.

**REDACCIÓN AUTORIZADA:** SÍ, exclusivamente para la revisión V02 de `Methods B01 — Design, scope, and units`.

**DECISIONES CONGELADAS RELEVANTES:** separación funcional de ranking histórico, evidencia normativa y explicación con LLM local; Top-3 fijo e inmutable antes de la explicación; ausencia de inserción/eliminación/sustitución/reordenamiento y de feedback generativo; SERIE como unidad de análisis; DAM como unidad de agrupamiento cuando exista dependencia; apoyo a decisión no vinculante; revisión experta fuera del flujo automático; alcance empírico restringido al Capítulo 87; `MWDP_V1.0` como protocolo obligatorio.

**CLAIMS AUTORIZADOS RELEVANTES:** `C01`, `C02`, `C03` y `C07` únicamente dentro del alcance definido por el prompt.

**CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:** no se utilizó `C15`; no se utilizó `C16`, `C18` ni ningún claim de resultados, inferencia o Grupo 3. `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`; `GROUP3 = NOT_STARTED`.

**FUENTES EXTERNAS QUE DEBEN VERIFICARSE:** ninguna; la revisión no incorpora literatura externa ni citas.

**BLOQUEOS O CONTRADICCIONES DETECTADOS:** ninguno para B01 V02. La discrepancia editorial previa sobre Grupo 3 fue corregida por la IA Gestora (`B01-M04 = CLOSED_BY_IA_GESTORA`) y el `SRC-03` vivo confirma `GROUP3 = NOT_STARTED`.

### 2. Correcciones ejecutadas

- **B01-M01 — ADDRESSED.** Se eliminó el lenguaje de gobernanza interna y el alcance se expresa mediante una formulación científica autosuficiente.
- **B01-M02 — ADDRESSED.** La primera aparición inglesa define `Declaración Aduanera de Mercancías (DAM; customs declaration)`; el espejo español conserva `Declaración Aduanera de Mercancías (DAM)`.
- **B01-M03 — ADDRESSED.** Se eliminó el claim positivo de configurabilidad y se conserva únicamente el límite de que la evaluación no establece generalización empírica fuera de Capítulo 87.
- **B01-M05 — ADDRESSED.** La sección abre con la arquitectura auditable de apoyo a decisión y su desacoplamiento funcional; NANDINA Capítulo 87 aparece después como entorno de prueba regulatorio controlado. No se añadió novelty, superioridad, ausencia de prior art ni generalización.

### 3. Alcance de la revisión

Se revisó únicamente `Methods B01`. La V02 conserva el piloto experimental aplicado y offline, el carácter no vinculante del apoyo a decisión, la revisión experta fuera del flujo automático y las unidades de observación/análisis, agrupamiento, consulta y salida. No incorpora resultados, cifras, métricas, inferencia, causalidad, literatura externa ni contenido reservado a B02–B09.

### 4. Artefactos generados

- `article/sections/methods/Methods_B01_V02.md` — bloque independiente bilingüe revisado.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md` — candidato acumulativo V02 que contiene únicamente B01 revisado.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.docx` — Word candidato bilingüe, editable y neutral/reversible, sin citas ni comentarios de cita.
- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V02.md` — este informe de revisión.

Los artefactos V01 se preservan sin sobrescritura. No se creó `ARTICLE_MASTER_V001.*` y no se avanzó a B02.

### 5. QA MWDP

- `CITATION_COMMENT_COVERAGE = 0/0`; no existen citas que requieran comentarios de auditoría.
- `ACCESS_RECHECK_REQUIRED = NONE`.
- Se verificó equivalencia semántica EN–ES para arquitectura, límites, unidades y fuerza epistémica.
- El Word reproduce el contenido científico del master candidato V02 y mantiene layout neutral/reversible, sin Mendeley ni campos bibliográficos simulados.
- El texto principal inglés de B01 contiene `253` palabras, excluyendo headings y metadatos.

---

## English

### 1. Onboarding and operational state

**FILES READ:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`, in full); `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`; `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V01.md`; `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V01.md`; `article/sections/methods/Methods_B01_V01.md`; `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md`; the living `SRC-03`; and `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V02.md`.

**ACTIVE PHASE:** `PHASE_1 = OPENED`.

**ASSIGNED BLOCK STATE:** `METHODS_B01 = REVISION_REQUIRED`.

**DRAFTING AUTHORIZED:** YES, exclusively for the V02 revision of `Methods B01 — Design, scope, and units`.

**RELEVANT FROZEN DECISIONS:** functional separation of historical ranking, normative evidence, and local-LLM explanation; immutable fixed Top-3 before explanation; no insertion/deletion/substitution/reordering and no generative feedback; SERIES as analysis unit; DAM as grouping unit when dependence exists; non-binding decision support; expert review outside the automated flow; empirical scope restricted to Chapter 87; `MWDP_V1.0` as binding protocol.

**RELEVANT AUTHORIZED CLAIMS:** `C01`, `C02`, `C03`, and `C07`, only within the scope defined by the prompt.

**RELEVANT PROHIBITED OR PENDING CLAIMS:** `C15` was not used; `C16`, `C18`, and all result, inferential, or Group-3 claims were not used. `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`; `GROUP3 = NOT_STARTED`.

**EXTERNAL SOURCES REQUIRING VERIFICATION:** none; the revision introduces no external literature or citations.

**BLOCKERS OR CONTRADICTIONS DETECTED:** none for B01 V02. The previous editorial-control discrepancy concerning Group 3 was corrected by the Managing AI (`B01-M04 = CLOSED_BY_IA_GESTORA`), and living `SRC-03` confirms `GROUP3 = NOT_STARTED`.

### 2. Corrections implemented

- **B01-M01 — ADDRESSED.** Internal governance language was removed and the scope is stated in self-contained manuscript-facing scientific terms.
- **B01-M02 — ADDRESSED.** The first English occurrence defines `Declaración Aduanera de Mercancías (DAM; customs declaration)`; the Spanish mirror retains `Declaración Aduanera de Mercancías (DAM)`.
- **B01-M03 — ADDRESSED.** The positive configurability claim was removed; only the boundary that the evaluation does not establish empirical generalization beyond Chapter 87 is retained.
- **B01-M05 — ADDRESSED.** The subsection now opens with the auditable decision-support architecture and its functional decoupling; NANDINA Chapter 87 is introduced afterward as the controlled regulatory testbed. No novelty, superiority, prior-art absence, or generalization claim was added.

### 3. Revision scope

Only `Methods B01` was revised. V02 preserves the applied offline experimental pilot, non-binding decision-support status, expert review outside the automated workflow, and the observation/analysis, grouping, query, and output units. It introduces no results, numbers, metrics, inference, causality, external literature, or content reserved for B02–B09.

### 4. Generated artifacts

- `article/sections/methods/Methods_B01_V02.md` — revised standalone bilingual block.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md` — V02 cumulative candidate containing only revised B01.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.docx` — bilingual editable candidate Word master with neutral/reversible layout and no citations or citation comments.
- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V02.md` — this revision report.

V01 artifacts were preserved without overwrite. No `ARTICLE_MASTER_V001.*` was created, and B02 was not started.

### 5. MWDP QA

- `CITATION_COMMENT_COVERAGE = 0/0`; there are no citations requiring audit comments.
- `ACCESS_RECHECK_REQUIRED = NONE`.
- EN–ES semantic equivalence was checked for architecture, boundaries, units, and epistemic strength.
- The Word candidate reproduces the scientific content of the V02 master candidate and preserves a neutral/reversible layout with no Mendeley or simulated bibliographic fields.
- The English B01 main text contains `253` words, excluding headings and metadata.

---

## Checklist / Lista de control

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V02
B01_M01 = ADDRESSED
B01_M02 = ADDRESSED
B01_M03 = ADDRESSED
B01_M05 = ADDRESSED
SOURCE_SNAPSHOT(S) = [ae4cf9b7876759234bfbeff4560dcdb4a2644de2; e7ac1dd0de37e9cf78e0b7bb3a720dbde69561be; 8b11aed826d8c4985814f62e61a6554b8d77fa4a; 4deff065072dd020236b0b5dc5aa3cab139c4359; e69da61e52d8dbb4c74f6e4a210ec5d06387e767; 895992ce2c13819b7ebeb69234d118654a714dea; d32fa718933b97c0a1b95ff528b1cbd74cc7f44c; ceaa754ef0012862f4952b378dd4a12dfb6e33f7; cac5c562a30da80db61da7a335381f21741f2d69; 34fbf6c8d905da6934cc518fba0c4cc9d4cc1b7e; 2cbaa9e809fd067d1c8e40e97e23480ba3ee6d05; 52c45948bbc085a25faf4df850ae15e6ca682d17; 21bc5de58af3ea0f5429f1f11da130762185f779; 2ba49f154cc9fa927a0d10e50721ff2117a0c93c; 9f463c6f14d7480670f23b2eb3d0db5dda4888eb; 723be86367be1a2922769cd1dc4c08e27f038fab; 9c1fdb4c077ed67078db106c85076b9423bffd20; 5f81f5601c27a5308726eae21f8d0ffd6b674179; f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6; adcd9be3aaa9c13929575d6f348fa6f9693bccbf; 4f969137b00f927af035ecb8c282eab2defd653a]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
POSITIONING_ORDER = GENERAL_ARCHITECTURE_FIRST / NANDINA_CH87_AS_TESTBED_SECOND
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md + .docx
ENGLISH_MAIN_TEXT_WORD_COUNT = 253
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```
