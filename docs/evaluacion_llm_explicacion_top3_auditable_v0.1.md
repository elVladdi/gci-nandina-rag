# Evaluacion LLM explicacion Top-3 auditable v0.1

## Objetivo

La Fase 10B implementa una version formal de explicacion auditable LLM+RAG sobre el Top-3 historico recuperado para `data_aduanas` clase 87 corregido. El objetivo es producir dos salidas complementarias:

- JSON tecnico reproducible para evaluacion automatica.
- Fichas auditables legibles para revision humana.

El LLM no busca NANDINA, no clasifica desde cero y no reordena candidatos. Recibe solamente los tres candidatos ya recuperados por el ranking historico base y los explica con evidencia historica y normativa incluida en el payload.

## Relacion con Fase 10A

Fase 10A queda como diagnostico previo. Mostro que `qwen2.5:7b-instruct` via Ollama local podia generar JSON valido, preservar Top-3 y no inventar codigos, pero la citacion de evidencia y la comparacion eran todavia ligeras.

Fase 10B no reinterpreta retroactivamente 10A. La extiende con:

- Prompt v0.2 mas estricto.
- Muestra de 50 casos.
- Separacion de evidencia historica y normativa por candidato.
- Conservacion obligatoria de `candidate_id_unico` y `evidence_id`.
- Rubrica formal de estructura, trazabilidad, pertinencia, comparacion e incertidumbre.
- Fichas auditables por caso.

## Antecedentes usados

La lectura local de antecedentes inspiro el diseno en cinco puntos:

- `Explainable Product Classification for Customs.pdf`: utilidad de precedentes clasificados y explicaciones interpretables para reducir esfuerzo de revision experta.
- `Classification of Goods Using Text Descriptions With Sentences Retrieval.pdf`: valor de recuperar descripciones historicas similares como soporte de decision.
- `A Deterministic Agentic Workflow for HS Tariff Classification.pdf`: necesidad de flujos deterministas y controlados frente a prompting libre.
- `Consensus-based Agentic LLM Framework for Harmonized Tariff Schedule Code Classification.pdf`: importancia de evidencia, incertidumbre y escalamiento humano en tareas arancelarias.
- `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification.pdf`: necesidad de rutas jerarquicas validas y evidencia auditable en clasificacion regulatoria fina.
- `ICCA-RAG Intelligent Customs Clearance Assistant Using RAG.pdf`: separacion entre recuperacion documental y generacion basada en contexto, con foco en fidelidad de respuesta.

## Por que el LLM no recupera ni reordena

Las metricas corregidas de Fase 9A sobre `data_aduanas` clase 87 muestran que el historico real ya domina como ranking operativo:

| Metrica | Valor |
| --- | ---: |
| Top-1 | 0.8628 |
| Top-3 | 0.9374 |
| Top-10 | 0.9801 |
| Recall@100 | 1.0000 |
| MRR | 0.9062 |

Fase 9B recomendo `historical_with_normative_backfill_if_missing_code`: historico como ranking principal y normativo como backfill, trazabilidad y evidencia documental. Ademas, Fase 9C-A mostro que usar el LLM como re-ranker degrada Top-1/MRR. Por eso 10B limita el LLM a explicar el Top-3 fijo.

## Muestra y criterio

La muestra contiene 50 casos del evalset `data_aduanas` clase 87 corregido. La seleccion fue deterministica con `seed = 2026`, ordenando por bucket de soporte historico, cantidad de soporte, rank exacto y `case_id`.

| Estrato objetivo | Casos |
| --- | ---: |
| NANDINA correcta en rank 1 historico | 15 |
| NANDINA correcta en rank 2-3 historico | 15 |
| NANDINA correcta en rank 4-10 historico | 10 |
| Casos dificiles o de bajo soporte historico | 10 |

El balance se logro exactamente, sin fallback. Disponibilidad por estrato: rank 1 = 868, rank 2-3 = 75, rank 4-10 = 43, dificil/bajo soporte = 61.

La etiqueta esperada se conserva solo en `sample_cases.csv` para auditoria. No se envia al LLM en `payloads.jsonl`.

Correccion metodologica menor: la nota de control del payload fue cambiada a `Payload limitado a datos observables, candidatos Top-3 y evidencias recuperadas.`. Con ello el payload ya no contiene terminos asociados a etiquetas esperadas ni variables de resultado, ni siquiera en texto explicativo no informativo.

## Prompt v0.2

El prompt versionado esta en:

```text
src/llm/explain_top3_nandina_prompt_v0.2.md
```

El prompt exige JSON estricto, explicacion por candidato, cita de `candidate_id_unico`, cita de `evidence_id`, comparacion Top-3 con criterios explicitos, advertencias ante evidencia normativa generica como "Los demas", advertencias ante datos faltantes y prohibicion explicita de reordenar, agregar candidatos, inventar codigos o emitir clasificacion oficial.

Durante la corrida se reforzo una regla del mismo prompt v0.2: `comparacion_top3.criterios_comparados` no puede quedar vacio. La primera ejecucion habia generado 50 JSON validos y trazables, pero 7 casos dejaron esa lista vacia; por rubrica, se considero fallo real y se regenero la corrida completa.

Tras la correccion de la nota del payload se regenero Fase 10B completa. Las metricas duras de paso a 10C se mantienen cumplidas; el score promedio de auditabilidad cambia levemente de 0.9560 a 0.9520 por variacion de la nueva corrida local.

## Estructura JSON

La salida esperada incluye:

- `id_unico`, `case_id` y `descripcion_mercancia`.
- `resumen_observable`.
- `candidatos_explicados`, con tres candidatos en ranks 1, 2 y 3.
- `ruta_jerarquica` por candidato.
- `soporte` restringido a `alto`, `medio` o `bajo`.
- `evidencia_historica_usada`, con `candidate_id_unico`.
- `evidencia_normativa_usada`, con `evidence_id`.
- `coincidencias`, `diferencias_o_dudas`, `razon_de_soporte` y `advertencias`.
- `comparacion_top3`.
- `conclusion_auditable`.
- `advertencia_final`.

## Ficha auditable

Cada ficha integra identificacion del caso, descripcion observada, Top-3 recibido por el LLM, respuesta parseada, evidencias citadas y controles de calidad del evaluador.

Ejemplos:

- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00047.md`
- `outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards/DA-EVAL-00059.md`

Indice general:

```text
outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/audit_cards.md
```

## Rubrica

La rubrica evalua:

- Estructura: JSON valido, 3 candidatos presentes, orden Top-3 intacto, sin candidatos fuera del pool y sin codigos inventados.
- Trazabilidad: evidencia historica y normativa citada por candidato, conservando `candidate_id_unico` y `evidence_id`.
- Pertinencia: coincidencias y diferencias observables, sin atributos inventados segun controles heuristicos.
- Comparacion: Top-3 comparado con criterios explicitos y explicacion de menor soporte de alternativos.
- Incertidumbre: advertencias ante evidencia generica, datos faltantes y uso de soporte bajo/medio cuando corresponde.

## Metricas

| Metrica | Valor |
| --- | ---: |
| Casos procesados | 50 |
| JSON valido | 1.0000 |
| Top-3 completo | 1.0000 |
| Ranking preservado | 1.0000 |
| Sin codigos fuera del pool | 1.0000 |
| Sin codigos inventados | 1.0000 |
| Evidencia historica citada por candidato | 1.0000 |
| Evidencia normativa citada por candidato | 1.0000 |
| Comparacion Top-3 presente | 1.0000 |
| Conclusion auditable presente | 1.0000 |
| Advertencia final presente | 1.0000 |
| Sin clasificacion oficial | 1.0000 |
| Sin senales de re-ranking | 1.0000 |
| Score promedio de auditabilidad por caso | 0.9520 |

Distribucion de soporte en 150 candidatos explicados:

| Soporte | Candidatos | Tasa |
| --- | ---: | ---: |
| alto | 31 | 0.2067 |
| medio | 51 | 0.3400 |
| bajo | 68 | 0.4533 |

Otros controles:

| Control | Valor |
| --- | ---: |
| Candidatos con advertencias | 0.4800 |
| Coincidencias observables presentes | 0.5800 |
| Diferencias observables presentes | 1.0000 |
| Advertencia ante normativa generica cuando aplica | 0.7200 |
| Advertencia de datos faltantes | 0.4400 |

Fallos secundarios:

| Tipo | Casos |
| --- | ---: |
| `conclusion_auditable_missing` | 1 |
| `generic_normative_warning_missing` | 14 |
| `missing_data_warning_absent` | 28 |
| `observable_matches_missing` | 21 |

Estos fallos no afectan los criterios duros de paso a 10C, pero son utiles para reforzar explicaciones cualitativas futuras.

## Outputs

Outputs regenerables e ignorados por Git:

```text
outputs/evaluation/llm_explanation_top3_audit_sample_v0.1/
```

Archivos generados:

- `sample_cases.csv`
- `payloads.jsonl`
- `llm_explanations.jsonl`
- `llm_explanations.csv`
- `audit_quality_metrics.json`
- `audit_quality_summary.md`
- `case_audit_quality_summary.csv`
- `audit_cards.md`
- `audit_cards/` con 50 fichas Markdown.

## Validaciones

- `ast.parse` ejecutado sobre los cuatro scripts nuevos.
- `payloads.jsonl` contiene 50 casos.
- `llm_explanations.jsonl` contiene 50 respuestas.
- `audit_cards.md` existe.
- `audit_cards/` contiene 50 fichas `.md`.
- El constructor valida nombres de claves estructurales prohibidas de forma recursiva, sin depender de substrings en notas explicativas.
- `payloads.jsonl` no contiene `expected_nandina`, `nandina_esperada`, `expected_rank_historical`, `exact_rank`, `acierto` ni `error`, ni como clave ni como texto.
- No se envian etiquetas esperadas ni variables de resultado al LLM.
- No se uso OpenAI, APIs remotas ni servicios con costo.
- El runner solo permite URLs Ollama locales.

## Limitaciones

- La evaluacion mide auditabilidad estructural y trazabilidad, no verdad juridica de la clasificacion.
- La pertinencia semantica se evalua con controles heuristicos; la revision experta sigue siendo necesaria.
- Algunas respuestas aun omiten coincidencias observables explicitas o advertencias de datos faltantes.
- La evidencia normativa puede ser generica para codigos residuales.
- La muestra es balanceada y controlada, no reemplaza una evaluacion temporal o sobre el evalset completo.

## Decision

Fase 10B pasa metodologicamente a Fase 10C. Cumple los umbrales formales: JSON valido >= 0.95, Top-3 preservado = 1.00, sin codigos fuera del pool = 1.00, evidencia historica y normativa citada por candidato >= 0.95, comparacion Top-3 presente >= 0.95, advertencia final presente >= 0.95 y sin senales de re-ranking ni clasificacion oficial.
