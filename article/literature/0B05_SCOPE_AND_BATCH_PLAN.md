# 0B-05 — Datos, procedencia, reproducibilidad, conocimiento y fuentes normativas / Data, provenance, reproducibility, knowledge, and normative sources

## Español

### 1. Propósito

`0B-05` completa el mapa bibliográfico de Fase 0B en tres dimensiones que no deben confundirse:

1. documentación/gobernanza de datos;
2. procedencia, trazabilidad, reproducibilidad y auditoría del ciclo de vida;
3. fundamentos de información/conocimiento y autoridad documental de fuentes normativas oficiales.

El bloque no declara novelty. Su función es fijar fronteras científicas para describir banco histórico, corpus normativo, versionamiento, provenance, reproducibilidad, conocimiento explícito documental y autoridad normativa sin convertir documentación en correctness ni retrieval en juicio jurídico.

### 2. Sub-lotes

#### 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail

Estado: **`APPROVED / FROZEN`**.

Artefacto canónico:

`article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

Fronteras congeladas:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

F3 recibe fundamento documental, no prueba de independencia; F4 conserva la frontera correctness; F5 queda restringido al candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida. G6 sigue eliminado y G7 absorbido en F2.

#### 0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado

Estado: **`APPROVED / FROZEN`**.

Registros:

- Prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.
- Revisión interna: `article/reviews/0B05B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación: `article/reviews/0B05B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Lote congelado:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

Fronteras congeladas:

- `data`, `information` y `knowledge` no son sinónimos universales ni etapas lineales necesarias; sus definiciones/relaciones dependen del marco conceptual.
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`.
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`.
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

`DOCUMENTED_EXPLICIT_KNOWLEDGE` queda autorizado solo como `OPERACIONALIZACION_DEL_PROYECTO`. El corpus normativo puede describirse bajo esa operacionalización como fuente documental formalizada/versionada/recuperable sin inferir totalidad del expertise jurídico ni corrección automática de aplicación. El banco histórico conserva precedentes/experiencia registrada, no la totalidad del knowing experto. La revisión experta permanece fuera del sistema automatizado.

Normalizaciones C1–C8 integradas:

- D-I-K no se congela como disyunción ontológica rígida;
- Zins: 44 panel contributors + Zins = 45 scholars, ≈130 definiciones; atribuciones separadas;
- Hildreth & Kimble: duality, no dicotomía rígida;
- fuentes anidadas continúan secundarias si se usan independientemente;
- Al-Hawamdeh: explicit/externalized knowledge → information es posición del autor, no consenso universal;
- implicit/know-how permanece distinto de tacit estricto;
- documented explicit knowledge es operacionalización del proyecto;
- autoridad, vigencia, jerarquía y suficiencia jurídica de fuentes oficiales quedan para 0B-05C.

Impacto metodológico:

- F1/F2/F4/F5: solo `METHOD_BOUNDARY_RELEVANT`; no cambia su estado provisional.
- F3: `NOT_RELEVANT_TO_GAP_CANDIDATE` en este lote.
- G6/G7 permanecen cerrados.
- No novelty ni gap definitivo.

#### 0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales

Estado: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

0B-05C será una auditoría de **fuentes oficiales primarias**, separada de la literatura académica. Antes de abrirlo debe definirse el conjunto exacto de fuentes y el prompt ejecutable.

Objetivo previsto:

- verificar autoridad emisora;
- identificar documento/instrumento exacto;
- registrar versión/edición y fecha;
- verificar vigencia aplicable al alcance del estudio;
- distinguir jerarquía y función documental;
- registrar identificador/enlace estable cuando exista;
- separar `autoridad documental` de `corrección jurídica de una clasificación`;
- separar `fuente oficial` de `evidencia suficiente para un caso`;
- evitar que WCO/OMA, Comunidad Andina, SUNAT u otras fuentes oficiales sean tratadas como artículos científicos.

Fuentes candidatas a auditar deberán derivarse del corpus/documentación gobernante del proyecto y confirmarse antes de crear el prompt. El freeze de 0B-05B **no abre automáticamente 0B-05C**.

### 3. Relación con freezes previos

0B-05 no reabre 0A, resultados experimentales congelados, 0B-01–0B-04B, 0B-05A ni 0B-05B. La IA experimental no es revisora bibliográfica rutinaria y conserva autoridad exclusiva sobre el Plan Maestro.

### 4. Gate

Completados:

`0B-05A -> APPROVED / FROZEN`

`0B-05B -> APPROVED / FROZEN`

Siguiente gate permitido:

`definir fuentes y alcance 0B-05C -> crear prompt ejecutable -> READY_FOR_DRAFTING -> ejecución/auditoría de fuentes oficiales -> revisión interna -> aprobación del autor -> freeze`.

Hasta esa apertura:

- 0B-05C no está activo;
- 0B-06 no inicia;
- 0C sigue bloqueado;
- no se redacta el manuscrito ni se declara novelty/gap definitivo.

---

## English

### 1. Purpose

`0B-05` completes Phase 0B across three distinct dimensions: data documentation/governance; provenance, traceability, reproducibility, and lifecycle audit; and information/knowledge foundations plus authority of official normative sources.

The block does not establish novelty. It sets scientific boundaries for describing historical data, normative corpora, versioning, provenance, reproducibility, documented explicit knowledge, and normative authority without turning documentation into correctness or retrieval into legal judgment.

### 2. Sub-batches

#### 0B-05A

Status: **`APPROVED / FROZEN`**.

Canonical artifact: `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

Frozen boundaries distinguish dataset documentation, identity/versioning, data/workflow provenance, reproducibility, replication, generalization, transparency trails, lifecycle audit, output-level auditability, and substantive/legal correctness.

#### 0B-05B

Status: **`APPROVED / FROZEN`**.

Governing records:

- `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`;
- `article/reviews/0B05B_INTERNAL_REVIEW.md`;
- `article/reviews/0B05B_AUTHOR_APPROVAL.md`;
- `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.

Frozen corpus: Zins; Hildreth & Kimble; Al-Hawamdeh.

Frozen boundaries:

- data, information, and knowledge are not universal synonyms or necessary linear stages; definitions and relationships are framework-dependent;
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`;
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`;
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

`DOCUMENTED_EXPLICIT_KNOWLEDGE` is authorized only as `PROJECT_OPERATIONALIZATION`. C1–C8 are integrated, including non-rigid D-I-K interpretation, normalized Zins attribution/counting, Hildreth & Kimble duality, nested-source controls, Al-Hawamdeh-specific consensus limits, preservation of implicit/know-how vs strict tacit knowledge, and reservation of official-source authority/currency/hierarchy for 0B-05C.

F1/F2/F4/F5 receive methodological boundary relevance only; F3 is not relevant to the gap candidate in this batch. No provisional candidate state changes and no final novelty/gap is declared.

#### 0B-05C

Status: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

0B-05C will be a separate audit of **official primary sources**, not academic literature. Before opening, the exact source set and executable prompt must be defined.

Planned checks include issuing authority, exact instrument/document identity, version/edition and date, applicable currency, documentary hierarchy/function, stable identifiers/links, separation of documentary authority from legal correctness, and separation of official-source status from evidentiary sufficiency for a particular case.

Candidate sources must be derived from governing project documentation and confirmed before prompt creation. The 0B-05B freeze does **not** automatically open 0B-05C.

### 3. Prior freezes and governance

0B-05 does not reopen 0A, frozen experiments, 0B-01–0B-04B, 0B-05A, or 0B-05B. Experimental-AI review is not routine and the experimental AI retains exclusive authority over the Master Plan.

### 4. Gate

Completed:

`0B-05A -> APPROVED / FROZEN`

`0B-05B -> APPROVED / FROZEN`

Next allowed gate:

`define 0B-05C source set and scope -> create executable prompt -> READY_FOR_DRAFTING -> official-source audit -> internal review -> author approval -> freeze`.

Until then, 0B-05C is not active, 0B-06 is not started, 0C remains blocked, and manuscript drafting/final novelty-gap claims remain prohibited.
