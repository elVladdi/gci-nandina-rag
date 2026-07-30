# Evaluacion LLM rerank pool v0.1

## Objetivo

La Fase 7B evalua de forma diagnostica/acotada y preliminar si un LLM local puede reordenar candidatos NANDINA ya recuperados, sin buscar ni inventar codigos fuera del pool.

La fase usa Ollama local, no usa APIs pagadas/remotas, no usa Text2Trade, no modifica devset/evalset/Excel fuente y no cambia la estrategia del pool mirando resultados del evalset.

## Configuracion

- Modelo: `qwen2.5:7b-instruct`.
- Servicio: Ollama local en `http://127.0.0.1:11434`.
- Digest del modelo: `845dbda0ea48ed749caafd9e6037047aa19acfcfd82e704d7ca97d631a0b697e`.
- Cuantizacion: `Q4_K_M`.
- Prompt: `src/llm/rerank_nandina_prompt_v0.1.md`.
- Temperatura: `0`.
- Pool strategy: `hierarchical_80_dual_backfill_20`.
- Candidate limit: `20`.
- Casos: 13 del devset.
- Tiempo de la corrida final: aproximadamente 111 segundos.

No se enviaron 100 candidatos porque el contexto crece con la evidencia textual por candidato. Esta corrida diagnostica usa un subconjunto cerrado de 20 candidatos por caso.

## Regla de candidate_limit

Con `candidate_limit=20`, el LLM no recibio el pool completo de 100. Por ello se reporta:

- `sent_pool_at_candidate_limit = 8/13 = 0.6154`.
- Metricas condicionadas calculadas solo sobre esos 8 casos.

No se compara directamente el desempeno del LLM contra `final_pool@100 = 0.7692` del devset. La comparacion directa se hace contra el ranking original de los 20 candidatos efectivamente enviados.

## Ajustes tecnicos en devset

La primera prueba devolvio JSON parseable, pero no respetaba el esquema esperado. Se corrigio solo prompt/parsing en devset:

1. Se agrego un JSON Schema dinamico con enum cerrado a los 20 codigos enviados.
2. Se valido que `selected_nandina` coincida con rank 1.
3. Se eliminaron duplicados conservando la primera aparicion y renumerando ranks, sin agregar ni cambiar codigos.

La corrida final obtuvo JSON valido normalizado en 13/13 casos y cero codigos fuera del pool. Tres casos requirieron normalizacion de duplicados, por lo que la adherencia cruda al esquema fue 10/13 = 0.7692. Esta normalizacion permite auditar la salida, pero tambien evidencia que el prompt/schema v0.1 aun no es suficientemente estricto para una corrida final sobre evalset.

## Metricas globales

| Metrica | LLM | Ranking original enviado |
| --- | ---: | ---: |
| Casos | 13 | 13 |
| Top-1 | 0.0769 | 0.3846 |
| Top-3 | 0.0769 | 0.5385 |
| Top-5 | 0.0769 | 0.6154 |
| Top-10 | 0.0769 | 0.6154 |
| MRR | 0.0769 | 0.4679 |

Metricas de calidad:

- JSON valido despues de normalizacion: 13/13 = 1.0000.
- Adherencia cruda al esquema: 10/13 = 0.7692.
- Casos normalizados: 3.
- Codigos fuera del pool: 0.
- Casos sin respuesta valida: 0.
- Casos donde la NANDINA correcta no estaba entre los 20 enviados: 5.

## Metricas condicionadas al pool enviado

Denominador: los 8 casos donde la NANDINA correcta estaba dentro de los 20 candidatos enviados.

| Metrica | LLM condicionado | Ranking original condicionado |
| --- | ---: | ---: |
| Top-1 | 0.1250 | 0.6250 |
| Top-3 | 0.1250 | 0.8750 |
| Top-5 | 0.1250 | 1.0000 |
| Top-10 | 0.1250 | 1.0000 |
| MRR | 0.1250 | 0.7604 |

## Comparacion por caso

Sobre los 8 casos condicionados:

- Ganados por LLM: 0.
- Perdidos por LLM: 7.
- Sin cambio: 1.
- Casos donde el LLM sube la NANDINA correcta: 0.
- Casos donde el LLM baja la NANDINA correcta: 7.

El unico caso conservado fue `devset-06`, NANDINA `02013000`, que permanecio en rank 1. Entre los deterioros, el ranking original tenia la NANDINA correcta en rank 1 para `devset-01`, `devset-02`, `devset-03` y `devset-04`, pero el LLM no la incluyo en su ranking devuelto.

## Limitaciones metodologicas

Esta corrida no debe interpretarse como validacion final del componente LLM+RAG. Quedan limitaciones que deben corregirse antes de escalar:

- El runner no fijo `num_ctx` explicitamente en Ollama; por tanto, el contexto efectivo puede no haber usado toda la ventana disponible del modelo.
- El esquema permitia `ranked_candidates` con minimo 1 y maximo 10 elementos, no exactamente 10; por ello Top-3, Top-5 y Top-10 no son una comparacion perfecta contra el ranking original enviado.
- El LLM recibio solo 20 candidatos por caso, no el pool completo de 100.
- La fase no evalua calidad de justificacion ni concordancia evidencia-justificacion; solo re-ranking cerrado sobre devset.

## Decision sobre evalset

No se ejecuto evalset.

Aunque el JSON normalizado fue valido en 100% y no hubo codigos fuera del pool, la adherencia cruda al esquema fue 76.9%, por debajo del umbral de 90%. Ademas, el LLM no gano ningun caso y deterioro 7 de 8 casos condicionados. Ejecutar 600 casos no esta metodologicamente justificado con esta configuracion.

## Conclusion

`qwen2.5:7b-instruct` con el prompt v0.1 y 20 candidatos no mejora el ordenamiento cuando el codigo correcto esta disponible. El ranking documental original supera ampliamente al re-ranking LLM tanto globalmente como condicionado al pool enviado en esta configuracion.

Fase 7B queda cerrada como diagnostico preliminar negativo para esta configuracion, no como descarte definitivo del uso de LLM. Antes de una nueva prueba conviene mejorar el diseno de evidencia/prompt, fijar `num_ctx`, exigir una salida exactamente comparable y validar primero en devset. La prioridad general sigue siendo mejorar recuperacion: el pool de evalset completo solo contiene la NANDINA correcta en 160/600 casos.

## Artefactos

- `src/llm/rerank_nandina_prompt_v0.1.md`.
- `src/experiments/run_llm_rerank_pool_devset.py`.
- `src/experiments/evaluate_llm_rerank_pool.py`.
- `outputs/evaluation/llm_rerank_pool_devset_v0.1/`.
