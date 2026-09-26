# D-059 — Experimental Design B04 / Section 4.5 start

```text
DECISION_ID = D-059
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B04
SECTION = 4.5 Historical retrieval configuration and candidate-generation protocol
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Base

D-058 cerró e integró Experimental Design B03 y promovió `ARTICLE_MASTER_V012.md` como master canónico byte-exacto. Antes de abrir B04, la IA Gestora verificó el estado experimental vivo relevante en `main` y las fuentes primarias de recuperación histórica.

El benchmark vigente conserva H100 con 2,950 series y EVAL con 1,056 series. La recuperación histórica usa `DESCRIPCION DE MERCANCIAS CONCATENADA` como consulta y `NANDINA` como etiqueta de referencia. El artefacto de ejecución congelado registra `history_depth=2950`, `candidate_depth=100`, BM25 `k1=1.5`, `b=0.75`, y deduplicación de candidatos por NANDINA. El código de evaluación ordena registros históricos por score BM25 y desempata por `case_id`; después recorre ese ranking y conserva la primera aparición de cada código NANDINA para construir un ranking de códigos únicos. El Top-3 usado aguas abajo son los tres primeros códigos únicos de ese ranking histórico.

La función metodológica de 4.5 es describir la configuración y el protocolo de generación de candidatos. No debe adelantar los valores de Top-1/Top-3/Top-k o MRR que pertenecen a Results, ni convertir candidate retrieval en accuracy global del sistema.

## 2. Alcance autorizado

Se autoriza exclusivamente:

- Part I: `4.5 Historical retrieval configuration and candidate-generation protocol`;
- Part II: espejo español semánticamente equivalente;
- integración de ambos bloques en un nuevo master Markdown candidato acumulativo derivado exclusivamente de V012;
- integración de ambos bloques en un nuevo DOCX candidato acumulativo derivado exclusivamente del DOCX B03 exacto bajo custodia local.

No se reabre Sections 1–4.4. No se redacta 4.6–4.8, Results, Discussion, Conclusion, Abstract, Title o Keywords.

## 3. Fuentes científicas primarias mínimas

La IA de Redacción debe consultar directamente, en el estado vivo de `main` que observe al ejecutar, al menos:

- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`;
- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json`;
- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json` y/o los artefactos de split pertinentes;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md` como snapshot editorial de control, contrastándolo con las fuentes vivas y sin sustituirlas.

Puede consultar artefactos adicionales si son necesarios para verificar un claim. No debe usar literatura científica para inventar parámetros o completar vacíos de implementación.

## 4. Fronteras obligatorias

- historical retrieval = generador/ranker principal de candidatos;
- ranking de registros históricos ≠ ranking final de códigos únicos;
- fixed Top-3 = primeros tres códigos NANDINA únicos tras deduplicación;
- normative retrieval no participa en la generación ni reordenamiento del Top-3;
- local LLM no participa en la generación ni reordenamiento del Top-3;
- candidate retrieval ≠ overall classification accuracy;
- no narrar métricas observadas de desempeño en Methods;
- configurabilidad del framework ≠ generalización empírica;
- no introducir resultados de EXP11A/EXP11B, comparaciones normativas, inferencia HE2 o sensitivity results en 4.5.

## 5. Continuidad DOCX obligatoria

La entrega Word es obligatoria, no condicional. El baseline exacto es:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`

SHA-256:

`9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`

Si la IA de Redacción no dispone de ese binario exacto o su hash no coincide, debe detenerse con `BLOCKED_MISSING_EXACT_B03_DOCX_BASELINE`. Está prohibido reconstruir el DOCX desde Markdown o desde un Word anterior.

## 6. Gate

El prompt atómico gobernante será `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5.md`. La entrega vuelve a la IA Gestora para auditoría independiente. No existe autorización implícita para B05/4.6.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING
NEXT_ACTOR = IA_REDACCION
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```