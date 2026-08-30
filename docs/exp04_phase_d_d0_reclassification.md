# EXP-04 Fase D: reclasificación D0

## Estado

La corrida preservada en `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/` se denomina desde esta fase **D0 — pretrained dense SBERT baseline**. No debe presentarse como resultado final Text2Trade.

Sus outputs, hashes, métricas y auditoría se preservan sin modificar. El índice legado `data/processed/indexes/text2trade_nandina8_v1/index/vectors.npy` conserva SHA-256 `67cd07f96fe98712940db467ea2510018698e40e3b3a24e8478256e62e0f3773`.

## Motivos de no aceptación como Text2Trade final

1. La microauditoría D0 no pudo reconstruir los vectores con el modelo local declarado: 0 de 21 muestras coincidieron byte a byte; el coseno reconstruido/almacenado observado fue 0.1473237–0.7768146.
2. El pipeline D0 usa `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` como SBERT preentrenado, sin fine-tuning NANDINA ni Multiple Negatives Ranking Loss (MNRL).
3. Aunque el artefacto histórico registra configuración MCD, la corrida D0 usó una sola pasada determinista y no aplicó reranking MCD ni incertidumbre.
4. El `hnsw.index` histórico no está presente; D0 evaluó brute-force exacto sobre los vectores heredados.

Por ello, el **legacy dense index is not accepted as final Text2Trade artifact**.

## Evidencia preservada

- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/gate_d_vector_integrity_v0.2.json`
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/gate_d_vector_sample_check_v0.2.csv`
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/gate_d_retrieval_sample_v0.2.csv`
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/run_metadata.json`

D0 permanece únicamente como comparador histórico en la tabla A/B/C/D0/D1a.
