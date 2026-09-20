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

Automated tariff coding has most often been framed as a text-to-code prediction problem: a model receives a product or declaration description and returns one or more HS labels. Early work treated this as supervised text categorization, with models trained on historical declarations and evaluated at a defined level of the tariff hierarchy. Ding et al. used a Background Net classifier to map goods-declaration text to HS categories, illustrating a conventional direct-classification formulation (Ding et al., 2015). CNN-based work later showed that short descriptions could be classified separately at HS2 and HS4, while also exposing the increased class cardinality at finer levels (Luppes, 2019). At larger scale, Ruder compared conventional machine-learning and neural classifiers on more than one million cargo descriptions spanning thousands of HS6 classes (Ruder, 2020). These studies share a supervised prediction objective, but their target levels, label spaces, datasets, and evaluation measures differ; reported percentages therefore should not be read as directly comparable measures of tariff-classification performance.

Subsequent work has changed the representation of trade text without necessarily changing that prediction objective. Anggoro et al., for example, fine-tuned Sentence-BERT with Multiple Negative Ranking loss to obtain transaction embeddings and then used those fixed-length representations as inputs to SVM and Random Forest classifiers for HS-code prediction (Anggoro et al., 2025). Other approaches exploit the hierarchy more explicitly. Lee et al. first predict a four-digit heading, retrieve relevant sentences from the HS manual, and then predict the six-digit subheading from the product description together with the retrieved sentences (Lee et al., 2021). This staged design differs from treating HS2, HS4, or HS6 as independent flat classification targets because information produced between levels can participate in the later decision.

A second family formulates the problem as retrieval or ranking rather than as a single-label decision. Stassin et al. compared supervised neural models with semantic-similarity methods over HS6, HS8, and HS10 and evaluated whether relevant codes appeared near the top of a ranked output (Stassin et al., 2023). Pain likewise used semantic textual similarity to generate ranked commodity recommendations and evaluated whether the expected commodity code appeared among the top-k suggestions (Pain, 2021). In this formulation, the model's immediate output is a candidate list that can support a subsequent human or automated decision. This distinction is operationally important: Top-k retrieval measures the presence and ordering of candidates, whereas classification accuracy evaluates a selected label. The two objectives can coexist in tariff-assistance systems, but their metrics and denominators should not be treated as interchangeable.

A third task begins from a code that has already been assigned and asks whether that assignment is coherent or plausible. Spichakova and Haav combine textual similarity with similarity derived from the HS taxonomy to assess assigned-code correctness and to provide alternative predictions or recommendations (Spichakova & Haav, 2020). Such validation or correction is not equivalent to generating candidates from an uncoded description, because the existing code is part of the object being assessed and the evaluation depends on assumptions about the historical labels used as reference.

Taken together, this literature spans direct classification, staged hierarchical prediction, candidate retrieval/ranking, and post-assignment validation. The boundaries between these tasks matter because the same technologies—embeddings, neural encoders, similarity functions, or historical records—can support different outputs and evaluation criteria. They also clarify the point at which external documentary knowledge enters a system: in some designs it participates in the classification decision itself, while in others retrieval is used to expose supporting material around candidate codes. That functional distinction motivates the next subsection on knowledge-enhanced retrieval and regulatory reasoning.

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

La clasificación arancelaria automatizada se ha formulado con frecuencia como un problema de predicción de texto a código: un modelo recibe la descripción de un producto o una declaración y devuelve una o más etiquetas HS. Los primeros trabajos abordaron esta tarea como categorización supervisada de texto, con modelos entrenados sobre declaraciones históricas y evaluados en un nivel definido de la jerarquía arancelaria. Ding et al. emplearon un clasificador Background Net para asignar el texto de declaraciones de mercancías a categorías HS, lo que ejemplifica una formulación convencional de clasificación directa (Ding et al., 2015). Trabajos posteriores con CNN mostraron que las descripciones cortas podían clasificarse por separado en HS2 y HS4, y también hicieron visible el aumento de cardinalidad de clases en niveles más finos (Luppes, 2019). A mayor escala, Ruder comparó clasificadores de aprendizaje automático convencional y redes neuronales sobre más de un millón de descripciones de carga distribuidas entre miles de clases HS6 (Ruder, 2020). Estos estudios comparten un objetivo de predicción supervisada, pero difieren en nivel objetivo, espacio de etiquetas, datasets y medidas de evaluación; por ello, sus porcentajes reportados no deben interpretarse como medidas directamente comparables del desempeño de clasificación arancelaria.

Trabajos posteriores han modificado la representación del texto comercial sin cambiar necesariamente ese objetivo de predicción. Anggoro et al., por ejemplo, ajustaron Sentence-BERT con Multiple Negative Ranking loss para obtener embeddings de transacciones y utilizaron después esas representaciones de longitud fija como entradas de clasificadores SVM y Random Forest para predecir códigos HS (Anggoro et al., 2025). Otros enfoques explotan de manera más explícita la jerarquía. Lee et al. predicen primero un heading de cuatro dígitos, recuperan oraciones pertinentes del manual HS y posteriormente predicen la subpartida de seis dígitos a partir de la descripción del producto junto con las oraciones recuperadas (Lee et al., 2021). Este diseño por etapas difiere de tratar HS2, HS4 o HS6 como objetivos planos independientes, porque la información producida entre niveles puede participar en la decisión posterior.

Una segunda familia formula el problema como recuperación o ranking, en lugar de una decisión de etiqueta única. Stassin et al. compararon modelos neuronales supervisados con métodos de similitud semántica en HS6, HS8 y HS10 y evaluaron si los códigos pertinentes aparecían en las primeras posiciones de una salida ordenada (Stassin et al., 2023). Pain también empleó similitud textual semántica para generar recomendaciones ordenadas de mercancías y evaluó si el código esperado aparecía entre las sugerencias Top-k (Pain, 2021). En esta formulación, la salida inmediata del modelo es una lista de candidatos que puede apoyar una decisión humana o automatizada posterior. Esta distinción es importante en términos operativos: las métricas Top-k de recuperación evalúan la presencia y el orden de candidatos, mientras que la accuracy de clasificación evalúa una etiqueta seleccionada. Ambos objetivos pueden coexistir en sistemas de asistencia arancelaria, pero sus métricas y denominadores no deben tratarse como intercambiables.

Una tercera tarea parte de un código ya asignado y pregunta si esa asignación es coherente o plausible. Spichakova y Haav combinan similitud textual con similitud derivada de la taxonomía HS para evaluar la corrección del código asignado y proporcionar predicciones o recomendaciones alternativas (Spichakova & Haav, 2020). Esta validación o corrección no equivale a generar candidatos desde una descripción sin código, porque el código existente forma parte del objeto evaluado y la evaluación depende de supuestos sobre las etiquetas históricas utilizadas como referencia.

En conjunto, esta literatura abarca clasificación directa, predicción jerárquica por etapas, recuperación/ranking de candidatos y validación posterior a la asignación. Las fronteras entre estas tareas son relevantes porque las mismas tecnologías —embeddings, codificadores neuronales, funciones de similitud o registros históricos— pueden sostener salidas y criterios de evaluación diferentes. También permiten precisar el punto en que el conocimiento documental externo entra al sistema: en algunos diseños participa en la propia decisión de clasificación, mientras que en otros la recuperación se utiliza para exponer material de respaldo alrededor de códigos candidatos. Esta diferencia funcional prepara la siguiente subsección sobre recuperación enriquecida con conocimiento y razonamiento regulatorio.

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
