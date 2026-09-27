# Respuesta — Experimental Design B07 / Section 4.8 — V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
BLOCK_REVISION = V01
ROLE = IA_REDACCION
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
GOVERNING_PROMPT_GIT_BLOB = 9955ea1617b0b13ceeadc83f357dc982eba313ef
GOVERNING_DECISION = D-080
GROUND_TRUTH_DECISION = D-079
PROTOCOL_READ = MWDP_V1.0 / PASS
ACTIVE_PHASE = EXPERIMENTAL DESIGN
ASSIGNED_BLOCK_STATE = B07 / SECTION 4.8 / OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B07_V01_ONLY
DRAFTING_AUTHORIZED = YES / SECTION 4.8 EN/ES ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED / NOT_DRAFTED
DISCUSSION = NOT_AUTHORIZED / NOT_DRAFTED
CONCLUSION = NOT_AUTHORIZED / NOT_DRAFTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Onboarding y control de gobernanza

Se completó el onboarding obligatorio antes de redactar. Se leyeron `START_HERE.md`, `README.md`, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, `STYLE_GUIDE.md`, el prompt B07 exacto, MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-078, D-079, D-080, `KBS_ARTICLE_WORKING_STRUCTURE_V02.md` y el master canónico V015. El estado vivo autorizaba exclusivamente Section 4.8 y mantenía cerrados Results, Discussion y Conclusion.

```text
ARTICLE_BRANCH_HEAD_PRE_EXECUTION = a7111d8e30176b3ee59a4888e387107b0be49242
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V015.md
BASELINE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c / PASS
BASELINE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9 / PASS
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2 / PASS
```

### Snapshot público y re-verificación

El repositorio público de reproducibilidad se re-verificó directamente antes de la redacción. El estado vivo coincide con el snapshot de D-079 y no existe drift material para B07.

```text
REPRO_REPOSITORY = elVladdi/gci-nandina-rag-reproducibility
SOURCE_SNAPSHOT_REPRO_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
SOURCE_SNAPSHOT_REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
REPRO_REPOSITORY_DRIFT_ASSESSMENT = NO_MATERIAL_DRIFT
REPRO_PACKAGE_STATUS = DOCUMENTED_SCAFFOLD / NOT_FULL_REFERENCE_RELEASE
```

Se verificaron los siguientes recursos primarios del snapshot:

| Recurso | Git blob verificado | Uso en B07 |
|---|---|---|
| `README.md` | `eb31035160d88fbe5634ca8df414c4ed741bd624` | Modos `reference`/`custom`/`synthetic`, configurabilidad documentada y carácter objetivo de los comandos mostrados. |
| `docs/REPRODUCIBILITY.md` | `839b4245fcf4497ebf6ced28dd8771e3b29601c4` | Distinción entre reproducción de referencia y replicación externa; requisitos de determinismo, manifests y validación en entorno limpio. |
| `docs/DATA_PROVENANCE.md` | `e7fac0b48c9fc53c2e09f99807d8be7609277ac6` | Procedencia, decisión de redistribución y tratamiento de entradas restringidas. |
| `docs/EXPERIMENT_PROTOCOL.md` | `3782e98bd6423ce3a7cfe7a4cd5d620e2573ccaa` | Contrato de ejecución y metadatos de run manifest. |
| `docs/DATA_CONTRACT.md` | `4611667ced7f596089822b749800555be21e7fb8` | Campos lógicos, grouping unit, niveles arancelarios y metadatos reproducibles. |
| `docs/TAXONOMY_AND_NORMATIVE_CORPUS.md` | `9512b1583c5a78cc0cd2d356a60f30d3ddfc41ed` | Configurabilidad de jerarquía/corpus y límites de cobertura. |
| `docs/USING_YOUR_OWN_DATA.md` | `e852ab22c47164689699b8be8d338763c5f23f44` | Replicación externa con datos compatibles y manifiesto propio. |
| `docs/EXPECTED_RESULTS.md` | `361686e6c6d300a8c8732819a1db4c58b278d839` | Registro aún incompleto de la futura release; no se trasladaron resultados observados a Methods. |
| `configs/examples/custom_dataset.example.yaml` | `5ac8467786de8cf331fc9ba6861cc51652633f2f` | Configuración materializada para datos propios compatibles. |
| `scripts/README.md` | `09ec6d886205290d6ae109762f1c5f90a053ef06` | Confirma que el runner canónico es interfaz planificada, no runner materializado. |
| `configs/presets/README.md` | `f698911b4604b4b0105fa0c5097754451b7263e3` | Confirma que los presets de referencia están planificados y aún no materializados. |
| `data/README.md` | `062cf7ea2c0e35b1420561068bd254ca273c07f9` | Frontera de redistribución y exclusión de entradas restringidas. |

La inspección recursiva del tree confirmó que el snapshot no contiene `requirements.txt`/lockfile, el runner canónico `scripts/reproduce_all.py`, los runners ejecutables de validación/experimento, un preset Clase-87 congelado, datasets administrativos de referencia redistribuidos, resultados canónicos materializados ni una validación clean-environment final. La redacción trata los comandos documentados como interfaces objetivo y no como capacidad actual de reproducción integral desde un fresh clone.

### Claims y fronteras de interpretación

```text
AUTHORIZED_CLAIMS_USED = C15 / C17 WITH GOVERNED BOUNDS
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_AVOIDED = C16; COMPLETE_OR_STABLE_REFERENCE_RELEASE; ONE_COMMAND_FRESH_CLONE_REPRODUCTION; PUBLIC_ADMINISTRATIVE_REFERENCE_DATA; LEGAL_CORRECTNESS_FROM_REPRODUCIBILITY; EMPIRICAL_GENERALIZATION_FROM_CONFIGURABILITY
ACCESS_RECHECK_REQUIRED = NONE
RESULTS_LEAKAGE = NONE
REPRO_STATUS_OVERCLAIMING = NONE
PUBLIC_VS_RESTRICTED_BOUNDARY = PASS
PRESENT_VS_PLANNED_RESOURCE_BOUNDARY = PASS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

C15 se utilizó únicamente para describir configurabilidad del dataset, alcance por capítulos, profundidad arancelaria, jurisdicción y corpus compatible como propiedad de diseño. C17 se utilizó para separar reproducción del estudio de referencia y replicación externa. No se afirmó transferencia de desempeño, disponibilidad pública de datos administrativos de referencia, corrección jurídica ni capacidad computacional no materializada.

### Artefactos y QA

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B07_V01.md
SECTION_ARTIFACT_COMMIT = c3cc9971f7d2aaebd629b07cad235e8efa3ee526
SECTION_ARTIFACT_GIT_BLOB = 324eac1190fb3c13101e477e41eeb1f8d0c46e30
SECTION_ARTIFACT_SHA256 = eaf09d02081bb9dcb00f714efd746cf71d160521b37bdf66d1cfce5ad0a21263
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md
MASTER_CANDIDATE_SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = 0d8a4ad3dd03c5b69feeec6a5710d296a5a76662
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = DEFERRED / D-035
DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
DOCX_CANDIDATE_SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
DOCX_SOURCE = EXACT_B06_V02_BINARY / DIRECT_OOXML_EDIT
DOCX_RECONSTRUCTED_FROM_MD = NO
DOCX_CUSTODY = AUTHOR_HANDOFF / D-021 / D-027 / D-035
DOCX_GITHUB_UPLOAD = NOT_ATTEMPTED
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + 0 NEW
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / BYTE_IDENTICAL
ENGLISH_WORD_COUNT_SECTION_4_8 = 459
SECTION_4_8_ONLY_MD_DIFF = PASS
SECTIONS_1_TO_4_7_PRESERVED = PASS
RESULTS_PLUS_PRESERVED = PASS
EN_ES_EQUIVALENCE = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
REPRO_STATUS_OVERCLAIMING = NONE
PUBLIC_VS_RESTRICTED_BOUNDARY = PASS
PRESENT_VS_PLANNED_RESOURCE_BOUNDARY = PASS
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = 14/14 PASS
ZIP_ENTRY_SET = PRESERVED / 14 OF 14
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / 51 OF 51 PAGES INSPECTED
VISUAL_QA = PASS / NO CLIPPING, TRUNCATION, OVERLAP OR MATERIAL FORMAT LOSS
EXPERIMENTAL_REVIEW_TRIGGER = NOT_REQUIRED_UNLESS_SOURCE_DRIFT_OR_NEW_EXPERIMENTAL_CLAIM
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

El DOCX candidato se editó directamente desde el binario B06 V02 exacto. El conjunto de 14 entradas del paquete OOXML se preservó y únicamente cambió `word/document.xml`; `comments.xml` y los demás componentes permanecieron byte-idénticos. El contenido anterior a 4.8 y todo el contenido desde Results en adelante permanecieron preservados. Las 51 páginas renderizadas fueron inspeccionadas visualmente.

### MWDP_DELIVERY_CHECKLIST

```text
ONBOARDING_PROTOCOL_READ = PASS
BLOCK_VERSION = B07 / V01
SOURCE_SNAPSHOTS = REPRO_HEAD_254831cd955103faa2517065a7eed7fb340bbccc / REPRO_TREE_078a85255fa1f3234b4f7ed51ef2660b903d486e
AUTHORIZED_CLAIMS = C15 / C17 WITH LIMITS
CONDITIONAL_CLAIMS = NONE
PROHIBITED_CLAIMS = NONE USED
ACCESS_RECHECK = NONE
CITATION_COVERAGE = 40/40 INHERITED COMMENTS PRESERVED / NO NEW LITERATURE CITATIONS
EN_ES_EQUIVALENCE = PASS
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md + ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
ENGLISH_MAIN_TEXT_WORD_COUNT = 459 / SECTION 4.8 BODY
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

```text
B07_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
BLOCK_REVISION = V01
ROLE = DRAFTING_AI
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
GOVERNING_PROMPT_GIT_BLOB = 9955ea1617b0b13ceeadc83f357dc982eba313ef
GOVERNING_DECISION = D-080
GROUND_TRUTH_DECISION = D-079
PROTOCOL_READ = MWDP_V1.0 / PASS
ACTIVE_PHASE = EXPERIMENTAL DESIGN
ASSIGNED_BLOCK_STATE = B07 / SECTION 4.8 / OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B07_V01_ONLY
DRAFTING_AUTHORIZED = YES / SECTION 4.8 EN/ES ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED / NOT_DRAFTED
DISCUSSION = NOT_AUTHORIZED / NOT_DRAFTED
CONCLUSION = NOT_AUTHORIZED / NOT_DRAFTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Onboarding and governance control

Mandatory onboarding was completed before drafting. The live editorial state authorized only Section 4.8 under B07 V01 and kept Results, Discussion, and Conclusion closed. The exact V015 Markdown and exact B06 V02 DOCX passed the required identity checks.

```text
ARTICLE_BRANCH_HEAD_PRE_EXECUTION = a7111d8e30176b3ee59a4888e387107b0be49242
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V015.md
BASELINE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c / PASS
BASELINE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9 / PASS
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2 / PASS
```

### Public source snapshot and recheck

The public reproducibility repository was rechecked directly before drafting. Its live HEAD and recursive tree are identical to the D-079 snapshot, so no material source drift affects B07.

```text
REPRO_REPOSITORY = elVladdi/gci-nandina-rag-reproducibility
SOURCE_SNAPSHOT_REPRO_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
SOURCE_SNAPSHOT_REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
REPRO_REPOSITORY_DRIFT_ASSESSMENT = NO_MATERIAL_DRIFT
REPRO_PACKAGE_STATUS = DOCUMENTED_SCAFFOLD / NOT_FULL_REFERENCE_RELEASE
```

Primary verification covered the public README, reproducibility, provenance, experimental-protocol, data-contract, taxonomy/corpus, own-data, expected-results documentation, the materialized custom-data configuration example, the script/preset/data directory documentation, and the recursive tree. The tree confirms that the current snapshot lacks a dependency lock, canonical reproduction runner, executable validation/experiment runners, frozen Chapter-87 reference preset, redistributed administrative reference datasets, materialized canonical reference results, and final clean-environment validation. Documented commands are therefore treated as target interfaces rather than current fresh-clone one-command reproduction capability.

### Claims and interpretation boundaries

```text
AUTHORIZED_CLAIMS_USED = C15 / C17 WITH GOVERNED BOUNDS
CONDITIONAL_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_USED = NONE
PROHIBITED_CLAIMS_AVOIDED = C16; COMPLETE_OR_STABLE_REFERENCE_RELEASE; ONE_COMMAND_FRESH_CLONE_REPRODUCTION; PUBLIC_ADMINISTRATIVE_REFERENCE_DATA; LEGAL_CORRECTNESS_FROM_REPRODUCIBILITY; EMPIRICAL_GENERALIZATION_FROM_CONFIGURABILITY
ACCESS_RECHECK_REQUIRED = NONE
RESULTS_LEAKAGE = NONE
REPRO_STATUS_OVERCLAIMING = NONE
PUBLIC_VS_RESTRICTED_BOUNDARY = PASS
PRESENT_VS_PLANNED_RESOURCE_BOUNDARY = PASS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

C15 is used only for design configurability; C17 is used only for the governed distinction between reference reproduction and external replication. No empirical-performance transfer, public availability of restricted reference data, legal correctness, or unmaterialized computational capability is claimed.

### Artifacts and QA

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B07_V01.md
SECTION_ARTIFACT_COMMIT = c3cc9971f7d2aaebd629b07cad235e8efa3ee526
SECTION_ARTIFACT_GIT_BLOB = 324eac1190fb3c13101e477e41eeb1f8d0c46e30
SECTION_ARTIFACT_SHA256 = eaf09d02081bb9dcb00f714efd746cf71d160521b37bdf66d1cfce5ad0a21263
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md
MASTER_CANDIDATE_SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = 0d8a4ad3dd03c5b69feeec6a5710d296a5a76662
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = DEFERRED / D-035
DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
DOCX_CANDIDATE_SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
DOCX_SOURCE = EXACT_B06_V02_BINARY / DIRECT_OOXML_EDIT
DOCX_RECONSTRUCTED_FROM_MD = NO
DOCX_CUSTODY = AUTHOR_HANDOFF / D-021 / D-027 / D-035
CITATION_COMMENT_COVERAGE = 40/40 PRESERVED + 0 NEW
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / BYTE_IDENTICAL
ENGLISH_WORD_COUNT_SECTION_4_8 = 459
SECTION_4_8_ONLY_MD_DIFF = PASS
SECTIONS_1_TO_4_7_PRESERVED = PASS
RESULTS_PLUS_PRESERVED = PASS
EN_ES_EQUIVALENCE = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
REPRO_STATUS_OVERCLAIMING = NONE
PUBLIC_VS_RESTRICTED_BOUNDARY = PASS
PRESENT_VS_PLANNED_RESOURCE_BOUNDARY = PASS
ZIP_OOXML_INTEGRITY = PASS
XML_RELS_PARSE = 14/14 PASS
ZIP_ENTRY_SET = PRESERVED / 14 OF 14
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / 51 OF 51 PAGES INSPECTED
VISUAL_QA = PASS / NO CLIPPING, TRUNCATION, OVERLAP OR MATERIAL FORMAT LOSS
EXPERIMENTAL_REVIEW_TRIGGER = NOT_REQUIRED_UNLESS_SOURCE_DRIFT_OR_NEW_EXPERIMENTAL_CLAIM
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
```

The cumulative DOCX was edited directly from the exact B06 V02 binary. Only `word/document.xml` changed at package-content level; all 40 inherited comments, their anchors/references, and all other OOXML parts were preserved. Sections 1–4.7 and Results-plus content remain unchanged. All 51 rendered pages were visually inspected.

### MWDP_DELIVERY_CHECKLIST

```text
ONBOARDING_PROTOCOL_READ = PASS
BLOCK_VERSION = B07 / V01
SOURCE_SNAPSHOTS = REPRO_HEAD_254831cd955103faa2517065a7eed7fb340bbccc / REPRO_TREE_078a85255fa1f3234b4f7ed51ef2660b903d486e
AUTHORIZED_CLAIMS = C15 / C17 WITH LIMITS
CONDITIONAL_CLAIMS = NONE
PROHIBITED_CLAIMS = NONE USED
ACCESS_RECHECK = NONE
CITATION_COVERAGE = 40/40 INHERITED COMMENTS PRESERVED / NO NEW LITERATURE CITATIONS
EN_ES_EQUIVALENCE = PASS
MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md + ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
ENGLISH_MAIN_TEXT_WORD_COUNT = 459 / SECTION 4.8 BODY
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

```text
B07_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
