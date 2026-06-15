# Evaluacion Text2Trade dense v0.1

## Objetivo

Esta subfase evalua el artefacto denso Text2Trade existente sobre el evalset final `data/processed/evalset_v0.1.csv`, usando recuperacion por fuerza bruta sobre vectores congelados y comparando sus metricas contra el baseline BM25 de Fase 4.

La evaluacion mide recuperacion documental de candidatos NANDINA-8. No ejecuta LLM, no clasifica mercancias oficialmente y no reemplaza revision experta.

## Artefactos usados

La evaluacion usa el directorio local:

```text
data/processed/indexes/text2trade_nandina8_v1/
```

Artefactos principales:

- `index/vectors.npy`: matriz densa congelada de documentos NANDINA-8.
- `index/id_map.json`: mapa entre filas vectoriales, `doc_id` y codigo NANDINA.
- `store/nandina8_docstore.jsonl`: docstore con texto y metadatos por documento.
- `model/`: modelo local SentenceTransformer usado para codificar consultas.
- `retrieval_config.json`: configuracion declarada del recuperador denso.
- `text2trade_nandina8_run_metadata.json`: metadata historica de construccion del artefacto.

En la inspeccion previa, `vectors.npy`, `id_map.json` y `nandina8_docstore.jsonl` contenian 7644 registros consistentes, con embeddings de dimension 384.

## Por que fuerza bruta y no HNSW

La metadata historica declara `index/hnsw.index`, pero ese archivo no existe fisicamente en el checkout actual. Para evitar reconstruir indices y mantener la evaluacion limitada a artefactos congelados, la Fase 5B evalua por fuerza bruta:

1. Carga `vectors.npy`.
2. Codifica cada descripcion del evalset con el modelo local.
3. Normaliza embeddings segun `retrieval_config.json`.
4. Calcula producto punto/coseno contra todos los vectores.
5. Ordena candidatos y calcula metricas Top-k.

No se usa `hnswlib`, no se usa HNSW y no se ejecuta LLM.

## Comandos reproducibles

Desde la raiz del repositorio, con el `.venv` del proyecto activo:

```powershell
python -m src.experiments.evaluate_dense_text2trade `
  --evalset data\processed\evalset_v0.1.csv `
  --artifact-dir data\processed\indexes\text2trade_nandina8_v1 `
  --output-dir outputs\evaluation\text2trade_dense_eval_v0.1 `
  --k-list 1,3,5,10 `
  --retrieval-depth 10
```

Comparacion contra BM25:

```powershell
python -m src.analysis.compare_bm25_dense `
  --bm25-metrics outputs\evaluation\bm25_eval_v0.1\metrics.json `
  --bm25-results outputs\evaluation\bm25_eval_v0.1\results.csv `
  --dense-metrics outputs\evaluation\text2trade_dense_eval_v0.1\metrics.json `
  --dense-results outputs\evaluation\text2trade_dense_eval_v0.1\results.csv `
  --output-dir outputs\evaluation\text2trade_dense_eval_v0.1
```

## Outputs regenerables

Los resultados se generan bajo:

```text
outputs/evaluation/text2trade_dense_eval_v0.1/
```

Archivos:

- `results.csv`
- `metrics.json`
- `summary.md`
- `comparison_bm25_dense.json`
- `comparison_bm25_dense.md`

Estos outputs son regenerables y permanecen ignorados por Git.

## Resultados dense

Sobre 600 casos del evalset final v0.1:

| Metrica | Valor |
|---|---:|
| Top-1 NANDINA8 | 0.0000 |
| Top-3 NANDINA8 | 0.0000 |
| Top-5 NANDINA8 | 0.0033 |
| Top-10 NANDINA8 | 0.0050 |
| MRR | 0.0010 |
| Top-10 HS4 | 0.0117 |
| Top-10 HS2 | 0.0467 |
| Casos con cero resultados | 0 |
| Casos sin match Top-10 | 597/600 |

El evalset conserva 599 casos con `regimen=10` y 1 caso con `regimen=12`; se reporta como alerta metodologica sin modificar el dataset.

## Comparacion contra BM25

| Metrica | BM25 | Dense | Delta dense-BM25 |
|---|---:|---:|---:|
| Top-1 NANDINA8 | 0.0050 | 0.0000 | -0.0050 |
| Top-3 NANDINA8 | 0.0433 | 0.0000 | -0.0433 |
| Top-5 NANDINA8 | 0.0483 | 0.0033 | -0.0450 |
| Top-10 NANDINA8 | 0.0517 | 0.0050 | -0.0467 |
| MRR | 0.0290 | 0.0010 | -0.0281 |
| Top-10 HS4 | 0.1933 | 0.0117 | -0.1817 |
| Top-10 HS2 | 0.3800 | 0.0467 | -0.3333 |

Casos Top-10:

- Ganados por dense: 3.
- Perdidos por dense: 31.
- Ambos fallan: 566.
- Ambos aciertan: 0.

## Interpretacion metodologica

Text2Trade dense por fuerza bruta no mejora el baseline BM25 en este evalset. El resultado sugiere una desalineacion entre las descripciones comerciales SUNAT del evalset y el espacio semantico/documental representado por los embeddings NANDINA disponibles.

Este resultado no descarta variantes posteriores. Puede ser necesario explorar re-ranking, query rewriting, enriquecimiento de consultas o un flujo LLM+RAG auditado, pero esas alternativas requieren evaluaciones separadas y no se concluyen en esta subfase.

## Limitaciones

- `hnsw.index` esta ausente; no se reproduce el backend HNSW declarado historicamente.
- La evaluacion usa fuerza bruta sobre `vectors.npy`, no HNSW.
- La corrida depende del modelo local guardado en `data/processed/indexes/text2trade_nandina8_v1/model/`.
- El evalset tiene 1 caso con `regimen=12`; se mantiene sin cambios.
- No se ejecuto LLM.
- `hnswlib` no fue necesario para esta evaluacion y no quedo instalado en el `.venv`.
