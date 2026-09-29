# D-166 — Front matter B02 / Final Title interpretive boundary

## Español

```text
DECISION = D-166
PHASE = FRONT_MATTER
BLOCK = FRONT_MATTER_B02_TITLE
CANONICAL_MASTER = ARTICLE_MASTER_V032
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V032.md
CANONICAL_MASTER_MD_SHA256 = 0fcf9c2676add5128f86efc50788335bc435077bedbd7a8aedbf73f8f1549f64
CANONICAL_MASTER_MD_GIT_BLOB = 0bfddcfc1c4a2fbb6a9f03d1141cd33f5b21334f
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 4709944a4653dac813b5ebe68b1b14a13c9b87ceddadd315308e975289335156
CANONICAL_MASTER_DOCX_SIZE_BYTES = 111028
CANONICAL_MASTER_DOCX_COMMENTS = 48
CANONICAL_MASTER_DOCX_TRACKED_CHANGES = 0
CANONICAL_MASTER_DOCX_PAGE_COUNT = 71

TITLE_EN = DRAFT
TITLE_ES = DRAFT_SEMANTIC_MIRROR
ABSTRACT_EN_ES = PRESERVE_FROZEN
KEYWORDS_EN_ES = PRESERVE_PLACEHOLDER
SECTIONS_1_TO_7 = PRESERVE_FROZEN
END_MATTER = PRESERVE
TITLE_EXECUTION = NOT_YET_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Función científica del título

El título final debe condensar el objeto científico del artículo, no el detalle del testbed.

Debe hacer visible, de manera sobria y reader-facing, la contribución central ya integrada:

- apoyo auditable a la decisión en clasificación arancelaria;
- separación explícita de autoridad entre ranking histórico de candidatos, asociación documental y explicación controlada;
- preservación de procedencia/trazabilidad entre esos outputs;
- evaluación diferenciada por función.

El título no necesita mencionar todas estas piezas. Debe seleccionar la formulación mínima que identifique inequívocamente el objeto metodológico.

### 2. Prioridad conceptual

Orden de prioridad:

```text
ARCHITECTURAL_METHOD_OBJECT
-> DISTINCTIVE_AUTHORITY_SEPARATION_PROPERTY
-> TARIFF_CLASSIFICATION_DECISION_SUPPORT_DOMAIN_IF_USEFUL
-> EMPIRICAL_TESTBED_ONLY_IF_NEEDED_FOR_PRECISION
```

La arquitectura/metodología debe gobernar el título. El dominio aduanero puede aparecer para concretar la tarea, pero no debe convertir el benchmark NANDINA/Capítulo 87 en el alcance conceptual del trabajo.

### 3. Patrón editorial KBS

El empirical guide de 34 artículos KBS registra:

```text
OBSERVED_TITLE_MEAN = 10.6 English words
OBSERVED_TITLE_RANGE = 7-14 English words
COLON_TWO_PART_TITLES = 17/34
```

Estos valores son guía editorial, no una restricción matemática rígida.

Se favorece un título técnico, específico y compacto. Puede emplearse una estructura de una parte o dos partes separadas por dos puntos cuando mejore precisión.

### 4. Contenido permitido

El título puede emplear, si resulta natural y fiel:

- auditable decision support;
- tariff classification;
- decision authority / authority separation;
- candidate ranking;
- documentary evidence;
- controlled explanation;
- provenance;
- configurable framework.

No es obligatorio incluir todos estos términos.

### 5. Contenido a evitar

No usar como framing principal:

- `RAG for HS classification`;
- `LLM + RAG + BM25`;
- `NANDINA Chapter 87` como definición del objeto científico;
- códigos experimentales internos;
- H100, EVAL, SERIE, DAM;
- Decision 885/906;
- porcentajes o métricas;
- nombres de fases internas.

Evitar títulos que sean una oración larga o una lista de componentes.

### 6. Claims prohibidos

El título no puede introducir ni insinuar:

```text
NOVEL / NOVELTY
FIRST
STATE_OF_THE_ART / SOTA
SUPERIOR / SUPERIORITY
ACCURATE / HIGH_ACCURACY
LEGAL_CORRECTNESS
HUMAN_VALIDATED
GENERALIZABLE / GENERALIZATION
DEPLOYMENT_READY / PRODUCTION_READY
AUTONOMOUS_CLASSIFICATION
END_TO_END_CLASSIFIER
```

No convertir `auditable` en claim de auditoría jurídica o corrección legal. En el manuscrito, auditable se refiere a inspectabilidad/trazabilidad de outputs y evidencia dentro del flujo evaluado.

### 7. Frontera de autoridad

El título debe ser compatible con:

```text
historical retrieval = candidate generation/ranking authority
fixed Top-3 = fixed before documentary association and generation
documentary association = evidence attachment / no reranking
local LLM = controlled explanation only
```

Debe evitar cualquier título que sugiera que el LLM clasifica, que la evidencia normativa decide el ranking o que todo el pipeline es un único clasificador.

### 8. Testbed y alcance

El benchmark NANDINA-8 / Chapter 87 puede figurar únicamente si aporta precisión editorial real. Si aparece:

- debe quedar como aplicación, contexto o testbed;
- no debe sugerir que la arquitectura se limita conceptualmente a Capítulo 87;
- no debe implicar generalización a otras jurisdicciones o dominios.

Preferencia editorial: mencionar `tariff classification` como dominio de tarea antes que detallar `NANDINA Chapter 87` en el título.

### 9. Inglés y español

El inglés es publication-facing.

El título español debe ser un espejo semántico natural y conservar:

- mismo objeto científico;
- misma fuerza epistémica;
- mismo alcance;
- ausencia de claims promocionales.

No traducir literalmente si una formulación natural en español requiere ajuste sintáctico.

### 10. Diferencial permitido

El futuro bloque B02 podrá cambiar únicamente:

- contenido del placeholder de `## Title`;
- contenido del placeholder de `## Título`.

Debe preservar exactamente:

- Abstract/Resumen aprobados;
- Keywords/Palabras clave placeholders;
- Sections 1–7;
- end matter;
- comentarios/anclajes Word;
- 0 tracked changes.

### 11. Criterio de aceptación Gestora

IA Gestora evaluará:

```text
SCIENTIFIC_OBJECT_VISIBILITY
ARCHITECTURAL_CONTRIBUTION_VISIBILITY
AUTHORITY_BOUNDARY_FIDELITY
TASK_DOMAIN_PRECISION
TESTBED_SCOPE_HYGIENE
ANTI_OVERCLAIMING
KBS_TITLE_CONCISION
READER_FACING_NATURALNESS
EN_ES_SEMANTIC_EQUIVALENCE
NO_INTERNAL_TERMINOLOGY
```

No se autoriza todavía Keywords ni end matter.

---

## English

The final title must foreground the architectural-methodological object of the paper: auditable tariff-classification decision support built around explicit separation of authority among candidate ranking, documentary association, and controlled explanation. The customs/tariff domain may identify the task, but NANDINA Chapter 87 must not replace the scientific object with the empirical testbed.

The 34-article KBS guide observed a mean title length of 10.6 words, a 7–14 word range, and two-part colon titles in 17/34 papers; these are editorial guides, not hard constraints. The title must remain concise, technical, non-promotional, and free of novelty, superiority, legal-correctness, human-validation, generalization, deployment-readiness, or autonomous-classifier claims.

Only Title/Título will be editable in B02. The approved Abstract/Resumen, Keywords placeholders, Sections 1–7, and end matter remain frozen.
