# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.7
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-077
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V014.md
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V015
APPROVED_B06_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
APPROVED_B06_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
APPROVED_B06_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = B06_V015_PROMOTION_PENDING
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B06 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_7 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
AUTHOR_APPROVAL_GATE = SATISFIED
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

El artículo continúa construyéndose mediante masters acumulativos verificados. Mientras la promoción B06 no esté materializada y auditada, `ARTICLE_MASTER_V014.md` permanece como master Markdown canónico y `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx` como Word acumulativo canónico bajo custodia local del autor.

MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` siguen siendo vinculantes. Ningún bloque se integra por aprobación implícita y ninguna sección posterior se abre antes de cerrar el gate técnico precedente.

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
| B06 / 4.7 | CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION |
| ARTICLE_MASTER_V015 | AUTHORIZED / PENDING MATERIALIZATION AND VERIFICATION |
| 4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. Cierre B06

B06 V01 fue auditado con `PASS WITH CORRECTIONS`. D-074 definió un microgate estrecho B06-C01–B06-C04 y D-075 autorizó su ejecución. B06 V02 fue auditado en:

`article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V02.md@5f154e54faf5b59f301bbb07787616468304a04b` — `PASS`.

D-076 abrió exclusivamente el gate de aprobación autoral. El autor aprobó B06 V02 sin cambios y D-077 registra la aprobación y autoriza la promoción a V015.

### 4.1 Identidades aprobadas

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9

ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES
VISUAL_QA = PASS
```

### 4.2 Estado científico congelado

Section 4.7 conserva el estimando ponderado por series y la dependencia por DAM, bootstrap pareado por cluster con 10.000 réplicas y seed 20263001, matriz común `10000 × 67`, reglas de multiplicidad, control Bonferroni para HE2_A, Top-50 suplementaria con IC 95%, un único contraste HE2_B, ausencia de p-values y medida de efecto pareada no estandarizada. EXP11A, EXP11B, EXP12 y HE5 mantienen exactamente sus fronteras descriptivas/no estimables congeladas. No se introducen Results ni disposiciones HE2/HE5 en Methods.

## 5. Gate de promoción V015

La única acción de integración autorizada es promover byte-exactamente:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
TARGET = article/manuscript/ARTICLE_MASTER_V015.md
EXPECTED_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
EXPECTED_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
```

Después de materializar V015, IA Gestora debe verificar su identidad antes de declarar B06 integrado. El DOCX B06 V02 permanece bajo custodia local del autor y solo se convierte en baseline Word canónico después de la promoción verificada.

## 6. Próxima fase

Section 4.8 no está autorizada todavía. Una vez verificada V015, el siguiente trabajo posible será preparar B07 / Section 4.8 — Reproducibility resources, pero solo después de:

- sincronizar su ground truth con el repositorio de reproducibilidad y las fuentes vigentes;
- distinguir recursos públicos, restringidos y no redistribuibles;
- verificar qué permite reconstruir/reproducir el paquete y qué requiere datos externos del replicador;
- preparar un prompt específico bajo MWDP/SPCCR;
- auditar ese prompt independientemente;
- emitir una autorización editorial específica.

No debe redactarse Section 4.8 antes de ese gate.

```text
NEXT_ACTOR = AUTHOR / REPOSITORY_MATERIALIZATION
NEXT_ACTION = MATERIALIZE_APPROVED_B06_V02_MD_AS_ARTICLE_MASTER_V015_AND_RETURN_FOR_VERIFICATION
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Current cumulative state

B01–B05 are closed, approved, frozen, and integrated. B06 V02 passed the independent Managing-AI audit and has now been explicitly approved by the author without changes.

D-077 freezes the approved B06 V02 identities and authorizes promotion to `ARTICLE_MASTER_V015.md`. Until that promotion is materialized and verified, V014 remains the canonical Markdown master and the approved B05 V01 DOCX remains the canonical cumulative Word baseline.

## 2. Approved B06 identities

```text
APPROVED_B06_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
APPROVED_B06_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
APPROVED_B06_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

## 3. Promotion gate

The only authorized integration action is byte-exact promotion of the approved B06 V02 Markdown candidate to:

```text
article/manuscript/ARTICLE_MASTER_V015.md
EXPECTED_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
EXPECTED_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
```

Managing-AI verification is required after materialization before B06 can be marked integrated and before the B06 V02 DOCX becomes the canonical cumulative Word baseline.

## 4. Next block boundary

Section 4.8 remains closed. After V015 verification, B07 / Section 4.8 may be prepared only through its own ground-truth synchronization, MWDP/SPCCR drafting contract, independent prompt review, and explicit authorization. Results, Discussion, and Conclusion remain unauthorized.

```text
CURRENT_GATE = B06_V015_PROMOTION_PENDING
NEXT_ACTOR = AUTHOR / REPOSITORY_MATERIALIZATION
NEXT_ACTION = MATERIALIZE_APPROVED_B06_V02_MD_AS_ARTICLE_MASTER_V015_AND_RETURN_FOR_VERIFICATION
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
