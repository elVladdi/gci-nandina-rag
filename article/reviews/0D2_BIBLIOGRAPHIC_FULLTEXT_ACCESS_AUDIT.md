# 0D-2 — Auditoría de acceso full-text del corpus bibliográfico / Bibliographic Full-Text Access Audit

## Español

### 1. Objeto y alcance

Esta auditoría técnica-editorial verifica la disponibilidad efectiva y reutilizable del corpus bibliográfico consolidado requerido antes de abrir Fase 1. No reabre 0B, no reevalúa novelty/gap, no modifica la taxonomía de literatura y no autoriza claims nuevos.

Para cada fuente se comprueba, al nivel necesario para futura redacción:

```text
reference_identity_verified
full_text_or_pdf_accessible
source_text_searchable_or_inspectable
stable_source_identifier_available
citation_comment_support_possible
```

La auditoría se ejecutó contra el corpus consolidado de 62 fuentes. Se usaron los archivos full-text disponibles en la File Library del proyecto/cuenta y, para las fuentes oficiales o journal-native sin archivo local independiente recuperable, su texto completo primario y estable en la web oficial.

### 2. Aclaración crítica: 62 fuentes no equivalen a 62 PDF locales

El resultado no debe describirse como “62 PDF locales disponibles”. El estado exacto es:

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
FILE_LIBRARY_FULLTEXT = 58
OFFICIAL_PRIMARY_WEB_FULLTEXT = 4
PDF_FORMAT_FULLTEXT = 59
AUTHORITATIVE_HTML_FULLTEXT = 3
INACCESSIBLE = 0
```

Los 59 full-text en formato PDF corresponden a 58 documentos recuperables directamente desde File Library más el PDF oficial WCO de las General Rules for the Interpretation of the Harmonized System. Las tres fuentes restantes son full-text HTML primario/autoritativo: los dos procedimientos SUNAT y el artículo de Al-Hawamdeh en Information Research.

Por tanto, **el requisito científicamente relevante sí se cumple: las 62 fuentes pueden volver a inspeccionarse a texto completo para sustentar una cita**.

### 3. Fuentes primarias web sin PDF local independiente requerido

| REF | Fuente | Canal primario actual | Estado |
|---|---|---|---|
| REF-049 | SUNAT — DESPA-PE.00.03, Reconocimiento físico – extracción y análisis de muestras | `https://www.sunat.gob.pe/legislacion/procedim/despacho/procAsociados/despa-pe.00.03.htm` | `PASS / OFFICIAL_PRIMARY_HTML_FULLTEXT` |
| REF-050 | SUNAT — DESPA-PG.01, Importación para el consumo | `https://www.sunat.gob.pe/legislacion/procedim/despacho/importacion/importac/procGeneral/despa-pg.01.htm` | `PASS / OFFICIAL_PRIMARY_HTML_FULLTEXT` |
| REF-053 | WCO — General Rules for the Interpretation of the Harmonized System | `https://www.wcoomd.org/-/media/wco/public/global/pdf/topics/nomenclature/instruments-and-tools/hs-nomenclature-2022/2022/0001_2022e-gir.pdf?la=en` | `PASS / OFFICIAL_PRIMARY_PDF_FULLTEXT` |
| REF-056 | Al-Hawamdeh — Knowledge Management: Re-thinking Information Management and Facing the Challenge of Managing Tacit Knowledge | `https://informationr.net/ir/8-1/paper143.html` | `PASS / JOURNAL_PRIMARY_HTML_FULLTEXT` |

Para REF-049 y REF-050, la fuente viva oficial SUNAT es preferible a una copia PDF estática cuando el claim dependa de vigencia o versión. Para REF-053, se verificó el PDF oficial WCO de una página con las seis General Rules. REF-056 se encuentra íntegramente inspeccionable en el sitio del journal.

### 4. Manifiesto canónico de acceso

Los identificadores `REF-001`–`REF-062` quedan establecidos como identificadores internos estables de recuperación para la redacción. No sustituyen DOI, arXiv ID, URL institucional u otro identificador bibliográfico; los complementan para evitar ambigüedad entre duplicados de File Library.

| REF | Fuente canónica | Canal actual | Estado |
|---|---|---|---|
| REF-001 | A Deterministic Agentic Workflow for HS Tariff Classification: Multi-Dimensional Rule Reasoning with Interpretable Decisions | FILE_LIBRARY_FULLTEXT | PASS |
| REF-002 | ATLAS: Benchmarking and Adapting LLMs for Global Trade via Harmonized Tariff Code Classification | FILE_LIBRARY_FULLTEXT | PASS |
| REF-003 | An Ensemble-based Approach for Assigning Text to Correct Harmonized System Code | FILE_LIBRARY_FULLTEXT | PASS |
| REF-004 | Application of Machine Learning for Assessment of HS Code Correctness | FILE_LIBRARY_FULLTEXT | PASS |
| REF-005 | Application of Machine Learning for Automated HS-6 Code Assignment | FILE_LIBRARY_FULLTEXT | PASS |
| REF-006 | Attribute Knowledge and KBGAT for Predicting the Accuracy of the Harmonized System Code for Classifying Import and Export Commodities | FILE_LIBRARY_FULLTEXT | PASS |
| REF-007 | Auto-Categorization of HS Code Using Background Net Approach | FILE_LIBRARY_FULLTEXT | PASS |
| REF-008 | Automatic Product Classification in International Trade: Machine Learning and Large Language Models | FILE_LIBRARY_FULLTEXT | PASS |
| REF-009 | Automatic Tariff Classification System using Deep Learning | FILE_LIBRARY_FULLTEXT | PASS |
| REF-010 | Automating Harmonized System (HS) Code Classification from Unstructured Shipping Manifests using Large Language Models | FILE_LIBRARY_FULLTEXT | PASS |
| REF-011 | Similarity versus Supervision: Best Approaches for HS Code Prediction | FILE_LIBRARY_FULLTEXT | PASS |
| REF-012 | Classification of Goods Using Text Descriptions With Sentences Retrieval | FILE_LIBRARY_FULLTEXT | PASS |
| REF-013 | Classifying Short Text for the Harmonized System with Convolutional Neural Networks | FILE_LIBRARY_FULLTEXT | PASS |
| REF-014 | Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Schedule Code Classification | FILE_LIBRARY_FULLTEXT | PASS |
| REF-015 | Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification | FILE_LIBRARY_FULLTEXT | PASS |
| REF-016 | Customs Tariff Classification and the Use of Assistive Technologies | FILE_LIBRARY_FULLTEXT | PASS |
| REF-017 | Development of an Automated HS Code Classification System Using LLM Based on an Optimized RAG Framework | FILE_LIBRARY_FULLTEXT | PASS |
| REF-018 | Explainable Product Classification for Customs | FILE_LIBRARY_FULLTEXT | PASS |
| REF-019 | Harmonized System Code Classification Using Transfer Learning with Pre-Trained Weights | FILE_LIBRARY_FULLTEXT | PASS |
| REF-020 | HS Code Recommendation System for Imported Goods Based on Embedding-Based Similarity Measurement | FILE_LIBRARY_FULLTEXT | PASS |
| REF-021 | HSCodeComp: A Realistic and Expert-Level Benchmark for Deep Search Agents in Hierarchical Rule Application | FILE_LIBRARY_FULLTEXT | PASS |
| REF-022 | HSGraphAgent: Knowledge-Graph-Guided Large Language Models for Harmonized System Code Classification | FILE_LIBRARY_FULLTEXT | PASS |
| REF-023 | HS Code Prediction Tool Using Machine Learning | FILE_LIBRARY_FULLTEXT | PASS |
| REF-024 | Harmonized System Code Classification Using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Ranking Loss | FILE_LIBRARY_FULLTEXT | PASS |
| REF-025 | ICCA-RAG: Intelligent Customs Clearance Assistant Using Retrieval-Augmented Generation (RAG) | FILE_LIBRARY_FULLTEXT | PASS |
| REF-026 | LLM-Based Robust Product Classification in Commerce and Compliance | FILE_LIBRARY_FULLTEXT | PASS |
| REF-027 | Multimodal Approach for Harmonized System Code Prediction | FILE_LIBRARY_FULLTEXT | PASS |
| REF-028 | Text2Trade: A Semantic Search System with Monte Carlo Dropout Uncertainty Quantification for HS Code Retrieval | FILE_LIBRARY_FULLTEXT | PASS |
| REF-029 | ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT | FILE_LIBRARY_FULLTEXT | PASS |
| REF-030 | Dense Passage Retrieval for Open-Domain Question Answering | FILE_LIBRARY_FULLTEXT | PASS |
| REF-031 | Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs | FILE_LIBRARY_FULLTEXT | PASS |
| REF-032 | Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks | FILE_LIBRARY_FULLTEXT | PASS |
| REF-033 | ExtractGPT: Exploring the Potential of Large Language Models for Product Attribute Value Extraction | FILE_LIBRARY_FULLTEXT | PASS |
| REF-034 | Leveraging Passage Retrieval with Generative Models for Open Domain Question Answering | FILE_LIBRARY_FULLTEXT | PASS |
| REF-035 | Passage Re-Ranking with BERT | FILE_LIBRARY_FULLTEXT | PASS |
| REF-036 | Product Information Extraction using ChatGPT | FILE_LIBRARY_FULLTEXT | PASS |
| REF-037 | Query Expansion by Prompting Large Language Models | FILE_LIBRARY_FULLTEXT | PASS |
| REF-038 | Query Rewriting for Retrieval-Augmented Large Language Models | FILE_LIBRARY_FULLTEXT | PASS |
| REF-039 | Query2doc: Query Expansion with Large Language Models | FILE_LIBRARY_FULLTEXT | PASS |
| REF-040 | REALM: Retrieval-Augmented Language Model Pre-Training | FILE_LIBRARY_FULLTEXT | PASS |
| REF-041 | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | FILE_LIBRARY_FULLTEXT | PASS |
| REF-042 | Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | FILE_LIBRARY_FULLTEXT | PASS |
| REF-043 | SimCSE: Simple Contrastive Learning of Sentence Embeddings | FILE_LIBRARY_FULLTEXT | PASS |
| REF-044 | The Probabilistic Relevance Framework: BM25 and Beyond | FILE_LIBRARY_FULLTEXT | PASS |
| REF-045 | Using LLMs for the Extraction and Normalization of Product Attribute Values | FILE_LIBRARY_FULLTEXT | PASS |
| REF-046 | FAIR Data Pipeline: Provenance-Driven Data Management for Traceable Scientific Workflows | FILE_LIBRARY_FULLTEXT | PASS |
| REF-047 | Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing | FILE_LIBRARY_FULLTEXT | PASS |
| REF-048 | Conceptual Approaches for Defining Data, Information, and Knowledge | FILE_LIBRARY_FULLTEXT | PASS |
| REF-049 | Procedimiento específico “Reconocimiento físico – extracción y análisis de muestras” DESPA-PE.00.03 — SUNAT | OFFICIAL_PRIMARY_HTML_FULLTEXT | PASS |
| REF-050 | Procedimiento general “Importación para el consumo” DESPA-PG.01 — SUNAT | OFFICIAL_PRIMARY_HTML_FULLTEXT | PASS |
| REF-051 | Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science | FILE_LIBRARY_FULLTEXT | PASS |
| REF-052 | Datasheets for Datasets | FILE_LIBRARY_FULLTEXT | PASS |
| REF-053 | General Rules for the Interpretation of the Harmonized System — WCO | OFFICIAL_PRIMARY_PDF_FULLTEXT | PASS |
| REF-054 | Improving Reproducibility in Machine Learning Research: A Report from the NeurIPS 2019 Reproducibility Program | FILE_LIBRARY_FULLTEXT | PASS |
| REF-055 | Introduction to Information Retrieval | FILE_LIBRARY_FULLTEXT | PASS |
| REF-056 | Knowledge Management: Re-thinking Information Management and Facing the Challenge of Managing Tacit Knowledge | JOURNAL_PRIMARY_HTML_FULLTEXT | PASS |
| REF-057 | Manual de Frascati 2015: Guía para la recopilación y presentación de información sobre la investigación y el desarrollo experimental | FILE_LIBRARY_FULLTEXT | PASS |
| REF-058 | Model Cards for Model Reporting | FILE_LIBRARY_FULLTEXT | PASS |
| REF-059 | Positivism and Post-Positivism as the Basis of Quantitative Research in Pedagogy | FILE_LIBRARY_FULLTEXT | PASS |
| REF-060 | Qualitative Research in Counseling Psychology: A Primer on Research Paradigms and Philosophy of Science | FILE_LIBRARY_FULLTEXT | PASS |
| REF-061 | The Duality of Knowledge | FILE_LIBRARY_FULLTEXT | PASS |
| REF-062 | The TREC-8 Question Answering Track Evaluation | FILE_LIBRARY_FULLTEXT | PASS |

### 5. Regla obligatoria para la redacción futura

El `PASS` de acceso significa únicamente que el texto fuente puede recuperarse de nuevo. **No sustituye la lectura claim-level ni autoriza una cita por memoria.**

Cada vez que la IA de Redacción use una referencia deberá:

1. recuperar nuevamente la fuente full-text correspondiente a `REF-xxx`;
2. verificar identidad bibliográfica contra el corpus congelado;
3. localizar el pasaje exacto que sostiene el claim;
4. comprobar que el claim no excede fuerza, alcance, población, tarea, dataset o causalidad de la fuente;
5. insertar la cita conforme a la gobernanza vigente;
6. crear en el Word el comentario anclado obligatorio con extracto original, traducción, justificación y límite;
7. detener la entrega si la fuente no puede recuperarse o el pasaje no respalda el claim.

Si en una sesión futura una fuente de File Library deja de recuperarse, el estado global de esta auditoría histórica no permite fingir acceso: esa instancia se marca `ACCESS_RECHECK_REQUIRED` y se usa un canal legítimo alternativo o se solicita el archivo al autor.

### 6. Dictamen

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CANONICAL_ACCESS_MANIFEST = CREATED
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
FILE_LIBRARY_FULLTEXT = 58
OFFICIAL_PRIMARY_WEB_FULLTEXT = 4
PDF_FORMAT_FULLTEXT = 59
AUTHORITATIVE_HTML_FULLTEXT = 3
INACCESSIBLE = 0
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
BIBLIOGRAPHIC_SCIENTIFIC_REASSESSMENT = NOT_PERFORMED
PHASE_0B = REMAINS_CLOSED_AND_FROZEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
PHASE_1 = BLOCKED_PENDING_AUTHOR_APPROVAL_AND_0D_FREEZE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### 1. Scope

This technical-editorial audit verifies effective and reusable full-text access to the consolidated bibliographic corpus before Phase 1. It does not reopen Phase 0B, reassess novelty/gap, modify the literature taxonomy, or authorize new claims.

The 62-source corpus was checked against the full-text files currently retrievable through the account/project File Library and, where no independent local file is required or surfaced, against stable authoritative primary web full text.

### 2. Exact access result

The corpus must not be described as “62 local PDFs.” The accurate state is:

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
FILE_LIBRARY_FULLTEXT = 58
OFFICIAL_PRIMARY_WEB_FULLTEXT = 4
PDF_FORMAT_FULLTEXT = 59
AUTHORITATIVE_HTML_FULLTEXT = 3
INACCESSIBLE = 0
```

Fifty-eight sources are directly retrievable as full-text files from File Library. WCO REF-053 is additionally available as the official primary PDF, bringing PDF-format full text to 59. REF-049, REF-050, and REF-056 are authoritative complete HTML sources. Thus all 62 sources can currently be reinspected at full-text level for claim–citation–source auditing.

The four primary-web channels are the two live SUNAT procedures, the official WCO General Rules PDF, and Al-Hawamdeh's full journal article at Information Research. Their exact URLs are recorded in the Spanish section above and are language-independent identifiers.

### 3. Canonical manifest and future retrieval rule

The shared manifest above is the canonical 62-item access manifest for both language sections. `REF-001` through `REF-062` are stable internal retrieval identifiers; they complement rather than replace DOI, arXiv, official URL, or other stable bibliographic identifiers recorded in the frozen Phase-0B artifacts.

A `PASS` means only that the source can currently be retrieved and inspected. It does not authorize citation from memory. Every future use by the Writing AI must re-retrieve the relevant full text, verify source identity, locate the exact supporting passage, test claim strength and scope against that passage, and create the mandatory citation-anchored Word comment. Failure to retrieve the source in a future session triggers `ACCESS_RECHECK_REQUIRED`; prior audit status must never be used to simulate access.

### 4. Decision

```text
BIBLIOGRAPHIC_CORPUS_SIZE = 62
CANONICAL_ACCESS_MANIFEST = CREATED
CURRENT_FULLTEXT_ACCESS_CONFIRMED = 62/62
FILE_LIBRARY_FULLTEXT = 58
OFFICIAL_PRIMARY_WEB_FULLTEXT = 4
PDF_FORMAT_FULLTEXT = 59
AUTHORITATIVE_HTML_FULLTEXT = 3
INACCESSIBLE = 0
BIBLIOGRAPHIC_FULLTEXT_ACCESS_GATE = PASS
BIBLIOGRAPHIC_SCIENTIFIC_REASSESSMENT = NOT_PERFORMED
PHASE_0B = REMAINS_CLOSED_AND_FROZEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
PHASE_1 = BLOCKED_PENDING_AUTHOR_APPROVAL_AND_0D_FREEZE
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```
