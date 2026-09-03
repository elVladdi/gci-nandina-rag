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
- Estado de 0B-02: **`READY_FOR_DRAFTING`**.
- Prompt activo: `article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`.
- Plan de lotes: `article/literature/0B_LITERATURE_BATCH_PLAN.md`.
- Corpus PDF consolidado: `62` obras/documentos distintos; el flujo editorial dispone actualmente de acceso primario verificable al corpus completo `62/62`.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### 0B-01 — cierre formal

Estado final:

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

Correcciones integradas en el freeze:

1. P05 — Pain: `UN Comtrade commodity descriptions` = corpus de referencia/nomenclatura para ranking por similitud, no evidencia normativa equivalente al componente del proyecto actual.
2. P02 — Shubham et al.: conocimiento WCO/HS/KG usado durante selección de candidatos, no evidencia normativa posterior al ranking equivalente al proyecto actual.
3. Claims que un paper atribuye a terceros no migran a hechos independientes del manuscrito sin verificar la fuente primaria correspondiente.
4. P02 permanece `REVIEW_REQUIRED`; año final, venue y DOI no se completan por inferencia ni por fuente secundaria en 0B-01.

F1–F5 continúan exclusivamente como `CANDIDATE_GAP_ONLY` y pueden ser debilitados, falsados o reformulados por 0B-02/0B-03.

### 0B-02 — apertura formal

Objetivo: mapear literatura del corpus sobre retrieval, validación/corrección, conocimiento estructurado, explicabilidad y auditabilidad aduanera, distinguiendo cuidadosamente su función respecto de la arquitectura actual.

PDF asignados:

1. `Classification of Goods Using Text Descriptions With Sentences Retrieval.pdf`
2. `Text2Trade. A semantic search system whith Monte Carlo Droput Uncertainty Quantification For HS Code Retrieval..pdf`
3. `Explainable Product Classification for Customs.pdf`
4. `Application of machine learning for assessment of HS code correctness.pdf`
5. `Customs Tariff Classification and the Use of Assistive Technologies.pdf`
6. `Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities.pdf`

Los otros 56 documentos están `OUT_OF_SCOPE_FOR_CURRENT_BATCH`.

### Controles obligatorios de 0B-02

- Leer los seis PDF íntegramente.
- No usar web ni buscar literatura nueva.
- No completar silenciosamente el lote con otros PDF.
- Distinguir `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED`.
- Una afirmación secundaria citada por un paper no es un hecho independiente hasta verificar la fuente primaria.
- Distinguir code retrieval, sentence retrieval, precedent retrieval y evidence retrieval.
- Distinguir conocimiento/nomenclatura utilizado para seleccionar un código de evidencia normativa recuperada después del ranking.
- Distinguir explicabilidad model-centric de trazabilidad/auditabilidad documental.
- No inferir leakage por ausencia de group split documentado.
- No equiparar Top-k, accuracy, F1, MRR, uncertainty o rejection sin respetar sus definiciones y denominadores.
- Someter F1–F5 a presión explícita; no convertir supervivencia de candidatos en novelty.

### Gate de 0B-02

```text
IA de redacción
-> revisión científica/editorial interna contra PDF primarios
-> corrección si aplica
-> aprobación del autor
-> freeze de 0B-02
```

La IA experimental solo se incorporará si una interpretación bibliográfica afecta directamente un hecho experimental, claim experimental o restricción metodológica bajo su autoridad.

### Prohibiciones vigentes

No está autorizado durante 0B-02:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad;
- modificar 0A o el Plan Maestro;
- avanzar a 0B-03, 0C o fases posteriores;
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
- 0B-02 status: **`READY_FOR_DRAFTING`**.
- Active prompt: `article/prompts/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY.md`.
- Batch plan: `article/literature/0B_LITERATURE_BATCH_PLAN.md`.
- Consolidated PDF corpus: `62` distinct works/documents; the editorial workflow currently has primary verifiable access to `62/62`.
- Target journal: `PENDING — to be decided in Phase 0D`.
- Manuscript drafting: not started.

### Formal 0B-01 closure

```text
0B-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Canonical artifact: `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.

Records: `article/reviews/0B01_INTERNAL_REVIEW.md` and `article/reviews/0B01_AUTHOR_APPROVAL.md`.

The freeze incorporates the P05 and P02 terminology/provenance corrections, the primary-source rule for third-party claims, and P02's continuing `REVIEW_REQUIRED` metadata status. F1–F5 remain strictly `CANDIDATE_GAP_ONLY`.

### Formal 0B-02 opening

0B-02 analyzes only the six PDFs listed in the Spanish section: sentence retrieval, Text2Trade, explainable customs classification, HS-code correctness assessment, assistive technologies, and attribute-knowledge/KBGAT work. The other 56 documents remain `OUT_OF_SCOPE_FOR_CURRENT_BATCH`.

Mandatory controls include complete PDF reading; no web/new-literature search; provenance labels including `SECONDARY_CLAIM_UNVERIFIED`; distinction among code/sentence/precedent/evidence retrieval; distinction between nomenclature knowledge used for code selection and post-ranking normative evidence; distinction between model-centric explainability and documentary auditability; no leakage inference from missing grouped splits; metric-definition discipline; and explicit pressure testing of F1–F5 without novelty claims.

### 0B-02 gate

`drafting AI -> internal scientific/editorial review against primary PDFs -> correction if needed -> author approval -> freeze`

The experimental AI is involved only if literature interpretation directly affects experimental facts, claims, or methodological restrictions under its authority.

### Later phases

- `0B-03`: `NOT_STARTED`.
- `0B-04`: `NOT_STARTED`.
- `0B-05`: `NOT_STARTED`.
- `0B-06`: `NOT_STARTED`.
- `0C`: `BLOCKED` until 0B closes.
- `0D`: `BLOCKED` until 0C closes.
- Target journal: **not selected or frozen**; decision occurs in 0D.