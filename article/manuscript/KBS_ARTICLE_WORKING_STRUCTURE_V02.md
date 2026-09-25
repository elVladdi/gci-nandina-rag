# KBS Article Working Structure V02

```text
STRUCTURE_ID = KBS_ARTICLE_WORKING_STRUCTURE_V02
PARENT_STRUCTURE = KBS_ARTICLE_WORKING_STRUCTURE_V01
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
APPROVAL_DECISION = D-045
AMENDMENT_SCOPE = SECTION_4_CONTROLLED_RESTRUCTURE
PURPOSE = CUMULATIVE_BASE_FOR_SUBSEQUENT_MANUSCRIPT_VERSIONS
```

This file preserves the previously approved article structure except for the author-approved controlled restructuring of Section 4. It contains headings and drafting-purpose notes only; it does not approve manuscript prose. Future manuscript deliveries must preserve this cumulative structure unless the author explicitly approves another controlled amendment.

Structural principle: **problem and positioning → general decision-support architecture → specific experimental instantiation → evidence → interpretation**. The specific experimental testbed must not define the conceptual scope of the architecture.

For Section 4, the governing editorial principle is: **Methods describes the scientific objects, procedures, design decisions, execution conditions, evaluation protocols, and validity controls; exhaustive technical artifact identity belongs in reproducibility manifests/resources unless a concrete identifier is methodologically indispensable.**

---

# PART I — English manuscript master

## Title

Draft at the end. Foreground the scientific/architectural contribution; the customs domain may appear as application/testbed only if it improves precision.

## Abstract

Recommended order: concrete problem → limitation → proposed architecture → evaluation → main findings → bounded implication.

## Keywords

Select after final title and abstract.

# 1. Introduction

Prefer a continuous narrative unless final length justifies visible subsections. Internal rhetorical sequence:

- practical and scientific problem;
- concise synthesis of prior approaches;
- precise technical limitation;
- why the limitation matters;
- high-level proposal before experimental details;
- explicit contributions;
- evaluation context introduced only after the proposal is clear;
- final Research Questions;
- short roadmap.

# 2. Related work

## 2.1. Automated tariff classification and candidate retrieval

## 2.2. Knowledge-enhanced retrieval and regulatory reasoning

## 2.3. LLMs for classification, reasoning, and explanation

## 2.4. Evidence grounding, explainability, and auditability

## 2.5. Reproducibility and evaluation in knowledge-based decision support

## 2.6. Positioning of this study

Short comparative synthesis. A compact literature-positioning table may be used if every comparison is supported.

# 3. Decision-support architecture

Describe the general architecture before the empirical instantiation. Do not open this section with NANDINA, Chapter/Class 87, the Peruvian documentary corpus, H100, or experimental sample sizes.

## 3.1. Overview and information flow

Overall flow and architecture figure.

## 3.2. Query representation and normalization

## 3.3. Historical candidate retrieval and ranking

## 3.4. Fixed candidate set

## 3.5. Candidate-specific documentary retrieval

## 3.6. Evidence-context construction and controlled explanation

## 3.7. Configurability and interface requirements

State replaceable resources and explicit preconditions. Preserve `configurability/replicability ≠ empirical performance transfer`.

# 4. Experimental design

Present the offline experimental evaluation of a concrete instantiation of the Section-3 architecture. The empirical NANDINA/Chapter-87 setting bounds the evaluation; it does not define the conceptual scope of the architecture.

## 4.1. Experimental setting and scope

State the objective and controlled offline setting of the evaluation; the empirical code level/domain; SERIE as the analysis unit; DAM/customs declaration as the grouping unit where dependence matters; and the interpretation boundary that performance evidence belongs to this evaluated instantiation. Do not define the experiment primarily as a “non-binding decision-support pilot.” Prefer `evaluate` over `validate` unless an explicit validation criterion is defined and supported.

## 4.2. Historical data and experimental dataset construction

Explain the historical-data resource through provenance, acquisition, processing, curation, partition construction, and scientifically relevant composition. Do not organize the narrative around internal repository artifacts.

### 4.2.1. Source and data collection

Begin with the administrative source and the actual collection procedure: temporal scope, eligibility/selection criteria, manual collection where applicable, and the fields needed to represent each SERIE and its DAM. Intermediate spreadsheets/files are working artifacts, not the scientific source that should govern the narrative.

### 4.2.2. Processing and curation

Describe the automated transformation into a series-level analytical structure, text preparation, field derivation/validation, exclusion rules, duplicate/conflict handling, and delimitation to the evaluated Chapter-87 setting. Explain scientifically relevant operations rather than internal script names, repository paths, worksheet names, or fingerprints.

### 4.2.3. Partition construction and dataset composition

Explain construction of the historical, development, and evaluation partitions while preserving DAM as the grouping unit. State the relevant non-overlap controls and characterize each final partition using scientifically meaningful counts, preferably in a compact table if that improves readability. The former standalone “Target class space” subsection is removed: eight-digit NANDINA/Chapter 87 belongs to 4.1, while represented-code counts belong here.

## 4.3. Documentary corpus and evidence resource

Identify the documentary/normative sources, their authority and temporal boundary, and the resource used to provide candidate-specific evidence. Explain corpus preparation and representation, including hierarchical structure when methodologically relevant. Physical filenames, paths, hashes, and index artifacts belong to reproducibility resources unless indispensable to understanding the method.

## 4.4. Partition validity and dependence controls

Concentrate the controls that justify analytical use of the partitions: DAM separation, leakage checks, duplicate/near-duplicate diagnostics, historical-support conditions where relevant, and other authorized validity diagnostics. Distinguish design/validity controls from performance results.

## 4.5. Experimental system configuration and execution

Instantiate the Section-3 architecture without re-explaining it conceptually. Report only execution choices that materially affect the experiment: query representation, historical retrieval configuration, Top-k/Top-3 construction, candidate-specific documentary retrieval, context construction, local model/generation restrictions, and material software/hardware/runtime conditions. Use a compact configuration table if it improves readability.

## 4.6. Evaluation framework and protocols

Map `RQ → system function → output → evaluation unit → metric/protocol → permitted interpretation`. Preserve the separation among candidate ranking, documentary association, and controlled explanation.

### 4.6.1. Candidate-retrieval evaluation

Define the authorized retrieval metrics, evaluation unit, comparison logic, and interpretation boundary. Candidate-retrieval performance is not overall system/classification accuracy.

### 4.6.2. Documentary-evidence evaluation

Define the authorized coverage/association/traceability criteria. Documentary association is not substantive normative or legal correctness.

### 4.6.3. Controlled-explanation evaluation

Define the authorized structural, traceability/auditability, evidence-concordance, and other approved criteria/rubrics together with their limitations. Explanation quality does not establish legal correctness or faithful causal reconstruction of upstream ranking.

## 4.7. Statistical and robustness analysis

Include only inferential, sensitivity, and robustness analyses finally authorized by the experimental Master Plan. State units, comparisons, assumptions, and interpretation limits without anticipating results.

## 4.8. Reproducibility resources

Explain what the public reproducibility repository allows another researcher to reconstruct and which classes of resources it contains or references: redistributable data, configurations, code, manifests, documentation, and access/redistribution limitations. Do not turn the main prose into an inventory of SHA-256 values, internal paths, or filenames; exhaustive technical identities belong in the repository/manifests.

# 5. Results

Organize by scientific function/RQ, not by internal experiment IDs or execution chronology.

## 5.1. Data and partition checks

## 5.2. Candidate retrieval performance

Do not label candidate-retrieval metrics as overall system accuracy.

## 5.3. Documentary evidence retrieval

## 5.4. Controlled explanation quality

## 5.5. Sensitivity and robustness analyses

Only reconciled and authorized analyses.

## 5.6. Inferential results

Populate only after the relevant Group 3 analyses are closed and authorized for article use.

## 5.7. Summary by research question

Optional; retain only if it improves readability.

# 6. Discussion

## 6.1. Separating candidate ranking from documentary evidence

## 6.2. Controlled use of the LLM for explanation

## 6.3. Comparison with prior work

## 6.4. Implications for auditable decision support

## 6.5. Configurability and transfer conditions

## 6.6. Limitations

Consolidate benchmark/data limits, documentary-corpus and normative-drift limits, explanation-evaluation limits, legal-validity boundaries, external validity and reproducibility constraints.

# 7. Conclusion

Close on contribution → main evidence → scope → implication.

# Data availability

# Code and reproducibility resources

Retain as a separate statement only if appropriate under the final KBS submission format; otherwise integrate with Data availability.

# CRediT authorship contribution statement

# Funding

# Declaration of competing interest

# Acknowledgements

Only if applicable.

# References

# Supplementary material

Optional.

---

# PART II — Spanish semantic-control mirror

## Título

## Resumen

## Palabras clave

# 1. Introducción

Secuencia interna: problema → enfoques previos → limitación técnica → importancia → propuesta → contribuciones → contexto de evaluación → RQ → organización.

# 2. Trabajos relacionados

## 2.1. Clasificación arancelaria automatizada y recuperación de candidatos

## 2.2. Recuperación enriquecida con conocimiento y razonamiento regulatorio

## 2.3. LLM para clasificación, razonamiento y explicación

## 2.4. Fundamentación en evidencia, explicabilidad y auditabilidad

## 2.5. Reproducibilidad y evaluación en apoyo a decisiones basado en conocimiento

## 2.6. Posicionamiento del estudio

# 3. Arquitectura de apoyo a decisiones

## 3.1. Vista general y flujo de información

## 3.2. Representación y normalización de la consulta

## 3.3. Recuperación histórica y ranking de candidatos

## 3.4. Conjunto fijo de candidatos

## 3.5. Recuperación documental específica por candidato

## 3.6. Construcción de contexto y explicación controlada

## 3.7. Configurabilidad y requisitos de interfaz

# 4. Diseño experimental

Presentar la evaluación experimental offline de una instanciación concreta de la arquitectura de la Sección 3. El escenario empírico NANDINA/Capítulo 87 delimita la evaluación, no el alcance conceptual de la arquitectura.

## 4.1. Entorno y alcance experimental

Establecer el objetivo y las condiciones controladas de la evaluación offline; el nivel/dominio empírico de códigos; SERIE como unidad de análisis; DAM/declaración aduanera como unidad de agrupamiento cuando corresponda; y el límite interpretativo de que la evidencia de desempeño pertenece a esta instanciación evaluada. No definir el experimento principalmente como «piloto no vinculante de apoyo a decisiones». Preferir `evaluar` frente a `validar` salvo criterio explícito y sustentado de validación.

## 4.2. Datos históricos y construcción de los datasets experimentales

Explicar el recurso histórico mediante procedencia, adquisición, procesamiento, curación, construcción de particiones y composición científicamente relevante. No organizar la narración alrededor de artefactos internos del repositorio.

### 4.2.1. Fuente y recolección

Comenzar por la fuente administrativa y el procedimiento real de obtención: alcance temporal, criterios de elegibilidad/selección, recolección manual cuando corresponda y campos necesarios para representar cada SERIE y su DAM. Los Excel/archivos intermedios son artefactos de trabajo, no la fuente científica que debe gobernar la narración.

### 4.2.2. Procesamiento y curación

Describir la transformación automatizada hacia una estructura analítica por SERIE, preparación del texto, derivación/validación de campos, reglas de exclusión, tratamiento de duplicados/conflictos y delimitación al escenario evaluado del Capítulo 87. Explicar operaciones científicamente relevantes y no nombres internos de scripts, rutas, hojas físicas o fingerprints.

### 4.2.3. Construcción de particiones y composición

Explicar la construcción de los conjuntos histórico, desarrollo y evaluación preservando DAM como unidad de agrupamiento. Declarar los controles de no solapamiento relevantes y caracterizar cada partición final mediante conteos científicamente significativos, preferentemente en una tabla compacta si mejora la lectura. Se elimina la antigua subsección autónoma «Espacio de clases objetivo»: NANDINA de ocho dígitos/Capítulo 87 pertenece a 4.1 y los conteos de códigos representados pertenecen aquí.

## 4.3. Corpus documental y recurso de evidencia

Identificar las fuentes documentales/normativas, su autoridad y frontera temporal, y el recurso utilizado para aportar evidencia específica por candidato. Explicar preparación y representación del corpus, incluida la estructura jerárquica cuando sea metodológicamente pertinente. Nombres físicos de archivos, rutas, hashes y artefactos de índice pertenecen a los recursos de reproducibilidad salvo que sean indispensables para comprender el método.

## 4.4. Validez de particiones y control de dependencia

Concentrar los controles que justifican el uso analítico de las particiones: separación por DAM, controles de leakage, diagnósticos de duplicados/near-duplicates, condiciones de soporte histórico cuando correspondan y otros diagnósticos de validez autorizados. Distinguir controles de diseño/validez de resultados de desempeño.

## 4.5. Configuración y ejecución experimental

Instanciar la arquitectura de la Sección 3 sin volver a explicarla conceptualmente. Reportar solo decisiones de ejecución que afecten materialmente el experimento: representación de consulta, configuración de recuperación histórica, construcción del Top-k/Top-3, recuperación documental por candidato, construcción del contexto, modelo local/restricciones de generación y condiciones materiales de software/hardware/ejecución. Utilizar una tabla compacta de configuración si mejora la lectura.

## 4.6. Marco y protocolos de evaluación

Mapear `RQ → función del sistema → salida → unidad de evaluación → métrica/protocolo → interpretación permitida`. Mantener la separación entre ranking de candidatos, asociación documental y explicación controlada.

### 4.6.1. Evaluación de recuperación de candidatos

Definir las métricas autorizadas de recuperación, unidad de evaluación, lógica de comparación y límite interpretativo. El desempeño de recuperación de candidatos no constituye accuracy global del sistema/clasificación.

### 4.6.2. Evaluación de evidencia documental

Definir criterios autorizados de cobertura/asociación/trazabilidad. La asociación documental no constituye corrección normativa o jurídica sustantiva.

### 4.6.3. Evaluación de explicación controlada

Definir criterios/rúbricas autorizados de estructura, trazabilidad/auditabilidad, concordancia con evidencia y demás dimensiones aprobadas, junto con sus limitaciones. La calidad de explicación no establece corrección jurídica ni reconstrucción causal fiel del ranking upstream.

## 4.7. Análisis estadístico y de robustez

Incluir únicamente análisis inferenciales, de sensibilidad y robustez finalmente autorizados por el Plan Maestro experimental. Especificar unidades, comparaciones, supuestos y límites de interpretación sin anticipar resultados.

## 4.8. Recursos de reproducibilidad

Explicar qué permite reconstruir el repositorio público de reproducibilidad y qué clases de recursos contiene o referencia: datos redistribuibles, configuraciones, código, manifiestos, documentación y limitaciones de acceso/redistribución. No convertir la prosa principal en un inventario de SHA-256, rutas internas o nombres de archivos; las identidades técnicas exhaustivas pertenecen al repositorio/manifiestos.

# 5. Resultados

## 5.1. Controles de datos y particiones

## 5.2. Desempeño de recuperación de candidatos

## 5.3. Recuperación de evidencia documental

## 5.4. Calidad de la explicación controlada

## 5.5. Análisis de sensibilidad y robustez

## 5.6. Resultados inferenciales

## 5.7. Síntesis por pregunta de investigación

# 6. Discusión

## 6.1. Separación entre ranking de candidatos y evidencia documental

## 6.2. Uso controlado del LLM para explicación

## 6.3. Comparación con trabajos previos

## 6.4. Implicaciones para apoyo a decisiones auditable

## 6.5. Configurabilidad y condiciones de transferencia

## 6.6. Limitaciones

# 7. Conclusión

# Disponibilidad de datos

# Código y recursos de reproducibilidad

# Declaración CRediT de contribución de autoría

# Financiamiento

# Declaración de conflictos de interés

# Agradecimientos

# Referencias

# Material suplementario
