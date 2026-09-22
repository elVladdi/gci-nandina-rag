# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.8
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
RELATED_WORK_CLOSURE_DECISION = D-025
DOCX_CUSTODY_DECISION = D-021 / D-027 / D-029
GITHUB_ONLY_RESPONSE_DECISION = D-022
TECHNICAL_CLOSURE_MODE_DECISION = D-023
EXPERIMENTAL_RECONCILIATION_DECISION = D-030
INTRODUCTION_APPROVAL_DECISION = D-031
INTRODUCTION_INTEGRATION_DECISION = D-033
G6_G7_RECONCILIATION_DECISION = D-034
LATEST_EDITORIAL_DECISION = D-034
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
CANONICAL_MASTER_DOCX = LOCAL_AUTHOR_CUSTODY / D033
CANONICAL_MASTER_DOCX_SOURCE_FILENAME = ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx
CANONICAL_MASTER_DOCX_SHA256 = d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = DECISION_SUPPORT ARCHITECTURE
CURRENT_AUTHORIZED_BLOCK = ARCHITECTURE_B01 / SECTIONS_3_1_TO_3_4_ONLY
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
DECISION_SUPPORT_ARCHITECTURE = AUTHORIZED / ACTIVE
EXPERIMENTAL_DESIGN = NOT_YET_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica interna de gobernanza. El artículo se construye sobre un master acumulativo; cada bloque autorizado completa esa misma base y solo se vuelve canónico después de auditoría y aprobación expresa del autor.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, las decisiones congeladas, la literatura primaria verificada y las fuentes experimentales gobernantes cuando corresponda.

## 2. Principios científicos y editoriales vinculantes

- El artículo no es una versión abreviada de la tesis.
- El lector debe encontrar primero problema y posicionamiento, después la arquitectura general y solo luego la instanciación experimental específica.
- NANDINA, Clase/Capítulo 87, H100 y el corpus concreto no deben definir prematuramente el alcance conceptual de la arquitectura.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de la recuperación documental y de la generación.
- La recuperación documental/normativa aporta evidencia para candidatos ya fijados y no sustituye ni reordena el ranking histórico.
- El LLM local opera downstream para explicación controlada; no clasifica desde cero, no altera candidatos y no retroalimenta la clasificación.
- El reranker LLM permanece diagnóstico salvo decisión posterior expresa.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary/normative association ≠ substantive legal correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de observación/análisis; DAM es unidad de agrupamiento cuando existe dependencia.
- EXP11A expresa sensibilidad conjunta tamaño/composición, no efecto causal aislado del tamaño.
- EXP11B es descriptivo y no autoriza inferencia a una superpoblación de seeds.
- EXP12 no permite estimar el efecto de diversidad histórica bajo el diseño congelado.
- Ningún resultado pendiente se redactará como hallazgo.
- Toda afirmación científica debe trazarse a evidencia autorizada.
- Part I es el manuscript master inglés; Part II es el espejo español de control semántico.
- Las abstracciones deben traducirse a componentes, acciones, entradas, salidas y restricciones observables.
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen vigentes hasta decisión expresa posterior.

## 3. Arquitectura acumulativa aprobada

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

La estructura detallada permanece en `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`, aprobada mediante D-015. `Limitations` permanece integrada como `6.6 Limitations` salvo futura enmienda expresa.

## 4. Política del master acumulativo y DOCX

1. Cada bloque parte del último master acumulativo aprobado.
2. El master Markdown canónico actual es `ARTICLE_MASTER_V007.md`, blob `436e0522db0ac348efaed86f4e53a7e6db372471`.
3. El DOCX acumulativo actual es `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx`, bajo custodia local del autor, SHA-256 `d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c`, con 40 comentarios de auditoría de citas.
4. D-021 mantiene diferida la carga ordinaria del DOCX al repositorio; D-027 exige entrega efectiva del binario al autor; D-029 y D-033 gobiernan la identidad vigente del baseline.
5. No se crean Words independientes por sección: la nueva sección se inserta en el master acumulativo.
6. Part I y Part II deben conservar equivalencia semántica.
7. Todo bloque preserva exactamente las secciones y comentarios ya aprobados.
8. El SHA-256 del DOCX candidato debe registrarse en la respuesta versionada.
9. Si el baseline DOCX exacto no está disponible, la IA de Redacción se detiene; no reconstruye silenciosamente desde Markdown.
10. D-022 exige prompts y respuestas operativas sustantivas en GitHub; D-023 mantiene los cierres técnicos mínimos; D-027 gobierna el handoff efectivo de binarios.
11. Un candidato no se vuelve master canónico hasta auditoría de IA Gestora y aprobación expresa del autor.

## 5. Estado de fases y bloques

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Estructura KBS V01 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work 2.1–2.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction B01 V02 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Canonical master | `ARTICLE_MASTER_V007.md` |
| Decision-support architecture | AUTHORIZED / ACTIVE |
| Architecture B01 | AUTHORIZED / SECTIONS 3.1–3.4 ONLY |
| Architecture B02 | NOT_AUTHORIZED |
| Experimental design | NOT_AUTHORIZED |
| Experimental Group 5 | CLOSED / APPROVED |
| Experimental Group 6 | NOT_STARTED; G6-F01 ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED |
| Experimental Group 7 | PROSPECTIVE / NOT_ACTIVATED; formal activation requires Group 6 CLOSED/APPROVED |
| Experimental Group 8 | PROSPECTIVE / NOT_ACTIVATED; requires Group 7 CLOSED/APPROVED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |

## 6. Concurrencia editorial con Grupos 6–8 — D-034

La secuencia experimental de fichas y la redacción progresiva del artículo son procesos relacionados pero no idénticos.

D-034 fija:

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

La frase de G7-F01 “antes de escribir” se interpreta como antes de la redacción/actualización formal gobernada por Grupo 7, no como prohibición de la redacción editorial previa bajo `article/main-manuscript`.

Hasta el cierre de Grupo 6 permanecen provisionales la selección/numeración final de figuras, captions, referencias cruzadas, ubicación visual y cualquier pasaje de Results/Discussion cuya forma final dependa de esas figuras. Esto no bloquea Architecture ni Experimental design.

G7 debe sincronizar el manuscrito con el estado científico final G3–G6. G8 debe auditar claim→evidencia→cifra, coherencia Métodos–Resultados–Discusión, texto–tablas–figuras y readiness para el freeze. El cierre de G7 no equivale al freeze final.

D-034 no autoriza G6, G7 ni G8.

## 7. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED |
| 2 | Related Work | CLOSED / APPROVED / FROZEN |
| 3 | Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4 | Decision-support architecture | **ACTIVE — Architecture B01 authorized** |
| 5 | Experimental design | arquitectura suficientemente estable + autorización editorial expresa |
| 6 | Results provisional | Experimental design estable + gate editorial; consumir evidencia G5 cerrada |
| 7 | Figuras y visualizaciones | autorización experimental/editorial específica; cierre mediante Grupo 6 |
| 8 | Results definitivos | evidencia + visualizaciones requeridas cerradas |
| 9 | Discussion + Limitations | Results definitivos + contraste G4-F03 autorizado; sincronización final sujeta a G6/G7 |
| 10 | Conclusion | Discussion cerrada |
| 11 | Abstract | manuscrito completo |
| 12 | Title + Keywords | Abstract/manuscrito completos |
| 13 | Sincronización transversal G7 | Grupo 6 CLOSED/APPROVED y secuencia G7 formalmente activada |
| 14 | Auditoría/freeze G8 | Grupo 7 CLOSED/APPROVED |
| 15 | Adaptación final KBS | freeze científico + requisitos vigentes verificados |

Orden activo inmediato:

`Architecture B01 → auditoría → aprobación autoral → siguiente bloque de Architecture → Experimental design`.

No se autoriza avanzar automáticamente de B01 a B02 ni de Architecture a Experimental design.

## 8. Estado experimental consumible

Corte editorial vigente, reconciliado por D-030:

```text
EXPERIMENTAL_PLAN_BRANCH = docs/plan-maestro-temporal-2026-08-31
EXPERIMENTAL_PLAN_HEAD = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
EXPERIMENTAL_PLAN_BLOB = 9b388fe8cc19fce86ec3c15853e73899cb3e5666
EXPERIMENTAL_MAIN_CHECKPOINT = ca065618d5df0019f76ef5a971e858d91c263e1f
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F03_EXTERNAL_REAUDIT = PASS
G4_F03_COMPARISON_REGISTRY_COUNT = 11
G4_F03_AUTHORIZED_DISCUSSION_POINT_COUNT = 8
G4_F03_FORBIDDEN_DISCUSSION_POINT_COUNT = 14
GROUP5 = CLOSED / APPROVED
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5_CANONICAL_TABLE_COUNT = 9
GROUP6 = NOT_STARTED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Grupo 5 fija nueve tablas: dos principales inferenciales, dos secundarias/descriptivas y cinco de apéndice/suplemento. Sus roles son vinculantes para futura Results. No introdujo nuevas métricas o inferencia ni abrió Results/Discussion/Figures.

## 9. Fase activa — Architecture B01

Architecture B01 comprende exclusivamente:

- `3.1 Overview and information flow` / `Vista general y flujo de información`;
- `3.2 Query representation and normalization` / `Representación y normalización de la consulta`;
- `3.3 Historical candidate retrieval and ranking` / `Recuperación histórica y ranking de candidatos`;
- `3.4 Fixed candidate set` / `Conjunto fijo de candidatos`.

### Función narrativa

La sección debe describir la **arquitectura general antes de la instanciación experimental**. No debe abrir con NANDINA, Clase/Capítulo 87, H100, tamaños de datasets ni métricas observadas.

Debe explicar en términos concretos:

1. qué entra al sistema;
2. cómo se representa/normaliza la consulta;
3. cómo un banco histórico etiquetado produce un ranking de candidatos mediante una función de recuperación;
4. cómo se conserva el precedente histórico asociado a cada candidato;
5. cómo se obtiene el Top-3 fijo que delimita todo procesamiento downstream;
6. qué permanece fijo al salir de 3.4.

La implementación experimental vigente puede utilizarse para verificar acciones concretas, pero los parámetros, datasets, hashes, tamaños y resultados pertenecen a `Experimental design` o `Results`, no a Architecture.

### Fuentes mínimas

- `ARTICLE_MASTER_V007.md` e Introduction aprobada como restricción de consistencia;
- `START_HERE.md`, `ARTICLE_STATUS.md`, este Plan, decisiones, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, `STYLE_GUIDE.md`;
- `SRC-02` cuando esté disponible para arquitectura/metodología operativa;
- Plan Maestro experimental y `main@ca065618d5df0019f76ef5a971e858d91c263e1f` para verificar implementación;
- código/protocolos primarios de recuperación histórica cuando se describan acciones implementadas.

Si una afirmación arquitectónica depende de `SRC-02` y esa fuente no está accesible, no debe completarse por inferencia.

### Límites de B01

B01 no debe:

- redactar 3.5–3.7;
- describir el corpus normativo concreto en detalle;
- detallar prompts/modelo local/configuración experimental;
- introducir resultados o cifras de desempeño;
- presentar reranking diagnóstico como parte del flujo principal;
- convertir BM25 en requisito universal de la arquitectura si la afirmación pretende ser de interfaz/configurabilidad;
- declarar novelty, SOTA, superioridad global, generalización o corrección jurídica;
- modificar Introduction o Related Work;
- abrir Experimental design.

## 10. Ciclo obligatorio de cada bloque

`verificar baseline → reconstruir estado → verificar fuentes → ejecutar solo bloque autorizado → generar EN + espejo ES → preservar contenido previo → QA científica/SPCCR → versionar respuesta y artefactos → auditoría IA Gestora → correcciones si aplican → aprobación expresa del autor → integración canónica → siguiente gate`.

Toda cita científica nueva debe reabrirse en fuente primaria y quedar acompañada por comentario Word anclado a la cita inglesa. Si Architecture B01 no requiere citas bibliográficas nuevas, los 40 comentarios heredados se preservan exactamente y no se crean comentarios artificiales.

## 11. Criterios generales de aprobación

Una sección pasa a `APPROVED` solo si cumple su función narrativa; cada claim está respaldado por la fuente gobernante adecuada; no anticipa resultados ni detalles de testbed fuera de lugar; respeta los límites claim–evidencia; mantiene equivalencia EN/ES; preserva artefactos aprobados; pasa QA técnica del DOCX; y recibe aprobación expresa del autor después de auditoría de IA Gestora.

## 12. Front matter, end matter y targeting

Title, Abstract y Keywords se redactan al final. El end matter contemplará `Data availability`, `Code and reproducibility resources` si corresponde, CRediT, Funding, Declaration of competing interest, Acknowledgements si aplica, References y Supplementary material.

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
PUBLICATION_ROUTE_KBS = SUBSCRIPTION
```

Antes del paquete final se verificarán nuevamente los requisitos oficiales vigentes de KBS.

---

# English

## 1. Purpose

Manage iterative construction of the main scientific article without anticipating results, changing the approved experimental design, or importing internal governance prose into the manuscript. The article uses one cumulative master; each authorized block extends that master and becomes canonical only after audit and explicit author approval.

Drafting is governed by `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, the Claim–Evidence Matrix, Source Registry, frozen decisions, verified primary literature, and governing experimental sources where applicable.

## 2. Binding scientific and editorial principles

- The article is not a shortened thesis.
- Readers encounter problem/positioning first, then general architecture, then the specific empirical instantiation.
- NANDINA, Class/Chapter 87, H100, and the concrete corpus must not define the architecture's conceptual scope prematurely.
- Historical retrieval generates and ranks candidates; the Top-3 is fixed before documentary retrieval and generation.
- Normative/documentary retrieval attaches evidence to already fixed candidates and does not replace or reorder the historical ranking.
- The downstream local LLM produces controlled explanation only; it does not classify from scratch, alter candidates, or feed back into classification.
- The LLM reranker remains diagnostic unless expressly changed later.
- Candidate retrieval is not overall system accuracy; documentary association is not substantive legal correctness; auditability is not legal correctness; configurability is not empirical generalization.
- SERIE is the analysis unit and DAM is the grouping unit when dependence exists.
- EXP11A is joint size/composition sensitivity; EXP11B is descriptive without seed-superpopulation inference; EXP12 diversity effect is not estimable under the frozen design.
- No pending result may be written as a finding.
- Part I is the English manuscript master and Part II is the Spanish semantic-control mirror.
- `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain binding.

## 3. Approved cumulative structure

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion
7. Conclusion
8. KBS end matter

`6.6 Limitations` remains integrated within Discussion unless expressly amended.

## 4. Cumulative master and DOCX policy

The current canonical Markdown is `ARTICLE_MASTER_V007.md`, blob `436e0522db0ac348efaed86f4e53a7e6db372471`. The current cumulative DOCX is `ARTICLE_MASTER_CANDIDATE_INTRO_B01_V02.docx`, SHA-256 `d2b68366b706502202ab67860a1df0eccc7747c15df7a58de76607b5f8a69b9c`, with 40 citation-audit comments in verified author custody.

D-021, D-022, D-023, D-027, D-029, and D-033 continue to govern DOCX custody, GitHub-only operational responses, minimal technical closure, effective binary handoff, and baseline identity. Each block must preserve approved text/comments exactly, maintain EN/ES semantic equivalence, record candidate DOCX SHA-256, and stop rather than silently reconstruct a missing baseline.

## 5. Current state

Related Work 2.1–2.6 and Introduction B01 V02 are closed, approved, frozen, and integrated. `ARTICLE_MASTER_V007` is canonical. Decision-support architecture is now authorized and active; only Architecture B01 (Sections 3.1–3.4) is authorized. Architecture B02, Experimental design, Results, and Discussion are not yet authorized.

Experimental Group 5 is closed/approved. Group 6 remains not started, with G6-F01 eligible but unauthorized/unexecuted. Group 7 is prospective and may not be formally activated before Group 6 closes. Group 8 is prospective and follows Group 7.

## 6. Editorial concurrency with Groups 6–8 — D-034

The experimental ficha sequence and progressive article drafting are related but distinct workflows.

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

G7-F01's “before writing” requirement means before formal Group-7 drafting/update, not a ban on prior article drafting under `article/main-manuscript`.

Until Group 6 closes, final figure selection/numbering, captions, figure cross-references, visual placement, and Results/Discussion passages whose final form depends on those figures remain provisional. This does not block Architecture or Experimental design.

G7 synchronizes the manuscript with final G3–G6 science; G8 performs the final claim/evidence/number and cross-section audit and determines scientific-freeze readiness. D-034 does not authorize G6, G7, or G8.

## 7. Drafting order

The immediate active order is:

`Architecture B01 → Managing-AI audit → author approval → next Architecture block → Experimental design`.

Later phases are provisional Results using closed G5 evidence, Group-6 figures, final Results, Discussion/Limitations, Conclusion, Abstract, Title/Keywords, formal G7 synchronization, G8 audit/freeze, and final KBS adaptation. No block opens automatically.

## 8. Consumable experimental state

The article continues to consume D-030's cutoff: Master Plan HEAD `98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e`, blob `9b388fe8cc19fce86ec3c15853e73899cb3e5666`, and experimental `main@ca065618d5df0019f76ef5a971e858d91c263e1f`. Groups 3–5 are closed/approved, `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`, Group 5 has nine canonical tables, and Group 6 remains not started.

## 9. Active phase — Architecture B01

Architecture B01 covers only Sections 3.1–3.4: overview/information flow, query representation/normalization, historical candidate retrieval/ranking, and fixed candidate set.

It must describe the general architecture before the empirical instantiation. It must not open with NANDINA, Chapter/Class 87, H100, dataset sizes, or observed metrics. It should concretely explain the input, normalized query representation, retrieval/ranking from a labeled historical bank, retention of the historical precedent supporting each candidate, construction of the fixed Top-3, and what becomes immutable downstream.

The experimental implementation may verify concrete actions, but parameters, datasets, hashes, sample sizes, and performance belong to Experimental design or Results. Minimum sources are `ARTICLE_MASTER_V007`, governing article controls, SRC-02 when available, the experimental Master Plan/current main checkpoint, and primary historical-retrieval code/protocols for implementation claims. If an architecture claim depends on inaccessible SRC-02, it must not be inferred.

B01 must not draft Sections 3.5–3.7; detail the concrete normative corpus or local-LLM configuration; introduce results; promote diagnostic reranking into the main flow; make BM25 a universal architectural requirement when discussing configurable interfaces; claim novelty/SOTA/global superiority/generalization/legal correctness; modify Introduction/Related Work; or open Experimental design.

## 10. Mandatory block cycle and approval

`verify baseline → reconstruct state → verify sources → execute authorized block only → produce EN + ES mirror → preserve prior content → scientific/SPCCR QA → version artifacts/response → Managing-AI audit → corrections if required → explicit author approval → canonical integration → next gate`.

Any new scientific citation requires reopening the primary source and an anchored Word comment on the English citation. If B01 requires no new bibliographic citations, all 40 inherited comments are preserved exactly and no artificial comments are added.

A section becomes approved only after narrative, source/claim, scope, EN/ES, DOCX QA, preservation, Managing-AI audit, and explicit author-approval gates all pass.

## 11. Targeting

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
PUBLICATION_ROUTE_KBS = SUBSCRIPTION
```

Final KBS requirements will be rechecked before submission packaging.