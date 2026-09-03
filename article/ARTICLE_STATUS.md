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
- Estado de `0B-03B`: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Dictamen interno de `0B-03B`: **`PASS WITH MINOR CORRECTIONS`**.
- Revisión experimental de `0B-03B`: **`NOT_REQUIRED`**.
- Freeze de `0B-03B`: **`NOT_YET_AUTHORIZED`**.
- Prompt del bloque: `article/prompts/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING.md`.
- Revisión interna: `article/reviews/0B03B_INTERNAL_REVIEW.md`.
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

### Bloques cerrados de 0B

- `0B-01 = APPROVED / FROZEN` — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02 = APPROVED / FROZEN` — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A = APPROVED / FROZEN` — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.

La revisión y aprobación de 0B-03A están registradas en:

- `article/reviews/0B03A_INTERNAL_REVIEW.md`;
- `article/reviews/0B03A_AUTHOR_APPROVAL.md`.

### 0B-03B — revisión interna completada

```text
0B-03B = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE = NOT_YET_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Los seis PDF asignados fueron auditados como fuentes primarias del lote:

1. `A Deterministic Agentic Workflow for HS Tariff Classification.pdf`
2. `ATLAS-Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification.pdf`
3. `Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification.pdf`
4. `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification.pdf`
5. `HSCodeComp- A Realistic and Expert-level Benchmark for Deep Search Agents in Hierarchical Rule Application.pdf`
6. `HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification.pdf`

Los otros 56 PDF permanecen fuera del alcance de este lote.

### Normalizaciones que gobernarán el eventual freeze de 0B-03B

1. **ATLAS:** conservar `18,731` rulings declarados frente a splits que suman `18,654`; los `77` restantes permanecen `NO_VERIFICABLE_EN_PDF`.
2. **Deterministic Workflow:** `84.2%/77.4%` son agreement entre backbones, no ground-truth accuracy.
3. **Consensus Agentic:** el human-in-the-loop forma parte de la arquitectura, pero la evaluación cuantitativa no activa corrección humana.
4. **Constraint-Aware Search:** después de fijar la ruta, el generador final no puede cambiarla. La diferencia con F2 es que esa ruta se construye mediante búsqueda/reglas/LLM y no corresponde a un ranking Top-k histórico externo e inmutable.
5. **HSCodeComp:** G6 amplio queda eliminado como candidato a gap por existir anotación experta con adjudicación/control; la calidad de ground truth se conserva solo como principio metodológico.
6. **HSCodeComp/leakage:** cualquier acusación de leakage sobre benchmarks previos permanece `SECONDARY_CLAIM_UNVERIFIED` hasta revisar las fuentes primarias afectadas.
7. **HSGraphAgent:** `legally valid path` se restringe a cumplimiento de restricciones codificadas; no equivale a corrección jurídica independiente.
8. **F5:** solo sobrevive la formulación de evaluación formal, explícita y separada de auditabilidad documental por salida.
9. **G7:** se absorbe en F2 y deja de ser candidato independiente.
10. **Taxonomía/admisibilidad:** ATLAS no se rotula como agentic; `KEEP_CORE` es función del mapa 0B y `INHERITED_ELIGIBLE` no obliga a cita final.

### Candidatos provisionales después de la revisión de 0B-03B

Ninguno constituye gap definitivo ni novelty.

- **F1/G1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM` — precedentes históricos generan/fijan ranking; normativa llega después y no reordena.
- **F2/G2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED` — generador exclusivamente explicativo sobre ranking/Top-k fijado externamente por un componente previo independiente; no introduce/elimina/sustituye/reordena códigos y no retroalimenta clasificación.
- **F3/G3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT` — control de dependencia por unidad/grupo cuando el diseño contiene observaciones relacionadas susceptibles de cruzar particiones.
- **F4/G4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION` — predictive/candidate performance, path validity, rule consistency y evidence grounding ≠ corrección sustantiva/jurídica adjudicada.
- **F5/G5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED` — evaluación formal y separada de auditabilidad documental por salida.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; permanece solo como principio de calidad/procedencia del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

### Gate de 0B-03B

```text
IA de redacción
-> revisión científica/editorial interna contra PDF primarios [COMPLETADA]
-> aprobación expresa del autor [PENDIENTE]
-> integrar C1–C10 y crear freeze canónico de 0B-03B
-> evaluar apertura de 0B-04
```

No se requiere reejecución completa por la IA de redacción. No se requiere revisión de la IA experimental porque no se ha modificado ningún hecho/claim experimental congelado ni regla del Plan Maestro.

### Prohibiciones vigentes hasta aprobación del autor

No está autorizado:

- congelar 0B-03B sin aprobación expresa;
- abrir 0B-04, 0B-05 o 0B-06;
- abrir 0C o 0D;
- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad;
- modificar 0A o el Plan Maestro;
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
- 0B-03B status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**; material errors: `0`.
- Experimental review: `NOT_REQUIRED`.
- Freeze: `NOT_YET_AUTHORIZED`.
- Consolidated corpus: 62 distinct works/documents with verifiable primary access `62/62`.
- Target journal: pending until Phase 0D.
- Manuscript drafting: not started.

### Governing ground truth

The frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan or rewrite frozen ground truth; exclusive Master-Plan authority remains with the experimental workflow.

### Closed 0B blocks

0B-01, 0B-02, and 0B-03A are `APPROVED / FROZEN` with their canonical literature artifacts and review/approval records.

### 0B-03B internal review

The six assigned primary PDFs were audited. The drafting deliverable is analytically complete and passed internal review with minor corrections. No final gap or novelty has been declared.

The governing normalizations for a future freeze are:

1. ATLAS states 18,731 rulings while explicit splits total 18,654; 77 remain `NO_VERIFICABLE_EN_PDF`.
2. Deterministic Workflow's 84.2%/77.4% values are cross-backbone agreement, not ground-truth accuracy.
3. Consensus Agentic includes human escalation architecturally, but quantitative evaluation runs without corrective human intervention.
4. Constraint-Aware Search fixes the hierarchy path before its final generator, and that generator cannot change the path. The distinction from F2 is the provenance/structure of the decision: LLM/rule/evidence-generated path versus an externally fixed historical ranked Top-k.
5. HSCodeComp eliminates broad G6 as a gap candidate because it supplies expert annotation with adjudication/control; ground-truth quality remains only a methodological principle.
6. HSCodeComp's leakage claims about prior benchmarks remain `SECONDARY_CLAIM_UNVERIFIED` until those primary studies are audited.
7. HSGraphAgent's `legally valid path` means compliance with encoded constraints, not independent legal correctness.
8. F5 survives only as formal, explicit, separate per-output documentary-auditability evaluation.
9. G7 is merged into F2 and removed as an independent candidate.
10. ATLAS is not categorized as agentic; `KEEP_CORE` is a 0B-map role and `INHERITED_ELIGIBLE` does not mandate final citation.

### Updated provisional candidates

No candidate establishes novelty or a final gap.

- F1 survives narrowly: historical precedents fix ranking; normative evidence arrives afterward and cannot reorder it.
- F2 is further narrowed: explanation-only generation over an externally fixed immutable ranking/Top-k, with no code addition/deletion/substitution/reordering and no feedback into classification.
- F3 is retained with an applicability caveat for genuinely related/grouped observations.
- F4 remains a methodological distinction between predictive/candidate metrics and adjudicated substantive/legal correctness.
- F5 is further narrowed to formal separate per-output documentary auditability evaluation.
- G6 is eliminated as a gap candidate and retained only as a ground-truth-quality principle.
- G7 is merged into F2 and eliminated independently.

### Gate

`drafting AI -> internal primary-PDF review [complete] -> express author approval [pending] -> integrate C1-C10 and freeze 0B-03B -> assess opening 0B-04`.

No full drafting-AI rerun or experimental-AI review is required. Until express author approval, 0B-03B cannot be frozen, 0B-04 through 0B-06 cannot open, 0C/0D remain blocked, and manuscript drafting/novelty claims remain prohibited.
