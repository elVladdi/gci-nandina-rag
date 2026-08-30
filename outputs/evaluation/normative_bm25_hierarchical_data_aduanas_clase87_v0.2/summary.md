# EXP-04 Fase C - BM25 normativo jerarquico data_aduanas clase 87 v0.2

## Alcance

Se evaluo exclusivamente BM25 normativo jerarquico sobre el evalset data_aduanas clase 87 v0.2. No se ejecuto BM25 dual protegido, mezcla 70/30, union diagnostica, Text2Trade, dense retrieval, candidate pools, integracion historico-normativa, RAG, reranking LLM ni explicador LLM.

## Pipeline jerarquico

- Constructor de corpus: `src/corpus/build_hierarchical_nandina_corpus.py`.
- Constructor de indice: `src/experiments/build_bm25_hierarchical_index.py`.
- Runner exclusivo Fase C: `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`.
- Modulo BM25: `src/bm25_index.py` y `src/retrieval/bm25.py`.
- Corpus: `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.
- Corpus SHA-256: `f389ae6c303279cfea23697cbedb3315a5254254c2efc2450cf28f81243df175`.
- Indice: `data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl`.
- Indice SHA-256: `f828736ea700471c95d2b985bdd969d751cd36c3ca01c407049209010bdbe60b`.
- Version normativa en corpus: hierarchical_v0.1.
- Fuente: NANDINA.
- Unidad documental: one hierarchical document row per NANDINA-8 source row; effective evaluation collapses duplicate rows to unique NANDINA-8 codes by first BM25 score occurrence.
- Regla de texto: Seccion + Capitulo + Partida 4D + Subpartida HS6 nullable + NANDINA 8D + Unidad fisica, deduplicated by normalized text fragment.

## Auditoria del corpus

- Documentos jerarquicos totales: 7648.
- Documentos NANDINA-8: 7648.
- Codigos NANDINA-8 unicos: 7644.
- Codigos con multiples documentos: 2.
- Sin padre 4D explicito: 407.
- Sin padre HS6 explicito: 4504.
- Sin ambos padres: 185.
- Conflictos en auditoria fuente: 56.

## Evalset y query

- Evalset: `data/processed/data_aduanas_evalset_clase87_v0.2.csv`.
- Evalset SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- Casos evaluados: 1056.
- Query: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta: `NANDINA`.
- Profundidad efectiva: 200.

## Resultado global

| Metrica | Numerador | Denominador | Valor |
| --- | ---: | ---: | ---: |
| mrr_at_100 | 44.33224687474574 | 1056 | 0.041981294389 |
| mrr_at_200 | 45.76874185264425 | 1056 | 0.043341611603 |
| top_1 | 28 | 1056 | 0.026515151515 |
| top_3 | 55 | 1056 | 0.052083333333 |
| top_5 | 66 | 1056 | 0.062500000000 |
| top_10 | 69 | 1056 | 0.065340909091 |
| top_50 | 96 | 1056 | 0.090909090909 |
| recall_at_100 | 107 | 1056 | 0.101325757576 |
| pool_recall_at_200 | 321 | 1056 | 0.303977272727 |
| hs6_at_100 | 118 | 1056 | 0.111742424242 |
| hs4_at_100 | 264 | 1056 | 0.250000000000 |
| chapter_at_100 | 538 | 1056 | 0.509469696970 |
| hs6_at_200 | 363 | 1056 | 0.343750000000 |
| hs4_at_200 | 529 | 1056 | 0.500946969697 |
| chapter_at_200 | 810 | 1056 | 0.767045454545 |

El campo historico `mrr` en JSON se conserva como alias de MRR@200 porque Fase C corrio con depth 200. Para comparacion contra BM25 plano Fase B se usa exclusivamente MRR@100.

## Cobertura jerarquica

- Referencias en corpus: 1056/1056.
- Codigos unicos del evalset: 42.
- Codigos del evalset presentes como NANDINA-8 exacto en corpus: 42/42.
- Parent codes no cuentan como cobertura exacta.
- Exact@100: 107/1056 = 0.101325757576.
- HS6@100: 118/1056 = 0.111742424242.
- HS4@100: 264/1056 = 0.250000000000.
- Chapter@100: 538/1056 = 0.509469696970.
- Exact@200: 321/1056 = 0.303977272727.
- HS6@200: 363/1056 = 0.343750000000.
- HS4@200: 529/1056 = 0.500946969697.
- Chapter@200: 810/1056 = 0.767045454545.

## Comparacion plano vs jerarquico

| Metrica | Plano v0.2 | Jerarquico v0.2 | Delta |
| --- | ---: | ---: | ---: |
| Top-1 | 0.027462121212 | 0.026515151515 | -0.000946969697 |
| Top-3 | 0.051136363636 | 0.052083333333 | 0.000946969697 |
| Top-5 | 0.061553030303 | 0.062500000000 | 0.000946969697 |
| Top-10 | 0.065340909091 | 0.065340909091 | 0.000000000000 |
| Top-50 | 0.070075757576 | 0.090909090909 | 0.020833333333 |
| Recall@100 | 0.071022727273 | 0.101325757576 | 0.030303030303 |
| MRR@100 | 0.042297317267 | 0.041981294389 | -0.000316022878 |

Recall@200 y MRR@200 se reportan solo para jerarquico porque no existe artefacto BM25 plano depth 200 en Fase B.

## Cobertura comparable plano vs jerarquico

| Cobertura | Plano | Jerarquico | Delta |
| --- | ---: | ---: | ---: |
| Exact@100 | 0.071022727273 | 0.101325757576 | 0.030303030303 |
| HS-6@100 | 0.093750000000 | 0.111742424242 | 0.017992424242 |
| HS-4@100 | 0.208333333333 | 0.250000000000 | 0.041666666667 |
| Chapter@100 | 0.763257575758 | 0.509469696970 | -0.253787878788 |

## Compatibilidad

- Mismo set case_id historico/plano/jerarquico: True.
- Mismas etiquetas por case_id: True.
- Eval hash historico/plano/jerarquico: 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941 / 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941 / 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941.
- Compatible: True.

## Microauditoria Gate C

- MRR@100 recalculado desde `normative_hierarchical_case_summary.csv`: 0.041981294389.
- MRR@200 recalculado desde `normative_hierarchical_case_summary.csv`: 0.043341611603.
- Contribucion de ranks 101-200 al MRR legacy: 0.001360317214.
- Metricas jerarquicas recalculadas desde `normative_hierarchical_results.csv`.
- Distribucion de rank suma 1056 casos.
- Archivo grande: `normative_hierarchical_results.csv`, 85426164 bytes, 81.47 MiB aprox.; no fue modificado ni eliminado.

## Controles

- No se uso descripcion comercial evaluada para construir corpus.
- No se uso NANDINA verdadera como parte de la query.
- No se usaron DAM, SERIE, resultado historico, Top-3 historico ni outputs de otra estrategia como features de recuperacion.
- El ranking efectivo elimina codigos repetidos por primera aparicion BM25 antes de calcular metricas.
- Los hashes de Fase A/B permanecen iguales a los aprobados.

## Estado Gate C

GATE C APROBADO
