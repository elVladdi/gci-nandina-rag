# Inventario EXP-04 Fase A - BM25 historico v0.2

Este inventario continua los analisis EXP-01/EXP-03/EXP-02 y el addendum de soporte historico. Su alcance es deliberadamente estrecho: habilitar y documentar solo el rerun BM25 historico sobre `data_aduanas` clase 87 v0.2.

## Baseline autorizado

| Componente | Estado EXP-04 Fase A | Evidencia local |
| --- | --- | --- |
| Split historico v0.2 | Autorizado como corpus BM25 historico | `data/processed/data_aduanas_historico_clase87_v0.2.csv` |
| Evalset v0.2 | Autorizado como conjunto de evaluacion | `data/processed/data_aduanas_evalset_clase87_v0.2.csv` |
| Metadata split v0.2 | Requerida para hashes, conteos y configuracion | `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json` |
| Soporte por fila de evaluacion | Requerido para analisis por soporte historico | `outputs/audits/data_aduanas_splits_clase87_v0.2/historical_support_by_eval_row_v0.2.csv` |
| Duplicados exactos/cercanos | Requeridos para sensibilidad | `outputs/audits/data_aduanas_splits_clase87_v0.2/*duplicates*details_v0.2.csv` |
| Runner BM25 historico v0.1 | Usado solo como patron metodologico | `src/experiments/evaluate_historical_retrieval_data_aduanas.py` |
| Runner BM25 historico v0.2 | Nuevo runner aislado | `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py` |

## Componentes excluidos en esta fase

| Componente | Estado | Motivo |
| --- | --- | --- |
| BM25 normativo | No ejecutar | Fuera de alcance para Fase A historica |
| BM25 jerarquico | No ejecutar | Solo se reportan errores jerarquicos del Top-1 historico |
| Text2Trade / dense retrieval | No ejecutar | Fuera de alcance |
| Candidate pools / hybrid pools | No ejecutar | Fuera de alcance |
| RAG y reranking LLM | No ejecutar | Fuera de alcance y no reproducible sin otra fase |
| Explicador LLM | No ejecutar | Fuera de alcance |

## Gates implementados

- Hash historico v0.2: `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- Hash evalset v0.2: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- Conteos: 2950 historico, 1056 evaluacion, 42 NANDINA en evaluacion.
- `case_id` unico y con prefijo `DA-EVAL-V02-` en evaluacion.
- Cero solapamiento `id_unico` historico/evaluacion.
- 1056/1056 filas de evaluacion con soporte historico segun audit v0.2.
- `candidate_depth >= 50` para reportar Top-50.
- Flags explicitos `llm_used=False`, `text2trade_used=False`, `remote_api_used=False`, `normative_bm25_used_as_candidate_source=False`.

## Salidas esperadas

El runner produce `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/` con ranking completo, resumen por caso, metricas globales con numerador/denominador, distribucion de posicion, sensibilidad por soporte, sensibilidad por duplicados, errores jerarquicos Top-1, comparacion v0.1-v0.2 y metadata de ejecucion con hashes de outputs.