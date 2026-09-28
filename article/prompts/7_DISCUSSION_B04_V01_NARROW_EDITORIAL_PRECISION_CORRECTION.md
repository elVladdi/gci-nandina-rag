# Prompt — Discussion B04 V01 narrow editorial/scientific-precision correction — produce V02

## Español

### Rol

Actúa exclusivamente como IA de Redacción. Corrige Discussion B04 / §6.4 de forma estrecha conforme a la auditoría de IA Gestora. No redactes §6.5, §6.6 ni Conclusion y no modifiques ningún bloque previamente integrado.

### Onboarding y autoridades obligatorias

Antes de modificar artefactos, lee íntegramente y aplica:

1. `article/START_HERE.md`.
2. `article/README.md`.
3. `article/ARTICLE_STATUS.md`.
4. `article/ARTICLE_WRITING_PLAN.md`.
5. `article/DECISIONS.md`.
6. `article/SOURCE_REGISTRY.md`.
7. `article/CLAIM_EVIDENCE_MATRIX.md`.
8. `article/STYLE_GUIDE.md`.
9. `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` — MWDP v1.0.
10. `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md` — SPCCR v1.0.
11. `article/governance/D013_KBS_EMPIRICAL_WRITING_GUIDE_APPROVAL.md`.
12. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md` — contenido sustantivo aprobado por D-013.
13. `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`.
14. `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`.
15. `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`.
16. `article/governance/D133_DISCUSSION_B04_SECTION6_4_INTERPRETIVE_BOUNDARY_AND_AUDITABILITY_TRACE.md`.
17. `article/governance/D136_SUBSTANTIVE_EDITORIAL_AUDIT_AND_INTERNAL_TERMINOLOGY_CONTROL.md`.
18. `article/reviews/7_DISCUSSION_B04_SECTION6_4_INTERNAL_REVIEW_V01.md`.
19. La autorización vigente que apunte expresamente a este prompt.
20. Este prompt completo.

No uses una conversación anterior como fuente de verdad. Si el estado vivo contradice esta instrucción o si falta un baseline exacto, detente y registra la condición en la response versionada.

### Estado y artefactos de entrada

El master canónico sigue siendo `article/manuscript/ARTICLE_MASTER_V026.md`; B04 V01 no está aprobado ni integrado.

La corrección debe partir de los artefactos candidatos B04 V01 exactos entregados por la ejecución anterior:

```text
INPUT_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.md
EXPECTED_SHA256 = bfd15b2a3d28278b317a028e9cff0baeef8458ada5f8083f1b54cf267dd0d0ac
EXPECTED_GIT_BLOB_IF_MATERIALIZED = 9c918f6258086809068b5baadcedb9145acb0663

INPUT_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.docx
EXPECTED_SHA256 = 8abb1dc3ca1885066be8588db328121eca907447faf5959be3f1b2d89d193b8b
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT_REPORTED = 66
```

Verifica los SHA-256 antes de editar. Si alguno no coincide, detente. No reconstruyas el Word desde Markdown. Edita directamente el DOCX B04 V01 exacto.

### Objetivo exclusivo

Producir `Discussion_B04_V02` corrigiendo únicamente los defectos identificados por la revisión interna V01. El núcleo científico, cifras, cinco funciones argumentales y límites de D-133 deben permanecer iguales.

No introduzcas nueva literatura, citas, resultados, inferencias, métricas, pruebas, hipótesis ni claims.

### Corrección obligatoria 1 — no atribuir una explicación causal del ranking

La formulación V01 `why a candidate entered the ranking` / `por qué un candidato ingresó al ranking` excede lo demostrado. La evidencia permite inspeccionar el candidato/rank y la provenance o precedente histórico asociado, pero no demuestra una explicación causal o completa de por qué el recuperador produjo esa posición.

Reformula ambas versiones para expresar inspección/trazabilidad de la posición del candidato y su soporte/provenance histórico, sin lenguaje de causalidad, rationale completo ni explicación del comportamiento interno del recuperador.

### Corrección obligatoria 2 — eliminar terminología interna de implementación y QA

El texto publicable no debe contener literalmente:

```text
PROMPT_SCHEMA_SPECIFICATION_MISMATCH
advertencias_globales
```

Conserva el hallazgo científico subyacente de C36/D-133 en lenguaje reader-facing: el esquema de validación exigía un campo de advertencias globales que la instrucción de generación no solicitaba; por esa inconsistencia de especificación los 50 casos fallaron ese control automático, sin que ello equivalga a 50 explicaciones sustantivamente inválidas.

No sustituyas estos identificadores por otros nombres internos. Describe el problema, no su etiqueta de QA.

### Corrección obligatoria 3 — eliminar voz de gobernanza interna

Sustituye formulaciones como `frozen rubric` / `rúbrica congelada` por lenguaje científico de evaluación, por ejemplo `predefined evaluation rubric` / `rúbrica de evaluación predefinida` o equivalente.

Evita presentar las implicaciones como `governance requirements` del proyecto. Exprésalas como requisitos o consideraciones de diseño e implementación del sistema. Se puede conservar la idea metodológica de separación de roles/autoridad cuando sea necesaria, pero la prosa no debe sonar a decisión D-xxx, contrato editorial, bitácora de QA o especificación del repositorio.

### Corrección obligatoria 4 — naturalidad del español

El espejo español debe ser científicamente natural y semánticamente equivalente, no una traducción mecánica. Elimina anglicismos evitables de V01, especialmente:

```text
explicación downstream
accuracy de clasificación
prompt/schema
schema
 deployment operativo / deployment
```

Usa equivalentes naturales adecuados al contexto, como `explicación posterior`, `exactitud global de clasificación` únicamente dentro de la negación delimitadora, `instrucción de generación`, `esquema de validación` y `despliegue operativo`. Conserva `ranking histórico`, `Top-3`, `LLM` y otros términos técnicos ya estabilizados cuando resulten necesarios.

### Corrección obligatoria 5 — claridad KBS/SPCCR

Revisa cada oración de §6.4 para que quede claro:

```text
ENTITY/COMPONENT -> ACTION -> OBJECT/INPUT -> OUTPUT/OBSERVATION -> LIMIT
```

Evita acumulación de abstracciones, nominalizaciones, lenguaje promocional, frases vagas sobre `auditability`, y repeticiones de conceptos ya establecidos en §§6.1–6.3 que no aporten la implicación propia de §6.4.

El texto debe sonar a Discussion de un research article de KBS, no a documento de gobernanza o reporte de control interno.

### Ground truth que debe permanecer exacto

```text
RQ2_EXACT_DOCUMENTARY_ASSOCIATION = 3168/3168 candidate slots
RQ2_TOP3_MEMBERSHIP_ORDER_PRESERVED = 1056/1056 cases
RQ3_STRUCTURAL_TOP3_ORDER = 50/50 cases
RQ3_STRUCTURAL_SLOT_CONTROLS = 150/150 slots
QUALITATIVE_AUDITABILITY = 28/50 = 56.0%
MEAN_TRACEABILITY = 2.00/2
MEAN_VERIFIABILITY = 0.54/2
MEAN_HISTORICAL_NORMATIVE_SEPARATION = 1.04/2
SCHEMA_CONTROL = 0/50 solely because of the generation-instruction/validation-schema specification inconsistency
QUALITATIVE_EVALUATOR = LLM-AS-JUDGE / NOT HUMAN VALIDATION
```

No cambies denominadores, unidades, modalidad del evaluador ni fuerza epistémica.

### Límites científicos obligatorios

La V02 debe mantener inequívocamente:

```text
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
TRACEABILITY != VERIFIABILITY
TRACEABILITY != HUMAN_VALIDATION
CONFIGURABILITY != EXTERNAL_GENERALIZATION
```

No afirmar ni implicar novelty, first-ever, SOTA, superioridad, safety, hallucination reduction, causal improvement, replacement of experts, human acceptance, deployment readiness, legal validity, external generalization ni `FINAL_GAP`.

### Diferencial autorizado

Modifica exclusivamente §6.4 inglés y §6.4 español. No corrijas ahora la deuda editorial registrada de §6.2 ni ninguna otra sección.

```text
SECTIONS_1_TO_6_3 = PRESERVE
SECTION_6_4 = CORRECT_V01_TO_V02
SECTIONS_6_5_TO_6_6 = PRESERVE_PLACEHOLDERS
CONCLUSION = PRESERVE
REFERENCES = PRESERVE
END_MATTER = PRESERVE
```

### Citas, comentarios y Word

No agregues, elimines ni muevas citas. No agregues ni elimines comentarios.

```text
NEW_ENGLISH_CITATION_OCCURRENCES = 0
NEW_CITATION_COMMENTS = 0
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Preserva los 48 comentarios heredados y sus anclajes. Verifica diferencial OOXML y render completo. No reconstruyas el Word desde Markdown.

### Entregables V02

1. `article/sections/discussion/Discussion_B04_V02.md`.
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.md`.
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx`.
4. `article/responses/7_DISCUSSION_B04_SECTION6_4_RESPONSE_V02.md`.

Aplica D-022 para la response GitHub y D-027/D-035 para los masters acumulativos grandes y el DOCX exacto. No uses Base64 manual, chunking, fragmentación, reensamblado ni reconstrucción del Word.

### Checklist obligatorio de salida

La response V02 debe declarar como mínimo:

```text
PROTOCOL_READ = MWDP_V1.0
SPCCR_READ = SPCCR_V1.0
KBS_EWG_34_V01_READ = YES
D136_READ = YES
BLOCK = DISCUSSION_B04_SECTION_6_4
BLOCK_REVISION = V02
INPUT_CANDIDATE_MD_IDENTITY = PASS / BLOCKED
INPUT_CANDIDATE_DOCX_IDENTITY = PASS / BLOCKED
AUTHORIZED_CLAIMS_USED = ...
CONDITIONAL_CLAIMS_USED = ...
PROHIBITED_CLAIMS_USED = NONE
NEW_RESULTS_OR_INFERENCE = NONE
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
RETRIEVER_CAUSAL_RATIONALE_CLAIM = NONE
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
CITATION_COMMENT_COVERAGE = 48/48 / CUMULATIVE_INHERITED
COMMENTS = 48
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

Incluye SHA-256 de todos los artefactos V02, Git blob esperado del master Markdown, diferencial exacto, partes OOXML modificadas, page count y visual QA.

### Gate de salida

Detente tras completar la corrección V02.

```text
EXPECTED_EXIT = DISCUSSION_B04_V02_COMPLETED_PENDING_GESTORA_REAUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Perform only the narrow V01→V02 correction for Discussion §6.4. Preserve all authorized metrics and scientific boundaries. Remove the unsupported implication that provenance explains why the retriever ranked a candidate; remove internal diagnostic/implementation labels from publication prose while retaining the underlying specification-mismatch limitation; replace internal-governance wording with reader-facing scientific language; naturalize the Spanish mirror; and enforce KBS/SPCCR concreteness. Do not touch §6.2 or any other integrated section. Add no citations or comments. Preserve 48 comments and zero tracked changes. Stop at `DISCUSSION_B04_V02_COMPLETED_PENDING_GESTORA_REAUDIT`.
