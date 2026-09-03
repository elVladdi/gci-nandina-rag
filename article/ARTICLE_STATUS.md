# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0A-01 — Ground truth documental`: **`APPROVED / FROZEN`**.
- `0A-02 — Ground truth experimental`: **`APPROVED / FROZEN`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- Bloque activo: **`0B-01 — Clasificación HS directa y aprendizaje supervisado`**.
- Estado de `0B-01`: **`READY_FOR_DRAFTING`**.
- Prompt activo: `article/prompts/0B01_HS_CLASSIFICATION_CORE_LITERATURE.md`.
- Plan de lotes: `article/literature/0B_LITERATURE_BATCH_PLAN.md`.
- Corpus PDF conocido disponible para la IA de redacción: **`62` obras/documentos distintos**.
- Alcance de análisis de 0B-01: **`8` PDF asignados**.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Idioma del chat: español.
- Artefactos GitHub del entorno del artículo: español + inglés con equivalencia semántica.

### Ground truth congelado de 0A

Los artefactos que gobiernan el trabajo posterior son:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

El corte experimental congelado de 0A-02 fue:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`.

El Plan Maestro continúa siendo fuente viva bajo autoridad exclusiva del flujo experimental. Ningún bloque bibliográfico puede modificarlo ni reescribir silenciosamente el ground truth histórico congelado.

### Apertura formal de 0B

La Fase 0B está abierta para construir un **mapa crítico de literatura y taxonomía** antes de definir gap, contribución o Research Questions.

0B se ejecutará por lotes temáticos controlados. El autor informó que la IA de redacción ya dispone de **62 PDF distintos** para esta fase, después de consolidar duplicados y sufijos automáticos. En el corte informado, `37/62` ya poseen entrada en el índice bibliográfico versionado de GitHub y `25/62` todavía no están indexados allí. La falta de entrada en GitHub no implica invalidez o exclusión; sí obliga a gobernar su procedencia/admisibilidad antes de utilizarlos en el manuscrito.

La disponibilidad de los 62 PDF no elimina el esquema de lotes. Un documento visible pero no asignado al bloque activo queda `OUT_OF_SCOPE_FOR_CURRENT_BATCH` hasta que se abra su lote correspondiente.

El protocolo bibliográfico aplicable es `article/BIBLIOGRAPHIC_FRAMEWORK.md` y el plan operativo actualizado es `article/literature/0B_LITERATURE_BATCH_PLAN.md`.

### PDF asignados a 0B-01

0B-01 analiza exclusivamente estos ocho trabajos:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

Si la IA de redacción ya puede acceder íntegramente a estos archivos dentro de su conversación, **no deben volver a adjuntarse**. Si alguno no está disponible o no puede leerse completo, solo debe solicitarse ese archivo específico.

Los otros PDF del corpus de 62 se conservarán para 0B-02 y lotes posteriores cuando sean pertinentes. No se permite utilizarlos dentro de 0B-01 para completar silenciosamente información de los ocho papers activos.

### Alcance autorizado de 0B-01

La IA de redacción debe:

- completar el onboarding de la rama;
- leer los ocho PDF asignados completos;
- construir la matriz crítica paper por paper;
- distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA` y `NO_VERIFICABLE_EN_PDF`;
- comparar tarea, nivel HS, datasets, método, validación, jerarquía, normativa, precedentes, explicabilidad, auditabilidad, dependencia/leakage y relación con el presente enfoque;
- proponer únicamente `CANDIDATE_GAP_ONLY`, sin novelty definitiva;
- recomendar `KEEP_CORE`, `KEEP_SUPPORTING`, `REVIEW_REQUIRED` o `EXCLUDE_FROM_ARTICLE` para cada trabajo;
- detenerse al finalizar 0B-01.

### Prohibiciones vigentes

Durante 0B-01 no está autorizado:

- realizar búsqueda web;
- buscar literatura nueva;
- analizar los otros PDF del corpus de 62;
- redactar secciones del manuscrito;
- declarar novelty, gap definitivo o superioridad;
- avanzar a 0B-02, 0C o fases posteriores;
- modificar GitHub desde la IA de redacción;
- alterar 0A o el Plan Maestro.

Las referencias heredadas pueden ser antiguas, proceedings, tesis o preprints; su pertinencia se evalúa en 0B. Las reglas 2022–2026, journal peer-reviewed y Q1/Q2 aplican a literatura académica nueva según `BIBLIOGRAPHIC_FRAMEWORK.md`. La mera disponibilidad de un PDF no convierte automáticamente una referencia nueva en `APPROVED_NEW`.

### Gate de 0B-01

Secuencia obligatoria:

```text
IA de redacción
-> revisión científica/editorial interna
-> corrección si aplica
-> aprobación del autor
-> cierre de 0B-01
```

La IA experimental no es revisora obligatoria de literatura. Solo se solicitará su intervención si una interpretación bibliográfica afecta directamente hechos experimentales, claims experimentales o restricciones metodológicas bajo su autoridad.

### Fases posteriores

- `0B-02` y lotes posteriores: `NOT_STARTED`.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta completar 0A y 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta completar 0C.
- Revista objetivo: **no definida ni congelada**; se decidirá en 0D.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Overall state: `IN_ANALYSIS`.
- Phase `0A — Documentary and experimental ground truth`: **`CLOSED / APPROVED`**.
- `0A-01 — Documentary ground truth`: **`APPROVED / FROZEN`**.
- `0A-02 — Experimental ground truth`: **`APPROVED / FROZEN`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- Active block: **`0B-01 — Direct HS classification and supervised learning`**.
- `0B-01` status: **`READY_FOR_DRAFTING`**.
- Active prompt: `article/prompts/0B01_HS_CLASSIFICATION_CORE_LITERATURE.md`.
- Batch plan: `article/literature/0B_LITERATURE_BATCH_PLAN.md`.
- Known PDF corpus available to the drafting AI: **`62` distinct works/documents**.
- 0B-01 analytical scope: **`8` assigned PDFs**.
- Target journal: `PENDING — to be decided in Phase 0D`.
- Manuscript drafting: not started.
- Chat language: Spanish.
- Article-workspace GitHub artifacts: Spanish + English with semantic equivalence.

### Frozen 0A ground truth

The governing downstream artifacts are:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

The frozen 0A-02 experimental cutoff was:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`.

The Master Plan remains a living source under exclusive experimental-workflow authority. No literature block may modify it or silently rewrite frozen historical ground truth.

### Formal opening of 0B

Phase 0B is open to build a **critical literature map and taxonomy** before defining the gap, contribution, or Research Questions.

The author reported that the drafting AI already has access to **62 distinct PDFs** for this phase after duplicate consolidation. At the reported cutoff, `37/62` already have an entry in the versioned GitHub bibliographic index and `25/62` do not yet have one. Missing GitHub indexing does not imply invalidity or exclusion, but provenance/admissibility must be governed before manuscript use.

Availability of all 62 PDFs does not remove controlled batches. A visible document not assigned to the active block remains `OUT_OF_SCOPE_FOR_CURRENT_BATCH` until its corresponding batch is opened.

The governing bibliographic protocol is `article/BIBLIOGRAPHIC_FRAMEWORK.md`, and the updated operational plan is `article/literature/0B_LITERATURE_BATCH_PLAN.md`.

### PDFs assigned to 0B-01

0B-01 analyzes only the eight works listed in the Spanish section. If the drafting AI can already access them fully in its conversation, they **must not be re-uploaded**. If one is inaccessible or unreadable in full, only that specific file should be requested.

The remaining PDFs in the 62-document corpus are reserved for 0B-02 and later batches when relevant. They may not be used inside 0B-01 to silently fill information gaps in the eight active papers.

### Authorized scope of 0B-01

The drafting AI must complete onboarding, read all eight assigned PDFs, build the critical paper-level matrix, distinguish `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, and `NO_VERIFICABLE_EN_PDF`, compare the required scientific dimensions, produce only provisional `CANDIDATE_GAP_ONLY` items, recommend a bibliographic role for each paper, and stop after 0B-01.

### Current prohibitions

During 0B-01, the drafting AI may not perform web search, search for new literature, analyze the other PDFs in the 62-document corpus, draft manuscript sections, declare novelty/final gap/superiority, advance beyond 0B-01, modify GitHub, or alter 0A/Master Plan.

Inherited references may be old, proceedings, theses, or preprints; their relevance is assessed in 0B. The 2022–2026, peer-reviewed-journal, and Q1/Q2 constraints apply to new academic literature under `BIBLIOGRAPHIC_FRAMEWORK.md`. Mere PDF availability does not automatically make a new reference `APPROVED_NEW`.

### 0B-01 gate

```text
drafting AI
-> internal scientific/editorial review
-> correction if required
-> author approval
-> 0B-01 closure
```

The experimental AI is not a mandatory literature reviewer. It will be involved only when a bibliographic interpretation directly affects experimental facts, experimental claims, or methodological restrictions under its authority.

### Later phases

- `0B-02` and later batches: `NOT_STARTED`.
- `0C — Gap, contribution, and Research Questions`: `BLOCKED` until 0A and 0B are complete.
- `0D — Editorial architecture and journal fit`: `BLOCKED` until 0C is complete.
- Target journal: **not yet selected or frozen**; it will be decided in 0D.
