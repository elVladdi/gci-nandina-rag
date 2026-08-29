# EXP-04 Fase B - BM25 normativo plano data_aduanas clase 87 v0.2

## Alcance

Se evaluo exclusivamente BM25 normativo plano sobre el evalset data_aduanas clase 87 v0.2. No se ejecuto BM25 jerarquico, esquema dual, candidate pool, Text2Trade, integracion, RAG, reranking LLM ni explicador LLM.

## Corpus normativo plano

- Corpus: `data/processed/corpus_rag_v1_index.jsonl`.
- Corpus SHA-256: `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- Indice: `data/processed/indexes/bm25_nandina8.pkl`.
- Indice SHA-256: `fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b`.
- Documentos NANDINA-8 indexados: 7644.
- Texto indexado: titulo + texto_index, with texto fallback during index build.

## Evalset

- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.2.csv`.
- Evalset SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- Casos evaluados: 1056.
- Query: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta: `NANDINA`.

## Resultado global

| Metrica | Numerador | Denominador | Valor |
| --- | ---: | ---: | ---: |
| mrr | 44.66596703438809 | 1056 | 0.042297 |
| top_1 | 29 | 1056 | 0.027462 |
| top_3 | 54 | 1056 | 0.051136 |
| top_5 | 65 | 1056 | 0.061553 |
| top_10 | 69 | 1056 | 0.065341 |
| top_50 | 74 | 1056 | 0.070076 |
| recall_at_50 | 74 | 1056 | 0.070076 |
| recall_at_100 | 75 | 1056 | 0.071023 |
| partida_at_10 | 104 | 1056 | 0.098485 |
| sub_partida_at_10 | 76 | 1056 | 0.071970 |
| clase_at_10 | 420 | 1056 | 0.397727 |
| partida_at_50 | 185 | 1056 | 0.175189 |
| sub_partida_at_50 | 89 | 1056 | 0.084280 |
| clase_at_50 | 770 | 1056 | 0.729167 |
| partida_at_100 | 220 | 1056 | 0.208333 |
| sub_partida_at_100 | 99 | 1056 | 0.093750 |
| clase_at_100 | 806 | 1056 | 0.763258 |

## Cobertura normativa

- Codigos eval cubiertos por corpus: 42/42.
- Casos eval cubiertos por corpus: 1056/1056.
- Casos sin cobertura normativa: 0.
- Casos con codigo en corpus pero no recuperado Top-50: 982.

## Compatibilidad con historico v0.2

- Mismo set case_id: True.
- Mismas etiquetas por case_id: True.
- Compatible: True.
