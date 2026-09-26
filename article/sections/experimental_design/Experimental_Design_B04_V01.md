# Experimental Design B04 V01 — Section 4.5

```text
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
VERSION = V01
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
BASELINE_MASTER_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
SRC03_HEAD_READ = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_READ = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_READ = db0d0ad0d8435921a7838db6720eaea86a263763
AUTHORIZED_SCOPE = SECTION_4_5_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Part I — English manuscript text

### 4.5. Experimental system configuration and execution

The experimental query was the commercial-description field `DESCRIPCION DE MERCANCIAS CONCATENADA` from each evaluation SERIE. Historical retrieval tokenized this text deterministically by lowercasing it, applying Unicode NFKD decomposition, removing combining marks, and extracting alphanumeric tokens with the `[a-z0-9]+` pattern. The same procedure was applied to the 2,950 records in the H100 historical bank. No query rewriting, normative text, or language-model output was introduced before historical retrieval.

Historical candidates were produced with BM25 over H100 using k1 = 1.5 and b = 0.75. For each evaluation query, the implementation scored the historical records, considered the full H100 depth of 2,950 records, and retained up to 100 unique code candidates. Record-level results were ordered by decreasing BM25 score, with `case_id` as the deterministic tie-breaker. The ordered records were then traversed by NANDINA code: the first occurrence of a code created that code candidate, and the corresponding highest-ranked historical record was retained as its precedent. The first three unique codes formed the fixed Top-3 used by all downstream stages.

Documentary association followed the primary Phase-F contract after the Top-3 had been fixed. The historical Top-3 was the sole ranking source, and each candidate's eight-digit NANDINA code was used for direct lookup in the frozen hierarchical NANDINA corpus. The matched eight-digit record supplied exact candidate-level evidence, while section, chapter, heading, and six-digit parent information remained explicit hierarchical context. This path did not perform commercial-description retrieval over the normative corpus, score fusion, candidate-pool integration, fallback to another code, candidate insertion or substitution, reranking, or LLM-based selection. The historical precedent retained for each candidate was the record selected by the BM25 ranking before code deduplication.

For controlled explanation, the generation context was constructed only after the fixed Top-3 and candidate-specific evidence were available. Each context record contained the case identifier and commercial description together with the original candidate rank, NANDINA code, historical score, historical-precedent identifier and text, hierarchical code path, and candidate-linked normative evidence and provenance. The frozen generation inputs excluded the expected label and evaluation-only fields, did not load later reranking artifacts, and triggered no retrieval during generation. Context construction therefore packaged already selected candidates and evidence; it did not reopen candidate search.

The explanation stage used a local Ollama backend with `qwen2.5:7b-instruct` (7.6B parameters, Q4_K_M quantization, GGUF format). The frozen execution used Ollama 0.32.15, `num_ctx=8192`, `temperature=0`, JSON output, `stream=false`, and a 300-s request timeout; `top_p`, `top_k`, `seed`, and `num_predict` were left at backend-default or otherwise unspecified values. The prompt bound to the execution required exactly the received Top-3, prohibited adding, deleting, or reordering candidates, restricted the explanation to supplied historical and normative evidence, prohibited external knowledge and official-classification claims, and required strict JSON output. The LLM therefore generated an explanation of an upstream fixed ranking and had no authority to change or feed back into classification.

The frozen runtime records identify the historical-retrieval execution as Python 3.10.11 on Windows 10 and the Phase-F integration and local generation environment as Python 3.12.13 on Windows 11; the generation backend was local rather than a remote API. No CPU, GPU, or RAM minimum was frozen as an experimental requirement, so no hardware threshold is asserted here. These settings define the reported instantiation and its reproducible execution conditions; candidate-retrieval performance, documentary-association outcomes, and explanation quality are evaluated separately in the protocols that follow.

## Part II — Spanish semantic-control mirror

### 4.5. Configuración y ejecución experimental

La consulta experimental fue el campo de descripción comercial `DESCRIPCION DE MERCANCIAS CONCATENADA` de cada SERIE de evaluación. La recuperación histórica tokenizó este texto de manera determinista mediante conversión a minúsculas, descomposición Unicode NFKD, eliminación de marcas combinantes y extracción de tokens alfanuméricos con el patrón `[a-z0-9]+`. El mismo procedimiento se aplicó a los 2.950 registros del banco histórico H100. Antes de la recuperación histórica no se introdujeron reescritura de consulta, texto normativo ni salidas del modelo de lenguaje.

Los candidatos históricos se generaron con BM25 sobre H100 utilizando k1 = 1,5 y b = 0,75. Para cada consulta de evaluación, la implementación puntuó los registros históricos, consideró la profundidad completa de H100 de 2.950 registros y retuvo hasta 100 candidatos de código únicos. Los resultados a nivel de registro se ordenaron por puntuación BM25 decreciente, usando `case_id` como criterio determinista de desempate. Después se recorrieron los registros ordenados por código NANDINA: la primera aparición de un código creaba ese candidato y el registro histórico mejor posicionado correspondiente se conservaba como su precedente. Los tres primeros códigos únicos formaron el Top-3 fijo utilizado por todas las etapas posteriores.

La asociación documental siguió el contrato primario de la Fase F después de fijar el Top-3. El Top-3 histórico fue la única fuente de ranking y el código NANDINA de ocho dígitos de cada candidato se utilizó para una consulta directa en el corpus NANDINA jerárquico congelado. El registro coincidente de ocho dígitos aportó la evidencia exacta a nivel de candidato, mientras que la información de sección, capítulo, partida y subpartida de seis dígitos permaneció como contexto jerárquico explícito. Esta ruta no realizó recuperación sobre el corpus normativo a partir de la descripción comercial, fusión de puntuaciones, integración de pools de candidatos, fallback a otro código, inserción o sustitución de candidatos, reranking ni selección mediante LLM. El precedente histórico conservado para cada candidato fue el registro seleccionado por el ranking BM25 antes de la deduplicación por código.

Para la explicación controlada, el contexto de generación se construyó únicamente después de disponer del Top-3 fijo y de la evidencia específica por candidato. Cada registro de contexto incluyó el identificador del caso y la descripción comercial, junto con el rank original del candidato, código NANDINA, puntuación histórica, identificador y texto del precedente histórico, ruta jerárquica del código y evidencia normativa vinculada al candidato con su procedencia. Las entradas de generación congeladas excluyeron la etiqueta esperada y los campos de uso exclusivo de evaluación, no cargaron artefactos posteriores de reranking y no activaron recuperación durante la generación. Por tanto, la construcción del contexto empaquetó candidatos y evidencia ya seleccionados; no reabrió la búsqueda de candidatos.

La etapa de explicación utilizó un backend Ollama local con `qwen2.5:7b-instruct` (7,6B parámetros, cuantización Q4_K_M y formato GGUF). La ejecución congelada utilizó Ollama 0.32.15, `num_ctx=8192`, `temperature=0`, salida JSON, `stream=false` y timeout de 300 s por solicitud; `top_p`, `top_k`, `seed` y `num_predict` quedaron con valores predeterminados del backend o sin especificación explícita. El prompt vinculado a la ejecución exigía conservar exactamente el Top-3 recibido, prohibía agregar, eliminar o reordenar candidatos, restringía la explicación a la evidencia histórica y normativa suministrada, prohibía conocimiento externo y afirmaciones de clasificación oficial y exigía salida JSON estricta. En consecuencia, el LLM generó una explicación de un ranking fijado aguas arriba y no tuvo autoridad para modificarlo ni retroalimentar la clasificación.

Los registros de runtime congelados identifican la ejecución de recuperación histórica con Python 3.10.11 sobre Windows 10 y la integración de Fase F y el entorno de generación local con Python 3.12.13 sobre Windows 11; el backend de generación fue local y no una API remota. No se congeló un mínimo de CPU, GPU o RAM como requisito experimental, por lo que aquí no se establece ningún umbral de hardware. Estas configuraciones definen la instanciación reportada y sus condiciones reproducibles de ejecución; el desempeño de recuperación de candidatos, los resultados de asociación documental y la calidad de las explicaciones se evalúan por separado en los protocolos posteriores.
