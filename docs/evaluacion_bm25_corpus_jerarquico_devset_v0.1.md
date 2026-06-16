# Evaluacion BM25 corpus jerarquico devset v0.1

## Objetivo

Comparar el ranking BM25 inicial actual contra un indice BM25 construido sobre un corpus NANDINA8 con contexto jerarquico 4D/6D/8D. La evaluacion usa solo el devset intermedio de 13 casos; no se ejecuto evalset, LLM ni Text2Trade.

## Por que se reconstruyo el corpus

El corpus plano actual indexa varias subpartidas con textos demasiado breves, por ejemplo `Solido`, `Ruedas` o `Los demas`. El corpus jerarquico agrega seccion, capitulo, partida 4D, HS6 cuando existe, descripcion NANDINA8 y unidad fisica en `texto_index_jerarquico`.

## Metricas comparativas

| Metrica | BM25 actual | BM25 jerarquico | Delta |
|---|---:|---:|---:|
| Top-1 | 0.3846 | 0.3846 | +0.0000 |
| Top-3 | 0.4615 | 0.5385 | +0.0769 |
| Top-5 | 0.4615 | 0.6154 | +0.1538 |
| Top-10 | 0.5385 | 0.6154 | +0.0769 |
| MRR | 0.4370 | 0.4701 | +0.0331 |
| Recall@50 | 0.6154 | 0.6923 | +0.0769 |
| Recall@100 | 0.6154 | 0.6923 | +0.0769 |
| Top-10 HS4 | 0.8462 | 0.7692 | -0.0769 |
| Top-10 HS2 | 0.8462 | 0.7692 | -0.0769 |

## Casos ganados y perdidos

- Ganados: 4.
- Perdidos: 2.
- Sin cambio: 7.
- Antes no encontrados y ahora encontrados: 1.
- Casos degradados: 2.

## Ejemplos concretos

- `28151100`: antes el texto plano era `Solido`; despues queda enriquecido con la partida 28.15 sobre hidroxido de sodio, sosa o soda caustica, mas la forma solida.
- `Los demas`: las descripciones genericas dejan de depender solo de la frase generica porque el texto indexable incorpora el contexto de partida/capitulo disponible.

## Smoke tests

- Consulta `soda caustica solida`: BM25 actual rank 0; jerarquico rank 3.
- Consulta `ruedas`: BM25 actual rank 1; jerarquico rank 5.

## Decision metodologica

No escalar todavia al evalset como sustituto directo: revisar degradaciones del devset y considerar una variante hibrida que preserve senales cortas utiles del corpus plano.

## Limitaciones

- El devset tiene 13 casos y solo sirve como senal temprana.
- La cobertura HS6 del JSONL intermedio es incompleta; muchos registros usan contexto 4D sin HS6 explicito.
- La comparacion no valida fundamento legal ni clasificacion oficial, solo recuperacion lexical BM25.
