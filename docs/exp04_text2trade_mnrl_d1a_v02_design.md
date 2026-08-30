# EXP-04 Fase D: D1a Text2Trade-inspired MNRL v0.2

## Alcance y nomenclatura

D1a es una **adaptación local inspirada en Text2Trade**, no una reproducción íntegra del artículo. Conserva el bi-encoder, MNRL, negativos jerárquicos, cosine similarity y ranking NANDINA-8. Separa el MCD para una posible variante posterior D1b.

El paper de Ravi et al., *Text2Trade: A Semantic Search System with Monte Carlo Dropout Uncertainty Quantification for HS Code Retrieval*, usa MiniLM como base tras comparar MiniLM y MPNet; ajusta SBERT con MNRL y negativos jerárquicos, y recupera por coseno. Sus datos combinan CBP CROSS, EBTI y USTR, con 171,247 pares de entrenamiento y 4,924 HS-6; sus negativos priorizan mismo HS-4, luego capítulo, y finalmente aleatorios. El MCD se aplica con 50 pasadas y reranking `0.8 * avg_cos + 0.2 * top3_freq`, pesos seleccionados en su validación. Reporta Recall@1/3/5/10, nDCG@10 y MAP@10.

Fuente metodológica primaria: https://jacobhowardecon.github.io/docs/papers/Text2Trade.pdf

## Diferencias con la adaptación local

| Aspecto | Artículo original | D1a local |
|---|---|---|
| Unidad de código | HS-6 | NANDINA-8, Clase 87 |
| Datos | CBP CROSS, EBTI, USTR | histórico Aduanas v0.2 + corpus normativo congelado |
| Modelo base | MiniLM seleccionado entre bases evaluadas | `paraphrase-multilingual-MiniLM-L12-v2` local congelado; apropiado para texto comercial en español, sin afirmar ser el checkpoint original |
| Entrenamiento | MNRL + negativos jerárquicos | MNRL triplete con negativos jerárquicos deterministas |
| MCD | Sí, reranking e incertidumbre | No en D1a; reservado para D1b |
| Selección | validación del paper | configuración única fijada antes de entrenar; sin dev/eval para selección |

## Datos, leakage y positivos

Entrenamiento: `data/processed/data_aduanas_historico_clase87_v0.2.csv` con SHA-256 `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.

- 2,950 filas históricas, 28 DAM y 66 códigos NANDINA-8.
- Cada fila usa como query `DESCRIPCION DE MERCANCIAS CONCATENADA` y como positivo el documento normativo NANDINA-8 de su etiqueta.
- Las 2,950 etiquetas históricas tienen positivo en `corpus_rag_v1_index.jsonl`, SHA-256 `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0`.
- Hay 457 grupos de descripción histórica normalizada repetida (1,033 filas repetidas adicionales). No se deduplican para no alterar el banco aprobado; el batching evita repetir código positivo dentro de un batch cuando sea posible.
- Frente al evalset oficial v0.2 SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`, el histórico tiene cero solapamiento por DAM, `id_unico` y `case_id`. El evalset no entra en pares, negativos, configuración ni selección.

El devset v0.2 tiene 100 series, 6 DAM y 9 códigos, con 91% de sus series en una DAM. Por esa concentración no se usará para early stopping, búsqueda de hiperparámetros ni selección taxonómica. D1a tampoco usa métricas de evaluación durante entrenamiento.

## Texto normativo y negativos

Cada documento normativo se reconstruye determinísticamente desde el corpus congelado: `titulo.strip() + "\\n" + texto_index.strip()` y `strip()` exterior; si no hay título se usa solo el texto. La prioridad de campo es `texto_index`, `texto`, `text`, `content`, `descripcion`; no hay lowercase. Query y documento se truncan por el tokenizer a 128 tokens, lado derecho.

Por cada `case_id`, el negativo explícito se elige con SHA-256 del caso sobre el primer pool no vacío: (1) código histórico distinto con mismo HS-4, (2) código histórico distinto del mismo capítulo, (3) otro código histórico. Así los negativos provienen exclusivamente de las etiquetas históricas de entrenamiento y del corpus normativo congelado; no se consulta ninguna etiqueta del evalset.

## Configuración congelada D1a

La configuración canónica está en `src/configs/text2trade_mnrl_v0.2.json`:

- base local `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`;
- `MultipleNegativesRankingLoss`, cosine, escala 20;
- 1 época, batch 8, AdamW, learning rate `2e-5`, weight decay `0.01`, clipping de gradiente 1.0 y warmup lineal 10%;
- semilla 2026, CPU, float32, max sequence length 128, sin AMP;
- sin early stopping, sin MCD, sin ajuste ni selección con dev/eval.

La elección usa parámetros fijos del paper cuando están especificados y defaults técnicos de SentenceTransformers para MNRL. No se compararán variantes ni se ajustarán parámetros frente al evalset.

## Gates y salida prevista

Después del fine-tuning se reconstruirá un índice nuevo en `data/processed/indexes/text2trade_mnrl_nandina8_v0.2/`; D0 nunca se sobrescribe. Antes de evaluar los 1,056 casos se ejecutará una muestra determinística de integridad vectorial reconstruyendo documento→vector. Solo si ese gate pasa se calcularán Top-k, Recall, MRR y diagnósticos jerárquicos para D1a.

La evaluación comparará Historical BM25, Normative BM25 flat, Normative BM25 hierarchical, D0 pretrained dense SBERT baseline y D1a Text2Trade-inspired MNRL. MCD queda explícitamente fuera de esta tarea.
