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

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt:

`article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

Revisión interna:

`article/reviews/0B05A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

Lote final:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

La identidad científica del tercer archivo es **FAIR Data Pipeline: provenance-driven data management for traceable scientific workflows**; se conserva el nombre físico del archivo suministrado para localizar la copia analizada.

La revisión primaria acepta como fronteras gobernantes:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

Y:

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

Estas expresiones son fronteras metodológicas, no una escala lineal de madurez ni una cadena de implicación.

Correcciones obligatorias para el eventual freeze:

- **C1 Bender & Friedman:** data statements = documentación/contextualización; casos post hoc y value scenarios no prueban efectos causales sobre bias, calidad, generalización o reproducibilidad.
- **C2 Gebru metadata:** la copia analizada gobierna como `arXiv:1803.09010v8 — 1 Dec 2021`; metadata editorial final = `REVIEW_REQUIRED_FOR_FINAL_CITATION` / no verificable en la copia, sin reconstrucción silenciosa.
- **C3 Gebru vs Pineau:** no homogeneizar el significado de reproducibility entre ambos papers.
- **C4 FAIR Data Pipeline:** núcleo = provenance/lineage + identificación de versiones; full reproducibility es deseable, pero los autores declaran que no es core requirement.
- **C5 Pineau:** conservar `reproducible ≠ replicable ≠ robust ≠ generalisable` como convención operacional del paper y no causalizar asociaciones del programa.
- **C6 Raji:** SMACTR = cinco etapas; Post-Audit no es sexta etapa; transparency trail/ADHF = lifecycle auditability, no formal per-output auditability, auditoría externa independiente ni legal correctness.
- **C7 Taxonomía cruzada:** documentación, identity/versioning, provenance, reproducibility y audit trail deben permanecer separados y ninguno garantiza automáticamente la propiedad siguiente.

El análisis no contiene errores materiales; no se requiere devolución a la IA de redacción antes del gate de autor.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse y abrirse después del freeze de 0B-05A.

Fuentes candidatas heredadas, sujetas a confirmación primaria antes de apertura:

- `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`;
- `The Duality of Knowledge.pdf`;
- `Knowledge Management: Re-thinking Information Management and Facing the Challenge of Managing Tacit Knowledge` únicamente si se confirma acceso al PDF primario completo dentro del corpus heredado.

Objetivo previsto: delimitar `data`, `information`, `documented/explicit knowledge`, conocimiento tácito/no codificado y el alcance legítimo de describir un corpus normativo como conocimiento explícito documental. No se permitirá presentar la recuperación documental como sustituto de conocimiento experto ni adoptar una pirámide DIKW como transformación automática si las fuentes no la sostienen.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / CLOSED_BY_GATE`**.

Solo podrá definirse después del freeze de 0B-05B y de verificar qué fuentes oficiales primarias del corpus vigente requieren auditoría documental adicional.

Su función no será una revisión académica, sino una **auditoría de fuente primaria oficial** separada, siguiendo `article/BIBLIOGRAPHIC_FRAMEWORK.md`: autoridad emisora, versión, vigencia, fecha, alcance, jerarquía documental, identificador/enlace estable y función evidencial. Las fuentes WCO/OMA, Comunidad Andina y SUNAT no se tratarán como artículos científicos ni se usarán para sustituir literatura académica cuando el claim sea metodológico.

### 3. Relación con los freezes previos

0B-05 no reabre:

- 0A-01 ni 0A-02;
- los resultados experimentales congelados;
- 0B-01 a 0B-04B;
- G6, eliminado como candidato a gap;
- G7, absorbido en F2.

La revisión de 0B-05A no modifica hechos experimentales congelados ni activa a la IA experimental.

### 4. Relación con F1–F5

0B-05 es principalmente fundacional y de gobernanza. No constituye por sí mismo evidencia de ausencia de prior art aduanero.

- **F1/F2:** `NOT_RELEVANT_TO_GAP_CANDIDATE` en 0B-05A; no reciben evidencia de novelty.
- **F3:** `METHOD_FOUNDATION_RELEVANT`; documentar composición, relaciones, curación y particiones no equivale a controlar dependencia ni demostrar independencia.
- **F4:** `METHOD_BOUNDARY_RELEVANT`; provenance, reproducibility, auditability y substantive/legal correctness no son equivalentes.
- **F5:** `METHOD_CONTRAST_RELEVANT`; el lote muestra prior art fuerte en provenance, transparency trails e internal audit, por lo que queda prohibida cualquier formulación amplia de ausencia de trazabilidad/auditabilidad. Solo permanece el candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida, todavía sin novelty.

### 5. Gate de 0B-05A

Gate actual:

`0B-05A INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> aprobación expresa del autor -> integrar C1–C7 en artefacto canónico -> freeze 0B-05A -> definir/abrir 0B-05B`.

No es necesario devolver la entrega a la IA de redacción porque `MATERIAL_ERRORS = 0`.

La IA experimental solo interviene si una interpretación bibliográfica amenaza o modifica un hecho/claim experimental congelado o una restricción bajo su autoridad; esta condición no se ha producido en 0B-05A.

### 6. Prohibiciones

Mientras 0B-05A esté pendiente de aprobación del autor:

- no congelar el bloque;
- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva;
- no usar otros PDF para completar el lote;
- no confundir documentación con calidad o validez;
- no confundir reproducibilidad con replicación externa o generalización;
- no convertir audit trail en corrección jurídica;
- no modificar 0A ni el Plan Maestro;
- no abrir 0B-05B, 0B-05C, 0B-06 o 0C.

---

## English

### 1. Purpose

`0B-05` completes the Phase-0B literature map across three dimensions that must remain distinct: dataset documentation/governance; provenance, traceability, reproducibility, and lifecycle audit; and conceptual information/knowledge plus official normative-source authority.

The block is not a novelty search. Invalid equivalences include `documentation = dataset adequacy`, `versioning = reproducibility`, `provenance = correctness`, `traceability = complete auditability`, `reproducibility = external replication/generalization`, `audit trail = legal correctness`, and `retrieved normative document = correct legal application`.

### 2. Controlled sub-batches

#### 0B-05A — Data documentation, provenance, reproducibility, and audit trail

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

Internal review: `article/reviews/0B05A_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.

The primary-PDF review accepts the governing boundaries:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

and

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

These are methodological boundaries, not a linear maturity or implication ladder.

Mandatory freeze corrections C1–C7: keep Bender & Friedman as documentation rather than causal validation; preserve the analyzed Gebru copy as arXiv v8 and leave final-citation metadata pending rather than silently reconstructing it; keep Gebru/Pineau reproducibility terminology distinct; keep FAIR Data Pipeline centered on provenance/lineage because full reproducibility is explicitly not a core requirement; preserve Pineau's 2×2 terminology and non-causal interpretation; keep SMACTR at five stages and lifecycle audit separate from output-level/external/legal auditability; and prevent the cross-paper taxonomy from being read as automatic implication.

No material error requires a return to the drafting AI.

#### 0B-05B — Information, documented explicit knowledge, and limits of codified knowledge

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may open only after 0B-05A is frozen. Candidate inherited sources remain Zins, Hildreth & Kimble, and Al-Hawamdeh only if complete primary-PDF access is confirmed before opening.

#### 0B-05C — Authority, currency, and traceability of normative/official sources

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It will remain a separate primary-official-source audit after 0B-05B.

### 3. Prior freezes and gap governance

0B-05 does not reopen 0A/0B freezes or experimental results. G6 remains eliminated and G7 remains merged into F2. F1/F2 receive no novelty evidence from 0B-05A. F3 gains documentation foundation only; F4 gains a correctness boundary; F5 is further narrowed by strong prior art on provenance, transparency trails, and internal audit, leaving only the narrow candidate of formal, explicit, separate documentary auditability evaluation at output level, still without novelty status.

### 4. Gate

`0B-05A INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> express author approval -> integrate C1–C7 into the canonical artifact -> freeze 0B-05A -> define/open 0B-05B`.

Experimental-AI review is not required because no frozen experimental fact/claim or authority restriction was affected.

### 5. Prohibitions

Until author approval: no 0B-05A freeze, manuscript drafting, final novelty/gap claim, new-literature search, out-of-batch supplementation, conflation of documentation/provenance/reproducibility/audit trail with correctness/legal validity, Master-Plan/0A modification, or opening of 0B-05B/0B-05C/0B-06/0C.
