# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.0
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-041
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_AUTHORIZED_BLOCK = EXPERIMENTAL_DESIGN_B01 / SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
ARCHITECTURE = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = AUTHORIZED / ACTIVE
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica interna de gobernanza. El artículo se construye sobre un master acumulativo; cada bloque autorizado completa esa misma base y solo se vuelve canónico después de auditoría de la IA Gestora y aprobación expresa del autor cuando el gate aplicable lo exige.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, las decisiones congeladas, literatura primaria verificada cuando corresponda y las fuentes experimentales gobernantes para todo hecho empírico.

## 2. Principios científicos y editoriales vinculantes

- El artículo no es una versión abreviada de la tesis.
- La secuencia editorial es problema/posicionamiento → arquitectura general → instanciación experimental → resultados → interpretación.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de la recuperación documental y de la generación.
- La recuperación documental/normativa aporta evidencia para candidatos ya fijados y no cambia su composición ni orden.
- El LLM local opera downstream para explicación controlada; no clasifica desde cero ni retroalimenta la clasificación.
- El reranking LLM permanece diagnóstico salvo decisión posterior expresa.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary/normative association ≠ substantive legal correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es la unidad de análisis; DAM/declaración es la unidad de agrupamiento cuando existe dependencia.
- EXP11A expresa sensibilidad conjunta tamaño/composición, no efecto causal aislado del tamaño.
- EXP11B es descriptivo y no autoriza inferencia a una superpoblación de seeds.
- EXP12 no permite estimar el efecto de diversidad histórica bajo el diseño congelado.
- Toda afirmación científica debe trazarse a evidencia autorizada.
- Part I es el manuscript master inglés; Part II es el espejo español de control semántico.
- Las abstracciones deben traducirse a componentes, entradas, acciones, salidas y restricciones observables.
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen vinculantes.

## 3. Estructura acumulativa

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion + Limitations
7. Conclusion
8. KBS end matter

La estructura detallada permanece en `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`, aprobada mediante D-015.

## 4. Política del master acumulativo y DOCX

1. Cada bloque parte del último master aprobado e integrado.
2. El master Markdown canónico actual es `ARTICLE_MASTER_V009.md`, SHA-256 `ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28`, Git blob `40f20437458715c615fc1762f025ebcdbb3b6fc2`.
3. El DOCX acumulativo actual es `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx`, bajo custodia local efectiva del autor, SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`, con 40 comentarios heredados y 0 tracked changes en la última auditoría aprobada.
4. D-021 difiere la carga ordinaria del DOCX; D-027 exige entrega efectiva del binario exacto al autor.
5. D-035 obliga al handoff timeout-safe para artefactos acumulativos grandes después del antecedente de timeout. No se usa Base64 manual, fragmentación/chunking, recomposición, archivos auxiliares ni múltiples commits como workaround.
6. La codificación interna automática de una API o conector no constituye Base64 manual.
7. No se reconstruye el DOCX desde Markdown. Si falta el baseline exacto o falla su hash, la IA de Redacción se detiene.
8. Los bloques nuevos preservan exactamente las secciones y comentarios ya aprobados.
9. El master candidato no se vuelve canónico hasta auditoría de IA Gestora, aprobación autoral cuando corresponda e integración técnica verificada.

## 5. Continuidad operativa de la IA Gestora

La IA Gestora no introduce pausas artificiales. Cuando un gate queda satisfecho y la siguiente acción es determinista, técnica y está dentro de su mandato —materializar un master ya aprobado, actualizar estado, abrir el siguiente bloque elegible o versionar el prompt— continúa automáticamente sin pedir al autor que escriba «continúa».

Solo se detiene ante un gate real: decisión científica/editorial del autor; archivo exacto no disponible; dependencia controlada por IA Experimental u otra autoridad; contradicción irresuelta entre fuentes gobernantes; o evidencia insuficiente para una afirmación/bloque.

## 6. Estado de fases y bloques

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Estructura KBS V01 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work 2.1–2.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction B01 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Canonical master | `ARTICLE_MASTER_V009.md` |
| Experimental Design B01 — 4.1 + 4.2.1–4.2.4 | AUTHORIZED / ACTIVE |
| Experimental Design 4.3+ | NOT_AUTHORIZED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

Los grupos experimentales no se administran en esta tabla. Se consultan mediante `SRC-03` en modo de solo lectura únicamente cuando una afirmación o gate editorial depende materialmente de ellos.

## 7. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED |
| 2 | Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 3 | Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4 | Decision-support architecture | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 5A | Experimental Design B01 — 4.1 + 4.2 | **ACTIVE / AUTHORIZED** |
| 5B+ | Experimental Design restante | gates atómicos posteriores |
| 6 | Results provisional | Experimental Design suficientemente estable + gate editorial + evidencia consumible |
| 7 | Figuras/visualizaciones | control experimental/editorial específico |
| 8 | Results definitivos | evidencia y visualizaciones necesarias cerradas |
| 9 | Discussion + Limitations | Results definitivos + contraste de literatura autorizado |
| 10 | Conclusion | Discussion cerrada |
| 11 | Abstract | manuscrito completo |
| 12 | Title + Keywords | Abstract/manuscrito completos |
| 13 | Sincronización transversal | según dependencias externas vigentes |
| 14 | Auditoría/freeze científico | después de sincronización y auditorías requeridas |
| 15 | Adaptación final KBS | freeze científico + requisitos vigentes verificados |

## 8. Concurrencia con el proceso experimental

El proceso editorial y el experimental son distintos. Solo la IA Experimental administra el Plan Maestro experimental. La IA Gestora consulta `SRC-03` en modo de solo lectura.

D-034 mantiene, entre otras, estas reglas:

```text
GROUP6_CLOSE_REQUIRED_FOR_FORMAL_G7_ACTIVATION = YES
GROUP6_CLOSE_REQUIRED_FOR_ARCHITECTURE_DRAFTING = NO
GROUP6_CLOSE_REQUIRED_FOR_EXPERIMENTAL_DESIGN_DRAFTING = NO
FORMAL_G7_ACTIVATION_BEFORE_GROUP6_CLOSE = NOT_PERMITTED
G7_F03_ROLE = SYNCHRONIZATION_AND_TRANSVERSAL_CLOSURE
G7_F03_ROLE_IS_ARTICLE_INCEPTION = false
GROUP7_CLOSE_REQUIRED_BEFORE_GROUP8 = YES
SCIENTIFIC_FINAL_FREEZE_REQUIRES_GROUP8 = true
```

Último snapshot verificado:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_HEAD = b74b96d0163807007e4579d86450dd235125b30f
SRC03_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
DEVELOPMENT_MAIN = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

Este estado no bloquea Experimental Design B01.

## 9. Fase activa — Experimental Design B01

### 9.1 Alcance

B01 comprende exclusivamente:

- 4.1 Evaluation setting;
- 4.2 Historical data;
- 4.2.1 Data source and selection;
- 4.2.2 Target class space;
- 4.2.3 Preparation and curation;
- 4.2.4 Versioned datasets used in the experiment.

### 9.2 Función narrativa

B01 inaugura la instanciación empírica concreta después de la arquitectura general cerrada. Debe establecer un piloto offline no vinculante en NANDINA Chapter 87; SERIE como unidad de análisis; DAM/declaración como unidad de agrupamiento cuando la dependencia sea relevante; procedencia y selección de datos; espacio de códigos representado; preparación/curación; e identidad versionada de H100, DEV y EVAL.

No debe repetir la lógica arquitectónica de Section 3 ni anticipar resultados.

### 9.3 Ground truth mínimo

El benchmark v0.2 congelado usa:

- H100: 2,950 series / 28 DAM / 66 códigos representados;
- DEV: 100 series / 6 DAM / 9 códigos representados;
- EVAL: 1,056 series / 67 DAM / 42 etiquetas de referencia representadas;
- SHA H100: `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`;
- SHA DEV: `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`;
- SHA EVAL: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.

La metadata canónica es `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`; la configuración es `src/configs/data_aduanas_split_clase87_v0.2.json`. La estrategia `T5-safe-159` usa asignaciones explícitas de DAM. `seed=2026` es metadato/configuración y no el mecanismo de asignación v0.2.

La procedencia histórica debe preservar el límite forense: el workbook actual reproduce funcionalmente el contenido procesado relevante, pero el workbook histórico completo no es byte-identificable con el actual. No se afirmará identidad binaria de la fuente histórica original.

### 9.4 Claims y límites

Relevantes: C06 y C07 `AUTHORIZED`; C19 solo como snapshot histórico cuando sea necesario; C20 `REVIEW_REQUIRED` y su cifra 48/59 no se usa; C21 dentro de sus límites y, en principio, diferido a validez/limitaciones.

B01 no incorpora retrieval performance, resultados de hipótesis, HE2/HE5, EXP11A/EXP11B/EXP12 ni resultados inferenciales. Tampoco presenta 66 códigos como universo exhaustivo de Chapter 87: son los códigos representados en H100.

### 9.5 Transferencia y entregables

Se reutiliza el patrón probado de D-035:

- section MD pequeño: GitHub;
- response pequeña: GitHub;
- master Markdown acumulativo candidato: adjunto exacto al autor + SHA-256;
- DOCX acumulativo candidato: adjunto exacto al autor + SHA-256;
- sin reintentar la transferencia directa del master grande;
- sin Base64 manual, fragmentación/chunking, recomposición o workarounds auxiliares.

## 10. Ciclo obligatorio de cada bloque

```text
IA Gestora reconstruye estado/evidencia
→ abre/versiona bloque y prompt
→ IA de Redacción ejecuta solo el bloque
→ entrega artefactos y respuesta versionada
→ IA Gestora audita independientemente
→ corrección si corresponde
→ PASS
→ aprobación expresa del autor cuando aplique
→ IA Gestora integra/promueve técnicamente
→ continúa automáticamente hasta el siguiente gate real
```

## 11. Estado inmediato

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_EXPERIMENTAL_DESIGN_B01_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Purpose

Manage iterative construction of the main scientific article without anticipating results, changing the approved experimental design, or transferring internal governance jargon into publishable prose. Each authorized block extends the same cumulative master and becomes canonical only after the required audit, author gate, and technical integration.

## 2. Binding principles

The article is not a shortened thesis. Its sequence is problem/positioning → general architecture → empirical instantiation → results → interpretation. Historical retrieval owns candidate generation/ranking; the Top-3 is fixed before documentary/generative stages; documentary retrieval attaches evidence without changing candidates; and the local LLM explains the fixed Top-3 without classifying from scratch or feeding back into ranking. Diagnostic reranking remains outside the primary flow.

Candidate retrieval is not overall classification accuracy; documentary association is not substantive legal correctness; auditability is not legal correctness; configurability/replication is not empirical generalization. SERIE is the analysis unit and DAM/declaration is the grouping unit when dependence matters. EXP11A is joint size/composition sensitivity, EXP11B is descriptive, and EXP12 does not estimate the historical-diversity effect. `FINAL_GAP` and `NOVELTY` remain undefined/undeclared.

Part I is the publication-facing English master; Part II is the Spanish semantic-control mirror. Abstract claims must be expressed through observable components, inputs, actions, outputs, and constraints.

## 3. Cumulative structure

Introduction → Related work → Decision-support architecture → Experimental design → Results → Discussion/Limitations → Conclusion → KBS end matter.

## 4. Cumulative-master and DOCX policy

The canonical Markdown is `ARTICLE_MASTER_V009.md`, SHA-256 `ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28`, Git blob `40f20437458715c615fc1762f025ebcdbb3b6fc2`. The exact local DOCX baseline is `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx`, SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`, with 40 inherited comments and no tracked changes at the approved audit.

D-021/D-027 govern local binary custody; D-035 governs timeout-safe handoff of large artifacts. No DOCX reconstruction from Markdown is permitted. Automatic connector encoding is not manual Base64.

## 5. Managing-AI continuity

The Managing AI proceeds automatically after satisfied gates whenever the next action is deterministic and within mandate. It stops only for a genuine author decision, unavailable exact artifact, external-authority dependency, unresolved governing-source contradiction, or missing evidence.

## 6. Current phase state

Related Work, Introduction, and Architecture 3.1–3.7 are closed/approved/frozen/integrated. `ARTICLE_MASTER_V009` is canonical. Experimental Design B01 (4.1 + 4.2.1–4.2.4) is authorized/active. Section 4.3+, Results, Discussion, and Conclusion remain unauthorized.

## 7. Drafting order

Approved structure → Related Work → Introduction → Architecture → Experimental Design in atomic blocks → provisional Results → required visualizations → final Results → Discussion/Limitations → Conclusion → Abstract → Title/Keywords → transversal synchronization → final scientific audit/freeze → KBS adaptation.

## 8. Experimental-process concurrency

The editorial and experimental processes remain distinct. Only the Experimental AI manages the experimental Master Plan; the Managing AI reads `SRC-03` when needed. D-034 does not require Group-6 closure for Experimental-Design drafting. Current read-only snapshot: `SRC-03@b74b96d0163807007e4579d86450dd235125b30f`, blob `7b63fdb14b75eace173ac3c94775d39ed7ed7a57`; development `main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`.

## 9. Active phase — Experimental Design B01

B01 covers only 4.1 and 4.2.1–4.2.4. It establishes the offline, non-binding NANDINA Chapter-87 evaluation setting; SERIE and DAM units; historical-data provenance and selection; represented target-code space; preparation/curation; and versioned H100/DEV/EVAL identities.

Frozen v0.2 datasets: H100 2,950 series / 28 DAM / 66 represented codes; DEV 100 / 6 / 9; EVAL 1,056 / 67 / 42 represented reference labels. Their SHA-256 values are fixed in the Spanish control version and the canonical metadata. `T5-safe-159` uses explicit DAM assignments; `seed=2026` is provenance/configuration metadata rather than the v0.2 assignment mechanism.

The historical provenance statement must distinguish functional reproduction of processed content from binary identity of the original workbook. Retrieval-performance results, hypothesis outcomes, HE2/HE5, EXP11A/B/12 results, and later Experimental-Design content remain outside B01.

Large cumulative Markdown and DOCX candidates use the D-035 exact-file handoff pattern; the section MD and small response may be versioned directly.

## 10. Mandatory block cycle

Managing AI reconstructs evidence → opens/versioned prompt → Drafting AI executes only the block → artifacts/response → independent Managing-AI audit → correction if needed → PASS → author approval where required → canonical integration/promotion → automatic progression to next genuine gate.

## 11. Immediate state

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_EXPERIMENTAL_DESIGN_B01_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
