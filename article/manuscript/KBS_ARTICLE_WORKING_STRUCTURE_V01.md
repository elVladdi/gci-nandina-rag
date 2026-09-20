# KBS Article Working Structure V01

```text
STRUCTURE_ID = KBS_ARTICLE_WORKING_STRUCTURE_V01
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
APPROVAL_DECISION = D-015
PURPOSE = CUMULATIVE_BASE_FOR_SUBSEQUENT_MANUSCRIPT_VERSIONS
WORD_FILENAME = KBS_ARTICLE_WORKING_STRUCTURE_V01.docx
WORD_SHA256 = 0336e2a433e843c48702ef818b7e59ab0d3545022fc95874e85d26694af526b5
```

This file defines the complete approved structure of the article. It contains headings and drafting-purpose notes only; it does not approve manuscript prose. Future manuscript deliveries must preserve this cumulative structure unless the author explicitly approves a controlled amendment.

Structural principle: **problem and positioning → general decision-support architecture → specific experimental instantiation → evidence → interpretation**. The specific experimental testbed must not define the conceptual scope of the architecture.

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

Only here does the manuscript move from the general architecture to the specific empirical instantiation used to evaluate it.

## 4.1. Evaluation setting

Introduce the offline regulatory/classification testbed and delimit the non-binding decision-support scope.

## 4.2. Historical data

### 4.2.1. Data source and selection

### 4.2.2. Target class space

### 4.2.3. Preparation and curation

### 4.2.4. Versioned datasets used in the experiment

## 4.3. Documentary corpus

### 4.3.1. Source documents and scope

### 4.3.2. Corpus preparation

### 4.3.3. Versioning and temporal validity

### 4.3.4. Retrieval index

## 4.4. Partitioning and dependence control

Series-level observation, DAM-level grouping where dependence exists, split construction, leakage controls, duplicates and near-duplicate diagnostics.

## 4.5. System configuration

## 4.6. Evaluation framework and research-question mapping

Map `RQ → function → output → metric → permitted interpretation`.

## 4.7. Candidate-retrieval evaluation

## 4.8. Documentary-evidence evaluation

## 4.9. Controlled-explanation evaluation

## 4.10. Statistical analysis

Populate only with analyses finally authorized by the experimental master plan.

## 4.11. Reproducibility resources

Identify the public reproducibility repository and the exact scope of versioned data, configurations, scripts, manifests, hashes, instructions and declared limitations.

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

## 4.1. Entorno de evaluación

## 4.2. Datos históricos

### 4.2.1. Fuente y selección de datos

### 4.2.2. Espacio de clases objetivo

### 4.2.3. Preparación y curación

### 4.2.4. Datasets versionados utilizados en el experimento

## 4.3. Corpus documental

### 4.3.1. Documentos fuente y alcance

### 4.3.2. Preparación del corpus

### 4.3.3. Versionado y validez temporal

### 4.3.4. Índice de recuperación

## 4.4. Particionamiento y control de dependencia

## 4.5. Configuración del sistema

## 4.6. Marco de evaluación y correspondencia con las preguntas de investigación

## 4.7. Evaluación de recuperación de candidatos

## 4.8. Evaluación de recuperación de evidencia documental

## 4.9. Evaluación de explicaciones controladas

## 4.10. Análisis estadístico

## 4.11. Recursos de reproducibilidad

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
