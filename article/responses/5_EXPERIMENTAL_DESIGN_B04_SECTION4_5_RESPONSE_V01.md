# Respuesta — Experimental Design B04 / Section 4.5 — V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
BLOCK_REVISION = V01
ROLE = IA_REDACCION
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
GOVERNING_PROMPT_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
GOVERNING_DECISION = D-062
PROTOCOL_READ = MWDP_V1.0
ACTIVE_PHASE = EXPERIMENTAL DESIGN
ASSIGNED_BLOCK_STATE = B04 / SECTION 4.5 / AUTHORIZED_FOR_DRAFTING
DRAFTING_AUTHORIZED = YES
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED / NOT_DRAFTED
RESULTS = NOT_AUTHORIZED / NOT_DRAFTED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Onboarding obligatorio

```text
ARCHIVOS_LEIDOS = [
  article/START_HERE.md,
  article/README.md,
  article/ARTICLE_STATUS.md,
  article/ARTICLE_WRITING_PLAN.md,
  article/DECISIONS.md,
  article/SOURCE_REGISTRY.md,
  article/CLAIM_EVIDENCE_MATRIX.md,
  article/STYLE_GUIDE.md,
  article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035,
  article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md,
  article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md,
  article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md,
  article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md,
  article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md,
  article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md,
  article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md,
  article/governance/D058_EXPERIMENTAL_DESIGN_B03_INTEGRATION_AND_V012_PROMOTION.md,
  article/governance/D060_RECENT_GOVERNANCE_CORRECTION_AND_B04_SCOPE_RESET.md,
  article/governance/D061_CONTROL_SYNC_AND_B04_PROMPT_V03_REQUIREMENT.md,
  article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md,
  article/governance/D062_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03_EXECUTION_AUTHORIZATION.md
]
FASE_ACTIVA = EXPERIMENTAL DESIGN
ESTADO_BLOQUE_ASIGNADO = B04 / SECTION 4.5 / AUTHORIZED_FOR_DRAFTING
REDACCION_AUTORIZADA = SI / SOLO SECTION 4.5 EN/ES
DECISIONES_CONGELADAS_RELEVANTES = [D-021, D-022, D-027, D-035, D-045, D-058, D-060, D-061, D-062]
CLAIMS_AUTORIZADOS_RELEVANTES = [recuperacion historica genera y ordena candidatos; Top-3 fijo antes de etapas documental/generativa; Phase F asocia evidencia por lookup NANDINA-8 sin alterar ranking; LLM local restringido a explicacion]
CLAIMS_PROHIBIDOS_O_PENDIENTES_RELEVANTES = [candidate retrieval != overall classification accuracy; documentary association != substantive normative/legal correctness; explanation != legal correctness; configurability != empirical generalization; FINAL_GAP; NOVELTY]
FUENTES_EXTERNAS_A_VERIFICAR = [SRC-03, main, artefactos primarios]
BLOQUEOS_O_CONTRADICCIONES = NONE
```

### Baselines y fuentes vivas

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78 / PASS
BASELINE_MD_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455 / PASS
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b / PASS
SRC03_HEAD_OBSERVED = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_OBSERVED = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
LIVE_SOURCE_MATERIAL_DRIFT_FOR_4_5 = NO
```

Fuentes primarias verificadas directamente en `main`:

- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py` — Git blob `71092fa49364e941ad56fa11f146970ba90b7207`;
- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json` — Git blob `a43893eca3dd756a1ff11935a9cf55afb728e8f4`;
- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`;
- `src/configs/historical_normative_integration_v0.2.json` — Git blob `ed217e7fc3f5eca054ccd0faf442df3ef0ac90be`;
- `outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_run_metadata.json` — Git blob `ffbebf0959a25010b14894b7476602f24cfac390`;
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_pre_generation_check_v0.2.json` — Git blob `43675a7252a16830f3c4ac608d1a573a91d63a62`;
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/gate_i_generation_manifest_v0.2.json` — Git blob `ba61e3e121ea6e7fc2c3dee63b0f12c70398c6e9`;
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_generation_metadata_v0.2.json` — Git blob `ac3b3e6b422a15c7eefe7e95eb0cd1c55e3f1825`;
- `outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_contexts_v0.2.jsonl` — Git blob `6e040c0e0393e535b8e1fcfde9ab0250f487b636`;
- `src/llm/explain_top3_nandina_prompt_v0.2.md` — Git blob `04f9b25dbbf2e90e2a4cacf1e69c904043b0d08f`; el hash SHA-256 enlazado por la ejecución es `1b56ba51863df4d73c8cd882d9154d32df3339a6292d4f72f61d400876f8b1d0`.

### Trazabilidad del contenido redactado

La Section 4.5 se limitó a decisiones de ejecución verificadas: representación y tokenización de la consulta, BM25 sobre H100 con los parámetros ejecutados, ordenamiento de registros y deduplicación por NANDINA, construcción del Top-3 fijo, lookup documental NANDINA-8 de Phase F, construcción del contexto posterior a la fijación del ranking, modelo/backend local y restricciones de generación, y condiciones de software/runtime documentadas. No se incorporaron métricas de rendimiento, outcomes de Phase F, resultados HE4, HE2, EXP11A/EXP11B, EXP12, inferencia ni comparaciones de superioridad.

```text
HARDWARE_CONDITION = NOT_FROZEN / NOT_REPORTED_IN_4_5
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

### Artefactos y handoff

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B04_V01.md
SECTION_ARTIFACT_COMMIT = ade9d022663458d7bbe5aee939e1d7899365a7c8
SECTION_ARTIFACT_SHA256 = 709308c1e52adac7184f5c4a016b836056270f117a496c2a050b18fcf7a5f462
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
MASTER_CANDIDATE_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = 7dbee2c05896e3c45df9cd17518342f1e6446676
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = DEFERRED_TO_GESTORA_UNDER_D035
DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx
DOCX_CANDIDATE_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
DOCX_CUSTODY = AUTHOR_HANDOFF / D-021 / D-027
DOCX_GITHUB_UPLOAD = NOT_ATTEMPTED
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + 0 NEW
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / PRESERVED
ENGLISH_MAIN_TEXT_WORD_COUNT = 549
```

### QA diferencial y binario

```text
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
FULL_DOCX_RENDER = PASS / 44 OF 44 PAGES INSPECTED
EN_ES_SEMANTIC_EQUIVALENCE = PASS
```

El DOCX candidato fue editado acumulativamente desde el binario B03 exacto; no se reconstruyó desde Markdown. Solo se sustituyeron los bloques de instrucción/placeholder de Section 4.5 en inglés y español. Sections 1–4.4 y 4.6+ se conservaron. El master Markdown candidato se derivó exclusivamente de V012 y su diferencial también se limita a los dos bloques 4.5.

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
BLOCK_REVISION = V01
ROLE = DRAFTING_AI
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
GOVERNING_PROMPT_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
GOVERNING_DECISION = D-062
PROTOCOL_READ = MWDP_V1.0
ACTIVE_PHASE = EXPERIMENTAL DESIGN
ASSIGNED_BLOCK_STATE = B04 / SECTION 4.5 / AUTHORIZED_FOR_DRAFTING
DRAFTING_AUTHORIZED = YES
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED / NOT_DRAFTED
RESULTS = NOT_AUTHORIZED / NOT_DRAFTED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Mandatory onboarding

```text
FILES_READ = [
  article/START_HERE.md,
  article/README.md,
  article/ARTICLE_STATUS.md,
  article/ARTICLE_WRITING_PLAN.md,
  article/DECISIONS.md,
  article/SOURCE_REGISTRY.md,
  article/CLAIM_EVIDENCE_MATRIX.md,
  article/STYLE_GUIDE.md,
  article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035,
  article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md,
  article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md,
  article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md,
  article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md,
  article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md,
  article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md,
  article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md,
  article/governance/D058_EXPERIMENTAL_DESIGN_B03_INTEGRATION_AND_V012_PROMOTION.md,
  article/governance/D060_RECENT_GOVERNANCE_CORRECTION_AND_B04_SCOPE_RESET.md,
  article/governance/D061_CONTROL_SYNC_AND_B04_PROMPT_V03_REQUIREMENT.md,
  article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md,
  article/governance/D062_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03_EXECUTION_AUTHORIZATION.md
]
ACTIVE_PHASE = EXPERIMENTAL DESIGN
ASSIGNED_BLOCK_STATE = B04 / SECTION 4.5 / AUTHORIZED_FOR_DRAFTING
DRAFTING_AUTHORIZED = YES / SECTION 4.5 EN/ES ONLY
RELEVANT_FROZEN_DECISIONS = [D-021, D-022, D-027, D-035, D-045, D-058, D-060, D-061, D-062]
RELEVANT_AUTHORIZED_CLAIMS = [historical retrieval generates and ranks candidates; fixed Top-3 precedes documentary/generative stages; Phase F associates evidence through NANDINA-8 lookup without changing ranking; local LLM is restricted to explanation]
RELEVANT_PROHIBITED_OR_PENDING_CLAIMS = [candidate retrieval != overall classification accuracy; documentary association != substantive normative/legal correctness; explanation != legal correctness; configurability != empirical generalization; FINAL_GAP; NOVELTY]
EXTERNAL_SOURCES_TO_VERIFY = [SRC-03, main, primary artifacts]
BLOCKERS_OR_CONTRADICTIONS = NONE
```

### Baselines and live sources

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78 / PASS
BASELINE_MD_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455 / PASS
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b / PASS
SRC03_HEAD_OBSERVED = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_OBSERVED = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
LIVE_SOURCE_MATERIAL_DRIFT_FOR_4_5 = NO
```

Primary artifacts were verified directly in `main`, including the historical-retrieval implementation and metadata, v0.2 split metadata, Phase-F configuration and execution metadata, HE4 pre-generation/generation manifests, the frozen generation metadata and contexts, and the hash-bound explanation prompt. The observed Git identities are the same as those recorded in the Spanish section above.

### Drafted-content traceability

Section 4.5 was restricted to verified execution choices: query representation and tokenization, BM25 over H100 with executed parameters, record ordering and NANDINA deduplication, fixed Top-3 construction, Phase-F NANDINA-8 documentary lookup, context construction after ranking freeze, the local model/backend and generation restrictions, and documented software/runtime conditions. No performance metrics, Phase-F outcomes, HE4 results, HE2 results, EXP11A/EXP11B results, EXP12 results, inferential findings, or superiority comparisons were introduced.

```text
HARDWARE_CONDITION = NOT_FROZEN / NOT_REPORTED_IN_4_5
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

### Artifacts and handoff

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B04_V01.md
SECTION_ARTIFACT_COMMIT = ade9d022663458d7bbe5aee939e1d7899365a7c8
SECTION_ARTIFACT_SHA256 = 709308c1e52adac7184f5c4a016b836056270f117a496c2a050b18fcf7a5f462
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md
MASTER_CANDIDATE_SHA256 = 1614d33707fa5ba830caca14f918578ea5960d8798c1b8de9ac4bcecc4b0dfad
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = 7dbee2c05896e3c45df9cd17518342f1e6446676
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = DEFERRED_TO_GESTORA_UNDER_D035
DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx
DOCX_CANDIDATE_SHA256 = dd8b702445d28a724a3dd990bcbc26ae4ca015c37b5ed172716daa8f6ab88611
DOCX_CUSTODY = AUTHOR_HANDOFF / D-021 / D-027
DOCX_GITHUB_UPLOAD = NOT_ATTEMPTED
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + 0 NEW
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / PRESERVED
ENGLISH_MAIN_TEXT_WORD_COUNT = 549
```

### Differential and binary QA

```text
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
FULL_DOCX_RENDER = PASS / 44 OF 44 PAGES INSPECTED
EN_ES_SEMANTIC_EQUIVALENCE = PASS
```

The DOCX candidate was cumulatively edited from the exact B03 binary and was not rebuilt from Markdown. Only the English and Spanish Section-4.5 drafting-note/placeholder blocks were replaced. Sections 1–4.4 and 4.6+ were preserved. The cumulative Markdown candidate was derived only from V012 and its differential is likewise confined to the two Section-4.5 blocks.

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```
