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
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04`: `NOT_STARTED`.
- `0B-05`: `NOT_STARTED`.
- `0B-06`: `NOT_STARTED`.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Corpus consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth gobernante

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

Los bloques bibliográficos no modifican el Plan Maestro ni el ground truth de 0A. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro.

### Bloques cerrados de 0B

- `0B-01 = APPROVED / FROZEN` — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02 = APPROVED / FROZEN` — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A = APPROVED / FROZEN` — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B = APPROVED / FROZEN` — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.

Registros de 0B-03B:

- `article/reviews/0B03B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`;
- `article/reviews/0B03B_AUTHOR_APPROVAL.md` — aprobación expresa recibida.

### 0B-03B — cierre formal

```text
0B-03B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Las normalizaciones C1–C10 de `article/reviews/0B03B_INTERNAL_REVIEW.md` quedan integradas y gobernantes en el artefacto canónico congelado.

### Hallazgos gobernantes después de 0B-03B

1. La literatura reciente ya incluye workflows deterministas, consenso multiagente, búsqueda jerárquica/regulatoria, deep-search benchmarks y clasificación guiada por knowledge graph.
2. En varios antecedentes, normativa/reglas/jerarquía participan directamente en la decisión de clasificación; esto es distinto del diseño actual donde la evidencia normativa llega después de que el ranking histórico queda fijado.
3. Wang et al. ya separa una ruta jerárquica fijada de un generador posterior de evidence/rationale; por tanto, una formulación amplia de “explicación posterior a una decisión fijada” no puede considerarse gap.
4. HSCodeComp aporta un antecedente de ground truth multi-experto con adjudicación/control; G6 amplio queda eliminado como candidato a gap.
5. Rutas, snippets, citations, traces y provenance ya están presentes; F5 solo sobrevive en la forma estrecha de evaluación formal, explícita y separada de auditabilidad documental por salida.
6. `legally valid path`, path validity o cumplimiento de constraints codificados no equivalen a corrección jurídica independiente.
7. Claims de leakage atribuidos por HSCodeComp a benchmarks previos permanecen `SECONDARY_CLAIM_UNVERIFIED` hasta auditoría primaria de esos trabajos.

### Candidatos provisionales después de 0B-03B

Ninguno constituye novelty ni gap definitivo.

- **F1/G1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM` — precedentes históricos recuperados generan/fijan ranking; normativa llega después y no reordena.
- **F2/G2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED` — generador exclusivamente explicativo sobre ranking/Top-k fijado externamente por un componente previo independiente; no introduce/elimina/sustituye/reordena códigos y no retroalimenta clasificación.
- **F3/G3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT` — control de dependencia por unidad/grupo cuando existen observaciones relacionadas susceptibles de cruzar particiones.
- **F4/G4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION` — predictive/candidate performance, path validity, rule consistency y evidence grounding no equivalen a corrección sustantiva/jurídica adjudicada.
- **F5/G5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED` — evaluación formal y separada de auditabilidad documental por salida.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; se conserva solo como principio de calidad/procedencia/adjudicación del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

### Gate siguiente

El cierre de 0B-03B está completo. La apertura de `0B-04 — Fundamentos de Information Retrieval y RAG` aún **no se ha ejecutado** en este cambio y debe seguir el plan de lotes y la gobernanza bibliográfica vigentes.

Mientras 0B permanezca abierto:

- no redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- no declarar novelty, gap definitivo o superioridad;
- no abrir 0C;
- no modificar 0A ni el Plan Maestro;
- no convertir secondary claims en hechos sin verificar la fuente primaria.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**; 0A-01 and 0A-02 are **`APPROVED / FROZEN`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, and 0B-03B are **`APPROVED / FROZEN`**.
- 0B-04, 0B-05, and 0B-06 remain `NOT_STARTED`.
- 0C remains `BLOCKED` until 0B closes; 0D remains `BLOCKED` until 0C closes.
- Target journal remains pending until Phase 0D.
- Manuscript drafting has not started.
- Consolidated corpus: 62 distinct works/documents with primary verifiable access `62/62`.

### Governing ground truth

Frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan or rewrite frozen 0A ground truth; exclusive Master-Plan authority remains with the experimental workflow.

### Closed 0B blocks

0B-01, 0B-02, 0B-03A, and 0B-03B are approved/frozen with their canonical literature artifacts. The governing 0B-03B records are `article/reviews/0B03B_INTERNAL_REVIEW.md` and `article/reviews/0B03B_AUTHOR_APPROVAL.md`.

### 0B-03B formal closure

```text
0B-03B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

C1–C10 from the internal review are integrated into the canonical frozen artifact.

### Governing findings after 0B-03B

Recent literature already includes deterministic agentic workflows, multi-agent consensus, hierarchical/regulation-driven search, deep-search benchmarks, and knowledge-graph-guided classification. In several systems, regulatory rules/hierarchy directly determine classification rather than merely documenting a fixed historical ranking. Wang et al. already separates a fixed hierarchical path from downstream evidence/rationale generation, so broad “post-decision explanation” is not an uncovered space. HSCodeComp provides a direct expert/adjudication precedent, eliminating broad G6. Traceable paths, snippets, citations, and structured traces already exist; F5 survives only as formal, explicit, separate per-output documentary-auditability evaluation. Encoded path validity or `legally valid path` is not independent legal adjudication. Leakage claims about earlier benchmarks remain secondary until those primary studies are directly audited.

### Provisional candidates after 0B-03B

- F1: survives narrowly.
- F2: further narrowed to explanation-only generation over an externally fixed immutable ranked Top-k, with no code addition/deletion/substitution/reordering and no feedback into classification.
- F3: retained with applicability caveat.
- F4: retained as a methodological distinction, not novelty.
- F5: further narrowed to formal/separate per-output auditability evaluation.
- G6: eliminated as a gap candidate; retained only as a ground-truth-quality principle.
- G7: merged into F2 and eliminated independently.

None establishes a final gap or novelty.

### Next gate

0B-03B closure is complete. Opening `0B-04 — Information Retrieval and RAG foundations` has **not** been executed in this change and remains subject to the literature batch plan and bibliographic governance.

While 0B remains open, manuscript drafting, final-gap/novelty claims, 0C opening, Master-Plan modification, and promotion of unverified secondary claims remain prohibited.
