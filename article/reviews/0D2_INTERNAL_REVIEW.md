# Revisión interna 0D-2 V01 / 0D-2 V01 Internal Review

## Español

### Dictamen

```text
0D2_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
MATERIAL_ERRORS = 0
CORRECTIONS_REQUIRED = 4
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

La respuesta V01 conserva correctamente el estado científico congelado, no abre redacción de manuscrito, mantiene KBS → ESWA → IPM, formaliza una política de escritura y claim–evidence sólida, y recoge correctamente el workflow acumulativo `.md`/`.docx`, APA 7 provisional en Word, gestión final con Mendeley y comentarios de auditoría por cita.

No se detectó error científico material. Sin embargo, cuatro puntos deben corregirse antes de congelar 0D-2 porque afectan directamente la prevención de reescrituras y la gobernanza operativa.

### 0D2-M01 — Requisitos KBS potencialmente reescribientes todavía no suficientemente cerrados

**Estado:** `OPEN / CORRECTION_REQUIRED`.

V01 clasifica como `UNVERIFIED_NONBLOCKING` la plantilla KBS, límite de extensión y anonimización, y conserva detalles de estructura como `UNVERIFIED`/convención observada. Esto es demasiado permisivo para el objetivo expreso de 0D-2: cerrar antes de Fase 1 aquello capaz de producir reescritura.

La auditoría independiente confirmó en fuente oficial accesible que KBS enlaza un Guide for Authors vigente y que el scope exige investigación original en sistemas basados en conocimiento/IA. También confirmó que los artículos 2026 se etiquetan como `Research article`. Sin embargo, el cuerpo del Guide for Authors continúa inaccesible directamente en este entorno. Una reproducción secundaria fechada en 2026 muestra indicios de requisitos potencialmente relevantes —p. ej., recomendación de hasta 20 páginas de manuscrito a doble espacio para research/review papers y revisión single-anonymized—, pero, al no ser fuente primaria, esos datos NO se incorporan como requisitos cerrados.

**Corrección obligatoria:** V02 debe separar explícitamente:

```text
KBS_REQUIREMENTS_VERIFIED_FROM_PRIMARY
KBS_REQUIREMENTS_UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT
KBS_REQUIREMENTS_DEFERABLE_WITHOUT_REWRITE_RISK
```

Los requisitos no verificados que puedan afectar longitud, formato inicial o arquitectura deben quedar como condición pre-redacción o como una política interna conservadora que elimine efectivamente el riesgo. Si no puede demostrarse que la política interna neutraliza la reescritura, el gate debe quedar `BLOCKED`, no `PASS_WITH_CORRECTIONS`.

En particular, V02 debe justificar de forma explícita si un Word neutral puede absorber posteriormente el formato KBS sin reescritura científica y debe fijar desde el inicio una disciplina de extensión conservadora compatible con un posible límite de páginas, sin atribuir ese límite a KBS mientras no se verifique oficialmente.

### 0D2-M02 — La estructura bilingüe del Word fue introducida sin decisión expresa del autor

**Estado:** `OPEN / AUTHOR-DEPENDENT DESIGN DECISION`.

V01 introduce unilateralmente:

```text
Part I — English manuscript master
Part II — Spanish semantic-control mirror
```

en el mismo `.docx`. El autor sí fijó bilingüismo para artefactos GitHub y el inglés como idioma maestro del manuscrito, pero no aprobó específicamente que el Word acumulativo contenga una segunda parte española completa.

Esta decisión aumenta tamaño, mantenimiento y riesgo de desalineación del Word, por lo que no puede marcarse `CLOSED_FOR_DRAFTING` sin aprobación explícita.

**Corrección obligatoria:** V02 debe convertir esta solución en una decisión pendiente y presentar una alternativa mínima:

- `OPTION_A`: Word interno bilingüe Part I EN + Part II ES;
- `OPTION_B`: Word maestro solo en inglés y control semántico bilingüe conservado en los `.md`/artefactos de gobernanza.

No seleccionar unilateralmente una opción. Registrar `DOCX_LANGUAGE_LAYOUT = PENDING_AUTHOR_DECISION` hasta resolución del autor.

### 0D2-M03 — Política de citas del `.md` demasiado cercana al APA 7 provisional del Word

**Estado:** `OPEN / CORRECTION_REQUIRED`.

La regla autoral/prompt dice que **solo el Word** usa citas/referencias provisionales en APA 7. V01 indica que el `.md` mantiene citas visibles coherentes con el Word y una bibliografía verificable, lo que deja abierta la posibilidad de duplicar APA 7 en Markdown y crear una segunda superficie bibliográfica que luego deba reconvertirse.

**Corrección obligatoria:** V02 debe fijar que:

```text
WORD = provisional APA7 presentation layer
MARKDOWN = stable citation/source identifiers + human-readable citation placeholders as needed, but NOT a second APA7 formatting authority
```

El `.md` puede conservar trazabilidad de fuentes y correspondencia semántica, pero la presentación bibliográfica APA 7 provisional es exclusiva del Word.

### 0D2-M04 — Convención de versionado mezcla revisión de bloque e integración del master

**Estado:** `OPEN / CORRECTION_REQUIRED`.

V01 propone que una corrección use `V002`, `V003`, etc., mientras también establece que el número del master aumenta por integración aprobada y no por intentos descartados. Esto puede producir ambigüedad entre:

- revisión del mismo bloque;
- revisión del mismo master candidato;
- nueva integración aprobada al master.

**Corrección obligatoria:** separar los contadores. Ejemplo admisible:

```text
BLOCK_REVISION = B01_V01, B01_V02, ...
MASTER_INTEGRATION = MASTER_V001, MASTER_V002, ...
MASTER_CANDIDATE_REVISION = MASTER_V001_CANDIDATE_R01, R02, ...
```

Solo `MASTER_V00N` avanza cuando una integración es aprobada. Una corrección del mismo candidato no debe aparentar una nueva integración.

### Verificaciones que pasan sin corrección

- preservación de `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED`;
- RQ1/RQ2/RQ3/RQ4 y dependencias de Grupo 3;
- bloqueo C10/C11 para EXP-11B;
- separación candidate retrieval / normative evidence / controlled explanation;
- política anti-overclaiming y anti-alucinación;
- comentarios Word anclados por instancia de cita con fuente, autores, extracto original, traducción, justificación y límite;
- IA de Redacción como responsable de generar/actualizar `.md` y `.docx`;
- IA Gestora/IA Experimental/autor como auditores según competencia;
- APA 7 provisional en Word y Mendeley gestionado por el autor al final;
- estrategia KBS → ESWA → IPM y transferencia gobernada por motivo de rechazo;
- política Elsevier de declaración de uso de IA, verificada independientemente en fuente oficial;
- formato general Elsevier de highlights (3–5 bullets, ≤85 caracteres) verificado a nivel publisher, sin promoverlo indebidamente a requisito KBS específico.

### Gate

```text
0D2_V01 = PASS_WITH_CORRECTIONS
0D2_M01 = OPEN
0D2_M02 = OPEN
0D2_M03 = OPEN
0D2_M04 = OPEN
NEXT_ACTOR = IA_DE_REDACCION
REVISION_V02 = REQUIRED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Decision

```text
0D2_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
MATERIAL_ERRORS = 0
CORRECTIONS_REQUIRED = 4
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

V01 correctly preserves the frozen scientific state, does not open manuscript drafting, keeps the KBS → ESWA → IPM cascade, and establishes strong writing, claim–evidence, cumulative `.md`/`.docx`, provisional Word APA-7, final author-side Mendeley, and citation-comment governance.

No material scientific error was found. Four issues must nevertheless be corrected before 0D-2 can be frozen because they directly affect rewrite prevention and operational governance.

### 0D2-M01 — Potentially rewrite-relevant KBS requirements remain insufficiently closed

**Status:** `OPEN / CORRECTION_REQUIRED`.

V01 treats the KBS template, length limit, and anonymization as `UNVERIFIED_NONBLOCKING`, while article-structure details remain `UNVERIFIED`/observed convention. This is too permissive for the explicit purpose of 0D-2: to close before Phase 1 the decisions that can force later rewriting.

Independent audit confirmed from accessible official sources that KBS links a current Guide for Authors, its scope requires original research in knowledge-based/AI systems, and 2026 journal content is labelled `Research article`. The body of the Guide remains directly inaccessible in this environment. A 2026 secondary reproduction contains indications of potentially relevant rules—e.g., a preference for no more than 20 double-line-spaced manuscript pages for research/review papers and a single-anonymized review model—but these are NOT promoted to official requirements because the reproduction is not a primary source.

**Required correction:** V02 must explicitly separate:

```text
KBS_REQUIREMENTS_VERIFIED_FROM_PRIMARY
KBS_REQUIREMENTS_UNVERIFIED_BUT_POTENTIALLY_REWRITE_RELEVANT
KBS_REQUIREMENTS_DEFERABLE_WITHOUT_REWRITE_RISK
```

Any unverified item that may affect length, initial format, or architecture must either remain a pre-drafting condition or be neutralized by a conservative internal policy that demonstrably prevents scientific rewriting. If that cannot be shown, the gate must be `BLOCKED`, not `PASS_WITH_CORRECTIONS`.

V02 must specifically justify whether a neutral Word master can later absorb KBS formatting without scientific rewriting and must set a conservative length discipline from the start, without attributing an unverified page limit to KBS.

### 0D2-M02 — Bilingual Word layout was introduced without explicit author approval

**Status:** `OPEN / AUTHOR-DEPENDENT DESIGN DECISION`.

V01 unilaterally introduces:

```text
Part I — English manuscript master
Part II — Spanish semantic-control mirror
```

inside the same `.docx`. The author did establish bilingual GitHub artifacts and English as the master manuscript language, but did not specifically approve a full Spanish mirror inside the cumulative Word file.

This choice increases document size, maintenance, and divergence risk and therefore cannot be marked `CLOSED_FOR_DRAFTING` without explicit approval.

**Required correction:** V02 must present this as a pending decision with at least:

- `OPTION_A`: bilingual internal Word, Part I EN + Part II ES;
- `OPTION_B`: English-only Word master, with bilingual semantic control maintained in `.md`/governance artifacts.

Do not choose unilaterally. Record `DOCX_LANGUAGE_LAYOUT = PENDING_AUTHOR_DECISION` until the author resolves it.

### 0D2-M03 — Markdown citation policy is too close to the Word provisional APA-7 layer

**Status:** `OPEN / CORRECTION_REQUIRED`.

The author/prompt rule states that **only Word** uses provisional APA-7 citations/references. V01 says Markdown keeps visible citations consistent with provisional Word and a verifiable bibliography, leaving open the possibility of duplicating APA-7 formatting in Markdown and creating a second bibliography surface that later requires conversion.

**Required correction:** V02 must establish:

```text
WORD = provisional APA7 presentation layer
MARKDOWN = stable citation/source identifiers + human-readable citation placeholders as needed, but NOT a second APA7 formatting authority
```

Markdown may preserve source traceability and semantic correspondence, but provisional APA-7 presentation belongs exclusively to Word.

### 0D2-M04 — Versioning convention conflates block revision with master integration

**Status:** `OPEN / CORRECTION_REQUIRED`.

V01 proposes `V002`, `V003`, etc. for corrections while also stating that the master number increases only after approved integration. This creates ambiguity between block revision, candidate-master revision, and a newly approved master integration.

**Required correction:** separate the counters. One acceptable pattern is:

```text
BLOCK_REVISION = B01_V01, B01_V02, ...
MASTER_INTEGRATION = MASTER_V001, MASTER_V002, ...
MASTER_CANDIDATE_REVISION = MASTER_V001_CANDIDATE_R01, R02, ...
```

Only `MASTER_V00N` advances after an approved integration. Correcting a candidate must not look like a new integration.

### Checks passing without correction

The following pass: frozen scientific boundaries and RQs; Group-3 and EXP-11B restrictions; functional separation; anti-overclaiming/anti-hallucination controls; citation-anchored Word comments; Writing AI ownership of manuscript generation; audit-role separation; provisional APA 7 in Word and author-side final Mendeley management; KBS → ESWA → IPM cascade; Elsevier AI-disclosure policy; and publisher-level highlights format without falsely promoting it to a KBS-specific rule.

### Gate

```text
0D2_V01 = PASS_WITH_CORRECTIONS
0D2_M01 = OPEN
0D2_M02 = OPEN
0D2_M03 = OPEN
0D2_M04 = OPEN
NEXT_ACTOR = WRITING_AI
REVISION_V02 = REQUIRED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_AUTHORIZED
PHASE_1 = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```