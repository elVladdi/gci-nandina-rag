# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.5
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-075
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V014.md
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B06_NARROW_CORRECTION_V01
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B06 = REVISION_REQUIRED / NARROW_CORRECTION_AUTHORIZED
SECTION_4_7_SCIENTIFIC_CORE = PASS
SECTION_4_7_MD_DOCX_CONTINUITY = PASS
AUTHOR_APPROVAL_GATE = NOT_OPEN
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

`ARTICLE_MASTER_V014.md` permanece como master Markdown canónico verificado. El Word canónico vigente sigue siendo `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx` bajo custodia local del autor hasta que B06 supere corrección, auditoría y aprobación autoral.

MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` siguen siendo vinculantes. No se reconstruyen masters acumulativos, no se sustituyen baselines exactos y ningún PASS científico abre por sí mismo integración ni el siguiente bloque.

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
| B06 / 4.7 | REVISION_REQUIRED / NARROW_CORRECTION_AUTHORIZED |
| 4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. B06 V01 — auditoría independiente

Contrato inicial ejecutado:

`article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf`

Response recibida:

`article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V01.md@fc08bee93556809171262b6ab56b4124c30d0867`

Auditoría Gestora:

`article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V01.md@3d19fbb47fd48abe15520264eea3b29969084295` — `PASS WITH CORRECTIONS`.

El núcleo científico, el alcance, la equivalencia EN/ES y la continuidad MD/DOCX pasan. La revisión no requiere rehacer B06 desde cero.

## 5. Corrección estrecha autorizada

D-074 define cuatro incidencias y prohíbe cualquier expansión del alcance:

- **B06-C01:** 67 clusters DAM, matriz común `10000 × 67` y multiplicidad `m` de todas las series de una DAM remuestreada;
- **B06-C02:** Top-50 con IC percentil bilateral 95% y efecto congelado como diferencia pareada no estandarizada, sin efecto estandarizado post hoc;
- **B06-C03:** reglas HE5 omitidas sobre no estimabilidad de calidad de descripción, proximidad jerárquica descriptiva y buckets literales de soporte histórico sin threshold de insuficiencia;
- **B06-C04:** corrección de dos blobs de procedencia en la response.

Contrato correctivo único:

`article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547`

Git blob:

`90592518a2197ee6a7889797bf43da60b8b06fcf`

Revisión del prompt:

`article/reviews/5_EXPERIMENTAL_DESIGN_B06_NARROW_METHODS_CORRECTION_PROMPT_REVIEW_V01.md@024fa0eb8a47425c49241ac0db4bd929bcfbf202` — `PASS`.

Autorización: D-075.

## 6. Baselines exactos del microgate

La corrección debe editar exclusivamente los candidatos B06 V01 ya auditados:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Está prohibido volver a V014/B05 como baseline de edición o reconstruir el Word desde Markdown.

## 7. Fuentes verificadas para la corrección

```text
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
G3_ANALYTICAL_CONTRACT_BLOB = 76862c10fd84fd70588da2d65f96dbe3b40914f6
G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
G3_INFERENTIAL_RESULTS_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
```

La matriz claim–evidencia vigente mantiene C08, C26 y C27 como `AUTHORIZED` dentro de sus límites descriptivos. C14 continúa `CONDITIONAL`, pero no es el claim que gobierna las correcciones B06-C01–C03.

## 8. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B06_V01_NARROW_METHODS_CORRECTION
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
EXPECTED_SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V02.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
EXPECTED_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Current cumulative state

`ARTICLE_MASTER_V014.md` remains the verified canonical Markdown master, and the approved B05 V01 DOCX remains the canonical cumulative Word baseline in local author custody. B01–B05 are closed, approved, frozen, and integrated.

B06 V01 passed scientific-core, scope, bilingual-equivalence, Markdown-continuity, and DOCX/OOXML checks, but independent review returned `PASS WITH CORRECTIONS`. No full rewrite is required.

## 2. Authorized narrow correction

D-074 restricts the revision to B06-C01 through B06-C04. The sole executable corrective contract is:

`article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547`

with Git blob `90592518a2197ee6a7889797bf43da60b8b06fcf`. Its independent prompt review passed, and D-075 authorizes execution.

The correction must use the exact B06 V01 candidates as editing baselines:

```text
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Returning to V014/B05 as an editing baseline or reconstructing the DOCX from Markdown is prohibited.

## 3. Gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B06_NARROW_CORRECTION_V01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ONLY_B06_V01_NARROW_METHODS_CORRECTION
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

A corrected B06 V02 must return to the Managing AI for differential audit before any author-approval gate can open.