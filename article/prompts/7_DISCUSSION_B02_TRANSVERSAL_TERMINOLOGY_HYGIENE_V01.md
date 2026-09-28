# Prompt — Discussion B02 transversal terminology hygiene V01

## Español

### Rol y alcance

Actúa exclusivamente como IA de Redacción. Ejecuta una corrección editorial transversal y estrecha sobre Discussion §6.2 en inglés y español. No reescribas su núcleo científico, no modifiques ninguna otra sección y no redactes Conclusion.

### Onboarding obligatorio

Antes de modificar artefactos, lee íntegramente y aplica, en este orden:

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
12. `article/governance/KBS_EMPIRICAL_WRITING_GUIDE_34_ARTICLES_DRAFT.md`.
13. `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`.
14. `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`.
15. `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`.
16. `article/governance/D136_SUBSTANTIVE_EDITORIAL_AUDIT_AND_INTERNAL_TERMINOLOGY_CONTROL.md`.
17. `article/governance/D149_DISCUSSION_B06_V02_REAUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md`.
18. `article/governance/D150_DISCUSSION_B06_V02_AUTHOR_APPROVAL_AND_V029_PROMOTION_GATE.md`.
19. `article/governance/D151_DISCUSSION_B06_V029_VERIFICATION_INTEGRATION_AND_DISCUSSION_CLOSURE.md`.
20. `article/governance/D152_DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_BOUNDARY.md`.
21. La revisión interna vigente de este prompt.
22. La autorización vigente que apunte expresamente a este prompt.
23. Este prompt completo.
24. `article/manuscript/ARTICLE_MASTER_V029.md` como único baseline Markdown canónico.

No uses una conversación anterior como fuente de verdad. Si el estado vivo contradice este prompt, si la autorización no apunta a este prompt, o si falta el Word baseline exacto, detente y registra el bloqueo en la response versionada.

### Preflight obligatorio

La response debe registrar como mínimo:

```text
ARCHIVOS_LEIDOS = ...
FASE_ACTIVA = DISCUSSION / TRANSVERSAL_EDITORIAL_CLEANUP
ESTADO_DEL_BLOQUE = SECTION_6_2_INTEGRATED_WITH_LOGGED_EDITORIAL_DEBT
CORRECCION_AUTORIZADA = YES / SECTION_6_2_EN_ES_ONLY
FUENTES_EXTERNAS_QUE_DEBEN_VERIFICARSE = NONE
BLOQUEOS_O_CONTRADICCIONES = NONE / ...
```

### Baselines exactos

Markdown canónico:

```text
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V029.md
EXPECTED_SHA256 = f10f8c74396c570f4e65ec3ff9fe176a4b8df9aea31c1349eb6472bd552c5b80
EXPECTED_GIT_BLOB = 9d72dc684ec16cb7baef4f813b979de7127e4bc4
```

Word canónico acumulativo bajo custodia del autor:

```text
INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V02.docx
EXPECTED_SHA256 = baeb1653040da74a193d2b79650873b0d24564895347bb3c22d30cdfd96f0ea3
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 69
```

Verifica ambas identidades antes de editar. Si no coinciden, detente. Edita directamente el DOCX exacto; **no reconstruyas Word desde Markdown**.

### Scope diferencial autorizado

```text
SECTION_6_2_EN = NARROW_TERMINOLOGY_HYGIENE_ONLY
SECTION_6_2_ES = NARROW_TERMINOLOGY_HYGIENE_ONLY
SECTIONS_1_TO_6_1 = PRESERVE
SECTIONS_6_3_TO_6_6 = PRESERVE
CONCLUSION = PRESERVE_PLACEHOLDER
REFERENCES = PRESERVE
END_MATTER = PRESERVE
NEW_RESULTS = NONE
NEW_INFERENCE = NONE
NEW_LITERATURE = NONE
NEW_CITATIONS = NONE
```

### Correcciones obligatorias

Corrige exclusivamente las marcas internas identificadas por D-152:

1. reemplaza `frozen auditability criterion` / `criterio congelado de auditabilidad` por lenguaje científico público de criterio predefinido;
2. reemplaza `frozen schema` / `esquema congelado` por `validation schema` / `esquema de validación` o equivalente natural;
3. elimina el nombre interno de campo `advertencias_globales`; conserva solo que el esquema exigía un campo de salida que la instrucción de generación no solicitaba;
4. elimina `micro-audit` / `microauditoría` y el diagnóstico `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`; conserva que `0/50` se debió a una incompatibilidad entre instrucción de generación y esquema de validación y no debe interpretarse como cincuenta explicaciones sustantivamente inválidas;
5. elimina `independent_ai_reviewer_01` y `AI_EXPERT_ROLE`; conserva que la puntuación cualitativa fue realizada por un LLM-as-judge y no por expertos humanos en aduanas;
6. naturaliza jerga operacional como `upstream` cuando aparezca en la zona corregida, usando una expresión reader-facing equivalente como `preceding ranking stage` / `etapa previa de ranking`, sin alterar el contrato de autoridad.

No conviertas esta tarea en una reescritura estilística amplia. El objetivo es únicamente higiene terminológica y naturalidad local.

### Invariantes científicas obligatorias

Preserva exactamente las siguientes cifras y relaciones:

```text
FIXED_TOP3_AND_ORDER_PRESERVED = 50/50 CASES
STRUCTURAL_SLOT_CHECKS = 150/150 CANDIDATE SLOTS
QUALITATIVE_AUDITABILITY = 28/50 = 56.0% / 56,0%
TRACEABILITY_MEAN = 2.00/2
VERIFIABILITY_MEAN = 0.54/2
HISTORICAL_NORMATIVE_SEPARATION_MEAN = 1.04/2
SCHEMA_COMPLIANCE = 0/50 / SPECIFICATION_INCOMPATIBILITY_ONLY
QUALITATIVE_SCORING = LLM_AS_JUDGE / NOT_HUMAN_CUSTOMS_EXPERTS
LLM_HAS_NO_AUTHORITY_TO_CHANGE_TOP3 = TRUE
LLM_OUTPUT_DOES_NOT_FEED_BACK_INTO_CLASSIFICATION = TRUE
TRACEABILITY != EXPLANATION_QUALITY_GUARANTEE
AUDITABILITY != LEGAL_CORRECTNESS
LLM_CONTROL != CAUSAL_FAITHFULNESS_GUARANTEE
```

Mantén las citas existentes de §6.2 y su soporte sustantivo. No agregues, elimines ni muevas citas o comentarios. No introduzcas novelty, SOTA, superioridad, legal correctness, human validation, deployment readiness, external generalization, causalidad nueva ni claims nuevos.

### Control D-136 / KBS / SPCCR

La salida debe cumplir:

```text
SCIENTIFIC_FIDELITY = PASS
EPISTEMIC_STRENGTH = UNCHANGED / BOUNDED
INTERNAL_TERMINOLOGY_LEAKAGE_IN_6_2 = NONE
READER_FACING_PROSE = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_CONCRETE_PROSE = PASS
```

### Word, comentarios y control diferencial

No agregues, elimines ni muevas comentarios. Preserva sus anclajes.

```text
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
NEW_ENGLISH_CITATION_OCCURRENCES = 0
NEW_CITATION_COMMENTS = 0
```

Realiza auditoría diferencial Markdown y OOXML. Solo deben cambiar los párrafos estrictamente necesarios de §6.2 EN/ES y, en OOXML, idealmente solo `word/document.xml`. Renderiza el DOCX completo y revisa las páginas afectadas.

D-035: no usar Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. D-027: entrega el DOCX exacto al autor como artefacto adjunto. D-022: versiona primero la response en GitHub.

### Entregables

1. `article/sections/discussion/Discussion_B02_TRANSVERSAL_V01.md`.
2. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_TRANSVERSAL_V01.md`.
3. `ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_TRANSVERSAL_V01.docx`.
4. `article/responses/7_DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_RESPONSE_V01.md`.

### Checklist de salida

La response debe declarar al menos:

```text
PROTOCOL_READ = MWDP_V1.0
SPCCR_READ = SPCCR_V1.0
KBS_EWG_34_V01_READ = YES
D136_READ = YES
ONBOARDING = PASS / BLOCKED
INPUT_MASTER_MD_IDENTITY = PASS / BLOCKED
INPUT_MASTER_DOCX_IDENTITY = PASS / BLOCKED
SECTION_6_2_MODIFIED = YES / NARROW_TERMINOLOGY_HYGIENE_ONLY
OTHER_SECTIONS_MODIFIED = NO
CONCLUSION_MODIFIED = NO
NEW_RESULTS_OR_INFERENCE = NONE
NEW_LITERATURE = NONE
NEW_ENGLISH_CITATION_OCCURRENCES = 0
INTERNAL_TERMINOLOGY_LEAKAGE_IN_6_2 = NONE
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
COMMENTS = 48
TRACKED_CHANGES = 0
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
```

### Gate de salida

Detente después de producir esta corrección transversal.

```text
EXPECTED_EXIT = DISCUSSION_B02_TRANSVERSAL_V01_COMPLETED_PENDING_GESTORA_REAUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Correct only Section 6.2 EN/ES in the exact V029 cumulative Markdown and B06 V02 Word baselines. Remove internal QA/governance identifiers and replace them with reader-facing wording without changing any result, inference, citation, scientific relationship, or other manuscript section. Stop at `DISCUSSION_B02_TRANSVERSAL_V01_COMPLETED_PENDING_GESTORA_REAUDIT`.