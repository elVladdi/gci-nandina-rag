# D-061 — Sincronización de controles y requisito de Prompt B04 V03 / Control synchronization and B04 Prompt V03 requirement

## Español

```text
DECISION_ID = D-061
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_AUDIT = article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02.md@2a184469cd36710c45c2045a8aa0c0db45204c47
PARENT_DECISION = D-060
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
B02_SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
B03_SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
D059 = SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION / PROCEDURAL_ONBOARDING_ORDER_DEFECT
ARTICLE_STATUS = MUST_BE_SYNCHRONIZED_TO_V012_B04
ARTICLE_WRITING_PLAN = MUST_BE_SYNCHRONIZED_TO_V012_B04
B04_PROMPT_V03 = REQUIRED / NOT_YET_MATERIALIZED
SECTION_4_5 = ELIGIBLE / EXECUTION_BLOCKED_UNTIL_CONTROL_SYNC_AND_V03
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Motivo

La auditoría reforzada V02 confirmó que el contenido científico de B02/4.3 y B03/4.4 permanece válido y que `ARTICLE_MASTER_V012.md` es el master canónico vigente. Sin embargo, `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` continuaban declarando V010/B02 como estado activo. Además, el Prompt B04 V02, aunque corrigió sustancialmente el alcance científico de 4.5, afirmó seguir el orden de onboarding de `START_HERE.md` y enumeró los archivos en un orden distinto.

### 2. Corrección de controles

Se autoriza y exige sincronizar los dos controles vivos:

- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`.

Ambos deben reflejar como mínimo:

- master canónico `ARTICLE_MASTER_V012.md`;
- DOCX acumulativo vigente `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`;
- B02/4.3 y B03/4.4 cerrados, aprobados, congelados e integrados;
- D-059 y Prompt B04 V01 superseded;
- Prompt B04 V02 no ejecutable como contrato final debido al defecto procedimental de onboarding;
- Section 4.5 como siguiente bloque científico, pero sin ejecución válida hasta materializar V03;
- Sections 4.6–4.8 y Results no autorizados;
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED`.

La sincronización de estos archivos es administrativa/editorial. No reabre ciencia aprobada ni modifica resultados experimentales.

### 3. Prompt B04 V03

El Prompt B04 V03 debe ser autosuficiente y preservar íntegramente el alcance científico y los contratos acumulativos válidos de V02. La corrección obligatoria incluye:

1. usar exactamente el orden de onboarding de `START_HERE.md`:
   `START_HERE → README → ARTICLE_STATUS → ARTICLE_WRITING_PLAN → DECISIONS → SOURCE_REGISTRY → CLAIM_EVIDENCE_MATRIX → STYLE_GUIDE → archivo específico de la tarea`;
2. mantener MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-058, D-060 y D-061;
3. mantener el alcance completo de 4.5 `Experimental system configuration and execution`;
4. mantener la continuidad obligatoria Markdown + DOCX, QA OOXML, comentarios, tracked changes, render y handoff real al autor;
5. mantener las fronteras científicas y la prohibición de anticipar Results.

V02 se conserva como artefacto histórico; no debe sobrescribirse silenciosamente.

### 4. Gate

```text
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
NEXT_ACTOR = IA_GESTORA
B04_EXECUTION = BLOCKED_UNTIL_V03
AUTHOR_APPROVAL_GATE = NOT_APPLICABLE_AT_THIS_STAGE
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-061
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_AUDIT = article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V02.md@2a184469cd36710c45c2045a8aa0c0db45204c47
PARENT_DECISION = D-060
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
B02_SECTION_4_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
B03_SECTION_4_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
D059 = SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
B04_PROMPT_V02 = SUPERSEDED_FOR_EXECUTION / PROCEDURAL_ONBOARDING_ORDER_DEFECT
ARTICLE_STATUS = MUST_BE_SYNCHRONIZED_TO_V012_B04
ARTICLE_WRITING_PLAN = MUST_BE_SYNCHRONIZED_TO_V012_B04
B04_PROMPT_V03 = REQUIRED / NOT_YET_MATERIALIZED
SECTION_4_5 = ELIGIBLE / EXECUTION_BLOCKED_UNTIL_CONTROL_SYNC_AND_V03
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Rationale

The reinforced V02 audit confirmed that B02/4.3 and B03/4.4 remain scientifically valid and that `ARTICLE_MASTER_V012.md` is the current canonical master. However, `ARTICLE_STATUS.md` and `ARTICLE_WRITING_PLAN.md` still declared V010/B02 as active. In addition, B04 Prompt V02 substantially corrected the scientific scope of Section 4.5 but claimed to follow the `START_HERE.md` onboarding order while listing the files in a different sequence.

### 2. Control-file correction

The Managing AI is authorized and required to synchronize:

- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`.

Both controls must reflect at least the canonical V012 Markdown, the current B03 cumulative DOCX, closure/integration of B02/4.3 and B03/4.4, supersession of D-059 and B04 Prompt V01, non-executability of B04 Prompt V02 as the final contract due to its onboarding-order defect, Section 4.5 as the next scientific block but blocked until V03 is materialized, continued closure of Sections 4.6–4.8 and Results, and the continuing `FINAL_GAP = NOT_DEFINED` / `NOVELTY = NOT_DECLARED` boundaries.

This synchronization is administrative/editorial. It does not reopen approved science or alter experimental results.

### 3. B04 Prompt V03

B04 Prompt V03 must be self-contained and preserve all scientifically and procedurally valid content from V02. It must:

1. use the exact `START_HERE.md` onboarding sequence:
   `START_HERE → README → ARTICLE_STATUS → ARTICLE_WRITING_PLAN → DECISIONS → SOURCE_REGISTRY → CLAIM_EVIDENCE_MATRIX → STYLE_GUIDE → task-specific file`;
2. preserve MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-058, D-060, and D-061;
3. preserve the complete Section-4.5 scope, `Experimental system configuration and execution`;
4. preserve mandatory cumulative Markdown + DOCX continuity, OOXML/comment/tracked-change/render QA, and actual author handoff;
5. preserve all scientific boundaries and the prohibition on anticipating Results.

V02 remains a historical artifact and must not be silently overwritten.

### 4. Gate

```text
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
NEXT_ACTOR = MANAGING_AI
B04_EXECUTION = BLOCKED_UNTIL_V03
AUTHOR_APPROVAL_GATE = NOT_APPLICABLE_AT_THIS_STAGE
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```