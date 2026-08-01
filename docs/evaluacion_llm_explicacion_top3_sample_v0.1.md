# Evaluacion LLM explicacion Top-3 sample v0.1

## Objetivo de Fase 10A

Fase 10A implementa una primera evaluacion diagnostica de LLM+RAG para explicacion auditable comparativa del Top-3 NANDINA recuperado por el ranking historico base `data_aduanas` clase 87.

El LLM no busca NANDINA, no clasifica desde cero y no reordena candidatos. Su rol queda limitado a explicar, comparar y declarar incertidumbre sobre los tres candidatos ya recuperados.

## Por que explicacion y no recuperacion/re-ranking

La recuperacion historica real de Fase 9A ya alcanzo `Top-1 = 0.8638`, `Top-3 = 0.9384`, `Top-10 = 0.9791`, `Recall@100 = 0.9980` y `MRR = 0.9071`. Fase 9C-A mostro que usar el LLM como re-ranker degrada Top-1 y MRR.

Por eso Fase 10A conserva el orden historico como decision operativa temprana y usa el LLM solo para generar justificacion textual estructurada con evidencia normativa entregada en el payload.

## Modelo usado

- Modelo local: `qwen2.5:7b-instruct`.
- Runtime: Ollama local en `127.0.0.1:11434`.
- Temperatura: `0`.
- Politica: sin OpenAI, sin APIs remotas, sin descargas y sin servicios con costo.

## Muestra

La muestra diagnostica contiene 30 casos del evalset `data_aduanas` clase 87:

| Categoria objetivo | Casos |
| --- | ---: |
| Correcta en rank 1 historico | 10 |
| Correcta en rank 2-3 historico | 10 |
| Correcta en rank 4-10 historico | 5 |
| Dificiles o bajo soporte historico | 5 |

El balance se logro exactamente. La seleccion fue deterministica: se priorizaron casos con menor soporte historico, luego rank historico y finalmente `case_id`. La etiqueta esperada queda en `sample_cases.csv` para auditoria, pero no se entrega al LLM en `payloads.jsonl`.

## Estructura del prompt

El prompt versionado esta en `src/llm/explain_top3_nandina_prompt_v0.1.md`. Exige JSON estricto con:

- `id_unico`.
- `descripcion_mercancia`.
- `candidatos_explicados`, con tres objetos y `rank_original` 1, 2 y 3.
- `soporte` restringido a `alto`, `medio` o `bajo`.
- `coincidencias`, `diferencias_o_dudas`, `evidencias_usadas` y `justificacion`.
- `comparacion_top3`.
- `advertencias`.

## Controles anti-invencion

Los payloads fijan explicitamente el Top-3 original. El evaluador verifica:

- JSON valido.
- Tres candidatos explicados completos.
- Respeto del Top-3 original.
- No agregar candidatos fuera del pool.
- No cambiar ranking.
- No inventar codigos.
- Evidencia normativa citada por candidato.
- Comparacion Top-3 presente.
- Advertencias e incertidumbre cuando corresponda.

## Metricas de calidad

| Metrica | Valor |
| --- | ---: |
| Casos procesados | 30 |
| JSON valido | 1.0000 |
| Candidatos explicados completos | 1.0000 |
| Respeta Top-3 original | 1.0000 |
| No agrega candidatos fuera del pool | 1.0000 |
| No cambia ranking | 1.0000 |
| No inventa codigos | 1.0000 |
| Evidencia citada por candidato | 0.9000 |
| Advertencias emitidas | 0.1333 |
| Diferencias o dudas presentes | 1.0000 |
| Comparacion Top-3 presente | 0.9667 |

Distribucion de soporte en 90 candidatos explicados:

| Soporte | Candidatos |
| --- | ---: |
| alto | 26 |
| medio | 30 |
| bajo | 34 |

Fallos detectados:

| Tipo | Casos |
| --- | ---: |
| `evidencia_no_citada_por_candidato` | 3 |
| `comparacion_top3_ausente` | 1 |

## Ejemplos breves

Salida correcta resumida: `DA-EVAL-00047` conserva `87024090`, `87031000`, `87046010` en ranks 1, 2 y 3; asigna soportes `alto`, `medio`, `bajo`; compara los tres candidatos sin reordenarlos.

Salida correcta con advertencia: `DA-EVAL-00059` conserva `87032410`, `87032390`, `87032310`; declara duda sobre cilindrada y mantiene comparacion Top-3.

Salida incorrecta resumida: `DA-EVAL-00088` conserva el Top-3, pero no cumple evidencia citada por candidato y deja ausente la comparacion Top-3. El caso se cuenta como fallo estructural parcial.

## Limitaciones

- Es una muestra diagnostica pequena, no el evalset completo.
- La evaluacion mide estructura y auditabilidad basica, no verdad juridica de la explicacion.
- El umbral de evidencia citada pasa justo en 0.9000; conviene reforzar el prompt antes de escalar.
- La evidencia normativa disponible puede ser breve o generica para algunas NANDINAS.
- El LLM no corrige errores de recuperacion; solo explica el Top-3 recibido.

## Decision

Fase 10A pasa a Fase 10B como explicacion controlada. La condicion es mantener el LLM como justificador de candidatos ya recuperados, no como recuperador, clasificador ni re-ranker, y reforzar en 10B la citacion obligatoria de evidencia por candidato.

## Outputs

Outputs regenerables e ignorados por Git:

```text
outputs/evaluation/llm_explanation_top3_sample_v0.1/
```

Archivos principales:

- `sample_cases.csv`
- `payloads.jsonl`
- `llm_explanations.jsonl`
- `llm_explanations.csv`
- `explanation_quality_metrics.json`
- `explanation_quality_summary.md`
- `case_quality_summary.csv`
