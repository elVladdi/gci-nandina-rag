# D-080 — Autorización de ejecución B07 / Section 4.8 / B07 Section 4.8 execution authorization

## Español

```text
DECISION_ID = D-080
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-079
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
AUTHORIZED_PROMPT_GIT_BLOB = 9955ea1617b0b13ceeadc83f357dc982eba313ef
PROMPT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_PROMPT_INTERNAL_REVIEW_V01.md@3b142e106ac167fd1f43edeecc5d9340025bed48
PROMPT_REVIEW_RESULT = PASS
B07_STATE = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B07_V01_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Autorización

Después de verificar la integración byte-exacta de B06 en V015, sincronizar el ground truth de reproducibilidad mediante D-079 y obtener `PASS` en la revisión independiente del prompt B07 V01, se autoriza exclusivamente la ejecución de Section 4.8 bajo el contrato identificado arriba.

Ningún otro prompt B07 queda autorizado de forma concurrente.

## 2. Baselines obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V015.md
BASELINE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
BASELINE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
BASELINE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

No se permite usar un Word anterior ni reconstruir el DOCX desde Markdown.

## 3. Frontera científica específica

B07 debe describir el estado real del paquete de reproducibilidad público, no el estado aspiracional de una futura release. Debe distinguir:

- recursos/documentación actualmente materializados;
- componentes objetivo todavía no materializados;
- entradas restringidas o no redistribuidas.

La configurabilidad del framework permanece como propiedad de diseño y no como demostración de generalización empírica.

## 4. Estado de salida esperado

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B07_SECTION_4_8_PROMPT_V01
EXPECTED_SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B07_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
EXPECTED_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V01.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
```

B07 debe volver a IA Gestora para auditoría independiente. Esta decisión no abre Results, Discussion ni Conclusion.

---

## English

```text
DECISION_ID = D-080
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-079
BLOCK = EXPERIMENTAL_DESIGN_B07_SECTION_4_8
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
AUTHORIZED_PROMPT_GIT_BLOB = 9955ea1617b0b13ceeadc83f357dc982eba313ef
PROMPT_REVIEW_RESULT = PASS
B07_STATE = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B07_V01_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
```

B07 execution is authorized only under the independently reviewed V01 prompt. The exact V015 Markdown and B06 V02 DOCX are the sole cumulative baselines.

Section 4.8 must describe the verified current state of the public reproducibility package, explicitly separating resources already materialized, planned/not-yet-materialized components, and restricted/non-redistributed inputs. No unsupported claim of complete computational reproduction or empirical generalization is permitted.

The resulting B07 candidates and response must return to the Managing AI for independent audit. Results and later sections remain closed.