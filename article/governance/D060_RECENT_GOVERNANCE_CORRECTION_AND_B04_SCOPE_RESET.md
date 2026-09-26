# D-060 — Corrección de gobernanza reciente y restablecimiento del alcance B04 / Recent governance correction and B04 scope reset

## Español

```text
DECISION_ID = D-060
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_AUDIT = article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V01.md@549e4546c5fafb8510f7c2dc7d20d531b9c61aa4
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
B02_SECTION_4_3 = RATIFIED / CLOSED / APPROVED / FROZEN / INTEGRATED
B03_SECTION_4_4 = RATIFIED / CLOSED / APPROVED / FROZEN / INTEGRATED
D059 = SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION
B04_PROMPT_V01_COMMIT = 7a7aef7994c909e1fde6c01fa8dad7c2cb52f525
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
SECTION_4_5 = OPEN / AUTHORIZED_ONLY_UNDER_CORRECTED_FULL_SCOPE_PROMPT
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Ratificación de B02, B03 y masters canónicos

La auditoría retrospectiva no encontró un error científico persistente en B02/4.3, B03/4.4 ni en sus promociones canónicas. Se ratifican D-055 y D-058 en cuanto a sus efectos científicos y técnicos válidos:

- `ARTICLE_MASTER_V011.md` fue una materialización byte-exacta del candidato B02 aprobado;
- `ARTICLE_MASTER_V012.md` fue una materialización byte-exacta del candidato B03 aprobado;
- Section 4.3 y Section 4.4 permanecen cerradas, aprobadas, congeladas e integradas;
- el DOCX acumulativo vigente para abrir el siguiente bloque es `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`, SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`.

La omisión inicial del DOCX en B03 quedó cerrada antes de la aprobación autoral. No se reabre B03.

### 2. Normalización de la revisión B03 histórica

La etiqueta histórica `PASS_WITH_BLOCKING_TECHNICAL_CORRECTION` se interpreta canónicamente como `PASS WITH CORRECTIONS`, de acuerdo con el vocabulario permitido por `START_HERE.md`. La corrección exigida fue técnica —continuidad DOCX— y quedó cerrada mediante el microgate posterior; el resultado final B03 es `PASS`.

No se reescribe retroactivamente el review histórico.

### 3. Incumplimiento bilingüe documentado

D-055, D-056 y D-058 quedaron materializados en español solamente; D-057 presenta una sección inglesa resumida y no equivalente en extensión/completitud; algunos prompts/reviews recientes también omitieron el espejo inglés completo.

Sus efectos científicos ya auditados no se invalidan por este defecto de presentación, pero esos artefactos **no constituyen precedente válido de formato**. Desde D-060, toda nueva decisión, prompt, review, status y plan creado/modificado bajo `article/` debe cumplir estrictamente D002/README/START_HERE: español e inglés con la misma información científica, alcance, restricciones y fuerza epistémica.

### 4. Restablecimiento exacto de Section 4.5

D-045 y `KBS_ARTICLE_WORKING_STRUCTURE_V02.md` gobiernan. Section 4.5 es exactamente:

`4.5 Experimental system configuration and execution / Configuración y ejecución experimental`.

Su función no puede reducirse a recuperación histórica. Debe instanciar la arquitectura de Section 3 sin reexplicarla conceptualmente y describir únicamente decisiones de ejecución que afectaron materialmente el experimento:

1. representación y normalización de la consulta;
2. configuración de recuperación histórica;
3. construcción del ranking Top-k y del Top-3 fijo;
4. asociación documental específica por candidato en la ruta primaria realmente ejecutada;
5. construcción del contexto suministrado al generador;
6. modelo local, prompt/configuración y restricciones de generación realmente ejecutados;
7. condiciones materiales de software/hardware/runtime únicamente cuando estén verificadas y sean relevantes para reproducibilidad/interpretación.

La subsección no debe anticipar resultados ni métricas observadas de desempeño.

### 5. Supersession de D-059 y B04 Prompt V01

D-059 restringió indebidamente 4.5 a `Historical retrieval configuration and candidate-generation protocol`. Esa definición contradice la estructura autoral congelada. En consecuencia:

- D-059 queda `SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION`;
- `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5.md@7a7aef7994c909e1fde6c01fa8dad7c2cb52f525` queda `SUPERSEDED / DO_NOT_EXECUTE`;
- no se modifica ni elimina el archivo histórico; su identidad se conserva para trazabilidad;
- la única ejecución B04 válida será la realizada bajo el nuevo prompt V02 expresamente gobernado por D-060.

Si el prompt V01 ya hubiera sido enviado o iniciado, su salida no puede aprobarse como B04 completo. Debe detenerse o reconciliarse exclusivamente mediante el prompt V02; no se presume que el subalcance histórico cubra la subsección completa.

### 6. Contrato obligatorio para B04 V02

El nuevo prompt debe invocar expresamente:

- `START_HERE.md` y su onboarding íntegro;
- MWDP v1.0;
- SPCCR;
- D-021, D-022, D-027 y D-035;
- D-045, D-058 y D-060;
- el estado vivo de SRC-03 y `main`;
- la Structure V02 y el master canónico V012.

Debe exigir los artefactos acumulativos Markdown y DOCX, el handoff real del DOCX al autor, QA OOXML/comentarios/tracked changes/render, equivalencia bilingüe y el checklist completo MWDP. La ausencia de una obligación acumulativa en un prompt no debe volver a interpretarse como derogación.

### 7. Fronteras científicas para 4.5

Permanecen vinculantes:

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
RESULTS_VALUES_IN_4_5 = NONE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 8. Estado posterior

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_CORRECTED_DRAFTING
NEXT_ACTOR = IA_REDACCION
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V02.md
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V02_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-060
DATE = 2026-09-26
STATUS = ACTIVE / BINDING
PARENT_AUDIT = article/reviews/INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V01.md@549e4546c5fafb8510f7c2dc7d20d531b9c61aa4
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
B02_SECTION_4_3 = RATIFIED / CLOSED / APPROVED / FROZEN / INTEGRATED
B03_SECTION_4_4 = RATIFIED / CLOSED / APPROVED / FROZEN / INTEGRATED
D059 = SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION
B04_PROMPT_V01_COMMIT = 7a7aef7994c909e1fde6c01fa8dad7c2cb52f525
B04_PROMPT_V01 = SUPERSEDED / DO_NOT_EXECUTE
SECTION_4_5 = OPEN / AUTHORIZED_ONLY_UNDER_CORRECTED_FULL_SCOPE_PROMPT
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Ratification of B02, B03, and canonical masters

The retrospective audit found no persistent scientific error in B02/4.3, B03/4.4, or their canonical promotions. D-055 and D-058 are ratified with respect to their valid scientific and technical effects: V011 was the byte-exact approved B02 candidate, V012 was the byte-exact approved B03 candidate, Sections 4.3 and 4.4 remain closed/approved/frozen/integrated, and the current cumulative DOCX baseline is `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx` at SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`.

The initial B03 DOCX omission was closed before author approval and does not reopen B03.

### 2. Historical B03 review-verdict normalization

The historical token `PASS_WITH_BLOCKING_TECHNICAL_CORRECTION` is canonically interpreted as `PASS WITH CORRECTIONS`, consistent with the review vocabulary allowed by `START_HERE.md`. The required correction was technical DOCX continuity; the subsequent microgate closed it and B03 ultimately passed. The historical review file is not rewritten retroactively.

### 3. Documented bilingual noncompliance

D-055, D-056, and D-058 were materialized only in Spanish; D-057 contains an English section that is materially shorter than the Spanish decision; and some recent prompts/reviews likewise omitted a complete English mirror. Their already-audited scientific effects are not invalidated by this presentation defect, but those artifacts are not valid formatting precedents. From D-060 onward, every new or modified decision, prompt, review, status, and plan under `article/` must strictly follow D002/README/START_HERE: Spanish and English with equivalent scientific information, scope, restrictions, and epistemic strength.

### 4. Exact restoration of Section 4.5

D-045 and `KBS_ARTICLE_WORKING_STRUCTURE_V02.md` govern. Section 4.5 is exactly `Experimental system configuration and execution / Configuración y ejecución experimental`.

Its function may not be reduced to historical retrieval. It must instantiate the Section-3 architecture without conceptually re-explaining it and describe only execution choices that materially affected the experiment: query representation/normalization; historical-retrieval configuration; Top-k/fixed-Top-3 construction; candidate-specific documentary association in the actually executed primary path; context construction; the actually executed local model/prompt/generation restrictions; and material software/hardware/runtime conditions only when verified and relevant to reproducibility or interpretation. The subsection must not anticipate performance results.

### 5. Supersession of D-059 and B04 Prompt V01

D-059 improperly narrowed 4.5 to `Historical retrieval configuration and candidate-generation protocol`, contradicting the author-frozen structure. Therefore D-059 is `SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION`, and `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5.md@7a7aef7994c909e1fde6c01fa8dad7c2cb52f525` is `SUPERSEDED / DO_NOT_EXECUTE`. The historical files are retained for traceability and are not silently altered. The only valid B04 execution is under the corrected V02 prompt governed by D-060.

If Prompt V01 has already been sent or started, its output is not eligible for approval as complete B04. It must stop or be reconciled strictly through V02; the historical-retrieval subset is not presumed to cover the complete subsection.

### 6. Mandatory B04 V02 contract

The corrected prompt must explicitly invoke complete `START_HERE.md` onboarding, MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, D-045/D-058/D-060, live SRC-03 and `main`, Structure V02, and canonical V012. It must require cumulative Markdown and DOCX artifacts, actual DOCX handoff to the author, OOXML/comment/tracked-change/render QA, bilingual equivalence, and the complete MWDP checklist. Omission of an accumulated obligation from a block prompt must never again be interpreted as repeal.

### 7. Scientific boundaries for 4.5

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
RESULTS_VALUES_IN_4_5 = NONE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 8. Post-decision state

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_CORRECTED_DRAFTING
NEXT_ACTOR = DRAFTING_AI
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V02.md
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V02_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```