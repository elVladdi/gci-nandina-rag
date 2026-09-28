# Internal review — Discussion B04 / Section 6.4 — V01

## Español

```text
REVIEW = 7_DISCUSSION_B04_SECTION6_4_INTERNAL_REVIEW_V01
PHASE = DISCUSSION
BLOCK = DISCUSSION_B04_SECTION_6_4
BLOCK_REVISION = V01
SECTION_ARTIFACT = article/sections/discussion/Discussion_B04_V01.md@3f8749234d3535fb7ccdf8d1546295160c64e3d0
SECTION_ARTIFACT_GIT_BLOB = 8f27bbce34e437ecb512195a393156e09331ee4f
EXECUTION_RESPONSE = article/responses/7_DISCUSSION_B04_SECTION6_4_RESPONSE_V01.md@e27f03b3d4103a3436fe26566a97a22c974ce57c
BOUNDARY = D-133
EXECUTION_AUTHORIZATION = D-135
AUDIT_STANDARD = MWDP_V1.0 + SPCCR_V1.0 + KBS_EWG_34_V01 + D-136
VERDICT = PASS WITH CORRECTIONS
MANDATORY_CORRECTIONS = YES
AUTHOR_APPROVAL_GATE = NOT_OPEN
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Alcance de la auditoría

La revisión no se limita a hashes, commits, diferencial u OOXML. Se inspeccionó el texto real de §6.4 contra D-133, la matriz claim–evidence, Discussion §§6.1–6.3, `STYLE_GUIDE.md`, `SPCCR_V1.0` y `KBS_EWG_34_V01`.

La response de IA Redacción declara identidades de baseline correctas, diferencial restringido a §6.4, 48 comentarios heredados, 0 tracked changes y render completo. Esos controles quedan registrados como evidencia operacional declarada, pero el DOCX candidato binario no está disponible en la sesión actual de IA Gestora para una auditoría independiente. Dado que el texto ya requiere corrección sustantiva/editorial, no corresponde abrir el gate autoral ni realizar promoción antes de una V02 corregida.

```text
TECHNICAL_EXECUTION_REPORT = CONSISTENT / DECLARED
INDEPENDENT_DOCX_BINARY_AUDIT = DEFERRED_UNTIL_CORRECTED_V02
TEXTUAL_SCIENTIFIC_EDITORIAL_AUDIT = COMPLETED
```

## 2. Fidelidad científica y anti-overclaiming

El núcleo científico es correcto. Se preservan los datos autorizados: 3,168/3,168 slots, 1,056/1,056 casos, 50/50 casos, 150/150 slots, 28/50 = 56.0%, trazabilidad 2.00/2, verificabilidad 0.54/2 y separación historical–normative 1.04/2. El texto mantiene explícitamente que estos resultados no demuestran classification accuracy, substantive normative correctness, legal correctness, human validation, deployment readiness, causal safety, hallucination reduction ni external generalization.

No se detectaron resultados nuevos, nueva literatura, nuevas citas, CI, p-values, tests, novelty, SOTA ni superioridad global.

Sin embargo, la frase inglesa `why a candidate entered the ranking` y su espejo español `por qué un candidato ingresó al ranking` atribuyen a la inspectabilidad una capacidad explicativa más fuerte que la evidencia disponible. El sistema permite inspeccionar la posición/candidato y su provenance/precedente asociado, pero no se evaluó una explicación causal o completa de por qué el recuperador produjo esa posición. Debe reformularse de manera no causal y trazable.

```text
NUMERICAL_GROUND_TRUTH = PASS
PROHIBITED_SCIENTIFIC_CLAIMS = NONE
NEW_RESULTS_OR_INFERENCE = NONE
RETRIEVER_RATIONALE_OVERSTATEMENT = CORRECTION_REQUIRED
```

## 3. Coherencia argumental y función de Discussion

La secuencia de cinco párrafos es funcionalmente adecuada para §6.4: separación de roles → provenance a nivel de candidato → insuficiencia de la trazabilidad → implicaciones de diseño → límites de uso. Es coherente con §§6.1–6.3 y no contradice la arquitectura congelada.

La sección, no obstante, debe evitar repetir la voz de gobernanza interna del proyecto. `frozen rubric` y `engineering and governance requirements` son comprensibles en artefactos de control, pero en el artículo deben expresarse como `predefined evaluation rubric` y `design and implementation requirements` o equivalentes, manteniendo el significado científico sin exponer el proceso editorial interno.

```text
SECTION_FUNCTION = PASS
ARGUMENT_SEQUENCE = PASS
CROSS_SECTION_COHERENCE = PASS
INTERNAL_GOVERNANCE_VOICE = CORRECTION_REQUIRED
```

## 4. Terminología interna y adecuación KBS

Se detecta filtración directa de identificadores de implementación/QA al texto publicable:

- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`;
- `advertencias_globales` como nombre literal de campo interno.

La limitación científica subyacente sí debe permanecer, porque C36/D-133 la autorizan. Lo que debe desaparecer es el identificador interno. La formulación reader-facing debe explicar que el esquema de validación exigía un campo de advertencias globales que la instrucción de generación no solicitaba, por lo que los 50 casos fallaron ese control automático por una inconsistencia entre la especificación de generación y el esquema de validación, no por invalidez sustantiva de las explicaciones.

Esto sigue exactamente el principio de `KBS_EWG_34_V01`: el manuscrito debe explicar objetos, operaciones, condiciones y resultados, y no sonar como bitácora de QA, documento de gobernanza o especificación contractual interna.

```text
INTERNAL_DIAGNOSTIC_CODE_LEAKAGE = FAIL / CORRECTION_REQUIRED
INTERNAL_IMPLEMENTATION_FIELD_LEAKAGE = FAIL / CORRECTION_REQUIRED
SCIENTIFIC_LIMITATION_TO_PRESERVE = YES
KBS_READER_FACING_LANGUAGE = REVISION_REQUIRED
```

## 5. Claridad, abstracción y naturalidad bilingüe

La estructura agente–acción–objeto es en general explícita y no existe una acumulación severa de nominalizaciones. El bloque no falla por abstracción global, pero sí contiene expresiones que vuelven la prosa más contractual/interna de lo necesario.

En español hay anglicismos evitables que deben naturalizarse sin alterar terminología científica gobernada: `explicación downstream`, `accuracy de clasificación`, `prompt/schema` y `deployment operativo`. Deben reemplazarse por equivalentes científicos naturales, por ejemplo `explicación posterior`, `exactitud global de clasificación` solo en la negación delimitadora correspondiente, `instrucción de generación/esquema de validación` y `despliegue operativo`. `ranking histórico`, `Top-3` y `LLM` pueden conservarse por ser terminología técnica estable del manuscrito.

```text
ABSTRACTION_DENSITY = ACCEPTABLE_WITH_LOCAL_CORRECTIONS
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
SPANISH_NATURALNESS = CORRECTION_REQUIRED
EN_ES_EPISTEMIC_EQUIVALENCE = PASS / MUST_BE_PRESERVED_IN_V02
```

## 6. Deuda editorial heredada

Durante la comprobación transversal se observó que §6.2 ya integrado conserva etiquetas internas como `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`, `advertencias_globales`, `independent_ai_reviewer_01`, `AI_EXPERT_ROLE` y términos de QA como `micro-audit`. D-136 prohíbe corregir silenciosamente contenido previamente aprobado. Se registra por tanto una deuda editorial para un gate transversal posterior, antes del cierre final del manuscrito.

```text
LEGACY_EDITORIAL_DEBT = DISCUSSION_B02_INTERNAL_TERMINOLOGY_HYGIENE
IMMEDIATE_SILENT_EDIT = PROHIBITED
REQUIRED_BEFORE_FINAL_MANUSCRIPT_FREEZE = YES / CONTROLLED_TRANSVERSAL_GATE
```

## 7. Correcciones obligatorias para B04 V02

La V02 debe ser estrecha: mantener exactamente el mismo ground truth, estructura argumental y ausencia de nuevas citas, modificando únicamente §6.4 en inglés/español para (a) eliminar la sobreinterpretación `why a candidate entered the ranking`; (b) sustituir códigos/campos internos por lenguaje científico reader-facing; (c) eliminar voz de gobernanza interna; (d) naturalizar el español; y (e) preservar explícitamente todos los límites científicos de D-133.

No se autoriza modificar §§1–6.3, §§6.5–6.6, Conclusion, referencias ni end matter.

## 8. Disposición

```text
DISCUSSION_B04_V01_AUDIT = PASS_WITH_CORRECTIONS
SCIENTIFIC_CORE = PASS
EDITORIAL_TERMINOLOGY_HYGIENE = REVISION_REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_REDACCION_AFTER_CORRECTION_PROMPT_AUTHORIZATION
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

Discussion B04 V01 preserves the authorized numerical ground truth and the principal scientific boundaries, and it introduces no new literature, results, inference, novelty, superiority, legal-correctness, human-validation, safety, deployment, or external-generalization claim. Its scientific core therefore passes.

The block nevertheless requires a narrow editorial/scientific-precision revision before author review. The wording `why a candidate entered the ranking` overstates what provenance inspection demonstrates; it must not imply a causal or complete explanation of the retrieval decision. Publication prose also leaks the internal diagnostic label `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` and the implementation field name `advertencias_globales`, and uses internal-governance wording such as `frozen rubric`. These must be replaced with reader-facing descriptions while preserving the underlying specification-mismatch limitation. The Spanish mirror additionally requires removal of avoidable Anglicisms.

```text
VERDICT = PASS WITH CORRECTIONS
SCIENTIFIC_CORE = PASS
INTERNAL_TERMINOLOGY_LEAKAGE = CORRECTION_REQUIRED
RETRIEVER_RATIONALE_OVERSTATEMENT = CORRECTION_REQUIRED
SPANISH_NATURALNESS = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
```
