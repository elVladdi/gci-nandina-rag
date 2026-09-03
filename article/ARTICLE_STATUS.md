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
- Bloque activo: **`0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera`**.
- Estado de 0B-02: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Dictamen interno 0B-02: **`PASS WITH MINOR CORRECTIONS`**.
- Revisión: `article/reviews/0B02_INTERNAL_REVIEW.md`.
- Prompt de origen: `article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`.
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

Registros:

- `article/reviews/0B01_INTERNAL_REVIEW.md`;
- `article/reviews/0B01_AUTHOR_APPROVAL.md`.

Correcciones congeladas: P05/UN Comtrade como corpus de referencia para ranking y no evidencia normativa; P02/WCO-HS como conocimiento usado durante selección y no evidencia normativa posterior; claims de terceros sujetos a verificación primaria; metadata P02 `REVIEW_REQUIRED`.

### 0B-02 — revisión interna completada

PDF revisados:

1. `Classification of Goods Using Text Descriptions With Sentences Retrieval.pdf`
2. `Text2Trade. A semantic search system whith Monte Carlo Droput Uncertainty Quantification For HS Code Retrieval..pdf`
3. `Explainable Product Classification for Customs.pdf`
4. `Application of machine learning for assessment of HS code correctness.pdf`
5. `Customs Tariff Classification and the Use of Assistive Technologies.pdf`
6. `Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities.pdf`

Los otros 56 documentos permanecen `OUT_OF_SCOPE_FOR_0B02`.

Dictamen:

```text
0B-02 INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = PENDING
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Correcciones/normalizaciones gobernantes para el futuro freeze:

1. **P01:** distinguir el universo disponible/filtrado del test temporal efectivo. El test final es 1,652 casos y la validación previa 1,835. HS6 Top-3 = 0.955 sin retrieved sentences y 0.937 con retrieved sentences; no atribuir 0.955 al pipeline con sentence retrieval.
2. **P03:** tabla total = 17,068 coreanos + 209,635 internacionales = 226,703; split descrito = 201,435 train + 5,000 validation + 5,000 test = 211,435; los 15,268 restantes no tienen disposición explícita en el PDF y deben quedar `NO_VERIFICABLE_EN_PDF`.
3. **P03 encuesta:** helpfulness operativo = 65.7 % con score 4–5; `>85 %` corresponde a accuracy percibida ≥3. La frase introductoria de 85 % helpful es inconsistente con el cuerpo. Reducción de tiempo/esfuerzo = percepción, no medición causal.
4. **Caveats P02/P04/P06:** Text2Trade sigue `REVIEW_REQUIRED`, su sector analysis no es validación externa y 171,247+37,794=209,041 frente a “≈208,000”; P04 ≈84.23 % de scores 3–4 presupone códigos históricos correctos y no mide detección de misclasificación real; P06 imprime Recall=`TP/(TP+TN)`, por lo que F1 se conserva solo como valor reportado con caveat, y su CV por triples no demuestra independencia por mercancía/declaración ni leakage.

### Candidatos a gap tras 0B-02

Todos continúan **provisionales** y no constituyen novelty:

- F1: `CANDIDATE_GAP_ONLY — NARROWED` a ranking fijado por precedentes históricos + evidencia normativa solo posterior y no reordenadora.
- F2: `CANDIDATE_GAP_ONLY — NARROWED` a generador posterior restringido a Top-k fijo, sin códigos externos ni reordenamiento.
- F3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- F4: `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION` entre retrieval/coherence/corrección sustantiva.
- F5: `CANDIDATE_GAP_ONLY — NARROWED` a evaluación formal y separada de trazabilidad/auditabilidad documental.
- G6: `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM` sobre ground truth independiente para correctness.

### Gate vigente de 0B-02

```text
revisión interna completada
-> aprobación expresa del autor
-> integración C1–C4
-> creación/freeze del artefacto canónico 0B-02
-> apertura de 0B-03
```

No es necesaria una nueva ejecución completa de la IA de redacción. No se requiere IA experimental porque la revisión no modifica ground truth ni claims experimentales.

### Prohibiciones vigentes

Hasta recibir aprobación expresa del autor de 0B-02 no está autorizado:

- marcar 0B-02 `APPROVED / FROZEN`;
- abrir o ejecutar 0B-03;
- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad;
- modificar 0A o el Plan Maestro;
- usar resultados experimentales pendientes como cerrados;
- convertir secondary claims en hechos sin verificación primaria.

### Fases posteriores

- `0B-03`: `NOT_STARTED`.
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
- Phase `0A`: **`CLOSED / APPROVED`**.
- `0A-01`: **`APPROVED / FROZEN`**.
- `0A-02`: **`APPROVED / FROZEN`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- `0B-01 — Direct HS classification and supervised learning`: **`APPROVED / FROZEN`**.
- Active block: **`0B-02 — Retrieval, validation, knowledge, and customs auditability`**.
- 0B-02 status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**.
- Review record: `article/reviews/0B02_INTERNAL_REVIEW.md`.
- Consolidated corpus: 62 distinct works/documents; primary verifiable access `62/62`.
- Target journal: pending until Phase 0D.
- Manuscript drafting: not started.

### Formal 0B-01 closure

`0B-01 = APPROVED / FROZEN`; internal review passed with minor corrections; author approval received; no experimental review required. Canonical artifact: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.

### 0B-02 internal review complete

The six PDFs listed in the Spanish section were independently checked against their primary documents. The other 56 documents remain outside 0B-02 scope.

```text
0B-02 INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = PENDING
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Governing corrections for the future freeze:

1. **P01:** distinguish available/filtered data from the actual temporal test. Final test = 1,652 cases; prior validation = 1,835. HS6 Top-3 is 0.955 without retrieved sentences and 0.937 with retrieved sentences; do not assign 0.955 to the sentence-retrieval pipeline.
2. **P03:** data table total = 17,068 Korean + 209,635 international = 226,703; explicit split = 201,435 train + 5,000 validation + 5,000 test = 211,435. The disposition of the remaining 15,268 records is not explicitly stated and must remain `NOT_VERIFIABLE_IN_PDF`.
3. **P03 survey:** operational helpfulness = 65.7% scoring 4–5; `>85%` refers to perceived accuracy ≥3. The introduction's 85% helpfulness wording is internally inconsistent. Time/effort reduction is perceptual rather than causal evidence.
4. **P02/P04/P06 caveats:** Text2Trade remains `REVIEW_REQUIRED`, its sector analysis is not external validation, and 171,247+37,794=209,041 versus “≈208,000”; P04's ≈84.23% scores 3–4 assume historical labels are correct and do not measure true misclassification detection; P06 prints Recall=`TP/(TP+TN)`, so F1 values remain author-reported with a metric caveat, and triple-level CV does not establish commodity/declaration independence or leakage.

### Candidate-gap status after 0B-02

All remain provisional and do not establish novelty:

- F1: `CANDIDATE_GAP_ONLY — NARROWED`.
- F2: `CANDIDATE_GAP_ONLY — NARROWED`.
- F3: `CANDIDATE_GAP_ONLY — SURVIVES THIS BATCH`.
- F4: `CANDIDATE_GAP_ONLY — SUPPORTED AS A METHODOLOGICAL DISTINCTION`.
- F5: `CANDIDATE_GAP_ONLY — NARROWED`.
- G6: `CANDIDATE_GAP_ONLY — NEW, METHODOLOGICAL; NOT A NOVELTY CLAIM`.

### Current 0B-02 gate

`internal review complete -> explicit author approval -> integrate C1–C4 -> freeze canonical 0B-02 artifact -> open 0B-03`.

A full drafting-AI rerun is not required. Experimental-AI review is not required because no frozen experimental ground truth or claim was changed.

### Later phases

- `0B-03` through `0B-06`: `NOT_STARTED`.
- `0C`: `BLOCKED` until 0B closes.
- `0D`: `BLOCKED` until 0C closes.
- Target journal: not selected or frozen; decision occurs in 0D.
