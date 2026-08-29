# Microauditoria BM25 normativo plano v0.2 a nivel de codigo

## Resultado

Gate B endurecido: APPROVED.

## Corpus 7748 vs 7644

El corpus `data/processed/corpus_rag_v1_index.jsonl` contiene 7748 registros totales. De ellos, 7644 son `tipo = nandina_8` y 104 son registros no NANDINA-8: {'nandina_8': 7644, 'nota_capitulo': 87, 'nota_seccion': 9, 'rgi': 6, 'rgi_contexto': 2}.

No hay codigos NANDINA-8 repetidos: 7644 codigos unicos, multiplicidad maxima 1 y distribucion {'1': 7644}.

## Unidad de ranking

BM25 devuelve hits documentales (`doc_idx`, score). `src/retrieval/bm25.py` traduce cada `doc_idx` a `index.doc_ids[doc_idx]` como codigo. En el indice plano usado por Fase B hay un documento por codigo NANDINA-8, por lo que el ranking efectivo es un ranking de codigos no repetidos. No existe deduplicacion posterior porque no hay duplicados de codigo en el indice.

Casos evaluados: 1056. Casos con codigos repetidos en ranking efectivo: 0. Maxima repeticion de un mismo codigo dentro de un caso: 1. La primera aparicion del codigo de referencia coincide con `rank_ref`: True.

## Metricas recalculadas

| Metrica | Numerador | Denominador | Valor |
|---|---:|---:|---:|
| Top-1 | 29 | 1056 | 0.027462121212121212 |
| Top-3 | 54 | 1056 | 0.05113636363636364 |
| Top-5 | 65 | 1056 | 0.061553030303030304 |
| Top-10 | 69 | 1056 | 0.06534090909090909 |
| Top-50 | 74 | 1056 | 0.07007575757575757 |
| Recall@100 | 75 | 1056 | 0.07102272727272728 |
| MRR | 44.66596703438809 | 1056 | 0.04229731726741296 |

## Cobertura NANDINA-8

`normative_target_digits = 8` y `normative_supported_digits_for_primary_baseline = 8`. Los 42 codigos del evalset tienen entrada NANDINA-8 en el corpus; no se contabilizo cobertura por padre HS-6.
