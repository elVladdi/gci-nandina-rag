# Prompt — Results B02 V01 narrow Spanish naturalness correction

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente la corrección estrecha autorizada por D-094 sobre Results B02 / Section 5.2. No avances a Results B03 ni a ninguna sección posterior.

Este prompt opera bajo MWDP v1.0, SPCCR, D-021/D-027/D-035, D-092, D-093 y D-094. El contenido científico de B02 V01 ya pasó auditoría Gestora; por tanto, **no debe reescribirse**.

### 1. Baselines exactos obligatorios

Usa exclusivamente los dos candidatos B02 V01 entregados al autor:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.md
BASELINE_MD_SHA256 = 87b85f095e0cef6d6f9b12e70223596b563014a38bcacfa37c4e0448a66dad6c
BASELINE_MD_GIT_BLOB_EXPECTED_FROM_BYTES = 804ae5709f08e878202f48465d4671bf70dc15c7

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.docx
BASELINE_DOCX_SHA256 = c267f7da5415161b812aed10cef66929b6b6cd2be51ecb2196d43c2e1180ce6f
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Verifica ambas identidades antes de editar. Si no coinciden, detente con `BLOCKED_BASELINE_IDENTITY_MISMATCH`.

No regreses a V017 ni a B01 para reconstruir los candidatos. No reconstruyas el DOCX desde Markdown. Edita directamente el binario Word exacto B02 V01.

### 2. Corrección autorizada — única

En **Part II — Spanish semantic-control mirror**, §5.2 solamente, aplica estas sustituciones exactas:

```text
A. "métricas de early ranking"
   → "métricas de desempeño en las primeras posiciones del ranking"

B. "framework primario"
   → "flujo primario del framework"

C. "Section 5.6"
   → "Sección 5.6"
```

La sustitución A debe aplicarse a las dos ocurrencias existentes en el cuerpo español de §5.2.

No cambies ninguna cifra, denominador, nombre de método, métrica, orden de resultados ni afirmación científica.

### 3. Contenido que debe permanecer byte/semanticamente estable

```text
PART_I_ENGLISH_SECTION_5_2 = PRESERVE_EXACTLY
SECTIONS_1_TO_5_1 = PRESERVE_EXACTLY
SECTIONS_5_3_PLUS = PRESERVE_EXACTLY
DISCUSSION = PRESERVE_EXACTLY
CONCLUSION = PRESERVE_EXACTLY
END_MATTER = PRESERVE_EXACTLY
NO_NEW_TABLE = TRUE
NO_NEW_LITERATURE = TRUE
NO_NEW_RESULT = TRUE
NO_INFERENCE = TRUE
NO_HE2_DISPOSITION = TRUE
```

No cambies `BM25 normativo flat`, `Exact Recall@100`, `Exact Recall@200`, `Pool@200` ni `Text2Trade-inspired MNRL`, porque son identificadores/denominaciones técnicas del bloque y no forman parte de la corrección autorizada.

### 4. D-035 — entrega timeout-safe

```text
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
REAL_FILE_HANDOFF_MD_DOCX_TO_AUTHOR = REQUIRED
```

Versiona en GitHub únicamente el artefacto pequeño de sección corregido y la response. Entrega los candidatos acumulativos MD/DOCX como archivos reales.

### 5. Artefactos obligatorios

Genera exactamente:

1. `article/sections/results/Results_B02_V02.md`;
2. `ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.md`;
3. `ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx`;
4. `article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V02.md`.

### 6. QA obligatorio

La response debe registrar al menos:

```text
PROTOCOL_READ = PASS
BLOCK = RESULTS_B02_SECTION_5_2
BLOCK_REVISION = V02
CORRECTION_DECISION = D-094
BASELINE_MD_SHA256 = 87b85f095e0cef6d6f9b12e70223596b563014a38bcacfa37c4e0448a66dad6c
BASELINE_DOCX_SHA256 = c267f7da5415161b812aed10cef66929b6b6cd2be51ecb2196d43c2e1180ce6f
ENGLISH_SECTION_5_2_PRESERVED = PASS
SPANISH_CORRECTION_A_OCCURRENCES = 2
SPANISH_CORRECTION_B_OCCURRENCES = 1
SPANISH_CORRECTION_C_OCCURRENCES = 1
NO_OTHER_SECTION_5_2_REWRITE = PASS
SECTIONS_OUTSIDE_5_2_PRESERVED = PASS
NUMERICAL_CONTENT_PRESERVED = PASS
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
ZIP_OOXML_INTEGRITY = PASS
COMMENTS_XML_BYTE_IDENTICAL = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = PASS
D035_TIMEOUT_SAFE_HANDOFF = PASS
BASE64_MANUAL = NO
CHUNKING = NO
FRAGMENTATION = NO
REASSEMBLY = NO
```

### 7. Exit

Cierra con:

```text
RESULTS_B02_V02_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

En chat responde únicamente en español con la ruta+commit exactos de la response y entrega `ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.md` y `.docx` como archivos reales. Detente después de B02 V02.

---

## English

Apply only the three frozen Spanish-mirror phrase corrections authorized by D-094 to the exact B02 V01 cumulative MD and DOCX. Preserve the English §5.2, all scientific/numerical content, all other sections, comments, and OOXML continuity. Do not advance beyond B02.