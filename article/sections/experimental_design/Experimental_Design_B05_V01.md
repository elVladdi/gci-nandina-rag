# Experimental Design B05 V01 — Section 4.6

```text
BLOCK = EXPERIMENTAL_DESIGN_B05_SECTION_4_6
VERSION = V01
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99
GOVERNING_DECISION = D-068
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MASTER_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
BASELINE_MASTER_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
BASELINE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
SRC03_HEAD_READ = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_READ = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_READ = db0d0ad0d8435921a7838db6720eaea86a263763
AUTHORIZED_SCOPE = SECTION_4_6_AND_4_6_1_TO_4_6_3_ONLY
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Part I — English manuscript text

## 4.6. Evaluation framework and protocols

Section 4.6 evaluates the three outputs that correspond to RQ1–RQ3 as separate objects rather than collapsing them into a single system score. RQ1 concerns the historical candidate ranking, RQ2 concerns documentary evidence associated with the already fixed Top-3, and RQ3 concerns the structure and traceability of the controlled explanation produced from those fixed candidates and their evidence. For each function, the protocol specifies its output, evaluation unit, criterion, and permitted interpretation. RQ4 remains a validity and robustness boundary: partition/dependence controls are described in Section 4.4 and the inferential and robustness procedures are reserved for Section 4.7. The protocols below define how each function was evaluated; observed values are reported only in Results.

### 4.6.1. Candidate-retrieval evaluation

The primary unit for candidate-retrieval evaluation was the SERIE. For each evaluation series, the reference eight-digit NANDINA code was compared with the ordered candidate codes returned by a retrieval method. Early-ranking performance was defined by Top-1, Top-3, Top-5, and Top-10 indicators and by MRR@100; Top-50 was retained as a supplementary metric. A Top-k indicator records whether the reference code occurs within the first k positions. MRR@100 assigns the reciprocal of the reference-code rank when it occurs within the first 100 positions and zero otherwise. These quantities measure the presence and position of the reference code in a candidate ranking, not overall system or legal-classification accuracy.

RQ1 compared the historical ranking with the corrected comparable retrieval families frozen by the analytical contract: flat normative BM25, hierarchical normative BM25, and the Text2Trade-inspired MNRL family (D1a). The same evaluation cases and reference labels define the scoring object across these families, but the normative and D1a families are comparators only; they do not become candidate sources in the primary framework path described in Sections 3 and 4.5. Inferential treatment of paired differences and DAM-level dependence is specified separately in Section 4.7.

Deep coverage was evaluated separately from early ranking. Under the frozen HE2_B protocol, the corrected hierarchical family was characterized with exact-code Recall@100 and Recall@200/Pool@200. The Phase-E candidate-pool variants were treated as descriptive coverage inventories at Pool@50, Pool@100, and Pool@200 rather than as alternative rankings. This separation prevents a deeper candidate inventory from being interpreted as evidence about the quality of the framework's fixed historical ranking.

### 4.6.2. Documentary-evidence evaluation

RQ2 was evaluated after the historical Top-3 had been fixed. The primary unit was the candidate slot, with case-level summaries used when the three slots of a case had to be considered jointly. Exact documentary evidence was defined by availability of a direct eight-digit NANDINA association for that candidate. Hierarchical HS6, HS4, and chapter information was tracked separately as parent context and was not promoted to exact candidate evidence.

The protocol also checked whether each candidate retained its historical precedent, whether the candidate, precedent, and documentary record remained traceable to one another, and whether documentary association preserved the composition and order of the upstream Top-3. The evaluation label was excluded from candidate, precedent, evidence, ordering, and fallback decisions and was used only after construction when a metric required a reference label. Accordingly, this protocol measures documentary coverage, association, traceability, and ranking invariance; it does not establish substantive normative correctness or legal correctness. Observed coverage and invariance rates are reserved for Results.

### 4.6.3. Controlled-explanation evaluation

RQ3 used two complementary evaluation layers. The automatic layer checked structural and traceability constraints in the generated artifact: preservation of the three candidate codes and their order, absence of missing, duplicated, or external codes, rank consistency, validity of cited historical and normative references, candidate-to-evidence traceability, presence of the required comparison and warning structure, JSON parsing/structure, and absence of explicit reference-label leakage. The frozen schema did not define a pre-generation per-case `automatic_validation_pass` rule, so no retrospective binary pass label was introduced for this layer.

The qualitative layer applied a frozen eight-dimension rubric, with each dimension scored from 0 to 2: traceability, verifiability, separation of historical and normative evidence, prudence of the conclusion, consistency with the fixed Top-3, detection of generic normative evidence, comparison among candidates, and utility for human audit. A case met the protocol's auditable-case criterion when the total was at least 12/16 and no hard violation was present. Hard violations covered changing the Top-3 or its order, introducing a code outside `top3_original`, issuing an official or categorical claim of a definitely correct code, failing to frame the conclusion as documentary support for expert review, or violating the strict-JSON requirement of the technical artifact. The `advertencias_globales` field was excluded from scoring because the frozen prompt and schema did not align on that field.

Qualitative scoring used a deterministic 50-case sample stratified by support bucket, support count, exact reference rank, and `case_id`, with seed 2026. The fixed composition was 10 difficult/low-support cases, 15 rank-1 cases, 15 rank-2–3 cases, and 10 rank-4–10 cases. Ground truth, reference rank, and sample bucket were hidden from the evaluator, and neither external evidence nor web information was used.

The pre-scoring protocol originally specified human/manual review, but the executed qualitative assessment used an independent AI evaluator in an expert role (LLM-as-judge); human scoring was not performed. This evaluator-modality deviation is therefore part of the protocol's interpretation boundary. The qualitative scores characterize conformity with the frozen rubric under that AI-evaluator setting and support analysis of structure, traceability, verifiability, and auditability. They do not constitute human expert validation, legal correctness, an official classification decision, or a faithful causal reconstruction of why the upstream ranking was produced.

## Part II — Spanish semantic-control mirror

## 4.6. Marco y protocolos de evaluación

La Sección 4.6 evalúa como objetos separados las tres salidas correspondientes a RQ1–RQ3, en lugar de condensarlas en una única puntuación del sistema. RQ1 se refiere al ranking histórico de candidatos, RQ2 a la evidencia documental asociada con el Top-3 ya fijado y RQ3 a la estructura y trazabilidad de la explicación controlada producida a partir de esos candidatos fijos y su evidencia. Para cada función, el protocolo especifica su salida, unidad de evaluación, criterio e interpretación permitida. RQ4 permanece como una frontera de validez y robustez: los controles de partición/dependencia se describen en la Sección 4.4 y los procedimientos inferenciales y de robustez se reservan para la Sección 4.7. Los protocolos siguientes definen cómo se evaluó cada función; los valores observados se reportan únicamente en Resultados.

### 4.6.1. Evaluación de recuperación de candidatos

La unidad primaria para evaluar la recuperación de candidatos fue la SERIE. Para cada serie de evaluación, el código NANDINA de ocho dígitos de referencia se comparó con los códigos candidatos ordenados devueltos por un método de recuperación. El desempeño en posiciones tempranas se definió mediante indicadores Top-1, Top-3, Top-5 y Top-10 y mediante MRR@100; Top-50 se conservó como métrica suplementaria. Un indicador Top-k registra si el código de referencia aparece dentro de las primeras k posiciones. MRR@100 asigna el recíproco del rank del código de referencia cuando este aparece dentro de las primeras 100 posiciones y cero en caso contrario. Estas cantidades miden la presencia y posición del código de referencia en un ranking de candidatos, no la accuracy global del sistema ni la corrección jurídica de la clasificación.

RQ1 comparó el ranking histórico con las familias de recuperación comparables corregidas y congeladas por el contrato analítico: BM25 normativo plano, BM25 normativo jerárquico y la familia MNRL inspirada en Text2Trade (D1a). Los mismos casos de evaluación y etiquetas de referencia definen el objeto de puntuación entre estas familias, pero las familias normativa y D1a son únicamente comparadores; no pasan a ser fuentes de candidatos en la ruta primaria del framework descrita en las Secciones 3 y 4.5. El tratamiento inferencial de las diferencias pareadas y de la dependencia a nivel de DAM se especifica por separado en la Sección 4.7.

La cobertura profunda se evaluó por separado del ranking temprano. Bajo el protocolo HE2_B congelado, la familia jerárquica corregida se caracterizó mediante Recall@100 de código exacto y Recall@200/Pool@200. Las variantes de pools de candidatos de la Fase E se trataron como inventarios descriptivos de cobertura en Pool@50, Pool@100 y Pool@200, y no como rankings alternativos. Esta separación evita interpretar un inventario de candidatos más profundo como evidencia sobre la calidad del ranking histórico fijo del framework.

### 4.6.2. Evaluación de evidencia documental

RQ2 se evaluó después de fijar el Top-3 histórico. La unidad primaria fue el slot de candidato, con resúmenes a nivel de caso cuando era necesario considerar conjuntamente los tres slots de un caso. La evidencia documental exacta se definió por la disponibilidad de una asociación directa NANDINA de ocho dígitos para ese candidato. La información jerárquica HS6, HS4 y de capítulo se registró por separado como contexto parental y no se promovió a evidencia exacta del candidato.

El protocolo también comprobó si cada candidato conservaba su precedente histórico, si candidato, precedente y registro documental permanecían trazables entre sí y si la asociación documental preservaba la composición y el orden del Top-3 upstream. La etiqueta de evaluación se excluyó de las decisiones de candidatos, precedentes, evidencia, orden y fallback y se utilizó solo después de la construcción cuando una métrica requería una etiqueta de referencia. En consecuencia, este protocolo mide cobertura, asociación y trazabilidad documental, además de invariancia del ranking; no establece corrección normativa sustantiva ni corrección jurídica. Las tasas observadas de cobertura e invariancia se reservan para Resultados.

### 4.6.3. Evaluación de explicación controlada

RQ3 utilizó dos capas de evaluación complementarias. La capa automática verificó restricciones estructurales y de trazabilidad del artefacto generado: preservación de los tres códigos candidatos y su orden, ausencia de códigos faltantes, duplicados o externos, consistencia de rank, validez de las referencias históricas y normativas citadas, trazabilidad candidato–evidencia, presencia de la estructura requerida de comparación y advertencias, parseo/estructura JSON y ausencia de leakage explícito de la etiqueta de referencia. El esquema congelado no definió una regla pre-generación de `automatic_validation_pass` por caso, por lo que no se introdujo retrospectivamente una etiqueta binaria de aprobación para esta capa.

La capa cualitativa aplicó una rúbrica congelada de ocho dimensiones, cada una puntuada de 0 a 2: trazabilidad, verificabilidad, separación de evidencia histórica y normativa, prudencia de la conclusión, consistencia con el Top-3 fijo, detección de evidencia normativa genérica, comparación entre candidatos y utilidad para auditoría humana. Un caso cumplía el criterio protocolario de ficha auditable cuando el total era al menos 12/16 y no existía hard violation. Las hard violations comprendían cambiar el Top-3 o su orden, introducir un código fuera de `top3_original`, emitir una clasificación oficial o una afirmación categórica de código definitivamente correcto, no formular la conclusión como apoyo documental para revisión experta o incumplir el requisito de JSON estricto del artefacto técnico. El campo `advertencias_globales` se excluyó del scoring porque el prompt y el esquema congelados no estaban alineados respecto de ese campo.

La puntuación cualitativa utilizó una muestra determinista de 50 casos estratificada por bucket de soporte, conteo de soporte, rank exacto de referencia y `case_id`, con seed 2026. La composición fijada fue de 10 casos difíciles/de bajo soporte, 15 casos de rank 1, 15 casos de rank 2–3 y 10 casos de rank 4–10. El ground truth, el rank de referencia y el bucket de la muestra se ocultaron al evaluador, y no se utilizaron evidencia externa ni información web.

El protocolo previo al scoring había especificado originalmente revisión humana/manual, pero la evaluación cualitativa ejecutada utilizó un evaluador de IA independiente en rol experto (LLM-as-judge); no se realizó puntuación humana. Esta desviación de modalidad del evaluador forma parte, por tanto, del límite de interpretación del protocolo. Las puntuaciones cualitativas caracterizan la conformidad con la rúbrica congelada bajo ese esquema de evaluación por IA y sustentan el análisis de estructura, trazabilidad, verificabilidad y auditabilidad. No constituyen validación por expertos humanos, corrección jurídica, una decisión oficial de clasificación ni una reconstrucción causal fiel de por qué se produjo el ranking upstream.
