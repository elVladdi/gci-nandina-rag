# D-152 — Discussion B02 transversal terminology-hygiene boundary

## Español

```text
DECISION = D-152
PHASE = DISCUSSION / TRANSVERSAL_EDITORIAL_CLEANUP
TARGET_SECTION = 6.2 CONTROLLED USE OF THE LLM FOR EXPLANATION
CANONICAL_MASTER = ARTICLE_MASTER_V029
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V029.md
CANONICAL_MASTER_MD_GIT_BLOB = 9d72dc684ec16cb7baef4f813b979de7127e4bc4
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = baeb1653040da74a193d2b79650873b0d24564895347bb3c22d30cdfd96f0ea3
AUTHORIZED_SCOPE = SECTION_6_2_EN_ES_TERMINOLOGY_HYGIENE_ONLY
SCIENTIFIC_REWRITE = PROHIBITED
NEW_RESULTS = PROHIBITED
NEW_INFERENCE = PROHIBITED
NEW_LITERATURE = PROHIBITED
NEW_CITATIONS = PROHIBITED
CITATION_MOVEMENT = PROHIBITED
OTHER_SECTIONS = PRESERVE
CONCLUSION = NOT_AUTHORIZED
```

### Deuda editorial exacta

La §6.2 integrada contiene prosa científicamente aceptada, pero todavía expone etiquetas de control interno incompatibles con D-136 y con una voz KBS reader-facing. La corrección autorizada debe retirar exclusivamente esas marcas internas y conservar la misma fuerza epistémica, cifras, secuencia argumental y citas.

Objetivos obligatorios:

1. sustituir `frozen auditability criterion` / `criterio congelado de auditabilidad` por lenguaje público de criterio predefinido;
2. retirar `frozen schema` / `esquema congelado` y describirlo simplemente como esquema de validación;
3. retirar el nombre interno de campo `advertencias_globales` y expresar que el esquema exigía un campo de salida que la instrucción de generación no solicitaba;
4. retirar el diagnóstico interno `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `micro-audit` / `microauditoría`, preservando la conclusión pública: el `0/50` refleja una incompatibilidad de especificación y no cincuenta explicaciones sustantivamente inválidas;
5. retirar `independent_ai_reviewer_01` y `AI_EXPERT_ROLE` y describir únicamente el hecho científicamente relevante: la evaluación cualitativa fue realizada por un LLM-as-judge, no por expertos humanos en aduanas;
6. donde mejore la naturalidad, reemplazar jerga operacional como `upstream` por formulación reader-facing equivalente, sin alterar el contrato de autoridad ni la causalidad.

### Invariantes que no pueden cambiar

```text
FIXED_TOP3_PRESERVED = 50/50 CASES
CANDIDATE_SLOT_STRUCTURAL_CHECKS = 150/150
QUALITATIVE_AUDITABILITY = 28/50 = 56.0% / 56,0%
TRACEABILITY_MEAN = 2.00/2
VERIFIABILITY_MEAN = 0.54/2
HISTORICAL_NORMATIVE_SEPARATION_MEAN = 1.04/2
SCHEMA_COMPLIANCE = 0/50 / SPECIFICATION_INCOMPATIBILITY_ONLY
QUALITATIVE_SCORING = LLM_AS_JUDGE / NOT_HUMAN_EXPERT_VALIDATION
TRACEABILITY != EXPLANATION_QUALITY_GUARANTEE
AUDITABILITY != LEGAL_CORRECTNESS
LLM_CONTROL != CAUSAL_FAITHFULNESS_GUARANTEE
```

Las citas existentes a Marra de Artiñano et al. (2023) y Kim et al. (2025) deben permanecer en los mismos pasajes sustantivos. No se autoriza añadir, eliminar o desplazar citas/comentarios.

### Requisitos técnicos

La intervención debe partir directamente del Word canónico acumulativo B06 V02, no reconstruirse desde Markdown. Deben preservarse los 48 comentarios heredados y sus anclajes, mantener 0 tracked changes y realizar auditoría diferencial OOXML y render completo. D-022, D-027 y D-035 siguen siendo vinculantes.

### Gate

```text
CURRENT_GATE = DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = CREATE_REVIEW_AND_AUTHORIZE_TRANSVERSAL_CORRECTION_PROMPT
EXPECTED_POST_CORRECTION_STATE = PENDING_GESTORA_REAUDIT
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

D-152 authorizes only a narrow bilingual terminology-hygiene correction in Section 6.2. The scientific argument, figures, evidence strength, citations, candidate-authority contract, and all other sections are frozen. The correction must remove internal QA/governance labels and replace them with reader-facing scientific wording while preserving exactly the already approved interpretation. Conclusion remains unauthorized.