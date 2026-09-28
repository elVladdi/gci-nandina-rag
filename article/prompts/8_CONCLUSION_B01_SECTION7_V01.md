# Prompt — Conclusion B01 / Section 7 V01

## Español

### Rol

Actúa exclusivamente como IA de Redacción. Redacta únicamente Section 7 / Conclusion en inglés y español sobre los masters acumulativos exactos autorizados. No modifiques ninguna sección previa ni el front/end matter.

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
17. `article/governance/D151_DISCUSSION_B06_V029_VERIFICATION_INTEGRATION_AND_DISCUSSION_CLOSURE.md`.
18. `article/governance/D152_DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_BOUNDARY.md`.
19. `article/governance/D153_DISCUSSION_B02_TRANSVERSAL_TERMINOLOGY_HYGIENE_EXECUTION_AUTHORIZATION.md`.
20. `article/governance/D154_DISCUSSION_B02_TRANSVERSAL_V01_REAUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md`.
21. `article/governance/D155_DISCUSSION_B02_TRANSVERSAL_AUTHOR_APPROVAL_V030_VERIFICATION_AND_EDITORIAL_FREEZE.md`.
22. `article/governance/D156_CONCLUSION_SECTION7_INTERPRETIVE_BOUNDARY.md`.
23. La revisión interna vigente de este prompt.
24. La autorización vigente que apunte expresamente a este prompt.
25. Este prompt completo.
26. `article/manuscript/ARTICLE_MASTER_V030.md`.

No uses conversaciones anteriores como fuente de verdad. Si el estado vivo contradice estas instrucciones o falta un baseline exacto, detente y registra el bloqueo en la response versionada.

### Preflight obligatorio

La response debe registrar:

```text
ARCHIVOS_LEÍDOS:
FASE_ACTIVA:
ESTADO_DEL_BLOQUE_ASIGNADO:
REDACCIÓN_AUTORIZADA: SÍ / NO
DECISIONES_CONGELADAS_RELEVANTES:
CLAIMS_AUTORIZADOS_RELEVANTES:
CLAIMS_PROHIBIDOS_O_PENDIENTES_RELEVANTES:
FUENTES_EXTERNAS_QUE_DEBEN_VERIFICARSE:
BLOQUEOS_O_CONTRADICCIONES_DETECTADOS:
```

### Baselines exactos

Markdown canónico:

```text
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V030.md
EXPECTED_SHA256 = ba4d3d5021a6be5fc43a435c3618c65e0778b900609b708014cb04d7866b9b7d
EXPECTED_GIT_BLOB = 2683f5933205219ed62e16418d3f9a0ace7460bd
```

Word acumulativo bajo custodia del autor:

```text
INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_TRANSVERSAL_V01.docx
EXPECTED_SHA256 = 340e283924a9364447344469cf4eb077bbf93f7d32509f8f173d0a01fb3bbc0f
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 69
```

Verifica ambas identidades antes de editar. Si no coinciden, detente. **No reconstruyas el DOCX desde Markdown.** Edita directamente el Word acumulativo exacto.

### Scope de edición

```text
SECTIONS_1_TO_6_6 = PRESERVE
SECTION_7_CONCLUSION = DRAFT_EN_AND_ES
FRONT_MATTER = PRESERVE
DATA_AVAILABILITY = PRESERVE_PLACEHOLDER
CODE_REPRODUCIBILITY = PRESERVE_PLACEHOLDER
CREDIT = PRESERVE_PLACEHOLDER
FUNDING = PRESERVE_PLACEHOLDER
COMPETING_INTEREST = PRESERVE_PLACEHOLDER
ACKNOWLEDGEMENTS = PRESERVE_PLACEHOLDER
REFERENCES = PRESERVE
SUPPLEMENTARY_MATERIAL = PRESERVE_PLACEHOLDER
```

No edites Title, Abstract, Keywords ni ningún end matter.

### Función científica de Conclusion

Conclusion debe cerrar el artículo con esta secuencia:

```text
CONTRIBUTION -> MAIN_EVIDENCE -> SCOPE -> BOUNDED_IMPLICATION
```

No debe repetir Results ni Discussion en miniatura. Debe sintetizar qué se estudió, qué evidencia principal quedó establecida, bajo qué límites se interpreta y qué implicación acotada se deriva.

Redacta aproximadamente 300–400 palabras en inglés, preferentemente 3–4 párrafos, con espejo semántico natural en español.

#### Párrafo 1 — contribución/metodología

Resume la contribución metodológica ya aprobada: la arquitectura separa explícitamente la autoridad de historical candidate retrieval, candidate-specific documentary association y controlled explanation. Historical retrieval genera/rankea candidatos y fija Top-3 antes de evidence retrieval y generation; etapas posteriores no pueden cambiar membership/order. Candidate retrieval, documentary association y explanation se evalúan como objetos distintos.

No declares novelty, first, SOTA o superioridad.

#### Párrafo 2 — evidencia principal

Integra solo las cifras indispensables ya aprobadas. Puedes usar:

- historical BM25 H100: Top-1 = 50.95%, Top-3 = 67.14%, MRR@100 = 0.6297;
- exact documentary association = 3,168/3,168 candidate slots;
- Top-3 membership/order preserved = 1,056/1,056 cases en documentary stage;
- explanation Top-3/order preserved = 50/50 cases;
- qualitative auditability criterion = 28/50 = 56.0%.

Si mencionas las comparaciones inferenciales, limita la afirmación a que apoyan el resultado de candidate retrieval **dentro del benchmark y diseño inferencial internos**, sin convertirlo en superioridad global del framework.

Mantén explícitamente:

```text
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
LLM_AS_JUDGE != HUMAN_EXPERT_VALIDATION
```

#### Párrafo 3 — alcance y limitaciones

Sintetiza, sin lista exhaustiva, las limitaciones que gobiernan la interpretación: colección administrativa purposiva; Chapter 87/NANDINA-8; dependencia intra-DAM y similitud residual; sensibilidad del banco histórico sin efecto causal aislado de tamaño; objetos de robustness no estimables; Decision 885/906 documentary drift; qualitative explanation assessment limitada a 50 casos y LLM-as-judge; no operational/legal/human validation; paquete público de reference reproduction todavía incompleto.

No introduzcas nuevos diagnósticos ni magnitudes.

#### Párrafo 4 — implicación acotada

Cierra con una implicación reader-facing: separar autoridad y preservar provenance hace que ranking, documentary evidence y generated explanation puedan inspeccionarse como salidas diferenciadas en decision support. La re-instanciación con otros datos/corpora/modelos es condicional a interfaces/provenance y requiere validación propia. No implica performance transfer, external generalization, deployment readiness ni legal validity.

### Claims y límites vinculantes

Preserva estas relaciones:

```text
ARCHITECTURE = TECHNICAL_CORE_OF_FRAMEWORK
HISTORICAL_RETRIEVAL = ONLY_PRIMARY_CANDIDATE_RANKING_AUTHORITY
FIXED_TOP3 = ESTABLISHED_BEFORE_DOCUMENTARY_AND_GENERATIVE_STAGES
NORMATIVE_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
REPRODUCTION != EXTERNAL_REPLICATION
REINSTANTIATION != DEPLOYMENT_READINESS
CHAPTER87_RESULTS = NOT_TRANSFERABLE_BY_ASSUMPTION
HE2 = SUPPORTED_ONLY_WITHIN_FROZEN_INTERNAL_INFERENTIAL_SCOPE
HE5 = INCONCLUSIVE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No introduzcas literatura, búsqueda externa, citas nuevas, cálculos, intervalos, p-values, resultados, inferencias, mecanismos causales, novelty, SOTA, superiority, legal correctness, human validation, deployment readiness ni external generalization.

### Control D-136 / KBS / SPCCR

La prosa publicable debe cumplir:

```text
SCIENTIFIC_FIDELITY = PASS
EPISTEMIC_STRENGTH = BOUNDED
NO_NEW_RESULTS_OR_INFERENCE = PASS
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
READER_FACING_PROSE = PASS
ABSTRACTION_DENSITY = ACCEPTABLE
AGENT_ACTION_OBJECT_CLARITY = PASS
NOMINALIZATION_OVERLOAD = ABSENT
PROCESS_RELATIONSHIPS_EXPLICIT = PASS
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
KBS_CONCRETE_PROSE = PASS
```

No uses en el manuscrito IDs de decisiones, gates, hashes, commits, nombres de prompt/response, usernames, códigos de QA, IDs internos de experimentos, nombres internos de campos o etiquetas de gobernanza.

### Citas, comentarios y Word

Conclusion no debe introducir citas nuevas.

```text
NEW_ENGLISH_CITATION_OCCURRENCES = 0
NEW_CITATION_COMMENTS = 0
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Preserva los 48 comentarios heredados y sus anclajes. Realiza auditoría diferencial OOXML y render completo. No reconstruyas Word desde Markdown.

D-035: no usar Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. D-027: entregar el DOCX exacto al autor. D-022: versionar primero la response en GitHub.

### Entregables

1. `article/sections/conclusion/Conclusion_B01_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_CONCLUSION_B01_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_CONCLUSION_B01_V01.docx`
4. `article/responses/8_CONCLUSION_B01_SECTION7_RESPONSE_V01.md`

### Checklist MWDP obligatorio

La response debe declarar al menos:

```text
PROTOCOL_READ = MWDP_V1.0
SPCCR_READ = SPCCR_V1.0
KBS_EWG_34_V01_READ = YES
D136_READ = YES
ONBOARDING = PASS / BLOCKED
BLOCK = CONCLUSION_B01_SECTION_7
INPUT_MASTER_MD_IDENTITY = PASS / BLOCKED
INPUT_MASTER_DOCX_IDENTITY = PASS / BLOCKED
SECTIONS_1_TO_6_6_MODIFIED = NO
CONCLUSION_MODIFIED = YES
FRONT_END_MATTER_MODIFIED = NO
NEW_RESULTS_OR_INFERENCE = NONE
NEW_LITERATURE = NONE
NEW_ENGLISH_CITATION_OCCURRENCES = 0
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
COMMENTS = 48
TRACKED_CHANGES = 0
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### Gate de salida

Detente después de producir Conclusion B01 V01.

```text
EXPECTED_EXIT = CONCLUSION_B01_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
FRONT_MATTER_FINALIZATION = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Draft only Section 7 Conclusion in English and Spanish from the exact V030 Markdown and transversal-clean Word baselines. Synthesize approved contribution, main evidence, scope, and bounded implication. Preserve all prior sections and all front/end matter. Introduce no literature, citations, results, calculations, inference, novelty, superiority, legal correctness, human validation, deployment-readiness, or external-generalization claims. Stop at `CONCLUSION_B01_V01_COMPLETED_PENDING_GESTORA_AUDIT`.