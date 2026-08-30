# EXP-04 Fase D - Text2Trade dense v0.2 inventory

## Estado previo

EXP-04 Fases A, B y C permanecen congeladas. Este inventario identifica la implementacion densa antes de ejecutar Fase D sobre `data/processed/data_aduanas_evalset_clase87_v0.2.csv`.

## Implementacion existente

- Runner v0.1 historico: `src/experiments/evaluate_dense_text2trade.py`.
- Runner data_aduanas v0.1: `src/experiments/evaluate_dense_text2trade_data_aduanas.py`.
- Runner v0.2 creado para Fase D: `src/experiments/evaluate_dense_text2trade_data_aduanas_v02.py`.
- Modulo de retrieval: `src/retrieval/dense_text2trade.py`.
- Artefacto denso: `data/processed/indexes/text2trade_nandina8_v1/`.

## Identidad Text2Trade en este repositorio

El repositorio implementa una adaptacion local de Text2Trade: recuperacion semantica densa con bi-encoder SentenceTransformer preentrenado sobre documentos NANDINA-8 congelados. No se asume que todo el articulo Text2Trade este implementado. Monte Carlo Dropout aparece en `retrieval_config.json` y en el notebook historico, pero el retriever evaluable usa embeddings deterministas y no ejecuta MCD para esta comparacion.

- Referencia local: `Referencias/README.md` lista `Text2Trade. A semantic search system whith Monte Carlo Droput Uncertainty Quantification For HS Code Retrieval..pdf`.
- Notebook fuente historico: `notebooks/05_Text2Trade_Indexacion_NANDINA.ipynb`.
- Modelo: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.
- Revision Hugging Face: no registrada en metadata local; Fase D congela hashes de archivos locales del modelo.
- Embedding dimension: 384.
- Pooling: mean tokens (`1_Pooling/config.json`).
- Normalizacion: `normalize_embeddings=True`.
- Similarity metric: cosine via dot product sobre vectores normalizados.
- ANN configurado historicamente: hnswlib/cosine, M=64, ef_construction=200, ef_search=200.
- ANN usado en Fase D: ninguno; `hnsw.index` no existe fisicamente, se usa fuerza bruta sobre `vectors.npy`.

## Corpus denso

- Corpus fuente: `data/processed/corpus_rag_v1_index.jsonl`.
- Corpus fuente SHA-256: `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- Docstore: `data/processed/indexes/text2trade_nandina8_v1/store/nandina8_docstore.jsonl`.
- Docstore SHA-256: `acff90a10c3a0e52e8a8a6adbaf98fd747b76af01218acffcff00956952a5721`.
- Vectores: `data/processed/indexes/text2trade_nandina8_v1/index/vectors.npy`.
- Vectores SHA-256: `67cd07f96fe98712940db467ea2510018698e40e3b3a24e8478256e62e0f3773`.
- ID map SHA-256: `b9d526c66a61a3fc5aeb5209a9431ac74566eb1971418ea67b43fbd6e877e976`.
- Documentos indexados: 7644.
- Codigos NANDINA-8 unicos: 7644.
- Duplicados por codigo: 0.
- Unidad documental: un vector/documento por codigo NANDINA-8 unico.
- Texto indexado: `texto_index` del docstore congelado.
- Cobertura eval v0.2: 42/42 codigos, 1056/1056 casos.

## Evalset y query

- Evalset oficial: `data/processed/data_aduanas_evalset_clase87_v0.2.csv`.
- Evalset SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- Casos: 1056.
- Query: exclusivamente `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- No se incorpora NANDINA real, DAM, SERIE, case_id, resultados historicos, Top-3, BM25 plano/jerarquico ni etiquetas derivadas como texto semantico.

## Dependencias y entorno observado

- Python ejecutable: `.venv/Scripts/python.exe` sobre Python 3.10.11.
- Device observado: CPU.
- numpy: 2.2.6.
- torch: 2.12.0+cpu.
- sentence-transformers: 5.5.1.
- transformers: 5.12.1.
- tokenizers: 0.22.2.
- hnswlib: no importable en la venv actual; no se usa para Fase D.

## Salida esperada

`outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/`

No se sobrescriben outputs v0.1 ni Fases A/B/C. No se inicia Fase E.
