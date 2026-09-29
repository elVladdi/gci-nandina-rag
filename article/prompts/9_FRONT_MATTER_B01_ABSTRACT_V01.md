# Prompt — Front matter B01 / Abstract V01

## Español

### Rol

Actúa exclusivamente como IA de Redacción. Redacta únicamente el Abstract final en inglés y su espejo semántico natural en español sobre los masters acumulativos exactos autorizados. No modifiques Title, Keywords, ninguna sección 1–7 ni el end matter.

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
17. `article/governance/D155_DISCUSSION_B02_TRANSVERSAL_AUTHOR_APPROVAL_V030_VERIFICATION_AND_EDITORIAL_FREEZE.md`.
18. `article/governance/D156_CONCLUSION_SECTION7_INTERPRETIVE_BOUNDARY.md`.
19. `article/governance/D157_CONCLUSION_B01_V01_EXECUTION_AUTHORIZATION.md`.
20. `article/governance/D158_CONCLUSION_B01_V01_REAUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md`.
21. `article/governance/D159_CONCLUSION_B01_AUTHOR_APPROVAL_V031_VERIFICATION_AND_INTEGRATION.md`.
22. `article/governance/D160_FRONT_MATTER_ABSTRACT_INTERPRETIVE_BOUNDARY.md`.
23. La revisión interna vigente de este prompt.
24. La autorización vigente que apunte expresamente a este prompt.
25. Este prompt completo.
26. `article/manuscript/ARTICLE_MASTER_V031.md`.

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
INPUT_MASTER_MD = article/manuscript/ARTICLE_MASTER_V031.md
EXPECTED_SHA256 = 6f05e9e3b8a480fb24c46f5984214900cb8d77bfb203589b179da15aff059300
EXPECTED_GIT_BLOB = a8bfdcd30d1ec205c486102d991c37085f307b8c
```

Word acumulativo bajo custodia del autor:

```text
INPUT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_CONCLUSION_B01_V01.docx
EXPECTED_SHA256 = d561a0f25eca77ea234f9a0684786b57f8969436c8db1481cabbcc6db0f0792d
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_PAGE_COUNT = 71
```

Verifica ambas identidades antes de editar. Si no coinciden, detente. **No reconstruyas el DOCX desde Markdown.** Edita directamente el Word acumulativo exacto.

### Scope de edición

```text
TITLE = PRESERVE_PLACEHOLDER
ABSTRACT_EN = DRAFT
KEYWORDS = PRESERVE_PLACEHOLDER
SECTIONS_1_TO_7 = PRESERVE
END_MATTER = PRESERVE
SPANISH_TITLE = PRESERVE_PLACEHOLDER
SPANISH_ABSTRACT = DRAFT
SPANISH_KEYWORDS = PRESERVE_PLACEHOLDER
```

Solo sustituye las instrucciones/placeholder de Abstract/Resumen por texto final. No edites Title/Título, Keywords/Palabras clave ni ningún otro contenido.

### Función científica del Abstract

El Abstract debe poder entenderse sin conocimiento previo de NANDINA y condensar el artículo con esta secuencia:

```text
PROBLEM_AND_LIMITATION
-> PROPOSAL_AND_AUTHORITY_BOUNDARIES
-> EVALUATION_AND_MAIN_EVIDENCE
-> BOUNDED_INTERPRETATION
```

Redacta aproximadamente 200–250 palabras en inglés, preferentemente en un único párrafo continuo, y un espejo semántico natural en español.

#### Movimiento 1 — problema y limitación

Explica brevemente que los sistemas de apoyo a clasificación arancelaria pueden combinar generación/ranking de candidatos, material documental y generación explicativa, pero que cuando varias etapas pueden modificar la misma decisión se vuelve difícil atribuir qué componente produjo cada salida y evaluar ranking, evidencia y explicación como objetos distintos.

No declares un `FINAL_GAP`, ausencia absoluta de prior art, novelty ni first.

#### Movimiento 2 — propuesta y contrato de autoridad

Presenta el framework y su núcleo arquitectónico:

- historical retrieval recibe la descripción normalizada, genera/rankea candidatos y fija un Top-3;
- ese Top-3 se fija antes de documentary association y generation;
- candidate-specific documentary association añade evidencia a cada candidato sin insertar, eliminar, sustituir ni reordenar;
- el local LLM solo explica los candidatos recibidos y su contexto, sin autoridad de clasificación o feedback al ranking;
- candidate retrieval, documentary association y controlled explanation se evalúan separadamente.

No describas el sistema como un RAG indiferenciado ni al LLM como clasificador autónomo.

#### Movimiento 3 — evaluación y evidencia principal

Ubica la evaluación en un benchmark offline de clasificación arancelaria a nivel NANDINA-8 dentro del Chapter 87, con separación por DAM/declaración donde corresponde.

Usa solo las cifras centrales necesarias. Prioridad:

```text
HISTORICAL_TOP3 = 67.14%
HISTORICAL_TOP1 = 50.95% / OPTIONAL
MRR_AT_100 = 0.6297 / OPTIONAL
EXACT_DOCUMENTARY_ASSOCIATION = 3168/3168 CANDIDATE_SLOTS
DOCUMENTARY_TOP3_PRESERVATION = 1056/1056 CASES
EXPLANATION_TOP3_PRESERVATION = 50/50 CASES
QUALITATIVE_AUDITABILITY = 28/50 = 56.0%
```

No es obligatorio incluir todas las cifras. Prioriza Top-3, asociación/invariancia documental y el resultado cualitativo de explicación. Si la economía del texto lo exige, omite Top-1 y MRR antes que saturar el Abstract.

La asociación documental debe quedar delimitada al corpus evaluado y no convertirse en substantive normative correctness. El 56.0% debe identificarse como criterio cualitativo predefinido bajo evaluación LLM-as-judge, no como validación humana.

No introduzcas intervalos, p-values, métricas de comparadores, HE2/HE5, sensibilidad detallada, near-duplicates, buckets, códigos internos de experimentos ni nuevas inferencias.

#### Movimiento 4 — interpretación delimitada

Cierra reader-facing: separar autoridad y preservar provenance permite inspeccionar ranking, documentary evidence y generated explanation como salidas diferenciadas.

Mantén explícito o inequívoco que:

```text
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
LLM_AS_JUDGE != HUMAN_EXPERT_VALIDATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
REINSTANTIATION != DEPLOYMENT_READINESS
```

No es necesario listar literalmente todas estas desigualdades si el mismo límite se expresa de forma fluida y inequívoca. El Abstract debe dejar claro que la evidencia corresponde al benchmark offline evaluado y no demuestra transferencia de desempeño, legal validity, human validation ni deployment readiness.

### Claims y límites vinculantes

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
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No introduzcas literatura, búsqueda externa, citas, resultados, cálculos, inferencia, mecanismos causales, novelty, SOTA, superiority, legal correctness, human validation, deployment readiness ni external generalization nuevos.

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
ABSTRACT_SELF_CONTAINED = PASS
```

No uses en el manuscrito IDs de decisiones, gates, hashes, commits, nombres de prompt/response, usernames, códigos de QA, IDs internos de experimentos o nombres internos de campos. Evita `H100` en el Abstract: usa una formulación reader-facing como `historical BM25 over the full historical bank` si fuera necesario identificar la configuración.

### Citas, comentarios y Word

El Abstract no debe introducir citas.

```text
NEW_ENGLISH_CITATION_OCCURRENCES = 0
NEW_CITATION_COMMENTS = 0
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
```

Preserva los 48 comentarios heredados y sus anclajes. Realiza auditoría diferencial OOXML y render completo. No reconstruyas Word desde Markdown.

D-035: no usar Base64 manual, chunking, fragmentación, reensamblado ni workarounds equivalentes. D-027: entregar el DOCX exacto al autor. D-022: versionar primero la response en GitHub.

### Entregables

1. `article/sections/front_matter/Abstract_B01_V01.md`
2. `ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V01.md`
3. `ARTICLE_MASTER_CANDIDATE_ABSTRACT_B01_V01.docx`
4. `article/responses/9_FRONT_MATTER_B01_ABSTRACT_RESPONSE_V01.md`

### Checklist MWDP obligatorio

La response debe declarar al menos:

```text
PROTOCOL_READ = MWDP_V1.0
SPCCR_READ = SPCCR_V1.0
KBS_EWG_34_V01_READ = YES
D136_READ = YES
ONBOARDING = PASS / BLOCKED
BLOCK = FRONT_MATTER_B01_ABSTRACT
INPUT_MASTER_MD_IDENTITY = PASS / BLOCKED
INPUT_MASTER_DOCX_IDENTITY = PASS / BLOCKED
TITLE_MODIFIED = NO
ABSTRACT_MODIFIED = YES
KEYWORDS_MODIFIED = NO
SECTIONS_1_TO_7_MODIFIED = NO
END_MATTER_MODIFIED = NO
NEW_RESULTS_OR_INFERENCE = NONE
NEW_LITERATURE = NONE
NEW_ENGLISH_CITATION_OCCURRENCES = 0
INTERNAL_TERMINOLOGY_LEAKAGE = NONE
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
ABSTRACT_SELF_CONTAINED = PASS
COMMENTS = 48
TRACKED_CHANGES = 0
OOXML_CHANGED_PARTS = ...
FULL_DOCX_PAGE_COUNT = ...
FULL_DOCX_RENDER = PASS / BLOCKED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT
```

### Gate de salida

Detente después de producir Abstract B01 V01.

```text
EXPECTED_EXIT = FRONT_MATTER_B01_ABSTRACT_V01_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
TITLE = NOT_AUTHORIZED
KEYWORDS = NOT_AUTHORIZED
END_MATTER_FINALIZATION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English control summary

Draft only the final English Abstract and its semantically equivalent Spanish mirror from exact canonical V031 and the exact cumulative Conclusion Word baseline. Preserve Title, Keywords, Sections 1–7, and all end matter. Use the KBS-style sequence problem/limitation -> proposal and authority separation -> evaluation/main evidence -> bounded interpretation, approximately 200–250 English words, no citations, and no new results or claims. Keep candidate retrieval, documentary association, and controlled explanation distinct; use only essential approved figures; and do not convert candidate retrieval into overall accuracy, documentary association into normative/legal correctness, or LLM-as-judge auditability into human validation. Stop after the Abstract candidate and do not proceed to Title, Keywords, or end matter.
