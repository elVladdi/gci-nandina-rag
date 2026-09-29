# D-173 — Title B02 V02 KBS-identity editorial re-audit and V03 requirement

## Español

```text
DECISION = D-173
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE

CANONICAL_MASTER = ARTICLE_MASTER_V032
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
CANONICAL_MASTER_MD_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f

PREVIOUS_TITLE_CANDIDATE = TITLE_B02_V02
PREVIOUS_TITLE =
Separating Candidate Ranking, Documentary Evidence, and Explanation in Tariff Classification Decision Support

PREVIOUS_GATE_DECISION = D-172
PREVIOUS_GATE_STATUS = OPEN / AUTHOR_DECISION_NOT_YET_GIVEN
D172_DISPOSITION = SUPERSEDED_BEFORE_AUTHOR_APPROVAL

KBS_IDENTITY_EDITORIAL_REVIEW =
article/reviews/10_FRONT_MATTER_B02_TITLE_KBS_IDENTITY_EDITORIAL_REVIEW_V01.md@8bbc263e0a17972d9a04e73c0ac091e416594511
KBS_IDENTITY_EDITORIAL_REVIEW_GIT_BLOB =
ba9aed182dc806c6f3407e448202909a44d32cb8
KBS_IDENTITY_EDITORIAL_REVIEW_RESULT = REVISE_TITLE_TO_V03

TITLE_B02_V02_TECHNICAL_AUDIT = RETAINED_PASS
TITLE_B02_V02_SCIENTIFIC_FIDELITY = PASS
TITLE_B02_V02_FINAL_EDITORIAL_ACCEPTANCE = WITHDRAWN
TITLE_B02_V02_CANONICAL_PROMOTION = NOT_AUTHORIZED

TITLE_B02_V03_REQUIRED = YES

TARGET_TITLE_EN_V03 =
Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

TARGET_TITLE_ES_V03 =
Arquitectura basada en conocimiento para el apoyo a la decisión en clasificación arancelaria: separación del ranking de candidatos, la evidencia documental y la explicación

KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Motivo de reapertura

D-172 abrió el gate de aprobación autoral de Title B02 V02 después de una auditoría editorial, científica y técnica completa.

Antes de la aprobación del autor se realizó una revisión adicional centrada en una pregunta editorial de primera lectura: si un lector de *Knowledge-Based Systems*, sin conocer el manuscrito, identifica en el título no solo el dominio y la operación, sino también el objeto científico/computacional que hace natural el trabajo dentro de KBS.

El corpus de 34 artículos aceptados confirma que no es obligatorio incluir literalmente `AI` o `knowledge`. Sí existe, sin embargo, una regularidad fuerte: el título hace visible un objeto algorítmico, de representación, inferencia, aprendizaje, arquitectura o conocimiento.

V02 describe bien la separación funcional, pero no identifica con suficiente fuerza que la contribución es una arquitectura knowledge-based de apoyo a decisiones.

### 2. Validez de "knowledge-based"

El término queda autorizado únicamente como caracterización de sistema completo.

La arquitectura integra:

- historical precedents con labels y provenance;
- documentary/normative knowledge candidato-específico;
- candidate–evidence associations;
- provenance explícita;
- explicación generativa restringida al contexto suministrado.

El propio manuscrito utiliza `knowledge-based decision support` y `multi-stage knowledge-based systems`.

No se autoriza interpretar `knowledge-based` como:

- expert system simbólico clásico;
- razonamiento legal por reglas;
- knowledge graph obligatorio;
- corpus normativo con autoridad sobre el ranking;
- garantía de corrección normativa o jurídica.

### 3. Efecto sobre D-172

```text
D172_AUTHOR_APPROVAL_GATE = WITHDRAWN
D172_AUTHOR_DECISION = NONE
D172_CANONICAL_PROMOTION = NONE
V032_REMAINS_CANONICAL = YES
```

El candidato V02 permanece preservado como artefacto técnica y editorialmente auditado, pero deja de ser elegible para promoción canónica.

### 4. Frontera V03

El título V03 debe hacer visibles simultáneamente:

```text
CONTRIBUTION_TYPE = DECISION-SUPPORT ARCHITECTURE
KBS_IDENTITY = KNOWLEDGE-BASED
TASK_DOMAIN = TARIFF CLASSIFICATION
DISTINCTIVE_OPERATION =
SEPARATION OF CANDIDATE RANKING + DOCUMENTARY EVIDENCE + EXPLANATION
```

No debe:

- presentar AI/LLM como autoridad de clasificación;
- presentar documentary knowledge como fuente del ranking;
- reducir el alcance a NANDINA/Chapter 87;
- introducir novelty, first/SOTA, superiority, legal correctness, human validation, external generalization o deployment readiness.

### 5. Título fijado para V03

```text
TITLE_EN_V03 =
Knowledge-Based Decision-Support Architecture for Tariff Classification: Separating Candidate Ranking, Documentary Evidence, and Explanation

TITLE_ES_V03 =
Arquitectura basada en conocimiento para el apoyo a la decisión en clasificación arancelaria: separación del ranking de candidatos, la evidencia documental y la explicación
```

La IA de Redacción no debe generar alternativas. Debe materializar exactamente estos textos.

### 6. Baselines

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

No utilizar ningún candidato Title V01/V02 como baseline.

### 7. Gate

```text
CURRENT_GATE = FRONT_MATTER_B02_TITLE_V03_PROMPT_PREPARATION
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_AND_REVIEW_TITLE_B02_V03_PROMPT

CANONICAL_MASTER = ARTICLE_MASTER_V032
TITLE = V02_SUPERSEDED_EDITORIALLY / V03_REQUIRED
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
```

---

## English

D-173 withdraws the D-172 author-approval gate before any author decision and requires Title B02 V03.

The accepted-KBS corpus shows that literal use of "AI" or "knowledge" is not mandatory, but first-read recognition of the KBS-relevant computational, inferential, representational, learning, architectural, or knowledge object is a strong editorial pattern.

V03 therefore makes the contribution type, KBS scientific identity, task domain, and distinctive separation operation explicit. "Knowledge-based" is authorized only as a system-level characterization and does not imply symbolic expert-system reasoning, normative ranking authority, or legal correctness.

V032 remains canonical. Keywords and end matter remain unauthorized.
