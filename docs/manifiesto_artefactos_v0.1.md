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
