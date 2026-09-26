# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-062
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
CURRENT_AUTHORIZED_BLOCK = EXPERIMENTAL_DESIGN_B04_SECTION_4_5
AUTHORIZED_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V03_ONLY
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica interna de gobernanza. Cada bloque parte del último master integrado y solo se vuelve canónico después de los gates de auditoría, corrección, aprobación e integración aplicables.

La redacción se rige por `KBS_EWG_34_V01`, MWDP v1.0, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, decisiones activas y fuentes experimentales gobernantes para todo hecho empírico.

## 2. Principios científicos y editoriales vinculantes

- El artículo no es una versión abreviada de la tesis.
- Secuencia narrativa: problema/posicionamiento → arquitectura general → instanciación experimental → resultados → interpretación.
- El objeto general es un **framework configurable para apoyo auditable a la clasificación arancelaria**.
- Section 3 es el núcleo técnico del framework.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de la etapa documental y generativa.
- La evidencia documental/normativa se asocia a candidatos ya fijados y no cambia composición ni orden.
- El LLM local opera downstream para explicación controlada; no clasifica desde cero ni retroalimenta el ranking.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary/normative association ≠ substantive normative correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de análisis; DAM/declaración es unidad de agrupamiento cuando la dependencia sea metodológicamente relevante.
- EXP11A expresa sensibilidad conjunta tamaño/composición, no efecto causal aislado del tamaño.
- EXP11B es descriptivo y no autoriza inferencia a una superpoblación de seeds.
- EXP12 no permite estimar el efecto de diversidad histórica bajo el diseño congelado.
- Toda afirmación científica debe ser autorizada y trazable.
- Part I es el manuscript principal en inglés; Part II es el espejo español de control semántico.
- Las abstracciones deben traducirse a componentes, entradas, acciones, salidas y restricciones observables.
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen vinculantes.

### 2.1 Regla específica de Methods

Methods describe objetos científicos, procedencia, procedimientos, decisiones de diseño, ejecución, protocolos de evaluación y controles de validez. La identidad técnica exhaustiva de artefactos pertenece a manifiestos y recursos de reproducibilidad salvo necesidad metodológica concreta. La prosa principal no se organiza alrededor de hashes, rutas internas o inventarios de archivos.

## 3. Estructura acumulativa

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion + Limitations
7. Conclusion
8. KBS end matter

La estructura detallada gobernante es `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`, aprobada mediante D-045.

### 3.1 Section 4 aprobada

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

## 4. Política del master acumulativo y DOCX

1. Cada bloque parte del último master aprobado e integrado.
2. Master Markdown canónico vigente: `ARTICLE_MASTER_V012.md`, SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`, Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`.
3. DOCX acumulativo vigente: `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`, custodia local del autor, SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, 40 comentarios heredados y 0 tracked changes.
4. D-021/D-027 gobiernan custodia y entrega efectiva del binario; D-035 gobierna handoff timeout-safe.
5. No se reconstruye DOCX desde Markdown ni desde un Word anterior.
6. No se usa Base64 manual, chunking, recomposición ni workarounds prohibidos.
7. Los bloques nuevos preservan secciones, comentarios, estilos semánticos, tablas y captions aprobados salvo reapertura explícita.
8. MWDP v1.0 es acumulativo; ausencia de una regla en un prompt no la deroga.

## 5. Estado de fases y bloques

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Structure V02 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work 2.1–2.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction B01 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Experimental Design B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Experimental Design B02 / 4.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Experimental Design B03 / 4.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Canonical master | `ARTICLE_MASTER_V012.md` |
| Experimental Design B04 / 4.5 | **OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V03_ONLY** |
| Sections 4.6–4.8 | NOT_AUTHORIZED |
| Experimental figures/captions from Group 6 | CLOSED / APPROVED externally; EDITORIAL_INTEGRATION_DEFERRED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

## 6. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED; Section 4 amended by D-045 |
| 2 | Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 3 | Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4 | Decision-support architecture | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5A | 4.1 + 4.2.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5B | 4.3 Documentary corpus and evidence resource | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5C | 4.4 Partition validity and dependence controls | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5D | 4.5 Experimental system configuration and execution | **ACTIVE / AUTHORIZED UNDER PROMPT V03** |
| 5E | 4.6 Evaluation framework and protocols | NOT_AUTHORIZED |
| 5F | 4.7 Statistical and robustness analysis | NOT_AUTHORIZED |
| 5G | 4.8 Reproducibility resources | NOT_AUTHORIZED |
| 6 | Results provisional | Experimental Design sufficiently stable + editorial gate + consumable evidence |
| 7 | Integración editorial de figuras experimentales aprobadas | solo cuando Results/material secundario correspondiente esté abierto |
| 8 | Final Results | Results provisional + recursos autorizados + auditoría editorial |
| 9 | Discussion + Limitations | final Results + authorized literature contrast |
| 10 | Conclusion | Discussion closed |
| 11 | Abstract | complete manuscript |
| 12 | Title + Keywords | Abstract/manuscript complete |
| 13 | Transversal synchronization | according to live external dependencies |
| 14 | Scientific audit/freeze | after synchronization and required audits |
| 15 | Final KBS adaptation | scientific freeze + current submission requirements |

## 7. Concurrencia con el proceso experimental

Solo la IA Experimental administra `SRC-03` y el Plan Maestro experimental. La IA Gestora y la IA de Redacción los consultan en solo lectura.

Antes de cada bloque que dependa de hechos experimentales se consulta la rama viva `docs/plan-maestro-temporal-2026-08-31` y se determina si cualquier drift altera materialmente los hechos consumidos.

Último corte sincronizado registrado por el artículo:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
GROUP6 = CLOSED / APPROVED
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

El avance externo no modifica automáticamente el gate editorial local.

## 8. Fase activa — B04 / Section 4.5

### 8.1 Contrato vigente

Solo es ejecutable:

`article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035`

Git blob:

`6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36`

La revisión interna del prompt emitió `PASS` en `article/reviews/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_PROMPT_V03_INTERNAL_REVIEW_V01.md@f19f2005d6de7b83b649677a7d29ca384765b54b` y D-062 autorizó la ejecución.

V01 y V02 permanecen históricos y no ejecutables.

### 8.2 Función narrativa

4.5 debe instanciar Section 3 y describir elecciones de ejecución materialmente relevantes:

1. representación/normalización de consulta;
2. configuración de recuperación histórica;
3. Top-k y fixed Top-3;
4. asociación documental específica por candidato;
5. construcción del contexto;
6. modelo local, prompt/configuración y restricciones de generación;
7. software/hardware/runtime solo cuando estén verificados y sean relevantes.

No debe anticipar métricas observadas de desempeño ni convertirse en inventario técnico del repositorio.

### 8.3 Entregables obligatorios

B04 debe producir exactamente:

- `article/sections/experimental_design/Experimental_Design_B04_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V01.docx`;
- `article/responses/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_RESPONSE_V01.md`.

El DOCX es obligatorio, parte exclusivamente del B03 exacto y debe ser entregado efectivamente al autor.

## 9. Ciclo obligatorio

```text
IA Gestora reconstruye estado/evidencia
→ abre/versiona bloque y prompt cerrado
→ IA de Redacción ejecuta solo el bloque
→ entrega artefactos y response versionada
→ IA Gestora audita independientemente claim por claim
→ IA Experimental revisa solo si existe trigger material
→ corrección si corresponde
→ PASS
→ aprobación expresa del autor cuando aplique
→ IA Gestora integra/promueve técnicamente
→ abre el siguiente gate solo si queda habilitado
```

## 10. Estado inmediato

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B04_SECTION_4_5_PROMPT_V03
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md
PROMPT_COMMIT = 36f0093f0cdfbd78560f7af6a9e25be6e1f67035
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
PRIOR_CITATION_COMMENTS = 40 / PRESERVE
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Purpose

Manage iterative construction of the main scientific article without anticipating Results, altering the approved experimental design, or transferring internal governance logic into publication prose. Each block starts from the latest integrated master and becomes canonical only after all applicable audit, correction, approval, and integration gates.

Drafting is governed by `KBS_EWG_34_V01`, MWDP v1.0, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, active decisions, and governing experimental sources for every empirical fact.

## 2. Binding scientific and editorial principles

The article remains a configurable-framework paper whose Section-3 architecture is the technical core. Historical retrieval generates and orders candidates; the Top-3 is frozen before documentary/generative stages; documentary evidence does not rerank; the local LLM is downstream explanation only. Candidate retrieval is not global accuracy; normative association is not substantive correctness; auditability is not legal correctness; configurability is not empirical generalization. SERIE remains the analysis unit and DAM/declaration the grouping unit where dependence matters. EXP11A/EXP11B/EXP12 retain their frozen interpretations. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED`.

## 3. Governing structure

The detailed governing structure remains `KBS_ARTICLE_WORKING_STRUCTURE_V02.md` with Section 4 organized as 4.1 setting/scope, 4.2 historical data/dataset construction, 4.3 documentary corpus, 4.4 partition validity, 4.5 experimental system configuration and execution, 4.6 evaluation framework/protocols, 4.7 statistical/robustness analysis, and 4.8 reproducibility resources.

## 4. Cumulative master policy

Canonical Markdown is `ARTICLE_MASTER_V012.md` at SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`, blob `dfea73f5f462fc65cf98347f796deadc6da58455`. The current cumulative Word baseline is `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx` at SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, in author custody, with 40 inherited comments and zero tracked changes. DOCX reconstruction is prohibited; D-021/D-027/D-035 and MWDP remain binding.

## 5. Phase state

B01, B02/4.3, and B03/4.4 are closed, approved, frozen, and integrated. B04/4.5 is **OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_V03_ONLY**. Sections 4.6–4.8, Results, Discussion, and Conclusion remain unauthorized.

## 6. Drafting order

The active step is Phase 5D / Section 4.5. Phase 5E/4.6 and later phases remain closed. Group-6 figures remain externally approved resources whose editorial insertion is deferred until the corresponding Results/secondary-material gate opens.

## 7. Experimental concurrency

Only the Experimental AI manages SRC-03 and the experimental Master Plan. The Managing and Drafting AIs read them only. The Drafting AI must re-read live SRC-03/main for B04 and assess whether any drift materially changes the consumed facts; external progress does not automatically alter the editorial gate.

## 8. Active phase — B04 / Section 4.5

The only executable contract is `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md@36f0093f0cdfbd78560f7af6a9e25be6e1f67035`, blob `6f7d7c76abbdc8c25e8bb2e51e072952b0feaf36`. Its internal review at `f19f2005d6de7b83b649677a7d29ca384765b54b` returned `PASS`, and D-062 authorized execution. V01/V02 remain historical and non-executable.

Section 4.5 instantiates Section 3 and reports materially relevant execution choices: query representation/normalization, historical retrieval, Top-k/fixed Top-3 construction, candidate-specific documentary association, context construction, local model/prompt/generation restrictions, and verified material software/hardware/runtime conditions. Observed performance values remain outside 4.5.

Mandatory deliverables are the versioned B04 block, cumulative candidate Markdown master, cumulative candidate DOCX master, and bilingual versioned response. The DOCX must derive only from the exact B03 binary and must actually be handed to the author.

## 9. Mandatory cycle

```text
Managing AI reconstructs state/evidence
→ versions a closed block prompt
→ Drafting AI executes only that block
→ delivers artifacts and versioned response
→ Managing AI independently audits claims, scope, bilingual equivalence, Word, comments, and versioning
→ Experimental AI reviews only when a material trigger exists
→ corrections if required
→ PASS
→ explicit author approval when applicable
→ Managing AI integrates/promotes
→ next gate opens only if authorized
```

## 10. Immediate state

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B04_SECTION_4_5_DRAFTING_V03
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ONLY_B04_SECTION_4_5_PROMPT_V03
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5_V03.md
PROMPT_COMMIT = 36f0093f0cdfbd78560f7af6a9e25be6e1f67035
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
PRIOR_CITATION_COMMENTS = 40 / PRESERVE
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```