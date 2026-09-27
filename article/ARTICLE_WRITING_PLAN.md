# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.8
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-080
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V015.md
CANONICAL_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B07_SECTION_4_8_DRAFTING_V01
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B06 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B07 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B07_V01_ONLY
SECTION_4_8 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B07_V01_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política acumulativa

`ARTICLE_MASTER_V015.md` es el master Markdown canónico verificado. El Word acumulativo canónico vigente es `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx`, bajo custodia local del autor.

MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md` y la estructura congelada permanecen vinculantes. Ningún bloque posterior se abre por inferencia ni por mera existencia de artefactos.

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
| B06 / 4.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| ARTICLE_MASTER_V015 | CANONICAL / VERIFIED |
| B07 / 4.8 | OPEN / AUTHORIZED UNDER B07 V01 ONLY |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. Cierre técnico de B06

D-078 verificó que el archivo materializado `ARTICLE_MASTER_V015.md` posee Git blob `e9a17899ccbcb9971e6dfb5002f908e17a0441d9`, exactamente igual al candidato B06 V02 aprobado. Por identidad byte-exacta se conserva el SHA-256 auditado `b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c`.

El baseline Word acumulativo vigente es:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0
```

## 5. Fase activa — B07 / Section 4.8

Ground truth: D-079.

Contrato único ejecutable:

`article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577`

Git blob:

`9955ea1617b0b13ceeadc83f357dc982eba313ef`

Revisión interna:

`article/reviews/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_PROMPT_INTERNAL_REVIEW_V01.md@3b142e106ac167fd1f43edeecc5d9340025bed48` — `PASS`.

Autorización: D-080.

### 5.1 Función científica

Section 4.8 debe explicar los recursos de reproducibilidad verificables sin equiparar documentación con reproducción computacional ya demostrada. Debe distinguir de forma explícita:

1. recursos públicos actualmente materializados;
2. componentes planificados/no materializados de la futura release de referencia;
3. entradas restringidas o no redistribuidas.

La prosa debe explicar capacidades y fronteras, no inventariar hashes/rutas internas.

### 5.2 Snapshot público de reproducibilidad

```text
REPRO_REPOSITORY = elVladdi/gci-nandina-rag-reproducibility
REPRO_MAIN_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
REPRO_PACKAGE_STATUS = DOCUMENTED_SCAFFOLD / NOT_FULL_REFERENCE_RELEASE
```

El snapshot sí contiene documentación de protocolo, contratos de datos/procedencia/taxonomía, reglas de reproducibilidad y una configuración de ejemplo para datos propios. No contiene todavía runner canónico de reproducción, runners ejecutables mostrados como interfaz objetivo, preset Clase-87 congelado, dependency lock, resultados canónicos, datos administrativos de referencia redistribuidos ni validación clean-environment de la release final.

### 5.3 Claims

- C15: configurabilidad para otros capítulos/niveles/jurisdicciones — autorizada solo como propiedad de diseño.
- C17: separación entre reproducción de referencia y replicación externa — autorizada.
- C16: generalización empírica fuera de Chapter 87 — prohibida.

La reproducibilidad/documentación no autoriza claims de corrección jurídica, generalización empírica ni disponibilidad pública de datos no verificada.

### 5.4 Recheck obligatorio

Debido al carácter progresivo del repositorio de reproducibilidad, el estado público deberá re-verificarse antes del freeze final/submission. Cualquier recurso nuevo se incorporará mediante un nuevo gate; B07 V01 no debe anticiparlo.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B07_SECTION_4_8_PROMPT_V01
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V015.md
BASELINE_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
BASELINE_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Current cumulative state

`ARTICLE_MASTER_V015.md` is the verified canonical Markdown master. `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx` is the cumulative Word baseline in local author custody. B01–B06 are closed, approved, frozen, and integrated.

B07 / Section 4.8 is open only under `article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577`, which passed independent prompt review and was authorized by D-080.

## 2. B07 scientific function and source boundary

Section 4.8 must describe verified reproducibility resources while distinguishing materialized public resources, planned/not-yet-materialized reference-release components, and restricted/non-redistributed inputs.

The audited public snapshot is `gci-nandina-rag-reproducibility@254831cd955103faa2517065a7eed7fb340bbccc`, tree `078a85255fa1f3234b4f7ed51ef2660b903d486e`. It provides protocol/data/provenance/taxonomy documentation and an example custom-data configuration, but it is not yet a complete runnable reference release.

Reference reproduction and external replication must remain distinct. Configurability is a design property, not evidence of empirical generalization. The public-resource state must be rechecked before final freeze/submission.

## 3. Gate

```text
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
CURRENT_GATE = EXPERIMENTAL_DESIGN_B07_SECTION_4_8_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```