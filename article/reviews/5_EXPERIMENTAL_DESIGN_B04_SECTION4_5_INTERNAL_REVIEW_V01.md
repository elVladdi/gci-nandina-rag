# Revisión interna — Experimental Design B04 / Section 4.5 — V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
REVIEW_VERSION = V01
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
DRAFTING_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_RESPONSE_V01.md@b2774bc44fb5d8ece0b3d505b8d875974211445d
SECTION = article/sections/experimental_design/Experimental_Design_B04_V01.md@ade9d022663458d7bbe5aee939e1d7899365a7c8
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
B04_MASTER_CANDIDATE_MD_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
B04_MASTER_CANDIDATE_MD_GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
B04_MASTER_CANDIDATE_DOCX_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
SCIENTIFIC_SCOPE = PASS
CLAIM_EVIDENCE_AUDIT = CORRECTION_REQUIRED / TWO_NARROW_PRECISION_ITEMS
DIFFERENTIAL_MD_AUDIT = PASS
BILINGUAL_EQUIVALENCE = PASS
SCOPE_CONTROL = PASS
DOCX_CONTINUITY = PASS
DOCX_OOXML = PASS
CITATION_COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
MASTER_CANDIDATE_GLOBAL_STATUS = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_CORRECTION_VERIFIED
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

### 1. Alcance de la auditoría independiente

La IA Gestora auditó la entrega B04 independientemente de los `PASS` declarados por la IA de Redacción. Se verificaron la prosa inglesa y el espejo español, la identidad de los dos masters candidatos entregados por el autor, la integridad OOXML, comentarios/anclajes, tracked changes, el diferencial acumulativo contra V012 y los claims metodológicos contra fuentes experimentales primarias del estado congelado consumido por B04.

No se detectó drift material de SRC-03/main para los hechos consumidos por 4.5. No aparece un trigger que requiera revisión de IA Experimental: las dos observaciones siguientes corrigen precisión de redacción frente a evidencia ya congelada; no cambian diseño, resultados, inferencias, arquitectura ni estado experimental.

### 2. Contenido validado

La sección representa correctamente, dentro de Methods, los siguientes hechos y límites:

- consulta desde `DESCRIPCION DE MERCANCIAS CONCATENADA` y tokenización determinista mediante minúsculas, NFKD, eliminación de marcas combinantes y patrón `[a-z0-9]+`;
- banco H100 de 2,950 registros, BM25 con `k1=1.5` y `b=0.75`, `history_depth=2950`, `candidate_depth=100`, orden por score decreciente con `case_id` como desempate y deduplicación por NANDINA;
- fixed Top-3 formado por los tres primeros códigos únicos y fijado antes de las etapas documental y generativa;
- Phase F con Top-3 histórico como única fuente de ranking, lookup directo NANDINA-8, ausencia de reranking, score fusion, candidate-pool integration, candidate insertion/substitution y LLM selection;
- construcción del contexto después de fijar Top-3, sin expected label/evaluation-only fields, sin Phase-G/reranking cargado y sin retrieval durante generación;
- Ollama local, `qwen2.5:7b-instruct`, 7.6B, Q4_K_M, GGUF, Ollama 0.32.15, `num_ctx=8192`, `temperature=0`, JSON, `stream=false`, timeout 300 s, con `top_p`, `top_k`, `seed` y `num_predict` backend-default/unspecified;
- restricciones del prompt que impiden agregar, eliminar o reordenar candidatos, usar conocimiento externo o emitir clasificación oficial;
- separación de decisiones de configuración respecto de resultados posteriores y ausencia de métricas observadas de desempeño en 4.5.

### 3. Correcciones estrechas obligatorias

#### B04-C01 — precisión sobre `history_depth=2950`

Texto actual EN:

```text
For each evaluation query, the implementation scored the historical records, considered the full H100 depth of 2,950 records, and retained up to 100 unique code candidates.
```

Problema: la implementación construye el índice sobre los 2,950 registros de H100 y configura `history_depth=2950`, pero `_bm25_scores` solo crea entradas de score para documentos que contienen al menos un término de la consulta. `_dedup_candidates` ordena `scores.items()` y aplica el límite `history_depth`; no materializa ni ordena explícitamente documentos de score cero ausentes del diccionario. La redacción actual puede leerse como si cada consulta hubiera producido un ranking explícito de los 2,950 registros.

Reemplazo autorizado EN:

```text
For each evaluation query, the implementation scored the historical matches using the 2,950-record H100 bank, set the historical ranking depth to 2,950, and retained up to 100 unique code candidates.
```

Texto actual ES:

```text
Para cada consulta de evaluación, la implementación puntuó los registros históricos, consideró la profundidad completa de H100 de 2.950 registros y retuvo hasta 100 candidatos de código únicos.
```

Reemplazo autorizado ES:

```text
Para cada consulta de evaluación, la implementación puntuó las coincidencias históricas usando el banco H100 de 2.950 registros, fijó la profundidad del ranking histórico en 2.950 y retuvo hasta 100 candidatos de código únicos.
```

Esta corrección no cambia el experimento ni sus parámetros; evita atribuir a la implementación una materialización de documentos con score cero que el código no demuestra.

#### B04-C02 — separar regla metodológica de outcome de cobertura exacta

Texto actual EN:

```text
The matched eight-digit record supplied exact candidate-level evidence, while section, chapter, heading, and six-digit parent information remained explicit hierarchical context.
```

Problema: formulada sin condición, la oración puede interpretarse como afirmación de que todo candidate slot obtuvo un match exacto. La cobertura exacta observada es un outcome de Phase F y pertenece a Results. Methods debe describir la regla de asociación sin anticipar ese outcome.

Reemplazo autorizado EN:

```text
When an exact eight-digit match was available, that record supplied candidate-level evidence, while section, chapter, heading, and six-digit parent information remained explicit hierarchical context.
```

Texto actual ES:

```text
El registro coincidente de ocho dígitos aportó la evidencia exacta a nivel de candidato, mientras que la información de sección, capítulo, partida y subpartida de seis dígitos permaneció como contexto jerárquico explícito.
```

Reemplazo autorizado ES:

```text
Cuando existía una coincidencia exacta de ocho dígitos, ese registro aportaba evidencia a nivel de candidato, mientras que la información de sección, capítulo, partida y subpartida de seis dígitos permanecía como contexto jerárquico explícito.
```

El párrafo ya conserva `fallback = none`; por tanto, esta formulación expresa la regla metodológica sin revelar la tasa observada de cobertura exacta.

### 4. Auditoría de masters candidatos

El archivo Markdown entregado por el autor fue verificado directamente:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
GIT_BLOB = 7dbee2c05896e3c45df9cd17518342f1e6446676
```

La reconstrucción diferencial de V012 sustituyendo únicamente los bloques EN/ES de 4.5 por los placeholders canónicos reproduce exactamente:

```text
V012_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
V012_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
```

Por tanto, el diferencial Markdown fuera de 4.5 es `PASS`.

El DOCX candidato entregado por el autor fue verificado directamente:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx
SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = 14/14 PASS
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603
TRACKED_CHANGES = 0
SECTION_4_5_EN_ES = PRESENT
SECTION_4_6_BOUNDARY_EN_ES = PRESENT
```

La continuidad DOCX pasa; las correcciones autorizadas deben realizarse sobre este B04 V01 exacto, no sobre B03 ni mediante reconstrucción desde Markdown.

### 5. Dictamen

El alcance científico, la arquitectura, las fuentes, la separación Methods/Results, la equivalencia bilingüe y la continuidad acumulativa son correctos. No se autoriza una reescritura de 4.5.

El candidato global queda `CORRECTION_REQUIRED` únicamente por B04-C01 y B04-C02. Tras una corrección diferencial exacta, la IA Gestora debe verificar V02 antes de abrir el gate de aprobación autoral.

```text
AUTHORIZED_CORRECTION_COUNT = 2 ITEMS / 4 LITERAL EN-ES REPLACEMENTS
SCIENTIFIC_REWRITE = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_CORRECTION_VERIFIED
B05 = NOT_AUTHORIZED
```

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
REVIEW_VERSION = V01
SCIENTIFIC_SCOPE = PASS
CLAIM_EVIDENCE_AUDIT = CORRECTION_REQUIRED / TWO_NARROW_PRECISION_ITEMS
DIFFERENTIAL_MD_AUDIT = PASS
BILINGUAL_EQUIVALENCE = PASS
SCOPE_CONTROL = PASS
DOCX_CONTINUITY = PASS
DOCX_OOXML = PASS
CITATION_COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
MASTER_CANDIDATE_GLOBAL_STATUS = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = SUSPENDED_UNTIL_CORRECTION_VERIFIED
B05 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

The Managing AI independently audited B04 rather than adopting the Drafting AI's declared `PASS` values. Section 4.5 correctly instantiates the frozen architecture and is supported by the primary historical-retrieval, Phase-F integration, context-construction, model-manifest, and prompt artifacts. It also correctly avoids performance metrics and downstream outcomes.

Two narrow wording corrections are required before author approval. B04-C01 replaces language that can imply that all 2,950 historical records were explicitly ranked for each query; the implementation indexes the 2,950-record bank and sets `history_depth=2950`, while the score dictionary contains matched documents. B04-C02 makes exact documentary matching conditional so Methods describes the lookup rule without implicitly reporting the observed exact-evidence coverage outcome.

No other scientific rewriting is authorized. The Markdown differential against V012 passes exactly. The candidate DOCX also passes package integrity, XML/RELS parsing, 40/40 comment-anchor preservation, zero tracked changes, and Section-4.5/4.6 boundary checks. The correction must start from the exact B04 V01 candidate masters and produce B04 V02 for differential re-audit.