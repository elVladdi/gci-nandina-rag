# 0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail / Data documentation, provenance, reproducibility, and audit trail

## Español

### 1. Estado

- Bloque: `0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail`.
- Estado: **`APPROVED / FROZEN`**.
- Entrega inicial: análisis metodológico A–K de cinco PDF primarios por la IA de redacción.
- Revisión científica/editorial interna: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales detectados: `0`.
- Aprobación expresa del autor: recibida el `2026-09-03`.
- Revisión experimental: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Gap definitivo: `NOT_DEFINED`.
- Manuscrito: `NOT_DRAFTED`.

Registros gobernantes:

- `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`;
- `article/reviews/0B05A_INTERNAL_REVIEW.md`;
- `article/reviews/0B05A_AUTHOR_APPROVAL.md`.

Este artefacto congela el mapa metodológico canónico de 0B-05A. Las etiquetas `KEEP_CORE_METHOD` expresan función bibliográfica dentro del mapa y no obligación de cita final.

### 2. Corpus congelado

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

La identidad científica del tercer archivo es **FAIR data pipeline: provenance-driven data management for traceable scientific workflows**. Se conserva el nombre físico de la copia suministrada únicamente para su localización.

Los cinco documentos se trataron como fuentes primarias del sub-lote. Los demás documentos del corpus quedaron fuera de alcance.

### 3. Distinciones metodológicas congeladas

Primera frontera:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

Segunda frontera:

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`

Estas expresiones son **fronteras metodológicas**, no una escala lineal de madurez y no implican que una propiedad garantice automáticamente la siguiente.

### 4. Taxonomía por paper

- Bender & Friedman: `DATASET_DOCUMENTATION / DATA_STATEMENT / CONTEXTUALIZATION / GENERALIZATION_BOUNDARY`.
- Gebru et al.: `DATASET_DOCUMENTATION / DATASHEET_FOR_DATASETS / DATA_LIFECYCLE_DOCUMENTATION / VERSIONING_DOCUMENTATION / SPLIT_DOCUMENTATION`.
- Mitchell et al.: `DATASET_IDENTITY_VERSIONING / DATA_PROVENANCE_LINEAGE / WORKFLOW_PROVENANCE / TRACEABILITY`.
- Pineau et al.: `REPRODUCIBILITY / REPLICATION / ROBUSTNESS / GENERALIZATION_BOUNDARY / REPRODUCIBILITY_REPORTING`.
- Raji et al.: `INTERNAL_ALGORITHMIC_AUDIT / TRANSPARENCY_TRAIL / LIFECYCLE_DOCUMENTATION / DESIGN_HISTORY`.

Ninguno de los cinco papers constituye por sí mismo una evaluación formal de auditabilidad documental por salida comparable a una rúbrica caso-a-caso como HE4.

### 5. Normalizaciones C1–C7 integradas

#### C1 — Bender & Friedman: documentación, no validación causal

Los `data statements` se congelan como una práctica de documentación/contextualización de datasets lingüísticos. Los dos casos analizados por los autores son reconstrucciones `post hoc`; los `value scenarios` ilustran usos plausibles y no constituyen predicciones ni experimentos causales.

Los beneficios propuestos respecto de bias, ingeniería, generalización o reproducibilidad deben formularse como objetivos, argumentos o beneficios esperados de los autores, no como efectos experimentalmente demostrados.

El `Provenance Appendix` documenta datasets fuente reutilizados; no equivale a workflow lineage computacional con run IDs, hashes, commits, entornos y relaciones ejecutables de producción.

#### C2 — Gebru et al.: metadata de la copia analizada

La copia primaria auditada se identifica como `arXiv:1803.09010v8 [cs.DB] — 1 Dec 2021`.

La eventual metadata editorial final queda:

`REVIEW_REQUIRED_FOR_FINAL_CITATION / NO_VERIFICABLE_EN_LA_COPIA_ANALIZADA`.

No se infiere que una publicación editorial posterior no exista y no se reconstruyen venue, DOI, volumen o paginación desde memoria o fuentes externas dentro de este freeze.

#### C3 — Gebru vs Pineau: reproducibility no se armoniza silenciosamente

Gebru et al. utilizan `reproducibility` en un sentido amplio que incluye la posibilidad de facilitar la creación de datasets alternativos con características similares. Pineau et al. adoptan una taxonomía 2×2 específica.

El artículo futuro debe conservar el uso propio de cada fuente y, cuando adopte la terminología de Pineau, identificarla expresamente como convención operacional de ese trabajo.

Documentar relaciones entre instancias, splits, mantenimiento y versiones no equivale a ejecutar group splitting, detectar leakage, demostrar independencia estadística ni implementar identidad inmutable.

#### C4 — FAIR Data Pipeline: provenance/lineage es el núcleo

FAIR Data Pipeline se congela principalmente como fundamento de `PROVENANCE/LINEAGE + VERSION IDENTIFICATION`.

El paper documenta research objects y relaciones que permiten rastrear outputs hacia código/modelos, parámetros y datos fuente. Registra o enlaza versiones específicas de datos y software, actividades y metadatos de procedencia.

Los propios autores establecen que la reproducibilidad es deseable pero **no es un core requirement**. Por tanto:

`PROVENANCE ≠ FULL REPRODUCIBILITY`.

Versiones, commits, identificadores, checksums, inputs y outputs pueden apoyar trazabilidad y reproducción, pero no garantizan que una transformación sea correcta ni que un resultado pueda reproducirse automáticamente bajo cualquier entorno.

#### C5 — Pineau et al.: convención operacional y no causalidad

Se congela la taxonomía adoptada por el paper:

- mismos datos + mismas herramientas analíticas = `Reproducible`;
- datos diferentes + mismas herramientas = `Replicable`;
- mismos datos + herramientas diferentes = `Robust`;
- datos diferentes + herramientas diferentes = `Generalisable`.

Esta terminología se trata como convención de Pineau et al., no como nomenclatura universal.

Los datos del NeurIPS 2019 Reproducibility Program se interpretan descriptivamente. La disponibilidad de código/datos puede facilitar reproducción y revisión, pero no prueba correctness ni reproducción automática. Las asociaciones entre code availability, checklist/reviewer variables y resultados editoriales no se interpretan causalmente.

Los autores no establecen evidencia concluyente de que el programa haya mejorado causalmente la calidad científica de los trabajos publicados.

#### C6 — Raji et al.: lifecycle audit ≠ output-level auditability

SMACTR conserva cinco etapas:

1. `Scoping`;
2. `Mapping`;
3. `Artifact Collection`;
4. `Testing`;
5. `Reflection`.

`Post-Audit` puede aparecer en el flujo ampliado, pero no se convierte en una sexta etapa del acrónimo SMACTR.

El `transparency trail`, el `Algorithmic Design History File (ADHF)` y los artefactos de auditoría permiten reconstruir decisiones, riesgos y eventos del ciclo de desarrollo. Se clasifican como `LIFECYCLE AUDITABILITY / INTERNAL ALGORITHMIC AUDIT`, no como:

- formal per-output auditability;
- data-lineage automatizado;
- auditoría externa independiente;
- legal correctness;
- demostración empírica de reducción causal de harms.

El framework se encuentra ilustrado mediante escenarios organizacionales/hipotéticos y no queda congelado como instrumento cuya eficacia causal haya sido validada por benchmark/control empírico.

#### C7 — Taxonomía cruzada: fronteras, no escalera

El mapa general no debe dibujarse ni redactarse como una secuencia causal o de madurez del tipo:

`documentación -> versionamiento -> provenance -> reproducibilidad -> auditabilidad -> correctness`.

Cada propiedad responde a una pregunta distinta y requiere evidencia propia.

### 6. Hallazgos gobernantes por dimensión

#### 6.1 Dataset documentation

Bender & Friedman y Gebru et al. fundamentan la necesidad de documentar contexto, curación, composición, relaciones entre instancias, anotación, usos, mantenimiento, actualizaciones, splits y limitaciones. Esa documentación mejora la inspectabilidad/contextualización del dataset, pero no certifica representatividad, ausencia de sesgo, calidad universal ni adecuación para cualquier tarea.

#### 6.2 Dataset identity/versioning

Describir una versión no equivale a establecer identidad técnica inmutable. Los mecanismos técnicos de versión/identificación y la relación entre objetos de una ejecución deben tratarse separadamente de la documentación narrativa del dataset.

#### 6.3 Provenance/lineage

Provenance responde a relaciones de producción y dependencia: qué objetos, versiones, procesos/agentes o transformaciones participaron en la producción de un resultado. Esta trazabilidad no demuestra que inputs, transformaciones o outputs sean sustantivamente correctos.

#### 6.4 Reproducibility/replication/generalization

Reproducir un resultado bajo las mismas condiciones no equivale a replicarlo bajo condiciones/datos distintos ni demuestra generalización. La disponibilidad de artefactos es un facilitador, no una garantía automática.

#### 6.5 Audit trail y auditability

Un transparency trail o un internal lifecycle audit puede hacer inspeccionables decisiones, documentación, riesgos y eventos del proceso. Esto no equivale a evaluar formalmente, mediante criterios explícitos y separados, la auditabilidad documental de cada output individual.

### 7. Relación congelada con F1–F5

0B-05A es fundacional/de gobernanza y no constituye un pressure test de novelty aduanera.

- **F1:** sin evidencia de novelty en este lote.
- **F2:** sin evidencia de novelty en este lote.
- **F3:** `METHOD_FOUNDATION_RELEVANT` únicamente para documentación de relaciones, unidades, curación y particiones. Regla congelada: `documentar dependencia ≠ controlarla ≠ demostrar independencia`.
- **F4:** `METHOD_BOUNDARY_RELEVANT`; se refuerza `provenance/reproducibility/auditability ≠ substantive/legal correctness`.
- **F5:** `METHOD_CONTRAST_RELEVANT`; existe prior art fuerte en provenance, transparency trails e internal algorithmic auditing. Queda prohibida cualquier formulación amplia de ausencia de trazabilidad/auditabilidad. Solo permanece como candidato estrecho, todavía sin novelty, la **evaluación formal, explícita y separada de auditabilidad documental por salida**.

G6 permanece eliminado como candidato a gap. G7 permanece absorbido en F2.

### 8. Claims metodológicos autorizables

Quedan autorizables, con sus límites:

- Los data statements y datasheets proporcionan mecanismos estructurados para contextualizar/documentar datasets, pero no certifican calidad, representatividad o generalización.
- Los datasheets incluyen documentación de relaciones entre instancias, splits y mantenimiento/versiones, pero no implementan por sí mismos control de dependencia o leakage.
- Un workflow de provenance puede enlazar outputs con inputs, software/configuración y versiones concretas; ese lineage no demuestra correctness.
- Provenance detallada puede apoyar la reproducibilidad, pero no es equivalente a reproducibilidad completa.
- Bajo Pineau et al., reproducibility, replication, robustness y generalization son categorías distintas según datos y herramientas analíticas; esta es una convención del paper.
- Code/data availability puede facilitar reproducción, pero no garantiza correctness ni éxito reproductivo automático.
- Internal algorithmic auditing puede preservar un transparency trail del lifecycle, pero no equivale a formal per-output auditability ni legal correctness.

### 9. Claims prohibidos o excesivos

Queda prohibido afirmar, basándose en este lote, que:

- documentar un dataset demuestra alta calidad o representatividad;
- data statements eliminan bias o demuestran generalización;
- datasheets garantizan reproducibilidad o independencia de splits;
- describir una versión equivale a identidad técnica inmutable;
- FAIR/provenance implica automáticamente reproducibilidad;
- lineage demuestra correctness;
- disponer de código/datos garantiza reproducción;
- reproducibility, replication y generalization son intercambiables;
- el programa NeurIPS 2019 demostró causalmente mayor calidad científica;
- SMACTR fue validado empíricamente como sistema que reduce harms;
- internal audit equivale a auditoría externa o legal compliance;
- transparency trail equivale a output-level auditability;
- F3, F4 o F5 quedan establecidos como gaps definitivos por estos cinco papers.

### 10. Función bibliográfica

Los cinco trabajos quedan `KEEP_CORE_METHOD` dentro del mapa metodológico 0B-05A:

- Bender & Friedman: documentación contextual de datos y límites de generalización;
- Gebru et al.: documentación del ciclo de vida, splits, relaciones, mantenimiento y versiones;
- Mitchell et al.: provenance/lineage, version identity y traceability;
- Pineau et al.: reproducibility/replication/generalization boundaries y reporting;
- Raji et al.: internal lifecycle audit, transparency trail y design-history artifacts.

Esto no obliga a citar los cinco trabajos en el manuscrito final.

### 11. Estado de cierre

```text
0B-05A = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El cierre de 0B-05A no abre automáticamente 0B-05B, 0B-05C, 0B-06 o 0C y no autoriza redacción del manuscrito.

---

## English

### 1. Status

- Block: `0B-05A — Data documentation, provenance, reproducibility, and audit trail`.
- Status: **`APPROVED / FROZEN`**.
- Initial deliverable: A–K methodological analysis of five assigned primary PDFs by the drafting AI.
- Internal scientific/editorial review: **`PASS WITH MINOR CORRECTIONS`**.
- Material errors: `0`.
- Express author approval: received on `2026-09-03`.
- Experimental review: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Final gap: `NOT_DEFINED`.
- Manuscript: `NOT_DRAFTED`.

Governing records are the 0B-05A prompt, internal review, and author-approval record. This artifact freezes the canonical 0B-05A methodological map.

### 2. Frozen corpus

The five primary works are Bender & Friedman on data statements; Gebru et al. on datasheets; the supplied FAIR Data Pipeline paper; Pineau et al. on the NeurIPS 2019 Reproducibility Program; and Raji et al. on internal algorithmic auditing. Other corpus documents remained out of scope.

### 3. Frozen methodological boundaries

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`

These are methodological boundaries, not a linear maturity ladder or an implication chain.

### 4. Frozen taxonomy by paper

- Bender & Friedman: dataset documentation, data statements, contextualization, and generalization boundaries.
- Gebru et al.: dataset documentation, datasheets, data-lifecycle documentation, versioning documentation, and split documentation.
- Mitchell et al.: dataset identity/versioning, data/workflow provenance, and traceability.
- Pineau et al.: reproducibility, replication, robustness, generalization boundaries, and reproducibility reporting.
- Raji et al.: internal algorithmic audit, transparency trail, lifecycle documentation, and design history.

None of the five papers is frozen as a formal case-by-case documentary output-auditability evaluation equivalent to HE4.

### 5. Integrated C1–C7 normalizations

**C1 — Bender & Friedman.** Data statements are documentation/contextualization. Their two cases are post-hoc reconstructions and value scenarios are illustrative rather than predictive or causal validation. Proposed benefits regarding bias, engineering, generalization, or reproducibility remain author arguments/expected benefits, not experimentally demonstrated effects. The provenance appendix documents source datasets rather than executable workflow lineage.

**C2 — Gebru metadata.** The analyzed primary copy is `arXiv:1803.09010v8 [cs.DB] — 1 Dec 2021`. Final editorial metadata remains `REVIEW_REQUIRED_FOR_FINAL_CITATION / NOT_VERIFIABLE_IN_THE_ANALYZED_COPY`; no later-publication nonexistence is inferred and no metadata is silently reconstructed.

**C3 — Gebru vs Pineau terminology.** Their uses of reproducibility remain source-specific. Gebru's broader use is not silently harmonized with Pineau's 2×2 taxonomy. Documenting relationships, splits, maintenance, and versions does not itself perform group splitting, leakage detection, independence testing, or immutable technical identity.

**C4 — FAIR Data Pipeline.** Its governing role is provenance/lineage and version identification. The paper supports tracing outputs to code/models, parameters, and source data. Full reproducibility is desirable but explicitly not a core requirement; therefore provenance is not full reproducibility, and technical identifiers/versioning do not guarantee correctness or automatic reproduction.

**C5 — Pineau et al.** The frozen 2×2 convention is: same data/same analytical tools = reproducible; different data/same tools = replicable; same data/different tools = robust; different data/different tools = generalisable. This is a paper-specific convention. Program observations remain descriptive/non-causal; code/data availability does not establish correctness or automatic reproducibility, and the program did not establish causal improvement in scientific quality.

**C6 — Raji et al.** SMACTR has five stages: Scoping, Mapping, Artifact Collection, Testing, and Reflection. Post-Audit is not a sixth SMACTR stage. Transparency trails and ADHF support lifecycle auditability and documentary reconstruction, not formal per-output auditability, automated data lineage, independent external audit, legal correctness, or empirically proven harm reduction.

**C7 — Cross-paper taxonomy.** Documentation, identity/versioning, provenance, reproducibility, audit trails, and correctness remain distinct properties and must not be represented as an automatic maturity or implication chain.

### 6. Governing findings by dimension

Data statements and datasheets support structured dataset documentation and contextual interpretation but do not certify dataset quality, representativeness, bias absence, or universal suitability. Dataset version descriptions are distinct from technical immutable identity. Provenance records production/dependency relationships and does not establish substantive correctness. Reproducibility is distinct from replication and generalization. Lifecycle transparency/internal audit is distinct from formal per-output auditability.

### 7. Frozen relation to F1–F5

0B-05A is methodological/governance-oriented rather than a customs-novelty pressure test.

- F1/F2 receive no novelty evidence.
- F3 receives documentation/dependency-reporting foundation only: documenting dependence is not controlling it and not proving independence.
- F4 is reinforced as a methodological boundary separating provenance/reproducibility/auditability from substantive or legal correctness.
- F5 is further narrowed because provenance, transparency trails, and internal algorithmic auditing have strong prior art. Broad claims of missing traceability/auditability are prohibited. Only the narrow candidate of a formal, explicit, separate documentary auditability evaluation at output level remains, without novelty status.

G6 remains eliminated and G7 remains merged into F2.

### 8. Authorized methodological claims

The frozen batch may support claims that structured data statements/datasheets contextualize datasets without certifying quality; split/relationship documentation does not itself control dependence; workflow provenance can connect outputs to inputs/software/configuration/versions without proving correctness; provenance can support but is not equivalent to complete reproducibility; Pineau's reproducibility/replication/robustness/generalization categories are distinct under that paper's convention; code/data availability facilitates but does not guarantee reproduction; and internal algorithmic auditing can preserve lifecycle transparency without constituting per-output or legal correctness assessment.

### 9. Prohibited overclaims

The batch does not authorize claims that dataset documentation proves quality/representativeness/generalization, that datasheets guarantee reproducibility or split independence, that FAIR/provenance automatically implies reproducibility, that lineage proves correctness, that code/data availability guarantees reproduction, that Pineau's terminology is universal, that NeurIPS 2019 interventions causally improved scientific quality, that SMACTR is empirically validated to reduce harms, that internal audit is equivalent to external/legal audit, or that F3–F5 are definitive gaps.

### 10. Bibliographic role

All five works remain `KEEP_CORE_METHOD` within 0B-05A. This role does not require all five to appear in the final manuscript.

### 11. Closure state

```text
0B-05A = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Closing 0B-05A does not automatically open 0B-05B, 0B-05C, 0B-06, or 0C and does not authorize manuscript drafting.
