# Gestión de información documental para recomendación auditable de subpartidas NANDINA con LLM+RAG

Repositorio del piloto experimental offline de la investigación de maestría:

**Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline.**

El proyecto organiza corpus normativo, conjuntos de evaluación, recuperación documental y experimentos offline para apoyar la recomendación auditable de subpartidas NANDINA. No produce clasificación oficial, no reemplaza revisión experta y no está diseñado como sistema operativo institucional.

## Estado Actual

El repositorio contiene las fases cerradas y versionadas hasta la comparación BM25 vs Text2Trade dense:

- **Fase 1:** base reproducible BM25, corpus indexable y smoke test.
- **Fase 2:** protocolo experimental v0.1 y manifiesto de artefactos.
- **Fase 3:** evalset final v0.1 construido, deduplicado, validado y versionado.
- **Fase 4:** evaluación formal del baseline BM25 sobre el evalset final.
- **Fase 5:** evaluación Text2Trade dense por fuerza bruta y comparación contra BM25.

El branch principal es `main` y los artefactos versionables están pensados para reconstruir las evaluaciones. Los outputs bajo `outputs/` son regenerables y permanecen ignorados por Git.

## Alcance Metodológico

El experimento evalúa recuperación documental para recomendación de candidatos NANDINA-8 a partir de descripciones comerciales. La evaluación se realiza offline y se limita al corpus, configuraciones y evalset documentados en este repositorio.

El alcance empírico está concentrado en registros del régimen 10, importación para el consumo. El evalset actual conserva 599 casos con `regimen=10` y 1 caso con `regimen=12`; este caso se reporta como alerta metodológica y no debe usarse para generalizar resultados a otros regímenes aduaneros.

Las métricas reportadas miden recuperación de candidatos y ranking. No equivalen a clasificación oficial ni a validación jurídica de subpartidas.

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
