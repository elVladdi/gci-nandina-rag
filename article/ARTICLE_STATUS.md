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
- Estado de `0B-01`: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Dictamen interno: **`PASS WITH MINOR CORRECTIONS`**.
- Revisión: `article/reviews/0B01_INTERNAL_REVIEW.md`.
- Prompt de origen: `article/prompts/0B01_HS_CLASSIFICATION_CORE_LITERATURE.md`.
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

### Estado de 0B-01 después de revisión interna

La IA de redacción completó el análisis de los ocho PDF asignados y se realizó una verificación científica/editorial independiente contra los documentos primarios.

El dictamen interno es **`PASS WITH MINOR CORRECTIONS`**. Las correcciones son acotadas y deterministas; no requieren una nueva ejecución analítica completa por la IA de redacción ni revisión de la IA experimental.

Correcciones gobernantes para la versión canónica de 0B-01:

1. **P05 — Pain (2021):** las descripciones de commodities del `UN Comtrade sheet` deben tratarse como corpus de referencia/nomenclatura utilizado para ranking por similitud, no como `evidencia normativa` equivalente a la recuperación normativa del proyecto actual.
2. **P02 — Shubham et al.:** el conocimiento derivado de WCO/HS/KG utilizado durante selección debe distinguirse de la evidencia normativa recuperada después del ranking en el proyecto actual. P02 permanece `REVIEW_REQUIRED` por metadata editorial incompleta y limitaciones de trazabilidad del protocolo.
3. Las afirmaciones que los papers atribuyan a fuentes terceras no pueden convertirse en hechos independientes del manuscrito sin verificar la fuente primaria correspondiente.
4. P02 no puede recibir año final, venue o DOI por inferencia o por una fuente secundaria dentro del cierre de 0B-01.

La revisión confirmó además que P08 sí documenta envío de casos rechazados a procesamiento manual; P07 es una tesis de maestría y deben mantenerse separadas `accuracy = 0.62` y `weighted F1 = 0.61`; y el 90 % de P04 no es comparable con una accuracy general de clasificación HS multiclase.

Los cinco elementos F1–F5 permanecen exclusivamente como `CANDIDATE_GAP_ONLY`. No constituyen todavía gap ni novelty.

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

Los otros PDF del corpus de 62 continúan fuera de alcance para 0B-01 y se reservarán para sus lotes correspondientes.

### Próximo gate autorizado

La única transición autorizada ahora es:

```text
revisión interna 0B-01 completada
-> aprobación expresa del autor de 0B-01 con las correcciones registradas
-> creación/congelamiento del artefacto canónico 0B-01
-> 0B-01 = APPROVED / FROZEN
-> apertura de 0B-02
```

No debe iniciarse 0B-02 antes de la aprobación expresa del autor.

### Prohibiciones vigentes

Mientras 0B-01 permanezca pendiente de aprobación del autor no está autorizado:

- redactar secciones del manuscrito;
- declarar novelty, gap definitivo o superioridad;
- abrir 0B-02, 0C o fases posteriores;
- modificar el Plan Maestro desde el flujo del artículo;
- convertir afirmaciones secundarias de los papers en hechos sin verificación primaria;
- cerrar silenciosamente la metadata `REVIEW_REQUIRED` de P02.

Las referencias heredadas pueden ser antiguas, proceedings, tesis o preprints; su pertinencia se evalúa en 0B. Las reglas 2022–2026, journal peer-reviewed y Q1/Q2 aplican a literatura académica nueva según `BIBLIOGRAPHIC_FRAMEWORK.md`.

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
- `0B-01` status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**.
- Review: `article/reviews/0B01_INTERNAL_REVIEW.md`.
- Source prompt: `article/prompts/0B01_HS_CLASSIFICATION_CORE_LITERATURE.md`.
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

### 0B-01 status after internal review

The drafting AI completed the analysis of the eight assigned PDFs, followed by an independent scientific/editorial verification against the primary documents.

The internal verdict is **`PASS WITH MINOR CORRECTIONS`**. The corrections are bounded and deterministic; they do not require a full analytical rerun by the drafting AI or review by the experimental AI.

Governing corrections for the canonical 0B-01 version:

1. **P05 — Pain (2021):** commodity descriptions from the `UN Comtrade sheet` must be treated as a reference/nomenclature corpus used for similarity ranking, not as `normative evidence` equivalent to the current project's normative retrieval.
2. **P02 — Shubham et al.:** WCO/HS/KG-derived knowledge used during selection must be distinguished from post-ranking normative evidence retrieval in the current project. P02 remains `REVIEW_REQUIRED` because of incomplete editorial metadata and protocol-traceability limitations.
3. Statements attributed by the papers to third-party sources may not become independent manuscript facts without verification of the corresponding primary source.
4. P02 must not be assigned a final year, venue, or DOI by inference or from a secondary source during 0B-01 closure.

The review also confirmed that P08 explicitly sends rejected cases to manual processing; P07 is a Master's thesis and `accuracy = 0.62` must remain distinct from `weighted F1 = 0.61`; and P04's 90% result is not comparable with general multiclass HS-classification accuracy.

All five F1–F5 items remain strictly `CANDIDATE_GAP_ONLY`. They are not yet a gap or novelty claim.

### PDFs assigned to 0B-01

0B-01 covers only the eight works listed in the Spanish section. The remaining PDFs in the 62-document corpus remain out of scope for 0B-01 and are reserved for their corresponding batches.

### Next authorized gate

The only authorized transition is now:

```text
0B-01 internal review complete
-> explicit author approval of 0B-01 with the recorded corrections
-> create/freeze canonical 0B-01 artifact
-> 0B-01 = APPROVED / FROZEN
-> open 0B-02
```

0B-02 must not start before explicit author approval.

### Current prohibitions

While 0B-01 is awaiting author approval, the workflow may not draft manuscript sections; declare novelty, final gap, or superiority; open 0B-02, 0C, or later phases; modify the Master Plan from the article workflow; turn papers' secondary statements into facts without primary verification; or silently close P02's `REVIEW_REQUIRED` metadata.

Inherited references may be old, proceedings, theses, or preprints; their relevance is assessed in 0B. The 2022–2026, peer-reviewed-journal, and Q1/Q2 constraints apply to new academic literature under `BIBLIOGRAPHIC_FRAMEWORK.md`.

### Later phases

- `0B-02` and later batches: `NOT_STARTED`.
- `0C — Gap, contribution, and Research Questions`: `BLOCKED` until 0A and 0B are complete.
- `0D — Editorial architecture and journal fit`: `BLOCKED` until 0C is complete.
- Target journal: **not yet selected or frozen**; it will be decided in 0D.
