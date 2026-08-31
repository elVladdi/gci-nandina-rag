# EXP-04 Fase K: evaluación cualitativa HE4 v0.2

## Procedencia y limitación

La puntuación recibida fue realizada por `AI_EXPERT_ROLE` (`independent_ai_reviewer_01`), no por la modalidad `HUMAN/MANUAL REVIEW` preparada originalmente. Esto se registra como `EVALUATOR_MODALITY_DEVIATION`; no se modificaron los scores ni justificaciones recibidos.

No se expusieron ground truth, rank de referencia ni buckets durante la puntuación; tampoco se utilizó evidencia externa, web o retrieval. `advertencias_globales` permanece excluido por `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`.

## Resultado

- Casos auditables: 28/50 (56.0%).
- No auditables: 22/50 (44.0%).
- Total: media 11.72, mediana 12.0, rango 6-15.
- Hard violations: 0.

## Dimensiones

| Dimensión | 0 | 1 | 2 | Media | Mediana |
| --- | ---: | ---: | ---: | ---: | ---: |
| trazabilidad | 0 | 0 | 50 | 2.00 | 2.0 |
| verificabilidad | 24 | 25 | 1 | 0.54 | 1.0 |
| separacion_historico_normativo | 13 | 22 | 15 | 1.04 | 1.0 |
| prudencia_de_la_conclusion | 0 | 11 | 39 | 1.78 | 2.0 |
| consistencia_con_top3_fijo | 0 | 2 | 48 | 1.96 | 2.0 |
| deteccion_de_evidencia_normativa_generica | 4 | 8 | 38 | 1.68 | 2.0 |
| comparacion_entre_candidatos | 0 | 27 | 23 | 1.46 | 1.0 |
| utilidad_para_auditoria_humana | 1 | 35 | 14 | 1.26 | 1.0 |

## Comparación con advertencias J

| Grupo J | Casos | Auditables | Tasa | Media total |
| --- | ---: | ---: | ---: | ---: |
| generic_normative_warning_missing | 9 | 1 | 11.1% | 9.67 |
| other_cases | 41 | 27 | 65.9% | 12.17 |

## Dictamen HE4

HE4 se clasifica como `PARTIALLY SUPPORTED`: J preserva los controles estructurales relevantes, mientras K aporta 28 fichas auditables bajo la regla congelada. El resultado conserva tanto la limitación prompt-schema de J como la desviación de modalidad del evaluador en K.
