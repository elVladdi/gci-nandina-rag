# EXP-04 Fase A - BM25 historico data_aduanas clase 87 v0.2

## Alcance

Se evaluo exclusivamente BM25 historico sobre el split congelado v0.2. No se uso BM25 normativo, BM25 jerarquico, Text2Trade, pools hibridos, RAG, reranking LLM, explicador LLM ni APIs remotas.

## Validacion de entrada

- Historico v0.2: 2950 series, sha256 `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- Evaluacion v0.2: 1056 series, sha256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- Codigos NANDINA en evaluacion: 42.
- Casos de evaluacion con soporte historico: 1056.
- Solapamiento `id_unico` historico/evaluacion: 0.
- Profundidad Top-50 habilitada: True.

## Resultado global

| Metrica | Numerador | Denominador | Valor |
| --- | ---: | ---: | ---: |
| mrr | 664.9713833162234 | 1056 | 0.629708 |
| exact_at_1 | 538 | 1056 | 0.509470 |
| exact_at_3 | 709 | 1056 | 0.671402 |
| exact_at_5 | 806 | 1056 | 0.763258 |
| exact_at_10 | 941 | 1056 | 0.891098 |
| exact_at_50 | 1047 | 1056 | 0.991477 |
| partida_at_10 | 1055 | 1056 | 0.999053 |
| sub_partida_at_10 | 990 | 1056 | 0.937500 |
| clase_at_10 | 1056 | 1056 | 1.000000 |
| partida_at_50 | 1056 | 1056 | 1.000000 |
| sub_partida_at_50 | 1056 | 1056 | 1.000000 |
| clase_at_50 | 1056 | 1056 | 1.000000 |

## Duplicados y soporte

- Casos con duplicado exacto historico-evaluacion: 35.
- Casos con near duplicate historico-evaluacion >=0.95: 44.
- Casos con al menos 50 candidatos BM25 unicos: 1010.

## Decision

BM25 historico v0.2 mantiene una recuperacion fuerte sobre evaluacion v0.2 y queda habilitado como baseline historico congelado para comparaciones posteriores, sin activar componentes normativos ni LLM.
