# Prompt — Experimental Design B07 V01 narrow public-reproducibility scope correction

## Español

### Rol

Actúa como **IA de Redacción científica**. Corrige exclusivamente B07 / Section 4.8 a partir de los candidatos B07 V01 ya entregados. No reescribas el bloque completo y no avances a Results.

Este prompt opera bajo MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-078, D-079, D-080, D-081 y especialmente D-082. D-082 prevalece sobre D-079 únicamente respecto de la presencia narrativa del repositorio interno de desarrollo en Section 4.8.

### 1. Baselines exactos obligatorios

Usa exclusivamente los dos candidatos B07 V01 entregados al autor:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md
BASELINE_MD_SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
BASELINE_MD_GIT_BLOB_EXPECTED_FROM_BYTES = 0d8a4ad3dd03c5b69feeec6a5710d296a5a76662

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
BASELINE_DOCX_SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Si cualquiera de los hashes no coincide, detente con `BLOCKED_BASELINE_IDENTITY_MISMATCH`.

No regreses a V015/B06 para editar. No reconstruyas el DOCX desde Markdown.

### 2. D-035 activado

Existe antecedente inmediato de timeout en B07. Por tanto, D-035 está activado:

```text
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
REAL_FILE_HANDOFF_TO_AUTHOR = REQUIRED
```

La response pequeña sí debe versionarse en GitHub. Los candidatos acumulativos MD/DOCX deben entregarse como archivos reales al autor.

### 3. Corrección única autorizada

El autor rechazó B07 V01 porque Section 4.8 abre presentando el repositorio interno de desarrollo experimental y comparándolo con el repositorio público de reproducibilidad.

Esa presentación debe eliminarse.

#### B07-C01 — foco exclusivo en el recurso público

En la versión corregida:

- Section 4.8 debe abrir directamente con el repositorio público `gci-nandina-rag-reproducibility`;
- no menciones ni describas el repositorio interno de desarrollo experimental en la prosa del manuscrito;
- no establezcas una comparación `development repository vs public repository`;
- si necesitas referirte a recursos no públicos, usa formulaciones científicas como `restricted or non-redistributed reference inputs`, sin dirigir al lector al repositorio interno.

Conserva las fronteras ya correctas de B07 V01:

- recursos actualmente materializados vs planificados/no materializados;
- paquete público todavía no equivalente a una release computacional completa;
- interfaces objetivo no presentadas como runners ya ejecutables;
- reference reproduction vs external replication;
- configurabilidad como propiedad de diseño, no generalización empírica;
- datos administrativos de referencia no afirmados como públicamente redistribuidos;
- recheck del snapshot antes de submission.

### 4. Alcance diferencial estricto

Solo puede cambiar Section 4.8 EN/ES y únicamente lo necesario para B07-C01.

```text
SECTIONS_1_TO_4_7 = BYTE/SEMANTICALLY PRESERVED
RESULTS_PLUS = PRESERVED
NO_NEW_RESULTS
NO_NEW_CLAIMS
NO_NEW_LITERATURE
NO_SCOPE_EXPANSION
```

La versión española debe ser semánticamente equivalente a la inglesa.

### 5. Artefactos obligatorios

Genera exactamente:

1. `article/sections/experimental_design/Experimental_Design_B07_V02.md`;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md`;
3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx`;
4. `article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V02.md`.

### 6. QA obligatorio

La response debe registrar al menos:

```text
PROTOCOL_READ = PASS
CORRECTION_SCOPE = B07-C01 ONLY
BASELINE_MD_SHA256
BASELINE_DOCX_SHA256
INTERNAL_DEVELOPMENT_REPOSITORY_MENTION_IN_SECTION_4_8 = NONE
PUBLIC_REPRO_REPOSITORY_FOCUS = PASS
MATERIALIZED_VS_PLANNED_VS_RESTRICTED = PASS
REFERENCE_REPRODUCTION_VS_EXTERNAL_REPLICATION = PASS
CONFIGURABILITY_GENERALIZATION_BOUNDARY = PASS
SECTION_4_8_ONLY_DIFF = PASS
SECTIONS_1_TO_4_7_PRESERVED = PASS
RESULTS_PLUS_PRESERVED = PASS
EN_ES_EQUIVALENCE = PASS
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
ZIP_OOXML_INTEGRITY = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
D035_TIMEOUT_SAFE_HANDOFF = PASS
BASE64_MANUAL = NO
CHUNKING = NO
FRAGMENTATION = NO
REASSEMBLY = NO
```

### 7. Exit

Cierra con:

```text
B07_V02_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

En chat responde únicamente en español con la ruta+commit exactos de la response y entrega los candidatos MD/DOCX como archivos reales. Detente después de B07 V02.

---

## English

Act only on the narrow author-requested B07-C01 correction. Use the exact B07 V01 MD/DOCX candidates as baselines. Remove the internal experimental-development repository from Section 4.8 manuscript prose and focus directly on the public `gci-nandina-rag-reproducibility` resource. Preserve all other B07 boundaries and all content outside Section 4.8.

Because B07 already experienced a timeout, D-035 is active: do not use manual Base64, chunking, fragmentation, reassembly, or direct GitHub materialization of the large cumulative master. Deliver the corrected cumulative MD/DOCX as real files to the author; version only the small response and section artifact in GitHub.