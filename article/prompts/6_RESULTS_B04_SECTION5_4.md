# Prompt — Results B04 / Section 5.4 Controlled explanation quality

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente Results B04 / Section 5.4 — **Controlled explanation quality** sobre el master acumulativo canónico. No avances a Section 5.5 ni a ninguna sección posterior.

Este prompt opera bajo MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, D-103 y D-104. `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` y `STYLE_GUIDE.md` permanecen vinculantes.

### 1. Baselines exactos obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V019.md
BASELINE_MD_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
BASELINE_MD_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx
BASELINE_DOCX_SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Verifica ambas identidades antes de editar. Si alguna no coincide, detente con `BLOCKED_BASELINE_IDENTITY_MISMATCH`.

No reconstruyas el DOCX desde Markdown. Edita directamente el binario Word exacto B03 V01 y preserva comentarios, anchors, estilos, tablas, captions y OOXML heredado.

### 2. Snapshot y fuentes experimentales obligatorias

Usa únicamente:

```text
EXPERIMENTAL_REPOSITORY = elVladdi/gci-nandina-rag
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
HE4_DIRECTORY = outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2
CASES = 50
CANDIDATE_SLOTS = 150
```

Reconsulta directamente:

```text
he4_automatic_validation_metrics_v0.2.json
GIT_BLOB = a8adfe08da2b6b0052205fdb8650d9c86e8c5b82

he4_qualitative_metrics_v0.2.json
GIT_BLOB = 843e1edd17a023f6c3d6f0b5235dd3fba86369c1

he4_qualitative_findings_v0.2.md
GIT_BLOB = 4b9dd1b3079235b2c54d5777fc788f0e98b27e32

he4_he4_joint_jk_assessment_v0.2.json
GIT_BLOB = b617b4f397d0ffb4f8882ddda06790b1c539543e

he4_top3_invariance_v0.2.json
GIT_BLOB = 8ddc1703fb267e28b4301c13602f62b494846921

he4_traceability_validation_v0.2.json
GIT_BLOB = 580214070ac4c9aac1f10e4452614bc41b39d9a0

he4_label_leakage_audit_v0.2.json
GIT_BLOB = 2d078f7742806a95ab7f4004c1c140287510e8b4

gate_j_interpretation_v0.2.json
GIT_BLOB = 652610251f09ba841e7eff7598b399b8b745eec2

gate_k_qualitative_evaluation_manifest_v0.2.json
GIT_BLOB = 28963380bdcc22932d08591a709059f6fa00263b
```

No sustituyas estas fuentes por resultados históricos, archivos mutables, literatura, memoria ni inferencia propia.

### 3. Función científica de §5.4

Section 5.4 debe responder RQ3 con los resultados de la **explicación controlada del Top-3 fijo**. La subsección debe separar explícitamente:

1. **controles automáticos/estructurales** del artefacto generado;
2. **evaluación cualitativa** bajo la rúbrica congelada;
3. **limitaciones del protocolo ejecutado**, especialmente el mismatch prompt-schema y la modalidad AI del evaluador.

No presentes la etapa generativa como clasificador. El Top-3 se fijó upstream y la evaluación de §5.4 no reabre RQ1 ni RQ2.

### 4. Claims autorizados

```text
C35 = AUTHORIZED
C36 = AUTHORIZED
C37 = AUTHORIZED
C38 = AUTHORIZED
C39 = AUTHORIZED
C40 = AUTHORIZED
C41 = AUTHORIZED

C13 = PROHIBITED
C14 = CONDITIONAL / DO NOT USE AS AN UNBOUNDED UMBRELLA CLAIM
C18 = PROHIBITED
```

Usa los claims específicos C35–C41. No conviertas C14 en una afirmación más amplia que los resultados cuantificados.

### 5. Capa automática/estructural

Reporta de manera compacta que en los 50 casos:

```text
TOP3_ORDER_PRESERVATION = 50/50 = 100%
CANDIDATE_SET_CLOSURE = 50/50 = 100%
RANK_CONSISTENCY = 50/50 = 100%
TRACEABILITY_COMPLETENESS = 50/50 = 100%
HISTORICAL_REFERENCE_VALIDITY = 50/50 = 100%
NORMATIVE_REFERENCE_VALIDITY = 50/50 = 100%
COMPARISON_PRESENCE = 50/50 = 100%
EXPLICIT_LABEL_LEAKAGE_FREE = 50/50 = 100%
RAW_JSON_PARSE = 50/50 = 100%

SLOT_CANDIDATE_CODE_VALID = 150/150 = 100%
SLOT_HISTORICAL_REFERENCE_VALID = 150/150 = 100%
SLOT_NORMATIVE_REFERENCE_VALID = 150/150 = 100%
SLOT_RANK_CONSISTENT = 150/150 = 100%
```

No es necesario enumerar todos los controles redundantes si una redacción más compacta preserva el objeto medido.

**Prohibición crítica:**

```text
AUTOMATIC_VALIDATION_PASS = NOT_APPLICABLE
```

No inventes una tasa binaria global automática de 50/50. La fuente declara expresamente que no existía una regla per-case PASS/FAIL pre-generation en el schema/validator congelado.

### 6. Prompt-schema mismatch

Debe informarse el límite técnico de forma factual:

```text
SCHEMA_COMPLIANCE = 0/50
REQUIRED_FIELDS_COMPLETENESS = 0/50
CLASSIFICATION = PROMPT_SCHEMA_SPECIFICATION_MISMATCH
```

El schema v0.2 exigía `advertencias_globales`, pero el prompt v0.2 no incluía ese campo en la estructura exacta de salida. La microauditoría congelada establece que los 50 casos fallaban únicamente por ese campo y que no hubo otros schema errors.

Por tanto, no escribas:

- “all explanations failed automatic validation”;
- “0% explanation quality”;
- “0% structural validity”;
- ni ningún equivalente.

Puedes indicar que el resultado 0/50 de schema compliance quedó confounded por la incompatibilidad prompt-schema y debe interpretarse como limitación de especificación.

### 7. Evaluación cualitativa

Reporta:

```text
AUDITABLE_CASES = 28/50 = 56.0%
NON_AUDITABLE_CASES = 22/50 = 44.0%
TOTAL_SCORE_MEAN = 11.72/16
TOTAL_SCORE_MEDIAN = 12/16
TOTAL_SCORE_RANGE = 6–15
HARD_VIOLATIONS = 0/50
```

El criterio congelado de caso auditable fue `total >= 12/16 AND no hard violation`.

Los ocho promedios 0–2 autorizados son:

```text
TRACEABILITY = 2.00
VERIFIABILITY = 0.54
HISTORICAL_NORMATIVE_SEPARATION = 1.04
CONCLUSION_PRUDENCE = 1.78
FIXED_TOP3_CONSISTENCY = 1.96
GENERIC_NORMATIVE_EVIDENCE_DETECTION = 1.68
CANDIDATE_COMPARISON = 1.46
UTILITY_FOR_HUMAN_AUDIT = 1.26
```

La subsección debe mostrar el perfil, no solo los valores altos. En particular, **verificability = 0.54** y **historical/normative separation = 1.04** son resultados sustantivos del perfil y no deben omitirse si se reportan las fortalezas de trazabilidad o consistencia.

Puede utilizarse **una tabla compacta** con las ocho dimensiones si mejora la legibilidad. Si se utiliza, deriva su número de la secuencia real del master y evita duplicar en prosa todos los valores.

### 8. Control de advertencia normativa genérica

Puede reportarse de forma breve:

```text
GENERIC_NORMATIVE_WARNING_CONTROL = 41/50
MISSING_GENERIC_NORMATIVE_WARNING = 9/50

MISSING_GROUP_AUDITABLE = 1/9 = 11.1%
MISSING_GROUP_MEAN_TOTAL = 9.67
OTHER_CASES_AUDITABLE = 27/41 = 65.9%
OTHER_CASES_MEAN_TOTAL = 12.17
```

Esta comparación es descriptiva. No atribuyas causalidad, significancia ni efecto estimado de la advertencia.

### 9. Modalidad real del evaluador

Debe aparecer explícitamente, no como nota oculta:

```text
EVALUATOR_IDENTIFIER = independent_ai_reviewer_01
EVALUATOR_MODALITY = AI_EXPERT_ROLE
LLM_AS_JUDGE = TRUE
HUMAN_SCORING = FALSE
METHODOLOGICAL_DEVIATION = EVALUATOR_MODALITY_DEVIATION
```

Durante esa puntuación:

```text
GROUND_TRUTH_EXPOSED = FALSE
REFERENCE_RANK_EXPOSED = FALSE
BUCKET_EXPOSED = FALSE
EXTERNAL_EVIDENCE_USED = FALSE
WEB_USED = FALSE
RETRIEVAL_USED = FALSE
```

No escribas `human expert review`, `expert-validated`, `validated by customs experts` ni equivalentes. La utilidad para auditoría humana es **una dimensión de la rúbrica puntuada por un AI evaluator**, no una evaluación realizada por humanos.

### 10. Control de etiqueta en la generación

El audit congelado registra:

```text
LABEL_EXPOSED_TO_LLM = FALSE
LABEL_USED_FOR_CONTEXT = FALSE
LABEL_USED_FOR_EVIDENCE = FALSE
LABEL_USED_FOR_TOP3 = FALSE
LABEL_USED_FOR_SAMPLE_DESIGN = TRUE
```

Si se incluye, debe quedar claro que se trata de un control específico de la generación/muestra; no una declaración de ausencia total de leakage ni de independencia estadística.

### 11. Síntesis permitida

La evaluación experimental conjunta registra `PARTIALLY SUPPORTED`. En el manuscrito evita abrir o cerrar con el identificador interno `HE4`. Traduce el resultado a una síntesis funcional, por ejemplo: los controles estructurales de preservación y trazabilidad se cumplieron en los 50 casos, mientras que 28/50 alcanzaron el criterio cualitativo de auditabilidad y el perfil mostró debilidades en verificabilidad y separación de evidencia.

Esa síntesis debe mantener simultáneamente:

- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`;
- `EVALUATOR_MODALITY_DEVIATION`;
- 56% auditable bajo la rúbrica ejecutada;
- 0 hard violations;
- ausencia de equivalencia con legal correctness.

### 12. Qué NO pertenece a B04

No incluir:

- resultados de retrieval RQ1 ya reportados en §5.2;
- resultados de documentary coverage RQ2 ya reportados en §5.3 salvo referencia mínima de contexto;
- inferencia HE2, bootstrap, CI o p-values;
- EXP11A, EXP11B, Attempt06 o EXP12;
- HE5;
- literatura o comparación cross-study;
- Discussion;
- `FINAL_GAP` o `NOVELTY`;
- legal/substantive normative correctness;
- overall classification accuracy;
- generalización empírica fuera de Chapter 87;
- faithful causal explanation del ranking upstream;
- human validation.

### 13. Forma recomendada

Redacta §5.4 como resultados, no como repetición de Methods:

1. abre con los controles estructurales observados;
2. presenta de inmediato el mismatch prompt-schema para evitar una lectura engañosa del 0/50 de schema compliance;
3. presenta el resultado cualitativo 28/50 y el perfil dimensional;
4. cierra con la modalidad real del evaluador y una interpretación estrictamente acotada.

Evita abstracciones como `high-quality explanations`, `successful explanations`, `robust auditability`, `validated reasoning` si no se anclan directamente a una métrica concreta. Prefiere objetos medidos: Top-3 preservation, reference validity, traceability, auditable-case criterion, rubric dimension scores.

En el espejo español usa redacción natural; traduce `Section` como `Sección`. Puede conservarse `Top-3`, `LLM-as-judge` solo si mejora precisión, pero no abuses de calcos.

### 14. Alcance diferencial acumulativo

Solo sustituye el placeholder de Section 5.4 en Part I y Part II.

```text
SECTIONS_1_TO_5_3 = PRESERVE
SECTION_5_4 = DRAFT_THIS_BLOCK_ONLY
SECTIONS_5_5_TO_5_7 = PRESERVE_PLACEHOLDERS
DISCUSSION = PRESERVE_PLACEHOLDERS
CONCLUSION = PRESERVE_PLACEHOLDERS
END_MATTER = PRESERVE
NO_NEW_LITERATURE = TRUE
NO_SCOPE_EXPANSION = TRUE
```

### 15. D-035 — entrega timeout-safe

```text
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
REAL_FILE_HANDOFF_MD_DOCX_TO_AUTHOR = REQUIRED
```

Versiona en GitHub solo el artefacto pequeño de sección y la response. Entrega el MD acumulativo y DOCX acumulativo como archivos reales al autor.

### 16. Artefactos obligatorios

Genera exactamente:

1. `article/sections/results/Results_B04_V01.md`;
2. `ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md`;
3. `ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx`;
4. `article/responses/6_RESULTS_B04_SECTION5_4_RESPONSE_V01.md`.

### 17. QA obligatorio

La response debe registrar como mínimo:

```text
PROTOCOL_READ = PASS
BLOCK = RESULTS_B04_SECTION_5_4
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
SOURCE_RECHECK = PASS
BASELINE_MD_SHA256 = 47cdd0be95c3d6267caa915baeba41519eaa654948a36c060bf207d61a3da699
BASELINE_MD_GIT_BLOB = cb0dc9cf64f01d945e1ae952e558fd459335f95e
BASELINE_DOCX_SHA256 = c6e5a93ec88c90851a8f4a156791982d044d3c6286d5fe1574f4aa6863dd5a85
AUTHORIZED_CLAIMS_USED = C35 / C36 / C37 / C38 / C39 / C40 / C41 as applicable
PROHIBITED_CLAIMS_USED = NONE
AUTOMATIC_VALIDATION_PASS_INVENTED = NO
PROMPT_SCHEMA_MISMATCH_PRESERVED = PASS
EVALUATOR_MODALITY_DEVIATION_PRESERVED = PASS
HUMAN_VALIDATION_CLAIM = NO
LEGAL_CORRECTNESS_CLAIM = NO
SECTION_5_4_ONLY_DIFF = PASS
SECTIONS_1_TO_5_3_PRESERVED = PASS
SECTIONS_5_5_PLUS_PRESERVED = PASS
NUMERICAL_CONTENT = PASS
EN_ES_EQUIVALENCE = PASS
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
ZIP_OOXML_INTEGRITY = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = PASS
D035_TIMEOUT_SAFE_HANDOFF = PASS
BASE64_MANUAL = NO
CHUNKING = NO
FRAGMENTATION = NO
REASSEMBLY = NO
```

### 18. Exit

```text
RESULTS_B04_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B05_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

En chat responde únicamente en español con la ruta+commit exactos de la response y entrega los candidatos acumulativos MD/DOCX como archivos reales. Detente después de B04.

---

## English

Draft only Results B04 / Section 5.4 from the exact V019 Markdown and approved B03 V01 DOCX baselines. Recheck the frozen HE4 artifacts at `main@db0d0ad0d8435921a7838db6720eaea86a263763`. Separate automatic structural controls from qualitative rubric outcomes. Do not invent a per-case automatic pass rate. Preserve the documented prompt–schema mismatch that makes frozen schema compliance 0/50, and preserve the actual AI-expert-role/LLM-as-judge evaluator modality rather than calling it human review. Report the 28/50 auditable-case result and the eight-dimension profile with its weaknesses as well as strengths. Do not convert auditability, structure, traceability, or rubric conformity into legal correctness, overall classification accuracy, human validation, causal faithfulness, or external generalization. Preserve all content outside §5.4, apply D-035, and stop after B04.