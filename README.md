# Piloto experimental offline LLM+RAG para recomendación auditable de subpartidas NANDINA

Repositorio de investigación aplicada para evaluar un piloto offline de gestión de información documental orientado a la recomendación auditable de subpartidas NANDINA. El sistema no emite clasificación oficial ni reemplaza el criterio de un especialista; produce candidatos, evidencias y explicaciones trazables para apoyar la revisión humana.

## 1. Lectura correcta del proyecto

Este repositorio debe leerse en dos niveles:

1. **Proyecto de investigación**: documento académico inicial de maestría, concebido antes de la ejecución técnica. Define el problema, objetivos, hipótesis, variables, metodología offline, métricas y rúbrica de explicación auditable.
2. **Ejecución del piloto v0.1**: desarrollo técnico posterior registrado en este repositorio. Concreta decisiones metodológicas, corpus, scripts, evaluaciones, resultados, problemas encontrados y ajustes del flujo experimental.

La ejecución operacionaliza el proyecto y precisa qué técnicas funcionaron en el contexto disponible. La decisión metodológica final del piloto v0.1 es:

- usar **recuperación histórica BM25** sobre precedentes etiquetados como ranking operativo principal;
- usar el **corpus normativo NANDINA** como evidencia, trazabilidad y respaldo documental;
- usar un **LLM local** solo para generar explicaciones auditables del Top-3 fijo;
- no usar el LLM como clasificador libre ni como re-ranker final;
- mantener la revisión experta como requisito externo para cualquier uso operativo.

La revisión experta no formó parte de la evaluación automatizada del piloto v0.1.

## 2. Alcance vigente del piloto v0.1

```text
Clase = 87
Fuente experimental = data_aduanas
Modo = offline
Salida = recomendación auditable Top-3
```

El sistema trabaja con descripciones comerciales de DAM/series y no con decisiones oficiales nuevas. La etiqueta administrativa de referencia se usa únicamente para evaluación offline. Los resultados no deben generalizarse automáticamente a toda la NANDINA.

## 3. Pregunta experimental operativa

> ¿Puede una arquitectura offline basada en recuperación documental, banco histórico y LLM local producir recomendaciones NANDINA trazables y auditables a partir de descripciones comerciales?

La evaluación se separó en dos problemas:

1. **Recuperación**: verificar si la NANDINA esperada aparece en el ranking o en el pool de candidatos.
2. **Auditabilidad**: verificar si el sistema puede explicar un Top-3 fijo usando evidencia histórica y normativa, sin inventar códigos ni alterar el ranking.

## 4. Arquitectura final

![Framework RAG explicativo y auditable](data/Framework%20RAG.png)

**Figura 1. Framework RAG explicativo y auditable usado en el piloto.** La descripción comercial de una DAM/serie se normaliza y se convierte en objeto de consulta. El ranking principal se genera con BM25 sobre un banco histórico de 3,000 casos etiquetados. En paralelo, el corpus normativo NANDINA se consulta para recuperar evidencia documental y contexto jerárquico. El constructor de contexto RAG recibe el Top-3 fijo, sus precedentes históricos y la evidencia normativa asociada. Luego, un LLM local genera una justificación controlada, sin clasificar desde cero y sin reordenar candidatos. La salida final es una ficha auditable Top-3 con evidencia, comparación, nivel de soporte y advertencia de revisión experta.

## 5. Qué se desarrolló

### 5.1 Ingesta y normalización de `data_aduanas`

La fuente metodológica principal es un Excel local de DAM/series:

```text
data/Series - Descripciones.xlsx
```

El archivo no se versiona en Git. El parser transforma el formato por bloques de DAM en una tabla normalizada con una fila por serie. El identificador experimental vigente se construye como concatenación de declaración y serie (`id_unico`).

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

| Split | Filas | NANDINAS distintas | Uso |
|---|---:|---:|---|
| Histórico | 3,000 | 69 | Banco de precedentes para recuperación histórica |
| Desarrollo | 100 | 44 | Ajustes exploratorios y pruebas cortas |
| Evaluación | 1,006 | 62 | Evaluación final Clase 87 |

Criterios principales de curación:

- mantener solo `Clase = 87`;
- exigir `id_unico`, `DECLARACION`, `SERIE`, `NANDINA` válida de ocho dígitos y descripción concatenada no vacía;
- preservar las columnas `DESCRIPCION DE MERCANCIAS 1` a `DESCRIPCION DE MERCANCIAS 5`;
- construir `DESCRIPCION DE MERCANCIAS CONCATENADA` a partir de las líneas disponibles;
- excluir encabezados DAM detectados accidentalmente en zonas descriptivas;
- colapsar duplicados exactos por `id_unico`;
- excluir grupos conflictivos;
- evitar solapamiento de `id_unico` entre histórico, desarrollo y evaluación.

| Tipo | Conteo |
|---|---:|
| Filas Clase 87 de entrada | 4,232 |
| Filas curadas finales | 4,106 |
| Grupos duplicados exactos | 102 |
| Filas excedentes por duplicado exacto | 114 |
| Grupos conflictivos | 6 |
| Filas excluidas por conflicto | 12 |

### 5.3 Corpus normativo NANDINA

El corpus normativo sirve para recuperación documental, trazabilidad y evidencia. En el flujo final no actúa como ranking principal.

#### Flujo documentado de construcción

```text
data/processed/corpus/nandina/nandina_corpus.jsonl
        ↓ auditoría de jerarquía y calidad
src/corpus/audit_nandina_hierarchy.py
        ↓
data/processed/corpus_rag_v1_index.jsonl
        ↓ construcción jerárquica
src/corpus/build_hierarchical_nandina_corpus.py
        ↓
data/processed/corpus_nandina_hierarchical_v0.1.jsonl
        ↓ construcción BM25 reproducible
src/bm25_index.py + scripts versionados de ejecución
        ↓
índices BM25 plano y jerárquico
```

Scripts principales:

```text
src/corpus/text_index.py
src/corpus/audit_nandina_hierarchy.py
src/corpus/build_hierarchical_nandina_corpus.py
src/bm25_index.py
```

Artefactos principales:

```text
data/processed/corpus_rag_v1_index.jsonl
data/processed/corpus_nandina_hierarchical_v0.1.jsonl
data/processed/corpus_nandina_hierarchical_v0.1_metadata.json
data/processed/indexes/bm25_nandina8.pkl
```

Estado de los índices:

| Índice | Construcción codificada | Metadatos | `.pkl` versionado |
|---|---|---|---|
| BM25 normativo plano | Sí | Sí | Sí: `data/processed/indexes/bm25_nandina8.pkl` |
| BM25 normativo jerárquico | Sí | Sí, local | No; `bm25_nandina8_hierarchical_v0.1.pkl` se genera localmente |

La ausencia del `.pkl` jerárquico en Git no impide su regeneración cuando se dispone del corpus, los scripts versionados y las dependencias. La implementación común utiliza tokenización determinística, índice invertido, IDF y parámetros `k1 = 1.5` y `b = 0.75`.

#### Cobertura y limitaciones documentadas

La auditoría del corpus intermedio registró:

- 9,785 registros totales;
- 1,020 registros de partida 4D;
- 1,117 registros HS-6;
- 7,648 registros NANDINA de ocho dígitos;
- 407 NANDINA8 sin padre 4D explícito;
- 4,504 NANDINA8 sin padre HS-6 explícito;
- 56 grupos código–nivel con descripciones conflictivas;
- 17 descripciones con posible contaminación por encabezados.

El corpus jerárquico contiene 7,648 registros y 7,644 códigos únicos. La diferencia corresponde a registros duplicados conflictivos, principalmente `48051900` y `84472010`. Estas limitaciones deben conservarse al interpretar la cobertura normativa.

Detalle técnico: [`docs/trazabilidad_corpus_indices_v0.1.md`](docs/trazabilidad_corpus_indices_v0.1.md).

### 5.4 Recuperación normativa

Se evaluaron:

- BM25 normativo plano;
- BM25 normativo jerárquico;
- BM25 dual protegido;
- candidate pool normativo;
- dense retrieval Text2Trade por fuerza bruta.

Scripts principales:

```text
src/experiments/evaluate_bm25_data_aduanas.py
src/experiments/evaluate_dense_text2trade_data_aduanas.py
src/analysis/compare_bm25_dense_data_aduanas.py
src/experiments/evaluate_bm25_hierarchical_data_aduanas.py
src/experiments/build_candidate_pool_data_aduanas.py
```

La recuperación normativa aporta trazabilidad y respaldo documental, pero tiene baja exactitud temprana como ranking principal.

### 5.5 Recuperación histórica BM25

Script:

```text
src/experiments/evaluate_historical_retrieval_data_aduanas.py
```

La consulta principal es la descripción comercial concatenada de la serie. El método calcula similitud BM25 contra descripciones históricas, recupera precedentes similares y deduplica candidatos por NANDINA. Esta fue la técnica que dominó el ranking operativo en Clase 87.

### 5.6 Pool híbrido histórico + normativo

Script:

```text
src/experiments/build_hybrid_pool_data_aduanas.py
```

Estrategia consolidada:

```text
historical_with_normative_backfill_if_missing_code
```

El histórico domina el ranking; lo normativo entra como backfill, trazabilidad y evidencia documental, sin desplazar candidatos históricos tempranos.

### 5.7 LLM como re-ranker diagnóstico

Se probó el LLM para reordenar candidatos sobre una muestra de 20 casos. Degradó Top-1 y MRR frente al ranking original, por lo que no se incorporó al pipeline final.

```text
docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md
```

### 5.8 LLM como explicador auditable Top-3

Modelo:

```text
qwen2.5:7b-instruct via Ollama local
```

El LLM recibe la descripción, tres candidatos ya recuperados, precedentes históricos, evidencia normativa y reglas anti-invención. No recibe la etiqueta esperada; no puede agregar códigos ni reordenar el Top-3.

Scripts:

```text
src/llm/explain_top3_nandina_prompt_v0.2.md
src/llm/explain_top3_nandina_prompt_v0.3.md
src/experiments/build_llm_explanation_top3_audit_sample.py
src/experiments/run_llm_explanation_top3_audit_sample.py
src/experiments/evaluate_llm_explanation_top3_audit_sample.py
src/experiments/render_llm_explanation_audit_cards.py
```

## 6. Problemas encontrados y tratamiento aplicado

| Problema | Tratamiento aplicado | Estado |
|---|---|---|
| Corpus normativo plano con textos genéricos | Construcción de corpus jerárquico autocontenido | Mitigado; útil como evidencia, no como ranking principal |
| Jerarquía 4D/HS-6 incompleta | Contexto nullable y auditoría explícita | Documentado; no eliminado |
| Registros conflictivos duplicados | Conservación de advertencias y trazabilidad | Documentado |
| Baja exactitud temprana del ranking normativo | Separar corpus normativo de ranking operativo | Resuelto por diseño del pipeline |
| Brecha entre descripción comercial y lenguaje normativo | Evaluar recuperación histórica sobre precedentes reales | Mitigado en Clase 87 |
| Dense Text2Trade no recuperó adecuadamente | No incorporarlo al pipeline exacto | Descartado para v0.1 |
| LLM degradó ranking como re-ranker | No escalar LLM como reordenador | Decisión consolidada |
| LLM puede inventar o modificar candidatos | Top-3 fijo, reglas anti-invención y validación estructural | Mitigado por diseño |
| Evidencia normativa a veces genérica | Campo de soporte, advertencias y revisión experta | Mitigado, no eliminado |
| Generalización fuera de Clase 87 | Declarar limitación explícita | Pendiente para estudios posteriores |

## 7. Métricas usadas

### 7.1 Recuperación

| Métrica | Interpretación |
|---|---|
| Top-1 | La NANDINA esperada aparece en la primera posición |
| Top-3 | La NANDINA esperada aparece dentro de los tres primeros candidatos |
| Top-10 | La NANDINA esperada aparece dentro de los diez primeros candidatos |
| Recall@100 | La NANDINA esperada aparece dentro de los primeros 100 candidatos |
| Recall@200 | La NANDINA esperada aparece dentro de los primeros 200 candidatos |
| MRR | Media del recíproco del rank correcto |
| Partida@100 | Coincidencia por los primeros cuatro dígitos dentro del Top-100 |
| Subpartida@100 | Coincidencia por los primeros seis dígitos dentro del Top-100 |
| Clase@100 | Coincidencia por los primeros dos dígitos dentro del Top-100 |

### 7.2 Auditabilidad LLM

| Métrica | Interpretación |
|---|---|
| JSON válido | La respuesta cumple el formato esperado |
| Ranking preservado | El LLM conserva el Top-3 y su orden |
| Sin códigos fuera del pool | El LLM no inventa candidatos |
| Evidencia histórica citada | Cada candidato cita evidencia histórica disponible |
| Evidencia normativa citada | Cada candidato cita evidencia normativa disponible |
| Score de auditabilidad | Puntaje agregado de controles estructurales |

## 8. Resultados v0.1

| Método | Tipo | n | Top-1 | Top-10 | Recall@100 | Recall@200 | MRR | Decisión |
|---|---|---:|---:|---:|---:|---:|---:|---|
| BM25 normativo plano Clase 87 | Normativo | 1,006 | 0.0229 | 0.0467 | 0.0626 | NA | 0.0312 | Baseline auditable; no ranking principal |
| Dense Text2Trade Clase 87 | Denso | 1,006 | 0.0000 | 0.0000 | 0.0010 | NA | 0.0000 | No se incorpora al pipeline exacto |
| BM25 jerárquico Clase 87 | Normativo | 1,006 | 0.0249 | 0.0497 | 0.3449 | NA | 0.0385 | Respaldo normativo y trazabilidad |
| BM25 dual protegido Clase 87 | Normativo | 1,006 | 0.0239 | 0.0487 | 0.1948 | NA | 0.0340 | Fuente auxiliar, no principal |
| Candidate pool normativo | Normativo | 1,006 | NA | 0.0497 | 0.3489 | 0.6292 | NA | Respaldo documental |
| Recuperación histórica real | Histórico | 1,006 | 0.8628 | 0.9801 | 1.0000 | NA | 0.9062 | Ranking operativo principal |
| Pool híbrido histórico + normativo | Híbrido | 1,006 | 0.8628 | 0.9801 | 1.0000 | 1.0000 | 0.9062 | Estrategia recomendada |
| LLM re-ranker | LLM ranking | 20 | 0.2000 | 0.5000 | NA | NA | 0.3083 | Resultado negativo; no escalar |
| LLM explicación Top-3 | LLM explicación | 50 | NA | NA | NA | NA | NA | Explicador auditable |

En la fase 10B, las 50 respuestas fueron JSON válido, preservaron el Top-3, no introdujeron códigos externos y citaron evidencia histórica y normativa. El score promedio de auditabilidad fue 0.9520. La revisión cualitativa posterior detectó evidencia normativa genérica, predominio de evidencia histórica y tono excesivamente decisivo en algunas conclusiones; la fase 10D ajustó prompt, rúbrica y ficha.

## 9. Validación de hipótesis de trabajo

| Hipótesis / expectativa operativa | Estado | Evidencia principal |
|---|---|---|
| La arquitectura mejora la recuperación frente a baselines normativos | Respaldada en Clase 87 | Histórico/híbrido `Recall@100 = 1.0000` frente a pool normativo `Recall@100 = 0.3489` |
| El banco histórico es útil para recomendación NANDINA | Respaldada en Clase 87 | Histórico `Top-1 = 0.8628`, `Top-10 = 0.9801`, `MRR = 0.9062` |
| El corpus normativo jerárquico es útil | Parcialmente respaldada | Mejora cobertura normativa, pero no ofrece ranking temprano suficiente |
| El LLM mejora como re-ranker | No respaldada | El re-ranking LLM degrada Top-1 y MRR en la muestra diagnóstica |
| El LLM sirve como explicador auditable | Respaldada en la muestra de 50 casos | JSON válido, ranking preservado y evidencia citada |
| El enfoque RAG aporta trazabilidad | Respaldada por diseño y salidas | Se separan precedentes históricos, evidencia normativa y justificación controlada |

## 10. Decisiones metodológicas consolidadas

| Decisión | Justificación |
|---|---|
| Acotar v0.1 a Clase 87 | Permite cerrar un piloto evaluable con los datos disponibles |
| Usar recuperación histórica BM25 como ranking principal | Supera ampliamente a los baselines normativos en Clase 87 |
| Mantener el corpus normativo como evidencia | Aporta trazabilidad y contexto, aunque no ranking temprano suficiente |
| No usar Dense Text2Trade en v0.1 | Resultado empírico insuficiente en la configuración evaluada |
| No usar LLM como re-ranker final | Degradó el ranking en la muestra diagnóstica |
| Usar LLM solo como explicador Top-3 | Preserva ranking, evita invención de códigos y permite explicación auditable |
| Mantener Top-3 fijo | El constructor de contexto y el LLM no deben alterar el ranking completo |
| Incorporar advertencia de revisión experta | Evita que la explicación sea leída como clasificación oficial |

## 11. Reproducibilidad

La reproducibilidad debe interpretarse por capas:

- **Procedimiento y análisis**: scripts, parámetros, prompts, metadatos y documentos metodológicos están versionados.
- **Datos administrativos**: la reproducción completa requiere acceso autorizado al Excel fuente de DAM/series, que no se versiona.
- **Índice BM25 plano**: el `.pkl` está serializado y versionado.
- **Índice BM25 jerárquico**: el `.pkl` no está versionado, pero es regenerable mediante el corpus, el código y los metadatos disponibles.
- **LLM local**: la repetición requiere Ollama y disponibilidad local de `qwen2.5:7b-instruct`.

### 11.1 Preparar entorno

Requiere Python 3.10:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 11.2 Regenerar splits `data_aduanas`

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

Cuando se dispone del Excel local, puede añadirse `--regenerate-normalized` y `--source-xlsx "data\Series - Descripciones.xlsx"`.

### 11.3 Auditar y reconstruir el corpus jerárquico

```powershell
.\.venv\Scripts\python.exe -m src.corpus.audit_nandina_hierarchy
.\.venv\Scripts\python.exe -m src.corpus.build_hierarchical_nandina_corpus
```

### 11.4 Reproducir evaluaciones principales

```powershell
.\.venv\Scripts\python.exe -m src.experiments.evaluate_bm25_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_dense_text2trade_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_bm25_hierarchical_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.build_candidate_pool_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.evaluate_historical_retrieval_data_aduanas
.\.venv\Scripts\python.exe -m src.experiments.build_hybrid_pool_data_aduanas
```

### 11.5 Reproducir evaluación final integrada

```powershell
.\.venv\Scripts\python.exe -m src.analysis.build_integrated_final_evaluation
```

### 11.6 Reproducir explicación LLM Top-3

```powershell
ollama pull qwen2.5:7b-instruct
.\.venv\Scripts\python.exe -m src.experiments.build_llm_explanation_top3_audit_sample
.\.venv\Scripts\python.exe -m src.experiments.run_llm_explanation_top3_audit_sample
.\.venv\Scripts\python.exe -m src.experiments.evaluate_llm_explanation_top3_audit_sample
.\.venv\Scripts\python.exe -m src.experiments.render_llm_explanation_audit_cards
```

## 12. Estructura del repositorio

```text
.
|-- data/
|   |-- external/       # referencias externas locales
|   |-- interim/        # tablas intermedias regenerables
|   |-- processed/      # splits, corpus e índices versionados o regenerables
|   |-- raw/            # insumos locales, cuando aplica
|   |-- Framework RAG.png
|   `-- Series - Descripciones.xlsx   # fuente local no versionada
|-- docs/               # protocolos, informes, manifiestos y trazabilidad
|-- notebooks/          # exploración previa
|-- outputs/            # resultados regenerables ignorados por Git
|-- Referencias/        # bibliografía local no versionada
|-- src/
|   |-- analysis/
|   |-- corpus/
|   |-- evaluation/
|   |-- experiments/
|   |-- ingestion/
|   |-- llm/
|   |-- retrieval/
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
| `docs/trazabilidad_corpus_indices_v0.1.md` | Procedencia, auditoría, versionamiento y regeneración del corpus e índices |
| `docs/evaluacion_final_integrada_v0.1.md` | Cierre integrado de resultados e hipótesis |
| `docs/evaluacion_pool_hibrido_data_aduanas_clase87_v0.1.md` | Evaluación del pool histórico + normativo |
| `docs/evaluacion_llm_explicacion_top3_auditable_v0.1.md` | Evaluación formal de explicaciones Top-3 |
| `docs/revision_cualitativa_fichas_auditables_v0.1.md` | Revisión cualitativa de fichas |
| `docs/mejora_ficha_auditable_llm_top3_v0.1.md` | Mejora 10D del diseño auditable |
| `src/analysis/build_integrated_final_evaluation.py` | Evaluación final integrada reproducible |

## 14. Política de versionado y confidencialidad

Versionar en Git:

- scripts;
- protocolos y documentos metodológicos;
- metadatos y manifiestos;
- corpus o splits procesados cuando no contengan información sensible;
- artefactos binarios necesarios cuando su tamaño y licencia lo permitan.

No versionar por defecto:

- `outputs/`, porque son regenerables;
- `.venv/`, porque depende del entorno local;
- `data/interim/`, salvo decisión metodológica explícita;
- `data/Series - Descripciones.xlsx`, por ser una fuente local restringida;
- `Referencias/`, por contener bibliografía local pesada;
- credenciales, tokens, API keys o datos restringidos;
- el `.pkl` BM25 jerárquico, mientras se mantenga como artefacto local regenerable.

## 15. Limitaciones

- El alcance final es `Clase = 87`.
- El desempeño histórico depende de la existencia de precedentes etiquetados.
- Falta validación temporal o externa para códigos ausentes, cambios de distribución o nuevas familias de mercancías.
- La reproducción completa de los datos administrativos depende del Excel fuente no versionado.
- El corpus intermedio presenta padres jerárquicos ausentes, registros conflictivos y contaminación textual documentada.
- El corpus normativo mejora trazabilidad, pero no sustituye el criterio legal ni la revisión experta.
- El LLM explica candidatos recuperados; no debe utilizarse como clasificador oficial.
- La salida es una recomendación auditable, no una declaración aduanera ni una decisión vinculante.

## 16. Estado del piloto v0.1

El piloto experimental offline v0.1 está cerrado técnicamente bajo el alcance Clase 87.

Cierre metodológico:

1. recuperación histórica BM25 como ranking operativo principal;
2. corpus normativo jerárquico como evidencia, trazabilidad y respaldo;
3. LLM local solo para explicación auditable del Top-3 fijo;
4. revisión experta humana como requisito externo para cualquier uso operativo.

Pendientes posteriores:

- empaquetar la reproducibilidad en un comando único;
- crear un tag Git `v0.1-piloto`;
- evaluar generalización fuera de Clase 87;
- realizar validación temporal o externa si se dispone de nuevos datos.
