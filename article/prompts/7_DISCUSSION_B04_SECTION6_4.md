# Prompt — Discussion B04 / Section 6.4 — Implications for auditable decision support

## Español

### Rol

Actúa exclusivamente como IA de Redacción del manuscrito. No cambies gobernanza, no recalcules resultados, no introduzcas literatura nueva y no avances fuera del bloque autorizado.

### Autorización

Ejecuta únicamente Discussion B04 V01 / Section 6.4 bajo:

`article/governance/D133_DISCUSSION_B04_SECTION6_4_INTERPRETIVE_BOUNDARY_AND_AUDITABILITY_TRACE.md`

Usa exclusivamente como baseline Markdown:

`article/manuscript/ARTICLE_MASTER_V026.md`

```text
SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
GIT_BLOB = f6a63be554317e62103aa96c1091f4039249e5ee
```

Usa como baseline Word exclusivamente:

`ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx`

```text
SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 64
```

No reconstruyas Word desde Markdown. D-035 sigue vigente: no Base64 manual, chunking, fragmentación ni reensamblado.

### Fuentes internas obligatorias

Interpreta exclusivamente contenido ya integrado de Sections 3.1–3.7, 5.3, 5.4, 5.7, 6.1, 6.2 y 6.3. Section 2.5 puede usarse solo como marco conceptual ya integrado; no introduzcas nuevas citas en §6.4.

### Función editorial de §6.4

Explicar las implicaciones del diseño y de la evidencia observada para apoyo a decisiones auditable. La sección debe conectar el contrato de autoridad con la posibilidad de inspeccionar por separado ranking, asociación documental y explicación, y debe mostrar por qué trazabilidad estructural no equivale a verificabilidad, calidad cualitativa, validación humana ni corrección jurídica.

### Ground truth obligatorio

Conserva exactamente estas distinciones:

- historical retrieval genera y ordena candidatos;
- el Top-3 se fija antes de documentary association;
- documentary association no inserta, elimina, sustituye ni reordena candidatos;
- el LLM local es downstream explanation-only y no puede cambiar candidatos ni retroalimentar clasificación;
- RQ2: asociación documental exacta en 3,168/3,168 slots y preservación de membership/orden en 1,056/1,056 casos;
- RQ3: preservación del Top-3/orden y controles estructurales en 50/50 casos; controles por slot válidos en 150/150;
- auditabilidad cualitativa = 28/50 = 56.0%;
- trazabilidad media = 2.00/2; verificabilidad media = 0.54/2; separación historical–normative = 1.04/2;
- schema compliance = 0/50 exclusivamente por `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` relativo a `advertencias_globales`;
- evaluación cualitativa = LLM-as-judge, no evaluadores humanos.

### Contenido obligatorio

Redacta aproximadamente 350–450 palabras en inglés y una versión española semánticamente equivalente. Usa preferentemente cinco párrafos por idioma:

1. **Implicación del contrato de autoridad.** Explica que la separación de autoridad permite atribuir cada salida a una etapa concreta: ranking histórico, asociación documental y explicación. La implicación es inspeccionabilidad del proceso, no corrección sustantiva.
2. **Provenance y revisión a nivel de candidato.** Usa RQ2/RQ3 para explicar que conservar candidate membership/order y vínculos históricos/normativos permite rastrear qué información acompaña a cada candidato sin confundir esa trazabilidad con legal correctness o classification accuracy.
3. **Trazabilidad no suficiente.** Interpreta 28/50 (56.0%), trazabilidad 2.00/2, verificabilidad 0.54/2 y separación historical–normative 1.04/2. Debe quedar explícito que una explicación puede ser completamente trazable y aun así insuficientemente verificable o poco clara en la separación del papel de las evidencias.
4. **Implicaciones de ingeniería/gobernanza.** Señala como consecuencias de diseño: autoridad no solapada, provenance por candidato, presentación diferenciada de historical evidence vs normative evidence, y coherencia versionada prompt/schema. Menciona el 0/50 únicamente como mismatch de especificación y como evidencia de que contratos de interfaz inconsistentes pueden degradar validación técnica; no como fallo sustantivo de 50 explicaciones.
5. **Límite de uso.** Cierra reafirmando decision support y human review: los resultados no validan sustitución de expertos, deployment operativo, causal safety, reducción de alucinaciones, legal correctness, human-validated auditability ni generalización externa.

### Claims permitidas

Puedes sostener que:

- la asignación explícita de autoridad hace posible atribuir e inspeccionar outputs por etapa;
- candidate-level provenance facilita revisión del vínculo entre candidato, histórico, evidencia documental y explicación;
- la preservación estructural observada demuestra cumplimiento del contrato en el piloto evaluado;
- la auditabilidad cualitativa parcial muestra que trazabilidad y verificabilidad no son equivalentes;
- la coherencia prompt/schema es una condición técnica necesaria para validación automática consistente;
- el sistema debe describirse como decision support sujeto a revisión humana.

### Claims prohibidas

No afirmar ni implicar:

- novelty, first-ever o state of the art;
- superioridad global o comparaciones numéricas con prior work;
- overall classification accuracy;
- que documentary association sea substantive normative correctness;
- que auditability sea legal correctness;
- validación humana o aceptación por customs officers;
- reducción de alucinaciones, mayor seguridad o efecto causal del warning/control;
- deployment readiness o cumplimiento normativo operacional;
- external generalization;
- nuevos resultados, CI, p-values o tests;
- `FINAL_GAP`.

### Citas y comentarios Word

No introduzcas nuevas ocurrencias bibliográficas en §6.4. Preserva exactamente los 48 comentarios heredados del Word B03.

```text
COMMENTS = 48
TRACKED_CHANGES = 0
```

### Diferencial autorizado

Modifica exclusivamente los placeholders inglés y español de Section 6.4. Preserva Sections 1–6.3, Discussion §6.5–§6.6, Conclusion y end matter.

### Entregables

1. `article/sections/discussion/Discussion_B04_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.docx`
4. `article/responses/7_DISCUSSION_B04_SECTION6_4_RESPONSE_V01.md`

La response debe declarar SHA-256, Git blob esperado del Markdown acumulativo, auditoría diferencial, equivalencia EN/ES, conservación exacta de comentarios, integridad OOXML, render completo y cumplimiento de D-035.

Detente al completar §6.4. No avances a §6.5 ni a Conclusion.

```text
EXPECTED_EXIT = DISCUSSION_B04_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Draft only Discussion Section 6.4 against canonical V026 and the approved B03 Word baseline. Interpret the fixed-Top-3 authority contract, RQ2 provenance/ranking invariance, and RQ3 structural plus qualitative auditability results as bounded implications for auditable decision support. Make explicit that traceability is not verification, human validation, legal correctness, safety, deployment validation, or overall classification accuracy. Use the 56.0% auditability result and the 0.54/2 verifiability and 1.04/2 evidence-separation means to show that structural traceability is not sufficient for high-quality review. Add no new citations or Word comments; preserve all 48 inherited comments. Stop before Section 6.5.