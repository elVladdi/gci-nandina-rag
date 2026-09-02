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

La Fase 0B queda abierta para construir un **mapa crítico de literatura y taxonomía** antes de definir gap, contribución o Research Questions.

0B se ejecutará por lotes temáticos controlados. El primer lote es `0B-01` y se limita al núcleo heredado de trabajos sobre clasificación/asignación HS mediante aprendizaje supervisado, deep learning, transfer learning y representaciones de texto.

El protocolo bibliográfico aplicable es `article/BIBLIOGRAPHIC_FRAMEWORK.md` y el plan operativo de lotes es `article/literature/0B_LITERATURE_BATCH_PLAN.md`.

### PDF requeridos para 0B-01

El autor debe adjuntar a la IA de redacción exactamente estos ocho archivos:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

La lectura debe ser íntegra. No se autoriza sustituir un PDF faltante por abstract, snippet web, conocimiento general o referencia secundaria.

### Alcance autorizado de 0B-01

La IA de redacción debe:

- completar el onboarding de la rama;
- leer los ocho PDF completos;
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
- redactar secciones del manuscrito;
- declarar novelty, gap definitivo o superioridad;
- avanzar a 0B-02, 0C o fases posteriores;
- modificar GitHub desde la IA de redacción;
- alterar 0A o el Plan Maestro.

Las referencias heredadas pueden ser antiguas, proceedings, tesis o preprints; su pertinencia se evalúa en 0B. Las reglas 2022–2026, journal peer-reviewed y Q1/Q2 aplican únicamente a **nueva** literatura académica que eventualmente se busque en un lote posterior y con autorización expresa.

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

Phase 0B is opened to build a **critical literature map and taxonomy** before defining the gap, contribution, or Research Questions.

0B will be executed through controlled thematic batches. The first batch is `0B-01`, limited to inherited core work on HS classification/assignment through supervised learning, deep learning, transfer learning, and text representations.

The governing bibliographic protocol is `article/BIBLIOGRAPHIC_FRAMEWORK.md`, and the operational batch plan is `article/literature/0B_LITERATURE_BATCH_PLAN.md`.

### Required PDFs for 0B-01

The author must attach to the drafting AI exactly the eight files listed in the Spanish section. Each must be read in full. A missing PDF may not be replaced with an abstract, web snippet, general knowledge, or secondary reference.

### Authorized scope of 0B-01

The drafting AI must complete onboarding, read all eight PDFs, build the critical paper-level matrix, distinguish `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, and `NO_VERIFICABLE_EN_PDF`, compare the required scientific dimensions, produce only provisional `CANDIDATE_GAP_ONLY` items, recommend a bibliographic role for each paper, and stop after 0B-01.

### Current prohibitions

During 0B-01, the drafting AI may not perform web search, search for new literature, draft manuscript sections, declare novelty/final gap/superiority, advance beyond 0B-01, modify GitHub, or alter 0A/Master Plan.

Inherited references may be old, proceedings, theses, or preprints; their relevance is assessed in 0B. The 2022–2026, peer-reviewed journal, and Q1/Q2 constraints apply only to **new** academic literature that may later be searched under explicit authorization.

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
