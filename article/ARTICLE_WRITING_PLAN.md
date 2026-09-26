# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-061
CANONICAL_MASTER = ARTICLE_MASTER_V012
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
CANONICAL_MASTER_MD_SHA256 = d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78
CANONICAL_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
CURRENT_AUTHORIZED_SCIENTIFIC_BLOCK = SECTION_4_5 / ELIGIBLE_BUT_NOT_EXECUTABLE_UNTIL_V03
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = ELIGIBLE / EXECUTION_BLOCKED_UNTIL_B04_PROMPT_V03
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

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica interna de gobernanza. El artículo se construye sobre un master acumulativo; cada bloque autorizado parte del último master integrado y solo se vuelve canónico después de auditoría independiente, correcciones, aprobación autoral cuando corresponda e integración técnica verificada.

La redacción se rige por `KBS_EWG_34_V01`, MWDP v1.0, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, decisiones activas y fuentes experimentales gobernantes para todo hecho empírico.

## 2. Principios científicos y editoriales vinculantes

- El artículo no es una versión abreviada de la tesis.
- Secuencia narrativa: problema/posicionamiento → arquitectura general → instanciación experimental → resultados → interpretación.
- El objeto general es un **framework configurable para apoyo auditable a la clasificación arancelaria**.
- La arquitectura de Section 3 es el núcleo técnico del framework.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de la etapa documental y generativa.
- La evidencia documental/normativa se asocia a candidatos ya fijados y no cambia composición ni orden.
- El LLM local opera downstream para explicación controlada; no clasifica desde cero ni retroalimenta el ranking.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary/normative association ≠ substantive normative correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de análisis; DAM/declaración es unidad de agrupamiento cuando la dependencia entre series es metodológicamente relevante.
- EXP11A expresa sensibilidad conjunta tamaño/composición, no efecto causal aislado del tamaño.
- EXP11B es descriptivo y no autoriza inferencia a una superpoblación de seeds.
- EXP12 no permite estimar el efecto de diversidad histórica bajo el diseño congelado.
- Toda afirmación científica debe ser autorizada y trazable.
- Part I es el manuscript principal en inglés; Part II es el espejo español de control semántico.
- Las abstracciones deben traducirse a componentes, entradas, acciones, salidas y restricciones observables.
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen vinculantes.

### 2.1 Regla específica de Methods

Methods describe objetos científicos, procedencia, procedimientos, decisiones de diseño, ejecución, protocolos de evaluación y controles de validez. La identidad técnica exhaustiva de artefactos pertenece a manifiestos y recursos de reproducibilidad salvo que un identificador concreto sea metodológicamente indispensable.

La prosa principal no se organiza alrededor de SHA-256, rutas internas, nombres físicos de archivos/scripts, nombres de hojas o labels internos de configuración.

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
3. DOCX acumulativo vigente: `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`, custodia local del autor, SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, 40 comentarios heredados y 0 tracked changes en la auditoría aprobada.
4. D-021/D-027 gobiernan custodia local y entrega efectiva del binario; D-035 gobierna handoff timeout-safe.
5. No se reconstruye DOCX desde Markdown ni desde un Word anterior.
6. No se usa Base64 manual, chunking, recomposición ni workarounds de transferencia prohibidos.
7. Los bloques nuevos preservan secciones, comentarios, estilos semánticos, tablas y captions previamente aprobados salvo alcance explícitamente reabierto.
8. Un master candidato no se vuelve canónico hasta superar todos los gates aplicables.
9. MWDP v1.0 es acumulativo: la ausencia de una regla en un prompt específico no la deroga.

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
| Experimental Design B04 / 4.5 | ELIGIBLE / BLOCKED_UNTIL_PROMPT_V03 |
| Sections 4.6–4.8 | NOT_AUTHORIZED |
| Experimental figures/captions from Group 6 | CLOSED / APPROVED externally; EDITORIAL_INTEGRATION_DEFERRED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

Los grupos experimentales no se administran aquí. `SRC-03` se consulta en modo de solo lectura cuando una afirmación o gate editorial depende materialmente de ellos.

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
| 5D | 4.5 Experimental system configuration and execution | NEXT SCIENTIFIC BLOCK / WAITING FOR CORRECTED V03 CONTRACT |
| 5E | 4.6 Evaluation framework and protocols | NOT_AUTHORIZED |
| 5F | 4.7 Statistical and robustness analysis | NOT_AUTHORIZED |
| 5G | 4.8 Reproducibility resources | NOT_AUTHORIZED |
| 6 | Results provisional | Experimental Design sufficiently stable + editorial gate + consumable evidence |
| 7 | Integración editorial de figuras experimentales ya aprobadas | solo cuando Results/material secundario correspondiente esté abierto |
| 8 | Final Results | Results provisional + recursos visuales/tabulares autorizados + auditoría editorial |
| 9 | Discussion + Limitations | final Results + authorized literature contrast |
| 10 | Conclusion | Discussion closed |
| 11 | Abstract | complete manuscript |
| 12 | Title + Keywords | Abstract/manuscript complete |
| 13 | Transversal synchronization | according to live external dependencies |
| 14 | Scientific audit/freeze | after synchronization and required audits |
| 15 | Final KBS adaptation | scientific freeze + current submission requirements |

`Figure 1` de Section 3.1 sigue siendo una figura arquitectónica distinta de las tres figuras experimentales aprobadas por Grupo 6.

## 7. Concurrencia con el proceso experimental

Solo la IA Experimental administra `SRC-03` y el Plan Maestro experimental. La IA Gestora y la IA de Redacción lo consultan en solo lectura.

Antes de cada bloque que dependa de hechos experimentales se consulta la rama viva `docs/plan-maestro-temporal-2026-08-31` y se determina si un cambio posterior altera materialmente los hechos que pretende consumir el artículo.

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

Este avance externo no modifica por sí mismo el gate editorial local. Ningún avance experimental abre automáticamente Results, Discussion o el freeze científico final.

## 8. B04 / Section 4.5 — alcance correcto

La función de 4.5 está congelada por D-045 y Structure V02:

`4.5 Experimental system configuration and execution / Configuración y ejecución experimental`.

Debe instanciar la arquitectura de Section 3 sin reexplicarla conceptualmente y describir exclusivamente elecciones de ejecución materialmente relevantes. El contrato B04 correcto debe cubrir:

1. representación de consulta y normalización/tokenización realmente ejecutada;
2. configuración de recuperación histórica;
3. construcción del ranking Top-k y del fixed Top-3;
4. asociación documental específica por candidato en la ruta primaria ejecutada;
5. construcción del contexto suministrado al generador;
6. modelo local, prompt/configuración y restricciones de generación efectivamente ejecutadas;
7. condiciones materiales de software/hardware/runtime únicamente cuando estén verificadas y sean relevantes.

No debe anticipar resultados ni valores observados de desempeño.

### 8.1 Supersession reciente

- D-059 = `SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION`.
- `article/prompts/5_EXPERIMENTAL_DESIGN_B04_SECTION4_5.md` V01 = `SUPERSEDED / DO_NOT_EXECUTE`.
- B04 Prompt V02 corrigió el alcance científico pero no respetó el orden exacto de onboarding de `START_HERE.md`; por D-061 queda `SUPERSEDED_FOR_EXECUTION`.
- El siguiente contrato debe ser B04 Prompt V03, autosuficiente y semánticamente bilingüe.

### 8.2 Requisitos mínimos del Prompt V03

Debe usar exactamente el onboarding:

```text
START_HERE
→ README
→ ARTICLE_STATUS
→ ARTICLE_WRITING_PLAN
→ DECISIONS
→ SOURCE_REGISTRY
→ CLAIM_EVIDENCE_MATRIX
→ STYLE_GUIDE
→ task-specific file
```

Después debe invocar expresamente MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-058, D-060 y D-061; verificar SRC-03/main vivos; exigir master Markdown candidato y DOCX acumulativo candidato; exigir handoff real del DOCX al autor; exigir QA OOXML, comentarios/anclajes, tracked changes, render y equivalencia EN/ES; y detenerse al cerrar B04 sin abrir 4.6.

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
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = MATERIALIZE_AND_AUDIT_B04_PROMPT_V03
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
PRIOR_CITATION_COMMENTS = 40 / PRESERVE
SECTION_4_5 = ELIGIBLE / NOT_EXECUTABLE_UNTIL_V03
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Purpose

Manage iterative construction of the main scientific article without anticipating Results, altering the approved experimental design, or transferring internal governance logic into manuscript prose. The article uses a cumulative master: each authorized block starts from the latest integrated master and becomes canonical only after the applicable independent audit, corrections, author approval, and verified technical integration.

Drafting is governed by `KBS_EWG_34_V01`, MWDP v1.0, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, active decisions, and governing experimental sources for every empirical fact.

## 2. Binding scientific and editorial principles

- The article is not an abbreviated thesis.
- Narrative sequence: problem/positioning → general architecture → experimental instantiation → results → interpretation.
- The general object is a **configurable framework for auditable tariff-classification decision support**.
- Section 3 is the technical core of the framework.
- Historical retrieval generates and orders candidates.
- The Top-3 is frozen before documentary and generative stages.
- Documentary/normative evidence is associated with already fixed candidates and does not change composition or order.
- The local LLM operates downstream for controlled explanation; it does not classify from scratch or feed back into the ranking.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary/normative association ≠ substantive normative correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE is the analysis unit; DAM/declaration is the grouping unit when intra-declaration dependence is methodologically relevant.
- EXP11A is joint size/composition sensitivity, not an isolated causal size effect.
- EXP11B is descriptive and does not support inference to a seed superpopulation.
- EXP12 does not estimate a historical-diversity effect under the frozen design.
- Every scientific claim must be authorized and traceable.
- Part I is the English publication manuscript; Part II is the Spanish semantic-control mirror.
- Abstractions must be translated into observable components, inputs, actions, outputs, and constraints.
- `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain binding.

### 2.1 Methods-specific rule

Methods describe scientific objects, provenance, procedures, design choices, execution, evaluation protocols, and validity controls. Exhaustive artifact identity belongs in manifests and reproducibility resources unless a concrete identifier is methodologically indispensable.

The publication-facing narrative is not organized around hashes, internal paths, physical script/file names, worksheet names, or internal configuration labels.

## 3. Cumulative structure

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion + Limitations
7. Conclusion
8. KBS end matter

The governing detailed structure is `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`, approved through D-045.

### 3.1 Approved Section 4

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

## 4. Cumulative master and DOCX policy

1. Each block starts from the latest approved and integrated master.
2. Current canonical Markdown: `ARTICLE_MASTER_V012.md`, SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`, Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`.
3. Current cumulative DOCX: `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`, in local author custody, SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, with 40 inherited comments and zero tracked changes in the approved audit.
4. D-021/D-027 govern local custody and effective binary handoff; D-035 governs timeout-safe handoff.
5. The DOCX must not be reconstructed from Markdown or from an earlier Word file.
6. Manual Base64, chunking, recomposition, or prohibited transfer workarounds are not allowed.
7. New blocks preserve previously approved sections, comments, semantic styles, tables, and captions unless an explicit reopening authorizes otherwise.
8. A candidate master becomes canonical only after all applicable gates are passed.
9. MWDP v1.0 is cumulative: omission of a rule from a specific prompt does not repeal it.

## 5. Phase and block state

| Element | State |
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
| Experimental Design B04 / 4.5 | ELIGIBLE / BLOCKED_UNTIL_PROMPT_V03 |
| Sections 4.6–4.8 | NOT_AUTHORIZED |
| Group-6 experimental figures/captions | CLOSED / APPROVED externally; EDITORIAL_INTEGRATION_DEFERRED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

Experimental groups are not managed here. `SRC-03` is read-only for the Managing and Drafting AIs and is consulted whenever an editorial gate or claim materially depends on experimental state.

## 6. Drafting order

| Phase | Deliverable | Gate |
|---|---|---|
| 1 | Complete structure | CLOSED / AUTHOR_APPROVED; Section 4 amended by D-045 |
| 2 | Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 3 | Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4 | Decision-support architecture | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5A | 4.1 + 4.2.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5B | 4.3 Documentary corpus and evidence resource | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5C | 4.4 Partition validity and dependence controls | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5D | 4.5 Experimental system configuration and execution | NEXT SCIENTIFIC BLOCK / WAITING FOR CORRECTED V03 CONTRACT |
| 5E | 4.6 Evaluation framework and protocols | NOT_AUTHORIZED |
| 5F | 4.7 Statistical and robustness analysis | NOT_AUTHORIZED |
| 5G | 4.8 Reproducibility resources | NOT_AUTHORIZED |
| 6 | Provisional Results | sufficiently stable Experimental Design + editorial gate + consumable evidence |
| 7 | Editorial integration of already approved experimental figures | only when the corresponding Results/secondary-material gate is open |
| 8 | Final Results | provisional Results + authorized visual/tabular resources + editorial audit |
| 9 | Discussion + Limitations | final Results + authorized literature contrast |
| 10 | Conclusion | Discussion closed |
| 11 | Abstract | complete manuscript |
| 12 | Title + Keywords | Abstract/manuscript complete |
| 13 | Transversal synchronization | according to live external dependencies |
| 14 | Scientific audit/freeze | after synchronization and required audits |
| 15 | Final KBS adaptation | scientific freeze + current submission requirements |

Section-3 Figure 1 remains an architecture figure distinct from the three experimental figures approved by Group 6.

## 7. Concurrency with the experimental workflow

Only the Experimental AI manages `SRC-03` and the experimental Master Plan. The Managing and Drafting AIs access them read-only.

Before each block that depends on experimental facts, the live `docs/plan-maestro-temporal-2026-08-31` branch is checked to determine whether later changes materially affect the facts to be consumed by the article.

Latest synchronized cut registered by the article:

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

External progress does not itself change the local editorial gate. No experimental progress automatically opens Results, Discussion, or the final scientific freeze.

## 8. B04 / Section 4.5 — correct scope

The function of Section 4.5 is frozen by D-045 and Structure V02:

`4.5 Experimental system configuration and execution / Configuración y ejecución experimental`.

It instantiates Section 3 without conceptually re-explaining the architecture and reports only execution choices that materially affected the experiment. The correct B04 contract must cover:

1. query representation and actually executed normalization/tokenization;
2. historical-retrieval configuration;
3. Top-k and fixed-Top-3 construction;
4. candidate-specific documentary association in the actually executed primary path;
5. construction of context supplied to the generator;
6. actually executed local model, prompt/configuration, and generation restrictions;
7. material software/hardware/runtime conditions only when verified and relevant.

Observed performance values must not be anticipated.

### 8.1 Recent supersession

- D-059 = `SUPERSEDED_FOR_B04_SCOPE_AND_EXECUTION`.
- B04 Prompt V01 = `SUPERSEDED / DO_NOT_EXECUTE`.
- B04 Prompt V02 corrected the scientific scope but did not preserve the exact `START_HERE.md` onboarding order; under D-061 it is `SUPERSEDED_FOR_EXECUTION`.
- The next contract must be a self-contained, semantically bilingual B04 Prompt V03.

### 8.2 Minimum V03 requirements

It must use exactly:

```text
START_HERE
→ README
→ ARTICLE_STATUS
→ ARTICLE_WRITING_PLAN
→ DECISIONS
→ SOURCE_REGISTRY
→ CLAIM_EVIDENCE_MATRIX
→ STYLE_GUIDE
→ task-specific file
```

It must then explicitly invoke MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-058, D-060, and D-061; verify live SRC-03/main; require cumulative candidate Markdown and DOCX masters; require actual author handoff of the DOCX; require OOXML, comment/anchor, tracked-change, render, and EN/ES-equivalence QA; and stop after B04 without opening Section 4.6.

## 9. Mandatory cycle

```text
Managing AI reconstructs state/evidence
→ opens and versions a closed block prompt
→ Drafting AI executes only that block
→ delivers artifacts and versioned response
→ Managing AI independently audits claims, structure, terminology, bilingual equivalence, Word, comments, and versioning
→ Experimental AI reviews only when a material trigger exists
→ corrections if required
→ PASS
→ explicit author approval when applicable
→ Managing AI technically integrates/promotes
→ next gate opens only if authorized
```

## 10. Immediate state

```text
CURRENT_GATE = CONTROL_SYNC_FOR_B04_V03
NEXT_ACTOR = MANAGING_AI
NEXT_ACTION = MATERIALIZE_AND_AUDIT_B04_PROMPT_V03
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V012.md
BASELINE_MASTER_MD_GIT_BLOB = dfea73f5f462fc65cf98347f796deadc6da58455
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
BASELINE_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
PRIOR_CITATION_COMMENTS = 40 / PRESERVE
SECTION_4_5 = ELIGIBLE / NOT_EXECUTABLE_UNTIL_V03
SECTION_4_6_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```