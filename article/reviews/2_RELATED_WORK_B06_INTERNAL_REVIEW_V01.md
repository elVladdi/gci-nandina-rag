# Related Work B06 — Internal Review V01

## 1. Identificación

```text
BLOCK = RELATED_WORK_B06
SECTION = 2.6 Positioning of this study
DELIVERY_COMMIT = f8756f5ed6ebed98a567186035082db96b618032
SECTION_FILE = article/sections/related_work/RelatedWork_B06_V01.md
MASTER_CANDIDATE = article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B06_V01.md
RESPONSE_FILE = article/responses/2_RELATED_WORK_B06_RESPONSE_V01.md
BASELINE_PARENT = 1e5b7fe4bfd2af2108a47137ffdba6ed8166b15e
REVIEW_TYPE = INDEPENDENT_EDITORIAL_AND_SOURCE_AUDIT
```

## 2. Dictamen

```text
SCIENTIFIC_REVIEW = PASS
SOURCE_SUPPORT = PASS / 4_OF_4_CITATIONS
SCOPE_CONTROL = PASS
POSITIONING_BOUNDARIES = PASS
EN_ES_SEMANTIC_CONTROL = PASS
KBS_PROSE_AND_SPCCR = PASS
COMMIT_SCOPE = PASS / EXACTLY_3_AUTHORIZED_MD_FILES
SINGLE_COMMIT_DISCIPLINE = PASS
DOCX_REPORTED_QA = CONSISTENT_WITH_D021
MATERIAL_SCIENTIFIC_ERRORS = 0
MANDATORY_CORRECTIONS = 0
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
INTEGRATION = BLOCKED_PENDING_AUTHOR_APPROVAL
INTRODUCTION = NOT_AUTHORIZED
```

**Resultado:** `PASS`. B06 V01 es científicamente aceptable para solicitar aprobación del autor. No se promueve todavía `ARTICLE_MASTER_V006` y no se abre Introduction.

## 3. Auditoría independiente claim-by-claim contra fuentes primarias

### C1 — Lee et al. (2021)

**Claim del manuscrito:** el sistema predice primero el heading, recupera sentencias del HS manual y utiliza la descripción junto con esas sentencias recuperadas para predecir la subpartida posterior.

**Verificación primaria:** `Classification of Goods Using Text Descriptions With Sentences Retrieval` fue reabierto y revisado directamente. El artículo describe tres etapas: heading prediction; sentence retrieval desde el HS manual del heading predicho; y subheading prediction usando conjuntamente la descripción y las sentencias recuperadas. La sección Method confirma que las key sentences recuperadas se concatenan con la descripción antes de la predicción de subheading.

```text
C1_SOURCE_SUPPORT = PASS
C1_OVERCLAIM = NO
```

### C2 — Lee et al. (2023)

**Claim del manuscrito:** primero se predicen candidatos HS y luego se recupera evidencia del HS manual asociada con esos candidatos para apoyar la revisión humana.

**Verificación primaria:** `Explainable Product Classification for Customs` fue reabierto y revisado directamente. Los autores describen explícitamente un modelo de dos etapas: primero predice la clasificación del ítem y luego recupera evidencia sobre cada candidato desde el HS manual. La salida combina códigos candidatos y sentencias pertinentes como evidencia explicable para inspección de oficiales.

Este antecedente impide presentar `candidate prediction + evidence retrieval` como elemento diferenciador por sí solo, exactamente como exige el freeze de 0B-06.

```text
C2_SOURCE_SUPPORT = PASS
C2_PRIOR_ART_RECOGNITION = PASS
C2_OVERCLAIM = NO
```

### C3 — Wang et al. (2026)

**Claim del manuscrito:** la evidencia regulatoria interviene durante la búsqueda jerárquica y ayuda a seleccionar el siguiente salto; después de fijar la ruta se agrega evidencia para verificación y generación de rationale.

**Verificación primaria:** se revisó el full text primario de `Constraint-Aware Hierarchical Search for Regulation-Driven Fine-Grained Classification` (arXiv:2607.10588). El método recupera nodos hijos y evidencia en cada nivel; un decision model/LLM selecciona el siguiente hop o stop; después de fijar el path, la evidencia de los nodos visitados se agrega para verificación final y rationale generation.

La formulación de B06 preserva correctamente la diferencia entre `SEARCH_CONTROL / NEXT_HOP_DECISION` y `EXPLANATION_ONLY_GENERATION`.

```text
C3_SOURCE_SUPPORT = PASS
C3_FUNCTIONAL_DISTINCTION = PASS
C3_OVERCLAIM = NO
```

### C4 — Chen and Tanaka-Ishii (2026)

**Claim del manuscrito:** las fuentes jurídicas recuperadas forman parte de una representación/traza ejecutable que produce la etiqueta y puede ser refinada, incluida la posibilidad de nueva recuperación antes de la salida final.

**Verificación primaria:** se revisó el artículo primario `Executable explanation traces for legal LLM predictions via retrieval-augmented codification`, Frontiers in Artificial Intelligence (2026), DOI `10.3389/frai.2026.1905145`. El pipeline recupera autoridad legal, genera una representación/programa ejecutable, recibe feedback y puede refinar el programa o emitir recuperación adicional antes de producir la salida final. El propio artículo separa source support de legal correctness.

B06 utiliza este trabajo de manera acotada: como prior art contra una separación amplia entre explicación/auditabilidad y decisión, no como antecedente equivalente al Top-k upstream externo e inmutable.

```text
C4_SOURCE_SUPPORT = PASS
C4_SCOPE = PASS
C4_OVERCLAIM = NO
```

## 4. Coherencia con el posicionamiento congelado

La subsección implementa correctamente el objeto diferenciador ya congelado en `0C_SCIENTIFIC_POSITIONING_FROZEN.md`:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

La prosa no convierte ese contrato en novelty. Reconoce explícitamente que Lee et al. (2023) ya combina candidate prediction y evidence retrieval, y formula la diferencia restante en términos de secuencia y límites de autoridad.

No se observó ninguna de las prohibiciones materiales:

- no `first`, `novel`, `unique`, `unprecedented` ni ausencia universal;
- no SOTA ni superioridad cross-study;
- no resultados o cifras del presente estudio;
- no inferencia de correctness jurídica a partir de evidencia, provenance o explanation;
- no generalización empírica derivada de configurability;
- no anticipación del gap final.

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
POSITIONING_FREEZE_COMPATIBILITY = PASS
```

## 5. Estilo científico y abstracción

Se realizó control específico por la regla editorial previamente fijada de evitar prosa de gobernanza, abstracciones acumulativas y lenguaje contractual visible.

Aunque la subsección emplea términos de posicionamiento como `decision authority`, `sequencing` y `functional contract`, estos no quedan como abstracciones autosuficientes: cada uno se operacionaliza inmediatamente mediante acciones observables —quién fija el Top-3, cuándo se recupera la evidencia, qué puede o no modificar el LLM y qué salida se evalúa—. No aparecen códigos internos de gobernanza, nombres de gates ni taxonomías editoriales en el texto publicable.

Por ello no se justifica una V02 meramente estilística.

```text
UNSUPPORTED_ABSTRACTION = NOT_FOUND
VISIBLE_GOVERNANCE_LANGUAGE = NOT_FOUND
EXCESSIVE_NOMINALIZATION = NOT_MATERIAL
SPCCR = PASS
```

## 6. Control del commit y del alcance

Se comparó `1e5b7fe4bfd2af2108a47137ffdba6ed8166b15e` contra `f8756f5ed6ebed98a567186035082db96b618032`.

Resultado:

```text
COMMITS_AHEAD = 1
FILES_CHANGED = 3
FILES_AUTHORIZED = 3
UNAUTHORIZED_FILES = 0
```

Archivos del commit:

1. `article/sections/related_work/RelatedWork_B06_V01.md`
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B06_V01.md`
3. `article/responses/2_RELATED_WORK_B06_RESPONSE_V01.md`

No se modificaron `ARTICLE_STATUS.md`, governance, los masters canónicos, Related Work B01–B05 ni secciones posteriores.

```text
NET_FILE_SCOPE = PASS
SINGLE_COMMIT_DISCIPLINE = PASS
NEXT_SECTION_OPENED = NO
```

## 7. Control EN–ES

La versión española conserva el significado científico de la versión inglesa en los cinco párrafos: antecedentes funcionales, Lee 2023 como prior art cercano, contraste con Wang/Chen, separación del pipeline del presente estudio y evaluación por función. No introduce novelty, causalidad, resultados ni mayor fuerza epistémica que el inglés.

```text
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MEANING_STRENGTHENING_IN_ES = NO
```

## 8. DOCX bajo D-021

La respuesta de ejecución registra:

```text
BASELINE_DOCX_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
PRIOR_COMMENTS = 32
NEW_B06_CITATION_COMMENTS = 4
TOTAL_COMMENTS = 36
TRACKED_CHANGES = 0
OOXML_INTEGRITY = PASS
RENDER = PASS / 29_PAGES
FINAL_DOCX_LOCAL_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
CUSTODY = LOCAL / AUTHOR / D021
```

El binario local no está en GitHub y, conforme a D-021, su ausencia remota no es defecto de entrega. Esta revisión verifica la consistencia del reporte con D-021; no afirma una reinspección byte-for-byte del binario local desde la sesión de la IA Gestora.

```text
DOCX_REMOTE_ABSENCE = EXPECTED_BY_D021
DOCX_REPORTED_QA = CONSISTENT
DOCX_BYTE_LEVEL_REINSPECTION_BY_GESTORA = NOT_PERFORMED / LOCAL_CUSTODY
```

## 9. Cierre de revisión

```text
RELATED_WORK_B06_V01_INTERNAL_REVIEW = PASS
MATERIAL_CORRECTIONS_REQUIRED = 0
AUTHOR_APPROVAL = REQUIRED
MASTER_PROMOTION = NOT_AUTHORIZED_YET
RELATED_WORK_CLOSURE = PENDING_AUTHOR_APPROVAL
INTRODUCTION = NOT_AUTHORIZED
```

Próximo paso permitido: solicitar exclusivamente la aprobación del autor sobre B06 V01. Si el autor aprueba, la IA Gestora podrá versionar el cierre/integración correspondiente, promover el master canónico y solo entonces evaluar el gate de Introduction. Si el autor no aprueba, debe emitirse una corrección B06 acotada; no se abre ningún bloque posterior.
