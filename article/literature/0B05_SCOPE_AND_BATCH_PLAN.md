# 0B-05 — Datos, procedencia, reproducibilidad, conocimiento y fuentes normativas / Data, provenance, reproducibility, knowledge, and normative sources

## Español

### 1. Propósito

`0B-05` completa el mapa bibliográfico de la Fase 0B en tres dimensiones que no deben confundirse entre sí:

1. **documentación y gobernanza de datos**;
2. **procedencia, trazabilidad, reproducibilidad y auditoría del ciclo de vida**;
3. **fundamentos conceptuales de información/conocimiento y autoridad documental de fuentes normativas oficiales**.

El bloque no busca demostrar novelty. Su función es establecer qué puede sostenerse científicamente cuando el artículo describa el banco histórico, el corpus normativo, su versionamiento, la trazabilidad de artefactos, la reproducibilidad del experimento, el conocimiento explícito documental y el carácter autoritativo —pero no automáticamente suficiente— de las fuentes regulatorias.

Debe impedir equivalencias inválidas como:

- `documentar un dataset = demostrar que el dataset es adecuado`;
- `versionar = reproducir`;
- `provenance = correctness`;
- `traceability = auditability completa`;
- `reproducibility = external replication/generalization`;
- `audit trail = legal correctness`;
- `documento normativo recuperado = aplicación jurídica correcta`;
- `conocimiento explícito documental = totalidad del conocimiento experto`.

### 2. Criterio de partición

Por heterogeneidad conceptual, 0B-05 se divide en tres sub-lotes. Solo uno puede estar abierto a la vez.

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`APPROVED / FROZEN`**.

Registros:

- Prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.
- Revisión interna: `article/reviews/0B05A_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación del autor: `article/reviews/0B05A_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Lote congelado:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

La identidad científica del tercer archivo es **FAIR data pipeline: provenance-driven data management for traceable scientific workflows**.

Fronteras congeladas:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

Estas fronteras no constituyen una escala lineal de madurez ni una cadena de implicación.

C1–C7 integradas:

- Bender & Friedman: documentación/contextualización; casos post hoc y value scenarios no prueban efectos causales.
- Gebru: copia analizada `arXiv:1803.09010v8 — 1 Dec 2021`; metadata editorial final `REVIEW_REQUIRED_FOR_FINAL_CITATION`; no homogeneizar su uso de reproducibility con Pineau.
- FAIR Data Pipeline: núcleo = provenance/lineage + version identification; full reproducibility no es core requirement.
- Pineau: `reproducible ≠ replicable ≠ robust ≠ generalisable` como convención operacional del paper; asociaciones no causales.
- Raji: SMACTR = cinco etapas; Post-Audit no es sexta etapa; lifecycle auditability no equivale a formal per-output, external independent audit o legal correctness.
- Taxonomía cruzada: fronteras metodológicas, no escalera.

Impacto metodológico congelado:

- F1/F2: sin evidencia de novelty.
- F3: `METHOD_FOUNDATION_RELEVANT`; documentar relaciones, curación y particiones no equivale a controlar dependencia ni demostrar independencia.
- F4: `METHOD_BOUNDARY_RELEVANT`; provenance/reproducibility/auditability permanecen separados de substantive/legal correctness.
- F5: `METHOD_CONTRAST_RELEVANT`; existe prior art fuerte en provenance, transparency trails e internal audit. Queda prohibida cualquier formulación amplia de ausencia de trazabilidad/auditabilidad. Solo permanece el candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida, todavía sin novelty.
- G6 permanece eliminado; G7 permanece absorbido en F2.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

El freeze de 0B-05A habilita ahora únicamente la **definición formal** de 0B-05B. Antes de abrirlo deben confirmarse las fuentes primarias, fijarse el lote final y crearse un prompt ejecutable.

Fuentes candidatas heredadas, sujetas a confirmación primaria:

- `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`;
- `The Duality of Knowledge.pdf`;
- `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`, si se confirma acceso al PDF primario completo del corpus heredado.

Objetivo previsto:

- delimitar `data`, `information`, `documented/explicit knowledge` y conocimiento tácito/no codificado;
- evitar una transformación automática tipo DIKW si las fuentes no la sostienen;
- precisar en qué sentido un corpus normativo puede describirse como conocimiento explícito documental;
- preservar que recuperación/documentación de conocimiento explícito no sustituye conocimiento experto, interpretación o juicio profesional.

0B-05B seguirá siendo fundacional y no podrá declarar novelty ni gap definitivo.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse después del freeze de 0B-05B y de verificar qué fuentes oficiales primarias del corpus vigente requieren auditoría documental adicional.

Su función será una **auditoría de fuente primaria oficial** separada, siguiendo `article/BIBLIOGRAPHIC_FRAMEWORK.md`: autoridad emisora, versión, vigencia, fecha, alcance, jerarquía documental, identificador/enlace estable y función evidencial. WCO/OMA, Comunidad Andina y SUNAT no se tratarán como artículos científicos ni sustituirán literatura académica cuando el claim sea metodológico.

### 3. Relación con freezes previos

0B-05 no reabre:

- 0A-01 ni 0A-02;
- resultados experimentales congelados;
- 0B-01 a 0B-04B;
- 0B-05A una vez congelado;
- G6, eliminado;
- G7, absorbido en F2.

La IA experimental no fue requerida en 0B-05A porque ninguna interpretación bibliográfica modificó hechos/claims experimentales congelados ni restricciones bajo su autoridad.

### 4. Gate

0B-05A completó:

`IA de redacción -> revisión interna -> aprobación expresa del autor -> freeze`.

Siguiente gate permitido:

`confirmar fuentes primarias 0B-05B -> definir lote final -> crear prompt ejecutable -> READY_FOR_DRAFTING -> IA de redacción -> revisión interna -> aprobación expresa del autor -> freeze -> evaluar apertura de 0B-05C`.

0B-05C permanece cerrado hasta completar ese gate.

### 5. Prohibiciones vigentes

Mientras 0B permanezca abierto:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva salvo apertura explícita de 0B-06;
- no confundir conocimiento explícito documental con totalidad del conocimiento experto;
- no convertir fuentes normativas recuperadas en prueba automática de aplicación jurídica correcta;
- no modificar 0A ni el Plan Maestro;
- no reabrir G6/G7;
- no abrir 0B-05C, 0B-06 o 0C antes del gate correspondiente.

---

## English

### 1. Purpose

`0B-05` completes the Phase-0B literature map across three distinct dimensions: data documentation/governance; provenance, traceability, reproducibility, and lifecycle audit; and conceptual information/knowledge plus official normative-source authority.

The block is not a novelty search. It prevents invalid equivalences such as documentation = dataset adequacy, versioning = reproducibility, provenance = correctness, reproducibility = external replication/generalization, audit trail = legal correctness, retrieved normative document = correct legal application, or documented explicit knowledge = the entirety of expert knowledge.

### 2. Controlled sub-batches

#### 0B-05A — Data documentation, provenance, reproducibility, and audit trail

Status: **`APPROVED / FROZEN`**.

Governing records are its prompt, internal review, author approval, and canonical frozen artifact `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`. Experimental review was `NOT_REQUIRED`.

Frozen boundaries:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

C1–C7 are integrated. F3 gains documentation foundation only; F4 remains a correctness boundary; F5 is narrowed by strong prior art on provenance, transparency trails, and internal audit to the still-provisional candidate of formal, explicit, separate documentary output-level auditability evaluation. G6 remains eliminated and G7 remains merged into F2.

#### 0B-05B — Information, documented explicit knowledge, and limits of codified knowledge

Status: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

The 0B-05A freeze only authorizes the formal definition of 0B-05B. Primary-source access must first be confirmed, then a final controlled batch and executable prompt must be created.

Candidate inherited sources are Zins on conceptual approaches to data/information/knowledge; Hildreth & Kimble on the duality of knowledge; and the inherited knowledge-management/tacit-knowledge paper only if complete primary-PDF access is confirmed.

The planned objective is to distinguish data, information, documented/explicit knowledge, and tacit/non-codified knowledge; reject automatic DIKW transformation unless supported; clarify the legitimate sense in which a normative corpus can be treated as documented explicit knowledge; and preserve that document retrieval does not replace expert interpretation or judgment.

#### 0B-05C — Authority, currency, and traceability of normative/official sources

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may be defined only after 0B-05B freezes. It will be a separate official-primary-source audit covering issuing authority, version, currency, date, scope, documentary hierarchy, stable identifiers, and evidentiary role for WCO, Andean Community, SUNAT, and other relevant official sources.

### 3. Prior freezes and experimental governance

0B-05 does not reopen 0A, frozen experiments, 0B-01 through 0B-04B, or frozen 0B-05A. G6/G7 remain closed as previously decided. Experimental-AI review was not required in 0B-05A because no frozen experimental fact/claim or authority restriction was changed.

### 4. Gate

0B-05A completed the drafting-AI -> internal-review -> author-approval -> freeze cycle.

Next permitted gate: confirm 0B-05B primary sources -> define final batch -> create executable prompt -> READY_FOR_DRAFTING -> drafting AI -> internal review -> author approval -> freeze -> assess opening 0B-05C.

### 5. Prohibitions

While 0B remains open, manuscript drafting, final novelty/gap claims, new-literature search outside an explicitly opened 0B-06, conflating documented explicit knowledge with all expert knowledge, treating retrieved official documents as automatic legal correctness, Master-Plan/0A modification, reopening G6/G7, or opening 0B-05C/0B-06/0C before their gates remain prohibited.
