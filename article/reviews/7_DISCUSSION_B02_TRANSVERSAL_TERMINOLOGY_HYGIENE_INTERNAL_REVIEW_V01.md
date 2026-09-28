# Internal review — Discussion B02 transversal terminology hygiene V01

## Español

```text
REVIEW = 7_DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_INTERNAL_REVIEW_V01
PHASE = DISCUSSION / TRANSVERSAL_EDITORIAL_CLEANUP
TARGET_SECTION = 6.2 CONTROLLED USE OF THE LLM FOR EXPLANATION
SOURCE_RESPONSE = article/responses/7_DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_RESPONSE_V01.md@5e153f75b8701a671b425e2bf3a0a4442e3bfc7b
SOURCE_SECTION = article/sections/discussion/Discussion_B02_TRANSVERSAL_V01.md@d10fdaddaabc9809b127e9c4edaa58ea5494910f
BOUNDARY = D-152
EXECUTION_AUTHORIZATION = D-153
AUDIT_GOVERNANCE = D-136 / MWDP_V1.0 / SPCCR_V1.0 / KBS_EWG_34_V01
VERDICT = PASS
MANDATORY_CORRECTIONS = NONE
AUTHOR_APPROVAL_GATE = RECOMMENDED_OPEN
```

### 1. Identidades verificadas

```text
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_TRANSVERSAL_V01.md
CANDIDATE_MD_SHA256 = ba4d3d5021a6be5fc43a435c3618c65e0778b900609b708014cb04d7866b9b7d
CANDIDATE_MD_GIT_BLOB = 2683f5933205219ed62e16418d3f9a0ace7460bd

CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_TRANSVERSAL_V01.docx
CANDIDATE_DOCX_SHA256 = 340e283924a9364447344469cf4eb077bbf93f7d32509f8f173d0a01fb3bbc0f

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B06_V02.docx
BASELINE_DOCX_SHA256 = baeb1653040da74a193d2b79650873b0d24564895347bb3c22d30cdfd96f0ea3
```

Las identidades locales de los dos candidatos coinciden exactamente con las declaradas en la response versionada. El baseline Word local coincide con la identidad canónica registrada por D-151/D-152.

### 2. Alcance diferencial

La comparación directa del DOCX candidato contra el baseline B06 V02 muestra 579 párrafos en ambos artefactos y únicamente seis párrafos modificados: tres en §6.2 inglés y sus tres espejos en §6.2 español. No se detectaron cambios en ninguna otra sección ni en Conclusion.

Los cambios son exactamente los autorizados por D-152:

1. `upstream result` / `resultado upstream` se reemplaza por formulación reader-facing referida a la etapa previa de ranking;
2. `frozen auditability criterion` / `criterio congelado` se reemplaza por `predefined` / `predefinido`;
3. se retiran `frozen schema`, `advertencias_globales`, `micro-audit`/`microauditoría` y `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`, preservando el significado público de incompatibilidad de especificación;
4. se retiran `independent_ai_reviewer_01` y `AI_EXPERT_ROLE`, manteniendo únicamente `LLM-as-judge` frente a expertos humanos en aduanas.

No aparecen en §6.2 candidata las etiquetas internas objetivo de D-152: `frozen`, `advertencias_globales`, `micro-audit`, `microauditoría`, `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`, `independent_ai_reviewer_01`, `AI_EXPERT_ROLE` ni `upstream`.

### 3. Fidelidad científica y epistemológica

La corrección conserva sin alteración material:

```text
FIXED_TOP3_PRESERVED = 50/50
CANDIDATE_SLOT_STRUCTURAL_CHECKS = 150/150
QUALITATIVE_AUDITABILITY = 28/50 = 56.0% / 56,0%
VERIFIABILITY_MEAN = 0.54/2 / 0,54/2
HISTORICAL_NORMATIVE_SEPARATION_MEAN = 1.04/2 / 1,04/2
SCHEMA_COMPLIANCE = 0/50 / SPECIFICATION_INCOMPATIBILITY_ONLY
QUALITATIVE_SCORING = LLM_AS_JUDGE / NOT_HUMAN_CUSTOMS_EXPERT_VALIDATION
TRACEABILITY != EXPLANATION_QUALITY_GUARANTEE
AUDITABILITY != LEGAL_CORRECTNESS
LLM_CONTROL != CAUSAL_FAITHFULNESS_GUARANTEE
```

Las citas de Marra de Artiñano et al. (2023) y Kim et al. (2025) permanecen en los mismos pasajes sustantivos. No se introdujo literatura, resultados, cálculos, inferencia, causalidad, generalización, legal correctness, human validation, deployment readiness ni novelty.

La secuencia argumental de §6.2 también se conserva: rol restringido del LLM → comparación funcional con LLMs con autoridad clasificadora → preservación estructural → límite entre trazabilidad y calidad → incompatibilidad de especificación y modalidad LLM-as-judge.

### 4. Calidad editorial D-136 / KBS / SPCCR

```text
SCIENTIFIC_FIDELITY = PASS
EPISTEMIC_STRENGTH = PASS / UNCHANGED_AND_BOUNDED
INTERNAL_TERMINOLOGY_HYGIENE = PASS
READER_FACING_PROSE = PASS
AGENT_ACTION_OBJECT_CLARITY = PASS
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
NOMINALIZATION_OVERLOAD = ABSENT
KBS_CONCRETE_PROSE = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
```

La frase inglesa `the present LLM receives a result from the preceding ranking stage` y el espejo español `recibe un resultado de la etapa previa de ranking` preservan el contrato de autoridad sin introducir causalidad. La reformulación del `0/50` atribuye correctamente el fallo a una incompatibilidad entre esquema de validación e instrucción de generación sin convertirlo en medida de calidad de explicación. La modalidad de evaluación queda expuesta en términos científicos públicos como LLM-as-judge y no como identificador interno del evaluador.

### 5. Equivalencia Markdown / DOCX

Los cinco párrafos de cuerpo más el heading de §6.2 inglés y los cinco párrafos de cuerpo más el heading de §6.2 español coinciden textualmente entre el Markdown acumulativo candidato y el DOCX acumulativo candidato, salvo la sintaxis Markdown `##` del heading. El cuerpo inglés contiene 438 palabras.

### 6. Integridad OOXML y comentarios

```text
BASELINE_OOXML_PARTS = 14
CANDIDATE_OOXML_PARTS = 14
OOXML_CHANGED_PARTS = word/document.xml ONLY
COMMENTS_XML = BYTE_IDENTICAL
COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
TRACKED_INSERTIONS = 0
TRACKED_DELETIONS = 0
```

No se añadieron, eliminaron ni movieron comentarios. No existen tracked changes.

### 7. Render diferencial

Ambos DOCX renderizan 69 páginas. La comparación pixel a pixel identifica solo las páginas 29, 30 y 64 como visualmente modificadas; las otras 66 páginas son pixel-identical al baseline. Las tres páginas modificadas fueron inspeccionadas a tamaño completo y no presentan clipping, solapamientos, glifos faltantes, roturas de párrafo ni desplazamientos de encabezado/pie.

```text
FULL_RENDER = PASS
PAGE_COUNT = 69
PIXEL_IDENTICAL_UNCHANGED_PAGES = 66
VISUALLY_CHANGED_PAGES = 29 / 30 / 64
LAYOUT_DEFECTS = NONE
```

### 8. Veredicto

La ejecución cumple D-152 y D-153 de forma estrecha y exacta. La deuda terminológica heredada de §6.2 queda resuelta en el candidato sin reabrir el núcleo científico, los resultados ni las citas. Bajo D-136, la corrección obtiene `PASS` sin correcciones obligatorias.

```text
DISCUSSION_B02_TRANSVERSAL_V01_REAUDIT = PASS
MANDATORY_CORRECTIONS = NONE
SCIENTIFIC_CORE = PASS / UNCHANGED
EDITORIAL_TERMINOLOGY_HYGIENE = PASS
TECHNICAL_INTEGRITY = PASS
AUTHOR_APPROVAL_GATE = OPEN_RECOMMENDED
CONCLUSION = NOT_AUTHORIZED_PENDING_AUTHOR_APPROVAL_AND_PROMOTION
```

---

## English

The Section 6.2 transversal terminology-hygiene candidate passes independent substantive/editorial and technical re-audit. Exactly six paragraphs changed relative to the B06 V02 Word baseline, all within Section 6.2 EN/ES and all within the D-152 boundary. Scientific claims, figures, citations, authority boundaries and inferential limits are unchanged. Markdown/DOCX Section 6.2 body text is exact, only `word/document.xml` changed, 48 comments and anchors are preserved, tracked changes remain zero, and the 69-page render passes with only pages 29, 30 and 64 visually changed. Verdict: `PASS`; no mandatory corrections.