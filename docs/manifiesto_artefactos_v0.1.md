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


## Evalset final v0.1

El evalset final v0.1 fue generado desde el Excel SUNAT real en modo `sunat-block` y congelado en `data/processed/evalset_v0.1.csv` con 600 casos unicos validos. Antes de congelarlo se auditaron 647 casos extraidos, 31 grupos duplicados exactos y 47 filas excedentes por la llave `descripcion + nandina_ref + regimen`.

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

## Evaluacion candidate pool v0.1

La Fase 7A construye y evalua un pool combinado de candidatos NANDINA usando `BM25_hierarchical_v0.1` como ranking documental principal y `BM25_dual_protected_top_5_backfill` como fuente auxiliar de expansion. La evaluacion corregida separa recall jerarquico, recall dual, union disponible (`union_oracle`) y pool final recortado (`final_pool`). La corrida no ejecuta LLM ni Text2Trade, no modifica devset/evalset/Excel fuente y no ajusta reglas mirando resultados del evalset.

Se versionan como codigo y documentacion metodologica:

- `src/experiments/build_candidate_pool.py`: construye el pool combinado para devset o evalset y genera metricas de cobertura exacta, HS4, HS2, union disponible y estrategias de pool final.
- `docs/evaluacion_candidate_pool_v0.1.md`: cierre metodologico de Fase 7A, correccion de `union_oracle` vs `final_pool`, metricas devset/evalset, aporte del dual, decision y limitaciones.

Se documentan como outputs regenerables e ignorados por Git:

- `outputs/evaluation/candidate_pool_devset_v0.1/`.
- `outputs/evaluation/candidate_pool_evalset_v0.1/`.

Estos outputs no se fuerzan al repositorio porque pueden regenerarse desde el script versionado, devset/evalset y los indices BM25 locales congelados.

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
