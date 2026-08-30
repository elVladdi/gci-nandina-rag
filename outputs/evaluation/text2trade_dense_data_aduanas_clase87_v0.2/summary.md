# EXP-04 Fase D - Text2Trade dense data_aduanas clase 87 v0.2

## Alcance

Se ejecuto exclusivamente Text2Trade / recuperacion densa sobre el evalset oficial v0.2. No se ejecutaron candidate pools, dual protegido, mezcla 70/30, union diagnostica, integracion historico-normativa, RAG, reranking LLM ni explicador LLM.

## Identidad Text2Trade implementada

- Adaptacion local: bi-encoder SentenceTransformer preentrenado sobre artefactos NANDINA-8 congelados.
- Modelo: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.
- Revision Hugging Face: no registrada en metadata local; se congela por hashes locales del modelo.
- Pooling: mean tokens.
- Normalizacion: embeddings normalizados.
- Similarity metric: cosine via dot product on normalized vectors.
- ANN: configuracion historica HNSW existe en metadata, pero `hnsw.index` no existe fisicamente; Fase D usa fuerza bruta sobre `vectors.npy`.
- Monte Carlo Dropout: aparece en `retrieval_config.json`, pero no forma parte de esta comparacion ejecutada; se uso encoding determinista.

## Corpus denso

- Corpus fuente: `data/processed/corpus_rag_v1_index.jsonl`.
- Corpus SHA-256: `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- Docstore: `data/processed/indexes/text2trade_nandina8_v1/store/nandina8_docstore.jsonl`.
- Docstore SHA-256: `acff90a10c3a0e52e8a8a6adbaf98fd747b76af01218acffcff00956952a5721`.
- Documentos indexados: 7644.
- Codigos NANDINA-8 unicos: 7644.
- Codigos eval cubiertos: 42/42.
- Casos eval cubiertos: 1056/1056.

## Metricas exactas

| Metrica | Numerador | Denominador | Valor |
| --- | ---: | ---: | ---: |
| Top-1 | 0 | 1056 | 0.000000000000 |
| Top-3 | 0 | 1056 | 0.000000000000 |
| Top-5 | 0 | 1056 | 0.000000000000 |
| Top-10 | 0 | 1056 | 0.000000000000 |
| Top-50 | 1 | 1056 | 0.000946969697 |
| Recall@100 | 4 | 1056 | 0.003787878788 |
| MRR@100 | 0.06384783476059974 | 1056 | 0.000060461965 |
| Recall@200 | 11 | 1056 | 0.010416666667 |
| MRR@200 | 0.11292224793780954 | 1056 | 0.000106933947 |

## Cobertura jerarquica diagnostica

- HS6@100: 35/1056 = 0.033143939394.
- HS4@100: 287/1056 = 0.271780303030.
- Chapter@100: 828/1056 = 0.784090909091.
- HS6@200: 148/1056 = 0.140151515152.
- HS4@200: 581/1056 = 0.550189393939.
- Chapter@200: 1027/1056 = 0.972537878788.

## Distribucion de posiciones

| Bucket | Cases |
| --- | ---: |
| 1 | 0 |
| 2-3 | 0 |
| 4-5 | 0 |
| 6-10 | 0 |
| 11-50 | 1 |
| 51-100 | 3 |
| 101-200 | 7 |
| >200_or_not_retrieved | 1045 |

## Estado Gate D

GATE D APROBADO
