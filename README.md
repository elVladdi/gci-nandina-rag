# Gestión de información documental para recomendación auditable de subpartidas NANDINA con LLM+RAG

Repositorio del piloto experimental offline de la investigación de maestría:

**Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline.**

El proyecto organiza corpus normativo, conjuntos de evaluación, recuperación documental y experimentos offline para apoyar la recomendación auditable de subpartidas NANDINA. No produce clasificación oficial, no reemplaza revisión experta y no está diseñado como sistema operativo institucional.

## Estado Actual

El repositorio contiene fases cerradas y versionadas hasta la Fase 6C:

- **Fase 1:** base reproducible BM25, corpus indexable y smoke test.
- **Fase 2:** protocolo experimental v0.1 y manifiesto de artefactos.
- **Fase 3:** evalset final v0.1 construido, deduplicado, validado y versionado.
- **Fase 4:** evaluación formal del baseline BM25 sobre el evalset final.
- **Fase 5:** evaluación Text2Trade dense por fuerza bruta y comparación contra BM25.
- **Fase 6A:** pruebas con LLM para query rewrite y multiquery sobre devset.
- **Fase 6B:** diagnóstico del corpus NANDINA plano, construcción jerárquica y recuperación dual hasta 6B-3.
- **Fase 6C:** validación controlada en evalset del BM25 dual `protected_top_5_backfill`, cerrada sin ajuste posterior de reglas.

Decisión metodológica vigente: `BM25_hierarchical_v0.1` queda como ranking documental principal por Top-10 y MRR en evalset; `BM25_dual_protected_top_5_backfill` queda como fuente auxiliar para ampliar el pool por su mejor Recall@100. La etapa LLM de re-ranking y justificación queda pendiente y deberá operar sobre candidatos recuperados, no buscar NANDINAS desde cero.

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

Decisión de cierre: `BM25_hierarchical_v0.1` queda como ranking inicial documental principal porque supera al dual protegido en Top-10 y MRR. El dual protegido obtiene el mejor Recall@100 y por ello se conserva como fuente auxiliar para ampliar el pool de candidatos, idealmente combinando candidatos de `BM25_hierarchical_v0.1` + `BM25_dual_protected_top_5_backfill` a profundidad 50 o 100. La etapa LLM posterior debe reordenar y justificar sobre ese pool recuperado con evidencia documental.

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
