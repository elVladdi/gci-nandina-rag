# Marco bibliográfico / Bibliographic Framework

## Español

### 1. Propósito

Este archivo define el marco bibliográfico controlado para el artículo científico principal. Su función es establecer qué literatura constituye el corpus inicial, cuándo puede incorporarse literatura adicional, cómo debe buscarse y validarse, y qué evidencia bibliográfica puede utilizarse durante la redacción.

No sustituye la lectura de los PDF ni autoriza por sí solo una cita. Toda referencia utilizada en el manuscrito debe haber sido verificada contra su fuente completa.

### 2. Corpus bibliográfico inicial

El corpus inicial del artículo estará formado por la literatura ya utilizada y documentada en:

1. el proyecto de investigación aprobado y su Anexo metodológico vigente;
2. la versión preliminar vigente de la tesis;
3. los PDF originales correspondientes a esas referencias, proporcionados por el autor.

Las referencias heredadas conservan su elegibilidad aunque tengan más de cinco años, pertenezcan a proceedings, tesis, documentos metodológicos, estándares o fuentes fundacionales. No deben eliminarse o reemplazarse únicamente por antigüedad. Su pertinencia para el artículo se evaluará durante la Fase 0B.

La tesis preliminar organiza actualmente los antecedentes y bases bibliográficas alrededor de, como mínimo, los siguientes ejes:

- clasificación arancelaria asistida por aprendizaje automático y modelos de lenguaje;
- clasificación arancelaria con LLM, RAG, agentes y evidencia documental;
- recuperación semántica e híbrida para códigos HS/NANDINA;
- explicabilidad, auditabilidad y soporte a la decisión aduanera;
- documentación de datos y conocimiento;
- gestión de información y conocimiento;
- conocimiento normativo arancelario y Sistema Armonizado;
- recuperación de información para ranking y evidencia documental;
- modelos de lenguaje, RAG y generación restringida por evidencia;
- procedencia, trazabilidad y reproducibilidad;
- evaluación del ranking, evidencia y explicación auditable.

### 3. Momento de carga de los PDF

Los PDF del corpus heredado no deben cargarse de manera indiscriminada al inicio.

El editor científico principal indicará el momento de carga cuando la Fase 0B esté lista para comenzar y emitirá una lista de referencias/PDF requeridos para el bloque de literatura que vaya a auditarse.

La carga se realizará por lotes temáticos para permitir lectura completa, trazabilidad y comparación entre trabajos.

Ninguna IA debe afirmar que ha revisado una referencia completa si solo ha visto una cita secundaria, un resumen, metadatos o un fragmento.

### 4. Estados bibliográficos

Cada referencia utilizada durante el proceso tendrá uno de los siguientes estados:

- `INHERITED_CORE`: referencia heredada del proyecto/tesis y pendiente o ya validada para el artículo.
- `CANDIDATE_NEW`: nueva referencia propuesta, todavía no autorizada.
- `APPROVED_NEW`: nueva referencia que cumplió los criterios de admisión y fue aprobada.
- `REVIEW_REQUIRED`: referencia cuya pertinencia, metadatos o contenido requieren revisión.
- `EXCLUDED`: referencia revisada pero no admisible para el artículo.
- `REPLACED`: referencia cuyo papel bibliográfico fue reemplazado mediante decisión explícita; no se elimina silenciosamente del registro histórico.

### 5. Regla para nuevas referencias académicas

Si durante la Fase 0B, la redacción, la revisión o la respuesta a revisores se detecta un vacío bibliográfico real, la IA de redacción podrá recibir instrucciones para buscar referencias nuevas.

Toda **nueva referencia académica** propuesta debe cumplir simultáneamente:

1. **Recencia:** publicada dentro de los últimos cinco años. Para el ciclo editorial 2026, la ventana operativa es 2022–2026 inclusive.
2. **Tipo de publicación:** artículo publicado en revista científica revisada por pares.
3. **Impacto:** revista de alto impacto. Se prioriza Q1; Q2 solo podrá aceptarse cuando el trabajo sea altamente específico y no exista una alternativa Q1 equivalente. No se incorporarán como nuevas referencias Q3/Q4, revistas no indexadas o editoriales de confiabilidad dudosa.
4. **Indexación verificable:** preferentemente Web of Science/JCR y/o Scopus/SJR/CiteScore.
5. **PDF completo disponible:** debe existir acceso al texto completo en PDF, por editorial, repositorio institucional, versión de autor u otra fuente legítima.
6. **Trazabilidad bibliográfica:** DOI u otro identificador estable y metadatos editoriales comprobables.
7. **Relevancia directa:** debe cubrir un gap, claim, método, benchmark, riesgo o comparación concreta del artículo. No se añadirán referencias solo para aumentar el número de citas.
8. **Verificación completa:** antes de citarla, debe leerse el PDF y comprobarse que respalda exactamente la afirmación para la que se propone.

Las nuevas tesis, proceedings, preprints, blogs, white papers o manuscritos no publicados no son admisibles como nuevas referencias académicas salvo autorización expresa del autor después de justificar por qué no existe una fuente de revista adecuada.

### 6. Fuentes normativas y oficiales

La regla de los últimos cinco años y de revista de alto impacto se aplica a **nueva literatura académica**.

Las fuentes normativas, regulatorias, estadísticas o institucionales primarias —por ejemplo, WCO/OMA, Comunidad Andina, SUNAT u otra autoridad competente— se gestionan como fuentes primarias oficiales, no como literatura académica. Para ellas rigen prioridad de autoridad, vigencia, versión, fecha y trazabilidad documental. Cualquier nueva fuente oficial debe identificarse separadamente y no utilizarse para sustituir evidencia científica cuando el claim requiera literatura académica.

### 7. Procedimiento de búsqueda para la IA de redacción

Cuando el editor autorice una búsqueda de literatura nueva, el prompt deberá definir el vacío exacto y prohibir búsquedas abiertas sin propósito.

La IA de redacción deberá devolver candidatos en una tabla que incluya como mínimo:

- autores;
- año;
- título;
- revista;
- DOI;
- indexación;
- cuartil/indicador de impacto y fuente del indicador;
- enlace legítimo al PDF completo;
- tipo de estudio;
- problema/tarea;
- dataset o corpus;
- método;
- resultado pertinente;
- limitación principal;
- claim o sección del artículo que podría respaldar;
- razón por la que la referencia heredada existente no es suficiente;
- recomendación `ADMIT / REJECT / REVIEW`.

La IA no podrá insertar directamente una referencia nueva en el manuscrito. Primero deberá ser revisada y pasar de `CANDIDATE_NEW` a `APPROVED_NEW`.

### 8. Regla contra referencias inventadas o incompletas

Está prohibido:

- inventar DOI, volumen, número, páginas, autores, año o revista;
- citar un trabajo a partir únicamente de snippets o resúmenes cuando el claim requiera el artículo completo;
- atribuir al paper una conclusión que procede de una fuente secundaria;
- confundir fecha de preprint con fecha de publicación final;
- utilizar métricas de impacto sin identificar de dónde provienen;
- citar una referencia nueva solo porque es reciente;
- reemplazar silenciosamente una fuente heredada por otra.

Cuando exista incertidumbre bibliográfica, se marcará `REVIEW_REQUIRED`.

### 9. Uso del corpus durante la Fase 0B

La Fase 0B no será una revisión narrativa basada en títulos. Cada trabajo deberá mapearse según el esquema definido en `ARTICLE_WRITING_PLAN.md`, incluyendo tarea exacta, nivel HS, datos, validación, retrieval/clasificación/generación, información normativa, explicabilidad, auditabilidad, dependencia de precedentes históricos, LLM, limitaciones y diferencia con el presente trabajo.

La finalidad es determinar qué problema resuelve realmente cada antecedente y qué espacio científico queda disponible. La existencia de un trabajo sobre “HS code prediction” no implica que resuelva el mismo problema que el artículo.

### 10. Regla de incorporación al manuscrito

Una referencia solo podrá utilizarse en el manuscrito cuando:

1. su PDF completo haya sido leído o auditado;
2. su función bibliográfica esté identificada;
3. la afirmación que respalda esté delimitada;
4. se hayan registrado sus límites de transferencia al contexto NANDINA;
5. no exista contradicción no resuelta con otra fuente relevante;
6. si es nueva, haya alcanzado estado `APPROVED_NEW`.

La selección final será más reducida que la bibliografía completa de la tesis. El artículo utilizará únicamente las referencias necesarias para sostener el problema, métodos, gap, comparaciones y discusión.

---

## English

### 1. Purpose

This file defines the controlled bibliographic framework for the main scientific article. Its purpose is to establish which literature forms the initial corpus, when additional literature may be incorporated, how it must be searched and validated, and which bibliographic evidence may be used during drafting.

It does not replace PDF reading and does not by itself authorize a citation. Every reference used in the manuscript must be verified against its full source.

### 2. Initial bibliographic corpus

The article's initial corpus will consist of the literature already used and documented in:

1. the approved research project and its current methodological Annex;
2. the current preliminary version of the thesis;
3. the original PDFs corresponding to those references, provided by the author.

Inherited references remain eligible even if they are more than five years old or are proceedings, theses, methodological documents, standards, or foundational sources. They must not be removed or replaced solely because of age. Their relevance to the article will be evaluated during Phase 0B.

The preliminary thesis currently organizes the literature and theoretical foundations around, at minimum, the following axes:

- tariff classification assisted by machine learning and language models;
- tariff classification with LLMs, RAG, agents, and documentary evidence;
- semantic and hybrid retrieval for HS/NANDINA codes;
- explainability, auditability, and customs decision support;
- data and knowledge documentation;
- information and knowledge management;
- tariff normative knowledge and the Harmonized System;
- information retrieval for ranking and documentary evidence;
- language models, RAG, and evidence-constrained generation;
- provenance, traceability, and reproducibility;
- evaluation of ranking, evidence, and auditable explanation.

### 3. Timing for PDF upload

The inherited-corpus PDFs must not be uploaded indiscriminately at the beginning.

The lead scientific editor will indicate when to upload them once Phase 0B is ready to start and will issue a list of the references/PDFs required for the literature block being audited.

Uploads will be organized in thematic batches to enable full reading, traceability, and comparison across studies.

No AI may claim to have reviewed a complete reference if it has only seen a secondary citation, abstract, metadata record, or excerpt.

### 4. Bibliographic statuses

Each reference used during the process will have one of the following statuses:

- `INHERITED_CORE`: reference inherited from the project/thesis and pending or already validated for the article.
- `CANDIDATE_NEW`: newly proposed reference, not yet authorized.
- `APPROVED_NEW`: new reference that met the admission criteria and was approved.
- `REVIEW_REQUIRED`: reference whose relevance, metadata, or content requires review.
- `EXCLUDED`: reviewed reference not admissible for the article.
- `REPLACED`: reference whose bibliographic role was replaced through an explicit decision; it is not silently removed from the historical record.

### 5. Rule for new academic references

If Phase 0B, drafting, review, or reviewer response reveals a genuine bibliographic gap, the drafting AI may be instructed to search for new references.

Every **new academic reference** proposed must simultaneously satisfy:

1. **Recency:** published within the last five years. For the 2026 editorial cycle, the operational window is 2022–2026 inclusive.
2. **Publication type:** peer-reviewed scientific journal article.
3. **Impact:** high-impact journal. Q1 is preferred; Q2 may only be accepted when the work is highly specific and no equivalent Q1 source is available. New Q3/Q4 references, non-indexed journals, or outlets of uncertain reliability will not be admitted.
4. **Verifiable indexing:** preferably Web of Science/JCR and/or Scopus/SJR/CiteScore.
5. **Full PDF available:** complete text must be accessible in PDF through the publisher, institutional repository, author version, or another legitimate source.
6. **Bibliographic traceability:** DOI or another stable identifier and verifiable publication metadata.
7. **Direct relevance:** it must cover a concrete gap, claim, method, benchmark, risk, or comparison in the article. References will not be added merely to increase citation count.
8. **Full verification:** before citation, the PDF must be read and checked to confirm that it supports exactly the statement for which it is proposed.

New theses, proceedings, preprints, blogs, white papers, or unpublished manuscripts are not admissible as new academic references unless the author explicitly approves them after a justification that no suitable journal source exists.

### 6. Normative and official sources

The five-year and high-impact-journal rule applies to **new academic literature**.

Primary normative, regulatory, statistical, or institutional sources — for example WCO, the Andean Community, SUNAT, or another competent authority — are managed as official primary sources rather than academic literature. For them, authority, validity, version, date, and documentary traceability take precedence. Any new official source must be identified separately and must not substitute scientific evidence when a claim requires academic literature.

### 7. Search procedure for the drafting AI

When the editor authorizes a search for new literature, the prompt must define the exact gap and prohibit open-ended searching without a specific purpose.

The drafting AI must return candidates in a table containing at minimum:

- authors;
- year;
- title;
- journal;
- DOI;
- indexing;
- quartile/impact indicator and the source of that indicator;
- legitimate link to the full PDF;
- study type;
- problem/task;
- dataset or corpus;
- method;
- relevant result;
- main limitation;
- article claim or section it could support;
- reason why the existing inherited reference is insufficient;
- `ADMIT / REJECT / REVIEW` recommendation.

The AI may not directly insert a new reference into the manuscript. It must first be reviewed and move from `CANDIDATE_NEW` to `APPROVED_NEW`.

### 8. Rule against invented or incomplete references

The following are prohibited:

- inventing DOI, volume, issue, pages, authors, year, or journal;
- citing a work based only on snippets or abstracts when the claim requires the full article;
- attributing to the paper a conclusion that comes from a secondary source;
- confusing a preprint date with the final publication date;
- using impact metrics without identifying their source;
- citing a new reference merely because it is recent;
- silently replacing an inherited source.

When bibliographic uncertainty exists, the reference must be marked `REVIEW_REQUIRED`.

### 9. Use of the corpus during Phase 0B

Phase 0B will not be a title-based narrative review. Each work must be mapped using the scheme defined in `ARTICLE_WRITING_PLAN.md`, including exact task, HS level, data, validation, retrieval/classification/generation, normative information, explainability, auditability, reliance on historical precedents, LLM use, limitations, and difference from the present work.

The purpose is to determine what problem each prior work actually solves and what scientific space remains available. The existence of a paper on “HS code prediction” does not imply that it solves the same problem as this article.

### 10. Rule for manuscript admission

A reference may only be used in the manuscript when:

1. its complete PDF has been read or audited;
2. its bibliographic function has been identified;
3. the supported statement has been delimited;
4. its transfer limitations to the NANDINA context have been recorded;
5. no unresolved contradiction exists with another relevant source;
6. if it is new, it has reached `APPROVED_NEW` status.

The final selection will be smaller than the thesis's full bibliography. The article will use only the references necessary to support the problem, methods, gap, comparisons, and discussion.
