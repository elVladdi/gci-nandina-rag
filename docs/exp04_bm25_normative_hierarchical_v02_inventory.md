# EXP-04 Fase C - BM25 normativo jerarquico v0.2

## Estado

GATE C APROBADO.

## Pipeline jerarquico identificado

- Constructor de corpus: `src/corpus/build_hierarchical_nandina_corpus.py`.
- Corpus jerarquico: `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.
- Constructor de indice: `src/experiments/build_bm25_hierarchical_index.py`.
- Indice BM25: `data/processed/indexes/bm25_nandina8_hierarchical_v0.1.pkl`.
- Runner exclusivo Fase C v0.2: `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`.
- Modulos BM25 reutilizados: `src/bm25_index.py`, `src/retrieval/bm25.py`.
- Configuracion: `src/configs/experiment_config.json`.
- Auditoria versionada fuente: `outputs/corpus/auditoria_nandina_jerarquica_v0.1/audit_summary.json`.

## Corpus congelado

- Path: `data/processed/corpus_nandina_hierarchical_v0.1.jsonl`.
- SHA-256: `f389ae6c303279cfea23697cbedb3315a5254254c2efc2450cf28f81243df175`.
- Registros totales: 7648.
- Documentos NANDINA-8: 7648.
- Codigos NANDINA-8 unicos: 7644.
- Codigos con multiples documentos: 2 (`48051900`, `84472010`).
- Version: `hierarchical_v0.1`.
- Fuente: `NANDINA`.
- Longitud texto jerarquico: min 130, mediana 328, max 16809.
- Campos: `section`, `section_title`, `chapter`, `chapter_title`, `partida_4d`, `descripcion_partida_4d`, `hs_6d`, `descripcion_hs_6d`, `nandina_8d`, `descripcion_nandina_8d`, `unidad_fisica`, `texto_index_jerarquico`.

## Construccion documental

Cada documento NANDINA-8 concatena seccion, capitulo, partida HS-4, HS-6 cuando existe, descripcion NANDINA-8 y unidad fisica. Las partes se deduplican por texto normalizado. No se agregan notas independientes; el contexto normativo puede aparecer solo si ya estaba embebido en descripciones extraidas.

La unidad final evaluada es codigo NANDINA-8 unico. Como el corpus heredado contiene documentos multiples para dos codigos, Fase C colapsa el ranking efectivo por primera aparicion BM25 antes de calcular Top-k, MRR y cobertura.

## Advertencias heredadas

- NANDINA-8 sin padre 4D explicito: 407.
- NANDINA-8 sin padre HS6 explicito: 4504.
- Sin ambos padres: 185.
- Grupos con descripciones conflictivas en auditoria fuente: 56.
- Posible contaminacion por encabezados en auditoria fuente: 17.
- Descripciones genericas o cortas fuente: 3498.

No se corrigieron estos problemas en Fase C.

## Comando

```powershell
& 'C:\Users\Vladimir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m src.experiments.evaluate_normative_bm25_hierarchical_data_aduanas_v02 --retrieval-depth 200
```

## Evalset

- Path: `data/processed/data_aduanas_evalset_clase87_v0.2.csv`.
- SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- Casos: 1056.
- Codigos NANDINA-8 unicos: 42.
- Query: `DESCRIPCION DE MERCANCIAS CONCATENADA`.
- Etiqueta: `NANDINA`.

## Metricas Fase C

| Metrica | Numerador | Denominador | Valor |
| --- | ---: | ---: | ---: |
| Top-1 | 28 | 1056 | 0.026515151515151516 |
| Top-3 | 55 | 1056 | 0.052083333333333336 |
| Top-5 | 66 | 1056 | 0.0625 |
| Top-10 | 69 | 1056 | 0.06534090909090909 |
| Top-50 | 96 | 1056 | 0.09090909090909091 |
| Recall@100 | 107 | 1056 | 0.10132575757575757 |
| Pool/Recall@200 | 321 | 1056 | 0.3039772727272727 |
| MRR | 45.76874185264425 | 1056 | 0.04334161160288281 |

## Cobertura jerarquica

| Cobertura | Numerador | Denominador | Valor |
| --- | ---: | ---: | ---: |
| Exact@100 | 107 | 1056 | 0.10132575757575757 |
| HS6@100 | 118 | 1056 | 0.11174242424242424 |
| HS4@100 | 264 | 1056 | 0.25 |
| Chapter@100 | 538 | 1056 | 0.509469696969697 |
| Exact@200 | 321 | 1056 | 0.3039772727272727 |
| HS6@200 | 363 | 1056 | 0.34375 |
| HS4@200 | 529 | 1056 | 0.5009469696969697 |
| Chapter@200 | 810 | 1056 | 0.7670454545454546 |

## Comparacion plano vs jerarquico

| Metrica | Plano v0.2 | Jerarquico v0.2 | Delta |
| --- | ---: | ---: | ---: |
| Top-1 | 0.027462121212121212 | 0.026515151515151516 | -0.0009469696969696965 |
| Top-3 | 0.05113636363636364 | 0.052083333333333336 | 0.0009469696969696965 |
| Top-5 | 0.061553030303030304 | 0.0625 | 0.0009469696969696965 |
| Top-10 | 0.06534090909090909 | 0.06534090909090909 | 0.0 |
| Top-50 | 0.07007575757575757 | 0.09090909090909091 | 0.020833333333333343 |
| Recall@100 | 0.07102272727272728 | 0.10132575757575757 | 0.03030303030303029 |
| MRR | 0.04229731726741296 | 0.04334161160288281 | 0.001044294335469849 |

## Outputs principales

- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_results.csv`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/hierarchical_coverage_summary.json`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/corpus_hierarchical_audit.json`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/historical_flat_vs_normative_hierarchical_compatibility_v0.2.json`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/flat_vs_hierarchical_comparison_v0.2.csv`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/summary.md`
