# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0A-01`: **`APPROVED / FROZEN`**.
- `0A-02`: **`APPROVED / FROZEN`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01 — Clasificación HS directa y aprendizaje supervisado`: **`APPROVED / FROZEN`**.
- `0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero`**.
- Estado de 0B-03A: **`READY_FOR_DRAFTING`**.
- Prompt activo: `article/prompts/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS.md`.
- Plan de lotes: `article/literature/0B_LITERATURE_BATCH_PLAN.md`.
- Corpus PDF consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### 0B-01 — cierre formal

```text
0B-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Artefacto canónico:
`article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`

### 0B-02 — cierre formal

```text
0B-02 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Artefacto canónico:
`article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`

Registros:
- `article/reviews/0B02_INTERNAL_REVIEW.md`;
- `article/reviews/0B02_AUTHOR_APPROVAL.md`.

Correcciones C1–C4 integradas:

1. P01: test temporal final 1,652, validación 1,835; HS6 Top-3 0.955 sin retrieved sentences y 0.937 con retrieved sentences.
2. P03: 226,703 casos tabulados frente a 211,435 asignados explícitamente a train/validation/test; 15,268 permanecen `NO_VERIFICABLE_EN_PDF`.
3. P03: helpfulness operativo 65.7% (score 4–5); >85% corresponde a otra distribución de percepción; reducción de tiempo/esfuerzo = percepción, no causalidad.
4. P02/P04/P06: Text2Trade `REVIEW_REQUIRED` y sin validación externa sectorial; P04 ≈84.23% no es detección adjudicada de misclasificación; P06 imprime Recall=`TP/(TP+TN)` y sus F1 se conservan con caveat; CV por triples no demuestra independencia ni leakage.

### Candidatos provisionales después de 0B-02

Todos siguen siendo `CANDIDATE_GAP_ONLY`, no novelty:

- F1: `NARROWED` a ranking fijado por precedentes históricos + evidencia normativa exclusivamente posterior y no reordenadora.
- F2: `NARROWED` a generador posterior restringido a Top-k fijo, sin códigos externos ni reordenamiento.
- F3: `SURVIVES THIS BATCH`.
- F4: `SUPPORTED AS A METHODOLOGICAL DISTINCTION` entre candidate retrieval/coherence y corrección sustantiva.
- F5: `NARROWED` a evaluación formal y separada de trazabilidad/auditabilidad documental.
- G6: `NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM` sobre ground truth independiente/adjudicado para correctness.

### 0B-03 — división controlada

Para preservar lectura completa, comparabilidad y auditoría independiente, 0B-03 se divide en `0B-03A` y `0B-03B`.

#### 0B-03A — activo

Objetivo: analizar cómo LLM, RAG y multimodalidad se utilizan realmente en clasificación/compliance aduanero y qué papel causal desempeñan retrieval, generación, reranking, documentos, imágenes y restricciones de salida.

PDF asignados:

1. `Automatic product classification in international trade Machine learning and large language models.pdf`
2. `Automating Harmonized System (HS) Code Classification from Unstructured Shipping Manifests using Large Language Models.pdf`
3. `Development of an Automated HS Code Classification System Using LLM Based on an Optimized RAG Framework.pdf`
4. `ICCA-RAG Intelligent Customs Clearance Assistant Using RAG.pdf`
5. `LLM-based robust product classification in commerce and compliance.pdf`
6. `Multimodal approach for Harmonized System code prediction.pdf`

Los otros 56 PDF permanecen `OUT_OF_SCOPE_FOR_0B03A`.

Controles obligatorios:
- lectura íntegra de 6/6 PDF;
- no web ni literatura nueva;
- no completar silenciosamente con tesis/Anexo u otros PDF;
- usar `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF`, `SECONDARY_CLAIM_UNVERIFIED`;
- distinguir LLM que decide códigos de LLM que solo explica candidatos;
- distinguir `RAG_CLASSIFICATION` de `RAG_EVIDENCE_SUPPORT`;
- distinguir reranking de explanation;
- auditar si existen restricciones `no new codes`, orden fijo, validación de código o guardrails;
- no convertir robustez, explainability, compliance o multimodalidad en claims más amplios que el protocolo medido;
- someter F1–F5 y G6 a presión explícita;
- no declarar novelty ni gap definitivo.

#### 0B-03B — previsto, no abierto

Estado: `NOT_STARTED`.

Se reservará para agentes, benchmarks y razonamiento jerárquico/regulatorio, incluyendo el conjunto previsto de seis trabajos registrado en `0B_LITERATURE_BATCH_PLAN.md`.

### Gate de 0B-03A

```text
IA de redacción
-> revisión científica/editorial interna contra PDF primarios
-> corrección si aplica
-> aprobación del autor
-> freeze de 0B-03A
-> apertura de 0B-03B
```

La IA experimental solo se incorporará si una interpretación bibliográfica afecta directamente un hecho experimental, claim experimental o restricción metodológica bajo su autoridad.

### Prohibiciones vigentes

Durante 0B-03A no está autorizado:
- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad;
- modificar 0A o el Plan Maestro;
- avanzar a 0B-03B, 0B-04, 0C o fases posteriores;
- usar resultados experimentales pendientes como cerrados;
- convertir secondary claims en hechos sin verificación primaria.

### Fases posteriores

- `0B-03B`: `NOT_STARTED`.
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
- Overall state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- 0A-01 and 0A-02: **`APPROVED / FROZEN`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01: **`APPROVED / FROZEN`**.
- 0B-02: **`APPROVED / FROZEN`**.
- Active block: **`0B-03A — LLM, RAG, and multimodality in customs classification/compliance`**.
- 0B-03A status: **`READY_FOR_DRAFTING`**.
- Active prompt: `article/prompts/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS.md`.
- Consolidated corpus: 62 distinct works/documents; primary verifiable access `62/62`.
- Target journal: pending until Phase 0D.
- Manuscript drafting: not started.

### 0B-02 closure

0B-02 is `APPROVED / FROZEN`; internal review passed with minor corrections; express author approval was received; no experimental review was required. Canonical artifact: `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.

The canonical freeze integrates the P01 denominator/variant correction, P03 dataset-accounting and survey corrections, and the governing caveats for Text2Trade, P04 correctness scoring, and P06's printed Recall formula/triple-level CV.

### Provisional candidate gaps

F1/F2/F5 are narrowed, F3 survives this batch provisionally, F4 survives as a methodological distinction, and G6 remains a new methodological candidate only. None establishes novelty.

### 0B-03 controlled split

0B-03 is split into `0B-03A` and `0B-03B` to preserve complete reading and independent verification.

0B-03A analyzes the six PDFs listed in the Spanish section and must distinguish direct LLM code determination from explanation of fixed candidates, RAG classification from evidence support, reranking from explanation, and actual output constraints/guardrails from unconstrained generation.

0B-03B remains `NOT_STARTED` and will cover agents, benchmarks, and hierarchical/regulatory reasoning after 0B-03A closes.

### Gate

`drafting AI -> internal scientific/editorial review against primary PDFs -> correction if needed -> author approval -> freeze -> open 0B-03B`.

Experimental-AI involvement is required only if literature interpretation directly affects experimental facts, claims, or restrictions under its authority.

### Later phases

- 0B-03B through 0B-06: `NOT_STARTED`.
- 0C: `BLOCKED` until 0B closes.
- 0D: `BLOCKED` until 0C closes.
- Target journal: not selected or frozen; decision occurs in 0D.
