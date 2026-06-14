# Evaluacion BM25 baseline v0.1

Este documento cierra la Fase 4 del piloto offline LLM+RAG NANDINA. La fase evalua el baseline BM25 puro sobre el evalset final v0.1 y registra un diagnostico metodologico previo a comparar variantes densas, re-ranking o LLM+RAG.

La evaluacion no ejecuta LLM, no modifica el evalset, no modifica el devset y no produce clasificacion oficial. Solo mide recuperacion documental frente a la NANDINA esperada.

## Objetivo

Medir si el indice BM25 NANDINA-8 recupera la subpartida esperada a partir de la descripcion comercial del evalset final v0.1.

El analisis distingue tres niveles:

- NANDINA8 exacta.
- Partida HS4.
- Capitulo HS2.

Esta separacion permite saber si BM25 falla completamente o si recupera familias cercanas aunque no llegue al codigo exacto.

## Insumos

- Evalset final: `data/processed/evalset_v0.1.csv`.
- Indice BM25: `data/processed/indexes/bm25_nandina8.pkl`.
- Configuracion operativa: `src/configs/experiment_config.json`.
- Snapshot metodologico v0.1: `src/configs/experiment_v0.1.json`.
- Script de evaluacion: `src/experiments/evaluate_bm25.py`.
- Script diagnostico: `src/analysis/diagnose_bm25_baseline.py`.

El evalset contiene 600 casos finales deduplicados y su alcance empirico esta concentrado en regimen 10, importacion para el consumo.

## Comandos reproducibles

Desde la raiz del repositorio:

```powershell
python -m src.experiments.evaluate_bm25 `
  --evalset data\processed\evalset_v0.1.csv `
  --k-list 1,3,5,10 `
  --output-dir outputs\evaluation\bm25_eval_v0.1
```

Luego ejecutar el diagnostico:

```powershell
python -m src.analysis.diagnose_bm25_baseline `
  --evalset data\processed\evalset_v0.1.csv `
  --index data\processed\indexes\bm25_nandina8.pkl `
  --results outputs\evaluation\bm25_eval_v0.1\results.csv `
  --output-dir outputs\evaluation\bm25_eval_v0.1 `
  --k-list 1,3,5,10 `
  --min-group-size 5 `
  --sample-size 50
```

Prueba de humo BM25:

```powershell
python -m src.experiments.smoke_test --top-n 5
```

## Outputs regenerables

Los resultados quedan bajo `outputs/evaluation/bm25_eval_v0.1/`:

- `results.csv`: resultados por caso, candidatos, scores y rank de la NANDINA esperada.
- `metrics.json`: metricas agregadas de evaluacion BM25.
- `summary.md`: resumen breve de la evaluacion.
- `diagnostics.json`: diagnostico de cobertura, fallos y desempeno jerarquico.
- `diagnostics.md`: resumen legible del diagnostico.
- `failure_sample.csv`: muestra cualitativa de fallos con candidatos Top-5.

Estos archivos son regenerables y permanecen ignorados por Git mediante `outputs/`.

## Metricas globales

Evaluacion BM25 pura sobre 600 casos:

| Metrica | Valor |
| --- | ---: |
| Casos evaluados | 600 |
| Casos con recuperacion | 584 |
| Top-1 accuracy | 0.0050 |
| Top-3 accuracy | 0.0433 |
| Top-5 accuracy | 0.0483 |
| Top-10 accuracy | 0.0517 |
| MRR | 0.0290 |
| Sin match en Top-10 | 569 |

## Metricas jerarquicas

| Corte | NANDINA8 exacta | Partida HS4 | Capitulo HS2 |
| --- | ---: | ---: | ---: |
| Top-1 | 0.0050 | 0.0217 | 0.0817 |
| Top-3 | 0.0433 | 0.0933 | 0.1767 |
| Top-5 | 0.0483 | 0.1133 | 0.2333 |
| Top-10 | 0.0517 | 0.1933 | 0.3800 |

## Diagnostico de cobertura

| Cobertura | Valor |
| --- | ---: |
| NANDINA8 unicas en evalset | 129 |
| NANDINA8 presentes en indice | 129 |
| NANDINA8 ausentes del indice | 0 |
| Cobertura unica NANDINA8 | 1.0000 |
| Casos cuyo codigo correcto existe en indice | 600/600 |
| Cero resultados recuperados | 16 |

El bajo desempeno exacto no se explica por ausencia de codigos en el indice.

## Diagnostico de fallos

- Casos donde la NANDINA correcta existe en indice pero no aparece en Top-10: 569.
- Casos donde la NANDINA correcta no existe en indice: 0.
- Casos con cero resultados recuperados: 16.
- Casos donde aparece el capitulo correcto pero no la partida: 112.
- Casos donde aparece la partida correcta pero no la NANDINA8 exacta: 85.

Familias con mayor cantidad de fallos exactos Top-10:

- Capitulos: `73`, `64`, `39`, `90`, `62`.
- Partidas: `7318`, `6402`, `9001`, `9503`, `6214`.

## Interpretacion metodologica

BM25 puro funciona como baseline lexical debil. La cobertura del indice es completa para los codigos observados en el evalset, por lo que el problema principal no es que falten subpartidas NANDINA8.

El salto entre Top-10 exacto NANDINA8 (0.0517), Top-10 HS4 (0.1933) y Top-10 HS2 (0.3800) indica que BM25 a veces recupera la familia arancelaria correcta, pero rara vez alcanza la granularidad exacta. Esto sugiere una brecha de lexicalizacion entre descripciones comerciales SUNAT y textos documentales NANDINA, ademas de una dificultad de granularidad dentro de partidas cercanas.

## Limitaciones

- No se ejecuta LLM ni reescritura de consultas.
- No se evalua una decision de clasificacion oficial.
- El resultado depende del indice BM25 local congelado y del corpus documental v0.1.
- El alcance empirico del evalset esta concentrado en regimen 10, importacion para el consumo.
- Las metricas por capitulo y partida deben interpretarse con cautela cuando el grupo tiene pocas instancias.

## Siguiente comparacion sugerida

Mantener BM25 puro como baseline lexical debil y compararlo, sobre el mismo evalset, contra:

- Text2Trade o recuperacion densa.
- Re-ranking documental.
- BM25 + LLM/RAG, manteniendo separada la evaluacion de recuperacion y cualquier etapa explicativa.

La comparacion siguiente debe conservar las metricas exactas NANDINA8 y las metricas jerarquicas HS4/HS2 para distinguir mejoras de cobertura familiar frente a mejoras de codigo exacto.
