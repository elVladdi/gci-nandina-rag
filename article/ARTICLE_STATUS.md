# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase vigente: `0A — Ground truth documental y experimental`.
- `0A-01 — Ground truth documental`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0A-02 — Ground truth experimental`**.
- Estado de `0A-02`: **`READY_FOR_DRAFTING`**.
- Prompt activo: `article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Idioma del chat: español.
- Artefactos GitHub del entorno del artículo: español + inglés con equivalencia semántica.
- Manuscrito redactado: no iniciado.

### Cierre de 0A-01

`0A-01` completó revisión interna, auditoría experimental independiente, pase experimental final y aprobación expresa del autor. Su estado es:

```text
0A-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS
EXPERIMENTAL_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
```

Artefacto congelado:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

Registros:

- `article/reviews/0A01_INTERNAL_REVIEW.md`;
- `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A01_AUTHOR_APPROVAL.md`.

El congelamiento de 0A-01 fija el ground truth documental del corte, pero no congela el estado experimental completo. `SRC-03` permanece como fuente viva.

### Apertura formal de 0A-02

Objetivo: consolidar el **ground truth experimental verificable** sin redactar todavía ninguna sección del artículo y sin ejecutar/modificar experimentos.

0A-02 debe distinguir resultados vigentes, snapshots históricos, experimentos ejecutados con alcance limitado, estados pendientes, claims no autorizados y limitaciones de trazabilidad.

Fuentes principales:

1. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
2. `article/CLAIM_EVIDENCE_MATRIX.md`;
3. `SRC-03` — Plan Maestro vivo en GitHub;
4. rama `main` y artefactos/commits experimentales versionados del repositorio de desarrollo;
5. repositorio de reproducibilidad solo cuando sea necesario para establecer el estado del protocolo de reproducción/replicación.

### Corte de apertura de 0A-02 — 2026-09-02

- HEAD de `main`: `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.
- Estado de ese HEAD: cierre del Bank Materialization Gate / comprobaciones de procedencia de EXP-11B; no constituye ejecución de retrieval H150/H200.
- `SRC-03` blob SHA: `0a9a82181c6c3840f74f0272e5c225568474058b`.

Estos SHA son snapshots de apertura. La IA de redacción debe verificar nuevamente ambos al ejecutar 0A-02 y reportar cualquier drift material.

### Estado experimental mínimo que debe preservarse al abrir 0A-02

- benchmark v0.2 H100/DEV/EVAL: vigente y congelado dentro de su alcance;
- `SERIE`: unidad de análisis;
- `DAM`: unidad de agrupamiento cuando existe dependencia;
- v0.1 `3,000/100/1,006`: snapshot histórico, no benchmark vigente;
- `995/1006`: hallazgo histórico autorizado y limitado al análisis del rediseño del split;
- `48/59`: `REVIEW_REQUIRED`;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED`: interpretación histórica/intermedia específica de EXP-08;
- decisión inferencial final HE5: `PENDING_GROUP3`;
- EXP-11A: cerrado/versionado, interpretación descriptiva; no efecto causal aislado del tamaño del banco;
- EXP-11B retrieval: `PENDING`;
- H150/H200: sin resultados de retrieval autorizados en el corte de apertura;
- EXP-12: `PENDING`;
- Grupo 2B: pendiente después de EXP-11B/EXP-12;
- Grupo 3: `PENDING`; decisión final HE2/HE5 pendiente;
- HE4: solo utilizable con sus limitaciones de auditoría; no demuestra corrección jurídica completa;
- asociación de evidencia normativa: no equivale automáticamente a corrección normativa sustantiva.

### Adjuntos para 0A-02

**Ninguno.**

La IA de redacción debe obtener las fuentes directamente desde GitHub. No debe solicitar Proyecto, Anexo, tesis preliminar, Plan Maestro local ni PDFs bibliográficos.

### Trabajo autorizado ahora

Ejecutar exclusivamente `0A-02` siguiendo íntegramente:

`article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`

La respuesta en chat debe ser únicamente en español.

No realizar búsqueda web, no analizar literatura, no iniciar 0B, no redactar el manuscrito y no modificar GitHub.

### Gate de 0A-02

1. IA de redacción entrega 0A-02.
2. Editor científico realiza revisión interna.
3. Se corrigen observaciones internas si corresponde.
4. **Solo cuando el editor científico lo indique**, la IA experimental realiza auditoría independiente de 0A-02.
5. Se resuelven observaciones experimentales.
6. El autor aprueba expresamente el bloque.
7. Se consolida el artefacto bilingüe definitivo y se congela 0A-02.

No abrir 0B mientras 0A no haya completado los componentes exigidos por el plan de redacción.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Overall status: `IN_ANALYSIS`.
- Current phase: `0A — Documentary and experimental ground truth`.
- `0A-01 — Documentary ground truth`: **`APPROVED / FROZEN`**.
- Active block: **`0A-02 — Experimental ground truth`**.
- `0A-02` status: **`READY_FOR_DRAFTING`**.
- Active prompt: `article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`.
- Target journal: `PENDING — to be decided in Phase 0D`.
- Chat language: Spanish.
- GitHub artifacts in the article workspace: Spanish + English with semantic equivalence.
- Manuscript drafting: not started.

### 0A-01 closure

`0A-01` completed internal review, independent experimental audit, final experimental pass, and explicit author approval. Its status is:

```text
0A-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS
EXPERIMENTAL_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
```

Frozen artifact:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

Records:

- `article/reviews/0A01_INTERNAL_REVIEW.md`;
- `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A01_AUTHOR_APPROVAL.md`.

Freezing 0A-01 fixes the documentary ground truth for its cutoff, but does not freeze the complete experimental state. `SRC-03` remains a living source.

### Formal opening of 0A-02

Objective: consolidate the **verifiable experimental ground truth** without drafting any manuscript section and without executing/modifying experiments.

0A-02 must distinguish current results, historical snapshots, executed experiments with limited scope, pending states, unauthorized claims, and traceability limitations.

Primary sources:

1. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
2. `article/CLAIM_EVIDENCE_MATRIX.md`;
3. `SRC-03` — living Master Plan on GitHub;
4. `main` branch and versioned experimental artifacts/commits from the development repository;
5. reproducibility repository only when needed to establish reproduction/replication protocol status.

### 0A-02 opening cutoff — 2026-09-02

- `main` HEAD: `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.
- Meaning of that HEAD: EXP-11B Bank Materialization Gate/provenance checks closure; it is not H150/H200 retrieval execution.
- `SRC-03` blob SHA: `0a9a82181c6c3840f74f0272e5c225568474058b`.

These SHAs are opening snapshots. The drafting AI must verify both again when executing 0A-02 and report any material drift.

### Minimum experimental state to preserve when opening 0A-02

- v0.2 H100/DEV/EVAL benchmark: current and frozen within its scope;
- `SERIES`: analysis unit;
- `DAM`: grouping unit when dependence exists;
- v0.1 `3,000/100/1,006`: historical snapshot, not current benchmark;
- `995/1006`: authorized historical finding limited to split-redesign analysis;
- `48/59`: `REVIEW_REQUIRED`;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED`: historical/intermediate interpretation specific to EXP-08;
- final inferential HE5 decision: `PENDING_GROUP3`;
- EXP-11A: closed/versioned, descriptive interpretation only; no isolated causal bank-size effect;
- EXP-11B retrieval: `PENDING`;
- H150/H200: no authorized retrieval results at the opening cutoff;
- EXP-12: `PENDING`;
- Group 2B: pending after EXP-11B/EXP-12;
- Group 3: `PENDING`; final HE2/HE5 decision pending;
- HE4: usable only with its audit limitations; does not demonstrate complete legal correctness;
- normative-evidence association does not automatically equal substantive normative correctness.

### Attachments for 0A-02

**None.**

The drafting AI must obtain the sources directly from GitHub. It must not request the Project, Annex, preliminary thesis, local Master Plan, or bibliographic PDFs.

### Authorized work now

Execute only `0A-02` by following in full:

`article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`

The chat response must be in Spanish only.

Do not perform web searches, analyze literature, start 0B, draft the manuscript, or modify GitHub.

### 0A-02 gate

1. Drafting AI delivers 0A-02.
2. Scientific editor performs internal review.
3. Internal observations are corrected when applicable.
4. **Only when the scientific editor explicitly requests it**, the experimental AI performs the independent 0A-02 audit.
5. Experimental observations are resolved.
6. The author explicitly approves the block.
7. The final bilingual artifact is consolidated and 0A-02 is frozen.

Do not open 0B until 0A has completed the components required by the writing plan.
