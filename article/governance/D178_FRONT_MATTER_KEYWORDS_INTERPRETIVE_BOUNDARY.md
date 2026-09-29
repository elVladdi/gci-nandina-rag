# D-178 — Front matter B03 / Keywords editorial boundary

## Español

```text
DECISION = D-178
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B03_KEYWORDS

CANONICAL_MASTER = article/manuscript/ARTICLE_MASTER_V033.md
CANONICAL_MASTER_SHA256 = bf90c8b10891d401aa34f7553248f30578c1e4b98bef0bcbf32ec1da4446c9f1
CANONICAL_MASTER_GIT_BLOB = 9b87c71290126f5223c6e4a252f95b5d64f71f49

CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_TITLE_B02_V03.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 1451c7c2d9a013603c749a7ad0730ea450f76700ff853b6d96d9d1f865882ed1
CANONICAL_MASTER_DOCX_SIZE_BYTES = 110921
CANONICAL_MASTER_DOCX_COMMENTS = 48
CANONICAL_MASTER_DOCX_TRACKED_CHANGES = 0
CANONICAL_MASTER_DOCX_PAGE_COUNT = 71

TITLE = CLOSED / APPROVED / FROZEN / INTEGRATED
ABSTRACT = CLOSED / APPROVED / FROZEN / INTEGRATED

KEYWORD_COUNT = 7
KEYWORDS_EN_EXACT =
1. Knowledge-based decision support
2. Tariff classification
3. Harmonized System
4. Information retrieval
5. Documentary evidence
6. Large language models
7. Provenance and traceability

KEYWORDS_ES_EXACT =
1. Apoyo a la decisión basado en conocimiento
2. Clasificación arancelaria
3. Sistema Armonizado
4. Recuperación de información
5. Evidencia documental
6. Modelos de lenguaje grandes
7. Procedencia y trazabilidad

KEYWORDS_STATUS = BOUNDARY_FIXED / NOT_YET_MATERIALIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Función editorial

Las Keywords deben complementar Title y Abstract, no volver a redactarlos.

El master V033 ya establece explícitamente que las Keywords deben representar:

```text
CONTRIBUTION + APPLICATION_DOMAIN
WITHOUT_REDUCING_THE_WORK_TO_THE_TESTBED
```

D-178 aplica ese principio con una selección de siete términos/frases que cubren:

- identidad científica del sistema;
- dominio de aplicación;
- vocabulario de clasificación aduanera buscable;
- función de recuperación;
- función de evidencia;
- componente generativo;
- propiedad de provenance/traceability.

### 2. Relación con el patrón editorial KBS

El corpus aceptado de *Knowledge-Based Systems* muestra que las palabras clave suelen combinar:

- objeto o dominio;
- método/familia técnica;
- mecanismo o representación;
- concepto evaluado cuando es central.

No existe obligación de repetir literalmente el título completo ni de usar el nombre de la revista como etiqueta.

La selección se mantiene suficientemente estándar para recuperación bibliográfica y evita términos internos del proyecto.

### 3. Justificación de cada keyword

#### Knowledge-based decision support

Representa el objeto científico global ya sustentado en el manuscrito. Se usa como caracterización de sistema, no como afirmación de expert system simbólico clásico.

#### Tariff classification

Es el dominio científico/aplicado principal y debe mantenerse visible para indexación.

#### Harmonized System

Aporta el vocabulario estándar del dominio aduanero sin reducir el artículo a NANDINA Chapter 87. NANDINA es una nomenclatura regional basada en HS y el testbed no define el alcance conceptual.

#### Information retrieval

Cubre la familia técnica del ranking histórico y la recuperación de material documental sin fijar la arquitectura a BM25.

#### Documentary evidence

Representa la segunda función gobernada del sistema: asociación de evidencia identificable con candidatos ya fijados.

#### Large language models

Representa la familia tecnológica de la etapa explicativa sin afirmar que el LLM clasifique o determine el ranking.

#### Provenance and traceability

Representa la propiedad transversal que permite inspeccionar las relaciones entre query, precedente histórico, candidato, evidencia y explicación. No equivale a legal correctness ni human validation.

### 4. Términos deliberadamente excluidos

```text
AUDITABLE / AUDITABILITY =
NOT_SELECTED_AS_KEYWORD
Reason: central interpretive concept but qualitative evidence is partial and LLM-as-judge; provenance/traceability is the more directly established property.

RAG / RETRIEVAL-AUGMENTED_GENERATION =
NOT_SELECTED
Reason: manuscript explicitly distinguishes this architecture from using RAG as a catch-all label.

BM25 =
NOT_SELECTED
Reason: implementation-specific; architecture does not require BM25.

NANDINA / CHAPTER_87 / PERU =
NOT_SELECTED
Reason: experimental testbed, not conceptual scope.

ARTIFICIAL_INTELLIGENCE =
NOT_SELECTED
Reason: overly broad; Large language models is the specific generative family actually instantiated.

EXPLAINABLE_AI =
NOT_SELECTED
Reason: would import a broader XAI framing than the controlled-explanation evidence directly supports.

LEGAL_CORRECTNESS / HUMAN_VALIDATION / DEPLOYMENT =
PROHIBITED
```

### 5. Bilingual equivalence

La versión española es una traducción semántica natural de la lista inglesa.

`Procedencia y trazabilidad` se utiliza como espejo de `Provenance and traceability`; no convierte provenance en una afirmación de corrección.

### 6. Scope de materialización

La siguiente ejecución solo podrá sustituir:

- `## Keywords`;
- `## Palabras clave`.

Title/Título y Abstract/Resumen están congelados.

Sections 1–7 y end matter permanecen fuera de scope.

### 7. Gate

```text
CURRENT_GATE = FRONT_MATTER_B03_KEYWORDS_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_AND_REVIEW_KEYWORDS_B03_V01_PROMPT

CANONICAL_MASTER = ARTICLE_MASTER_V033
CANONICAL_MASTER_GIT_BLOB = 9b87c71290126f5223c6e4a252f95b5d64f71f49

TITLE = CLOSED / APPROVED / FROZEN / INTEGRATED
ABSTRACT = CLOSED / APPROVED / FROZEN / INTEGRATED
KEYWORDS = BOUNDARY_FIXED / V01_REQUIRED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

D-178 fixes the editorial boundary for Keywords B03 after verified integration of Title B02 V03 into canonical V033.

The exact seven English/Spanish keywords are selected to cover the system's scientific identity, tariff-classification domain, broadly searchable customs terminology, retrieval function, documentary-evidence function, LLM explanation component, and provenance/traceability.

Auditability, RAG, BM25, NANDINA/Chapter 87, generic AI, and Explainable AI are deliberately excluded for claim-calibration or scope reasons. Only the Keywords/Palabras clave blocks may change in the next execution.
