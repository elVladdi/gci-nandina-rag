# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-073
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V014.md
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B06_SECTION_4_7_DRAFTING_V01
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = CLOSED / APPROVED / FROZEN / INTEGRATED
B06 / SECTION_4_7 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B06_V01_ONLY
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política acumulativa

El artículo se construye sobre masters acumulativos. `ARTICLE_MASTER_V014.md` es el master Markdown canónico verificado. El Word acumulativo canónico vigente es `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx`, bajo custodia local del autor.

MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` permanecen vinculantes. No se reconstruyen masters acumulativos ni se alteran bloques aprobados.

## 2. Estructura congelada de Experimental Design

```text
4.1 Experimental setting and scope
4.2 Historical data and experimental dataset construction
  4.2.1 Source and data collection
  4.2.2 Processing and curation
  4.2.3 Partition construction and dataset composition
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

## 3. Estado de construcción

| Bloque | Estado |
|---|---|
| Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B02 / 4.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B03 / 4.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B04 / 4.5 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B05 / 4.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| ARTICLE_MASTER_V014 | CANONICAL / VERIFIED |
| B06 / 4.7 | OPEN / AUTHORIZED UNDER B06 V01 ONLY |
| 4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. Cierre B05 y promoción V014

D-071 verificó que `ARTICLE_MASTER_V014.md` posee Git blob `20105abb745e382b923e4eb43d9a771a722df9e3`, exactamente igual al candidato B05 V01 aprobado. Por identidad byte-exacta se conserva también el SHA-256 auditado `e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97`.

B05 / Section 4.6 queda cerrado, aprobado, congelado e integrado. El baseline Word acumulativo es:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
COMMENTS = 40 / PRESERVE
```

## 5. Fase activa — B06 / Section 4.7

Ground truth: D-072.

Contrato único ejecutable:

`article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf`

Git blob:

`23159f8e85210c78ccfbb2acec4f5b560e83b984`

Revisión interna:

`article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_PROMPT_INTERNAL_REVIEW_V01.md@1ca287f50580c4c023abf959bb47546bf22e3057` — `PASS`.

Autorización: D-073.

### 5.1 Función científica

B06 describe la construcción de la inferencia y los análisis de sensibilidad/robustez sin reportar los valores observados. Debe conservar:

- SERIE como unidad primaria de análisis;
- DAM/declaración como cluster de dependencia;
- estimando pareado ponderado por series;
- remuestreo de DAM completas con todas sus series;
- 10.000 réplicas bootstrap y seed 20263001;
- la misma matriz de DAM remuestreadas para comparaciones pareadas;
- Top-1/3/5/10 + MRR@100 como familia primaria por comparador;
- IC percentil bilateral del 99% con regla Bonferroni FWER 95% dentro de cada familia de cinco métricas;
- Top-50 suplementario con IC 95%;
- un único contraste inferencial deep-coverage `Recall@200 - Recall@100` con IC 95%;
- ausencia de p-values;
- diferencia absoluta pareada como medida de efecto congelada, sin medida estandarizada post hoc.

### 5.2 Sensibilidad y robustez

- H25/H50/H75 vs H100: sensibilidad descriptiva conjunta tamaño/composición; no causalidad aislada del tamaño.
- H150/H200: sensibilidad descriptiva con diez seeds pareados sobre el mismo EVAL; sin inferencia a superpoblación de seeds.
- 0B-05C Attempt06: sensibilidad descriptiva bajo el estado correctivo gobernado.
- Phase-E pools: inventarios descriptivos de cobertura, no rankings alternativos ni inferencia primaria.
- EXP12: diversidad no estimable.
- Descripción ambigua/incompleta: prevalencia no estimable.
- Proximidad jerárquica: categorías descriptivas.
- Soporte histórico: buckets literales `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`, sin umbral post hoc de insuficiencia.

### 5.3 Fronteras

No introducir Results en 4.7: no point estimates, intervalos observados, p-values, disposiciones HE2/HE5, resultados de sensibilidad ni conclusiones de superioridad. El bootstrap describe incertidumbre dentro del benchmark interno Chapter 87 y no autoriza inferencia a población externa.

## 6. Sincronización experimental

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
G3_ANALYTICAL_CONTRACT_BLOB = 76862c10fd84fd70588da2d65f96dbe3b40914f6
G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
```

La IA de Redacción debe re-verificar fuentes vivas antes de ejecutar y detenerse ante drift material.

## 7. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B06_SECTION_4_7_PROMPT_V01
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V014.md
BASELINE_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
BASELINE_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
BASELINE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Current cumulative state

`ARTICLE_MASTER_V014.md` is the verified canonical Markdown master. `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx` is the cumulative Word baseline in local author custody. B01–B05 are closed, approved, frozen, and integrated.

B06 / Section 4.7 is open only under `article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf`, which passed independent prompt review and was authorized by D-073.

## 2. Scientific function and boundaries

Section 4.7 describes inferential, sensitivity, and robustness procedures without observed Results. It preserves the series-weighted estimand, DAM-cluster dependence handling, the frozen 10,000-replicate paired bootstrap with seed 20263001, the comparator-family interval/multiplicity rules, the single deep-coverage contrast, and the frozen descriptive/not-estimable sensitivity statuses.

No observed point estimates, observed intervals, p-values, final HE2/HE5 dispositions, superiority conclusions, external-population inference, causal historical-bank-size claims, seed-superpopulation inference, or standardized post-hoc effect measures belong in this Methods block.

## 3. Exact baselines and gate

```text
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
BASELINE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CURRENT_GATE = EXPERIMENTAL_DESIGN_B06_SECTION_4_7_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```