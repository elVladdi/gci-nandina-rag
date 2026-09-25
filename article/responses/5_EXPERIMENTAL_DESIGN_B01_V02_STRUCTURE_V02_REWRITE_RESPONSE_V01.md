# Experimental Design B01 V02 — Structure V02 rewrite response

## Part I — English

### Execution record

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
STRUCTURE_V02_GIT_BLOB_CHECK = f5270e02e3af1407a2dec2988d6382e433972d3e / PASS
SOURCE_MASTER_V009_GIT_BLOB_CHECK = 40f20437458715c615fc1762f025ebcdbb3b6fc2 / PASS
BASELINE_DOCX_SHA256_CHECK = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657 / PASS
SRC02_EXACT_FILE_CHECK = PASS / Anexo_1_NANDINA_LLM_RAG_v13 scientific identity
SRC03_HEAD_READ = b74b96d0163807007e4579d86450dd235125b30f
SRC03_BLOB_READ = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
SRC03_MATERIAL_CHANGE = NO
AUTHORIZED_SCOPE_ONLY = PASS
SECTION_3_FORWARD_REFERENCE_AMENDMENT_COUNT = 2
SECTION_4_3_AND_LATER_MODIFIED = NO
SHA_PATH_FILENAME_DISCLOSURE_IN_B01_PROSE = NONE
RESULTS_LEAKAGE = NONE
NEW_LITERATURE = NONE
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 40
SECTION_MD_PATH = article/sections/experimental_design/Experimental_Design_B01_V02.md
SECTION_MD_SHA256 = 7e9337fa6e8f0f33c6863c9292cb3f697fbcd7654630656518f6b83c14f75b4b
SECTION_MD_GIT_BLOB = 2f78e3c3f66e797c8328ae6f4b2dddd7c1871e7d
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
MASTER_CANDIDATE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
CANDIDATE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED / SUSPENDED
SECTION_4_3 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_DESIGN_B01_V02_REWRITE = DELIVERED_FOR_GESTORA_AUDIT
```

### Claim/fact traceability

| Claim/fact used in B01 | Primary source | Scope / strength |
|---|---|---|
| The evaluation is offline, bounded to eight-digit NANDINA within Chapter 87; SERIE is the analysis unit and DAM is the grouping unit when dependence matters. | SRC-03 living Master Plan; SRC-02 v13; D-046 | Experimental-setting fact for this instantiation only; no empirical generalization beyond the evaluated setting. |
| Administrative source and collection conditions: SUNAT Aduanet, import for consumption, Maritime Customs Office of Callao (118), declarations numbered 2 Jan–30 Mar 2026, collection 11–20 Apr 2026, orange/red channels, recorded cancellation date, authorized release, and at least one Chapter-87 tariff item. | SRC-02 v13 | Direct description of the governed collection procedure; administrative reference labels are not treated as legal ground truth. |
| Eligible declarations were opened and their series manually copied to the initial collection register; consultation screenshots were retained as procedural evidence rather than an additional label source. | SRC-02 v13 | Direct collection-method fact. |
| Automated Python processing converts collected material to one row per SERIE, preserves/concatenates merchandise-description lines, derives reproducible series identity and tariff hierarchy fields, and applies verified text preparation. | Frozen `sunat_series_parser.py`; SRC-02 v13 | Processing operations only to the extent directly implemented/documented. |
| Curation checks required fields, non-empty description, valid eight-digit NANDINA, hierarchical consistency, Chapter-87 membership, and critical parse-warning controls; exact admissible duplicates are collapsed and conflicting identifier groups are excluded. | Frozen `build_data_aduanas_splits.py`; frozen parser; SRC-02 v13 | Executed curation logic; no additional cleaning/imputation rule inferred. |
| Reconstructed intermediate: 11,320 series from 107 DAM; 4,232 Chapter-87 records before curation; 4,106 curated records. | SRC-03; SRC-02 v13; frozen processing artifacts | Dataset-construction counts, not performance results. |
| Version 0.2 uses explicit DAM assignments; the recorded seed is provenance metadata rather than the allocation mechanism. | Frozen v0.2 split metadata and configuration; SRC-03 | Split-construction mechanism. |
| Version 0.2 has zero DAM overlap and zero reproducible series-identifier overlap across historical, development, and evaluation partitions. | Frozen v0.2 split metadata/configuration; C06 | Structural partition control; detailed leakage/duplicate diagnostics deferred to Section 4.4. |
| Final composition: historical bank 2,950 series / 28 DAM / 66 represented codes; development 100 / 6 / 9; evaluation 1,056 / 67 / 42 represented reference codes. | Frozen v0.2 split metadata/configuration; SRC-03 | Descriptive dataset composition. The 66 historical codes are represented codes, not an exhaustive Chapter-87 universe. |
| Relevant processed historical content can be functionally reconstructed, but binary identity with the complete historical source workbook is not claimed. | SRC-03 forensic audit; SRC-02 v13 | Bounded provenance statement; no binary-identity claim. |

### Evidence omitted for insufficiency

None within the empirical facts actually used in this authorized B01 block. Claims outside the authorized scope, including performance, legal correctness, and empirical generalization, were not introduced.

---

## Part II — Spanish semantic-control mirror

### Registro de ejecución

```text
BLOCK = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
STRUCTURE_V02_GIT_BLOB_CHECK = f5270e02e3af1407a2dec2988d6382e433972d3e / PASS
SOURCE_MASTER_V009_GIT_BLOB_CHECK = 40f20437458715c615fc1762f025ebcdbb3b6fc2 / PASS
BASELINE_DOCX_SHA256_CHECK = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657 / PASS
SRC02_EXACT_FILE_CHECK = PASS / identidad científica Anexo_1_NANDINA_LLM_RAG_v13
SRC03_HEAD_READ = b74b96d0163807007e4579d86450dd235125b30f
SRC03_BLOB_READ = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
SRC03_MATERIAL_CHANGE = NO
AUTHORIZED_SCOPE_ONLY = PASS
SECTION_3_FORWARD_REFERENCE_AMENDMENT_COUNT = 2
SECTION_4_3_AND_LATER_MODIFIED = NO
SHA_PATH_FILENAME_DISCLOSURE_IN_B01_PROSE = NONE
RESULTS_LEAKAGE = NONE
NEW_LITERATURE = NONE
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 40
SECTION_MD_PATH = article/sections/experimental_design/Experimental_Design_B01_V02.md
SECTION_MD_SHA256 = 7e9337fa6e8f0f33c6863c9292cb3f697fbcd7654630656518f6b83c14f75b4b
SECTION_MD_GIT_BLOB = 2f78e3c3f66e797c8328ae6f4b2dddd7c1871e7d
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
MASTER_CANDIDATE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
CANDIDATE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED / SUSPENDED
SECTION_4_3 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_DESIGN_B01_V02_REWRITE = DELIVERED_FOR_GESTORA_AUDIT
```

### Trazabilidad claim/hecho

| Claim/hecho utilizado en B01 | Fuente primaria | Alcance / fuerza |
|---|---|---|
| La evaluación es offline, acotada a NANDINA de ocho dígitos dentro del Capítulo 87; SERIE es la unidad de análisis y DAM la unidad de agrupamiento cuando la dependencia es relevante. | SRC-03 Plan Maestro vivo; SRC-02 v13; D-046 | Hecho del entorno experimental de esta instanciación; sin generalización empírica fuera del escenario evaluado. |
| Fuente administrativa y condiciones de recolección: Aduanet/SUNAT, importación para el consumo, Aduana Marítima del Callao (118), declaraciones numeradas del 2 ene al 30 mar 2026, acopio del 11 al 20 abr 2026, canales naranja/rojo, fecha de cancelación registrada, levante autorizado y al menos una partida del Capítulo 87. | SRC-02 v13 | Descripción directa del procedimiento gobernante de recolección; las etiquetas administrativas de referencia no se tratan como verdad jurídica. |
| Las declaraciones elegibles se abrieron y sus series se copiaron manualmente al registro inicial; las capturas se conservaron como evidencia del procedimiento y no como fuente adicional de etiquetas. | SRC-02 v13 | Hecho directo del método de recolección. |
| El procesamiento automatizado en Python transforma el material recolectado en una fila por SERIE, conserva/concatena líneas de descripción, deriva identidad reproducible de serie y campos jerárquicos arancelarios y aplica la preparación textual verificada. | `sunat_series_parser.py` congelado; SRC-02 v13 | Operaciones de procesamiento solo en la medida directamente implementada/documentada. |
| La curación comprueba campos requeridos, descripción no vacía, NANDINA válido de ocho dígitos, coherencia jerárquica, pertenencia al Capítulo 87 y advertencias críticas de parseo; los duplicados exactos admisibles se colapsan y los grupos conflictivos se excluyen. | `build_data_aduanas_splits.py` congelado; parser congelado; SRC-02 v13 | Lógica de curación ejecutada; no se infieren reglas adicionales de limpieza o imputación. |
| Intermedio reconstruido: 11,320 series de 107 DAM; 4,232 registros del Capítulo 87 antes de curación; 4,106 registros curados. | SRC-03; SRC-02 v13; artefactos de procesamiento congelados | Conteos de construcción de datasets, no resultados de desempeño. |
| La versión 0.2 utiliza asignaciones explícitas de DAM; la semilla registrada es metadato de procedencia y no el mecanismo de asignación. | Metadata y configuración v0.2 congeladas; SRC-03 | Mecanismo de construcción de particiones. |
| La versión 0.2 tiene cero solapamiento de DAM y cero solapamiento del identificador reproducible de serie entre histórico, desarrollo y evaluación. | Metadata/configuración v0.2 congeladas; C06 | Control estructural de partición; diagnósticos detallados de leakage/duplicados se difieren a 4.4. |
| Composición final: banco histórico 2,950 series / 28 DAM / 66 códigos representados; desarrollo 100 / 6 / 9; evaluación 1,056 / 67 / 42 códigos de referencia representados. | Metadata/configuración v0.2 congeladas; SRC-03 | Composición descriptiva de datasets. Los 66 códigos históricos son códigos representados, no un universo exhaustivo del Capítulo 87. |
| El contenido histórico procesado relevante puede reconstruirse funcionalmente, pero no se afirma identidad binaria con el workbook histórico completo. | Auditoría forense de SRC-03; SRC-02 v13 | Afirmación acotada de procedencia; sin claim de identidad binaria. |

### Evidencia omitida por insuficiencia

Ninguna dentro de los hechos empíricos efectivamente utilizados en este bloque B01 autorizado. No se introdujeron claims fuera del alcance autorizado, incluidos desempeño, corrección jurídica o generalización empírica.
