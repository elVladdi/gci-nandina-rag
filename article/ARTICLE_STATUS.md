# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04A`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`APPROVED / FROZEN`**.
- `0B-05A`: **`APPROVED / FROZEN`**.
- `0B-05B`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales`**.
- Estado de `0B-05C`: **`READY_FOR_DRAFTING`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG`: **`OPEN_FOR_AUDIT`**.
- `0B-06`: **`NOT_STARTED / CLOSED_BY_GATE`**.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Corpus académico/documental consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth y gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

La Fase 0B no modifica el Plan Maestro ni 0A. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro y sobre decisiones experimentales correctivas.

0B-05C puede detectar `SOURCE_VERSION_DRIFT`, pero no puede actualizar el corpus, rerun experimentos, recalcular resultados ni reinterpretar claims congelados. Si el audit confirma o deja razonablemente abierta una afectación material del experimento, debe activarse revisión de la IA experimental.

### Distinciones fundacionales congeladas

0B-04A:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

0B-05A:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

0B-05B:

- `data`, `information` y `knowledge` no son sinónimos universales ni etapas lineales necesarias;
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`;
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`;
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`;
- `DOCUMENTED_EXPLICIT_KNOWLEDGE` es solo `OPERACIONALIZACION_DEL_PROYECTO`.

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`; solo permanece el candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida.
- **G6:** `ELIMINATED AS GAP CANDIDATE`.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-05C no está autorizado a cambiar estos estados; solo puede aportar fronteras metodológicas y evidencia documental oficial.

### 0B-05B — cierre formal

Registros gobernantes:

- `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`;
- `article/reviews/0B05B_INTERNAL_REVIEW.md`;
- `article/reviews/0B05B_AUTHOR_APPROVAL.md`;
- `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.

Estado: **`APPROVED / FROZEN`**; `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

### 0B-05C — apertura formal

Alcance:

`article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Prompt activo:

`article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

#### Snapshot experimental que debe preservarse

Ref de desarrollo congelado por 0A-02:

`95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

Fuentes normativas de ingesta confirmadas:

- `data/external/Arancel 2022.pdf`;
- `data/processed/corpus/arancel/arancel2022_run_metadata.json`;
- `data/external/CAN Desición 885 - Nanadina Gaceta 4359.pdf`;
- `data/processed/corpus/nandina/run_metadata.json`.

SHA-256 fuente registrados:

- Arancel 2022: `a01a029e1ca29b6debc61d219c17dfc086354e00669246cc24a91ad9f454c7d0`;
- Decisión 885/Gaceta 4359: `8c4a30fb0328f151089ac4c7857ac447d3dd353de97122a11bde4550d594f0c6`.

#### Fuentes oficiales a auditar

- WCO/OMA: HS Convention cuando sea necesario, HS Nomenclature 2022, GIR 2022, enmiendas complementarias relevantes y estatus de Explanatory Notes solo para claims que lo requieran.
- Comunidad Andina: Decisión 885/Gaceta 4359; Decisión 906/Gaceta 5062; Resolución 2592/Gaceta 5761; otros instrumentos solo si son necesarios para Capítulo 87/vigencia.
- Perú: DS 404-2021-EF/Arancel de Aduanas 2022; modificaciones materialmente pertinentes; SUNAT/gob.pe NANDINA como orientación institucional; DESPA-PG.01 v8 y DESPA-PE.00.03 v4 únicamente para claims de procedencia/contexto administrativo.

La consulta web oficial está autorizada y exigida. La evidencia final debe proceder de WCO/OMA, Comunidad Andina, SUNAT, gob.pe, MEF o El Peruano.

#### Flag preliminar de drift

Durante la definición de 0B-05C se comprobó en la Gaceta Oficial de la Comunidad Andina que la **Decisión 906** modifica la Decisión 885, entra en vigencia `2023-01-01` e incluye cambios en el **Capítulo 87**, entre ellos las subpartidas `8704.41.10` y `8704.51.10`.

La lista congelada de 42 labels EVAL v0.2 no contiene esos dos códigos. Esto no permite declarar impacto cero porque queda por comprobar si aparecen como candidatos, históricos o evidencia.

Estado:

`PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`.

0B-05C debe separar:

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

Si el solapamiento experimental se confirma o permanece razonablemente posible, el entregable debe devolver `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED`. No debe intentar resolverlo.

La Resolución 2592 de 2026 se identificó preliminarmente como Notas Explicativas Complementarias para capítulos 1–22 y no constituye por sí sola evidencia de afectación directa a Capítulo 87.

### Gate vigente

```text
0B-05C = READY_FOR_DRAFTING
-> IA de análisis documental
-> auditoría de fuentes oficiales
-> revisión científica/editorial interna
-> IA experimental SI el trigger de impacto queda confirmado/abierto materialmente
-> corrección/normalización si aplica
-> aprobación expresa del autor
-> freeze 0B-05C
-> evaluar necesidad de 0B-06
```

### Prohibiciones vigentes

Durante 0B-05C no está autorizado:

- modificar Plan Maestro o 0A;
- sustituir retrospectivamente las fuentes usadas por el experimento;
- modificar/actualizar el corpus normativo;
- rerun experimentos o recalcular resultados;
- inferir legal correctness desde oficialidad o trazabilidad;
- confundir HS-6, NANDINA-8 y subpartida nacional de 10 dígitos;
- tratar una página institucional de orientación como sustituto del instrumento comunitario;
- redactar el manuscrito;
- declarar novelty/gap definitivo;
- abrir 0B-06 o 0C.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01 through 0B-05B: **`APPROVED / FROZEN`**.
- Active block: **`0B-05C — Authority, currency, and traceability of normative/official sources`**.
- 0B-05C: **`READY_FOR_DRAFTING`**.
- `PRELIMINARY_SOURCE_VERSION_DRIFT_FLAG = OPEN_FOR_AUDIT`.
- 0B-06: `NOT_STARTED / CLOSED_BY_GATE`.
- 0C/0D remain blocked.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governance

Frozen 0A artifacts remain authoritative. 0B-05C may detect source-version drift but cannot update the corpus, rerun experiments, recalculate results, reinterpret frozen claims, or modify the Master Plan. The experimental AI retains exclusive authority over the Master Plan and experimental corrective decisions.

### 0B-05C formal opening

Scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Active prompt: `article/prompts/0B05C_OFFICIAL_NORMATIVE_SOURCE_AUTHORITY_CURRENCY_TRACEABILITY.md`.

The batch compares `EXPERIMENTAL_SOURCE_SNAPSHOT` with `CURRENT_OFFICIAL_SOURCE_STATE`.

The frozen development snapshot at `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` identifies Arancel 2022 and CAN Decision 885/Gazette 4359 as ingested normative sources, together with their pipeline run metadata and recorded source-file SHA-256 values.

The controlled official set covers WCO HS 2022/GIR and needed amendments; Andean Decision 885, Decision 906, Resolution 2592 and only other instruments necessary for Chapter-87 currency; Peru DS 404-2021-EF/material amendments; and SUNAT sources only for specific institutional/administrative provenance claims.

Current official web verification is required and final evidence is limited to official WCO/Andean Community/SUNAT/gob.pe/MEF/El Peruano sources.

A preliminary flag is open: Decision 906, effective 2023-01-01, modifies Decision 885 and includes Chapter-87 changes, including 8704.41.10 and 8704.51.10. Those codes are absent from the frozen 42 EVAL reference labels, but zero experimental impact cannot be inferred until candidate/historical/evidence overlap is checked.

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

If material overlap is confirmed or reasonably remains open, the deliverable must return `EXPERIMENTAL_IMPACT_REVIEW_REQUIRED` without altering frozen experimental artifacts.

Resolution 2592 was preliminarily identified as complementary explanatory notes for Chapters 1–22 and therefore does not by itself establish Chapter-87 impact.

### Gate

`0B-05C READY_FOR_DRAFTING -> official-source analysis -> internal scientific/editorial review -> experimental AI if impact trigger is confirmed/materially open -> correction/normalization if needed -> express author approval -> freeze -> assess 0B-06 need`.

No Master-Plan/0A changes, corpus updates, reruns, manuscript drafting, final novelty/gap declarations, 0B-06, or 0C are authorized while 0B-05C remains open.
