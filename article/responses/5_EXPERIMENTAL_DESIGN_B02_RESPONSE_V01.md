# Experimental Design B02 — Execution response V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
EXECUTION_STATE = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
REPOSITORY = elVladdi/gci-nandina-rag
BRANCH = article/main-manuscript
INPUT_HEAD = d2c74644fd07d172fb54061ed43a524907a7d303
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B02_DOCUMENTARY_CORPUS_EVIDENCE_RESOURCE.md@d2c74644fd07d172fb54061ed43a524907a7d303
GOVERNING_DECISION = D-051
CANONICAL_MASTER_MD_GIT_BLOB = 8dc09fb841162005b2155491735336b0e70187c6
BASELINE_DOCX_SHA256 = 4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae
AUTHORIZED_SCOPE = SECTION_4_3_ONLY_ENGLISH_PLUS_SPANISH_SEMANTIC_MIRROR
```

### Fuentes gobernantes y verificación de entrada

Se leyeron `START_HERE.md`, `README.md`, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `KBS_ARTICLE_WORKING_STRUCTURE_V02.md`, D-050, D-051, la revisión de ground truth de B02, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, `STYLE_GUIDE.md` y el master canónico `ARTICLE_MASTER_V010.md`. El master Markdown local de entrada coincidió con SHA-256 `82f148046b604dc26fa87ac1852c846798928e3a4af68bf18fcddb2d150e8ab8` y con Git blob `8dc09fb841162005b2155491735336b0e70187c6`. El DOCX baseline coincidió con SHA-256 `4839cbbf8ded9ab10da5b7e29b3482abd4858db2a0881753b6c5250ec60ea2ae`.

El prompt también referencia `article/CLAIM_REGISTRY.md`; ese archivo no existe en la rama de entrada y la búsqueda del repositorio no devolvió un reemplazo homónimo. No se reconstruyó su contenido por inferencia. Para este bloque, el control epistémico específico quedó proporcionado directamente por D-051, la revisión de ground truth y `CLAIM_EVIDENCE_MATRIX.md`, sin contradicción material detectada.

### Evidencia técnica primaria verificada

Se verificaron directamente en `main` las fuentes exigidas: `historical_normative_integration_v0.2.json`, `he4_pre_explainer_v0.2.json`, `build_hierarchical_nandina_corpus.py`, `run_metadata.json`, `summary.csv`, `build_llm_explanation_top3_sample.py` y `build_llm_explanation_top3_audit_sample.py`. La evidencia primaria confirma que el ranking histórico es la única fuente del orden de candidatos, que el Top-3 se fija antes de la etapa documental y que la asociación documental primaria es un lookup directo por código NANDINA-8 en el corpus jerárquico. También confirma que no se utiliza query-based normative retrieval en esa ruta, no se fusionan scores, no se reordena el Top-3, no se insertan o sustituyen candidatos y la ausencia de registro exacto no activa fallback a otro código.

`SRC-03` vivo se comprobó en la rama `docs/plan-maestro-temporal-2026-08-31`: HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8`, blob del Plan Maestro `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`. El cambio más reciente activa administrativamente G7-F02 y no modifica los hechos de corpus, asociación documental, inmutabilidad del Top-3 ni frontera Decision 885/906 que gobiernan B02. No se detectó contradicción material con D-051.

### Trazabilidad claim-by-claim de la nueva Section 4.3

| Afirmación introducida | Soporte primario verificado | Límite preservado |
|---|---|---|
| El recurso primario es un corpus NANDINA jerárquico derivado de Decision 885 de la Comisión de la Comunidad Andina. | `run_metadata.json`; D-051; revisión de ground truth. | No se atribuye autoridad primaria nacional peruana. |
| El recurso representa jerarquía NANDINA y conserva niveles parentales, descripción, unidad y procedencia cuando están disponibles. | `build_hierarchical_nandina_corpus.py`. | El contexto parental no se presenta como evidencia exacta NANDINA-8 cuando falta el registro exacto. |
| La asociación de evidencia para cada candidato fijo se realiza mediante lookup exacto de su código NANDINA-8. | `historical_normative_integration_v0.2.json`; ambos constructores de explicación. | No se describe como BM25, búsqueda semántica o query retrieval sobre la descripción comercial. |
| La etapa documental no altera composición ni orden del Top-3 y no sustituye candidatos sin evidencia exacta. | Configuración de integración y constructores de payload. | No score fusion, reranking, candidate insertion/substitution ni fallback a otro código. |
| Decision 906 modificó Decision 885 y la ruta primaria mantuvo el snapshot derivado de Decision 885 para los casos 2026. | D-051 y revisión de ground truth, que congelan la autoridad y temporalidad oficial; configuración/corpus consumido. | Se declara desajuste temporal de versión, no incorrección general de Chapter 87 ni efectos cuantitativos de la corrección posterior. |
| La evidencia documental se entrega downstream para explicación controlada. | Configuración HE4 y constructores de explicación. | No se afirma corrección normativa sustantiva ni corrección jurídica. |

### Artefactos y verificación diferencial

```text
SECTION_MD_PATH = article/sections/experimental_design/Experimental_Design_B02_V01.md
SECTION_MD_SHA256 = 12ad71a96d5e9dc43fe523df39bf3967656725ba198954754013ff25f39202db
SECTION_MD_GIT_BLOB = 406b62f236ffda010c72652a261f194edadf47bc
SECTION_MD_COMMIT = f853e96b905b279f5ff07e25f4c84560d8402db1
MASTER_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.md
MASTER_CANDIDATE_MD_SHA256 = 22f5a6e1168e08ef6281488024a4ac5e4f6742ee90a96d8f31e5453c592bf592
MASTER_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V01.docx
MASTER_CANDIDATE_DOCX_SHA256 = 40d492911b2163a4c6a837f292f3056aa49bcbf69ce9dc3caf50aa80f021ae1e
FROZEN_TEXT_OUTSIDE_4_3 = UNCHANGED
SECTION_4_4_TO_4_8 = UNCHANGED_PLACEHOLDERS
RESULTS = UNCHANGED
```

La comparación Markdown reconstruye exactamente V010 al restaurar únicamente los dos bloques 4.3. En el DOCX se editó directamente el baseline exacto; no se reconstruyó desde Markdown. El paquete mantiene las mismas 14 partes OOXML y únicamente cambió `word/document.xml`. `word/comments.xml` permanece byte-identical con SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`.

```text
FINAL_COMMENT_COUNT = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
OOXML_INTEGRITY = CLEAN
FULL_RENDER_INSPECTION = CLEAN
RENDERED_PAGE_COUNT = 41
LAYOUT_CLIPPING = NONE_OBSERVED
LAYOUT_OVERLAP = NONE_OBSERVED
MISSING_GLYPHS = NONE_OBSERVED
DUPLICATED_OR_DISPLACED_HEADINGS = NONE_OBSERVED
```

El render completo de 41 páginas fue inspeccionado visualmente, incluidas las páginas que contienen 4.3 en inglés y español. No se observaron desbordes, solapamientos, glifos faltantes, páginas corruptas, encabezados desplazados ni pérdida visible de contenido.

### Validación de cierre

```text
SECTION_4_3_ONLY = YES
PRIMARY_RESOURCE = DECISION_885_DERIVED_HIERARCHICAL_NANDINA_CORPUS
PRIMARY_ASSOCIATION = EXACT_NANDINA8_CODE_LOOKUP
QUERY_BASED_NORMATIVE_RETRIEVAL_CLAIM = NO
DOCUMENTARY_RERANKING_CLAIM = NO
CANDIDATE_SUBSTITUTION_CLAIM = NO
DECISION_906_TEMPORAL_BOUNDARY_DISCLOSED = YES
DECISION_906_RESULTS_ANTICIPATED = NO
PERUVIAN_NATIONAL_AUTHORITY_MISATTRIBUTION = NO
ARANCEL2022_AS_PRIMARY_HE4_CONTEXT = NO
CLASSIFICATION_RESOLUTIONS_AS_PRIMARY_HE4_CONTEXT = NO
LEGAL_CORRECTNESS_CLAIM = NO
SECTION_4_4_PLUS_DRAFTED = NO
RESULTS_DRAFTED = NO
FROZEN_TEXT_MUTATED = NO
FINAL_GAP_DEFINED = NO
NOVELTY_DECLARED = NO
EXECUTION_STATE = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
```

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B02_SECTION_4_3
EXECUTION_STATE = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
REPOSITORY = elVladdi/gci-nandina-rag
BRANCH = article/main-manuscript
INPUT_HEAD = d2c74644fd07d172fb54061ed43a524907a7d303
AUTHORIZED_SCOPE = SECTION_4_3_ONLY_ENGLISH_PLUS_SPANISH_SEMANTIC_MIRROR
```

The governing files, D-050/D-051, the B02 ground-truth review, the canonical V010 master, the required primary technical sources, and the live experimental Master Plan were checked before drafting. The local Markdown baseline matched the governed V010 SHA-256 and Git blob, and the DOCX baseline matched its governed SHA-256. `article/CLAIM_REGISTRY.md`, although named by the prompt, is not present on the input branch; no content was inferred for it. D-051, the ground-truth review, and the Claim-Evidence Matrix provide the block-specific epistemic controls used here.

The live `SRC-03` state is HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8` with Master Plan blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`. Its latest change is administrative activation of G7-F02 and does not materially alter the B02 documentary ground truth.

Primary-source verification confirms a Decision-885-derived hierarchical NANDINA corpus, exact NANDINA-8 lookup for each already fixed Top-3 candidate, no query-based normative retrieval in the primary path, no score fusion or documentary reranking, no candidate insertion/substitution, and no fallback to another code when exact evidence is absent. The disclosed Decision-906 boundary is a version/temporal limitation relative to the 2026 cases; no corrective quantitative result or blanket Chapter-87 invalidity claim is introduced.

The cumulative Markdown changes only the two Section-4.3 blocks. The cumulative DOCX was edited from the exact baseline binary; only `word/document.xml` changed, the 40 inherited comments remain intact, tracked changes remain zero, and the complete 41-page render was visually inspected without observed layout defects. Sections 4.4–4.8 and Results remain undrafted.

```text
SECTION_4_3_ONLY = YES
PRIMARY_RESOURCE = DECISION_885_DERIVED_HIERARCHICAL_NANDINA_CORPUS
PRIMARY_ASSOCIATION = EXACT_NANDINA8_CODE_LOOKUP
QUERY_BASED_NORMATIVE_RETRIEVAL_CLAIM = NO
DOCUMENTARY_RERANKING_CLAIM = NO
CANDIDATE_SUBSTITUTION_CLAIM = NO
DECISION_906_TEMPORAL_BOUNDARY_DISCLOSED = YES
DECISION_906_RESULTS_ANTICIPATED = NO
PERUVIAN_NATIONAL_AUTHORITY_MISATTRIBUTION = NO
ARANCEL2022_AS_PRIMARY_HE4_CONTEXT = NO
CLASSIFICATION_RESOLUTIONS_AS_PRIMARY_HE4_CONTEXT = NO
LEGAL_CORRECTNESS_CLAIM = NO
SECTION_4_4_PLUS_DRAFTED = NO
RESULTS_DRAFTED = NO
FROZEN_TEXT_MUTATED = NO
FINAL_GAP_DEFINED = NO
NOVELTY_DECLARED = NO
EXECUTION_STATE = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
```
