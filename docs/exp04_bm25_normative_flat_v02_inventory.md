# Inventario EXP-04 Fase B - BM25 normativo plano v0.2

Este inventario documenta la auditoria previa del pipeline BM25 normativo plano antes del rerun sobre el evalset `data_aduanas` Clase 87 v0.2.

## Pipeline existente

| Elemento | Estado |
|---|---|
| Script v0.1 | `src/experiments/evaluate_bm25_data_aduanas.py` |
| Modulo de carga/recuperacion | `src/retrieval/bm25.py` |
| Implementacion BM25 | `src/bm25_index.py` |
| Configuracion base | `src/configs/experiment_config.json` |
| Indice plano | `data/processed/indexes/bm25_nandina8.pkl` |
| Metadata del indice | `data/processed/indexes/bm25_nandina8_run_metadata.json` |
| Corpus plano | `data/processed/corpus_rag_v1_index.jsonl` |
| Output v0.1 preservado | `outputs/evaluation/bm25_data_aduanas_clase87_evalset_v0.1/` |
| Runner v0.2 | `src/experiments/evaluate_normative_bm25_flat_data_aduanas_v02.py` |

## Corpus normativo plano

- Ruta: `data/processed/corpus_rag_v1_index.jsonl`.
- SHA-256: `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- Fuente registrada: `NANDINA`.
- Version registrada: `Decision_885`.
- Registros totales: 7748.
- Unidad documental evaluada: filas `tipo = nandina_8`.
- Documentos NANDINA-8 indexados: 7644.
- Codigos NANDINA-8 unicos: 7644.
- Texto indexado por el constructor: `titulo + texto_index`, con fallback a `texto`.
- Campos observados: `chapter`, `codigo`, `doc_id`, `fuente`, `idioma`, `pagina_fin`, `pagina_inicio`, `section`, `texto`, `texto_index`, `tipo`, `titulo`, `version`.
- Parametros BM25 del indice: `k1 = 1.5`, `b = 0.75`.

## Query autorizada

La query se construye exclusivamente desde `DESCRIPCION DE MERCANCIAS CONCATENADA` del evalset v0.2. No usa NANDINA verdadera, DAM, SERIE, Top-3 historico, resultados previos ni campos derivados.

## Exclusiones Fase B

No se ejecutan en esta fase: BM25 normativo jerarquico, esquema dual protegido, candidate pool normativo, Text2Trade, integracion historico-normativa, RAG, reranking LLM ni explicador LLM.

## Guardas v0.2

- Evalset v0.2 SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- Corpus plano SHA-256: `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- Indice plano SHA-256: `fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b`.
- Configuracion base SHA-256: `107f200365ac34be02d04e51b7a4ecd5119b1d3f619752243b0d3405d20d0a9d`.
- Se bloquea cualquier input `v0.1` como entrada de Fase B; los outputs v0.1 solo pueden leerse como referencia historica, no como resultado final.