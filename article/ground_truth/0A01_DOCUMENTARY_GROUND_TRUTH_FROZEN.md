# 0A-01 — Ground truth documental congelado / Frozen documentary ground truth

## Español

### 1. Estado del bloque

- Bloque: `0A-01 — Ground truth documental`.
- Estado: `APPROVED / FROZEN`.
- Fecha de aprobación del autor: 2026-09-02.
- Revisión científica/editorial interna: `PASS WITH MINOR TERMINOLOGY CORRECTION`, correcciones resueltas.
- Revisión experimental independiente final: `PASS — READY FOR AUTHOR APPROVAL`.
- Aprobación expresa del autor: recibida el 2026-09-02.
- Efecto: este artefacto constituye la referencia documental congelada de 0A-01 para las fases posteriores del artículo.

El congelamiento de 0A-01 no congela el estado experimental completo de la investigación. `SRC-03` continúa siendo una fuente viva y los experimentos pendientes conservan sus estados actuales. Cualquier actualización experimental posterior debe incorporarse mediante los gates correspondientes sin reescribir silenciosamente este registro histórico.

### 2. Fuentes gobernantes del corte

| ID | Fuente | Función en 0A-01 | Estado en el corte |
|---|---|---|---|
| SRC-01 | `Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf` | formulaciones aprobadas: problema, objetivos, hipótesis, justificación y alcance | fuente aprobada |
| SRC-02 | `Anexo_1_NANDINA_LLM_RAG_v13.docx` | arquitectura y metodología operativa vigente | fuente operativa vigente |
| SRC-03 | Plan Maestro experimental en `elVladdi/gci-nandina-rag`, rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | estado experimental actual | fuente viva; snapshot leído en 0A-01: `0a9a82181c6c3840f74f0272e5c225568474058b` |
| SRC-04 | tesis preliminar vigente identificada por el autor como `Molleapasa_gv.docx` | formulaciones posteriores y detección de snapshots obsoletos | fuente secundaria de comparación |

Los sufijos automáticos generados al adjuntar archivos, por ejemplo `(3)`, `(4)` o `(5)`, no constituyen por sí solos versiones científicas distintas.

### 3. Precedencia documental congelada

1. **Estado experimental actual:** `SRC-03` más artefactos y commits experimentales congelados del repositorio de desarrollo.
2. **Arquitectura y metodología operativa:** `SRC-02`.
3. **Problema, objetivos, hipótesis, justificación y alcance aprobados:** `SRC-01`.
4. **Formulaciones posteriores y borrador de tesis:** `SRC-04`.

Una discrepancia entre estas fuentes debe hacerse explícita. Ninguna IA del flujo editorial puede armonizarla silenciosamente.

### 4. Formulaciones aprobadas exactas en español

#### Título aprobado

**Evaluación de un piloto experimental offline de gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y explicación controlada con LLM local**

#### Problema general

**PG.** ¿En qué medida un piloto experimental offline de gestión de información documental, aplicado a la descripción de mercancías y compuesto por recuperación histórica para el ranking, recuperación normativa para la evidencia y un LLM local para la explicación restringida de un Top-3 fijo, permitirá recomendar subpartidas NANDINA con desempeño medible, trazabilidad documental y auditabilidad?

#### Problemas específicos

**PE1.** ¿Cómo se estructurarán y versionarán el banco histórico etiquetado y el corpus normativo NANDINA para asegurar su curación, integridad jerárquica, trazabilidad y uso reproducible en el piloto?

**PE2.** ¿Qué desempeño alcanzarán las estrategias de recuperación normativa y la recuperación histórica en la generación y el ordenamiento de candidatos NANDINA, según métricas Top-k, MRR y cobertura del conjunto candidato?

**PE3.** ¿En qué medida la integración del ranking histórico con evidencia normativa permitirá conservar el desempeño de recomendación y aumentar la trazabilidad documental, y qué efecto tendrá el uso diagnóstico de un LLM local como reordenador (reranker) sobre el orden de los candidatos?

**PE4.** ¿En qué medida un LLM local, restringido a explicar un Top-3 fijo sin incorporar códigos externos ni alterar el ranking, generará salidas estructuradas, verificables y respaldadas por evidencia histórica y normativa?

**PE5.** ¿Qué patrones de error y qué límites de validez se identificarán en el piloto respecto de la calidad de las descripciones, la proximidad jerárquica de las subpartidas, la disponibilidad de precedentes históricos y el alcance interno de la evaluación?

#### Objetivo general

**OG.** Evaluar, mediante un piloto experimental offline, la contribución diferenciada de la recuperación histórica al ranking de candidatos, de la recuperación normativa a la evidencia documental y de un LLM local a la explicación restringida y auditable de un Top-3 fijo para la recomendación de subpartidas NANDINA.

#### Objetivos específicos

**OE1.** Construir y versionar un banco histórico etiquetado y un corpus normativo NANDINA, aplicando criterios de curación, integridad jerárquica, trazabilidad y reproducibilidad.

**OE2.** Implementar y comparar estrategias de recuperación normativa y recuperación histórica para generar y ordenar candidatos NANDINA, evaluando su desempeño mediante métricas Top-k, MRR y cobertura del conjunto candidato.

**OE3.** Evaluar la integración del ranking histórico con evidencia normativa y analizar, de forma diagnóstica, el efecto de un LLM local como reordenador (reranker) sobre el orden de los candidatos.

**OE4.** Diseñar e implementar un LLM local restringido a explicar un Top-3 fijo, sin incorporar códigos externos ni alterar el ranking, y evaluar la validez estructural, la trazabilidad y la concordancia de sus explicaciones con la evidencia recuperada.

**OE5.** Analizar cuantitativa y cualitativamente los errores y límites del piloto, considerando la calidad de las descripciones, la proximidad jerárquica, la disponibilidad de precedentes históricos y el alcance interno de la evaluación.

#### Hipótesis general

**HG.** En un piloto experimental offline aplicado, la diferenciación funcional de los componentes permitirá obtener una recomendación auditable de subpartidas NANDINA: la recuperación histórica alcanzará el mejor desempeño de ranking, la recuperación normativa aportará evidencia documental trazable y el LLM local generará explicaciones controladas sobre un Top-3 fijo sin necesidad de modificar el orden de los candidatos.

#### Hipótesis específicas

**HE1.** La estructuración y el versionamiento del banco histórico etiquetado y del corpus normativo NANDINA permitirán preservar la integridad jerárquica, la procedencia de la evidencia y la reproducibilidad de las corridas experimentales.

**HE2.** La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.

**HE3.** La integración del ranking histórico con evidencia normativa conservará el desempeño del ranking histórico y aumentará la trazabilidad documental; el uso diagnóstico del LLM local como reordenador no producirá una mejora consistente del orden de los candidatos.

**HE4.** El LLM local restringido a un Top-3 fijo generará salidas estructuradas que conservarán los tres candidatos y su orden, no incorporarán códigos externos y vincularán las explicaciones con evidencia histórica o normativa identificable. La calidad de esta vinculación se evaluará mediante criterios de verificabilidad, trazabilidad y concordancia entre evidencia y justificación.

**HE5.** Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.

### 5. Arquitectura y funciones vigentes

La arquitectura que gobierna la redacción posterior es:

`Descripción comercial → normalización → recuperación histórica → ranking histórico Top-k → Top-3 fijo → recuperación de evidencia normativa para esos candidatos → construcción de contexto → LLM local → explicación auditable del Top-3`.

Separación funcional obligatoria:

- **Recuperación histórica:** genera y ordena los candidatos principales.
- **Recuperación normativa:** aporta evidencia documental identificable para los candidatos y no sustituye ni reordena el ranking histórico.
- **LLM local:** explica el Top-3 previamente recuperado bajo contexto controlado; no clasifica desde cero, no incorpora códigos externos y no altera el ranking oficial.
- **Reranking con LLM:** evaluación diagnóstica y secundaria; no pertenece al flujo principal oficial.

### 6. Unidad de análisis y delimitación

- **SERIE** es la unidad experimental y de análisis.
- **DAM** es la unidad administrativa original y la unidad de agrupamiento utilizada cuando existe dependencia.
- La descripción normalizada de la serie es la unidad de consulta.
- El Top-3 explicado es la unidad de salida.
- Los documentos y fragmentos normativos son unidades recuperables de evidencia, no unidades principales de análisis.
- El piloto es offline, local, no productivo y no vinculante.
- La evaluación empírica se restringe a Clase/Capítulo 87 y al marco administrativo, temporal, documental y experimental definido.
- La revisión experta permanece fuera del sistema.
- No se autorizan inferencias de reducción de tiempos, reducción de errores operativos, eficiencia institucional, desempeño empresarial ni validez jurídica de la recomendación.

### 7. Discrepancias resueltas y reglas vigentes

1. **Snapshot preliminar obsoleto.** Las cifras `3,000/100/1,006` y los resultados asociados de la tesis preliminar corresponden a un estado experimental anterior y no gobiernan el artículo. El estado experimental vigente se obtiene de `SRC-03` y de los artefactos congelados.
2. **Independencia y DAM.** La ausencia de identificadores repetidos no demuestra independencia entre particiones. El rediseño v0.2 agrupa por DAM para eliminar el solapamiento de una misma DAM entre histórico, desarrollo y evaluación. Esto no implica independencia interna entre todas las series de una misma partición; la inferencia debe respetar la agrupación cuando corresponda.
3. **Hallazgo histórico v0.1.** `995/1006` casos del evalset v0.1 pertenecían a DAM también presentes en histórico. Su estado en `CLAIM_EVIDENCE_MATRIX.md` es `C19 = AUTHORIZED` y solo puede utilizarse como hallazgo histórico del rediseño de particiones.
4. **Cifra 48/59.** Permanece como `C20 = REVIEW_REQUIRED`; no debe utilizarse como cifra congelada en el manuscrito hasta completar su trazabilidad mediante artefacto versionado o recomputación auditable.
5. **EXP-08 y HE5.** El artefacto `outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_integrated_findings_v0.2.md` registra `HE5 = PARTIALLY_SUPPORTED` como interpretación histórica/intermedia específica de EXP-08. No constituye la decisión inferencial final de HE5. El estado final sigue `PENDING_GROUP3`.
6. **Plan Maestro.** Es un único documento lógico con dos copias operativas. La copia local y la copia GitHub deben contener el mismo contenido textual canónico; la equivalencia semántica no basta. Solo la IA experimental tiene autoridad de escritura. La IA editora y la IA de redacción tienen acceso de solo lectura. D-011 supersede a D-009 en sincronización, coexistencia y divergencia.
7. **SHA de SRC-03.** Identifica el snapshot concreto leído en un corte, no una identidad inmutable del Plan Maestro vivo.

### 8. Lo que 0A-01 no autoriza

El cierre de este bloque no autoriza:

- redactar todavía secciones del manuscrito;
- declarar novelty o contribución publicable definitiva;
- formular Research Questions definitivas;
- seleccionar la revista objetivo;
- anticipar resultados de H150/H200;
- presentar EXP-11B retrieval como ejecutado;
- presentar EXP-12 como ejecutado;
- cerrar inferencialmente HE2 o HE5 antes de Grupo 3;
- convertir asociación de evidencia normativa en corrección normativa sustantiva;
- convertir la auditabilidad estructural de HE4 en corrección jurídica.

### 9. Registros de auditoría

- Revisión interna: `article/reviews/0A01_INTERNAL_REVIEW.md`.
- Revisión experimental: `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`.
- Claims: `article/CLAIM_EVIDENCE_MATRIX.md`.
- Gobernanza: `article/DECISIONS.md` y `article/SOURCE_REGISTRY.md`.

### 10. Regla de congelamiento

Este artefacto registra el ground truth documental aprobado en el corte de 0A-01. No debe editarse silenciosamente para acomodar desarrollos posteriores. Una corrección futura requiere una decisión explícita y trazable que identifique el motivo, la fuente afectada y el impacto sobre fases posteriores.

---

## English

### 1. Block status

- Block: `0A-01 — Documentary ground truth`.
- Status: `APPROVED / FROZEN`.
- Author approval date: 2026-09-02.
- Internal scientific/editorial review: `PASS WITH MINOR TERMINOLOGY CORRECTION`, corrections resolved.
- Final independent experimental review: `PASS — READY FOR AUTHOR APPROVAL`.
- Explicit author approval: received on 2026-09-02.
- Effect: this artifact is the frozen documentary reference for 0A-01 governing later article phases.

Freezing 0A-01 does not freeze the research's complete experimental state. `SRC-03` remains a living source and pending experiments retain their current status. Later experimental updates must enter through the applicable gates without silently rewriting this historical record.

### 2. Governing sources at the cutoff

| ID | Source | Function in 0A-01 | Cutoff status |
|---|---|---|---|
| SRC-01 | `Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf` | approved formulations: problem, objectives, hypotheses, justification, and scope | approved source |
| SRC-02 | `Anexo_1_NANDINA_LLM_RAG_v13.docx` | current operational architecture and methodology | current operational source |
| SRC-03 | Experimental Master Plan in `elVladdi/gci-nandina-rag`, branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | current experimental status | living source; 0A-01 snapshot read: `0a9a82181c6c3840f74f0272e5c225568474058b` |
| SRC-04 | current preliminary thesis identified by the author as `Molleapasa_gv.docx` | later formulations and detection of stale snapshots | secondary comparison source |

Automatic suffixes generated when attaching files, such as `(3)`, `(4)`, or `(5)`, do not by themselves constitute distinct scientific versions.

### 3. Frozen documentary precedence

1. **Current experimental status:** `SRC-03` plus frozen experimental artifacts and commits from the development repository.
2. **Operational architecture and methodology:** `SRC-02`.
3. **Approved problem, objectives, hypotheses, justification, and scope:** `SRC-01`.
4. **Later formulations and thesis draft:** `SRC-04`.

Any discrepancy among these sources must be made explicit. No AI in the editorial workflow may silently harmonize it.

### 4. Approved formulations — controlled English translation

The Spanish formulations in Section 4 above are the authoritative approved wording. The following English text is a controlled translation for the bilingual GitHub record and does not replace the approved Spanish source wording.

#### Approved title

**Evaluation of an offline experimental pilot for documentary information management to support auditable recommendation of NANDINA subheadings through document retrieval and controlled explanation with a local LLM**

#### General problem

**GP.** To what extent will an offline experimental pilot for documentary information management, applied to merchandise descriptions and composed of historical retrieval for ranking, normative retrieval for evidence, and a local LLM for restricted explanation of a fixed Top-3, enable the recommendation of NANDINA subheadings with measurable performance, documentary traceability, and auditability?

#### Specific problems

**SP1.** How will the labeled historical bank and the NANDINA normative corpus be structured and versioned to ensure curation, hierarchical integrity, traceability, and reproducible use in the pilot?

**SP2.** What performance will normative-retrieval strategies and historical retrieval achieve in generating and ranking NANDINA candidates according to Top-k, MRR, and candidate-set coverage metrics?

**SP3.** To what extent will integrating the historical ranking with normative evidence preserve recommendation performance and increase documentary traceability, and what effect will diagnostic use of a local LLM as a reranker have on candidate ordering?

**SP4.** To what extent will a local LLM, restricted to explaining a fixed Top-3 without introducing external codes or altering the ranking, generate structured, verifiable outputs supported by historical and normative evidence?

**SP5.** What error patterns and validity limits will be identified in the pilot regarding description quality, hierarchical proximity of subheadings, availability of historical precedents, and the internal scope of the evaluation?

#### General objective

**GO.** Evaluate, through an offline experimental pilot, the differentiated contribution of historical retrieval to candidate ranking, normative retrieval to documentary evidence, and a local LLM to the restricted and auditable explanation of a fixed Top-3 for recommending NANDINA subheadings.

#### Specific objectives

**SO1.** Build and version a labeled historical bank and a NANDINA normative corpus by applying curation, hierarchical-integrity, traceability, and reproducibility criteria.

**SO2.** Implement and compare normative-retrieval and historical-retrieval strategies to generate and rank NANDINA candidates, evaluating their performance using Top-k, MRR, and candidate-set coverage metrics.

**SO3.** Evaluate integration of the historical ranking with normative evidence and diagnostically analyze the effect of a local LLM as a reranker on candidate ordering.

**SO4.** Design and implement a local LLM restricted to explaining a fixed Top-3, without introducing external codes or altering the ranking, and evaluate the structural validity, traceability, and concordance of its explanations with retrieved evidence.

**SO5.** Quantitatively and qualitatively analyze pilot errors and limits, considering description quality, hierarchical proximity, availability of historical precedents, and the internal scope of the evaluation.

#### General hypothesis

**GH.** In an applied offline experimental pilot, functional differentiation of the components will enable an auditable recommendation of NANDINA subheadings: historical retrieval will achieve the best ranking performance, normative retrieval will provide traceable documentary evidence, and the local LLM will generate controlled explanations over a fixed Top-3 without needing to modify candidate ordering.

#### Specific hypotheses

**SH1.** Structuring and versioning the labeled historical bank and the NANDINA normative corpus will preserve hierarchical integrity, evidence provenance, and reproducibility of experimental runs.

**SH2.** Historical retrieval will achieve better Top-k and MRR performance than normative-retrieval strategies, while hierarchical normative variants and candidate-set variants will expand documentary coverage at deeper ranks.

**SH3.** Integrating the historical ranking with normative evidence will preserve historical-ranking performance and increase documentary traceability; diagnostic use of the local LLM as a reranker will not produce a consistent improvement in candidate ordering.

**SH4.** The local LLM restricted to a fixed Top-3 will generate structured outputs that retain the three candidates and their order, introduce no external codes, and link explanations to identifiable historical or normative evidence. The quality of this linkage will be evaluated using verifiability, traceability, and evidence–justification concordance criteria.

**SH5.** Pilot errors and limits will concentrate in ambiguous or incomplete descriptions, hierarchically close subheadings, cases with insufficient historical precedents, and conditions that restrict validity of the results to the internally evaluated set.

### 5. Current architecture and functions

The architecture governing later drafting is:

`Commercial description → normalization → historical retrieval → historical Top-k ranking → fixed Top-3 → normative-evidence retrieval for those candidates → context construction → local LLM → auditable explanation of the Top-3`.

Mandatory functional separation:

- **Historical retrieval:** generates and ranks the primary candidates.
- **Normative retrieval:** provides identifiable documentary evidence for candidates and does not replace or reorder the historical ranking.
- **Local LLM:** explains the previously retrieved Top-3 under controlled context; it does not classify from scratch, introduce external codes, or alter the official ranking.
- **LLM reranking:** diagnostic and secondary evaluation only; it is not part of the official primary flow.

### 6. Analysis unit and scope

- **SERIES** is the experimental and analysis unit.
- **DAM** is the original administrative unit and the grouping unit used when dependence matters.
- The normalized series description is the query unit.
- The explained Top-3 is the output unit.
- Normative documents and fragments are retrievable evidence units, not primary analysis units.
- The pilot is offline, local, non-production, and non-binding.
- Empirical evaluation is restricted to Class/Chapter 87 and the defined administrative, temporal, documentary, and experimental setting.
- Expert review remains outside the system.
- Claims of reduced processing time, reduced operational error, institutional efficiency, business performance, or legal validity of the recommendation are not authorized.

### 7. Resolved discrepancies and current rules

1. **Stale preliminary snapshot.** The `3,000/100/1,006` figures and associated preliminary-thesis results belong to an earlier experimental state and do not govern the article. Current experimental status comes from `SRC-03` and frozen artifacts.
2. **Independence and DAM.** Absence of repeated identifiers does not demonstrate partition independence. The v0.2 redesign groups by DAM to remove overlap of the same DAM across historical, development, and evaluation partitions. This does not imply internal independence among all series within a partition; inferential procedures must respect grouping when applicable.
3. **Historical v0.1 finding.** `995/1006` v0.1 evaluation cases belonged to DAMs also present in historical data. Its status is `C19 = AUTHORIZED`, only as a historical finding supporting the partition redesign.
4. **48/59 figure.** It remains `C20 = REVIEW_REQUIRED`; it must not be used as a frozen manuscript figure until traceability is completed through a versioned artifact or auditable recomputation.
5. **EXP-08 and HE5.** `outputs/evaluation/exp08_split_sensitivity_v01_vs_v02/exp08_integrated_findings_v0.2.md` records `HE5 = PARTIALLY_SUPPORTED` as a historical/intermediate interpretation specific to EXP-08. It is not the final inferential HE5 decision. Final status remains `PENDING_GROUP3`.
6. **Master Plan.** It is one logical document represented by two operational copies. The local and GitHub copies must contain identical canonical textual content; semantic equivalence is insufficient. Only the experimental AI has write authority. The scientific-editor AI and drafting AI are read-only. D-011 supersedes D-009 for synchronization, coexistence, and divergence.
7. **SRC-03 SHA.** It identifies the concrete snapshot read at a cutoff, not the immutable identity of the living Master Plan.

### 8. What 0A-01 does not authorize

Closing this block does not authorize:

- drafting manuscript sections yet;
- declaring final novelty or publishable contribution;
- defining final Research Questions;
- selecting a target journal;
- anticipating H150/H200 results;
- presenting EXP-11B retrieval as executed;
- presenting EXP-12 as executed;
- making final inferential decisions on HE2 or HE5 before Group 3;
- converting normative-evidence association into substantive normative correctness;
- converting HE4 structural auditability into legal correctness.

### 9. Audit records

- Internal review: `article/reviews/0A01_INTERNAL_REVIEW.md`.
- Experimental review: `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`.
- Claims: `article/CLAIM_EVIDENCE_MATRIX.md`.
- Governance: `article/DECISIONS.md` and `article/SOURCE_REGISTRY.md`.

### 10. Freeze rule

This artifact records the approved documentary ground truth at the 0A-01 cutoff. It must not be silently edited to accommodate later developments. Any future correction requires an explicit, traceable decision identifying the reason, affected source, and impact on later phases.
