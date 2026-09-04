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

Estado: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Registros actuales:

- Prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.
- Revisión interna: `article/reviews/0B05B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Revisión experimental: `NOT_REQUIRED`.
- Aprobación del autor: `PENDING`.

Lote final controlado:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

Para el tercer trabajo puede existir un sufijo físico automático de adjunto, como `(2)`. Ese sufijo no constituye una versión científica; la identidad gobernante es el título del trabajo visible en la copia primaria.

La revisión interna confirmó que el lote no permite imponer una ontología DIKW universal. La notación `DATA ≠ INFORMATION ≠ KNOWLEDGE` solo puede sobrevivir como abreviatura de **no equivalencia automática/no sinonimia universal**, no como afirmación de conjuntos ontológicamente disjuntos, porque Zins admite concepciones en las que `information` es un tipo de `knowledge`.

Normalizaciones obligatorias para el freeze:

- Zins: `44 panel contributors + researcher = 45 scholars`, aproximadamente 130 definiciones; distinguir posiciones de participantes, síntesis de Zins y posición propia de Zins.
- Hildreth & Kimble: `duality`, no dicotomía rígida; hard/soft coexisten en proporciones variables y la frontera es contextual.
- Al-Hawamdeh: externalized/explicit knowledge como `information` es posición del autor, no consenso universal; conservar `implicit/know-how` distinto de `tacit` estricto.
- `DOCUMENTED_EXPLICIT_KNOWLEDGE`: solo `OPERACIONALIZACION_DEL_PROYECTO`, no ontología compartida por P01–P03.
- Claims anidados de Polanyi, Nonaka, Wenger, Lave, Cook & Brown y otros: `SECONDARY_CLAIM_UNVERIFIED` si se usan como proposiciones independientes.
- El carácter `autoritativo` de fuentes normativas pertenece a la documentación/gobernanza del proyecto; P01–P03 no verifican autoridad, vigencia, jerarquía o suficiencia jurídica de WCO/OMA, Comunidad Andina o SUNAT. Esa auditoría primaria corresponde a 0B-05C.

Fronteras aceptadas para el eventual freeze, sujetas a esas normalizaciones:

`DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`

`LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

Estas expresiones son fronteras metodológicas, no una ontología universal ni una cadena de implicación.

0B-05B sigue siendo **fundacional y conceptual**. No es un pressure test de novelty aduanera. Cualquier mapeo desde conceptos generales hacia componentes NANDINA debe etiquetarse `OPERACIONALIZACION_DEL_PROYECTO` y no atribuirse directamente a los autores.

Relación metodológica resultante con F1–F5:

- **F1:** `METHOD_BOUNDARY_RELEVANT`; no novelty.
- **F2:** `METHOD_BOUNDARY_RELEVANT`; no novelty.
- **F3:** `NOT_RELEVANT_TO_GAP_CANDIDATE`.
- **F4:** `METHOD_BOUNDARY_RELEVANT`.
- **F5:** `METHOD_BOUNDARY_RELEVANT` como máximo.
- Los estados provisionales F1–F5 no cambian.
- G6 permanece eliminado y G7 permanece absorbido en F2.

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

La IA experimental no es revisora bibliográfica rutinaria. Solo se activará si una interpretación de 0B-05B modifica o amenaza hechos/claims experimentales congelados o restricciones bajo su autoridad.

### 4. Gate

0B-05A completó:

`IA de redacción -> revisión interna -> aprobación expresa del autor -> freeze`.

Gate activo:

`0B-05B INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> aprobación expresa del autor -> incorporar C1–C8 al artefacto canónico -> freeze -> evaluar definición/apertura de 0B-05C`.

0B-05C permanece cerrado hasta completar ese gate.

### 5. Prohibiciones vigentes

Mientras 0B-05B no esté congelado:

- no redactar secciones del manuscrito;
- no declarar novelty ni gap definitivo;
- no buscar literatura nueva;
- no usar otros PDF para completar el lote;
- no imponer una pirámide DIKW universal;
- no confundir `explicit`, `codified`, `documented` y `stored` sin soporte de fuente;
- no confundir conocimiento explícito documental con totalidad del conocimiento experto;
- no convertir recuperación documental en comprensión, interpretación o aplicación jurídica correcta;
- no describir la explicación del LLM como conocimiento experto o clasificación oficial;
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

Status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.

Current records:

- Prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.
- Internal review: `article/reviews/0B05B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Experimental review: `NOT_REQUIRED`.
- Author approval: `PENDING`.

Final controlled batch:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

The internal review confirms that the batch does not support a universal DIKW ontology. `DATA ≠ INFORMATION ≠ KNOWLEDGE` may survive only as shorthand for non-automatic equivalence/non-universal synonymy, not ontological disjunction, because Zins explicitly allows conceptions in which information is a type of knowledge.

Mandatory freeze normalizations include: Zins's 44 panel contributors plus researcher = 45 scholars and approximately 130 definitions; separation of participant positions, Zins's synthesis, and Zins's own position; Hildreth & Kimble's `duality` rather than rigid dichotomy; Al-Hawamdeh's externalized/explicit-knowledge-to-information mapping as his conceptual position rather than universal consensus; preservation of implicit/know-how as distinct from strict tacit knowledge; `DOCUMENTED_EXPLICIT_KNOWLEDGE` as `PROJECT_OPERATIONALIZATION` only; and secondary-source status for nested claims when used independently.

The project's existing `authoritative` treatment of normative documents belongs to project governance/documentation; P01–P03 do not verify issuing authority, currency, hierarchy, or legal sufficiency of WCO/OMA, Andean Community, or SUNAT sources. That primary-source audit belongs to 0B-05C.

Accepted methodological boundaries for the eventual freeze are:

`DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`

`LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

These are methodological boundaries, not a universal ontology or implication chain.

F1/F2/F4/F5 receive `METHOD_BOUNDARY_RELEVANT` only; F3 is `NOT_RELEVANT_TO_GAP_CANDIDATE`. No provisional gap-candidate state changes. G6 remains eliminated and G7 remains merged into F2.

#### 0B-05C — Authority, currency, and traceability of normative/official sources

Status: **`NOT_STARTED / CLOSED_BY_GATE`**. It may be defined only after 0B-05B freezes. It will be a separate audit of official primary sources covering issuing authority, version, currency, date, scope, documentary hierarchy, stable identifiers, and evidentiary role.

### 3. Prior freezes and experimental governance

0B-05 does not reopen 0A, frozen experiments, 0B-01 through 0B-04B, or frozen 0B-05A. G6/G7 remain closed as previously decided. Experimental-AI review is not routine and is triggered only if a 0B-05B interpretation changes or threatens frozen experimental facts/claims or restrictions under its authority.

### 4. Gate

0B-05A completed its drafting-AI -> internal-review -> author-approval -> freeze cycle.

Active gate:

`0B-05B INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> express author approval -> incorporate C1–C8 into the canonical artifact -> freeze -> assess definition/opening of 0B-05C`.

### 5. Prohibitions

Until 0B-05B is frozen: no manuscript drafting; no final novelty/gap claims; no new-literature search; no out-of-batch supplementation; no universal DIKW pyramid; no unsupported conflation of explicit/codified/documented/stored knowledge; no equation of documented knowledge with complete expertise; no conversion of document retrieval into understanding/legal correctness; no description of LLM explanation as expert knowledge or official classification; no Master-Plan/0A modification; no reopening G6/G7; and no opening of 0B-05C/0B-06/0C before their gates.
