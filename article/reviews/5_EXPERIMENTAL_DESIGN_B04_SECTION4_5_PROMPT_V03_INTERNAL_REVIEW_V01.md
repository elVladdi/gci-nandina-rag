# Revisión interna — Prompt B04 / Section 4.5 V03 / Internal review — B04 Section 4.5 Prompt V03

## Español

```text
REVIEW_ID = B04_SECTION_4_5_PROMPT_V03_INTERNAL_REVIEW_V01
DATE = 2026-09-26
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
PROMPT_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
PARENT_AUDIT = article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02.md@2a184469cd36710c45c2045a8aa0c0db45204c47
PARENT_DECISION = D-061
VERDICT = PASS
ONBOARDING_ORDER = PASS
CONTROL_FILE_CONSISTENCY = PASS
SCIENTIFIC_SCOPE = PASS
MWDP_CONTRACT = PASS
DOCX_CONTINUITY = PASS
HANDOFF_REQUIREMENT = PASS
BILINGUAL_EQUIVALENCE = PASS
RESULTS_BOUNDARY = PASS
B05 = NOT_AUTHORIZED
```

### 1. Objeto

La IA Gestora auditó el Prompt B04 V03 después de sincronizar `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md`. El objetivo fue verificar que V03 cerrara los defectos detectados en V01/V02 sin alterar el alcance científico autoralmente congelado de Section 4.5.

### 2. Orden de onboarding

V03 reproduce correctamente el orden obligatorio de `START_HERE.md`:

1. `START_HERE.md`;
2. `README.md`;
3. `ARTICLE_STATUS.md`;
4. `ARTICLE_WRITING_PLAN.md`;
5. `DECISIONS.md`;
6. `SOURCE_REGISTRY.md`;
7. `CLAIM_EVIDENCE_MATRIX.md`;
8. `STYLE_GUIDE.md`;
9. archivo específico de la tarea.

Los contratos acumulativos —MWDP, SPCCR, D-021, D-022, D-027, D-035, D-045, D-058, D-060 y D-061— se leen después de ese orden y antes de producir contenido. No existe contradicción entre ambos requisitos.

### 3. Estado y baselines

El prompt usa correctamente:

- `ARTICLE_MASTER_V012.md`;
- SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`;
- Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`;
- SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`;
- 40 comentarios heredados como baseline de continuidad.

Es consistente con D-058, D-060, D-061 y los controles vivos sincronizados.

### 4. Alcance científico

V03 mantiene el alcance correcto de 4.5 `Experimental system configuration and execution / Configuración y ejecución experimental` y no lo vuelve a reducir a recuperación histórica.

Exige cubrir, con evidencia primaria:

- representación y preprocesamiento de consulta;
- recuperación histórica y parámetros realmente ejecutados;
- construcción Top-k / fixed Top-3;
- asociación documental por candidato en Phase F sin reranking;
- construcción del contexto;
- modelo local, prompt, parámetros y restricciones de generación;
- condiciones materiales de ejecución solo si están verificadas y son relevantes.

Esto es coherente con D-045 y Structure V02.

### 5. Fronteras científicas

El prompt conserva correctamente:

```text
HISTORICAL_RETRIEVAL = PRIMARY_CANDIDATE_GENERATOR_AND_RANKER
FIXED_TOP3 = FROZEN_BEFORE_DOCUMENTARY_AND_GENERATIVE_STAGES
PRIMARY_DOCUMENTARY_ASSOCIATION = CANDIDATE_SPECIFIC / NO_RERANK
LOCAL_LLM = DOWNSTREAM_EXPLANATION_ONLY
NO_INSERT_DELETE_SUBSTITUTE_REORDER
NO_CLASSIFICATION_FEEDBACK
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
NORMATIVE_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
```

También prohíbe trasladar a Methods valores observados de desempeño de candidate retrieval, Phase F, HE4, HE2, EXP11A/EXP11B/EXP12, latencias agregadas, tokens, auditability rates, global accuracy, legal correctness, gap o novelty.

### 6. Continuidad de artefactos y entrega

V03 exige los cuatro entregables correctos:

1. bloque B04 versionado;
2. master Markdown acumulativo candidato;
3. master DOCX acumulativo candidato;
4. response versionada bilingüe.

El DOCX es explícitamente obligatorio, debe derivarse del B03 exacto, preservar los 40 comentarios/anclajes heredados y `tracked changes = 0`, y debe ser entregado efectivamente al autor. El prompt incorpora el régimen timeout-safe de D-035 sin autorizar Base64/chunking/reensamblado ni reconstrucción posterior.

### 7. QA y gate

El checklist MWDP está presente. El QA exige identidad de baselines, preservación de Sections 1–4.4 y 4.6+, presencia 4.5 EN/ES, frontera 4.6, integridad OOXML, parsing XML/RELS, comentarios/anclajes, cero tracked changes, render completo y equivalencia EN/ES.

El gate final es correcto:

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```

No permite integrar B04 ni abrir 4.6.

### 8. Dictamen

`PASS`.

El Prompt B04 V03 puede convertirse en el contrato operativo vigente para la IA de Redacción. V01 y V02 permanecen históricos y no ejecutables.

---

## English

```text
REVIEW_ID = B04_SECTION_4_5_PROMPT_V03_INTERNAL_REVIEW_V01
DATE = 2026-09-26
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
PROMPT_GIT_BLOB = 6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36
PARENT_AUDIT = article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02.md@2a184469cd36710c45c2045a8aa0c0db45204c47
PARENT_DECISION = D-061
VERDICT = PASS
ONBOARDING_ORDER = PASS
CONTROL_FILE_CONSISTENCY = PASS
SCIENTIFIC_SCOPE = PASS
MWDP_CONTRACT = PASS
DOCX_CONTINUITY = PASS
HANDOFF_REQUIREMENT = PASS
BILINGUAL_EQUIVALENCE = PASS
RESULTS_BOUNDARY = PASS
B05 = NOT_AUTHORIZED
```

### 1. Purpose

The Managing AI audited B04 Prompt V03 after synchronizing `ARTICLE_STATUS.md` and `ARTICLE_WRITING_PLAN.md`. The review verified that V03 closes the V01/V02 defects without altering the author-frozen scientific function of Section 4.5.

### 2. Onboarding order

V03 correctly reproduces the mandatory `START_HERE.md` order: `START_HERE → README → ARTICLE_STATUS → ARTICLE_WRITING_PLAN → DECISIONS → SOURCE_REGISTRY → CLAIM_EVIDENCE_MATRIX → STYLE_GUIDE → task-specific file`. The cumulative contracts—MWDP, SPCCR, D-021, D-022, D-027, D-035, D-045, D-058, D-060, and D-061—are then read before any content is produced. The two requirements are compatible.

### 3. State and baselines

The prompt correctly binds canonical `ARTICLE_MASTER_V012.md` at SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`, Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`, and the cumulative B03 DOCX `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx` at SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, with 40 inherited comments as the continuity baseline. This matches D-058/D-060/D-061 and the synchronized live controls.

### 4. Scientific scope

V03 preserves the complete Section-4.5 scope `Experimental system configuration and execution` rather than narrowing it back to historical retrieval. It requires primary-evidence verification for query representation/preprocessing, historical retrieval, Top-k/fixed-Top-3 construction, candidate-specific Phase-F documentary association without reranking, context construction, local-model/prompt/generation restrictions, and material execution conditions only when verified and relevant. This is consistent with D-045 and Structure V02.

### 5. Scientific boundaries

V03 preserves the governing functional boundaries, including fixed Top-3 before documentary/generative stages, no documentary reranking, downstream explanation-only LLM use, no candidate insertion/deletion/substitution/reordering, no classification feedback, and the distinctions between candidate retrieval and global accuracy, normative association and substantive correctness, auditability and legal correctness, and configurability and empirical generalization.

The prompt also correctly excludes observed candidate-retrieval, Phase-F, HE4, HE2, EXP11A/EXP11B/EXP12, aggregate latency/token, auditability-rate, global-accuracy, legal-correctness, final-gap, and novelty results from Methods.

### 6. Artifact continuity and handoff

V03 requires the correct four deliverables: versioned B04 block, cumulative candidate Markdown master, cumulative candidate DOCX master, and bilingual versioned response. The DOCX is unconditionally mandatory, must derive from the exact B03 binary, preserve all 40 inherited citation comments/anchors with zero tracked changes, and must actually be handed to the author. D-035 timeout-safe handling is incorporated without authorizing Base64/chunking/reassembly or later reconstruction.

### 7. QA and gate

The MWDP checklist is present. QA covers baseline identity, preservation of Sections 1–4.4 and 4.6+, EN/ES 4.5 presence, Section-4.6 boundary, OOXML integrity, XML/RELS parsing, comment/anchor preservation, zero tracked changes, full render, and EN/ES equivalence.

The final gate is correct:

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B05 = NOT_AUTHORIZED
```

The prompt does not authorize B04 integration or Section 4.6.

### 8. Verdict

`PASS`.

B04 Prompt V03 is fit to become the active operational contract for the Drafting AI. V01 and V02 remain historical and non-executable.