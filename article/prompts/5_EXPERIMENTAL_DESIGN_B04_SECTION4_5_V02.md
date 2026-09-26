# Prompt — Experimental Design B04 / Section 4.5 — V02

## Español

### Rol

Actúa como **IA de Redacción** del artículo científico principal destinado a *Knowledge-Based Systems*. Ejecuta exclusivamente `EXPERIMENTAL_DESIGN_B04`, limitado a la Section 4.5 autoralmente congelada y su espejo español.

Este prompt **sustituye para ejecución** a `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5.md@7a7aef7994c909e1fde6c01fa8dad7c2cb52f525`, cuyo alcance fue auditado como incompleto. No continúes una ejecución V01 como si fuese equivalente a V02.

No eres la autoridad de cierre experimental. No modifiques experimentos, datos, métricas, scripts, `main`, SRC-03, Plan Maestro, decisiones, reviews ni archivos de gobernanza.

### 1. Onboarding y contratos acumulativos obligatorios

Trabaja en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Antes de redactar, lee íntegramente y en el orden exigido por `article/START_HERE.md`:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/STYLE_GUIDE.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/DECISIONS.md`;
9. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` completo — `MWDP_V1.0`;
10. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md` — SPCCR;
11. `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
12. `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`;
13. `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`;
14. `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`;
15. `article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md`;
16. `article/governance/D058_EXPERIMENTAL_DESIGN_B03_INTEGRATION_AND_V012_PROMOTION.md`;
17. `article/governance/D060_RECENT_GOVERNANCE_CORRECTION_AND_B04_SCOPE_RESET.md`;
18. `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`;
19. este prompt completo.

La ausencia de una regla acumulativa en una sección particular de este prompt **no la deroga**. MWDP v1.0 y las decisiones activas siguen vinculantes.

### 2. Baselines exactos

#### Markdown canónico

Usa exclusivamente:

`article/manuscript/ARTICLE_MASTER_V012.md`

Identidad obligatoria:

- SHA-256: `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`;
- Git blob: `dfea73f5f462fc65cf98347f796deadc6da58455`.

Verifica el blob antes de editar. Si GitHub no expone esa identidad exacta, detente y registra `BLOCKED_BASELINE_MD_DRIFT`.

#### DOCX acumulativo

El autor debe adjuntar:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`

SHA-256 obligatorio:

`9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`

Calcula el SHA-256 antes de editar. Si el binario no está disponible o no coincide, detente y registra:

`BLOCKED_MISSING_EXACT_B03_DOCX_BASELINE`

Está prohibido reconstruir el DOCX desde Markdown, HTML, PDF, texto plano u otro Word anterior.

### 3. Alcance científico exacto autorizado

Redacta exclusivamente:

- Part I: `4.5 Experimental system configuration and execution`;
- Part II: `4.5 Configuración y ejecución experimental`.

La función de 4.5 está congelada por D-045 y Structure V02. Debe **instanciar la arquitectura de Section 3 sin volver a explicarla conceptualmente** y reportar solo elecciones de ejecución que afectaron materialmente el experimento.

La subsección debe cubrir, en una secuencia científica compacta y no como inventario de repositorio:

1. **Representación de consulta.** Campo textual realmente usado, normalización/tokenización efectivamente ejecutada y cualquier preprocesamiento material que pueda verificarse en la implementación que produjo el benchmark.
2. **Recuperación histórica.** Banco H100 vigente, método BM25, parámetros realmente ejecutados y profundidades necesarias para explicar el protocolo; distinguir el ranking de registros del ranking de códigos.
3. **Construcción Top-k / fixed Top-3.** Regla de ordenamiento/desempate, deduplicación por NANDINA, precedente histórico retenido por código y fijación de los tres primeros códigos únicos antes de cualquier etapa documental/generativa.
4. **Asociación documental específica por candidato.** Describir la ruta primaria Phase F realmente ejecutada: el Top-3 histórico ya fijado es la única fuente de candidatos y la evidencia se asocia por lookup directo NANDINA-8 en el corpus jerárquico, con contexto parental explícitamente distinguido de evidencia exacta. No atribuir BM25/query retrieval a esta ruta primaria si no ocurrió.
5. **Construcción del contexto.** Identificar, solo a partir de artefactos primarios, qué campos/objetos del caso, candidatos, precedentes y evidencia entraron al contexto/generation input. Distinguir construcción de contexto de retrieval y de generación. No inventar campos ausentes.
6. **LLM local y restricciones de generación.** Identificar el modelo/backend realmente usado, la versión de prompt efectivamente enlazada por hash/manifiesto, parámetros explícitos materialmente relevantes y las restricciones que impiden insertar, eliminar, sustituir o reordenar candidatos o realimentar la clasificación.
7. **Condiciones materiales de ejecución.** Reportar software, runtime y hardware solo cuando estén directamente documentados y sean pertinentes para reproducibilidad o interpretación. Si una condición de hardware no está congelada de forma verificable, no la inventes; regístrala en la respuesta como `NOT_FROZEN / NOT_REPORTED_IN_4_5`.

Puede usarse **una tabla compacta de configuración** si mejora la legibilidad, pero no debe duplicar la prosa ni convertirse en inventario de hashes/rutas.

### 4. Fuente experimental viva obligatoria

Antes de formular claims, consulta directamente:

- repo `elVladdi/gci-nandina-rag`;
- SRC-03 vivo: rama `docs/plan-maestro-temporal-2026-08-31`, `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- `main` vivo y los artefactos primarios.

Registra HEAD/blob realmente observados. El último corte editorial conocido antes de este prompt era:

```text
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
```

No los trates como permanentes. Si hay drift, determina si cambia materialmente 4.5. Si existe contradicción científica no reconciliable mediante evidencia primaria, detente con `EXECUTION_STOPPED / REQUIRES_GESTORA_REVIEW` y deja el detalle en la response versionada, no en chat.

### 5. Fuentes primarias mínimas que debes verificar

#### Recuperación histórica

- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`;
- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json`;
- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`;
- los CSV/artefactos de historical retrieval necesarios para comprobar campos, precedente y trazabilidad.

La evidencia actualmente auditada indica, sujeto a tu re-verificación viva:

```text
H100_ROWS = 2950
EVAL_ROWS = 1056
QUERY_FIELD = DESCRIPCION DE MERCANCIAS CONCATENADA
LABEL_FIELD = NANDINA
BM25_K1 = 1.5
BM25_B = 0.75
HISTORY_DEPTH = 2950
CANDIDATE_DEPTH = 100
CANDIDATE_DEDUP = NANDINA
DOC_ORDER = descending BM25 score, then case_id
FIXED_TOP3 = first three unique NANDINA codes
```

No copies estos valores si la fuente primaria viva no los confirma.

#### Integración candidato–evidencia / Phase F

Verifica directamente:

- `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json`;
- `src/configs/historical_normative_integration_v0.2.json` si existe en el commit vivo;
- artefactos de integración que necesites para entender campos/contexto, especialmente candidate slots, case summary y traceability;
- código de ejecución de Phase F si un claim no queda probado por metadata.

Contrato metodológico que debe confirmarse:

```text
HISTORICAL_TOP3_ROLE = sole_ranking_source
EVIDENCE_OPERATION = CODE_TO_NORMATIVE_EVIDENCE_LOOKUP
EVIDENCE_SOURCE = frozen historical candidate NANDINA-8
QUERY_BASED_RETRIEVAL_IN_PRIMARY_PHASE_F = false
FALLBACK_TO_ANOTHER_CODE = none
RERANKING = false
SCORE_FUSION = false
CANDIDATE_INSERTION = false
CANDIDATE_SUBSTITUTION = false
LLM_IN_PHASE_F = false
```

Los resultados de cobertura/invariancia observados pertenecen a Results y no deben narrarse en 4.5.

#### Contexto y generación HE4

Verifica directamente, según procedencia/hash:

- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_pre_generation_check_v0.2.json`;
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_generation_manifest_v0.2.json`;
- metadata/inputs de generación y scripts de construcción de contexto que el manifiesto identifique;
- el prompt `src/llm/explain_top3_nandina_prompt_v0.*.md` cuya identidad coincida con el hash congelado de la ejecución; **no asumas por nombre cuál versión fue usada**.

La evidencia ya auditada indica, sujeto a re-verificación:

```text
BACKEND = Ollama local
MODEL = qwen2.5:7b-instruct
MODEL_PARAMETER_SIZE = 7.6B
QUANTIZATION = Q4_K_M
FORMAT = gguf
OLLAMA_VERSION = 0.32.15
NUM_CTX = 8192
TEMPERATURE = 0
OUTPUT_FORMAT = json
STREAM = false
RETRIEVAL_DURING_GENERATION = false
TOP3_CHANGE_AUTHORITY = none
```

`top_p`, `top_k`, `seed` y `num_predict` constan como backend-default/unspecified en el manifiesto auditado; no inventes valores explícitos.

No conviertas número de llamadas, tokens, latencias, resultados de validación o tasa de auditabilidad en Methods salvo que una magnitud sea estrictamente una condición de diseño y esté autorizada como tal. Los outcomes pertenecen a Results.

### 6. Distinción framework vs. instanciación

4.5 describe la **instanciación experimental**. Debe quedar claro que:

- BM25, H100, NANDINA-8, Chapter 87, Decision-885-derived corpus, Ollama/qwen y los parámetros ejecutados son decisiones de esta instanciación;
- el contrato funcional del framework permanece: banco histórico etiquetado → ranking → fixed Top-3 → evidencia por candidato → contexto → generador restringido;
- otro banco histórico, espacio de clases, profundidad arancelaria o corpus compatible puede requerir otra configuración;
- esa configurabilidad **no es evidencia de generalización de desempeño**.

No repitas extensamente Section 3. Explica qué se ejecutó aquí y cómo materializa el contrato ya definido.

### 7. Claims autorizados y fronteras

Los claims metodológicos deben estar trazados a evidencia primaria y compatibles con `CLAIM_EVIDENCE_MATRIX.md`.

Mantén como mínimo:

```text
HISTORICAL_RETRIEVAL = PRIMARY_CANDIDATE_GENERATOR_AND_RANKER
FIXED_TOP3 = FROZEN_BEFORE_DOCUMENTARY_AND_GENERATIVE_STAGES
PRIMARY_DOCUMENTARY_ASSOCIATION = CANDIDATE_SPECIFIC / NO_RERANK
LOCAL_LLM = DOWNSTREAM_EXPLANATION_ONLY
NO_INSERT_DELETE_SUBSTITUTE_REORDER
NO_CLASSIFICATION_FEEDBACK
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
NORMATIVE_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
```

### 8. Contenido prohibido en 4.5

No incluyas:

- Top-1/Top-3/Top-5/Top-10/Top-50, MRR o cualquier valor observado de rendimiento;
- `3168/3168`, tasas de evidencia/invariancia/cobertura u outcomes de Phase F;
- resultados cualitativos/automáticos HE4;
- número de casos auditables, puntuaciones de explicación o disposición HE4;
- resultados HE2, intervalos de confianza o contrastes inferenciales;
- EXP11A/EXP11B results;
- EXP12 como resultado de 4.5;
- comparaciones de superioridad con recuperación normativa/densa;
- latencias agregadas, tokens consumidos o calls completed como “resultado”;
- `accuracy` global del sistema/RAG/LLM;
- corrección normativa sustantiva o jurídica;
- claims de generalización fuera del testbed;
- `FINAL_GAP` o `NOVELTY`;
- detalles técnicos irrelevantes organizados como inventario de rutas/hashes.

### 9. Estilo Methods y SPCCR

Aplica estrictamente SPCCR:

- cada párrafo debe permitir identificar componente, entrada, acción, salida y restricción;
- evita apilar abstracciones o etiquetas internas;
- usa verbos operativos concretos;
- no conviertas Methods en documentación del repositorio;
- una función científica principal por párrafo;
- no presentes resultados como decisiones de diseño ni decisiones como resultados.

Antes de cerrar declara:

```text
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

### 10. Entregables obligatorios

#### A. Bloque versionado en GitHub

Crea:

`article/sections/experimental_design/Experimental_Design_B04_V01.md`

Debe contener:

- encabezado de trazabilidad;
- Part I — Section 4.5 completa en inglés;
- Part II — espejo español semánticamente equivalente;
- no otra sección.

#### B. Master Markdown acumulativo candidato

Deriva exclusivamente de V012:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md`

Solo pueden sustituirse los placeholders de Section 4.5 EN/ES por la prosa B04. Sections 1–4.4 y 4.6+ deben preservarse sin reescritura.

Por D-035, si el master grande presenta o tiene riesgo inmediato de timeout de transferencia, no uses Base64 manual, chunking, reensamblado ni workarounds. Entrégalo al autor como archivo exacto descargable y registra su SHA-256 en la response. No lo reconstruyas después.

#### C. DOCX acumulativo candidato — obligatorio

Partiendo **únicamente** del DOCX B03 exacto:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`

produce:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx`

Sustituye únicamente los placeholders 4.5 EN/ES. Preserva Sections 1–4.4 y 4.6+, estructura, estilos, tablas, captions y los 40 comentarios/anclajes heredados. `tracked changes = 0`.

El DOCX **debe entregarse efectivamente al autor como adjunto/archivo descargable en el chat de ejecución**, conforme a D-027. Un archivo que permanezca solo en filesystem temporal no constituye custodia del autor.

#### D. Response versionada

Crea:

`article/responses/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_RESPONSE_V01.md`

Debe ser bilingüe y registrar toda la respuesta sustantiva. Conforme a D-022, no repitas ese contenido en chat.

### 11. Checklist MWDP obligatorio en la response

Incluye explícitamente:

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
BLOCK_REVISION = V01
SOURCE_SNAPSHOT(S) = [SRC03 HEAD/blob, main commit, primary artifact identities]
AUTHORIZED_CLAIMS_USED = [lista]
CONDITIONAL_CLAIMS_USED = NONE / [lista]
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [lista]
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + [new/new if applicable]
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
ENGLISH_MAIN_TEXT_WORD_COUNT = [n]
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
```

Si aparece `EXPERIMENTAL_REVIEW_TRIGGER = PRESENT`, explica la causa en GitHub y no autoapruebes el cambio; la Gestora decidirá si requiere IA Experimental.

### 12. QA obligatorio Markdown/DOCX

Verifica y registra:

```text
BASELINE_MD_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455 / PASS
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b / PASS
SECTION_4_5_EN_PRESENT = PASS
SECTION_4_5_ES_PRESENT = PASS
SECTION_4_6_BOUNDARY_EN_ES = PASS
SECTIONS_1_TO_4_4_CONTENT_PRESERVED = PASS
SECTIONS_4_6_PLUS_CONTENT_PRESERVED = PASS
RESULTS_VALUES_IN_4_5 = NONE
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = PASS
COMMENTS_AND_ANCHORS_PRESERVED = PASS
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
```

Reporta SHA-256 final del master Markdown candidato y del DOCX candidato.

### 13. Gate de salida y chat

Detente tras producir los cuatro entregables autorizados. No redactes 4.6, 4.7, 4.8 ni Results. No integres B04 al master canónico. No modifiques archivos de estado/gobernanza.

Estado de salida:

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```

En chat responde **solo** con:

`RESPONSE_VERSIONED_IN_GITHUB = <path>@<commit_sha>`

más los enlaces/adjuntos descargables de `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md` y `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx` cuando D-035/D-027 requieran el handoff. No repitas resumen científico, QA, hashes o status blocks en chat.

---

## English

### Role

Act as the **Drafting AI** for the main scientific article targeting *Knowledge-Based Systems*. Execute only `EXPERIMENTAL_DESIGN_B04`, limited to the author-frozen Section 4.5 and its Spanish semantic-control mirror.

This prompt **supersedes for execution** `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5.md@7a7aef7994c909e1fde6c01fa8dad7c2cb52f525`, whose scope was audited as incomplete. Do not continue a V01 execution as if it were equivalent to V02.

You are not the experimental-closure authority. Do not modify experiments, data, metrics, scripts, `main`, SRC-03, the Master Plan, decisions, reviews, or governance files.

### 1. Mandatory onboarding and cumulative contracts

Work in `elVladdi/gci-nandina-rag`, branch `article/main-manuscript`.

Before drafting, read in full and in the order required by `article/START_HERE.md`:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/STYLE_GUIDE.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/DECISIONS.md`;
9. the complete `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — `MWDP_V1.0`;
10. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md` — SPCCR;
11. D-021;
12. D-022;
13. D-027;
14. D-035;
15. D-045;
16. D-058;
17. D-060;
18. `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`;
19. this complete prompt.

Omission of a cumulative rule from any particular subsection of this prompt **does not repeal it**. MWDP v1.0 and active decisions remain binding.

### 2. Exact baselines

#### Canonical Markdown

Use only:

`article/manuscript/ARTICLE_MASTER_V012.md`

Required identity:

- SHA-256: `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`;
- Git blob: `dfea73f5f462fc65cf98347f796deadc6da58455`.

Verify the blob before editing. If GitHub does not expose that exact identity, stop with `BLOCKED_BASELINE_MD_DRIFT`.

#### Cumulative DOCX

The author must attach:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`

Required SHA-256:

`9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`

Calculate its hash before editing. If the binary is unavailable or does not match exactly, stop with `BLOCKED_MISSING_EXACT_B03_DOCX_BASELINE`. Reconstructing the DOCX from Markdown, HTML, PDF, plain text, or another earlier Word file is prohibited.

### 3. Exact authorized scientific scope

Draft only:

- Part I: `4.5 Experimental system configuration and execution`;
- Part II: `4.5 Configuración y ejecución experimental`.

The function of 4.5 is frozen by D-045 and Structure V02. It must **instantiate the Section-3 architecture without conceptually re-explaining it** and report only execution choices that materially affected the experiment.

The subsection must cover, in compact scientific sequence rather than as a repository inventory:

1. **Query representation:** the actual text field, normalization/tokenization, and material preprocessing used by the implementation that produced the benchmark.
2. **Historical retrieval:** the current H100 bank, BM25 method, actually executed parameters, and depths needed to explain the protocol; distinguish record ranking from code ranking.
3. **Top-k / fixed Top-3 construction:** actual ordering/tie-break rule, NANDINA deduplication, historical precedent retained for each code, and freezing of the first three unique codes before any documentary/generative stage.
4. **Candidate-specific documentary association:** describe the actually executed primary Phase-F path: the fixed historical Top-3 is the sole candidate source and evidence is associated through direct NANDINA-8 lookup in the hierarchical corpus, with parent context distinguished from exact evidence. Do not attribute BM25/query retrieval to the primary path if it did not occur.
5. **Context construction:** identify, only from primary artifacts, which case, candidate, precedent, and evidence objects/fields entered the context/generation input. Distinguish context construction from retrieval and generation. Do not invent absent fields.
6. **Local LLM and generation restrictions:** identify the actually used model/backend, prompt version actually bound by hash/manifest, materially relevant explicit parameters, and restrictions preventing candidate insertion, deletion, substitution, reordering, or feedback into classification.
7. **Material execution conditions:** report software, runtime, and hardware only when directly documented and relevant to reproducibility or interpretation. If hardware is not verifiably frozen, do not invent it; record `NOT_FROZEN / NOT_REPORTED_IN_4_5` in the response.

A **compact configuration table** may be used if it improves readability, but it must not duplicate prose or become an inventory of internal paths/hashes.

### 4. Mandatory live experimental source check

Before making claims, directly read:

- repo `elVladdi/gci-nandina-rag`;
- live SRC-03 at branch `docs/plan-maestro-temporal-2026-08-31`, `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- live `main` and primary artifacts.

Record the HEAD/blob actually observed. The last known editorial cut before this prompt was:

```text
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
```

Do not treat them as permanent. If drift exists, determine whether it materially changes 4.5. If a scientific contradiction cannot legitimately be reconciled from primary evidence, stop with `EXECUTION_STOPPED / REQUIRES_GESTORA_REVIEW` and record details in the versioned response, not in chat.

### 5. Minimum primary sources to verify

#### Historical retrieval

Verify at least:

- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`;
- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json`;
- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`;
- historical-retrieval CSV/artifacts required to verify fields, precedent selection, and traceability.

Evidence already audited, subject to your live re-verification:

```text
H100_ROWS = 2950
EVAL_ROWS = 1056
QUERY_FIELD = DESCRIPCION DE MERCANCIAS CONCATENADA
LABEL_FIELD = NANDINA
BM25_K1 = 1.5
BM25_B = 0.75
HISTORY_DEPTH = 2950
CANDIDATE_DEPTH = 100
CANDIDATE_DEDUP = NANDINA
DOC_ORDER = descending BM25 score, then case_id
FIXED_TOP3 = first three unique NANDINA codes
```

Do not copy these values if the live primary source does not confirm them.

#### Candidate–evidence integration / Phase F

Directly verify:

- `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json`;
- `src/configs/historical_normative_integration_v0.2.json` if present at the live commit;
- integration artifacts needed to understand fields/context, especially candidate slots, case summary, and traceability;
- Phase-F execution code whenever metadata alone does not prove a claim.

Method contract to confirm:

```text
HISTORICAL_TOP3_ROLE = sole_ranking_source
EVIDENCE_OPERATION = CODE_TO_NORMATIVE_EVIDENCE_LOOKUP
EVIDENCE_SOURCE = frozen historical candidate NANDINA-8
QUERY_BASED_RETRIEVAL_IN_PRIMARY_PHASE_F = false
FALLBACK_TO_ANOTHER_CODE = none
RERANKING = false
SCORE_FUSION = false
CANDIDATE_INSERTION = false
CANDIDATE_SUBSTITUTION = false
LLM_IN_PHASE_F = false
```

Observed coverage/invariance outcomes belong to Results and must not be narrated in 4.5.

#### HE4 context and generation

Verify directly, following provenance/hash bindings:

- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_pre_generation_check_v0.2.json`;
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_generation_manifest_v0.2.json`;
- generation metadata/inputs and context-construction scripts identified by the manifest;
- the `src/llm/explain_top3_nandina_prompt_v0.*.md` version whose identity matches the frozen execution hash; **do not infer the used version from the filename alone**.

Evidence already audited, subject to re-verification:

```text
BACKEND = Ollama local
MODEL = qwen2.5:7b-instruct
MODEL_PARAMETER_SIZE = 7.6B
QUANTIZATION = Q4_K_M
FORMAT = gguf
OLLAMA_VERSION = 0.32.15
NUM_CTX = 8192
TEMPERATURE = 0
OUTPUT_FORMAT = json
STREAM = false
RETRIEVAL_DURING_GENERATION = false
TOP3_CHANGE_AUTHORITY = none
```

`top_p`, `top_k`, `seed`, and `num_predict` are recorded as backend-default/unspecified in the audited manifest; do not invent explicit values.

Do not convert call counts, token counts, aggregate latency, validation outcomes, or auditability rates into Methods unless a quantity is strictly a design condition and authorized as such. Outcomes belong to Results.

### 6. Framework versus instantiation

Section 4.5 describes the **experimental instantiation**. Make clear that BM25, H100, NANDINA-8, Chapter 87, the Decision-885-derived corpus, Ollama/qwen, and executed parameter values are choices of this instantiation; the framework contract remains labeled historical bank → ranking → fixed Top-3 → candidate evidence → context → restricted generator; another bank, class space, tariff depth, or compatible corpus may require another configuration; and configurability **is not evidence of performance generalization**.

Do not extensively repeat Section 3. Explain what was executed here and how it materializes the already defined contract.

### 7. Authorized claims and boundaries

Method claims must be traceable to primary evidence and compatible with `CLAIM_EVIDENCE_MATRIX.md`.

At minimum preserve:

```text
HISTORICAL_RETRIEVAL = PRIMARY_CANDIDATE_GENERATOR_AND_RANKER
FIXED_TOP3 = FROZEN_BEFORE_DOCUMENTARY_AND_GENERATIVE_STAGES
PRIMARY_DOCUMENTARY_ASSOCIATION = CANDIDATE_SPECIFIC / NO_RERANK
LOCAL_LLM = DOWNSTREAM_EXPLANATION_ONLY
NO_INSERT_DELETE_SUBSTITUTE_REORDER
NO_CLASSIFICATION_FEEDBACK
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
NORMATIVE_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
```

### 8. Content prohibited from 4.5

Do not include:

- Top-1/Top-3/Top-5/Top-10/Top-50, MRR, or any observed performance value;
- `3168/3168`, evidence/invariance/coverage rates, or Phase-F outcomes;
- automatic/qualitative HE4 results;
- auditable-case counts, explanation scores, or HE4 disposition;
- HE2 results, confidence intervals, or inferential contrasts;
- EXP11A/EXP11B results;
- EXP12 as a 4.5 result;
- superiority comparisons against normative/dense retrieval;
- aggregate latencies, token counts, or completed-call counts as results;
- global system/RAG/LLM `accuracy`;
- substantive normative or legal correctness;
- generalization claims beyond the testbed;
- `FINAL_GAP` or `NOVELTY`;
- irrelevant technical detail organized as a path/hash inventory.

### 9. Methods style and SPCCR

Apply SPCCR strictly: each paragraph must make component, input, action, output, and restriction identifiable; avoid stacked abstractions/internal labels; use concrete operational verbs; do not turn Methods into repository documentation; keep one primary scientific function per paragraph; and do not present results as design choices or design choices as results.

Before closing, declare:

```text
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

### 10. Mandatory deliverables

#### A. Versioned block in GitHub

Create `article/sections/experimental_design/Experimental_Design_B04_V01.md` containing a traceability header, complete English Part-I Section 4.5, and semantically equivalent Spanish Part-II Section 4.5, and no other section.

#### B. Cumulative candidate Markdown master

Derive only from V012:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md`

Only the EN/ES Section-4.5 placeholders may be replaced. Preserve Sections 1–4.4 and 4.6+ without rewrite.

Under D-035, if the large master has an immediate transfer-timeout risk, do not use manual Base64, chunking, reassembly, or other workarounds. Deliver the exact file to the author as a downloadable attachment and record its SHA-256 in the response. Do not reconstruct it later.

#### C. Mandatory cumulative DOCX candidate

Starting **only** from the exact B03 DOCX, produce:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx`

Replace only the EN/ES 4.5 placeholders. Preserve Sections 1–4.4 and 4.6+, structure, styles, tables, captions, and all 40 inherited citation comments/anchors. `tracked changes = 0`.

The DOCX **must actually be handed to the author as a downloadable attachment/file in the execution chat**, as required by D-027. A file that remains only in a temporary filesystem is not author custody.

#### D. Versioned response

Create:

`article/responses/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_RESPONSE_V01.md`

It must be bilingual and contain the complete substantive execution response. Under D-022, do not repeat that content in chat.

### 11. Mandatory MWDP checklist in the response

Include explicitly:

```text
PROTOCOL_READ = MWDP_V1.0
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
BLOCK_REVISION = V01
SOURCE_SNAPSHOT(S) = [SRC03 HEAD/blob, main commit, primary artifact identities]
AUTHORIZED_CLAIMS_USED = [list]
CONDITIONAL_CLAIMS_USED = NONE / [list]
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE / [list]
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + [new/new if applicable]
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
ENGLISH_MAIN_TEXT_WORD_COUNT = [n]
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT / PRESENT
```

If `EXPERIMENTAL_REVIEW_TRIGGER = PRESENT`, explain why in GitHub and do not self-approve the change; the Managing AI decides whether Experimental-AI review is required.

### 12. Mandatory Markdown/DOCX QA

Verify and record:

```text
BASELINE_MD_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455 / PASS
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b / PASS
SECTION_4_5_EN_PRESENT = PASS
SECTION_4_5_ES_PRESENT = PASS
SECTION_4_6_BOUNDARY_EN_ES = PASS
SECTIONS_1_TO_4_4_CONTENT_PRESERVED = PASS
SECTIONS_4_6_PLUS_CONTENT_PRESERVED = PASS
RESULTS_VALUES_IN_4_5 = NONE
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = PASS
COMMENTS_AND_ANCHORS_PRESERVED = PASS
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
```

Report the final SHA-256 for both candidate masters.

### 13. Exit gate and chat

Stop after producing the four authorized deliverables. Do not draft 4.6, 4.7, 4.8, or Results. Do not integrate B04 into the canonical master. Do not modify status/governance files.

Exit state:

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```

In chat respond **only** with:

`RESPONSE_VERSIONED_IN_GITHUB = <path>@<commit_sha>`

plus downloadable links/attachments for `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md` and `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx` when D-035/D-027 require handoff. Do not repeat scientific summaries, QA, hashes, or status blocks in chat.