# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0A-01`: **`APPROVED / FROZEN`**.
- `0A-02`: **`APPROVED / FROZEN`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0B-03B — Agentes, benchmarks y razonamiento jerárquico/regulatorio`**.
- Estado de `0B-03B`: **`READY_FOR_DRAFTING`**.
- Prompt activo: `article/prompts/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING.md`.
- Plan de lotes: `article/literature/0B_LITERATURE_BATCH_PLAN.md`.
- Corpus consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth gobernante

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

Ningún bloque bibliográfico puede modificar el Plan Maestro ni reescribir el ground truth experimental/documental congelado. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro.

### 0B-01 — cierre formal

`0B-01 = APPROVED / FROZEN`.

Artefacto: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.

### 0B-02 — cierre formal

`0B-02 = APPROVED / FROZEN`.

Artefacto: `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.

### 0B-03A — cierre formal

```text
0B-03A = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Artefacto canónico:

`article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`

Registros:

- `article/reviews/0B03A_INTERNAL_REVIEW.md`;
- `article/reviews/0B03A_AUTHOR_APPROVAL.md`.

Correcciones C1–C6 congeladas:

1. THE-RAG: `.44/.47/.51/.59/.60` HS6 Top-3 corresponde a `gemini_1.5_flash`, no a `gemini_1.5_flash_8b`; preservar el contraejemplo `llama3.1_8b` `.14` no-RAG vs `.11/.09` RAG.
2. Koch & Power: categoría operacional `FINE_TUNED_TRANSFORMER_CLASSIFIER`; “LLM” solo como terminología de autores cuando corresponda.
3. ICCA-RAG: evidence support para contexto de QA aduanero, no evidencia normativa posterior a un Top-k fijo; metadata/backtracking = procedencia técnica, no legal correctness/auditabilidad formal por candidato.
4. Gholamian: Icecat/WDC-222 no son HS; el experimento humano no debe generalizarse a beneficio humano de clasificación HS.
5. `SUPPORTS_CANDIDATE` = contraste compatible con supervivencia provisional en el lote, nunca evidencia de novelty.
6. Amel: `.500 -> .582` = +8.2 pp frente a D-only; `.647 -> .653` = +0.6 pp frente al mejor texto enriquecido.

### Candidatos provisionales tras 0B-03A

Todos permanecen `CANDIDATE_GAP_ONLY`:

- F1/G1: `SURVIVES IN NARROW FORM` — precedentes históricos generan/fijan ranking; normativa llega después y no reordena.
- F2/G2: `SURVIVES IN NARROW FORM` — generador posterior restringido a Top-k fijo, sin introducir/reordenar códigos.
- F3/G3: `SURVIVES THIS BATCH; METHODOLOGICAL` — control explícito de dependencia por unidad administrativa/grupo.
- F4/G4: `SURVIVES AS METHODOLOGICAL DISTINCTION` — predictive/candidate performance ≠ corrección sustantiva/jurídica adjudicada.
- F5/G5: `FURTHER NARROWED BY ICCA-RAG` — evaluación formal por caso de trazabilidad/auditabilidad, no mera metadata/faithfulness.
- G6: `SURVIVES; METHODOLOGICAL` — ground truth independiente/adjudicado para correctness.
- G7: `NEW/PROVISIONAL; PRESSURE TEST REQUIRED IN 0B-03B` — separación entre papel clasificatorio y explicativo del LLM.

Ninguno constituye gap definitivo ni novelty.

### 0B-03B — apertura formal

Objetivo: analizar agentes, benchmarks y razonamiento jerárquico/regulatorio para determinar si ya existen diseños que desacoplan clasificación, búsqueda, reglas, recuperación, explicación y verificación de una forma comparable al presente trabajo.

PDF asignados:

1. `A Deterministic Agentic Workflow for HS Tariff Classification.pdf`
2. `ATLAS-Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification.pdf`
3. `Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification.pdf`
4. `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification.pdf`
5. `HSCodeComp- A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application.pdf`
6. `HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification.pdf`

Los otros 56 PDF permanecen `OUT_OF_SCOPE_FOR_0B03B`.

Controles obligatorios:

- leer íntegramente 6/6 PDF;
- no usar web ni buscar literatura nueva;
- distinguir agentic classification, multi-agent consensus, deterministic workflow, deep/hierarchical search, regulation-driven search, KG-guided reasoning y post-hoc explanation;
- distinguir reglas/normativa usadas para decidir el código de evidencia posterior usada solo para respaldarlo;
- distinguir consensus/self-consistency de ground truth independiente;
- distinguir reasoning trace/citations de auditabilidad formal;
- auditar si candidatos están pre-fijados, si pueden introducirse nuevos códigos y si el orden puede cambiar;
- auditar validación de códigos, constraints, guardrails y abstención;
- someter F1–F5/G6/G7 a pressure test explícito;
- no convertir `SUPPORTS_CANDIDATE` en novelty;
- mantener separadas función científica y admisibilidad bibliográfica final;
- no modificar GitHub ni el Plan Maestro.

### Gate de 0B-03B

```text
IA de redacción
-> revisión científica/editorial interna contra PDF primarios
-> corrección si aplica
-> aprobación del autor
-> freeze de 0B-03B
-> evaluación de apertura de 0B-04
```

La IA experimental solo se incorporará si una interpretación bibliográfica afecta directamente hechos/claims experimentales o restricciones metodológicas bajo su autoridad.

### Prohibiciones vigentes

Durante 0B-03B no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad;
- modificar 0A o el Plan Maestro;
- avanzar a 0B-04, 0B-05, 0B-06, 0C o fases posteriores;
- usar resultados experimentales pendientes como cerrados;
- convertir claims secundarios en hechos sin verificar la fuente primaria.

### Fases posteriores

- `0B-04`: `NOT_STARTED`.
- `0B-05`: `NOT_STARTED`.
- `0B-06`: `NOT_STARTED`.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
- Revista objetivo: **no definida ni congelada**; se decidirá en 0D.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: `CLOSED / APPROVED`; 0A-01 and 0A-02 are `APPROVED / FROZEN`.
- Active phase: `0B — Critical literature map and taxonomy`.
- 0B-01, 0B-02, and 0B-03A are `APPROVED / FROZEN`.
- Active block: `0B-03B — Agents, benchmarks, and hierarchical/regulatory reasoning`.
- 0B-03B status: `READY_FOR_DRAFTING`.
- Active prompt: `article/prompts/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING.md`.
- Consolidated corpus: 62 distinct works/documents with primary verifiable access `62/62`.
- Target journal: pending until Phase 0D.
- Manuscript drafting: not started.

### Governing ground truth

The frozen 0A documentary and experimental artifacts remain authoritative. The literature workflow may not modify the Master Plan or rewrite frozen ground truth; exclusive Master-Plan authority remains with the experimental workflow.

### 0B-03A formal closure

`0B-03A = APPROVED / FROZEN`; internal review passed with minor corrections; express author approval was received; experimental review was not required; no final gap or novelty was declared.

Canonical artifact: `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.

The freeze incorporates exact THE-RAG model identity, Koch & Power taxonomy normalization, ICCA-RAG evidence-role qualification, the limited interpretation of Gholamian's human study, the provisional meaning of `SUPPORTS_CANDIDATE`, and baseline-specific multimodal gains.

### Provisional candidates after 0B-03A

F1/F2 survive only narrowly; F3/G6 remain methodological; F4 remains a methodological distinction; F5 is further narrowed by ICCA-RAG; G7 is new/provisional and must be pressure-tested in 0B-03B. All remain `CANDIDATE_GAP_ONLY`; none establishes novelty.

### 0B-03B opening

0B-03B analyzes only the six agentic/benchmark/hierarchical-regulatory papers listed in the Spanish section. It must determine whether prior systems already separate or combine code classification, hierarchical/deep search, regulatory rules, knowledge graphs, candidate constraints, explanation, verification, and auditability in ways comparable to the present architecture.

Mandatory controls include full reading, no web/new literature, explicit distinction among agentic classification, consensus, deterministic workflows, hierarchical/regulation-driven search, KG-guided reasoning, and downstream explanation; explicit analysis of candidate fixation/new-code capability/order changes; validation/guardrails; ground-truth quality; auditability versus reasoning traces; dependency controls; and pressure testing of F1–F5/G6/G7 without novelty claims.

### Gate

`drafting AI -> internal scientific/editorial review against primary PDFs -> correction if needed -> author approval -> freeze 0B-03B -> assess opening 0B-04`.

Experimental-AI involvement is required only if a literature interpretation changes experimental facts, claims, or restrictions under its authority.

### Later phases

0B-04 through 0B-06 remain `NOT_STARTED`; 0C is blocked until 0B closes; 0D is blocked until 0C closes; target journal remains undecided until 0D.
