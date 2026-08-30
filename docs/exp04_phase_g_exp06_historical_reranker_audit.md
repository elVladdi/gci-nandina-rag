# EXP-04 Fase G / EXP-06: auditoria del reranker historico

## Fuente de autoridad

La ficha externa `EXP-06_repetir_reranker_LLM_sobre_pool_final.md` fue leida antes de cualquier llamada al modelo. Exige un pool compatible por hash, muestra reproducible previa, candidatos cerrados y comparacion pareada; no fija semilla ni estratificacion basada en referencia.

## Implementacion historica auditada

| Artefacto | Hallazgo |
| --- | --- |
| `build_hybrid_historical_normative_pool.py` | Construye el pool a profundidad 100. La estrategia operacional seleccionada fue `historical_first_80_normative_20`: hasta 80 candidatos historicos, luego el pool normativo, luego historicos restantes; deduplicacion por codigo y renumeracion. Tambien contiene RRF y oraculo, pero no fueron usados por el reranker operacional. |
| `run_llm_rerank_hybrid_pool_sample.py` | Runner de la corrida EXP-06 precedente: `qwen2.5:7b-instruct`, Ollama local, `/api/generate`, `format=json`, `temperature=0`, sin seed/top-p/top-k/num_predict explicitos, timeout 180 s, sin retry y limite 10. |
| `rerank_hybrid_pool_prompt_v0.1.md` | Prompt cerrado: descripcion, rango original, codigo, pertenencia a fuentes y ranks de fuente; prohibe codigos externos y pide JSON. Permitio hasta diez elementos, por lo que no aseguraba una permutacion exacta. |
| `evaluate_llm_rerank_hybrid_pool_sample.py` | Mide Top-k, MRR y cambios. La muestra de 20 se estratifico usando `exact_rank`, `expected_nandina` y soporte de la referencia; esa regla no es portable porque G prohibe usar la etiqueta antes de generar. |
| `docs/evaluacion_llm_rerank_hybrid_pool_sample_v0.1.md` | Corrida DEVELOPMENT / HISTORICAL DIAGNOSTIC: 20 casos, JSON 20/20, 13 rankings incompletos, 0 ganancias y 4 perdidas; Top-1 0.2500 a 0.2000 y MRR 0.3542 a 0.3083. No se mezcla con v0.2. |

El reranker devset anterior tambien confirma el mismo modelo y backend, digest historico `845dbda0...`, cuantizacion `Q4_K_M`, temperatura 0 y salida estructurada. No fija una prueba pareada inferencial ni una politica de retry aplicable al reranker hibrido.

## Pool final portable v0.2

La regla historica es reconstruible: lista ordenada de profundidad 100, prefijo historico protegido de 80, fuente normativa y deduplicacion por primera aparicion. El equivalente v0.2 usa exclusivamente:

- resultados historicos congelados de Fase A, metodo `historical_bm25_data_aduanas_clase87_v0.2`;
- el artefacto ya aprobado de Fase E `hierarchical_80_dual_backfill_20` a profundidad 100 como fuente normativa cerrada equivalente.

No se vuelve a ejecutar BM25 dual ni se redefine Fase E. La columna `nandina_ref` del CSV de Fase E nunca se carga: el constructor selecciona solamente `pool_id`, `classification`, `case_id`, `depth`, `candidate_codes` y `effective_size`. El pool resultante es diagnostico, separado del ranking oficial A/F.

## Cambios del prompt

El prompt v0.2 conserva descripcion y los cuatro campos de candidato usados por el runner hibrido historico. El unico cambio es exigir exactamente diez codigos, no hasta diez. Clasificacion: **B, correccion de seguridad metodologica**. Hace verificable la clausura exigida por EXP-06; no agrega evidencia, conocimiento, candidatos, parametros ni optimizacion semantica.

La muestra v0.2 conserva el tamano diagnostico historico de 20, pero aplica muestreo aleatorio uniforme sobre case IDs ordenados y elegibles, con semilla fija `0`. Clasificacion: portabilidad necesaria por prohibicion de etiqueta; no observa resultados LLM ni referencias.
