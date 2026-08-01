# Piloto experimental offline LLM+RAG para recomendacion auditable de subpartidas NANDINA

Repositorio de investigacion aplicada para evaluar un piloto offline de gestion de informacion documental orientado a la recomendacion auditable de subpartidas NANDINA. El sistema no emite clasificacion oficial y no reemplaza la revision de un especialista; produce candidatos, evidencias y explicaciones trazables para apoyar la decision humana.

El alcance experimental vigente es `Clase = 87`, construido desde la fuente local `data_aduanas`. La arquitectura final usa recuperacion historica como ranking principal, evidencia normativa como trazabilidad y un LLM local solo para explicar el Top-3 ya recuperado.

## Resumen

El problema abordado es la dificultad de recomendar subpartidas NANDINA a partir de descripciones comerciales de mercancias, manteniendo trazabilidad hacia precedentes y evidencia documental. Se evaluaron distintas estrategias de recuperacion y uso de LLM en un entorno offline:

- BM25 normativo plano.
- Dense retrieval Text2Trade por fuerza bruta.
- BM25 normativo jerarquico.
- BM25 dual protegido.
- Candidate pool normativo.
- Recuperacion historica basada en ejemplos etiquetados.
- Pool hibrido historico + normativo.
- LLM como re-ranker diagnostico.
- LLM como generador de explicacion auditable del Top-3 fijo.

El hallazgo central es claro: para `data_aduanas` clase 87, la recuperacion historica real domina el ranking operativo. El corpus normativo aporta trazabilidad y respaldo documental, pero no alcanza por si solo la calidad necesaria para ser el recuperador principal. El LLM no mejoro el ranking cuando se uso como re-ranker; su uso defendible en este piloto es explicar candidatos ya recuperados, sin clasificar ni reordenar.

## Framework experimental

![Framework RAG explicativo y auditable](data/Framework%20RAG.png)

**Figura 1. Framework RAG explicativo y auditable usado en el piloto.** La descripcion comercial de una DAM/serie se normaliza y se convierte en objeto de consulta. El ranking principal se genera con BM25 sobre un banco historico de 3,000 casos etiquetados. En paralelo, el corpus normativo NANDINA se consulta para recuperar evidencia documental y contexto jerarquico. El constructor de contexto RAG recibe el Top-3 fijo, sus precedentes historicos y la evidencia normativa asociada. Luego un LLM local genera una justificacion controlada, sin clasificar desde cero y sin reordenar los candidatos. La salida final es una recomendacion auditable Top-3 con evidencia, nivel de soporte, comparacion y advertencia de revision experta.

La figura debe leerse como una arquitectura de apoyo a auditoria, no como un sistema automatico de clasificacion oficial. El punto critico es que el LLM esta despues de la recuperacion: explica candidatos ya encontrados por el sistema, pero no decide libremente una NANDINA.

## Pregunta Experimental

La pregunta operativa del piloto es:

> Puede una arquitectura offline basada en recuperacion documental, banco historico y LLM local producir recomendaciones NANDINA trazables y auditables a partir de descripciones comerciales?

La evaluacion se separo en dos problemas:

1. **Recuperacion:** verificar si la NANDINA esperada aparece en el ranking o en el pool de candidatos.
2. **Auditabilidad:** verificar si el sistema puede explicar un Top-3 fijo usando evidencia historica y normativa, sin inventar codigos ni alterar el ranking.

## Materiales

### Fuente data_aduanas

La fuente metodologica principal es `data_aduanas`, derivada de un Excel local de DAM/series:

```text
data/Series - Descripciones.xlsx
```

Este Excel no se versiona en Git. El parser normaliza el formato por bloques de DAM y genera una tabla con una fila por serie. El identificador unico experimental se construye como concatenacion de declaracion y serie (`id_unico`).

La capa normalizada intermedia queda en:

```text
data/interim/sunat_series_descripciones_normalized.csv
data/interim/sunat_series_descripciones_normalized.xlsx
data/interim/sunat_series_descripciones_normalized_metadata.json
```

Estos artefactos intermedios son regenerables y no son la fuente metodologica final. La fuente final de evaluacion son los splits procesados.

### Splits clase 87

La actualizacion metodologica principal usa solo `Clase = 87`. Los splits finales son:

```text
data/processed/data_aduanas_historico_clase87_v0.1.csv
data/processed/data_aduanas_devset_clase87_v0.1.csv
data/processed/data_aduanas_evalset_clase87_v0.1.csv
data/processed/data_aduanas_splits_clase87_v0.1_metadata.json
```

Conteos finales:

| Split | Filas | NANDINAS distintas | Uso |
| --- | ---: | ---: | --- |
| Historico | 3,000 | 69 | Banco de precedentes para recuperacion historica |
| Desarrollo | 100 | 44 | Ajustes exploratorios y pruebas cortas |
| Evaluacion | 1,006 | 62 | Evaluacion final clase 87 |

Criterios principales de curacion:

- Mantener solo `Clase = 87`.
- Exigir `id_unico`, `DECLARACION`, `SERIE`, `NANDINA` valida de 8 digitos y descripcion concatenada no vacia.
- Preservar columnas de descripcion por linea: `DESCRIPCION DE MERCANCIAS 1` a `DESCRIPCION DE MERCANCIAS 5`.
- Construir `DESCRIPCION DE MERCANCIAS CONCATENADA` a partir de las lineas reales disponibles.
- Excluir encabezados DAM que aparecian accidentalmente en zonas descriptivas, por ejemplo `REGISTRO DE ADUANAS`, `DECLARACION`, `FECHA NUMERACION`, `IDENTIFICACION`, `TRANSACCION`, `BASE IMPONIBLE` y `LIQUIDACION DEL ADEUDO`.
- Colapsar duplicados exactos por `id_unico` y excluir grupos conflictivos.
- Evitar solapamiento de `id_unico` entre historico, desarrollo y evaluacion.

Resultado de duplicados en la corrida v0.1:

| Tipo | Conteo |
| --- | ---: |
| Filas clase 87 de entrada | 4,232 |
| Filas curadas finales | 4,106 |
| Grupos duplicados exactos | 102 |
| Filas excedentes por duplicado exacto | 114 |
| Grupos conflictivos | 6 |
| Filas excluidas por conflicto | 12 |

### Corpus normativo NANDINA

El corpus normativo sirve para recuperacion documental, trazabilidad y evidencia. No es el ranking principal final.

Artefactos principales:

```text
data/processed/corpus_rag_v1_index.jsonl
data/processed/corpus_nandina_hierarchical_v0.1.jsonl
data/processed/indexes/bm25_nandina8.pkl
data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl
```

Durante el experimento se detecto que el corpus plano tenia descripciones demasiado cortas o genericas, por ejemplo textos como `Los demas` o `Partes`. Por eso se construyo una version jerarquica autocontenida que agrega contexto de niveles superiores. Esa mejora aumenta cobertura normativa, pero no convierte al corpus normativo en recuperador principal frente al banco historico.

### Modelo LLM

El LLM usado en las fases de diagnostico y explicacion fue:

```text
qwen2.5:7b-instruct via Ollama local
```

Controles metodologicos:

- Sin OpenAI.
- Sin APIs remotas.
- Sin servicios con costo.
- Temperatura controlada en las corridas documentadas.
- El LLM no recibe la etiqueta esperada.
- El LLM no puede proponer codigos fuera del Top-3 enviado.
- El LLM no reordena candidatos en la fase final de explicacion.

## Metodos

### 1. Normalizacion de data_aduanas

El Excel fuente tiene informacion de cabecera DAM y detalle de series. El parser transforma ese formato por bloques en una tabla normalizada, una fila por serie, conservando las etiquetas originales como columnas cuando corresponden.

Script:

```text
src/ingestion/sunat_series_parser.py
```

Comando base:

```powershell
.\.venv\Scripts\python.exe -m src.ingestion.sunat_series_parser `
  --input "data\Series - Descripciones.xlsx" `
  --output-csv data\interim\sunat_series_descripciones_normalized.csv `
  --output-xlsx data\interim\sunat_series_descripciones_normalized.xlsx `
  --metadata data\interim\sunat_series_descripciones_normalized_metadata.json `
  --label-audit outputs\audits\data_aduanas_ingestion_v0.1\label_audit.csv `
  --duplicate-audit outputs\audits\data_aduanas_ingestion_v0.1\duplicate_audit.csv `
  --overwrite
```

### 2. Construccion de splits

Script:

```text
src/evaluation/build_data_aduanas_splits.py
```

Comando reproducible:

```powershell
.\.venv\Scripts\python.exe -m src.evaluation.build_data_aduanas_splits `
  --input data\interim\sunat_series_descripciones_normalized.csv `
  --output-dir data\processed `
  --scope-class 87 `
  --historical-size 3000 `
  --dev-size 100 `
  --seed 2026 `
  --overwrite
```

Si se desea regenerar la capa normalizada desde el Excel local antes del split:

```powershell
.\.venv\Scripts\python.exe -m src.evaluation.build_data_aduanas_splits `
  --regenerate-normalized `
  --source-xlsx "data\Series - Descripciones.xlsx" `
  --input data\interim\sunat_series_descripciones_normalized.csv `
  --output-dir data\processed `
  --scope-class 87 `
  --historical-size 3000 `
  --dev-size 100 `
  --seed 2026 `
  --overwrite
```

### 3. Recuperacion normativa

Se evaluaron recuperadores sobre el corpus NANDINA:

- BM25 plano.
- BM25 jerarquico.
- BM25 dual protegido.
- Candidate pool normativo.
- Dense Text2Trade por fuerza bruta.

El objetivo fue medir si la NANDINA esperada aparece en el ranking normativo. La conclusion fue que lo normativo aporta trazabilidad, pero tiene baja exactitud temprana como ranking principal.

Scripts principales:

```text
src/experiments/evaluate_bm25_data_aduanas.py
src/experiments/evaluate_dense_text2trade_data_aduanas.py
src/analysis/compare_bm25_dense_data_aduanas.py
src/experiments/evaluate_bm25_hierarchical_data_aduanas.py
src/experiments/build_candidate_pool_data_aduanas.py
```

### 4. Recuperacion historica

La recuperacion historica usa el split historico como banco de precedentes etiquetados y evalua contra el split de evaluacion sin fuga por `id_unico`.

Script:

```text
src/experiments/evaluate_historical_retrieval_data_aduanas.py
```

La consulta principal es la descripcion comercial concatenada de la serie. El metodo recupera descripciones historicas similares y deduplica candidatos por NANDINA para producir un ranking de codigos.

### 5. Pool hibrido historico + normativo

El pool hibrido conserva el historico como ranking temprano y agrega evidencia normativa como respaldo. La estrategia recomendada es:

```text
historical_with_normative_backfill_if_missing_code
```

Script:

```text
src/experiments/build_hybrid_pool_data_aduanas.py
```

Decision: el historico domina el ranking; lo normativo entra como backfill, trazabilidad y evidencia documental, sin desplazar candidatos historicos tempranos.

### 6. LLM como re-ranker diagnostico

Se probo LLM para reordenar candidatos sobre una muestra de 20 casos. El resultado fue negativo: degrado Top-1 y MRR frente al ranking original enviado. Por eso no se escalo como componente del pipeline.

Documento:

```text
docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md
```

### 7. LLM como explicador auditable Top-3

El rol final del LLM es generar explicaciones auditables sobre el Top-3 fijo. El LLM recibe:

- descripcion de entrada;
- tres candidatos ya recuperados;
- evidencia historica por candidato;
- evidencia normativa por candidato;
- reglas anti-invencion;
- instruccion explicita de no clasificar, no agregar codigos y no reordenar.

Prompts y scripts:

```text
src/llm/explain_top3_nandina_prompt_v0.2.md
src/llm/explain_top3_nandina_prompt_v0.3.md
src/experiments/build_llm_explanation_top3_audit_sample.py
src/experiments/run_llm_explanation_top3_audit_sample.py
src/experiments/evaluate_llm_explanation_top3_audit_sample.py
src/experiments/render_llm_explanation_audit_cards.py
```

La fase 10D mejora el diseno de ficha con tono prudente, deteccion de evidencia normativa generica y campo de revision experta. No cambia metricas de recuperacion.

## Metricas

Las metricas de recuperacion usadas son:

| Metrica | Interpretacion |
| --- | --- |
| Top-1 | La NANDINA esperada aparece en la primera posicion |
| Top-3 | La NANDINA esperada aparece dentro de los tres primeros candidatos |
| Top-10 | La NANDINA esperada aparece dentro de los diez primeros candidatos |
| Recall@100 | La NANDINA esperada aparece dentro de los primeros 100 candidatos |
| Recall@200 | La NANDINA esperada aparece dentro de los primeros 200 candidatos |
| MRR | Media del reciproco del rank correcto |
| Partida@100 | Coincidencia por los primeros 4 digitos dentro del Top-100 |
| Sub Partida@100 | Coincidencia por los primeros 6 digitos dentro del Top-100 |
| Clase@100 | Coincidencia por los primeros 2 digitos dentro del Top-100 |

Las metricas de auditabilidad LLM usadas son:

| Metrica | Interpretacion |
| --- | --- |
| JSON valido | La respuesta cumple formato JSON esperado |
| Ranking preservado | El LLM conserva el Top-3 y su orden |
| Sin codigos fuera del pool | El LLM no inventa candidatos |
| Evidencia historica citada | Cada candidato cita evidencia historica disponible |
| Evidencia normativa citada | Cada candidato cita evidencia normativa disponible |
| Score de auditabilidad | Puntaje agregado de controles estructurales |

## Resultados

### Comparacion integrada

| Metodo | Tipo | n | Top-1 | Top-10 | Recall@100 | Recall@200 | MRR | Decision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| BM25 normativo plano clase 87 | Normativo | 1,006 | 0.0229 | 0.0467 | 0.0626 | NA | 0.0312 | Baseline auditable, no ranking principal |
| Dense Text2Trade clase 87 | Denso | 1,006 | 0.0000 | 0.0000 | 0.0010 | NA | 0.0000 | No se incorpora al pipeline exacto |
| BM25 jerarquico clase 87 | Normativo | 1,006 | 0.0249 | 0.0497 | 0.3449 | NA | 0.0385 | Respaldo normativo y trazabilidad |
| BM25 dual protegido clase 87 | Normativo | 1,006 | 0.0239 | 0.0487 | 0.1948 | NA | 0.0340 | Fuente auxiliar, no principal |
| Candidate pool normativo | Normativo | 1,006 | NA | 0.0497 | 0.3489 | 0.6292 | Respaldo documental |
| Recuperacion historica real | Historico | 1,006 | 0.8628 | 0.9801 | 1.0000 | NA | 0.9062 | Ranking operativo principal |
| Pool hibrido historico + normativo | Hibrido | 1,006 | 0.8628 | 0.9801 | 1.0000 | 1.0000 | 0.9062 | Estrategia recomendada |
| LLM re-ranker | LLM ranking | 20 | 0.2000 | 0.5000 | NA | NA | 0.3083 | Resultado negativo, no escalar |
| LLM explicacion Top-3 | LLM explicacion | 50 | NA | NA | NA | NA | NA | Explicador auditable |

### Resultado LLM explicativo

En la fase 10B, sobre 50 casos:

| Control | Resultado |
| --- | ---: |
| JSON valido | 1.0000 |
| Top-3 completo | 1.0000 |
| Ranking preservado | 1.0000 |
| Sin codigos fuera del pool | 1.0000 |
| Evidencia historica citada por candidato | 1.0000 |
| Evidencia normativa citada por candidato | 1.0000 |
| Comparacion Top-3 presente | 1.0000 |
| Advertencia final presente | 1.0000 |
| Score promedio de auditabilidad | 0.9520 |

La revision cualitativa 10C confirmo utilidad para auditoria humana, pero detecto tres cautelas: evidencia normativa generica, predominio de evidencia historica y tono demasiado decisivo en algunas conclusiones. La fase 10D corrigio el diseno de prompt, rubrica y ficha para incorporar prudencia y revision experta.

## Validacion de Hipotesis

| Hipotesis | Estado | Evidencia principal |
| --- | --- | --- |
| La arquitectura mejora la recuperacion frente a baselines normativos | Respaldada | Historico/hibrido `Recall@100 = 1.0000` frente a pool normativo `Recall@100 = 0.3489` |
| El banco historico es util para recomendacion NANDINA | Respaldada | Historico `Top-1 = 0.8628`, `Top-10 = 0.9801`, `MRR = 0.9062` |
| El corpus normativo jerarquico es util | Parcialmente respaldada | Mejora cobertura normativa, pero no ranking temprano suficiente |
| El LLM mejora como re-ranker | No respaldada | El re-ranking LLM degrada Top-1 y MRR en muestra diagnostica |
| El LLM sirve como explicador auditable | Respaldada | JSON valido, ranking preservado y evidencia citada en 50/50 casos |
| El enfoque RAG aporta trazabilidad | Respaldada | Se separan precedentes historicos, evidencia normativa y justificacion controlada |

## Como Reproducir

### 1. Preparar entorno

Requiere Python 3.10. En Windows:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
C:\Users\Vladimir\AppData\Local\Programs\Python\Python310\python.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Nota: `hnswlib` puede fallar en Windows si no estan instaladas las Microsoft C++ Build Tools. Para las evaluaciones ya cerradas, Dense Text2Trade se ejecuto por fuerza bruta y no requiere reconstruir HNSW.

### 2. Ejecutar smoke test BM25

```powershell
.\.venv\Scripts\python.exe -m src.experiments.smoke_test --top-n 3
```

### 3. Regenerar splits data_aduanas

Si ya existe la capa normalizada:

```powershell
.\.venv\Scripts\python.exe -m src.evaluation.build_data_aduanas_splits `
  --input data\interim\sunat_series_descripciones_normalized.csv `
  --output-dir data\processed `
  --scope-class 87 `
  --historical-size 3000 `
  --dev-size 100 `
  --seed 2026 `
  --overwrite
```

Si se parte del Excel local:

```powershell
.\.venv\Scripts\python.exe -m src.evaluation.build_data_aduanas_splits `
  --regenerate-normalized `
  --source-xlsx "data\Series - Descripciones.xlsx" `
  --input data\interim\sunat_series_descripciones_normalized.csv `
  --output-dir data\processed `
  --scope-class 87 `
  --historical-size 3000 `
  --dev-size 100 `
  --seed 2026 `
  --overwrite
```

### 4. Reproducir evaluaciones principales

```powershell
.\.venv\Scripts\python.exe -m src.experiments.evaluate_bm25_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_dense_text2trade_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_bm25_hierarchical_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.build_candidate_pool_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_historical_retrieval_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.build_hybrid_pool_data_aduanas
```

### 5. Reproducir evaluacion final integrada

La evaluacion final integrada no reejecuta LLM ni reentrena modelos. Consolida outputs existentes.

```powershell
.\.venv\Scripts\python.exe -m src.analysis.build_integrated_final_evaluation
```

Salidas:

```text
outputs/evaluation/integrated_final_evaluation_v0.1/integrated_metrics.json
outputs/evaluation/integrated_final_evaluation_v0.1/integrated_metrics.csv
outputs/evaluation/integrated_final_evaluation_v0.1/integrated_summary.md
outputs/evaluation/integrated_final_evaluation_v0.1/hypothesis_validation_matrix.csv
outputs/evaluation/integrated_final_evaluation_v0.1/hypothesis_validation_matrix.md
outputs/evaluation/integrated_final_evaluation_v0.1/experimental_decisions_timeline.csv
```

Documento final:

```text
docs/evaluacion_final_integrada_v0.1.md
```

### 6. Reproducir explicacion LLM Top-3

Esta parte requiere Ollama local y el modelo `qwen2.5:7b-instruct` instalado. No usa OpenAI ni APIs remotas.

```powershell
ollama pull qwen2.5:7b-instruct
```

Scripts principales:

```powershell
.\.venv\Scripts\python.exe -m src.experiments.build_llm_explanation_top3_audit_sample
.\.venv\Scripts\python.exe -m src.experiments.run_llm_explanation_top3_audit_sample
.\.venv\Scripts\python.exe -m src.experiments.evaluate_llm_explanation_top3_audit_sample
.\.venv\Scripts\python.exe -m src.experiments.render_llm_explanation_audit_cards
```

Outputs regenerables:

```text
outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/
```

## Estructura del Repositorio

```text
.
|-- data/
|   |-- external/       # referencias externas locales
|   |-- interim/        # tablas intermedias regenerables
|   |-- processed/      # splits, corpus e indices versionables o regenerables
|   |-- raw/            # insumos locales si aplica
|   |-- Framework RAG.png
|   `-- Series - Descripciones.xlsx   # fuente local no versionada
|-- docs/              # protocolos, informes, manifiestos y fichas metodologicas
|-- notebooks/         # exploracion previa
|-- outputs/           # resultados regenerables ignorados por Git
|-- Referencias/       # bibliografia local no versionada
|-- src/
|   |-- analysis/       # diagnosticos, comparaciones y evaluacion integrada
|   |-- corpus/         # construccion y auditoria de corpus
|   |-- evaluation/     # validacion y splits
|   |-- experiments/    # scripts de corrida experimental
|   |-- ingestion/      # parser data_aduanas
|   |-- llm/            # prompts LLM
|   |-- retrieval/      # recuperadores BM25/dense
|   `-- bm25_index.py
|-- requirements.txt
`-- README.md
```

## Artefactos Principales

| Artefacto | Rol |
| --- | --- |
| `docs/protocolo_experimental_v0.1.md` | Protocolo experimental general |
| `docs/manifest_artifacts_v0.1.json` | Manifiesto machine-readable de artefactos |
| `docs/manifiesto_artefactos_v0.1.md` | Manifiesto narrativo de artefactos |
| `docs/evaluacion_final_integrada_v0.1.md` | Cierre integrado de resultados e hipotesis |
| `docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md` | Evaluacion del pool historico + normativo |
| `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md` | Evaluacion formal de explicaciones Top-3 |
| `docs/revision_cualitativa_fichas_auditables_v0.1.md` | Revision cualitativa de fichas |
| `docs/mejora_ficha_auditable_llm_top3_v0.1.md` | Mejora 10D del diseno auditable |
| `src/analysis/build_integrated_final_evaluation.py` | Script reproducible de evaluacion final integrada |

## Politica de Versionado

Versionado en Git:

- scripts;
- protocolos;
- documentos metodologicos;
- splits procesados necesarios para reproducibilidad;
- manifiestos;
- imagen del framework si se desea que el README renderice en GitHub.

No versionado por defecto:

- `outputs/`, porque son regenerables;
- `.venv/`, porque depende del entorno local;
- `data/interim/`, salvo decision metodologica explicita;
- `data/Series - Descripciones.xlsx`, por ser fuente local;
- `Referencias/`, por contener bibliografia local pesada.

## Limitaciones

- El alcance final es `Clase = 87`; los resultados no deben generalizarse automaticamente a todas las clases NANDINA.
- El excelente desempeno historico depende de que existan precedentes etiquetados en el banco historico.
- Falta una validacion temporal o externa para medir desempeno ante codigos ausentes o cambios de distribucion.
- El corpus normativo mejora trazabilidad, pero no sustituye criterio legal ni revision experta.
- El LLM explica candidatos recuperados; no debe usarse como clasificador oficial.
- La salida es una recomendacion auditable, no una declaracion aduanera ni una decision vinculante.

## Estado del Piloto v0.1

El piloto experimental offline v0.1 esta cerrado tecnicamente. La decision metodologica final es:

1. Usar recuperacion historica como ranking operativo principal.
2. Usar corpus normativo jerarquico como evidencia, trazabilidad y respaldo.
3. Usar LLM local solo para generar explicaciones auditables del Top-3 fijo.
4. Mantener revision experta humana como cierre obligatorio.

Queda pendiente, para una etapa posterior, empaquetar la reproducibilidad en un comando unico, crear un tag Git `v0.1-piloto` y preparar la redaccion final de tesis/articulo.
