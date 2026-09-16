# Fase 1 — Methods B01 — Informe de revisión V03

## Español

### 1. Onboarding y estado operativo

**ARCHIVOS LEÍDOS:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`, íntegro); `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`; `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V02.md`; `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V02.md`; `article/sections/methods/Methods_B01_V02.md`; `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md`; el `SRC-03` vivo; y `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V03.md`.

**FASE ACTIVA:** `PHASE_1 = OPENED`.

**ESTADO DEL BLOQUE ASIGNADO:** `METHODS_B01 = REVISION_REQUIRED`.

**REDACCIÓN AUTORIZADA:** SÍ, exclusivamente para la revisión V03 de `Methods B01 — Design, scope, and units`.

**DECISIONES CONGELADAS RELEVANTES:** recuperación histórica como generador y ranking de candidatos; Top-3 fijo antes de recuperación normativa y generación; recuperación normativa como evidencia documental sin reranking; LLM local limitado a explicación downstream sin inserción, eliminación, sustitución, reordenamiento ni feedback; evaluación organizada por función; SERIE como unidad de análisis; DAM como unidad de agrupamiento cuando existe dependencia; apoyo a decisión no vinculante; revisión experta fuera del flujo automático; `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`; `MWDP_V1.0` y `SPCCR_V1.0` como reglas acumulativas vigentes.

**CLAIMS AUTORIZADOS RELEVANTES:** `C01`, `C02`, `C03`, `C07` y `C15`, este último únicamente como propiedad acotada de diseño/configurabilidad/replicabilidad.

**CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:** no se utilizó `C16`, `C18`, `C10`, `C11` ni ningún claim de resultados o inferencia de Grupo 3. `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`; `GROUP3 = NOT_STARTED`.

**FUENTES EXTERNAS QUE DEBEN VERIFICARSE:** ninguna; V03 no incorpora literatura externa ni citas.

**BLOQUEOS O CONTRADICCIONES DETECTADOS:** ninguno para B01 V03. El `SRC-03` vivo confirma `GROUP3 = NOT_STARTED`. La diferencia histórica entre el corte congelado 0A-02 y el estado experimental vivo no afecta este bloque porque V03 no incorpora resultados ni inferencias experimentales posteriores.

### 2. Correcciones ejecutadas

- **B01-M06 — ADDRESSED.** Se redujeron nominalizaciones y cadenas abstractas. El texto ahora identifica explícitamente qué recibe cada componente, qué hace, qué produce y qué no puede modificar.
- **B01-M07 — ADDRESSED.** Se hizo visible el contrato funcional completo: la recuperación histórica fija el ranking y el Top-3; la recuperación normativa obtiene evidencia para esos candidatos sin alterar el ranking; el LLM recibe candidatos más evidencia y produce la explicación bajo restricciones; la evaluación trata ranking, evidencia y explicación como funciones diferenciadas.
- **B01-M08 — ADDRESSED.** Se explicita que una nueva instancia puede emplear un banco/dataset histórico etiquetado, un universo de clases objetivo y un corpus documental o normativo definidos para el estudio o replicación, manteniendo el mismo contrato funcional. La formulación delimita expresamente esta propiedad como configurabilidad/replicabilidad de diseño y no como generalización empírica.
- **B01-M01, B01-M02, B01-M03 y B01-M05 — PRESERVED_CLOSED.** No se reintrodujo lenguaje de gobernanza interna; DAM mantiene su definición administrativa en inglés; configurabilidad y generalización permanecen separadas; y el método general precede al testbed NANDINA Capítulo 87.

### 3. Alcance científico de V03

La sección presenta primero el método general y su contrato funcional, después la frontera de configurabilidad y finalmente la instancia evaluada en NANDINA Capítulo 87. Conserva el piloto aplicado y offline, el carácter no vinculante, la revisión experta fuera del flujo automático y las unidades de observación/análisis, agrupamiento, consulta y salida.

No se incorporaron resultados, cifras, métricas, inferencia estadística, causalidad, `FINAL_GAP`, novelty final, superioridad, ausencia universal de prior art, literatura externa, EXP-11B, Grupo 3 ni contenido técnico de B02–B09.

### 4. Artefactos generados

- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V03.md` — este informe bilingüe.
- `article/sections/methods/Methods_B01_V03.md` — bloque independiente bilingüe revisado.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md` — candidato V03 que contiene únicamente B01 revisado.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.docx` — Word candidato bilingüe, editable y neutral/reversible, sin citas ni comentarios de cita.

Los artefactos V01 y V02 permanecen sin sobrescritura. No se creó `ARTICLE_MASTER_V001.*` y no se avanzó a B02.

### 5. QA de prosa, equivalencia y Word

- `ABSTRACTION_DENSITY = ACCEPTABLE`.
- `AGENT_ACTION_OBJECT_CLARITY = PASS`.
- `NOMINALIZATION_OVERLOAD = ABSENT`.
- `PROCESS_RELATIONSHIPS_EXPLICIT = PASS`.
- `CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS`.
- `EN_ES_SEMANTIC_EQUIVALENCE = PASS` para funciones, restricciones, configurabilidad, alcance y unidades.
- `CITATION_COMMENT_COVERAGE = 0/0`; no existen citas que requieran comentarios.
- `ACCESS_RECHECK_REQUIRED = NONE`.
- El Word reproduce el contenido científico del master candidato V03 y conserva el layout bilingüe neutral/reversible, sin Mendeley ni campos bibliográficos simulados.
- El texto principal inglés de B01 contiene `353` palabras, excluyendo headings y metadatos.

---

## English

### 1. Onboarding and operational state

**FILES READ:** `article/START_HERE.md`; `article/README.md`; `article/ARTICLE_STATUS.md`; `article/ARTICLE_WRITING_PLAN.md`; `article/DECISIONS.md`; `article/SOURCE_REGISTRY.md`; `article/CLAIM_EVIDENCE_MATRIX.md`; `article/STYLE_GUIDE.md`; `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (`MWDP_V1.0`, in full); `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`; `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`; `article/positioning/0D_EDITORIAL_ARCHITECTURE_AND_WRITING_GOVERNANCE_FROZEN.md`; `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`; `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`; `article/reviews/PHASE_1_METHODS_ENTRY_GATE.md`; `article/reviews/1_METHODS_B01_INTERNAL_REVIEW_V02.md`; `article/reviews/1_METHODS_B01_AUTHOR_REVIEW_V02.md`; `article/sections/methods/Methods_B01_V02.md`; `article/manuscript/ARTICLE_MASTER_CANDIDATE_V02.md`; the living `SRC-03`; and `article/prompts/1_METHODS_B01_DESIGN_SCOPE_UNITS_REVISION_V03.md`.

**ACTIVE PHASE:** `PHASE_1 = OPENED`.

**ASSIGNED BLOCK STATE:** `METHODS_B01 = REVISION_REQUIRED`.

**DRAFTING AUTHORIZED:** YES, exclusively for the V03 revision of `Methods B01 — Design, scope, and units`.

**RELEVANT FROZEN DECISIONS:** historical retrieval generates/ranks candidates; the Top-3 is fixed before normative retrieval and generation; normative retrieval supplies documentary evidence without reranking; the local LLM is downstream explanation only with no insertion, deletion, substitution, reordering, or classification feedback; evaluation is organized by function; SERIES is the analysis unit; DAM is the grouping unit when dependence exists; decision support is non-binding; expert review remains outside the automated flow; `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`; `MWDP_V1.0` and `SPCCR_V1.0` remain binding cumulative rules.

**RELEVANT AUTHORIZED CLAIMS:** `C01`, `C02`, `C03`, `C07`, and `C15`, with C15 used only as a bounded design/configurability/replicability property.

**RELEVANT PROHIBITED OR PENDING CLAIMS:** `C16`, `C18`, `C10`, `C11`, and all Group-3 result/inferential claims were not used. `FINAL_GAP = NOT_DEFINED`; `NOVELTY = NOT_DECLARED`; `GROUP3 = NOT_STARTED`.

**EXTERNAL SOURCES REQUIRING VERIFICATION:** none; V03 adds no external literature or citations.

**BLOCKERS OR CONTRADICTIONS DETECTED:** none for B01 V03. Living `SRC-03` confirms `GROUP3 = NOT_STARTED`. Historical differences between the frozen 0A-02 cutoff and the living experimental state do not affect this block because V03 introduces no later experimental result or inference.

### 2. Corrections implemented

- **B01-M06 — ADDRESSED.** Stacked abstractions and nominalizations were reduced. The text now states explicitly what each component receives, does, produces, and cannot modify.
- **B01-M07 — ADDRESSED.** The complete functional contract is visible: historical retrieval fixes the ranking and Top-3; normative retrieval obtains evidence for those candidates without changing the ranking; the LLM receives candidates plus evidence and produces the explanation under explicit restrictions; evaluation treats ranking, evidence, and explanation as distinct functions.
- **B01-M08 — ADDRESSED.** The text states that a new instance may use a study- or replication-specific labeled historical dataset/bank, target class universe, and documentary/normative corpus while preserving the same functional contract. This is explicitly bounded as design configurability/replicability, not empirical generalization.
- **B01-M01, B01-M02, B01-M03, and B01-M05 — PRESERVED_CLOSED.** No internal-governance wording was reintroduced; DAM remains properly defined in English; configurability remains distinct from generalization; and the general method precedes the NANDINA Chapter-87 testbed.

### 3. Scientific scope of V03

The subsection presents the general method and functional contract first, the configurability boundary second, and the NANDINA Chapter-87 empirical instance third. It preserves the applied offline pilot, non-binding decision-support status, expert review outside the automated flow, and the observation/analysis, grouping, query, and output units.

No results, figures, concrete metrics, statistical inference, causality, `FINAL_GAP`, final novelty, superiority, universal prior-art absence, external literature, EXP-11B, Group-3 results, or B02–B09 technical detail were introduced.

### 4. Generated artifacts

- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V03.md` — this bilingual report.
- `article/sections/methods/Methods_B01_V03.md` — revised standalone bilingual block.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md` — V03 candidate containing only revised B01.
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.docx` — bilingual editable candidate Word master with neutral/reversible layout and no citations or citation comments.

V01 and V02 artifacts remain preserved without overwrite. No `ARTICLE_MASTER_V001.*` was created, and B02 was not started.

### 5. Prose, equivalence, and Word QA

- `ABSTRACTION_DENSITY = ACCEPTABLE`.
- `AGENT_ACTION_OBJECT_CLARITY = PASS`.
- `NOMINALIZATION_OVERLOAD = ABSENT`.
- `PROCESS_RELATIONSHIPS_EXPLICIT = PASS`.
- `CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS`.
- `EN_ES_SEMANTIC_EQUIVALENCE = PASS` for functions, restrictions, configurability, scope, and units.
- `CITATION_COMMENT_COVERAGE = 0/0`.
- `ACCESS_RECHECK_REQUIRED = NONE`.
- The Word candidate reproduces the V03 master candidate's scientific content and preserves the neutral/reversible bilingual layout with no Mendeley or simulated bibliographic fields.
- The English B01 main text contains `353` words, excluding headings and metadata.

---

## Checklist / Lista de control

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = Methods_B01
BLOCK_REVISION = V03
B01_M06 = ADDRESSED
B01_M07 = ADDRESSED
B01_M08 = ADDRESSED
B01_M01_M02_M03_M05 = PRESERVED_CLOSED
SOURCE_SNAPSHOT(S) = [article/main-manuscript@706df9fc12d40accd05f3910540ad5018fce34f8; START_HERE=e7ac1dd0de37e9cf78e0b7bb3a720dbde69561be; README=8b11aed826d8c4985814f62e61a6554b8d77fa4a; ARTICLE_STATUS=e9c8d0183533c1c3e3a4811b73326b707ca550e7; ARTICLE_WRITING_PLAN=e69da61e52d8dbb4c74f6e4a210ec5d06387e767; DECISIONS=895992ce2c13819b7ebeb69234d118654a714dea; SOURCE_REGISTRY=d32fa718933b97c0a1b95ff528b1cbd74cc7f44c; CLAIM_EVIDENCE_MATRIX=ceaa754ef0012862f4952b378dd4a12dfb6e33f7; STYLE_GUIDE=cac5c562a30da80db61da7a335381f21741f2d69; MWDP=34fbf6c8d905da6934cc518fba0c4cc9d4cc1b7e; SPCCR=0b48c86adc612077b98db82713f1a2af4e1e3231; 0C_POSITIONING=6b8a8a1b6c093c259ffc0e04c8e1038a4f41da6c; 0D_FROZEN=2cbaa9e809fd067d1c8e40e97e23480ba3ee6d05; 0A01=52c45948bbc085a25faf4df850ae15e6ca682d17; 0A02=21bc5de58af3ea0f5429f1f11da130762185f779; METHODS_ENTRY_GATE=2ba49f154cc9fa927a0d10e50721ff2117a0c93c; B01_INTERNAL_REVIEW_V02=14bfa628701ff43204affb26e80b541d2f06d029; B01_AUTHOR_REVIEW_V02=aa1da36a8592b589450ed78b284f69ef1f61561d; Methods_B01_V02=bca3345651780c14f4ed9cd2ced347ac25da3bfc; ARTICLE_MASTER_CANDIDATE_V02_MD=0e498a15fa54fd7e35f4dd62ea626cc2df1729fd; V03_PROMPT=96c1b0adc840902ce0627ab54506184fab585fb4; SRC03_HEAD=f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6; SRC03_BLOB=adcd9be3aaa9c13929575d6f348fa6f9693bccbf]
AUTHORIZED_CLAIMS_USED = [C01, C02, C03, C07, C15]
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
CITATION_COMMENT_COVERAGE = 0/0
EN_ES_SEMANTIC_EQUIVALENCE = PASS
POSITIONING_ORDER = GENERAL_METHOD_AND_FUNCTIONAL_CONTRACT_FIRST / CONFIGURABILITY_BOUNDARY_SECOND / NANDINA_CH87_TESTBED_THIRD
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_V03.md + .docx
ENGLISH_MAIN_TEXT_WORD_COUNT = 353
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DELIVERY_STATE = REVISION_COMPLETED / AWAITING_INTERNAL_REVIEW
```
