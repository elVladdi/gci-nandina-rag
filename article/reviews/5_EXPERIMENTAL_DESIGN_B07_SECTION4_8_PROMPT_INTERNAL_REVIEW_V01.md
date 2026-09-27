# Revisión interna del prompt — Experimental Design B07 / Section 4.8 — V01

## Español

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B07_SECTION4_8_PROMPT_INTERNAL_REVIEW_V01
DATE = 2026-09-27
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
PROMPT_GIT_BLOB = 9955ea1617b0b13ceeadc83f357dc982eba313ef
GROUND_TRUTH = article/governance/D079_EXPERIMENTAL_DESIGN_B07_SECTION4_8_GROUND_TRUTH_SYNC.md@448bcb179cc2be0e211af26fadf77912c3d04056
VERDICT = PASS
```

## 1. Alcance

Se auditó el contrato B07 V01 antes de autorizar su ejecución. La revisión verificó onboarding, baselines acumulativos, MWDP/SPCCR, fuentes públicas vivas, control de overclaiming, fronteras de reproducibilidad, entregables y continuidad DOCX.

## 2. Onboarding y protocolos

**PASS.** El prompt reproduce exactamente el orden de lectura requerido por `START_HERE.md`: START_HERE → README → ARTICLE_STATUS → ARTICLE_WRITING_PLAN → DECISIONS → SOURCE_REGISTRY → CLAIM_EVIDENCE_MATRIX → STYLE_GUIDE → prompt específico.

Invoca expresamente MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-078 y D-079. No deroga reglas acumulativas por omisión.

## 3. Baselines

**PASS.** Los baselines son los únicos correctos después de la integración B06:

```text
ARTICLE_MASTER_V015.md
SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9

ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40
TRACKED_CHANGES = 0
```

El prompt prohíbe reconstrucción del DOCX y exige stop explícito ante ausencia o hash incorrecto.

## 4. Ground truth del repositorio de reproducibilidad

**PASS.** El prompt exige re-verificación viva del repositorio público y fija el snapshot auditado:

```text
REPRO_MAIN_HEAD = 254831cd955103faa2517065a7eed7fb340bbccc
REPRO_TREE = 078a85255fa1f3234b4f7ed51ef2660b903d486e
```

Exige distinguir materialización real de recursos planificados. Esta separación es científicamente necesaria porque el snapshot contiene documentación, contratos y configuración de ejemplo, pero no contiene todavía una release de referencia ejecutable completa.

## 5. Overclaiming y claims

**PASS.** El prompt autoriza C15 y C17 dentro de sus límites y prohíbe C16. También prohíbe afirmar:

- one-command/fresh-clone reproduction ya validada;
- preset Clase-87 congelado ya materializado;
- redistribución pública de los datos administrativos;
- release estable/final;
- clean-environment validation ya ejecutada;
- generalización empírica derivada de configurabilidad o reproducibilidad.

La distinción entre documentación/presente, planificado/no materializado y restringido/no redistribuido queda explícita.

## 6. Frontera editorial

**PASS.** Solo Section 4.8 EN/ES puede cambiar. Sections 1–4.7 deben preservarse; Results, Discussion, Conclusion y end matter permanecen fuera de alcance. `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` se conservan.

## 7. Entregables y MWDP

**PASS.** El prompt exige cuatro entregables, continuidad acumulativa MD/DOCX, preservación de 40 comentarios, 0 tracked changes, QA OOXML, render completo, equivalencia EN/ES, control de diferencias, word count y checklist MWDP.

## 8. Dictamen

No se detectan defectos de alcance, procedencia, baseline, onboarding, claims, continuidad Word ni overclaiming que impidan ejecución.

```text
VERDICT = PASS
B07_PROMPT = READY_FOR_EXECUTION_AUTHORIZATION
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B07_SECTION4_8_PROMPT_INTERNAL_REVIEW_V01
DATE = 2026-09-27
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8.md@bb3b6792f2eb79e6461ea3b4b4c55369e6dbf577
PROMPT_GIT_BLOB = 9955ea1617b0b13ceeadc83f357dc982eba313ef
GROUND_TRUTH = article/governance/D079_EXPERIMENTAL_DESIGN_B07_SECTION4_8_GROUND_TRUTH_SYNC.md@448bcb179cc2be0e211af26fadf77912c3d04056
VERDICT = PASS
```

The B07 V01 drafting contract correctly reproduces the mandatory START_HERE onboarding order, invokes MWDP/SPCCR and cumulative DOCX controls, uses the exact V015/B06-V02 baselines, and requires live verification of the public reproducibility repository.

The prompt accurately distinguishes currently materialized public resources from target/planned release components and restricted/non-redistributed inputs. It prevents unsupported claims of complete one-command reproduction, a frozen Class-87 preset, public administrative reference data, clean-environment validation, stable final release, or empirical generalization.

Only Section 4.8 EN/ES may change. Prior Methods content and all later manuscript sections remain frozen. Required deliverables and QA are complete and compatible with MWDP.

```text
VERDICT = PASS
B07_PROMPT = READY_FOR_EXECUTION_AUTHORIZATION
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS = NOT_AUTHORIZED
```