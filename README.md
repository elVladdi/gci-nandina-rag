# Gestión de información documental para recomendación auditable de subpartidas NANDINA con LLM+RAG

Repositorio del piloto experimental offline de la investigación de maestría:

**Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline.**

El proyecto organiza corpus normativo, conjuntos de evaluación, recuperación documental y experimentos offline para apoyar la recomendación auditable de subpartidas NANDINA. No produce clasificación oficial, no reemplaza revisión experta y no está diseñado como sistema operativo institucional.

## Estado Actual

El repositorio contiene fases cerradas y versionadas hasta la Fase 7B diagnostica preliminar:

- **Fase 1:** base reproducible BM25, corpus indexable y smoke test.
- **Fase 2:** protocolo experimental v0.1 y manifiesto de artefactos.
- **Fase 3:** evalset final v0.1 construido, deduplicado, validado y versionado.
- **Fase 4:** evaluación formal del baseline BM25 sobre el evalset final.
- **Fase 5:** evaluación Text2Trade dense por fuerza bruta y comparación contra BM25.
- **Fase 6A:** pruebas con LLM para query rewrite y multiquery sobre devset.
- **Fase 6B:** diagnóstico del corpus NANDINA plano, construcción jerárquica y recuperación dual hasta 6B-3.
- **Fase 6C:** validación controlada en evalset del BM25 dual `protected_top_5_backfill`, cerrada sin ajuste posterior de reglas.
- **Fase 7A:** construcción y evaluación del pool combinado `BM25_hierarchical_v0.1` + `BM25_dual_protected_top_5_backfill` sin LLM ni Text2Trade.
- **Fase 7A-2:** extraccion LLM de atributos previa a recuperacion sobre devset; no mejora recall y queda descartada como componente del pipeline.
- **Fase 7A-3:** BM25 por campos y expansion lexica controlada sobre devset; mejora fuerte en desarrollo, pero requiere validacion externa por riesgo de sobreajuste.
- **Fase 7A-3B:** validacion en evalset de `BM25_fielded_weighted_expanded_v0.1`, congelada desde devset; mejora levemente Recall@100, pero degrada Top-10/MRR frente a `BM25_hierarchical_v0.1`.
- **Fase 7B:** re-ranking diagnostico preliminar con `qwen2.5:7b-instruct` sobre devset; no mejora el ranking original, presenta limitaciones de diseno experimental y no pasa a evalset.
- **Fase 8A:** diagnostico y primer prototipo BM25 jerarquico HS2/HS4/HS6 -> NANDINA8; no mejora Recall@100 frente al directo ni al pool Fase 7A, por lo que no pasa a evalset como Fase 8B en esta forma.
- **Fase 8B:** pool expandido no restrictivo; mejora cobertura a Top-200 frente a Fase 7A, pero no mejora Recall@100 y queda lejos de 0.90.
- **Fase 9A:** recuperacion basada en ejemplos historicos con leave-one-out sobre evalset; `historical_bm25_description` alcanza `Recall@100 = 0.9100` sin LLM ni APIs remotas, condicionado a que exista precedente de la misma NANDINA en el banco historico.
- **Fase 9B:** pool hibrido historico + normativo; la estrategia operativa `historical_first_80_normative_20` alcanza `Recall@100 = 0.9167` sin fuga de etiqueta, rescata 5 singleton y mantiene Top-1/Top-10 de Fase 9A. El `oracle_historical_if_label_supported_else_normative` queda solo como techo diagnostico (`Recall@100 = 0.9250`).
- **Fase 9C-A:** re-ranking LLM diagnostico minimo sobre 20 casos del pool operativo `historical_first_80_normative_20`; JSON valido y sin violaciones de pool, pero degrada Top-1/MRR, por lo que no escala a 9C-B.

Decision metodologica vigente: el historico queda como fuente principal y lo normativo como backfill/trazabilidad. La estrategia operativa candidata es `historical_first_80_normative_20`, que mejora Fase 9A en `Recall@100` (`0.9167` vs `0.9100`) sin mirar la etiqueta esperada. El re-ranking LLM de 9C-A no debe escalarse porque degrada Top-1 y MRR; el LLM podria reservarse para justificacion controlada posterior.

El branch principal es `main` y los artefactos versionables están pensados para reconstruir las evaluaciones. Los outputs bajo `outputs/` son regenerables y permanecen ignorados por Git.

## Alcance Metodológico

El experimento evalúa recuperación documental para recomendación de candidatos NANDINA-8 a partir de descripciones comerciales. La evaluación se realiza offline y se limita al corpus, configuraciones y evalset documentados en este repositorio.

El alcance empírico está concentrado en registros del régimen 10, importación para el consumo. El evalset actual conserva 599 casos con `regimen=10` y 1 caso con `regimen=12`; este caso se reporta como alerta metodológica y no debe usarse para generalizar resultados a otros regímenes aduaneros.

Las métricas reportadas miden recuperación de candidatos y ranking. No equivalen a clasificación oficial ni a validación jurídica de subpartidas.

El devset preliminar se usa para desarrollo, diagnóstico y selección experimental preliminar. El evalset final v0.1 se reserva para validaciones controladas; la estrategia `protected_top_5_backfill` fue seleccionada como candidata desde devset, no desde resultados de evalset. La etapa LLM para re-ranking o justificación todavía no está evaluada como resultado final.

## Dataset de Evaluación

El devset preliminar queda en:

```text
data/processed/devset_validacion_intermedia.csv
```

Ese archivo se mantiene como conjunto pequeño para desarrollo, validación intermedia y pruebas de humo. No debe mezclarse con la evaluación final.

El evalset final v0.1 queda congelado en:

```text
data/processed/evalset_v0.1.csv
data/processed/evalset_v0.1_metadata.json
```

Características principales:

- 600 casos finales.
- Fuente: Excel SUNAT en formato por bloques.
- Deduplicación exacta por `descripcion + nandina_ref + regimen`.
- Columnas principales: `case_id`, `descripcion`, `nandina_ref`, `regimen`, `fuente_url`, `fecha_consulta`, `capitulo`, `partida`, `origen_caso`, `observaciones`.
- Documentación asociada:
  - `docs/protocolo_dataset_evaluacion_v0.1.md`
  - `docs/ficha_dataset_evaluacion_v0.1.md`
  - `docs/politica_curacion_evalset_v0.1.md`
  - `docs/guia_preparacion_excel_sunat_v0.1.md`

La ingesta desde Excel o CSV preparado por el usuario se realiza con:

```powershell
python -m src.evaluation.build_evalset_from_sunat_excel
```

## Estructura

```text
.
├── data/
│   ├── raw/                  # PDFs fuente locales
│   ├── external/             # referencias externas locales
│   └── processed/            # corpus, índices, evalset y artefactos procesados
├── docs/                     # documentación metodológica
├── notebooks/                # exploración y experimentos originales
├── outputs/                  # salidas regenerables ignoradas por Git
├── src/
│   ├── analysis/             # diagnósticos y comparaciones
│   ├── corpus/               # preparación de corpus
│   ├── evaluation/           # validación de datasets y métricas
│   ├── experiments/          # scripts ejecutables de evaluación/indexación
│   ├── retrieval/            # recuperación BM25 y dense
│   ├── utils/                # rutas y configuración
│   └── bm25_index.py         # índice BM25 compatible con pickles previos
├── requirements.txt
└── README.md
```

## Instalación

Desde la raíz del repositorio:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
C:\Users\Vladimir\AppData\Local\Programs\Python\Python310\python.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Nota: en Windows, `hnswlib` puede requerir Microsoft C++ Build Tools. Para la evaluación dense por fuerza bruta de Fase 5 no se necesita `hnswlib`; si la instalación completa falla solo por esa dependencia, puede instalarse el conjunto mínimo:

```powershell
python -m pip install numpy pandas torch sentence-transformers scikit-learn openpyxl
```

Si el proyecto se ejecuta desde otra ruta, puede fijarse la raíz con:

```powershell
$env:NANDINA_PROJECT_ROOT = "C:\ruta\al\repo"
```

## Configuración

La configuración operativa principal está en:

```text
src/configs/experiment_config.json
```

El snapshot metodológico oficial v0.1 está congelado en:

```text
src/configs/experiment_v0.1.json
```

Su protocolo asociado está en:

```text
docs/protocolo_experimental_v0.1.md
```

Las rutas se resuelven de forma relativa a la raíz del repositorio cuando es posible, para reducir dependencia de rutas absolutas locales.

## Corpus e Índice BM25

Si ya existe `data/processed/corpus_rag_v1_index.jsonl`, puede usarse directamente para BM25.

Para regenerar el campo `texto_index` a partir del corpus curado:

```powershell
python -m src.corpus.text_index
```

Para reconstruir el índice BM25 NANDINA-8:

```powershell
python -m src.experiments.build_bm25_index
```

Salidas por defecto:

```text
data/processed/indexes/bm25_nandina8.pkl
data/processed/indexes/bm25_nandina8_run_metadata.json
```

Para ejecutar una prueba mínima:

```powershell
python -m src.experiments.smoke_test --query "computadora portátil con procesador y memoria" --top-n 5
```

## Evaluación BM25 Baseline v0.1

La Fase 4 evalúa el baseline BM25 puro sobre el evalset final v0.1.

Scripts principales:

- `src/experiments/evaluate_bm25.py`
- `src/analysis/diagnose_bm25_baseline.py`

Para regenerar la evaluación:

```powershell
python -m src.experiments.evaluate_bm25 `
  --evalset data\processed\evalset_v0.1.csv `
  --k-list 1,3,5,10 `
  --output-dir outputs\evaluation\bm25_eval_v0.1
```

Para regenerar el diagnóstico:

```powershell
python -m src.analysis.diagnose_bm25_baseline `
  --evalset data\processed\evalset_v0.1.csv `
  --index data\processed\indexes\bm25_nandina8.pkl `
  --results outputs\evaluation\bm25_eval_v0.1\results.csv `
  --output-dir outputs\evaluation\bm25_eval_v0.1
```

Resultados principales:

| Métrica | Valor |
| --- | ---: |
| Casos evaluados | 600 |
| Casos con recuperación | 584 |
| Top-1 NANDINA8 | 0.0050 |
| Top-3 NANDINA8 | 0.0433 |
| Top-5 NANDINA8 | 0.0483 |
| Top-10 NANDINA8 | 0.0517 |
| MRR | 0.0290 |
| Top-10 HS4 | 0.1933 |
| Top-10 HS2 | 0.3800 |

Documento de cierre:

```text
docs/evaluacion_bm25_baseline_v0.1.md
```

Outputs regenerables:

```text
outputs/evaluation/bm25_eval_v0.1/
```

## Evaluación Text2Trade Dense v0.1

La Fase 5 evalúa el artefacto denso Text2Trade por fuerza bruta sobre el mismo evalset final v0.1. No usa HNSW porque `data/processed/indexes/text2trade_nandina8_v1/index/hnsw.index` no existe físicamente, y no ejecuta LLM.

Scripts principales:

- `src/retrieval/dense_text2trade.py`
- `src/experiments/evaluate_dense_text2trade.py`
- `src/analysis/compare_bm25_dense.py`

Artefactos densos usados:

```text
data/processed/indexes/text2trade_nandina8_v1/index/vectors.npy
data/processed/indexes/text2trade_nandina8_v1/index/id_map.json
data/processed/indexes/text2trade_nandina8_v1/store/nandina8_docstore.jsonl
data/processed/indexes/text2trade_nandina8_v1/model/
data/processed/indexes/text2trade_nandina8_v1/retrieval_config.json
```

Para regenerar la evaluación dense:

```powershell
python -m src.experiments.evaluate_dense_text2trade `
  --evalset data\processed\evalset_v0.1.csv `
  --artifact-dir data\processed\indexes\text2trade_nandina8_v1 `
  --output-dir outputs\evaluation\text2trade_dense_eval_v0.1 `
  --k-list 1,3,5,10 `
  --retrieval-depth 10
```

Para regenerar la comparación contra BM25:

```powershell
python -m src.analysis.compare_bm25_dense `
  --bm25-metrics outputs\evaluation\bm25_eval_v0.1\metrics.json `
  --bm25-results outputs\evaluation\bm25_eval_v0.1\results.csv `
  --dense-metrics outputs\evaluation\text2trade_dense_eval_v0.1\metrics.json `
  --dense-results outputs\evaluation\text2trade_dense_eval_v0.1\results.csv `
  --output-dir outputs\evaluation\text2trade_dense_eval_v0.1
```

Resultados dense principales:

| Métrica | Valor |
| --- | ---: |
| Top-1 NANDINA8 | 0.0000 |
| Top-3 NANDINA8 | 0.0000 |
| Top-5 NANDINA8 | 0.0033 |
| Top-10 NANDINA8 | 0.0050 |
| MRR | 0.0010 |
| Top-10 HS4 | 0.0117 |
| Top-10 HS2 | 0.0467 |

Comparación contra BM25:

| Métrica | BM25 | Text2Trade dense |
| --- | ---: | ---: |
| Top-10 NANDINA8 | 0.0517 | 0.0050 |
| MRR | 0.0290 | 0.0010 |
| Top-10 HS4 | 0.1933 | 0.0117 |
| Top-10 HS2 | 0.3800 | 0.0467 |

En este evalset, Text2Trade dense por fuerza bruta no mejora el baseline BM25.

Documento de cierre:

```text
docs/evaluacion_text2trade_dense_v0.1.md
```

Outputs regenerables:

```text
outputs/evaluation/text2trade_dense_eval_v0.1/
```

## Fase 6: Recuperación Jerárquica y Ranking Inicial Candidato

La primera hipótesis operativa de Fase 6 fue mejorar las consultas con LLM antes de BM25. Las pruebas de query rewrite y multiquery sobre el devset mostraron mejoras cualitativas puntuales, pero no mejoraron de forma suficiente ni estable el ranking inicial frente a BM25 Q0.

El diagnóstico posterior ubicó el problema principal en el corpus NANDINA plano: muchos documentos eran demasiado cortos o no autocontenidos para recuperar bien por BM25. Por ello se construyó un corpus jerárquico que incorpora contexto de partida 4D, HS6 cuando existe y NANDINA8. La ablation mostró una tensión clara: `C_hs6_leaf` protege precisión y MRR, mientras que las variantes con 4D amplían recall, pero pueden introducir ruido.

La Fase 6B-3 implementó recuperación dual: un índice de precisión `C_hs6_leaf`, un índice jerárquico de recall 4D/HS6/NANDINA8 y fusión `protected_top_5_backfill`. Esta estrategia fue seleccionada en devset como candidato experimental para validación controlada posterior en evalset.

Métricas principales sobre devset de 13 casos:

| Método | Top-1 | Top-10 | MRR | Recall@100 | Top-10 HS4/HS2 |
| --- | ---: | ---: | ---: | ---: | ---: |
| BM25 plano | 0.3846 | 0.5385 | 0.4370 | 0.6154 | 0.8462 |
| C_hs6_leaf | 0.4615 | 0.5385 | 0.4754 | 0.6154 | 0.7692 |
| Jerárquico v0.1 | 0.3846 | 0.6154 | 0.4701 | 0.6923 | 0.7692 |
| protected_top_5_backfill | 0.4615 | 0.6923 | 0.4991 | 0.7692 | 0.9231 |

Estas métricas son de desarrollo sobre devset y explican la selección del candidato experimental; no deben leerse como resultados finales del evalset.

### Validación controlada en evalset Fase 6C

La Fase 6C ejecutó una sola vez el evalset final v0.1 para la variante congelada `BM25_dual_protected_top_5_backfill`. No se ejecutó LLM, no se ejecutó Text2Trade y no se ajustaron reglas después de observar resultados del evalset.

| Método | Top-1 | Top-10 | MRR | Recall@100 |
| --- | ---: | ---: | ---: | ---: |
| BM25_flat_current | 0.0050 | 0.0517 | 0.0290 | 0.1633 |
| C_hs6_leaf | 0.0233 | 0.0400 | 0.0331 | 0.1650 |
| BM25_hierarchical_v0.1 | 0.0283 | 0.1067 | 0.0524 | 0.2500 |
| BM25_dual_protected_top_5_backfill | 0.0233 | 0.0850 | 0.0406 | 0.2700 |

Decision metodologica vigente: `BM25_hierarchical_v0.1`, `BM25_dual_protected_top_5_backfill`, `BM25_fielded_weighted_expanded_v0.1` y Fase 8B quedan como componentes normativos/lexicales de respaldo. Fase 9B confirma que el historico debe dominar cuando hay precedente, mientras el bloque normativo aporta trazabilidad y rescate de singleton. Fase 9C-A descarta escalar re-ranking LLM sobre el pool operativo.

Scripts y rutas principales:

- Query rewrite devset: `src/experiments/run_llm_query_rewrite_devset.py`, `src/experiments/evaluate_bm25_rewrite_devset.py`.
- Multiquery devset: `src/experiments/run_llm_multiquery_devset.py`, `src/experiments/evaluate_multiquery_rrf_devset.py`, `src/experiments/evaluate_weighted_bm25_multiquery_devset.py`.
- Corpus jerárquico: `src/corpus/audit_nandina_hierarchy.py`, `src/corpus/build_hierarchical_nandina_corpus.py`, `src/experiments/build_bm25_hierarchical_index.py`, `src/experiments/evaluate_bm25_hierarchical_devset.py`.
- Ablation jerárquica: `src/corpus/build_hierarchical_nandina_ablation_variants.py`, `src/experiments/evaluate_bm25_hierarchy_ablation_devset.py`.
- Dual backfill devset: `src/experiments/evaluate_bm25_dual_backfill_devset.py`.
- Dual backfill evalset: `src/experiments/evaluate_bm25_dual_backfill_evalset.py`.

Documentos de cierre y referencia:

- `docs/evaluacion_llm_query_rewrite_devset_v0.2.md`
- `docs/evaluacion_multiquery_rrf_devset_v0.1.md`
- `docs/evaluacion_weighted_bm25_multiquery_devset_v0.1.md`
- `docs/auditoria_corpus_nandina_jerarquico_v0.1.md`
- `docs/evaluacion_bm25_corpus_jerarquico_devset_v0.1.md`
- `docs/evaluacion_bm25_hierarchy_ablation_devset_v0.1.md`
- `docs/evaluacion_bm25_dual_backfill_devset_v0.1.md`
- `docs/evaluacion_bm25_dual_backfill_evalset_v0.1.md`

## Fase 7A: Candidate Pool NANDINA

La Fase 7A construye un pool combinado preservando `BM25_hierarchical_v0.1` como ranking principal y usando `BM25_dual_protected_top_5_backfill` como expansion auxiliar. No ejecuta LLM, no ejecuta Text2Trade y no ajusta reglas mirando resultados del evalset. La evaluacion corregida distingue cobertura de cada recuperador, union disponible (`union_oracle`) y pool final recortado (`final_pool`) que recibiria el LLM.

Script principal:

- `src/experiments/build_candidate_pool.py`

Documento de cierre:

- `docs/evaluacion_candidate_pool_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/candidate_pool_devset_v0.1/`
- `outputs/evaluation/candidate_pool_evalset_v0.1/`

Resultado de cierre: en evalset, la union real a Top-100 recupera `166/600 = 0.2767`, pero el pool entregable depende del ordenamiento y recorte. `hierarchical_first` queda en `final_pool@100 = 0.2500`; reservar espacio para dual con `hierarchical_80_dual_backfill_20` sube a `0.2667`. El pool puede alimentar una Fase 7B acotada y auditable, pero no es suficiente por si solo para una Fase 7B plena sin mejorar antes la recuperacion documental.

## Fase 7A-2: Extraccion LLM de Atributos Pre-Retrieval

La Fase 7A-2 evalua si `qwen2.5:7b-instruct` puede extraer atributos estructurados de la descripcion comercial y mejorar la consulta BM25 jerarquica sobre el devset. No se ejecuta sobre evalset.

Resultado de cierre: la extraccion de atributos no mejora Recall@50 ni Recall@100 frente a `BM25_hierarchical_Q0`; Top-10 se mantiene en `0.6154` y MRR cambia solo de `0.4701` a `0.4709`. Se observaron advertencias de control en algunas salidas LLM, por lo que esta via queda como diagnostico negativo y no como componente activo del pipeline.

Artefactos versionables:

- `src/llm/attribute_extraction_prompt_v0.1.md`
- `src/experiments/run_llm_attribute_extraction_devset.py`
- `src/experiments/evaluate_llm_attribute_retrieval_devset.py`
- `docs/evaluacion_llm_attribute_retrieval_devset_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/llm_attribute_retrieval_devset_v0.1/`

## Fase 7A-3: BM25 por Campos y Expansion Controlada en Devset

La Fase 7A-3 vuelve al cuello de botella de recuperacion documental y construye un corpus NANDINA ponderado por campos. La ponderacion se simula repitiendo texto de `descripcion_8d`, `descripcion_hs6`, `descripcion_4d` y expansion lexica controlada. No usa LLM, Text2Trade ni APIs remotas.

En devset, `BM25_fielded_weighted_expanded_v0.1` mejora fuertemente frente a `BM25_hierarchical_Q0`: Top-10 pasa de `0.6154` a `1.0000`, MRR de `0.4701` a `0.8654` y Recall@100 de `0.6923` a `1.0000`. Como el diccionario de expansion fue informado por casos del devset, esta mejora se trata como senal exploratoria con riesgo de sobreajuste y exige validacion unica en evalset sin ajustar reglas.

Artefactos versionables:

- `src/corpus/build_fielded_nandina_corpus.py`
- `src/corpus/controlled_lexical_expansions_v0.1.json`
- `src/experiments/build_bm25_fielded_index.py`
- `src/experiments/evaluate_bm25_fielded_devset.py`
- `docs/evaluacion_bm25_fielded_devset_v0.1.md`

Artefactos regenerables e ignorados por Git:

- `data/processed/corpus_nandina_fielded_v0.1.jsonl`
- `data/processed/corpus_nandina_fielded_expanded_v0.1.jsonl`
- `data/processed/corpus_nandina_fielded_v0.1_metadata.json`
- `data/processed/indexes/bm25_nandina8_fielded_v0.1.pkl`
- `data/processed/indexes/bm25_nandina8_fielded_expanded_v0.1.pkl`
- `data/processed/indexes/bm25_nandina8_fielded_v0.1_run_metadata.json`
- `outputs/evaluation/bm25_fielded_devset_v0.1/`

## Fase 7A-3B: BM25 Fielded Expanded Evalset

La Fase 7A-3B valida en evalset final la variante `BM25_fielded_weighted_expanded_v0.1`, seleccionada previamente en devset y congelada antes de mirar el evalset. No modifica el diccionario de expansion, no cambia pesos, no usa LLM, no usa Text2Trade y no usa APIs remotas.

Resultado de cierre: la variante fielded/expanded mejora cobertura amplia frente a `BM25_hierarchical_v0.1` (`Recall@100` de `0.2500` a `0.2617`), pero degrada ranking temprano (`Top-10` de `0.1067` a `0.0683`; `MRR` de `0.0524` a `0.0416`). En evalset, `BM25_fielded_weighted_v0.1` y `BM25_fielded_weighted_expanded_v0.1` coinciden en metricas exactas; la expansion solo mejora HS4/HS2 frente al fielded sin expansion. No queda como nuevo ranking base; puede considerarse como experimento de cobertura o posible fuente auxiliar para pool.

Script principal:

- `src/experiments/evaluate_bm25_fielded_evalset.py`

Documento de cierre:

- `docs/evaluacion_bm25_fielded_evalset_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/bm25_fielded_evalset_v0.1/`

## Fase 7B: Re-ranking LLM Diagnostico

La Fase 7B ejecuto `qwen2.5:7b-instruct` mediante Ollama local sobre los 13 casos del devset, con temperatura 0, estrategia `hierarchical_80_dual_backfill_20` y `candidate_limit=20`. No uso APIs pagadas/remotas ni Text2Trade.

Como el LLM recibio solo 20 candidatos, se reporta `sent_pool_at_candidate_limit = 8/13 = 0.6154`; las metricas condicionadas usan exclusivamente esos 8 casos y no se comparan directamente contra `final_pool@100`.

Resultados principales:

| Metrica | LLM | Ranking original enviado |
| --- | ---: | ---: |
| Top-1 global | 0.0769 | 0.3846 |
| MRR global | 0.0769 | 0.4679 |
| Top-1 condicionado | 0.1250 | 0.6250 |
| MRR condicionado | 0.1250 | 0.7604 |

El LLM gano 0 casos, perdio 7 y conservo 1 entre los 8 casos condicionados. La adherencia cruda al esquema fue 76.9%; tras normalizacion determinista de duplicados, JSON valido fue 100% y codigos fuera del pool 0. No se ejecuto evalset. Esta corrida queda como diagnostico preliminar: no usa `num_ctx` explicito, el esquema permitia devolver menos de 10 candidatos y la comparacion solo cubre los 20 candidatos enviados.

Artefactos versionables:

- `src/llm/rerank_nandina_prompt_v0.1.md`
- `src/experiments/run_llm_rerank_pool_devset.py`
- `src/experiments/evaluate_llm_rerank_pool.py`
- `docs/evaluacion_llm_rerank_pool_v0.1.md`

Outputs regenerables: `outputs/evaluation/llm_rerank_pool_devset_v0.1/`. Una siguiente iteracion deberia validar primero en devset con `candidate_limit` menor o evidencia compacta, `num_ctx` explicito, salida exactamente comparable y restricciones de idioma/formato mas estrictas.

## Fase 8A: Recuperacion Jerarquica por Niveles

La Fase 8A construye corpus e indices BM25 separados por nivel arancelario (`HS2`, `HS4`, `HS6` y `NANDINA8`) y evalua si filtrar NANDINA8 por familias recuperadas mejora el pool de candidatos. No usa LLM, Ollama, OpenAI, Text2Trade ni APIs remotas.

Diagnostico de techo: en evalset, `BM25_hierarchical_v0.1` logra `NANDINA8@100 = 0.2500`, `HS4@100 = 0.2850` y `HS2@100 = 0.4983`; el pool Fase 7A `hierarchical_80_dual_backfill_20` logra `final_pool@100 = 0.2667`, `HS4@100 = 0.2983` y `HS2@100 = 0.5283`. La brecha HS2 indica techo familiar, pero no se usa evalset para seleccionar estrategia.

Resultado devset: se probaron 102 configuraciones. El mejor resultado por `Recall@100` fue `direct_nandina8` (`Recall@100 = 0.6923`, `Top-10 = 0.6154`, `MRR = 0.4698`). Las mejores estrategias jerarquicas probadas quedaron en `Recall@100 = 0.6154`, por debajo del directo y del pool Fase 7A (`0.7692` en devset). No se recomienda Fase 8B sobre evalset con este prototipo restrictivo.

Artefactos versionables:

- `src/analysis/diagnose_hierarchical_retrieval_ceiling.py`
- `src/corpus/build_hierarchical_level_corpora.py`
- `src/experiments/build_bm25_level_indexes.py`
- `src/experiments/evaluate_hierarchical_bm25_devset.py`
- `docs/evaluacion_recuperacion_jerarquica_bm25_devset_v0.1.md`

Outputs regenerables e ignorados por Git:

- `data/processed/corpus_levels/`
- `data/processed/indexes/bm25_levels/`
- `outputs/analysis/hierarchical_retrieval_ceiling_v0.1/`
- `outputs/evaluation/hierarchical_bm25_devset_v0.1/`

## Fase 8B: Pool Expandido No Restrictivo

La Fase 8B usa las familias `HS2`, `HS4` y `HS6` como senales auxiliares de expansion, no como filtros excluyentes. La estrategia se selecciono solo con devset y el evalset se ejecuto una vez con la configuracion congelada. No se uso LLM, Ollama, OpenAI, Text2Trade ni APIs remotas.

Estrategia seleccionada desde devset: `phase7a_plus_all_sources_200`, con `protected_base = 50`, `HS2 Top-M = 3`, `HS4 Top-M = 5`, `HS6 Top-M = 10` y `pool_depth = 200`.

| Dataset | Metodo | Final@100 | Final@200 | HS2@100 | HS4@100 | HS6@100 | Rescates@100 | Perdidas@100 | Rescates@200 | Perdidas@200 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| devset | phase7a base | 0.7692 | NA | 0.9231 | 0.9231 | 0.7692 | 0 | 0 | NA | NA |
| devset | pool expandido 8B | 0.6923 | 0.9231 | 0.9231 | 0.9231 | 0.6923 | 0 | 1 | 3 | 1 |
| evalset | phase7a base | 0.2667 | NA | 0.5283 | 0.2983 | 0.2717 | 0 | 0 | NA | NA |
| evalset | pool expandido 8B | 0.2633 | 0.3233 | 0.5533 | 0.3033 | 0.2683 | 4 | 6 | 34 | 0 |

Decision: la expansion no restrictiva mejora cobertura amplia a `Recall@200 = 0.3233`, pero no mejora `Recall@100` frente al pool Fase 7A; a Top-100 rescata 4 casos y desplaza 6, mientras que a Top-200 rescata 34 y no pierde casos recuperados por 7A. El techo sigue lejos de `0.90`; falta `0.5767` aun midiendo a Top-200. La siguiente fase recomendada es Fase 9 con ejemplos historicos y/o clasificador supervisado.

Artefactos versionables:

- `src/experiments/build_nonrestrictive_expanded_pool.py`
- `docs/evaluacion_pool_expandido_no_restrictivo_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/nonrestrictive_expanded_pool_devset_v0.1/`
- `outputs/evaluation/nonrestrictive_expanded_pool_evalset_v0.1/`

## Fase 9A: Recuperacion Historica Leave-One-Out

La Fase 9A usa el evalset actual como banco inicial de ejemplos historicos `descripcion -> NANDINA`, con evaluacion leave-one-out: cada caso se consulta contra los otros 599, sin self-match y con deduplicacion por `nandina_ref`. No se usa LLM, Ollama, OpenAI ni APIs remotas.

Resultado principal: `historical_bm25_description` alcanza `Recall@100 = 0.9100`, `Top-1 = 0.7967` y `MRR = 0.8305` sobre 600 casos. La lectura correcta es condicionada: 546 casos tienen otra instancia de su misma NANDINA8 dentro del evalset y los 546 se recuperan en Top-100; los 54 fallos corresponden a NANDINA8 singleton, sin precedente interno. `historical_tfidf_char_word` se omitio porque `scikit-learn` no esta disponible en el runtime local usable y no se instalaron dependencias.

Frente a Fase 7A (`Recall@100 = 0.2667`) y Fase 8B (`Recall@100 = 0.2633`, `Recall@200 = 0.3233`), el enfoque historico mejora sustancialmente la cobertura cuando hay precedente disponible. La recomendacion para Fase 9B es construir un pool hibrido que incorpore recuperacion historica como fuente prioritaria, manteniendo senales normativas para trazabilidad y ampliando luego con historicos reales o validacion temporal.

Artefactos versionables:

- `src/experiments/evaluate_historical_examples_leave_one_out.py`
- `docs/evaluacion_recuperacion_historica_leave_one_out_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/historical_examples_leave_one_out_v0.1/`

## Fase 9B: Pool Hibrido Historico + Normativo

La Fase 9B combina la recuperacion historica de Fase 9A con los pools normativos/lexicales de Fase 7A y Fase 8B. Evalua cinco estrategias sin LLM, Ollama, OpenAI ni APIs remotas, deduplicando candidatos por `nandina_ref` y reportando metricas por soporte historico.

Resultado principal operativo: `historical_first_80_normative_20` alcanza `Top-1 = 0.7967`, `Top-10 = 0.8750`, `Recall@100 = 0.9167` y `MRR = 0.8306`. Frente a Fase 9A, rescata 5 singleton y pierde 1 caso. El oraculo `oracle_historical_if_label_supported_else_normative` alcanza `Recall@100 = 0.9250`, pero usa soporte de la NANDINA esperada y no se adopta como regla operativa.

Decision: usar `historical_first_80_normative_20` como candidato operativo de pool oficial auditable. La siguiente fase debe formalizar ese pool o probar una variante adaptativa basada en senales observables de confianza historica, no en soporte de la etiqueta esperada.

Artefactos versionables:

- `src/experiments/build_hybrid_historical_normative_pool.py`
- `docs/evaluacion_pool_hibrido_historico_normativo_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/hybrid_historical_normative_pool_v0.1/`

## Fase 9C-A: Re-ranking LLM Diagnostico Minimo

La Fase 9C-A evalua `qwen2.5:7b-instruct` mediante Ollama local como re-ranker cerrado sobre una muestra deterministica de 20 casos del pool operativo `historical_first_80_normative_20`, con `candidate_limit = 10`. No usa OpenAI ni APIs remotas.

Composicion de muestra: 5 casos con la NANDINA correcta en rank 1, 5 en rank 2-10, 5 en rank 11-100 y 5 singleton. Se omitieron las filas con `oracle` y solo se usaron filas del pool operativo.

| Ranking | Top-1 | Top-3 | Top-5 | Top-10 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original enviado | 0.2500 | 0.4500 | 0.5000 | 0.5000 | 0.3542 |
| LLM | 0.2000 | 0.4500 | 0.4500 | 0.5000 | 0.3083 |

Adherencia: JSON valido 20/20, violaciones de pool 0, duplicados 0. Resultado: 0 ganados, 4 perdidos y 16 sin cambio; 1 caso Top-1 correcto fue degradado. Decision: no escalar re-ranking a 9C-B. Si se usa LLM despues, debe ser para justificacion breve/controlada, no para reordenar el pool operativo.

Artefactos versionables:

- `src/llm/rerank_hybrid_pool_prompt_v0.1.md`
- `src/experiments/run_llm_rerank_hybrid_pool_sample.py`
- `src/experiments/evaluate_llm_rerank_hybrid_pool_sample.py`
- `docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/llm_rerank_hybrid_pool_sample_v0.1/`

## Manifiesto de Artefactos

El manifiesto versionado de artefactos está en:

```text
docs/manifest_artifacts_v0.1.json
docs/manifiesto_artefactos_v0.1.md
```

El manifiesto distingue artefactos versionados, ignorados, locales, referencias externas y salidas regenerables.

## Notebooks de Referencia

Los notebooks existentes documentan el desarrollo original:

- `01_Construccion_Corpus_NANDINA.ipynb`
- `02_Construccion_Corpus_Arancel2022_RGI_Notas.ipynb`
- `03_Curacion_Corpus_RAG.ipynb`
- `04_BM25_Indexacion_NANDINA.ipynb`
- `05_BM25_2Pasadas_LLM_Rewrite_Evaluacion.ipynb`
- `05_Text2Trade_Indexacion_NANDINA.ipynb`

## Política de Artefactos

No subir modelos pesados, PDFs grandes ni artefactos regenerables nuevos sin decisión explícita. Algunos artefactos pesados ya existían al iniciar la consolidación del proyecto; no se movieron ni eliminaron.

Los outputs bajo `outputs/` y el entorno `.venv/` están ignorados por Git. Deben regenerarse con los comandos documentados cuando se requiera reproducir una corrida.
