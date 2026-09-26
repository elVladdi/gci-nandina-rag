# Respuesta — Experimental Design B06 / Section 4.7 — V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
BLOCK_REVISION = V01
ROLE = IA_REDACCION
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
GOVERNING_DECISION = D-073
GROUND_TRUTH_DECISION = D-072
PROTOCOL_READ = MWDP_V1.0
ACTIVE_PHASE = EXPERIMENTAL DESIGN
ASSIGNED_BLOCK_STATE = B06 / SECTION 4.7 / AUTHORIZED_FOR_DRAFTING_UNDER_B06_V01_ONLY
DRAFTING_AUTHORIZED = YES / SECTION 4.7 EN/ES ONLY
SECTION_4_8 = NOT_AUTHORIZED / NOT_DRAFTED
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
  article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf,
  article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md,
  article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md,
  article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md,
  article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md,
  article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md,
  article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md,
  article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md,
  article/governance/D071_EXPERIMENTAL_DESIGN_B05_INTEGRATION_AND_V014_PROMOTION.md,
  article/governance/D072_EXPERIMENTAL_DESIGN_B06_SECTION4_7_GROUND_TRUTH_SYNC.md,
  article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md,
  article/manuscript/ARTICLE_MASTER_V014.md,
  article/governance/D073_EXPERIMENTAL_DESIGN_B06_SECTION4_7_EXECUTION_AUTHORIZATION.md
]
FASE_ACTIVA = EXPERIMENTAL DESIGN
ESTADO_BLOQUE_ASIGNADO = B06 / SECTION 4.7 / AUTHORIZED_FOR_DRAFTING_UNDER_B06_V01_ONLY
REDACCION_AUTORIZADA = SI / SOLO SECTION 4.7 EN/ES
DECISIONES_CONGELADAS_RELEVANTES = [D-004, D-005, D-008, D-021, D-022, D-027, D-035, D-045, D-071, D-072, D-073]
CLAIMS_AUTORIZADOS_RELEVANTES = [C07; C08 dentro de su alcance descriptivo; C26 dentro de su alcance descriptivo; C27; contrato inferencial Group 3 congelado]
CLAIMS_PROHIBIDOS_O_PENDIENTES_RELEVANTES = [candidate retrieval != overall classification accuracy; robustness != empirical generalization; no causal bank-size claim; no seed-superpopulation inference; EXP12 not executed/not estimable; no legal correctness; no Results values; no HE2/HE5 disposition; FINAL_GAP; NOVELTY]
FUENTES_EXTERNAS_VERIFICADAS = [SRC-03 vivo, main vivo, g3_analytical_contract_v0.1.md, g3_inferential_methods_and_checks_v0.1.md, g3_inferential_results_v0.1.json solo para identidad/procedencia del diseño]
BLOQUEOS_O_CONTRADICCIONES = NONE
```

### Baselines y snapshots vivos

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V014.md
BASELINE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97 / PASS
BASELINE_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3 / PASS
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
BASELINE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2 / PASS
SRC03_HEAD_OBSERVED = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB_OBSERVED = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN_OBSERVED = db0d0ad0d8435921a7838db6720eaea86a263763
LIVE_SOURCE_MATERIAL_DRIFT_FOR_4_7 = NO
```

### Matriz protocolo/claim → fuente primaria

| Protocolo o claim usado | Fuente primaria verificada | Alcance aplicado en 4.7 |
|---|---|---|
| SERIE como unidad de análisis; DAM como cluster cuando existe dependencia; estimando primario ponderado por SERIE | `docs/analysis/group3/g3_analytical_contract_v0.1.md` — blob `76862c10fd84fd70588da2d65f96dbe3b40914f6` | Define la unidad analítica, la dependencia y el estimando; no se sustituye por media no ponderada de DAM. |
| Bootstrap pareado por clusters de DAM, mismos casos/cluster para ambas estrategias, 10.000 réplicas, seed 20263001, intervalos percentiles bilaterales y ausencia de p-values | `g3_analytical_contract_v0.1.md` + `docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md` — blob `7a01b75184d95f8df121506079939279957204f6` | Procedimiento inferencial de las familias HE2 elegibles. |
| HE2_A: Top-1/3/5/10 y MRR@100; diferencia pareada `historical - comparator`; familias flat, hierarchical y D1a; 99% marginal CI para Bonferroni familywise 95%; Top-50 suplementaria | `g3_analytical_contract_v0.1.md` | Define métricas, signo del contraste y control de multiplicidad sin trasladar outcomes observados. |
| HE2_B: cobertura profunda separada, profundidad 100 vs 200, contribución `hit_recall_200 - hit_recall_100`, un CI bilateral 95%, sin ajuste de multiplicidad | `g3_analytical_contract_v0.1.md` | Define un único contraste inferencial independiente del ranking temprano. |
| EXP11A como sensibilidad conjunta tamaño/composición y no efecto causal aislado del tamaño | `g3_analytical_contract_v0.1.md` + C08 | Uso descriptivo únicamente. |
| EXP11B como sensibilidad descriptiva H150/H200 sobre diez seeds pareados; filas repetidas no independientes; sin inferencia a superpoblación de seeds | `g3_analytical_contract_v0.1.md` + C26 | Uso descriptivo únicamente. |
| Attempt06 como sensibilidad correctiva descriptiva; Phase-E pools como inventarios de cobertura; EXP12 no estimable; HE5 descriptivo | `g3_analytical_contract_v0.1.md` + C27 | No se introducen nuevos tests, thresholds, causalidad ni significancia. |
| Identidad del diseño inferencial ejecutado | `outputs/analysis/group3/g3_inferential_results_v0.1.json` — blob `8dd92de02e77e6e496baa0af9b5a3d763c19d7f1` | Consultado solo para identidad/procedencia metodológica; ningún valor de resultado, bound o decisión fue trasladado a Methods. |

`g3_metric_population_registry_v0.1.json` era una fuente opcional del prompt cuando fuese necesaria para resolver familias o estatus metodológico. No fue necesaria para sostener ningún claim de la redacción porque el contrato analítico y el documento de métodos inferenciales ya fijaban de forma suficiente esas definiciones.

### Control científico y de alcance

Section 4.7 describe únicamente los procedimientos estadísticos, de sensibilidad y de robustez autorizados. La dependencia intra-DAM se incorpora mediante remuestreo por clusters de DAM sin cambiar el estimando primario ponderado por SERIE. Las comparaciones HE2_A y HE2_B permanecen separadas; EXP11A, EXP11B, Attempt06, Phase E y HE5 conservan sus estados descriptivos, y EXP12 permanece no estimable.

No se incorporaron valores observados de efectos o intervalos, decisiones HE2/HE5, p-values, conclusiones de significancia, outcomes EXP11A/EXP11B/Attempt06, Discussion, novelty ni final gap.

```text
PRIMARY_INFERENTIAL_UNIT = DAM_CLUSTER
PRIMARY_ESTIMAND = SERIES_WEIGHTED
PAIRED_BOOTSTRAP = YES
BOOTSTRAP_REPLICATES = 10000
BOOTSTRAP_SEED = 20263001
HE2_A_FAMILYWISE_CONTROL = BONFERRONI_99_PERCENT_MARGINAL_CI
P_VALUES = NONE
HE2_B_SINGLE_CONTRAST = YES
EXP11A = DESCRIPTIVE_ONLY
EXP11B = DESCRIPTIVE_ONLY
ATTEMPT06 = DESCRIPTIVE_ONLY
EXP12 = NOT_ESTIMABLE
HE5_FAMILIES = DESCRIPTIVE_ONLY
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
ROBUSTNESS != EMPIRICAL_GENERALIZATION
SECTION_4_8_CONTENT = NONE
RESULTS_VALUES_IN_4_7 = NONE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
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

### Artefactos y QA

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V01.md
SECTION_ARTIFACT_COMMIT = 3124ac129bdd2b6bacf02819bbcd1d48cb0b5fb4
SECTION_ARTIFACT_GIT_BLOB = 7d2413c1516778dffe000e5ff2e8716c017f4d5a
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
MASTER_CANDIDATE_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = bda3bb6f9603039c48239deab779eec106588719
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = NOT_REQUIRED / LOCAL_AUTHOR_HANDOFF
DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
DOCX_CANDIDATE_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
DOCX_SOURCE = EXACT_B05_V01_BINARY / DIRECT_OOXML_EDIT
DOCX_RECONSTRUCTED_FROM_MD = NO
DOCX_CUSTODY = AUTHOR_HANDOFF / D-021 / D-027 / D-035
DOCX_GITHUB_UPLOAD = NOT_ATTEMPTED
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + 0 NEW
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / PRESERVED
ENGLISH_MAIN_TEXT_WORD_COUNT = 566 / SECTION_4_7_BODY
```

```text
MD_ONLY_SECTION_4_7_EN_ES_CHANGED = PASS
SECTIONS_1_TO_4_6_CONTENT_PRESERVED_MD = PASS
SECTIONS_4_8_PLUS_CONTENT_PRESERVED_MD = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = 14/14 PASS
ZIP_ENTRY_SET = PRESERVED
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
SECTION_4_7_EN_PRESENT = PASS
SECTION_4_7_ES_PRESENT = PASS
SECTION_4_8_BOUNDARY_EN_ES = PASS
SECTIONS_1_TO_4_6_CONTENT_PRESERVED_DOCX = PASS
SECTIONS_4_8_PLUS_CONTENT_PRESERVED_DOCX = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES INSPECTED
VISUAL_QA = PASS / NO CLIPPING, TRUNCATION, OVERLAP OR MATERIAL FORMAT LOSS
```

El DOCX se editó directamente desde el binario B05 V01 exacto. A nivel de contenido descomprimido del paquete OOXML, únicamente cambió `word/document.xml`; `comments.xml` y los demás componentes permanecieron sin cambios de contenido. La comparación del cuerpo documental fuera de Section 4.7 EN/ES es exacta respecto del baseline.

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
BLOCK_REVISION = V01
ROLE = DRAFTING_AI
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
GOVERNING_DECISION = D-073
GROUND_TRUTH_DECISION = D-072
PROTOCOL_READ = MWDP_V1.0
ACTIVE_PHASE = EXPERIMENTAL DESIGN
ASSIGNED_BLOCK_STATE = B06 / SECTION 4.7 / AUTHORIZED_FOR_DRAFTING_UNDER_B06_V01_ONLY
DRAFTING_AUTHORIZED = YES / SECTION 4.7 EN/ES ONLY
SECTION_4_8 = NOT_AUTHORIZED / NOT_DRAFTED
RESULTS = NOT_AUTHORIZED / NOT_DRAFTED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Mandatory onboarding and live-source control

The complete governed onboarding was read before drafting. Canonical `ARTICLE_MASTER_V014.md` passed its required SHA-256 and Git-blob identity checks, and the exact attached B05 V01 DOCX passed its required SHA-256 check. Live SRC-03 and development `main` remained at the synchronized heads recorded by D-072, with no material drift affecting Section 4.7.

Primary-source verification covered the frozen Group-3 analytical contract, the inferential-methods/checks document, and the inferential-results artifact only for execution-design identity and provenance. Result values and hypothesis decisions from that artifact were not transferred into Methods. The optional metric-population registry was not needed to support any drafted methodological statement because the required family definitions and methodological statuses were already fixed by the analytical contract and inferential-methods source.

### Scientific scope control

Section 4.7 states the DAM-cluster-aware paired bootstrap while preserving the series-weighted estimand. Eligible HE2_A and HE2_B procedures remain distinct. EXP11A, EXP11B, Attempt06, Phase-E candidate pools, and HE5 remain descriptive under their frozen contracts; EXP12 remains not estimable. No observed effects, confidence-interval bounds, p-values, hypothesis dispositions, sensitivity outcomes, Results prose, Discussion, novelty, or final-gap claim was introduced.

```text
PRIMARY_INFERENTIAL_UNIT = DAM_CLUSTER
PRIMARY_ESTIMAND = SERIES_WEIGHTED
PAIRED_BOOTSTRAP = YES
BOOTSTRAP_REPLICATES = 10000
BOOTSTRAP_SEED = 20263001
HE2_A_FAMILYWISE_CONTROL = BONFERRONI_99_PERCENT_MARGINAL_CI
P_VALUES = NONE
HE2_B_SINGLE_CONTRAST = YES
EXP11A = DESCRIPTIVE_ONLY
EXP11B = DESCRIPTIVE_ONLY
ATTEMPT06 = DESCRIPTIVE_ONLY
EXP12 = NOT_ESTIMABLE
HE5_FAMILIES = DESCRIPTIVE_ONLY
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
ROBUSTNESS != EMPIRICAL_GENERALIZATION
SECTION_4_8_CONTENT = NONE
RESULTS_VALUES_IN_4_7 = NONE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
ACCESS_RECHECK_REQUIRED = NONE
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### Artifacts and QA

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V01.md@3124ac129bdd2b6bacf02819bbcd1d48cb0b5fb4
SECTION_ARTIFACT_GIT_BLOB = 7d2413c1516778dffe000e5ff2e8716c017f4d5a
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
MASTER_CANDIDATE_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = bda3bb6f9603039c48239deab779eec106588719
DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
DOCX_CANDIDATE_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + 0 NEW
ENGLISH_MAIN_TEXT_WORD_COUNT = 566 / SECTION_4_7_BODY
EN_ES_SEMANTIC_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = 14/14 PASS
COMMENTS = 40 / STARTS 40 / ENDS 40 / REFERENCES 40
TRACKED_CHANGES = 0
DOCX_RECONSTRUCTED_FROM_MD = NO
SECTIONS_1_TO_4_6_CONTENT_PRESERVED = PASS
SECTIONS_4_8_PLUS_CONTENT_PRESERVED = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES INSPECTED
VISUAL_QA = PASS
```

The cumulative DOCX was edited directly from the exact B05 V01 binary. At decompressed OOXML-package-content level, only `word/document.xml` changed; all inherited citation comments remained intact. Document-body content outside the English and Spanish Section-4.7 blocks matched the baseline.

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
