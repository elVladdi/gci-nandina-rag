# Manifiesto de artefactos v0.1

Este documento resume la politica de datos, artefactos, checksums y Git/no Git del protocolo experimental v0.1. El detalle machine-readable esta en `docs/manifest_artifacts_v0.1.json`.

## Insumos oficiales de v0.1

Los insumos oficiales son los archivos necesarios para sostener el piloto offline y reconstruir el baseline BM25:

- `src/configs/experiment_v0.1.json`: snapshot metodologico oficial.
- `src/configs/experiment_config.json`: configuracion operativa usada por scripts.
- `data/raw/Arancel 2022.pdf`: fuente local del corpus arancelario.
- `data/raw/CAN Desición 885 - Nanadina Gaceta 4359.pdf`: fuente local NANDINA/CAN.
- `data/processed/corpus_rag_v1.jsonl`: corpus curado base.
- `data/processed/corpus_rag_v1_index.jsonl`: corpus indexable oficial.
- `data/processed/devset_validacion_intermedia.csv`: devset piloto actual.
- `data/processed/indexes/bm25_nandina8_run_metadata.json`: metadatos del indice BM25.

El indice `data/processed/indexes/bm25_nandina8.pkl` se considera artefacto de aceleracion. Esta disponible localmente y ya esta versionado, pero metodologicamente puede regenerarse desde el corpus indexable y los parametros BM25 congelados.



## Fuente operativa data_aduanas

La Fase 2 incorpora `data_aduanas` como fuente operativa normalizada y la Fase 3 actualizada la usa para construir particiones experimentales de `Clase = 87`. La fuente local fisica es `data/Series - Descripciones.xlsx`, procesada por `src/ingestion/sunat_series_parser.py`; el nombre metodologico de la fuente es `data_aduanas`.

Se documentan como trazabilidad versionable:

- `src/ingestion/sunat_series_parser.py`: parser de ingesta.
- `docs/protocolo_ingesta_sunat_series_v0.1.md`: protocolo de ingesta asociado, si se versiona junto con Fase 2.
- `src/evaluation/build_data_aduanas_splits.py`: constructor reproducible de particiones `data_aduanas` clase 87.
- `docs/protocolo_data_aduanas_clase87_v0.1.md`: protocolo de Fase 3 actualizada.
- `docs/ficha_data_aduanas_clase87_v0.1.md`: ficha de las particiones clase 87.
- `docs/politica_curacion_data_aduanas_clase87_v0.1.md`: politica de curacion y duplicados `id_unico`.
- `data/processed/data_aduanas_historico_clase87_v0.1.csv`: historico congelado, 3,000 filas.
- `data/processed/data_aduanas_devset_clase87_v0.1.csv`: desarrollo congelado, 100 filas.
- `data/processed/data_aduanas_evalset_clase87_v0.1.csv`: evaluacion congelada, 1,006 filas.
- `data/processed/data_aduanas_splits_clase87_v0.1_metadata.json`: metadata de generacion, curacion, checksums y validacion.

Se documentan como fuente local y artefactos regenerables/locales:

- `data/Series - Descripciones.xlsx`: fuente local `data_aduanas`; politica `local_only` y `external_reference`, sin forzar versionado Git.
- `data/interim/sunat_series_descripciones_normalized.csv`: capa normalizada intermedia, `ignored`, `local_only` y `regenerable`.
- `data/interim/sunat_series_descripciones_normalized.xlsx`: exportacion intermedia opcional, `ignored`, `local_only` y `regenerable`.
- `data/interim/sunat_series_descripciones_normalized_metadata.json`: metadata de normalizacion, `ignored`, `local_only` y `regenerable`.
- `outputs/audits/sunat_series_labels_v0.1/labels.csv`: auditoria de etiquetas, `ignored`, `local_only` y `regenerable`.
- `outputs/audits/sunat_series_labels_v0.1/id_unico_duplicates.csv`: auditoria de duplicados `id_unico`, `ignored`, `local_only` y `regenerable`.
- `outputs/audits/data_aduanas_splits_clase87_v0.1/`: auditorias regenerables de curacion, duplicados y distribucion por split, `ignored`, `local_only` y `regenerable`.

La normalizacion disponible registra 107 DAM detectadas, 11,320 series normalizadas, 11,320 filas con `id_unico` y 81 filas con advertencias de parseo. El alcance operativo de las particiones finales es `Clase = 87`: 4,232 instancias fuente, 69 NANDINAS distintas, 4,106 filas curadas finales, 126 filas excluidas por duplicados `id_unico`, sin exclusiones por campos obligatorios o calidad. Historico, desarrollo y evaluacion conservan las mismas columnas y no contienen `id_unico` repetidos ni solapados.

Esta incorporacion actualiza la Fase 3: el evalset v0.1 de 600 casos se conserva como artefacto historico/versionado, pero las particiones `data_aduanas` clase 87 pasan a ser la base metodologica para fases futuras una vez validadas.

## Evalset final v0.1

El evalset final v0.1 fue generado desde una fuente aduanera previa en modo `sunat-block` y congelado en `data/processed/evalset_v0.1.csv` con 600 casos unicos validos. Antes de congelarlo se auditaron 647 casos extraidos, 31 grupos duplicados exactos y 47 filas excedentes por la llave `descripcion + nandina_ref + regimen`.

La metadata asociada queda en `data/processed/evalset_v0.1_metadata.json` y registra fuente, fecha de consulta, formato de extraccion, regla de deduplicacion, conteos de calidad y checksums. Estos artefactos sostienen la evaluacion final posterior, pero no constituyen por si mismos resultados experimentales ni validacion de hipotesis. El alcance empirico queda concentrado en regimen `10` (importacion para el consumo), por lo que los resultados no deben generalizarse a otros regimenes aduaneros.

## Resultados preliminares

Las corridas `data/processed/runs/bm25_2pass_llm_*` con archivos existentes son resultados preliminares de BM25 + LLM rewrite. Sirven para inspeccion o comparacion exploratoria, pero no son validacion final.

El manifiesto incluye las corridas no vacias:

- `bm25_2pass_llm_20260117_135306`.
- `bm25_2pass_llm_20260117_145435`.
- `bm25_2pass_llm_20260117_160632`.
- `bm25_2pass_llm_20260117_162840`.
- `bm25_2pass_llm_20260117_175226`.
- `bm25_2pass_llm_20260117_182635`.
- `bm25_2pass_llm_20260117_185139`.

Los directorios vacios se registran como omitidos en el manifiesto JSON y no deben usarse como evidencia de resultados.

## Artefactos exploratorios

Text2Trade/dense retrieval queda como artefacto exploratorio o componente candidato, no como componente formal del protocolo v0.1.

Se documentan como trazabilidad:

- `data/processed/indexes/text2trade_nandina8_v1/retrieval_config.json`.
- `data/processed/indexes/text2trade_nandina8_v1/text2trade_nandina8_run_metadata.json`.

Se documentan como artefactos locales o regenerables:

- `data/processed/indexes/text2trade_nandina8_v1/index/vectors.npy`.
- `data/processed/indexes/text2trade_nandina8_v1/index/id_map.json`.
- `data/processed/indexes/text2trade_nandina8_v1/store/nandina8_docstore.jsonl`.
- `data/processed/indexes/text2trade_nandina8_v1/model/model.safetensors`.
- `data/processed/indexes/text2trade_nandina8_v1/eval/smoke_test_results.json`.

Estos ultimos no deben subirse a Git por peso, regenerabilidad o dependencia de modelos locales.

## Evaluacion BM25 baseline v0.1

La Fase 4 formaliza la evaluacion reproducible del baseline BM25 puro sobre `data/processed/evalset_v0.1.csv`.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_bm25.py`: ejecuta BM25 puro sobre el evalset final y genera resultados por caso y metricas agregadas.
- `src/analysis/diagnose_bm25_baseline.py`: analiza cobertura, fallos y desempeno jerarquico NANDINA8/HS4/HS2 a partir del evalset, indice y resultados BM25.
- `src/analysis/__init__.py`: declara el paquete de scripts de analisis.
- `docs/evaluacion_bm25_baseline_v0.1.md`: cierre metodologico de la evaluacion BM25 baseline v0.1.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/bm25_eval_v0.1/results.csv`.
- `outputs/evaluation/bm25_eval_v0.1/metrics.json`.
- `outputs/evaluation/bm25_eval_v0.1/summary.md`.
- `outputs/evaluation/bm25_eval_v0.1/diagnostics.json`.
- `outputs/evaluation/bm25_eval_v0.1/diagnostics.md`.
- `outputs/evaluation/bm25_eval_v0.1/failure_sample.csv`.

Estos outputs no se fuerzan al repositorio porque pueden regenerarse desde los scripts versionados, el evalset final, el indice BM25 y la configuracion operativa.

### Actualizacion BM25 data_aduanas clase 87 v0.1

La actualizacion de Fase 4 evalua el baseline BM25 normativo plano sobre `data/processed/data_aduanas_evalset_clase87_v0.1.csv`, usando `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta esperada. La corrida no ejecuta LLM ni Text2Trade y no modifica el evalset historico v0.1 ni los splits `data_aduanas` de Fase 3.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_bm25_data_aduanas.py`: evalua el indice normativo `data/processed/indexes/bm25_nandina8.pkl` sobre el evalset `data_aduanas` clase 87, con Top-k, MRR, Recall@50/100 y metricas jerarquicas Partida/Sub Partida/Clase.
- `docs/evaluacion_bm25_data_aduanas_clase87_v0.1.md`: cierre metodologico de la evaluacion BM25 normativa sobre `data_aduanas` clase 87.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/results.csv`.
- `outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/metrics.json`.
- `outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/summary.md`.
- `outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/failure_sample.csv`.

Resultado de cierre sobre 1,006 casos: Top-1 = 0.0229, Top-10 = 0.0467, MRR = 0.0312, Recall@50 = 0.0616 y Recall@100 = 0.0626. A nivel jerarquico, Clase@100 = 0.8887, Sub Partida@100 = 0.0755 y Partida@100 = 0.1252. Estos valores no son comparables de forma pareada con el BM25 historico de 600 casos porque cambian fuente, alcance y distribucion del evalset.

## Evaluacion Text2Trade dense v0.1

La Fase 5 formaliza una evaluacion reproducible del artefacto Text2Trade por fuerza bruta sobre `data/processed/evalset_v0.1.csv`, comparable contra el baseline BM25. No se usa HNSW porque `data/processed/indexes/text2trade_nandina8_v1/index/hnsw.index` esta ausente, no se reconstruye indice y no se ejecuta LLM.

Se versionan como codigo y documentacion metodologica:

- `src/retrieval/dense_text2trade.py`: carga vectores, mapa de ids, docstore y modelo local para recuperar candidatos por similitud densa.
- `src/experiments/evaluate_dense_text2trade.py`: evalua recuperacion dense por fuerza bruta sobre el evalset final y genera resultados por caso y metricas agregadas.
- `src/analysis/compare_bm25_dense.py`: compara BM25 baseline contra Text2Trade dense en Top-k NANDINA8, HS4, HS2, MRR y familias.
- `docs/evaluacion_text2trade_dense_v0.1.md`: cierre metodologico de la evaluacion dense y comparacion contra BM25.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/text2trade_dense_eval_v0.1/results.csv`.
- `outputs/evaluation/text2trade_dense_eval_v0.1/metrics.json`.
- `outputs/evaluation/text2trade_dense_eval_v0.1/summary.md`.
- `outputs/evaluation/text2trade_dense_eval_v0.1/comparison_bm25_dense.json`.
- `outputs/evaluation/text2trade_dense_eval_v0.1/comparison_bm25_dense.md`.

Estos outputs no se fuerzan al repositorio porque pueden regenerarse desde los scripts versionados, el evalset final y los artefactos Text2Trade locales congelados.

### Actualizacion Text2Trade dense data_aduanas clase 87 v0.1

La actualizacion de Fase 5 repite la evaluacion Dense Text2Trade vs BM25 sobre `data/processed/data_aduanas_evalset_clase87_v0.1.csv`, usando `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta esperada. La corrida usa fuerza bruta sobre los artefactos Text2Trade locales porque `hnsw.index` esta ausente; no reconstruye HNSW, no ejecuta LLM, no ejecuta Ollama y no usa APIs remotas. La Fase 5 historica de 600 casos se conserva como artefacto previo y no es comparable de forma directa con esta actualizacion.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_dense_text2trade_data_aduanas.py`: evalua Text2Trade dense sobre el evalset `data_aduanas` clase 87, con Top-k, MRR, Recall@50/100 y metricas jerarquicas Partida/Sub Partida/Clase.
- `src/analysis/compare_bm25_dense_data_aduanas.py`: compara BM25 clase 87 contra Dense clase 87, reportando deltas, casos ganados/perdidos/ambos recuperan/ambos fallan y comparacion jerarquica.
- `docs/evaluacion_text2trade_dense_data_aduanas_clase87_v0.1.md`: cierre metodologico de la evaluacion dense actualizada y su comparacion contra BM25.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/results.csv`.
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/metrics.json`.
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/summary.md`.
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/failure_sample.csv`.
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/comparison_bm25_dense_data_aduanas.json`.
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/comparison_bm25_dense_data_aduanas.md`.
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/case_comparison.csv`.

Resultado de cierre sobre 1,006 casos: Dense obtiene Top-1 = 0.0000, Top-10 = 0.0000, MRR = 0.0000, Recall@50 = 0.0010 y Recall@100 = 0.0010. A nivel jerarquico, Partida@100 = 0.2028, Sub Partida@100 = 0.0288 y Clase@100 = 0.8618. Frente a BM25 clase 87, Dense gana 0 casos Top-10, pierde 47, ambos recuperan 0 y ambos fallan 959. La decision metodologica es no promover Dense como recuperador principal ni sustituto de BM25 para este nuevo evalset.

## Evaluacion BM25 dual backfill evalset v0.1

La Fase 6C formaliza una validacion controlada sobre el evalset final de la variante `BM25_dual_protected_top_5_backfill`, seleccionada previamente en devset. La corrida no ejecuta LLM ni Text2Trade y no ajusta reglas mirando el evalset.

Decision metodologica de cierre: `BM25_hierarchical_v0.1` queda como ranking documental principal porque supera al dual protegido en Top-10 y MRR; `BM25_dual_protected_top_5_backfill` queda como fuente auxiliar para ampliar el pool por su mejor Recall@100. La siguiente fase debe disenar un pool combinado y un re-ranking LLM auditable sobre candidatos recuperados, no busqueda libre de NANDINAS desde cero.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_bm25_dual_backfill_evalset.py`: evalua BM25 plano, `C_hs6_leaf`, BM25 jerarquico v0.1 y el dual protegido sobre `data/processed/evalset_v0.1.csv`.
- `docs/evaluacion_bm25_dual_backfill_evalset_v0.1.md`: cierre metodologico de la validacion controlada en evalset.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_results.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_metrics.json`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_summary.md`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_comparison_vs_flat.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_comparison_vs_c_hs6.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_comparison_vs_hierarchical.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_family_analysis_hs2.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_family_analysis_hs4.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_family_analysis_regimen.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_top_rescues.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_top_deteriorations.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_all_methods_fail.csv`.
- `outputs/evaluation/bm25_dual_backfill_evalset_v0.1/dual_evalset_failure_sample.csv`.

Estos outputs no se fuerzan al repositorio porque pueden regenerarse desde el script versionado, el evalset final y los indices BM25 locales congelados.

### Actualizacion Fase 6B/6C data_aduanas clase 87 v0.1

La actualizacion reevalua de forma acotada las variantes normativas previamente definidas sobre `data/processed/data_aduanas_evalset_clase87_v0.1.csv`. No rehace la exploracion jerarquica, no repite todas las ablaciones antiguas y no ajusta reglas mirando el evalset clase 87.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_bm25_hierarchical_data_aduanas.py`: evalua `BM25_flat_current`, `BM25_hierarchical_v0.1` y `BM25_dual_protected_top_5_backfill` sobre `data_aduanas` clase 87, usando `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta esperada.
- `docs/evaluacion_bm25_jerarquico_dual_data_aduanas_clase87_v0.1.md`: cierre metodologico de la reinterpretacion Fase 6B/6C sobre clase 87.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/bm25_hierarchical_data_aduanas_clase87_v0.1/`.

Resultado de cierre sobre 1,006 casos: `BM25_hierarchical_v0.1` obtiene Top-1 = 0.0249, Top-10 = 0.0497, MRR = 0.0385 y Recall@100 = 0.3449; `BM25_dual_protected_top_5_backfill` obtiene Top-1 = 0.0239, Top-10 = 0.0487, MRR = 0.0340 y Recall@100 = 0.1948. Frente al BM25 plano clase 87, el jerarquico aporta mayor cobertura exacta profunda y el dual queda como cobertura auxiliar, pero ninguno se promueve como ranking principal para clase 87.

## Evaluacion candidate pool v0.1

La Fase 7A construye y evalua un pool combinado de candidatos NANDINA usando `BM25_hierarchical_v0.1` como ranking documental principal y `BM25_dual_protected_top_5_backfill` como fuente auxiliar de expansion. La evaluacion corregida separa recall jerarquico, recall dual, union disponible (`union_oracle`) y pool final recortado (`final_pool`). La corrida no ejecuta LLM ni Text2Trade, no modifica devset/evalset/Excel fuente y no ajusta reglas mirando resultados del evalset.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/build_candidate_pool.py`: construye el pool combinado para devset o evalset y genera metricas de cobertura exacta, HS4, HS2, union disponible y estrategias de pool final.
- `docs/evaluacion_candidate_pool_v0.1.md`: cierre metodologico de Fase 7A, correccion de `union_oracle` vs `final_pool`, metricas devset/evalset, aporte del dual, decision y limitaciones.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/candidate_pool_devset_v0.1/`.
- `outputs/evaluation/candidate_pool_evalset_v0.1/`.

Estos outputs no se fuerzan al repositorio porque pueden regenerarse desde el script versionado, devset/evalset y los indices BM25 locales congelados.

### Actualizacion Candidate Pool Normativo data_aduanas clase 87 v0.1

La actualizacion de Fase 7A construye y evalua un pool normativo sobre `data/processed/data_aduanas_evalset_clase87_v0.1.csv`, usando `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta esperada. La corrida no usa historico real como fuente de recuperacion, no usa Dense, no ejecuta LLM, Ollama, Text2Trade ni APIs remotas. El historico real queda reservado para Fase 9.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/build_candidate_pool_data_aduanas.py`: construye pools normativos clase 87 con `BM25_hierarchical_v0.1` y `BM25_dual_protected_top_5_backfill`; calcula `hierarchical_at_K`, `dual_at_K`, `union_oracle_at_K`, `final_pool_at_K` y metricas jerarquicas de Clase/Partida/Sub Partida.
- `docs/evaluacion_candidate_pool_data_aduanas_clase87_v0.1.md`: cierre metodologico de la actualizacion Fase 7A normativa sobre `data_aduanas` clase 87.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/`.

Resultado corregido sobre 1,006 casos: `union_oracle@100 = 0.3658`. El mejor pool operativo a Top-100 es `hierarchical_70_dual_backfill_30`, con `final_pool@100 = 0.3489`, `final_pool@200 = 0.6292`, `Partida@100 = 0.5885`, `Sub Partida@100 = 0.5268` y `Clase@100 = 0.7445`. A Top-200, `hierarchical_80_dual_backfill_20` y `hierarchical_70_dual_backfill_30` empatan en exactitud (`final_pool@200 = 0.6292`). El bloque normativo queda como respaldo/trazabilidad, no como fuente principal frente al pool historico de Fase 9.

## Evaluacion LLM rerank pool v0.1

La Fase 7B evalua de forma diagnostica preliminar el re-ranking cerrado con `qwen2.5:7b-instruct` mediante Ollama local sobre devset. Usa `hierarchical_80_dual_backfill_20`, temperatura 0 y `candidate_limit=20`; no usa APIs pagadas/remotas ni Text2Trade.

Se versionan:

- `src/llm/rerank_nandina_prompt_v0.1.md`: prompt JSON cerrado al pool enviado.
- `src/experiments/run_llm_rerank_pool_devset.py`: runner Ollama local con JSON Schema dinamico, validacion de pool y normalizacion auditable de duplicados.
- `src/experiments/evaluate_llm_rerank_pool.py`: metricas globales y condicionadas al pool efectivamente enviado.
- `docs/evaluacion_llm_rerank_pool_v0.1.md`: cierre metodologico y decision de no ejecutar evalset.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/llm_rerank_pool_devset_v0.1/`.

`sent_pool_at_candidate_limit` fue 0.6154. El LLM obtuvo Top-1 global 0.0769 y Top-1 condicionado 0.1250, por debajo del ranking original enviado (0.3846 global y 0.6250 condicionado). Gano 0 casos, perdio 7 y conservo 1. No se compara directamente contra `final_pool@100` porque el LLM recibio 20 candidatos. No se ejecuto evalset. La corrida queda como diagnostico preliminar con limitaciones: no fija `num_ctx`, el esquema no exige exactamente 10 candidatos y todavia requiere una iteracion mas estricta antes de cualquier evaluacion final LLM.

## Evaluacion LLM attribute retrieval devset v0.1

La Fase 7A-2 evalua una capa LLM pre-retrieval para extraer atributos estructurados desde descripciones comerciales y construir consultas BM25 jerarquicas protegidas. La corrida usa solo devset y `qwen2.5:7b-instruct` local mediante Ollama; no se ejecuta evalset ni Text2Trade.

Resultado de cierre: Top-10 se mantiene en 0.6154 y Recall@100 se mantiene en 0.6923 frente a `BM25_hierarchical_Q0`; MRR cambia marginalmente de 0.4701 a 0.4709. La via queda descartada como componente activo porque no aumenta cobertura y agrega riesgos de control de salida LLM.

Se versionan como codigo y documentacion metodologica:

- `src/llm/attribute_extraction_prompt_v0.1.md`: prompt para extraer atributos sin clasificar ni sugerir codigos.
- `src/experiments/run_llm_attribute_extraction_devset.py`: runner local Ollama sobre devset.
- `src/experiments/evaluate_llm_attribute_retrieval_devset.py`: evaluador BM25 jerarquico usando consultas derivadas de atributos.
- `docs/evaluacion_llm_attribute_retrieval_devset_v0.1.md`: cierre metodologico y decision de descarte.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/llm_attribute_retrieval_devset_v0.1/`.

## Evaluacion BM25 fielded devset v0.1

La Fase 7A-3 construye un corpus NANDINA por campos con pesos simulados por repeticion textual y una expansion lexica controlada aplicada al corpus, no a la consulta. La corrida usa solo devset, no ejecuta LLM, no usa Text2Trade ni APIs remotas.

Resultado de cierre en devset: `BM25_fielded_weighted_expanded_v0.1` sube Top-10 de 0.6154 a 1.0000, MRR de 0.4701 a 0.8654 y Recall@100 de 0.6923 a 1.0000 frente a `BM25_hierarchical_Q0`. Como el diccionario de expansion fue informado por casos del devset, se documenta como variante exploratoria con riesgo de sobreajuste y se congela antes de la validacion en evalset.

Se versionan como codigo y documentacion metodologica:

- `src/corpus/build_fielded_nandina_corpus.py`: genera corpus fielded y fielded-expanded desde el corpus jerarquico.
- `src/corpus/controlled_lexical_expansions_v0.1.json`: diccionario manual congelado de expansion lexica controlada.
- `src/experiments/build_bm25_fielded_index.py`: construye indices BM25 fielded y fielded-expanded.
- `src/experiments/evaluate_bm25_fielded_devset.py`: evalua variantes fielded sobre devset.
- `docs/evaluacion_bm25_fielded_devset_v0.1.md`: cierre metodologico de seleccion en devset.

Se documentan como artefactos regenerables e ignorados por Git:

- `data/processed/corpus_nandina_fielded_v0.1.jsonl`.
- `data/processed/corpus_nandina_fielded_expanded_v0.1.jsonl`.
- `data/processed/corpus_nandina_fielded_v0.1_metadata.json`.
- `data/processed/indexes/bm25_nandina8_fielded_v0.1.pkl`.
- `data/processed/indexes/bm25_nandina8_fielded_expanded_v0.1.pkl`.
- `data/processed/indexes/bm25_nandina8_fielded_v0.1_run_metadata.json`.
- `outputs/evaluation/bm25_fielded_devset_v0.1/`.

## Evaluacion BM25 fielded expanded evalset v0.1

La Fase 7A-3B valida en el evalset final la variante `BM25_fielded_weighted_expanded_v0.1`, seleccionada previamente usando devset en Fase 7A-3. El diccionario `src/corpus/controlled_lexical_expansions_v0.1.json` y los pesos del corpus fielded quedaron congelados antes de mirar evalset; no se ajustaron reglas despues de observar resultados.

La evaluacion no usa LLM, Text2Trade ni APIs remotas. La expansion controlada se aplica al corpus y no usa codigos como terminos buscables. El pool `phase7a_pool_hierarchical_80_dual_backfill_20` se reporta como pool auxiliar, no como ranking BM25 puro.

Resultado de cierre: la variante fielded/expanded mejora levemente cobertura amplia frente a `BM25_hierarchical_v0.1` (`Recall@100` 0.2617 contra 0.2500), pero degrada ranking temprano (`Top-10` 0.0683 contra 0.1067; `MRR` 0.0416 contra 0.0524). En evalset, `BM25_fielded_weighted_v0.1` y `BM25_fielded_weighted_expanded_v0.1` coinciden en metricas exactas; la expansion solo mejora HS4/HS2 frente al fielded sin expansion. No queda como nuevo ranking base; queda como experimento de cobertura amplia o posible fuente auxiliar de pool.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_bm25_fielded_evalset.py`: evalua `BM25_flat_current`, `BM25_hierarchical_v0.1`, `BM25_fielded_weighted_v0.1`, `BM25_fielded_weighted_expanded_v0.1` y el pool auxiliar Fase 7A sobre `data/processed/evalset_v0.1.csv`.
- `docs/evaluacion_bm25_fielded_evalset_v0.1.md`: cierre metodologico de la validacion externa preliminar en evalset.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/bm25_fielded_evalset_v0.1/fielded_evalset_results.csv`.
- `outputs/evaluation/bm25_fielded_evalset_v0.1/fielded_evalset_metrics.json`.
- `outputs/evaluation/bm25_fielded_evalset_v0.1/fielded_evalset_summary.md`.
- `outputs/evaluation/bm25_fielded_evalset_v0.1/fielded_evalset_case_comparison.csv`.
- `outputs/evaluation/bm25_fielded_evalset_v0.1/fielded_evalset_critical_cases.csv`.

## Evaluacion recuperacion jerarquica BM25 devset v0.1

La Fase 8A construye corpus e indices BM25 separados por niveles `HS2`, `HS4`, `HS6` y `NANDINA8`, diagnostica techo jerarquico y evalua estrategias restrictivas HS2/HS4/HS6 -> NANDINA8 sobre devset. No usa LLM, Ollama, OpenAI, Text2Trade ni APIs remotas. El evalset se usa solo para diagnostico de techo, no para seleccionar estrategia.

Resultado de cierre: ninguna estrategia jerarquica restrictiva supera a la recuperacion directa NANDINA8 ni al pool Fase 7A sobre devset. La mejor opcion directa conserva `Recall@100 = 0.6923`; las estrategias jerarquicas probadas quedan en `0.6154`, mientras el pool Fase 7A alcanza `0.7692`. No se selecciona una estrategia jerarquica para Fase 8B en esta forma.

Se versionan como codigo y documentacion metodologica:

- `src/analysis/diagnose_hierarchical_retrieval_ceiling.py`: diagnostica techo jerarquico HS2/HS4/HS6/NANDINA8 sobre devset y evalset usando recuperadores existentes.
- `src/corpus/build_hierarchical_level_corpora.py`: genera corpus por nivel desde el corpus fuente NANDINA.
- `src/experiments/build_bm25_level_indexes.py`: construye indices BM25 por nivel.
- `src/experiments/evaluate_hierarchical_bm25_devset.py`: evalua estrategias jerarquicas HS2/HS4/HS6 -> NANDINA8 sobre devset.
- `docs/evaluacion_recuperacion_jerarquica_bm25_devset_v0.1.md`: cierre metodologico de Fase 8A.

Se documentan como artefactos regenerables e ignorados por Git:

- `data/processed/corpus_levels/`.
- `data/processed/indexes/bm25_levels/`.
- `outputs/analysis/hierarchical_retrieval_ceiling_v0.1/`.
- `outputs/evaluation/hierarchical_bm25_devset_v0.1/`.

## Evaluacion pool expandido no restrictivo v0.1

La Fase 8B construye y evalua un pool expandido no restrictivo de candidatos NANDINA8. Las familias `HS2`, `HS4` y `HS6` se usan como senales auxiliares de backfill, no como filtros excluyentes. La estrategia se selecciona solo con devset y el evalset se ejecuta una vez con la configuracion congelada.

Estrategia seleccionada en devset: `phase7a_plus_all_sources_200`, `protected_base = 50`, `HS2 Top-M = 3`, `HS4 Top-M = 5`, `HS6 Top-M = 10`. En devset sube a `Recall@200 = 0.9231`, con una perdida frente al pool 7A a Top-100. En evalset logra `Recall@200 = 0.3233`; a Top-100 rescata 4 casos pero desplaza 6 frente al pool 7A, y a Top-200 rescata 34 casos sin perder casos recuperados por Fase 7A. `Recall@100 = 0.2633` no mejora el pool 7A (`0.2667`).

Decision de cierre: la expansion no restrictiva aporta cobertura a Top-200, pero el techo sigue lejos de `0.90`. Conviene pasar a Fase 9 con evidencia historica y/o clasificador supervisado, manteniendo el pool expandido como fuente auxiliar.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/build_nonrestrictive_expanded_pool.py`: construye y evalua pools no restrictivos para devset/evalset, con seleccion congelada desde devset.
- `docs/evaluacion_pool_expandido_no_restrictivo_v0.1.md`: cierre metodologico de Fase 8B.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/nonrestrictive_expanded_pool_devset_v0.1/`.
- `outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1/`.

## Evaluacion recuperacion historica leave-one-out v0.1

La Fase 9A evalua recuperacion basada en ejemplos historicos usando `data/processed/evalset_v0.1.csv` como banco inicial de pares `descripcion -> nandina_ref`. El protocolo es leave-one-out: cada caso se consulta contra los otros 599, sin self-match y con ranking final deduplicado por NANDINA8.

Resultado de cierre: `historical_bm25_description` alcanza `Recall@100 = 0.9100`, `Top-1 = 0.7967` y `MRR = 0.8305` sobre 600 casos. `historical_tfidf_char_word` se omite porque `scikit-learn` no esta disponible en el runtime local usable y no se instalaron dependencias. La corrida no usa LLM, Ollama, OpenAI ni APIs remotas.

Comparacion evalset: Fase 7A logra `Recall@100 = 0.2667`, Fase 8B logra `Recall@100 = 0.2633` y `Recall@200 = 0.3233`, mientras Fase 9A logra `Recall@100 = 0.9100`. El recuperador historico rescata 400 casos frente a Fase 7A/8B y deja 54 casos fuera de Top-100.

Decision de cierre: la mejora es sustancial; conviene ejecutar Fase 9B como pool hibrido historico + normativo, y ampliar despues el banco con historicos reales para validar generalizacion fuera del propio evalset.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_historical_examples_leave_one_out.py`: evalua BM25 historico leave-one-out sobre descripciones comerciales del evalset, calcula metricas exactas y jerarquicas, compara contra Fase 7A/8B si sus outputs existen y genera analisis de rescates/fallos.
- `docs/evaluacion_recuperacion_historica_leave_one_out_v0.1.md`: cierre metodologico de Fase 9A con protocolo, metricas, comparacion y decision.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/historical_examples_leave_one_out_v0.1/`.

### Actualizacion recuperacion historica data_aduanas clase 87 v0.1

La actualizacion de Fase 9A reemplaza el banco leave-one-out por un historico real separado: `data/processed/data_aduanas_historico_clase87_v0.1.csv` (3,000 filas) contra `data/processed/data_aduanas_evalset_clase87_v0.1.csv` (1,006 filas). Usa `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta esperada.

La corrida valida `id_unico_overlap_count = 0`, no permite self-match entre particiones, deduplica el ranking final por `NANDINA` y no usa BM25 normativo como fuente de candidatos. Tampoco usa LLM, Ollama, Text2Trade, OpenAI ni APIs remotas.

Resultado corregido sobre 1,006 casos: `Top-1 = 0.8628`, `Top-3 = 0.9374`, `Top-10 = 0.9801`, `Recall@100 = 1.0000` y `MRR = 0.9062`. A nivel jerarquico logra `Partida@100 = 1.0000`, `Sub Partida@100 = 1.0000` y `Clase@100 = 1.0000`. No quedan casos fuera de Top-100.

Comparacion metodologica: el mejor pool normativo Fase 7A sobre `data_aduanas` clase 87 alcanza `final_pool@100 = 0.3489` y `final_pool@200 = 0.6292`, por lo que la recuperacion historica real pasa a ser la fuente dominante recomendada para Fase 9B. El bloque normativo queda como backfill y trazabilidad, especialmente para codigos con poco o ningun soporte historico.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/evaluate_historical_retrieval_data_aduanas.py`: evalua recuperacion BM25 contra historico real `data_aduanas` clase 87, valida ausencia de solape por `id_unico`, deduplica candidatos por `NANDINA`, calcula metricas exactas, jerarquicas y por soporte historico, y genera analisis de fallos/rescates.
- `docs/evaluacion_recuperacion_historica_data_aduanas_clase87_v0.1.md`: cierre metodologico de la actualizacion Fase 9A sobre historico real separado.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/`.

## Evaluacion pool hibrido historico normativo v0.1

La Fase 9B combina recuperacion historica con fuentes normativas/lexicales ya generadas en Fase 7A y Fase 8B. El objetivo es mantener la fortaleza historica cuando existe precedente y usar lo normativo como trazabilidad y respaldo para singleton. La corrida no usa LLM, Ollama, OpenAI ni APIs remotas.

Estrategias evaluadas: `historical_first_95_normative_5`, `historical_first_80_normative_20`, `historical_first_50_normative_50`, `historical_plus_normative_rrf` y `oracle_historical_if_label_supported_else_normative`.

Resultado de cierre operativo: la mejor estrategia defendible es `historical_first_80_normative_20`, con `Top-1 = 0.7967`, `Top-10 = 0.8750`, `Recall@100 = 0.9167` y `MRR = 0.8306`. Frente a Fase 9A rescata 5 singleton y pierde 1 caso. En casos con precedente historico logra `Recall@100 = 0.9982`; en singleton logra `Recall@100 = 0.0926`.

Resultado diagnostico no operativo: `oracle_historical_if_label_supported_else_normative` alcanza `Recall@100 = 0.9250`, pero usa soporte de la NANDINA esperada (`support_counts[expected]`) y por eso queda solo como techo exploratorio, no como pipeline defendible para casos futuros.

Decision de cierre: el historico queda como fuente dominante; el bloque normativo queda como backfill y respaldo de trazabilidad. Conviene convertir `historical_first_80_normative_20` en pool oficial auditable o disenar una variante adaptativa basada en senales observables de confianza historica, no en soporte de la etiqueta esperada.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/build_hybrid_historical_normative_pool.py`: construye pools hibridos desde Fase 9A, Fase 7A y Fase 8B; calcula metricas exactas y jerarquicas, metricas por soporte historico, rescates, perdidas, singleton y contribucion de fuentes.
- `docs/evaluacion_pool_hibrido_historico_normativo_v0.1.md`: cierre metodologico de Fase 9B con fuentes, estrategias, comparacion, soporte historico, singleton y decision.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/hybrid_historical_normative_pool_v0.1/`.

### Actualizacion pool hibrido data_aduanas clase 87 v0.1

La actualizacion de Fase 9B combina el historico real de Fase 9A (`outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/`) con el pool normativo Fase 7A (`outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/`). Usa como fuente normativa `hierarchical_70_dual_backfill_30`, el mejor pool operativo normativo clase 87 a Top-100.

La corrida valida cero solape por `id_unico` entre historico y evalset, no usa la NANDINA esperada para decidir reglas, tolera casos sin candidatos normativos y no ejecuta LLM, Ollama, Text2Trade, Dense, OpenAI ni APIs remotas.

Estrategias evaluadas: `historical_only`, `historical_first_90_normative_10`, `historical_first_80_normative_20`, `historical_first_70_normative_30`, `historical_first_50_normative_50`, `historical_with_normative_backfill_if_low_support`, `historical_with_normative_backfill_if_missing_code` y `normative_only_reference`.

Resultado corregido sobre 1,006 casos: `historical_only` logra `Top-1 = 0.8628`, `Top-3 = 0.9374`, `Top-10 = 0.9801`, `Recall@100 = 1.0000`, `Recall@200 = 1.0000` y `MRR = 0.9062`. La estrategia recomendada `historical_with_normative_backfill_if_missing_code` conserva `Top-1 = 0.8628`, `Top-3 = 0.9374`, `Top-10 = 0.9801`, `Recall@100 = 1.0000`, `Recall@200 = 1.0000` y `MRR = 0.9062`. El normativo puro queda como referencia: `Top-1 = 0.0249`, `Top-10 = 0.0497`, `Recall@100 = 0.3489`, `Recall@200 = 0.6292` y `MRR = 0.0407`.

Decision de cierre: el historico solo se mantiene como ranking operativo temprano. El hibrido recomendado agrega backfill normativo posterior para trazabilidad y robustez futura, pero no mejora Top-100. Como todas las NANDINAS del evalset tienen soporte historico, el valor del backfill para codigos ausentes debe validarse despues con particiones temporales o historicos ampliados.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/build_hybrid_pool_data_aduanas.py`: construye pools hibridos clase 87 desde outputs regenerables de Fase 9A y Fase 7A, valida checksums e inexistencia de solape `id_unico`, calcula metricas exactas, jerarquicas, por soporte historico, contribucion por fuente y casos de bajo soporte.
- `docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md`: cierre metodologico de la actualizacion Fase 9B sobre `data_aduanas` clase 87.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1/`.

## Correccion data_aduanas descripciones v0.1

Se corrigio la ingesta SUNAT DAM para evitar que encabezados/secciones administrativas entren en `DESCRIPCION DE MERCANCIAS 1..5` o en `DESCRIPCION DE MERCANCIAS CONCATENADA`. La regla vive en `src/ingestion/sunat_series_parser.py` y se ejecuta desde el Excel local `data/Series - Descripciones.xlsx`, sin edicion manual de CSV.

La validacion post-correccion confirma cero apariciones de `REGISTRO DE ADUANAS`, `DECLARACION`, `FECHA NUMERACION`, `IDENTIFICACION`, `TRANSACCION`, `BASE IMPONIBLE` y `LIQUIDACION DEL ADEUDO` en las columnas descriptivas de historico, devset y evalset.

Se versiona como documentacion metodologica:

- `docs/correccion_data_aduanas_descripciones_v0.1.md`: diagnostico, causa, regla de correccion, conteos, validaciones, impacto en metricas 9A/9B y nota metodologica para Fase 10B.

## Evaluacion LLM rerank hybrid pool sample v0.1

La Fase 9C-A ejecuta una prueba diagnostica minima de LLM como re-ranker cerrado sobre el pool operativo `historical_first_80_normative_20`. Usa una muestra deterministica de 20 casos, `candidate_limit = 10`, temperatura 0 y el modelo local `qwen2.5:7b-instruct` mediante Ollama en `127.0.0.1:11434`. No usa OpenAI ni APIs remotas.

Composicion de muestra: 5 casos rank 1, 5 casos rank 2-10, 5 casos rank 11-100 y 5 singleton. Las filas con `oracle` se omitieron y solo se usaron filas del pool operativo.

Resultado de cierre: el ranking original enviado obtiene `Top-1 = 0.2500`, `Top-10 = 0.5000` y `MRR = 0.3542`; el re-ranking LLM obtiene `Top-1 = 0.2000`, `Top-10 = 0.5000` y `MRR = 0.3083`. Hubo JSON valido 20/20, violaciones de pool 0, duplicados 0, ganados 0, perdidos 4 y sin cambio 16.

Decision de cierre: no escalar re-ranking a Fase 9C-B porque degrada Top-1 y MRR. Si se usa LLM despues, debe evaluarse como justificacion breve/controlada de candidatos ya seleccionados, no como re-ranker operativo.

Se versionan como codigo, prompt y documentacion metodologica:

- `src/llm/rerank_hybrid_pool_prompt_v0.1.md`: prompt cerrado que prohibe inventar NANDINA, clasificar desde cero o devolver codigos fuera del pool.
- `src/experiments/run_llm_rerank_hybrid_pool_sample.py`: runner local Ollama para construir muestra, enviar Top-10, guardar respuesta cruda y normalizada, y detectar adherencia JSON/pool.
- `src/experiments/evaluate_llm_rerank_hybrid_pool_sample.py`: evaluador de ranking original vs LLM, MRR, ganados/perdidos/sin cambio y violaciones.
- `docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md`: cierre metodologico de Fase 9C-A.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/`.

## Evaluacion LLM explicacion Top-3 sample v0.1

La Fase 10A ejecuta una prueba diagnostica de LLM+RAG para explicacion auditable comparativa del Top-3 historico recuperado sobre `data_aduanas` clase 87. A diferencia de Fase 9C-A, el LLM no reordena candidatos, no busca NANDINA y no clasifica desde cero. Recibe solo los tres candidatos ya entregados por Fase 9A, en orden fijo, enriquecidos con contexto normativo jerarquico y evidencia textual.

Modelo local usado: `qwen2.5:7b-instruct` via Ollama en `127.0.0.1:11434`, temperatura 0. No se uso OpenAI, APIs remotas, descargas ni servicios con costo.

Composicion de muestra: 30 casos del evalset `data_aduanas` clase 87, balanceados como 10 rank 1, 10 rank 2-3, 5 rank 4-10 y 5 dificiles o de bajo soporte historico. La etiqueta esperada se conserva solo en `sample_cases.csv` para auditoria, no en el payload enviado al LLM.

Resultado de cierre: JSON valido 30/30, candidatos explicados completos 30/30, respeto del Top-3 original 30/30, ranking sin cambios 30/30, sin codigos inventados 30/30, evidencia citada por candidato 27/30 y comparacion Top-3 presente 29/30. Fallos parciales: 3 casos sin evidencia citada por todos los candidatos y 1 caso sin comparacion Top-3.

Decision de cierre: pasa a Fase 10B como explicacion controlada, no como recuperacion ni re-ranking. Para escalar, se recomienda reforzar la citacion obligatoria de evidencia por candidato.

Se versionan como codigo, prompt y documentacion metodologica:

- `src/llm/explain_top3_nandina_prompt_v0.1.md`: prompt cerrado para explicar y comparar el Top-3 sin agregar ni reordenar candidatos.
- `src/experiments/build_llm_explanation_top3_sample.py`: construye muestra, `sample_cases.csv` y `payloads.jsonl` con Top-3 historico y evidencia normativa.
- `src/experiments/run_llm_explanation_top3_sample.py`: runner local Ollama para generar explicaciones JSON estrictas.
- `src/experiments/evaluate_llm_explanation_top3_sample.py`: evaluador de estructura, adherencia al Top-3, no invencion y auditabilidad basica.
- `docs/evaluacion_llm_explicacion_top3_sample_v0.1.md`: cierre metodologico de Fase 10A.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/llm_explanation_top3_sample_v0.1/`.

## Evaluacion LLM explicacion Top-3 auditable v0.1

La Fase 10B formaliza la explicacion LLM+RAG auditable sobre el Top-3 historico recuperado usando los splits `data_aduanas` clase 87 corregidos. El LLM no busca NANDINA, no clasifica desde cero y no reordena candidatos; solo explica y compara los tres candidatos ya recuperados.

Modelo local usado: `qwen2.5:7b-instruct` via Ollama en `127.0.0.1:11434`, temperatura 0. No se uso OpenAI, APIs remotas, descargas ni servicios con costo.

Composicion de muestra: 50 casos del evalset `data_aduanas` clase 87, balanceados exactamente como 15 rank 1, 15 rank 2-3, 10 rank 4-10 y 10 dificiles o de bajo soporte historico. La etiqueta esperada queda solo en `sample_cases.csv` para auditoria, no en `payloads.jsonl`.

Resultado de cierre: JSON valido 50/50, Top-3 completo 50/50, ranking preservado 50/50, sin codigos fuera del pool 50/50, evidencia historica citada por candidato 50/50, evidencia normativa citada por candidato 50/50, comparacion Top-3 presente 50/50, advertencia final presente 50/50, sin clasificacion oficial 50/50 y score promedio de auditabilidad 0.9520.

Correccion metodologica menor: la nota del payload 10B fue cambiada a una frase neutral limitada a datos observables, candidatos Top-3 y evidencias recuperadas. La validacion posterior confirma que `payloads.jsonl` no contiene etiquetas esperadas ni variables de resultado, ni como claves ni como texto. Las metricas duras de paso se mantienen tras regenerar la fase completa; el score promedio cambia levemente por la nueva corrida local.

Decision de cierre: pasa metodologicamente a Fase 10C como explicacion auditable controlada. El LLM se mantiene como justificador de candidatos ya seleccionados, no como recuperador ni re-ranker.

Se versionan como codigo, prompt y documentacion metodologica:

- `src/llm/explain_top3_nandina_prompt_v0.2.md`: prompt cerrado formal que exige JSON estricto, trazabilidad por `candidate_id_unico` y `evidence_id`, comparacion Top-3 y advertencia final.
- `src/experiments/build_llm_explanation_top3_audit_sample.py`: constructor de muestra, payloads y metadata 10B.
- `src/experiments/run_llm_explanation_top3_audit_sample.py`: runner local Ollama con modo `--resume`, sin descarga de modelos y restringido a URLs locales.
- `src/experiments/evaluate_llm_explanation_top3_audit_sample.py`: evaluador formal de estructura, trazabilidad, comparacion, incertidumbre y criterios de paso a 10C.
- `src/experiments/render_llm_explanation_audit_cards.py`: renderizador de fichas auditables Markdown por caso.
- `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md`: cierre metodologico de Fase 10B.

Se documenta como output regenerable e ignorado por Git:

- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/`.

## Politica Git/no Git

Debe versionarse en Git:

- Configuraciones oficiales y operativas.
- Documentacion metodologica.
- Manifiestos.
- Dataset pequeno de validacion intermedia.
- Corpus y metadatos que ya estan trackeados y sostienen la trazabilidad de v0.1.

No debe subirse a Git:

- Nuevos archivos bajo `data/raw/*`.
- Nuevos archivos bajo `data/processed/*` salvo decision explicita.
- Corridas bajo `data/processed/runs/*`.
- Vectores, docstores, indices densos y pesos de modelos pesados.
- Salidas generadas bajo `outputs/*`.

La politica actual de `.gitignore` ya ignora nuevos contenidos en `data/raw`, `data/processed`, `outputs`, `models` e `indexes`, manteniendo solo `.gitkeep`. Algunos artefactos de `data/processed` ya estan versionados por historia del repositorio; el manifiesto los trata como parte congelada de v0.1, no como permiso general para subir nuevos datos procesados.

## Verificacion de integridad

Para verificar un archivo individual en PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "data/processed/corpus_rag_v1_index.jsonl"
```

El valor `Hash` debe coincidir con el campo `sha256` del artefacto correspondiente en `docs/manifest_artifacts_v0.1.json`.

Para revisar todos los paths del manifiesto, cargar el JSON y validar que cada `path` exista cuando `exists` sea `true`. Los directorios tienen `sha256: null`; los archivos listados tienen checksum. El propio manifiesto puede verificarse calculando su hash desde fuera del archivo.

## Reproducibilidad fuerte pendiente

Para una reproducibilidad mas fuerte faltaria:

- Registrar fuente externa oficial, URL o identificador persistente de cada PDF fuente.
- Documentar comandos exactos de reconstruccion de corpus, indice BM25 y artefactos Text2Trade.
- Crear un lockfile de dependencias o contenedor reproducible.
- Separar almacenamiento de artefactos pesados en una ubicacion externa versionada por checksum.
- Definir una politica formal para promover o descartar Text2Trade como componente experimental.
- Ejecutar evaluaciones controladas y registrar resultados finales en una fase posterior.

Hasta entonces, v0.1 debe interpretarse como protocolo congelado de piloto offline, no como validacion final de hipotesis.
