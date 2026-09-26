# Revisión interna del prompt — Experimental Design B05 / Section 4.6 — V01

## Español

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B05_SECTION4_6_PROMPT_INTERNAL_REVIEW_V01
DATE = 2026-09-26
ROLE = IA_GESTORA
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99
PROMPT_GIT_BLOB = 55108c6628da436c601b8a69a8397c32b2c0589d
PARENT_DECISION = D-067
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
REVIEW_RESULT = PASS
CORRECTION_REQUIRED = NO
EXECUTION_AUTHORIZATION = MAY_BE_ISSUED_BY_SEPARATE_DECISION
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

### 1. Onboarding y gobernanza

El prompt reproduce exactamente el orden obligatorio de `START_HERE.md`:

`START_HERE → README → ARTICLE_STATUS → ARTICLE_WRITING_PLAN → DECISIONS → SOURCE_REGISTRY → CLAIM_EVIDENCE_MATRIX → STYLE_GUIDE → prompt específico`.

Después invoca MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-066, D-067, Structure V02 y V013. La continuidad Markdown/DOCX es obligatoria y no condicional.

### 2. Baselines

El contrato fija correctamente:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
BASELINE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx
BASELINE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
```

El master canónico V013 contiene placeholders explícitos para 4.6, 4.6.1, 4.6.2 y 4.6.3 y conserva 4.7 como frontera posterior. Por tanto, el diferencial exigido es ejecutable sin reconstrucción del manuscrito.

### 3. Alcance científico

El prompt preserva la función congelada de 4.6 y mapea correctamente:

- RQ1 → candidate retrieval;
- RQ2 → documentary evidence;
- RQ3 → controlled explanation;
- RQ4 → límite de validez/robustez, sin invadir 4.7.

No reduce 4.6 a una sola función y no reabre 4.5.

### 4. Candidate-retrieval evaluation

La especificación coincide con el contrato analítico congelado:

- SERIE como unidad primaria;
- Top-1, Top-3, Top-5, Top-10 y MRR@100 como métricas primarias HE2_A;
- Top-50 como suplementaria;
- familias comparables flat, hierarchical y D1a corregidas;
- deep coverage/HE2_B separado del early ranking;
- Phase-E pools como cobertura descriptiva;
- inferencia/robustez reservada principalmente para 4.7.

La frontera `candidate retrieval ≠ overall classification accuracy` está explícita.

### 5. Documentary-evidence evaluation

El contrato refleja la ruta Phase F real: Top-3 histórico fijo como entrada, asociación por candidato, exact NANDINA-8 distinguido de contexto parental, precedente histórico, trazabilidad e invariancia del Top-3. Además prohíbe convertir cobertura/asociación en substantive normative/legal correctness y prohíbe narrar resultados observados como 3,168/3,168 o tasas empíricas.

### 6. Controlled-explanation evaluation

El prompt distingue correctamente:

1. controles automáticos estructurales/trazabilidad de Gate J;
2. evaluación cualitativa congelada de Gate K.

Preserva las ocho dimensiones 0–2, umbral `>=12/16` sin hard violation, hard constraints, exclusión de `advertencias_globales` y diseño de muestra de 50 casos.

La limitación metodológica crítica está expresamente protegida: la modalidad efectiva fue `AI_EXPERT_ROLE / LLM-as-judge`, `human_scoring=false`, con desviación frente al plan humano/manual original. No permite describirla como validación humana.

### 7. Control de leakage entre Methods y Results

El prompt prohíbe:

- resultados Top-k/MRR;
- resultados de cobertura/invariancia;
- scores y tasas HE4;
- decisiones HE2/HE5;
- inferencia/intervalos/p-values;
- resultados de sensibilidad;
- literatura/Discussion;
- novelty/final gap.

El límite con 4.7 y Results es suficientemente explícito.

### 8. Continuidad documental y QA

Se exige:

- master Markdown candidato acumulativo desde V013 exacto;
- DOCX candidato acumulativo desde el Word B04 V02 exacto;
- solo sustitución de placeholders 4.6–4.6.3 EN/ES;
- preservación 1–4.5 y 4.7+;
- 40 comment starts/ends/references;
- tracked changes = 0;
- OOXML/XML/RELS QA;
- equivalencia MD/DOCX y EN/ES;
- render completo;
- handoff real del DOCX al autor bajo custodia local.

### 9. Dictamen

No se identificó contradicción científica, omisión de continuidad DOCX, defecto de onboarding, leakage de Results ni expansión de alcance que requiera corrección.

```text
PROMPT_SCIENTIFIC_SCOPE = PASS
SOURCE_GROUNDING = PASS
RQ_MAPPING = PASS
RESULTS_BOUNDARY = PASS
SECTION_4_7_BOUNDARY = PASS
BILINGUAL_CONTRACT = PASS
DOCX_CONTINUITY = PASS
QA_CONTRACT = PASS
OVERALL = PASS
```

---

## English

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B05_SECTION4_6_PROMPT_INTERNAL_REVIEW_V01
DATE = 2026-09-26
ROLE = MANAGING_AI
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99
PROMPT_GIT_BLOB = 55108c6628da436c601b8a69a8397c32b2c0589d
PARENT_DECISION = D-067
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
REVIEW_RESULT = PASS
CORRECTION_REQUIRED = NO
EXECUTION_AUTHORIZATION = MAY_BE_ISSUED_BY_SEPARATE_DECISION
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

The prompt uses the exact mandatory onboarding sequence, binds MWDP/SPCCR and the applicable decisions, and makes cumulative Markdown and DOCX continuity mandatory. Its exact baselines are canonical V013 and the approved B04 V02 Word binary.

The scientific scope correctly covers the full Section 4.6 hierarchy and maps RQ1 to candidate retrieval, RQ2 to documentary evidence, RQ3 to controlled explanation, and RQ4 only to the validity/robustness boundary handled elsewhere.

Candidate-retrieval definitions match the frozen Group-3 contract; documentary-evidence evaluation reflects the actual fixed-Top-3 Phase-F association protocol without converting coverage into legal correctness; and controlled-explanation evaluation correctly separates automatic checks from the frozen qualitative rubric, including the actual AI-expert/LLM-as-judge evaluator modality and its deviation from the originally planned human/manual review.

Observed outcomes, hypothesis dispositions, inference, sensitivity results, Section 4.7 content, and Results are explicitly excluded. The prompt also requires differential Markdown/DOCX preservation, all 40 inherited comments, zero tracked changes, OOXML and rendering QA, semantic equivalence, and actual Word handoff.

```text
PROMPT_SCIENTIFIC_SCOPE = PASS
SOURCE_GROUNDING = PASS
RQ_MAPPING = PASS
RESULTS_BOUNDARY = PASS
SECTION_4_7_BOUNDARY = PASS
BILINGUAL_CONTRACT = PASS
DOCX_CONTINUITY = PASS
QA_CONTRACT = PASS
OVERALL = PASS
```