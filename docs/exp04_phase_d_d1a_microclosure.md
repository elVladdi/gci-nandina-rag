# EXP-04 Fase D / D1a: microcierre de Gate D

## Decisión

**GATE D APROBADO.** D1a es metodológicamente admisible como **B. Adaptación metodológica justificada por el comparador Text2Trade, pero no preespecificada en detalle**. No se cierra HE2: MCD y Fase E permanecen pendientes de una autorización posterior.

La conclusión B es deliberadamente más limitada que una preespecificación completa. El commit D1a fue creado después de observar D0, pero no hay evidencia de que se haya modificado la configuración D1a después de observar sus propios resultados v0.2. La autorización explícita para reconstruir Fase D permitió esa adaptación y fijó la prohibición de MCD, candidate pools y Fase E.

## Evidencia preexperimental y clasificación

Evidencia anterior a D0 (`9fcffa9`, 2026-08-29 23:21 -0500):

- [`notebooks/05_Text2Trade_Indexacion_NANDINA.ipynb`](../notebooks/05_Text2Trade_Indexacion_NANDINA.ipynb), introducido en `d73ff147` (2026-06-12), se describe como recuperación semántica densa inspirada en Text2Trade, con bi-encoder y una prueba MCD.
- El mismo notebook declara: "En Text2Trade el bi-encoder se fine-tunea. Aquí se inicia con un modelo preentrenado como baseline reproducible." Define además MCD con 50 pasadas y pesos `0.8`/`0.2`.
- [`docs/Proyecto_investigacion_Maestria_GCI.docx`](Proyecto_investigacion_Maestria_GCI.docx) fundamenta recuperación densa sobre consulta-descripción y documentos NANDINA, y justifica métricas Top-k; no define MNRL, dataset de entrenamiento, negativos, época, tasa de aprendizaje ni selección de checkpoint.
- La búsqueda en el árbol `9fcffa9^` para `MultipleNegativesRankingLoss`, `MNRL`, `hard negative` y `fine-tuning` solo encontró la nota del notebook sobre que Text2Trade fine-tunea el bi-encoder; no había pipeline local MNRL detallado.

Por tanto, el repositorio ya distinguía el enfoque Text2Trade del baseline SBERT congelado, pero D1a no era una receta local congelada antes de D0. La adaptación fue definida en `fe20ecb` (2026-08-29 23:57 -0500) y el pipeline en `c5c1544` (2026-08-30 00:02 -0500), ambos posteriores a D0 y previos al entrenamiento D1a. Esto descarta A, pero no C: la adaptación conserva elementos publicados del comparador (bi-encoder MiniLM, MNRL, negativos jerárquicos y coseno), declara sus diferencias y no reclama ser el checkpoint o la réplica completa del paper.

## Ausencia de tuning sobre eval

La configuración congelada [`src/configs/text2trade_mnrl_v0.2.json`](../src/configs/text2trade_mnrl_v0.2.json) tiene SHA-256 `d5bb787f726330285b1a3d85a2b370a7c37ee055c3d8904225a3b26f18c27254` y establece explícitamente `devset_used_for_training_or_selection=false` y `evalset_used_for_training_or_selection=false`.

- El evalset v0.2 (`3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`) no eligió modelo base, época, learning rate, batch size, negativos, checkpoint, pooling, max length, semilla ni variantes.
- El runner verifica el hash del evalset y los solapamientos por DAM, `id_unico` y `case_id`; carga el evalset exclusivamente para rechazar leakage. Los tres solapamientos fueron cero.
- No hubo búsqueda de hiperparámetros, early stopping, selección de checkpoint ni selección con devset. D1a ejecutó una única época y guardó el modelo final de esa época.
- Tras observar D0, la única decisión nueva fue sustituir el baseline no reproducible como comparador final por D1a MNRL. Su justificación es la auditoría D0: vectores heredados no reconstruibles y ausencia de fine-tuning/MNRL. No se usaron métricas D0 para elegir parámetros D1a.

## Configuración D1a exacta

| Campo | Valor |
|---|---|
| Base model | `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, copia local `data/processed/indexes/text2trade_nandina8_v1/model` |
| Estado | SBERT preentrenado local -> fine-tuned una vez para D1a; no checkpoint original Text2Trade |
| Train dataset | `data/processed/data_aduanas_historico_clase87_v0.2.csv` |
| Hash / tamaño | `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`; 2,950 filas; 66 códigos |
| Query | `DESCRIPCION DE MERCANCIAS CONCATENADA` |
| Positivo | documento normativo del código histórico: título + `texto_index`, omitiendo título vacío; 2,950/2,950 positivos presentes |
| Negativo | SHA-256 de `case_id` sobre primer pool no vacío: mismo HS-4 distinto, mismo capítulo distinto, otro código histórico; 2,875 HS-4 y 75 capítulo |
| Dev/eval usage | ninguno para entrenamiento, selección o early stopping |
| Loss | `MultipleNegativesRankingLoss`, coseno, escala 20 |
| Epochs / batch | 1 / 8, batches con código positivo único |
| Optimizer | AdamW, LR `2e-5`, weight decay `0.01`, gradient clipping `1.0` |
| Warmup | lineal, 10%, 60 de 608 pasos |
| Max sequence length | 128, truncamiento derecho |
| Semilla / device / dtype | 2026 / CPU / float32, AMP desactivado |
| Pooling / normalización / similitud | mean pooling, embeddings L2-normalized, producto punto equivalente a coseno |
| Checkpoint | modelo final de la única época; no se eligió checkpoint por dev/eval |

La pérdida registrada fue `3.7844367027282715` al inicio, `0.0044498443603515625` al final y media `1.3431913390951722`.

## Modelo e índice final

Modelo D1a local, no versionado por su tamaño total de 477,616,987 bytes:

| Archivo | Bytes | SHA-256 |
|---|---:|---|
| `models/text2trade_mnrl_v0.2/model.safetensors` | 470,637,416 | `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87` |
| `config.json` | 777 | `867cac582ca8ac9a39e1fd577d793a60089cf2786d86c547ad44c0a12be73b80` |
| `tokenizer.json` | 6,973,173 | `15e67157ec6fa47df5b142c36fbb0f3ea8e303a96de2e9bbb59b755c7cc46e49` |
| `tokenizer_config.json` | 649 | `ec1137c53aaa844aab218f337912175bbc7cd0e64ed0896a45d7f982af5c1c71` |
| `1_Pooling/config.json` | 94 | `bb80272f7adad76ce93073c25e18113ee66be1e91f60bcdd72aa41d05b28247e` |

El pooling final es `mean`, dimensión 384. El peso base era `7f4f89d628f87ade0e0b57c40affb6402cd77abc8110584d8d35dc86da514ee8`; el peso final anterior confirma una relación base -> fine-tuned verificable por hash, no solo por nombre.

Índice reconstruido desde el modelo final:

| Artefacto | Valor |
|---|---|
| Vectores | `data/processed/indexes/text2trade_mnrl_nandina8_v0.2/index/vectors.npy`; `137d8f28ed0cde0f4111a39b84aee04c514847e505594db77217bdd5a1fd5354`; `(7644, 384)`, `float32` |
| Docstore | `store/nandina8_docstore.jsonl`; `07589433dea72061480fdbf807c8c3ee3d1ada87631d4448b29974d754a9e948`; 7,644 documentos/códigos |
| Mapping | `index/id_map.json`; `5e4d85f2e1d92f14ef2eed2cfd3a4db2b300c6c88b6f5862197cfe56b52b604d`; mapeo uno a uno vector/documento/código |
| Corpus | `data/processed/corpus_rag_v1_index.jsonl`; `83768faae816b9d9b33a8fd36b73068d8b5f0b7a186e1c0f5b1c2c27580290f0` |

No se reutilizó el `vectors.npy` inválido de D0 (`67cd07f96fe98712940db467ea2510018698e40e3b3a24e8478256e62e0f3773`). D0 queda marcado como **INVALID AS FINAL TEXT2TRADE COMPARATOR** y no se usa para conclusiones finales.

## Gate de integridad vectorial

El gate previo a evaluación fue `PASS`: 21 muestras deterministas, coseno reconstruido/almacenado entre `0.999999887840059` y `1.0000001403452747`, diferencia absoluta máxima `1.1920928955078125e-07` y L2 máxima `4.3145173072568673e-07`. Hubo 9 coincidencias byte-a-byte y 12 diferencias float32 permitidas. El criterio fue coseno y máximo componente dentro de 8 epsilon float32 (`9.5367431640625e-07`). Esto demuestra compatibilidad modelo D1a -> índice D1a; no es la condición defectuosa de D0.

## Métricas D1a y distribución

Todos los valores proceden de `d1a_metrics.json` y del resumen de 1,056 casos ya existente; no se volvió a ejecutar retrieval.

| Métrica | Numerador / 1,056 | Valor |
|---|---:|---:|
| Top-1 | 0 | 0.0 |
| Top-3 | 4 | 0.003787878787878788 |
| Top-5 | 36 | 0.03409090909090909 |
| Top-10 | 165 | 0.15625 |
| Top-50 | 323 | 0.3058712121212121 |
| Recall@100 | 365 | 0.3456439393939394 |
| MRR@100 | 34.240088668205736 / 1,056 | 0.03242432639034634 |
| Recall@200 | 383 | 0.3626893939393939 |
| MRR@200 | 34.37125272378151 / 1,056 | 0.03254853477630825 |
| HS6@100 | 386 | 0.36553030303030304 |
| HS4@100 | 922 | 0.8731060606060606 |
| Chapter@100 | 1,035 | 0.9801136363636364 |
| HS6@200 | 410 | 0.38825757575757575 |
| HS4@200 | 1,018 | 0.9640151515151515 |
| Chapter@200 | 1,056 | 1.0 |

| Rango de referencia | Casos |
|---|---:|
| 1 | 0 |
| 2-3 | 4 |
| 4-5 | 32 |
| 6-10 | 129 |
| 11-50 | 158 |
| 51-100 | 42 |
| 101-200 | 18 |
| >200/no encontrado | 673 |
| **Total** | **1,056** |

## Comparación provisional A/B/C/D

`n/a` significa que ese output anterior no publicó esa métrica; no se infirió un valor.

| Estrategia | Top-1 | Top-10 | Top-50 | Recall@100 | MRR@100 | Recall@200 | MRR@200 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Historical BM25 | 0.509469696969697 | 0.8910984848484849 | 0.9914772727272727 | n/a | 0.6297077493524843 | n/a | n/a |
| Normative BM25 flat | 0.027462121212121212 | 0.06534090909090909 | 0.07007575757575757 | 0.07102272727272728 | 0.04229731726741296 | n/a | n/a |
| Normative BM25 hierarchical | 0.026515151515151516 | 0.06534090909090909 | 0.09090909090909091 | 0.10132575757575757 | 0.04334161160288281 | 0.3039772727272727 | 0.04334161160288281 |
| D0 pretrained dense baseline | 0.0 | 0.0 | 0.000946969696969697 | 0.003787878787878788 | 0.00006046196473541642 | 0.010416666666666666 | 0.00010693394691080449 |
| D1a Text2Trade-inspired MNRL | 0.0 | 0.15625 | 0.3058712121212121 | 0.3456439393939394 | 0.03242432639034634 | 0.3626893939393939 | 0.03254853477630825 |

D0 se conserva solo como línea histórica: **INVALID AS FINAL TEXT2TRADE COMPARATOR por índice histórico no reproducible**. D1a mejora sustancialmente su recall, pero no autoriza una conclusión sobre HE2 ni pasos posteriores.

## Tests y entorno

El HEAD auditado fue `cb72fab14fd806f87273c1e222d74f57cd04cd62`. En el entorno temporal externo `C:\Users\Vladimir\AppData\Local\Temp\exp04-d1a-tests-py312\Scripts\python.exe` se ejecutó:

```powershell
python -B -m unittest discover -s tests -v
```

Resultado: **90 tests in 5.097s, OK**. Incluye recomputación de métricas D1a desde trace, auditoría de leakage, hashes, reconstrucción de tres embeddings del índice final y validación A/B/C/D0/D1a.

| Uso | Runtime |
|---|---|
| Entrenamiento D1a | Python 3.10.11, Torch 2.12.0+cpu |
| Evaluación D1a | mismo runtime de la corrida (el metadata no registra versiones adicionales) |
| Tests finales | Python 3.12.13, NumPy 2.5.2, SentenceTransformers 6.0.0, Torch 2.13.0+cpu, Transformers 5.16.1 |

El `.venv` del proyecto y los `.venv` locales de referencia contienen `pyvenv.cfg` que apunta a `C:\Users\Vladimir\AppData\Local\Programs\Python\Python310\python.exe`; esa instalación ya no existe. El notebook histórico también menciona un entorno Conda `tesis-text2trade`, que tampoco está presente. Esto es un riesgo de environment drift para reproducción de entrenamiento, mitigado parcialmente por pesos, configuración, hashes, metadata y la verificación de reconstrucción de embeddings. El entorno temporal se creó desde el runtime portable de Codex y `requirements.txt`; está fuera de Git y no modifica los artefactos experimentales.

## Restricciones confirmadas

No se reentrenó, no se reconstruyeron embeddings, no se repitió retrieval, no se ejecutó MCD, candidate pools ni Fase E. Los artefactos grandes permanecen fuera de Git y no se usó Git LFS.
