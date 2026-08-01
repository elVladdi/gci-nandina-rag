# Gestión de información documental para recomendación auditable de subpartidas NANDINA con LLM+RAG

Repositorio del piloto experimental offline de la investigación de maestría:

**Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline.**

El proyecto organiza corpus normativo, conjuntos de evaluación, recuperación documental y experimentos offline para apoyar la recomendación auditable de subpartidas NANDINA. No produce clasificación oficial, no reemplaza revisión experta y no está diseñado como sistema operativo institucional.

## Estado Actual

El repositorio contiene las fases históricas cerradas y la actualización metodológica `data_aduanas` clase 87 preparada hasta Fase 9B:

- **Fase 1:** base reproducible BM25, corpus indexable y smoke test.
- **Fase 2:** protocolo experimental v0.1, manifiesto de artefactos e incorporacion de `data_aduanas` como fuente operativa normalizada para la proxima actualizacion de Fase 3.
- **Fase 3:** evalset final v0.1 conservado como artefacto historico y Fase 3 actualizada para preparar particiones `data_aduanas` clase 87: historico, desarrollo y evaluacion.
- **Fase 4:** evaluacion formal del baseline BM25 sobre el evalset final v0.1 historico y actualizacion BM25 normativa sobre el evalset `data_aduanas` clase 87.
- **Fase 5:** evaluación Text2Trade dense por fuerza bruta sobre el evalset historico de 600 casos y actualizacion Dense vs BM25 sobre `data_aduanas` clase 87.
- **Fase 6A:** pruebas con LLM para query rewrite y multiquery sobre devset.
- **Fase 6B:** diagnóstico del corpus NANDINA plano, construcción jerárquica y recuperación dual hasta 6B-3; reinterpretada de forma acotada sobre `data_aduanas` clase 87 como recuperación normativa/trazabilidad.
- **Fase 6C:** validación controlada en evalset del BM25 dual `protected_top_5_backfill`, cerrada sin ajuste posterior de reglas; actualizada con reevaluación clase 87 sin rediseñar variantes.
- **Fase 7A:** construcción y evaluación del pool combinado `BM25_hierarchical_v0.1` + `BM25_dual_protected_top_5_backfill` sin LLM ni Text2Trade; actualizada como candidate pool normativo para `data_aduanas` clase 87.
- **Fase 7A-2:** extraccion LLM de atributos previa a recuperacion sobre devset; no mejora recall y queda descartada como componente del pipeline.
- **Fase 7A-3:** BM25 por campos y expansion lexica controlada sobre devset; mejora fuerte en desarrollo, pero requiere validacion externa por riesgo de sobreajuste.
- **Fase 7A-3B:** validacion en evalset de `BM25_fielded_weighted_expanded_v0.1`, congelada desde devset; mejora levemente Recall@100, pero degrada Top-10/MRR frente a `BM25_hierarchical_v0.1`.
- **Fase 7B:** re-ranking diagnostico preliminar con `qwen2.5:7b-instruct` sobre devset; no mejora el ranking original, presenta limitaciones de diseno experimental y no pasa a evalset.
- **Fase 8A:** diagnostico y primer prototipo BM25 jerarquico HS2/HS4/HS6 -> NANDINA8; no mejora Recall@100 frente al directo ni al pool Fase 7A, por lo que no pasa a evalset como Fase 8B en esta forma.
- **Fase 8B:** pool expandido no restrictivo; mejora cobertura a Top-200 frente a Fase 7A, pero no mejora Recall@100 y queda lejos de 0.90.
- **Fase 9A:** recuperacion basada en ejemplos historicos; el diagnostico leave-one-out inicial alcanza `Recall@100 = 0.9100`, y la actualizacion corregida con historico real `data_aduanas` clase 87 alcanza `Recall@100 = 1.0000` sin LLM ni APIs remotas.
- **Fase 9B:** pool hibrido historico + normativo; la corrida historica conserva `historical_first_80_normative_20` como antecedente (`Recall@100 = 0.9167`) y la actualizacion corregida `data_aduanas` clase 87 recomienda `historical_with_normative_backfill_if_missing_code` (`Recall@100 = 1.0000`, `Recall@200 = 1.0000`) sin degradar Top-1/Top-10/MRR.
- **Fase 9C-A:** re-ranking LLM diagnostico minimo sobre 20 casos del pool operativo `historical_first_80_normative_20`; JSON valido y sin violaciones de pool, pero degrada Top-1/MRR, por lo que no escala a 9C-B.
- **Fase 10A:** explicacion LLM+RAG diagnostica del Top-3 historico ya recuperado sobre 30 casos `data_aduanas` clase 87; `qwen2.5:7b-instruct` via Ollama local genera JSON valido 30/30, respeta Top-3 y ranking 30/30, no inventa codigos 30/30 y pasa a 10B como explicacion controlada, no como recuperacion ni re-ranking.
- **Fase 10B:** explicacion LLM+RAG auditable formal del Top-3 historico sobre 50 casos `data_aduanas` clase 87 corregido; genera JSON tecnico y fichas auditables, preserva Top-3/ranking 50/50, cita evidencia historica y normativa por candidato 50/50 y pasa metodologicamente a 10C.

Decision metodologica vigente: el historico queda como fuente principal y lo normativo como backfill/trazabilidad. En `data_aduanas` clase 87 corregido, el hibrido recomendado conserva el orden historico temprano (`Top-1 = 0.8628`, `Top-10 = 0.9801`, `MRR = 0.9062`) y mantiene cobertura exacta completa a Top-100/Top-200; el normativo no desplaza candidatos historicos tempranos y queda como respaldo documental. El re-ranking LLM de 9C-A no debe escalarse porque degrada Top-1 y MRR. Fase 10B confirma que el LLM debe usarse como explicador auditable del Top-3 fijo, no como recuperador, clasificador ni re-ranker, y pasa metodologicamente a 10C.

El branch principal es `main` y los artefactos versionables están pensados para reconstruir las evaluaciones. Los outputs bajo `outputs/` son regenerables y permanecen ignorados por Git.

## Alcance Metodológico

El experimento evalúa recuperación documental para recomendación de candidatos NANDINA-8 a partir de descripciones comerciales. La evaluación se realiza offline y se limita al corpus, configuraciones y conjuntos documentados en este repositorio.

El evalset v0.1 de 600 casos se conserva como artefacto histórico: está concentrado en registros del régimen 10, importación para el consumo, y mantiene 599 casos con `regimen=10` y 1 caso con `regimen=12` como alerta metodológica. La actualización metodológica vigente usa `data_aduanas` con alcance arancelario `Clase = 87`, particionado en histórico, desarrollo y evaluación sin solapamiento por `id_unico`.

Las métricas reportadas miden recuperación de candidatos y ranking. No equivalen a clasificación oficial ni a validación jurídica de subpartidas.

El devset preliminar y el devset `data_aduanas` se usan para desarrollo, diagnóstico y selección experimental preliminar. Los evalsets se reservan para validaciones controladas. La evidencia vigente muestra que el re-ranking LLM probado no mejora el ranking; por ahora, el LLM queda como candidato posterior para justificación controlada, no como recuperador ni reordenador operativo.

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

El evalset v0.1 de 600 casos se conserva como artefacto historico/versionado. Sus metricas y evaluaciones previas no se borran ni se reinterpretan retroactivamente, pero deja de ser la base metodologica principal para fases futuras una vez validada la Fase 3 actualizada.


Características principales:

- 600 casos finales.
- Fuente: fuente aduanera previa en formato por bloques.
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

### Splits data_aduanas clase 87

La Fase 3 actualizada usa `data_aduanas` como fuente metodologica para construir particiones experimentales homogeneas de `Clase = 87`, sin `id_unico` repetidos dentro de particiones ni solapamiento entre ellas. La ingesta corregida corta o recorta encabezados DAM claros para que no entren en `DESCRIPCION DE MERCANCIAS 1..5` ni en `DESCRIPCION DE MERCANCIAS CONCATENADA`.

Artefactos finales:

```text
data/processed/data_aduanas_historico_clase87_v0.1.csv
data/processed/data_aduanas_devset_clase87_v0.1.csv
data/processed/data_aduanas_evalset_clase87_v0.1.csv
data/processed/data_aduanas_splits_clase87_v0.1_metadata.json
```

Conteos v0.1:

| Split | Filas | NANDINAS distintas |
| --- | ---: | ---: |
| historico | 3,000 | 69 |
| desarrollo | 100 | 44 |
| evaluacion | 1,006 | 62 |

Documentacion asociada:

- `docs/protocolo_data_aduanas_clase87_v0.1.md`
- `docs/ficha_data_aduanas_clase87_v0.1.md`
- `docs/politica_curacion_data_aduanas_clase87_v0.1.md`

El comando reproducible es:

```powershell
python -m src.evaluation.build_data_aduanas_splits `
  --input data\interim\sunat_series_descripciones_normalized.csv `
  --output-dir data\processed `
  --scope-class 87 `
  --historical-size 3000 `
  --dev-size 100 `
  --seed 2026 `
  --overwrite
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

La Fase 4 evalua el baseline BM25 puro sobre el evalset final v0.1 historico y conserva esa evaluacion sin reinterpretarla. La actualizacion de Fase 4 agrega una evaluacion separada del BM25 normativo plano sobre el evalset `data_aduanas` clase 87.

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

### Actualizacion data_aduanas clase 87

La actualizacion de Fase 4 evalua el indice normativo `data/processed/indexes/bm25_nandina8.pkl` sobre:

```text
data/processed/data_aduanas_evalset_clase87_v0.1.csv
```

Columnas usadas:

- Consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta esperada: `NANDINA`.

Para regenerar la evaluacion:

```powershell
python -m src.experiments.evaluate_bm25_data_aduanas
```

Resultados principales sobre 1,006 casos:

| Metrica | Valor |
| --- | ---: |
| Top-1 NANDINA8 | 0.0229 |
| Top-3 NANDINA8 | 0.0338 |
| Top-5 NANDINA8 | 0.0398 |
| Top-10 NANDINA8 | 0.0467 |
| MRR | 0.0312 |
| Recall@50 | 0.0616 |
| Recall@100 | 0.0626 |
| Partida@100 | 0.1252 |
| Sub Partida@100 | 0.0755 |
| Clase@100 | 0.8887 |

Documento de cierre:

```text
docs/evaluacion_bm25_data_aduanas_clase87_v0.1.md
```

Outputs regenerables e ignorados por Git:

```text
outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/
```

Estas metricas no son una comparacion pareada contra la Fase 4 historica: cambian fuente, alcance y tamano del evalset. BM25 normativo queda como baseline auditable de referencia, no como recuperacion historica principal.

## Evaluación Text2Trade Dense v0.1

La Fase 5 historica evalúa el artefacto denso Text2Trade por fuerza bruta sobre el mismo evalset final v0.1 de 600 casos. No usa HNSW porque `data/processed/indexes/text2trade_nandina8_v1/index/hnsw.index` no existe físicamente, y no ejecuta LLM. La actualizacion de Fase 5 repite Dense vs BM25 sobre el evalset `data_aduanas` clase 87 sin borrar ni reinterpretar la corrida historica.

Scripts principales:

- `src/retrieval/dense_text2trade.py`
- `src/experiments/evaluate_dense_text2trade.py`
- `src/analysis/compare_bm25_dense.py`
- `src/experiments/evaluate_dense_text2trade_data_aduanas.py`
- `src/analysis/compare_bm25_dense_data_aduanas.py`

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

### Actualizacion data_aduanas clase 87

La actualizacion de Fase 5 evalua el artefacto Text2Trade local sobre:

```text
data/processed/data_aduanas_evalset_clase87_v0.1.csv
```

Columnas usadas:

- Consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta esperada: `NANDINA`.

Para regenerar la evaluacion dense:

```powershell
python -m src.experiments.evaluate_dense_text2trade_data_aduanas
```

Para regenerar la comparacion contra BM25 clase 87:

```powershell
python -m src.analysis.compare_bm25_dense_data_aduanas
```

Resultados dense principales sobre 1,006 casos:

| Metrica | Valor |
| --- | ---: |
| Top-1 NANDINA8 | 0.0000 |
| Top-3 NANDINA8 | 0.0000 |
| Top-5 NANDINA8 | 0.0000 |
| Top-10 NANDINA8 | 0.0000 |
| MRR | 0.0000 |
| Recall@50 | 0.0010 |
| Recall@100 | 0.0010 |
| Partida@100 | 0.2028 |
| Sub Partida@100 | 0.0288 |
| Clase@100 | 0.8618 |

Comparacion contra BM25 clase 87:

| Metrica | BM25 | Text2Trade dense |
| --- | ---: | ---: |
| Top-10 NANDINA8 | 0.0467 | 0.0000 |
| MRR | 0.0312 | 0.0000 |
| Recall@100 | 0.0626 | 0.0010 |
| Partida@100 | 0.1252 | 0.2028 |
| Sub Partida@100 | 0.0755 | 0.0288 |
| Clase@100 | 0.8887 | 0.8618 |

Casos Top-10: dense gana 0, pierde 47, ambos recuperan 0 y ambos fallan 959. Dense no aporta frente a BM25 para recuperacion exacta en este nuevo evalset; solo mejora Partida@100, con degradacion exacta y jerarquica en Sub Partida/Clase.

Documento de cierre:

```text
docs/evaluacion_text2trade_dense_data_aduanas_clase87_v0.1.md
```

Outputs regenerables e ignorados por Git:

```text
outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.1/
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

### Actualizacion Fase 6B/6C data_aduanas clase 87

La actualizacion no rehace la exploracion jerarquica ni las ablaciones antiguas. Reevalua solo variantes normativas previamente definidas sobre `data/processed/data_aduanas_evalset_clase87_v0.1.csv`, usando `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta esperada.

| Metodo | Top-1 | Top-10 | MRR | Recall@50 | Recall@100 | Partida@100 | Sub Partida@100 | Clase@100 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| BM25_flat_current | 0.0229 | 0.0467 | 0.0312 | 0.0616 | 0.0626 | 0.1252 | 0.0755 | 0.8887 |
| BM25_hierarchical_v0.1 | 0.0249 | 0.0497 | 0.0385 | 0.0626 | 0.3449 | 0.5865 | 0.5209 | 0.7386 |
| BM25_dual_protected_top_5_backfill | 0.0239 | 0.0487 | 0.0340 | 0.0716 | 0.1948 | 0.5905 | 0.3708 | 0.7753 |

Decision metodologica clase 87: `BM25_hierarchical_v0.1` se conserva como recuperador normativo auxiliar de trazabilidad porque mejora Top-10/MRR y Recall@100 exacto frente al BM25 plano. El dual protegido queda como fuente auxiliar de cobertura, no como ranking principal. Las variantes A/B/E/F/G quedan como evidencia historica y no se reejecutan en esta actualizacion.

Documento de cierre:

- `docs/evaluacion_bm25_jerarquico_dual_data_aduanas_clase87_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/bm25_hierarchical_data_aduanas_clase87_v0.1/`

Decision metodologica vigente: `BM25_hierarchical_v0.1`, `BM25_dual_protected_top_5_backfill`, `BM25_fielded_weighted_expanded_v0.1` y Fase 8B quedan como componentes normativos/lexicales de respaldo. Fase 9B confirma que el historico debe dominar cuando hay precedente, mientras el bloque normativo aporta trazabilidad y rescate de singleton. Fase 9C-A descarta escalar re-ranking LLM sobre el pool operativo.

Scripts y rutas principales:

- Query rewrite devset: `src/experiments/run_llm_query_rewrite_devset.py`, `src/experiments/evaluate_bm25_rewrite_devset.py`.
- Multiquery devset: `src/experiments/run_llm_multiquery_devset.py`, `src/experiments/evaluate_multiquery_rrf_devset.py`, `src/experiments/evaluate_weighted_bm25_multiquery_devset.py`.
- Corpus jerárquico: `src/corpus/audit_nandina_hierarchy.py`, `src/corpus/build_hierarchical_nandina_corpus.py`, `src/experiments/build_bm25_hierarchical_index.py`, `src/experiments/evaluate_bm25_hierarchical_devset.py`.
- Ablation jerárquica: `src/corpus/build_hierarchical_nandina_ablation_variants.py`, `src/experiments/evaluate_bm25_hierarchy_ablation_devset.py`.
- Dual backfill devset: `src/experiments/evaluate_bm25_dual_backfill_devset.py`.
- Dual backfill evalset: `src/experiments/evaluate_bm25_dual_backfill_evalset.py`.
- Actualizacion clase 87: `src/experiments/evaluate_bm25_hierarchical_data_aduanas.py`.

Documentos de cierre y referencia:

- `docs/evaluacion_llm_query_rewrite_devset_v0.2.md`
- `docs/evaluacion_multiquery_rrf_devset_v0.1.md`
- `docs/evaluacion_weighted_bm25_multiquery_devset_v0.1.md`
- `docs/auditoria_corpus_nandina_jerarquico_v0.1.md`
- `docs/evaluacion_bm25_corpus_jerarquico_devset_v0.1.md`
- `docs/evaluacion_bm25_hierarchy_ablation_devset_v0.1.md`
- `docs/evaluacion_bm25_dual_backfill_devset_v0.1.md`
- `docs/evaluacion_bm25_dual_backfill_evalset_v0.1.md`
- `docs/evaluacion_bm25_jerarquico_dual_data_aduanas_clase87_v0.1.md`

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

### Actualizacion data_aduanas clase 87

La actualizacion de Fase 7A construye un candidate pool normativo sobre `data/processed/data_aduanas_evalset_clase87_v0.1.csv`, usando `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta esperada. No usa historico real como recuperador, no usa Dense, no usa LLM, no ejecuta Ollama, no usa Text2Trade y no usa APIs remotas.

Estrategias evaluadas: `hierarchical_only`, `dual_only`, `hierarchical_first_100`, `hierarchical_80_dual_backfill_20` y `hierarchical_70_dual_backfill_30`. `union_oracle` se reporta solo como techo diagnostico, no como pool operativo ordenado.

| Estrategia | Pool@100 | Pool@200 | Partida@100 | Sub Partida@100 | Clase@100 |
| --- | ---: | ---: | ---: | ---: | ---: |
| `hierarchical_only` | 0.3449 | 0.6233 | 0.5865 | 0.5209 | 0.7386 |
| `dual_only` | 0.1948 | 0.5934 | 0.5905 | 0.3708 | 0.7753 |
| `hierarchical_first_100` | 0.3449 | 0.5895 | 0.5865 | 0.5209 | 0.7386 |
| `hierarchical_80_dual_backfill_20` | 0.3459 | 0.6292 | 0.5865 | 0.5219 | 0.7406 |
| `hierarchical_70_dual_backfill_30` | 0.3489 | 0.6292 | 0.5885 | 0.5268 | 0.7445 |

Techos diagnosticos: `union_oracle@100 = 0.3658` y `union_oracle@200 = 0.6372`. Decision: `hierarchical_70_dual_backfill_30` queda como mejor respaldo normativo Top-100; a Top-200 empata en exactitud con `hierarchical_80_dual_backfill_20`. El bloque normativo queda como respaldo/trazabilidad frente al pool historico de Fase 9, no como fuente principal.

Artefactos versionables:

- `src/experiments/build_candidate_pool_data_aduanas.py`
- `docs/evaluacion_candidate_pool_data_aduanas_clase87_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/`

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

## Fase 9A: Recuperacion Historica

La Fase 9A mide recuperacion basada en precedentes clasificados. El diagnostico inicial usa el evalset historico como banco de ejemplos `descripcion -> NANDINA`, con evaluacion leave-one-out: cada caso se consulta contra los otros 599, sin self-match y con deduplicacion por `nandina_ref`. No se usa LLM, Ollama, OpenAI ni APIs remotas.

Resultado principal: `historical_bm25_description` alcanza `Recall@100 = 0.9100`, `Top-1 = 0.7967` y `MRR = 0.8305` sobre 600 casos. La lectura correcta es condicionada: 546 casos tienen otra instancia de su misma NANDINA8 dentro del evalset y los 546 se recuperan en Top-100; los 54 fallos corresponden a NANDINA8 singleton, sin precedente interno. `historical_tfidf_char_word` se omitio porque `scikit-learn` no esta disponible en el runtime local usable y no se instalaron dependencias.

Frente a Fase 7A (`Recall@100 = 0.2667`) y Fase 8B (`Recall@100 = 0.2633`, `Recall@200 = 0.3233`), el enfoque historico mejora sustancialmente la cobertura cuando hay precedente disponible. La recomendacion para Fase 9B es construir un pool hibrido que incorpore recuperacion historica como fuente prioritaria, manteniendo senales normativas para trazabilidad y ampliando luego con historicos reales o validacion temporal.

### Actualizacion data_aduanas clase 87

La actualizacion de Fase 9A reemplaza el banco leave-one-out por historico real separado:

- Historico: `data/processed/data_aduanas_historico_clase87_v0.1.csv` (3,000 filas).
- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.1.csv` (1,006 filas).
- Consulta: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta: `NANDINA`.

La validacion confirma `id_unico_overlap_count = 0`. El metodo `historical_bm25_data_aduanas_clase87` construye un indice BM25 local sobre las descripciones historicas, deduplica candidatos por `NANDINA` y no usa BM25 normativo como fuente de candidatos.

Resultados corregidos principales: `Top-1 = 0.8628`, `Top-3 = 0.9374`, `Top-10 = 0.9801`, `Recall@100 = 1.0000` y `MRR = 0.9062`. A nivel jerarquico, `Partida@100 = 1.0000`, `Sub Partida@100 = 1.0000` y `Clase@100 = 1.0000`. No quedan casos fuera de Top-100.

Frente al pool normativo Fase 7A actualizado para clase 87 (`final_pool@100 = 0.3489`; `final_pool@200 = 0.6292`), la mejora historica es sustancial. La recomendacion para Fase 9B actualizada es un pool hibrido con historico como fuente dominante y backfill normativo para trazabilidad y bajo soporte.

Artefactos versionables:

- `src/experiments/evaluate_historical_examples_leave_one_out.py`
- `docs/evaluacion_recuperacion_historica_leave_one_out_v0.1.md`
- `src/experiments/evaluate_historical_retrieval_data_aduanas.py`
- `docs/evaluacion_recuperacion_historica_data_aduanas_clase87_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/historical_examples_leave_one_out_v0.1/`
- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/`

## Fase 9B: Pool Hibrido Historico + Normativo

La Fase 9B historica combina la recuperacion leave-one-out de Fase 9A con los pools normativos/lexicales de Fase 7A y Fase 8B. Evalua cinco estrategias sin LLM, Ollama, OpenAI ni APIs remotas, deduplicando candidatos por `nandina_ref` y reportando metricas por soporte historico.

Resultado principal operativo: `historical_first_80_normative_20` alcanza `Top-1 = 0.7967`, `Top-10 = 0.8750`, `Recall@100 = 0.9167` y `MRR = 0.8306`. Frente a Fase 9A, rescata 5 singleton y pierde 1 caso. El oraculo `oracle_historical_if_label_supported_else_normative` alcanza `Recall@100 = 0.9250`, pero usa soporte de la NANDINA esperada y no se adopta como regla operativa.

Decision: usar `historical_first_80_normative_20` como candidato operativo de pool oficial auditable. La siguiente fase debe formalizar ese pool o probar una variante adaptativa basada en senales observables de confianza historica, no en soporte de la etiqueta esperada.

Artefactos versionables:

- `src/experiments/build_hybrid_historical_normative_pool.py`
- `docs/evaluacion_pool_hibrido_historico_normativo_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/hybrid_historical_normative_pool_v0.1/`

### Actualizacion data_aduanas clase 87

La actualizacion de Fase 9B combina:

- Historico real Fase 9A: `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.1/`.
- Normativo Fase 7A: `outputs/evaluation/candidate_pool_data_aduanas_clase87_v0.1/`, usando `hierarchical_70_dual_backfill_30`.

La validacion confirma cero solape por `id_unico` entre historico y evalset. Las estrategias no usan la NANDINA esperada para decidir reglas, no ejecutan LLM/Ollama/Text2Trade/Dense y no usan APIs remotas.

| Estrategia | Top-1 | Top-10 | Top-20 | Top-50 | Top-100 | Top-200 | MRR |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `historical_only` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 |
| `historical_with_normative_backfill_if_missing_code` | 0.8628 | 0.9801 | 0.9970 | 1.0000 | 1.0000 | 1.0000 | 0.9062 |
| `normative_only_reference` | 0.0249 | 0.0497 | 0.0517 | 0.0626 | 0.3489 | 0.6292 | 0.0407 |

Decision: recomendar `historical_with_normative_backfill_if_missing_code`. Conserva el ranking historico como orden operativo principal, no degrada Top-1/Top-10/Top-100/MRR y agrega backfill normativo posterior para trazabilidad y robustez futura. Como todas las NANDINAS del evalset tienen soporte historico y ya se alcanza cobertura completa a Top-100, el valor del backfill para codigos ausentes requiere validacion futura.

Artefactos versionables:

- `src/experiments/build_hybrid_pool_data_aduanas.py`
- `docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1/`

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

## Fase 10B: Explicacion LLM Top-3 Auditable

La Fase 10B formaliza la explicacion auditable LLM+RAG del Top-3 historico recuperado sobre `data_aduanas` clase 87 corregido. Usa `qwen2.5:7b-instruct` mediante Ollama local, temperatura 0, sin OpenAI, sin APIs remotas, sin descargas y sin servicios con costo.

La muestra contiene 50 casos del evalset, balanceados de forma deterministica: 15 casos con NANDINA correcta en rank 1 historico, 15 en rank 2-3, 10 en rank 4-10 y 10 dificiles o de bajo soporte historico. El balance se logro exactamente. La etiqueta esperada queda solo en `sample_cases.csv` para auditoria y no se envia al LLM.

Resultado principal: JSON valido 50/50, Top-3 completo 50/50, ranking preservado 50/50, sin codigos fuera del pool 50/50, evidencia historica citada por candidato 50/50, evidencia normativa citada por candidato 50/50, comparacion Top-3 presente 50/50, advertencia final presente 50/50 y score promedio de auditabilidad 0.9520.

Correccion metodologica menor: el payload 10B usa una nota neutral (`Payload limitado a datos observables, candidatos Top-3 y evidencias recuperadas.`) y la validacion posterior confirma que `payloads.jsonl` no contiene etiquetas esperadas ni variables de resultado, ni como claves ni como texto. Las metricas duras de paso se mantienen tras regenerar la fase; el score promedio cambia levemente por la nueva corrida local.

Decision: pasa metodologicamente a Fase 10C. La salida debe leerse como apoyo documental para revision experta; no reemplaza clasificacion oficial.

Artefactos versionables:

- `src/llm/explain_top3_nandina_prompt_v0.2.md`
- `src/experiments/build_llm_explanation_top3_audit_sample.py`
- `src/experiments/run_llm_explanation_top3_audit_sample.py`
- `src/experiments/evaluate_llm_explanation_top3_audit_sample.py`
- `src/experiments/render_llm_explanation_audit_cards.py`
- `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md`

Outputs regenerables e ignorados por Git:

- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/`

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
