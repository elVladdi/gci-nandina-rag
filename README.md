# Piloto experimental offline LLM+RAG para recomendación auditable de subpartidas NANDINA

Repositorio de investigación aplicada para evaluar un piloto offline de gestión de información documental orientado a la recomendación auditable de subpartidas NANDINA. El sistema no emite clasificación oficial y no reemplaza la revisión de un especialista; produce candidatos, evidencias y explicaciones trazables para apoyar la revisión humana.

## 1. Lectura correcta del proyecto

Este repositorio debe leerse en dos niveles:

1. **Proyecto de investigación**: documento académico inicial de maestría, concebido antes de la ejecución técnica. Define el problema, objetivos, hipótesis, variables, metodología offline, métricas y rúbrica de explicación auditable.
2. **Ejecución del piloto v0.1**: desarrollo técnico posterior registrado en este repositorio. Concreta decisiones metodológicas, corpus, scripts, evaluaciones, resultados, problemas encontrados y ajustes del flujo experimental.

La ejecución no cambia el núcleo del proyecto. Lo operacionaliza. El proyecto proponía una etapa de recuperación documental base para generar candidatos Top-N y un componente LLM+RAG para reordenar o explicar; la ejecución precisó qué técnicas funcionaban en el contexto disponible y cuáles no.

La decisión metodológica final del piloto v0.1 es:

- usar **recuperación histórica BM25** sobre precedentes etiquetados como ranking operativo principal;
- usar el **corpus normativo NANDINA** como evidencia, trazabilidad y respaldo documental;
- usar un **LLM local** solo para generar explicaciones auditables del Top-3 fijo;
- no usar el LLM como clasificador libre ni como re-ranker final;
- mantener la revisión experta como cierre obligatorio.

## 2. Alcance vigente del piloto v0.1

El proyecto de investigación fue formulado de manera general para subpartidas NANDINA de ocho dígitos. La ejecución técnica v0.1 se acotó a:

```text
Clase = 87
Fuente experimental = data_aduanas
Modo = offline
Salida = recomendación auditable Top-3
```

Este acotamiento permite cerrar un piloto reproducible y evaluable sin afirmar generalización automática a toda la NANDINA.

El sistema trabaja con descripciones comerciales de DAM/series y no con decisiones oficiales nuevas. La etiqueta de referencia se usa solo para evaluación offline.

## 3. Pregunta experimental operativa

> ¿Puede una arquitectura offline basada en recuperación documental, banco histórico y LLM local producir recomendaciones NANDINA trazables y auditables a partir de descripciones comerciales?

La evaluación se separó en dos problemas:

1. **Recuperación**: verificar si la NANDINA esperada aparece en el ranking o en el pool de candidatos.
2. **Auditabilidad**: verificar si el sistema puede explicar un Top-3 fijo usando evidencia histórica y normativa, sin inventar códigos ni alterar el ranking.

## 4. Arquitectura final

![Framework RAG explicativo y auditable](data/Framework%20RAG.png)

**Figura 1. Framework RAG explicativo y auditable usado en el piloto.** La descripción comercial de una DAM/serie se normaliza y se convierte en objeto de consulta. El ranking principal se genera con BM25 sobre un banco histórico de 3,000 casos etiquetados. En paralelo, el corpus normativo NANDINA se consulta para recuperar evidencia documental y contexto jerárquico. El constructor de contexto RAG recibe el Top-3 fijo, sus precedentes históricos y la evidencia normativa asociada. Luego un LLM local genera una justificación controlada, sin clasificar desde cero y sin reordenar candidatos. La salida final es una ficha auditable Top-3 con evidencia, comparación, nivel de soporte y advertencia de revisión experta.

La figura debe leerse como arquitectura de apoyo a auditoría, no como sistema automático de clasificación oficial.

## 5. Qué se desarrolló

### 5.1 Ingesta y normalización de `data_aduanas`

La fuente metodológica principal es un Excel local de DAM/series:

```text
data/Series - Descripciones.xlsx
```

Ese Excel no debe versionarse en Git. El parser transforma un formato por bloques de DAM en una tabla normalizada con una fila por serie. El identificador experimental se construye como concatenación de declaración y serie (`id_unico`).

Script principal:

```text
src/ingestion/sunat_series_parser.py
```

Artefactos intermedios regenerables:

```text
data/interim/sunat_series_descripciones_normalized.csv
data/interim/sunat_series_descripciones_normalized.xlsx
data/interim/sunat_series_descripciones_normalized_metadata.json
```

### 5.2 Construcción de splits Clase 87

La ejecución v0.1 usa solo `Clase = 87`.

Script:

```text
src/evaluation/build_data_aduanas_splits.py
```

Splits finales:

```text
data/processed/data_aduanas_historico_clase87_v0.1.csv
data/processed/data_aduanas_devset_clase87_v0.1.csv
data/processed/data_aduanas_evalset_clase87_v0.1.csv
data/processed/data_aduanas_splits_clase87_v0.1_metadata.json
```

Conteos finales:

| Split | Filas | NANDINAS distintas | Uso |
|---|---:|---:|---|
| Histórico | 3,000 | 69 | Banco de precedentes para recuperación histórica |
| Desarrollo | 100 | 44 | Ajustes exploratorios y pruebas cortas |
| Evaluación | 1,006 | 62 | Evaluación final Clase 87 |

Criterios principales de curación:

- mantener solo `Clase = 87`;
- exigir `id_unico`, `DECLARACION`, `SERIE`, `NANDINA` válida de 8 dígitos y descripción concatenada no vacía;
- preservar columnas `DESCRIPCION DE MERCANCIAS 1` a `DESCRIPCION DE MERCANCIAS 5`;
- construir `DESCRIPCION DE MERCANCIAS CONCATENADA` a partir de líneas reales disponibles;
- excluir encabezados DAM detectados accidentalmente en zonas descriptivas;
- colapsar duplicados exactos por `id_unico`;
- excluir grupos conflictivos;
- evitar solapamiento de `id_unico` entre histórico, desarrollo y evaluación.

Resultado de duplicados en la corrida v0.1:

| Tipo | Conteo |
|---|---:|
| Filas Clase 87 de entrada | 4,232 |
| Filas curadas finales | 4,106 |
| Grupos duplicados exactos | 102 |
| Filas excedentes por duplicado exacto | 114 |
| Grupos conflictivos | 6 |
| Filas excluidas por conflicto | 12 |

### 5.3 Corpus normativo NANDINA

El corpus normativo sirve para recuperación documental, trazabilidad y evidencia. En el resultado final no actúa como ranking principal.

Artefactos principales:

```text
data/processed/corpus_rag_v1_index.jsonl
data/processed/corpus_nandina_hierarchical_v0.1.jsonl
data/processed/indexes/bm25_nandina8.pkl
data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl
```

Problema encontrado: el corpus normativo plano contenía descripciones demasiado cortas o genéricas, por ejemplo `Los demás` o `Partes`. Por eso se construyó una versión jerárquica autocontenida que agrega contexto de niveles superiores. Esa mejora aumentó la cobertura normativa, pero no convirtió al corpus normativo en recuperador principal frente al banco histórico.

### 5.4 Recuperación normativa

Se evaluaron recuperadores sobre el corpus NANDINA:

- BM25 normativo plano;
- BM25 normativo jerárquico;
- BM25 dual protegido;
- candidate pool normativo;
- dense retrieval Text2Trade por fuerza bruta.

Objetivo: medir si la NANDINA esperada aparecía dentro del ranking normativo o del pool de candidatos.

Conclusión: la recuperación normativa aporta trazabilidad y respaldo documental, pero tiene baja exactitud temprana como ranking principal.

Scripts principales:

```text
src/experiments/evaluate_bm25_data_aduanas.py
src/experiments/evaluate_dense_text2trade_data_aduanas.py
src/analysis/compare_bm25_dense_data_aduanas.py
src/experiments/evaluate_bm25_hierarchical_data_aduanas.py
src/experiments/build_candidate_pool_data_aduanas.py
```

### 5.5 Recuperación histórica BM25

La recuperación histórica usa el split histórico como banco de precedentes etiquetados y evalúa contra el split de evaluación sin fuga por `id_unico`.

Script:

```text
src/experiments/evaluate_historical_retrieval_data_aduanas.py
```

La consulta principal es la descripción comercial concatenada de la serie. El método calcula similitud BM25 contra descripciones históricas, recupera precedentes similares y deduplica candidatos por NANDINA para producir un ranking de códigos.

Esta fue la técnica que terminó dominando el ranking operativo en Clase 87.

### 5.6 Pool híbrido histórico + normativo

El pool híbrido conserva la recuperación histórica como ranking temprano y agrega evidencia normativa como respaldo.

Script:

```text
src/experiments/build_hybrid_pool_data_aduanas.py
```

Estrategia recomendada:

```text
historical_with_normative_backfill_if_missing_code
```

Decisión: el histórico domina el ranking; lo normativo entra como backfill, trazabilidad y evidencia documental, sin desplazar candidatos históricos tempranos.

### 5.7 LLM como re-ranker diagnóstico

Se probó LLM para reordenar candidatos sobre una muestra de 20 casos. El resultado fue negativo: degradó Top-1 y MRR frente al ranking original enviado. Por eso no se escaló como componente final del pipeline.

Documento:

```text
docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md
```

Decisión metodológica: el LLM no debe reordenar ni clasificar en la versión final del piloto v0.1.

### 5.8 LLM como explicador auditable Top-3

El rol final del LLM es generar explicaciones auditables sobre el Top-3 fijo. El LLM recibe:

- descripción de entrada;
- tres candidatos ya recuperados;
- evidencia histórica por candidato;
- evidencia normativa por candidato;
- reglas anti-invención;
- instrucción explícita de no clasificar, no agregar códigos y no reordenar.

Modelo usado:

```text
qwen2.5:7b-instruct via Ollama local
```

Controles metodológicos:

- sin OpenAI;
- sin APIs remotas;
- sin servicios con costo;
- temperatura controlada;
- el LLM no recibe la etiqueta esperada;
- el LLM no puede proponer códigos fuera del Top-3 enviado;
- el LLM no reordena candidatos en la fase final de explicación.

Prompts y scripts:

```text
src/llm/explain_top3_nandina_prompt_v0.2.md
src/llm/explain_top3_nandina_prompt_v0.3.md
src/experiments/build_llm_explanation_top3_audit_sample.py
src/experiments/run_llm_explanation_top3_audit_sample.py
src/experiments/evaluate_llm_explanation_top3_audit_sample.py
src/experiments/render_llm_explanation_audit_cards.py
```

La fase 10D mejoró el diseño de ficha con tono prudente, detección de evidencia normativa genérica y campo de revisión experta. No cambia métricas de recuperación.

## 6. Problemas encontrados y tratamiento aplicado

| Problema | Tratamiento aplicado | Estado |
|---|---|---|
| Corpus normativo plano con textos genéricos | Construcción de corpus jerárquico autocontenido | Mitigado; útil como evidencia, no como ranking principal |
| Baja exactitud temprana del ranking normativo | Separar corpus normativo de ranking operativo | Resuelto por diseño del pipeline |
| Brecha entre descripción comercial y lenguaje normativo | Evaluar recuperación histórica sobre precedentes reales | Mitigado en Clase 87 |
| Riesgo de que Top-N no contenga la NANDINA esperada | Medición Top-k, Recall@100/200 y MRR | Evaluado en v0.1 |
| Dense Text2Trade no recuperó adecuadamente | No incorporarlo al pipeline exacto | Descartado para v0.1 |
| LLM degradó ranking como re-ranker | No escalar LLM como reordenador | Decisión consolidada |
| LLM puede inventar o modificar candidatos | Top-3 fijo, reglas anti-invención y validación estructural | Mitigado por diseño |
| Evidencia normativa a veces genérica | Campo de soporte, advertencias y revisión experta | Mitigado, no eliminado |
| Riesgo de overclaiming | Redacción como piloto offline, no clasificación oficial | Controlado metodológicamente |
| Generalización fuera de Clase 87 | Declarar limitación explícita | Pendiente para estudios posteriores |

## 7. Métricas usadas

### 7.1 Métricas de recuperación

| Métrica | Interpretación |
|---|---|
| Top-1 | La NANDINA esperada aparece en la primera posición |
| Top-3 | La NANDINA esperada aparece dentro de los tres primeros candidatos |
| Top-10 | La NANDINA esperada aparece dentro de los diez primeros candidatos |
| Recall@100 | La NANDINA esperada aparece dentro de los primeros 100 candidatos |
| Recall@200 | La NANDINA esperada aparece dentro de los primeros 200 candidatos |
| MRR | Media del recíproco del rank correcto |
| Partida@100 | Coincidencia por los primeros 4 dígitos dentro del Top-100 |
| Sub Partida@100 | Coincidencia por los primeros 6 dígitos dentro del Top-100 |
| Clase@100 | Coincidencia por los primeros 2 dígitos dentro del Top-100 |

### 7.2 Métricas de auditabilidad LLM

| Métrica | Interpretación |
|---|---|
| JSON válido | La respuesta cumple formato JSON esperado |
| Ranking preservado | El LLM conserva el Top-3 y su orden |
| Sin códigos fuera del pool | El LLM no inventa candidatos |
| Evidencia histórica citada | Cada candidato cita evidencia histórica disponible |
| Evidencia normativa citada | Cada candidato cita evidencia normativa disponible |
| Score de auditabilidad | Puntaje agregado de controles estructurales |

## 8. Resultados v0.1

### 8.1 Comparación integrada

| Método | Tipo | n | Top-1 | Top-10 | Recall@100 | Recall@200 | MRR | Decisión |
|---|---|---:|---:|---:|---:|---:|---:|---|
| BM25 normativo plano Clase 87 | Normativo | 1,006 | 0.0229 | 0.0467 | 0.0626 | NA | 0.0312 | Baseline auditable; no ranking principal |
| Dense Text2Trade Clase 87 | Denso | 1,006 | 0.0000 | 0.0000 | 0.0010 | NA | 0.0000 | No se incorpora al pipeline exacto |
| BM25 jerárquico Clase 87 | Normativo | 1,006 | 0.0249 | 0.0497 | 0.3449 | NA | 0.0385 | Respaldo normativo y trazabilidad |
| BM25 dual protegido Clase 87 | Normativo | 1,006 | 0.0239 | 0.0487 | 0.1948 | NA | 0.0340 | Fuente auxiliar, no principal |
| Candidate pool normativo | Normativo | 1,006 | NA | 0.0497 | 0.3489 | 0.6292 | Respaldo documental |
| Recuperación histórica real | Histórico | 1,006 | 0.8628 | 0.9801 | 1.0000 | NA | 0.9062 | Ranking operativo principal |
| Pool híbrido histórico + normativo | Híbrido | 1,006 | 0.8628 | 0.9801 | 1.0000 | 1.0000 | 0.9062 | Estrategia recomendada |
| LLM re-ranker | LLM ranking | 20 | 0.2000 | 0.5000 | NA | NA | 0.3083 | Resultado negativo; no escalar |
| LLM explicación Top-3 | LLM explicación | 50 | NA | NA | NA | NA | NA | Explicador auditable |

### 8.2 Resultado LLM explicativo

En la fase 10B, sobre 50 casos:

| Control | Resultado |
|---|---:|
| JSON válido | 1.0000 |
| Top-3 completo | 1.0000 |
| Ranking preservado | 1.0000 |
| Sin códigos fuera del pool | 1.0000 |
| Evidencia histórica citada por candidato | 1.0000 |
| Evidencia normativa citada por candidato | 1.0000 |
| Comparación Top-3 presente | 1.0000 |
| Advertencia final presente | 1.0000 |
| Score promedio de auditabilidad | 0.9520 |

La revisión cualitativa 10C confirmó utilidad para auditoría humana, pero detectó tres cautelas: evidencia normativa genérica, predominio de evidencia histórica y tono demasiado decisivo en algunas conclusiones. La fase 10D corrigió el diseño de prompt, rúbrica y ficha para incorporar prudencia y revisión experta.

## 9. Validación de hipótesis de trabajo

| Hipótesis / expectativa operativa | Estado | Evidencia principal |
|---|---|---|
| La arquitectura mejora la recuperación frente a baselines normativos | Respaldada en Clase 87 | Histórico/híbrido `Recall@100 = 1.0000` frente a pool normativo `Recall@100 = 0.3489` |
| El banco histórico es útil para recomendación NANDINA | Respaldada en Clase 87 | Histórico `Top-1 = 0.8628`, `Top-10 = 0.9801`, `MRR = 0.9062` |
| El corpus normativo jerárquico es útil | Parcialmente respaldada | Mejora cobertura normativa, pero no ranking temprano suficiente |
| El LLM mejora como re-ranker | No respaldada | El re-ranking LLM degrada Top-1 y MRR en muestra diagnóstica |
| El LLM sirve como explicador auditable | Respaldada en muestra de 50 casos | JSON válido, ranking preservado y evidencia citada en 50/50 casos |
| El enfoque RAG aporta trazabilidad | Respaldada por diseño y salidas | Se separan precedentes históricos, evidencia normativa y justificación controlada |

## 10. Decisiones metodológicas consolidadas

| Decisión | Justificación |
|---|---|
| Acotar v0.1 a Clase 87 | Permite cerrar un piloto evaluable y reproducible con datos disponibles. |
| Usar recuperación histórica BM25 como ranking principal | Supera ampliamente a los baselines normativos en Clase 87. |
| Mantener corpus normativo como evidencia | Aporta trazabilidad, contexto y soporte documental, aunque no ranking temprano suficiente. |
| No usar Dense Text2Trade en v0.1 | Resultado empírico insuficiente en la configuración evaluada. |
| No usar LLM como re-ranker final | Degradó el ranking en muestra diagnóstica. |
| Usar LLM solo como explicador Top-3 | Preserva ranking, evita invención de códigos y permite explicación auditable. |
| Mantener Top-3 fijo | El constructor de contexto y el LLM no deben recibir ni alterar todo el ranking. |
| Incorporar advertencia de revisión experta | Evita que la explicación sea leída como clasificación oficial. |

## 11. Cómo reproducir

### 11.1 Preparar entorno

Requiere Python 3.10. En Windows:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
C:\Users\Vladimir\AppData\Local\Programs\Python\Python310\python.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Nota: `hnswlib` puede fallar en Windows si no están instaladas las Microsoft C++ Build Tools. Para las evaluaciones ya cerradas, Dense Text2Trade se ejecutó por fuerza bruta y no requiere reconstruir HNSW.

### 11.2 Regenerar splits `data_aduanas`

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

### 11.3 Reproducir evaluaciones principales

```powershell
.\.venv\Scripts\python.exe -m src.experiments.evaluate_bm25_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_dense_text2trade_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_bm25_hierarchical_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.build_candidate_pool_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_historical_retrieval_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.build_hybrid_pool_data_aduanas
```

### 11.4 Reproducir evaluación final integrada

La evaluación final integrada consolida outputs existentes. No reejecuta LLM ni reentrena modelos.

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

### 11.5 Reproducir explicación LLM Top-3

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

## 12. Estructura del repositorio

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

## 13. Artefactos principales

| Artefacto | Rol |
|---|---|
| `docs/protocolo_experimental_v0.1.md` | Protocolo experimental general |
| `docs/manifest_artifacts_v0.1.json` | Manifiesto machine-readable de artefactos |
| `docs/manifiesto_artefactos_v0.1.md` | Manifiesto narrativo de artefactos |
| `docs/evaluacion_final_integrada_v0.1.md` | Cierre integrado de resultados e hipótesis |
| `docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md` | Evaluación del pool histórico + normativo |
| `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md` | Evaluación formal de explicaciones Top-3 |
| `docs/revision_cualitativa_fichas_auditables_v0.1.md` | Revisión cualitativa de fichas |
| `docs/mejora_ficha_auditable_llm_top3_v0.1.md` | Mejora 10D del diseño auditable |
| `src/analysis/build_integrated_final_evaluation.py` | Script reproducible de evaluación final integrada |

## 14. Política de versionado y confidencialidad

Versionar en Git:

- scripts;
- protocolos;
- documentos metodológicos;
- splits procesados necesarios para reproducibilidad, si no contienen información sensible;
- manifiestos;
- imagen del framework si se desea que el README renderice en GitHub.

No versionar por defecto:

- `outputs/`, porque son regenerables;
- `.venv/`, porque depende del entorno local;
- `data/interim/`, salvo decisión metodológica explícita;
- `data/Series - Descripciones.xlsx`, por ser fuente local;
- `Referencias/`, por contener bibliografía local pesada;
- credenciales, tokens, API keys o datos restringidos.

## 15. Limitaciones

- El alcance final es `Clase = 87`; los resultados no deben generalizarse automáticamente a todas las clases NANDINA.
- El desempeño histórico depende de que existan precedentes etiquetados en el banco histórico.
- Falta una validación temporal o externa para medir desempeño ante códigos ausentes, cambios de distribución o nuevas familias de mercancías.
- El corpus normativo mejora trazabilidad, pero no sustituye criterio legal ni revisión experta.
- El LLM explica candidatos recuperados; no debe usarse como clasificador oficial.
- La salida es una recomendación auditable, no una declaración aduanera ni una decisión vinculante.
- La evidencia normativa puede ser genérica en algunos casos; por eso la ficha incorpora nivel de soporte y revisión experta.

## 16. Estado del piloto v0.1

El piloto experimental offline v0.1 está cerrado técnicamente bajo el alcance Clase 87.

Cierre metodológico:

1. recuperación histórica BM25 como ranking operativo principal;
2. corpus normativo jerárquico como evidencia, trazabilidad y respaldo;
3. LLM local solo para explicación auditable del Top-3 fijo;
4. revisión experta humana como cierre obligatorio.

Pendientes para una etapa posterior:

- empaquetar la reproducibilidad en un comando único;
- crear un tag Git `v0.1-piloto`;
- preparar la redacción final de tesis/artículo;
- evaluar generalización fuera de Clase 87;
- realizar validación temporal o externa si se dispone de nuevos datos.
