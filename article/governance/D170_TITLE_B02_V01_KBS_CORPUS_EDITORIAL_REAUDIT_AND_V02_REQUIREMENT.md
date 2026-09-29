# D-170 — Title B02 V01 KBS corpus editorial re-audit and withdrawal of author approval gate

## Español

```text
DECISION = D-170
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE

CANONICAL_MASTER = ARTICLE_MASTER_V032
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
CANONICAL_MASTER_MD_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

PREVIOUS_TITLE_CANDIDATE = TITLE_B02_V01
PREVIOUS_TITLE =
Auditable Decision Support for Tariff Classification with Explicit Authority Separation

PREVIOUS_GATE_DECISION = D-169
PREVIOUS_GATE_STATUS = OPEN / AUTHOR_DECISION_NOT_YET_GIVEN
D169_DISPOSITION = SUPERSEDED_BEFORE_AUTHOR_APPROVAL

KBS_CORPUS_EDITORIAL_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_KBS_CORPUS_EDITORIAL_REVIEW_V01.md@6e0043e394d3bd996f13d0ec7bd8f8983df5fc71
KBS_CORPUS_EDITORIAL_REVIEW_GIT_BLOB =
99e1a51de0eab71159fdfe843bd7c0a9794d6002
KBS_CORPUS_EDITORIAL_REVIEW_RESULT = REVISE_TITLE

TITLE_B02_V01_TECHNICAL_AUDIT = RETAINED_PASS
TITLE_B02_V01_SCIENTIFIC_FIDELITY = PASS
TITLE_B02_V01_FINAL_EDITORIAL_ACCEPTANCE = WITHDRAWN
TITLE_B02_V01_CANONICAL_PROMOTION = NOT_AUTHORIZED

TITLE_B02_V02_REQUIRED = YES

TARGET_TITLE_EN_V02 =
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support

TARGET_TITLE_ES_V02 =
Separación del ranking de candidatos, la evidencia documental y la explicación en el apoyo a la decisión de clasificación arancelaria

KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Motivo de reapertura editorial

D-169 abrió el gate de aprobación autoral de Title B02 V01 después de una auditoría técnica y científica que permanece válida.

Antes de que el autor emitiera aprobación, se incorporó una nueva capa editorial solicitada expresamente por el autor: revisión del título frente al corpus completo de 34 artículos aceptados de la revista objetivo, *Knowledge-Based Systems*.

La auditoría de corpus no identifica una contradicción científica en V01. Identifica un problema de **representación editorial final**:

- `Explicit Authority Separation` es correcto pero abstracto para un lector externo;
- `Auditable` queda sobrerrepresentado como promesa principal respecto de la fortaleza específica de su evaluación cualitativa;
- el objeto metodológico que atraviesa todo el artículo es más concreto: separar candidate ranking, documentary evidence y explanation.

D-170 por tanto no revierte la validez técnica del candidato V01. Revierte únicamente su suficiencia editorial final.

### 2. Efecto sobre D-169

```text
D169_AUTHOR_APPROVAL_GATE = WITHDRAWN
D169_AUTHOR_DECISION = NONE
D169_CANONICAL_PROMOTION = NONE
V032_REMAINS_CANONICAL = YES
```

El candidato V01 queda preservado como artefacto históricamente auditado, pero no es elegible para promoción canónica.

### 3. Frontera editorial V02

El nuevo Title debe expresar directamente la operación que estructura el manuscrito:

```text
candidate ranking
+
documentary evidence
+
explanation
=
explicitly separated functions within tariff-classification decision support
```

El título no debe:

- convertir `auditability` en la promesa primaria;
- usar `authority separation` como concepto abstracto sin concretar sus objetos;
- mencionar NANDINA, Chapter 87, BM25, RAG, LLM o tecnologías como inventario;
- introducir novelty, first/SOTA, superiority, legal correctness, human validation, generalization o deployment readiness.

### 4. Título fijado para V02

La decisión editorial fija el siguiente texto para materialización:

```text
TITLE_EN_V02 =
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support

TITLE_ES_V02 =
Separación del ranking de candidatos, la evidencia documental y la explicación en el apoyo a la decisión de clasificación arancelaria
```

La IA de Redacción no debe generar alternativas. Su función en V02 será materializar exactamente estos dos títulos en Markdown y Word y ejecutar todos los controles diferenciales/OOXML/render.

### 5. Baselines

```text
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
INPUT_MASTER_MD_SHA256 = 0fcf9c2676add5128f86efc50788335bc435077bedbd7a8aedbf73f8f1549f64
INPUT_MASTER_MD_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx
INPUT_MASTER_DOCX_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156
INPUT_MASTER_DOCX_SIZE_BYTES = 111028
INPUT_MASTER_DOCX_COMMENTS = 48
INPUT_MASTER_DOCX_TRACKED_CHANGES = 0
INPUT_MASTER_DOCX_PAGE_COUNT = 71
```

No usar el candidato Word de Title V01 como baseline porque nunca fue aprobado ni promovido.

### 6. Gate

```text
CURRENT_GATE = FRONT_MATTER_B02_TITLE_V02_PROMPT_PREPARATION
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_AND_REVIEW_TITLE_B02_V02_PROMPT
CANONICAL_MASTER = ARTICLE_MASTER_V032
TITLE = V01_SUPERSEDED_EDITORIALLY / V02_REQUIRED
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

D-170 withdraws the D-169 author-approval gate before any author decision. Title B02 V01 remains technically and scientifically audited, but a full editorial audit against 34 accepted *Knowledge-Based Systems* articles found its final journal-facing formulation insufficient.

The revised title must expose the concrete methodological operation that structures the entire paper: separation of candidate ranking, documentary evidence, and explanation within tariff-classification decision support. The exact English and Spanish V02 titles are fixed above. V032 remains canonical; the unapproved V01 title candidate is not eligible for promotion. Keywords and end matter remain unauthorized.
