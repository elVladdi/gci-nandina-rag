# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.9
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
RELATED_WORK_CLOSURE_DECISION = D-025
DOCX_CUSTODY_DECISION = D-021 / D-027 / D-029 / D-033 / D-035 / D-037
GITHUB_ONLY_RESPONSE_DECISION = D-022
TECHNICAL_CLOSURE_MODE_DECISION = D-023
EXPERIMENTAL_RECONCILIATION_DECISION = D-030
INTRODUCTION_APPROVAL_DECISION = D-031
INTRODUCTION_INTEGRATION_DECISION = D-033
G6_G7_RECONCILIATION_DECISION = D-034
ARCHITECTURE_B01_APPROVAL_DECISION = D-036
ARCHITECTURE_B01_INTEGRATION_DECISION = D-037
ARCHITECTURE_B02_OPENING_DECISION = D-038
LATEST_EDITORIAL_DECISION = D-038
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V008
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
CANONICAL_MASTER_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = DECISION SUPPORT ARCHITECTURE
CURRENT_AUTHORIZED_BLOCK = ARCHITECTURE_B02 / SECTIONS_3_5_TO_3_7_ONLY
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B02 = AUTHORIZED / ACTIVE
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica interna de gobernanza. El artículo se construye sobre un master acumulativo; cada bloque autorizado completa esa misma base y solo se vuelve canónico después de auditoría de la IA Gestora y aprobación expresa del autor cuando el gate correspondiente lo exige.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, las decisiones congeladas, la literatura primaria verificada y las fuentes experimentales gobernantes cuando corresponda.

## 2. Principios científicos y editoriales vinculantes

- El artículo no es una versión abreviada de la tesis.
- El lector debe encontrar primero problema y posicionamiento, después la arquitectura general y solo luego la instanciación experimental específica.
- NANDINA, Clase/Capítulo 87, H100 y el corpus concreto no deben definir prematuramente el alcance conceptual de la arquitectura.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de la recuperación documental y de la generación.
- La recuperación documental/normativa aporta evidencia para candidatos ya fijados y no sustituye, elimina, inserta ni reordena el ranking histórico.
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

1. Cada bloque parte del último master acumulativo aprobado e integrado.
2. El master Markdown canónico actual es `ARTICLE_MASTER_V008.md`, SHA-256 `895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d`, blob Git `0145d13e1bc4e4fdeab79f7bad83d00f67221a76`.
3. El DOCX acumulativo actual es `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`, bajo custodia local efectiva del autor, SHA-256 `f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4`, con 40 comentarios heredados.
4. D-021 mantiene diferida la carga ordinaria del DOCX al repositorio; D-027 exige entrega efectiva del binario al autor.
5. D-035 obliga a usar handoff timeout-safe para artefactos grandes cuando una vía directa ya haya demostrado producir timeout. No se usa Base64 manual, fragmentación/chunking ni recomposición como workaround.
6. La codificación interna automática de una API o conector no constituye Base64 manual y no está prohibida.
7. No se crean Words independientes por sección: cada nuevo bloque se inserta en el master acumulativo.
8. Part I y Part II deben conservar equivalencia semántica.
9. Todo bloque preserva exactamente las secciones y comentarios ya aprobados.
10. El SHA-256 del DOCX candidato debe registrarse en la respuesta versionada.
11. Si el baseline DOCX exacto no está disponible, la IA de Redacción se detiene; no reconstruye silenciosamente desde Markdown.
12. Un candidato no se vuelve master canónico hasta auditoría de IA Gestora y aprobación del autor cuando corresponda.

## 5. Continuidad operativa de la IA Gestora

La IA Gestora no debe introducir pausas artificiales entre gates.

Cuando un gate queda satisfecho y la siguiente acción es determinista, técnica y está dentro de su mandato —por ejemplo, materializar un master ya aprobado, actualizar el estado, abrir el siguiente bloque elegible o versionar su prompt— debe continuar automáticamente sin pedir al autor que escriba «continúa» ni trasladarle una operación que la Gestora puede ejecutar.

La Gestora se detiene únicamente cuando existe un gate real que exige alguna de estas condiciones:

- aprobación, rechazo o decisión científica/editorial del autor;
- entrega de un archivo exacto que no está disponible en el entorno;
- decisión o evidencia que pertenece a la IA Experimental u otra autoridad externa;
- contradicción entre fuentes gobernantes que no puede resolverse por precedencia;
- falta de evidencia necesaria para una afirmación o bloque.

La continuidad automática no elimina los gates de aprobación; elimina únicamente las pausas que no representan una decisión real.

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
| Architecture B01 — 3.1–3.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Canonical master | `ARTICLE_MASTER_V008.md` |
| Architecture B02 — 3.5–3.7 | AUTHORIZED / ACTIVE |
| Experimental design | NOT_AUTHORIZED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

Los grupos experimentales no forman parte de la gestión editorial de esta tabla. Su estado se consulta como dependencia externa mediante `SRC-03` solo cuando un gate editorial depende materialmente de ellos.

## 7. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED |
| 2 | Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 3 | Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4A | Architecture B01 — 3.1–3.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| 4B | Architecture B02 — 3.5–3.7 | **ACTIVE / AUTHORIZED** |
| 5 | Experimental design | Architecture suficientemente cerrada + autorización editorial expresa |
| 6 | Results provisional | Experimental design estable + gate editorial + evidencia experimental consumible |
| 7 | Figuras/visualizaciones | control experimental/editorial específico; no se gestionan desde esta tabla |
| 8 | Results definitivos | evidencia y visualizaciones necesarias cerradas |
| 9 | Discussion + Limitations | Results definitivos + contraste de literatura autorizado |
| 10 | Conclusion | Discussion cerrada |
| 11 | Abstract | manuscrito completo |
| 12 | Title + Keywords | Abstract/manuscrito completos |
| 13 | Sincronización transversal | según dependencias externas vigentes |
| 14 | Auditoría/freeze científico | después de sincronización y auditorías requeridas |
| 15 | Adaptación final KBS | freeze científico + requisitos vigentes verificados |

No se autoriza avanzar automáticamente desde B02 a Experimental design sin auditoría, aprobación autoral e integración de B02. Una vez cumplidos esos gates, la IA Gestora sí debe continuar automáticamente con el cierre técnico y preparar el siguiente gate elegible.

## 8. Concurrencia con el proceso experimental

El proceso editorial y el proceso experimental son relacionados pero distintos. Solo la IA Experimental administra el Plan Maestro experimental. La IA Gestora lo consulta en modo de solo lectura cuando una afirmación o gate editorial depende de hechos experimentales.

D-034 mantiene estas reglas:

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

La selección/numeración final de figuras, captions, referencias cruzadas y pasajes finales de Results/Discussion dependientes de esas figuras permanecen sujetos al cierre experimental correspondiente. Esto no bloquea Architecture B02.

El último HEAD externo verificado durante la apertura de B02 fue `docs/plan-maestro-temporal-2026-08-31@b74b96d0163807007e4579d86450dd235125b30f`. Este dato es un snapshot de consulta, no una fuente que la IA Gestora pueda modificar.

## 9. Fase activa — Architecture B02

### 9.1 Alcance

Architecture B02 comprende exclusivamente:

- `3.5 Candidate-specific documentary retrieval` / `Recuperación documental específica por candidato`;
- `3.6 Evidence-context construction and controlled explanation` / `Construcción de contexto de evidencia y explicación controlada`;
- `3.7 Configurability and interface requirements` / `Configurabilidad y requisitos de interfaz`.

### 9.2 Función narrativa

La sección debe continuar la frontera ya congelada en B01:

`fixed Top-3 → candidate-specific documentary evidence → evidence-context construction → controlled local-LLM explanation → configurability/interface requirements`.

3.5 explica cómo se asocia evidencia documental identificable a cada candidato ya fijado sin modificar el ranking.

3.6 explica cómo se construye un contexto trazable que conserva descripción/consulta, candidato y posición, respaldo histórico disponible, evidencia documental y procedencia; luego fija el contrato del LLM como explicador downstream sin autoridad sobre el ranking.

3.7 explica qué recursos pueden reemplazarse en otra instanciación y qué interfaces deben preservarse. Debe dejar claro que pueden cambiar el banco histórico etiquetado, el espacio de clases objetivo y un corpus documental compatible, pero que esa configurabilidad no demuestra transferencia de desempeño.

### 9.3 Corpus que alimenta la explicación

B02 debe dejar explícito que la evidencia que alimenta el contexto de explicación procede de un corpus documental/normativo compatible y versionado para la instanciación. El corpus empírico concreto, sus documentos, preparación, vigencia temporal, segmentación e índice pertenecen a Section 4.3.

### 9.4 Repositorio de reproducibilidad

B02 debe explicar su función arquitectónica sin convertirla en un inventario experimental: conservar y distribuir, cuando sea posible, los artefactos versionados/trazables necesarios para reconstruir la instanciación evaluada —por ejemplo configuraciones, scripts, manifiestos, hashes, instrucciones y recursos redistribuibles—. Section 4.11 documentará los artefactos concretos, sus identidades y restricciones.

### 9.5 Fuentes mínimas

- `ARTICLE_MASTER_V008.md` como baseline canónico;
- `START_HERE.md`, `ARTICLE_STATUS.md`, este Plan, decisiones, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, `STYLE_GUIDE.md`;
- `SRC-02` para arquitectura/metodología operativa;
- fuentes de implementación únicamente cuando sea necesario verificar una interfaz o acción concreta, sin elevar decisiones particulares de la instanciación a requisitos universales.

### 9.6 Claims mínimos

Autorizados: C02, C03, C15, C17.

Prohibidos/restringidos: C12, C13, C16, C18.

### 9.7 Límites

B02 no debe:

- modificar Introduction, Related Work o 3.1–3.4;
- redactar Section 4 ni posteriores;
- introducir corpus concreto, parámetros, tamaños, hashes o resultados experimentales salvo que un identificador sea indispensable para trazabilidad interna y no aparezca como prosa publicable;
- convertir evidencia documental en corrección jurídica;
- convertir el LLM en clasificador;
- presentar reranking diagnóstico como flujo principal;
- convertir un modelo, prompt, índice, corpus o BM25 en requisito universal si la afirmación pretende describir la arquitectura general;
- declarar novelty, SOTA, generalización o `FINAL_GAP`;
- promover `ARTICLE_MASTER_V009`.

## 10. Ciclo obligatorio de cada bloque

```text
IA Gestora reconstruye estado y evidencia
→ IA Gestora abre/versiona bloque y prompt
→ IA de Redacción ejecuta solo el bloque
→ entrega artefactos y respuesta versionada
→ IA Gestora audita independientemente
→ corrección si corresponde
→ PASS
→ aprobación expresa del autor
→ IA Gestora integra/promueve técnicamente
→ IA Gestora continúa automáticamente hasta el siguiente gate real
```

Un `PASS` de la IA de Redacción no sustituye la auditoría de la IA Gestora. La aprobación autoral no sustituye la materialización canónica. La materialización canónica no autoriza por sí sola el bloque siguiente si el plan exige una decisión separada; en ese caso la IA Gestora debe emitirla sin pedir una confirmación redundante al autor.

## 11. Estado inmediato

```text
CURRENT_GATE = ARCHITECTURE_B02
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ARCHITECTURE_B02_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
BASELINE_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx
BASELINE_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
ARCHITECTURE_B02 = AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
ARTICLE_MASTER_V009 = NOT_AUTHORIZED
```

---

# English

## 1. Purpose

Manage the iterative construction of the main scientific article without anticipating results, changing the approved experimental design, or transferring internal governance language into manuscript prose. The article is built on a cumulative master; each authorized block completes that same base and becomes canonical only after Managing-AI audit and explicit author approval where the applicable gate requires it.

Drafting is governed by `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, the `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, frozen decisions, verified primary literature, and governing experimental sources when relevant.

## 2. Binding scientific and editorial principles

The article is not a shortened thesis. The reader encounters the problem and positioning first, then the general architecture, and only afterwards the concrete experimental instantiation. The experimental NANDINA/Class-87 setting must not define the architecture prematurely.

Historical retrieval generates and ranks candidates. The Top-3 is fixed before documentary retrieval and generation. Documentary/normative retrieval supplies evidence for already fixed candidates and cannot replace or reorder the historical ranking. The local LLM operates downstream for controlled explanation, does not classify from scratch, cannot alter candidates, and cannot feed information back into classification. LLM reranking remains diagnostic unless a later explicit decision changes that status.

The following boundaries remain binding: candidate retrieval is not overall classification accuracy; documentary association is not substantive legal correctness; auditability is not legal correctness; configurability/replicability is not empirical generalization; EXP11A is joint size/composition sensitivity rather than an isolated causal size effect; EXP11B is descriptive and does not support seed-superpopulation inference; EXP12 does not estimate a historical-diversity effect. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain unchanged.

Part I is the publication-facing English master. Part II is the Spanish semantic-control mirror. Abstract concepts must be expressed through observable components, inputs, actions, outputs, and constraints.

## 3. Approved cumulative architecture

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion
7. Conclusion
8. KBS end matter

The detailed structure remains in `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`, approved through D-015.

## 4. Cumulative master and DOCX policy

The canonical Markdown master is `ARTICLE_MASTER_V008.md`, SHA-256 `895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d`, Git blob `0145d13e1bc4e4fdeab79f7bad83d00f67221a76`.

The current cumulative DOCX is `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`, in effective local author custody, SHA-256 `f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4`, with 40 inherited comments.

D-021 defers routine DOCX repository upload; D-027 requires actual delivery of the exact binary to the author. D-035 requires timeout-safe handoff for large artifacts after a direct route has demonstrated timeout behavior. Manual Base64, fragmentation/chunking, and recomposition are not permitted as workarounds. Automatic internal encoding used by an API or connector is not manual Base64 and is not prohibited.

A missing exact DOCX baseline must stop drafting; it must not be silently reconstructed from Markdown.

## 5. Managing-AI operational continuity

The Managing AI must not introduce artificial pauses between satisfied gates.

When a gate is satisfied and the next action is deterministic, technical, and within its mandate — such as materializing an already approved master, updating status, opening the next eligible block, or versioning its prompt — it proceeds automatically without requiring the author to type “continue” or perform an operation the Managing AI can execute.

The Managing AI stops only for a genuine gate requiring author scientific/editorial judgment, an unavailable exact artifact, a decision/evidence source controlled by the Experimental AI or another authority, an unresolved governing-source contradiction, or missing evidence required for the task.

Automatic continuity removes artificial pauses; it does not remove author-approval gates.

## 6. Phase and block state

| Element | State |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| KBS Structure V01 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work 2.1–2.6 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction B01 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture B01 — 3.1–3.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Canonical master | `ARTICLE_MASTER_V008.md` |
| Architecture B02 — 3.5–3.7 | AUTHORIZED / ACTIVE |
| Experimental design | NOT_AUTHORIZED |
| Results | NOT_AUTHORIZED |
| Discussion | NOT_AUTHORIZED |
| Conclusion | NOT_AUTHORIZED |

Experimental groups are not managed in this editorial state table. Their state is read from `SRC-03` only when an editorial gate materially depends on it.

## 7. Drafting sequence

The operational sequence is: approved structure → Related Work → Introduction → Architecture B01 → Architecture B02 → Experimental design → provisional Results → required visualizations → final Results → Discussion/Limitations → Conclusion → Abstract → Title/Keywords → transversal synchronization → final scientific audit/freeze → KBS adaptation.

Architecture B02 is the only currently authorized drafting block. Experimental design requires a separate editorial authorization after Architecture B02 has been audited, approved by the author, and integrated.

## 8. Concurrency with the experimental process

The editorial and experimental processes are related but distinct. Only the Experimental AI manages the experimental Master Plan. The Managing AI reads it when an editorial claim or gate depends on experimental facts.

D-034 remains binding: formal Group-7 activation requires Group-6 closure, but Architecture and Experimental-design drafting do not; G7-F03 is synchronization/transversal closure rather than article inception; final scientific-freeze readiness requires the later audit sequence. Figure numbering/captions/cross-references and figure-dependent final Results/Discussion prose remain subject to the relevant experimental closure.

The latest external HEAD verified when B02 was opened was `docs/plan-maestro-temporal-2026-08-31@b74b96d0163807007e4579d86450dd235125b30f`. This is a read-only snapshot for the Managing AI.

## 9. Active phase — Architecture B02

Architecture B02 exclusively covers Sections 3.5–3.7: candidate-specific documentary retrieval; evidence-context construction and controlled explanation; configurability and interface requirements.

Its narrative continuation is:

`fixed Top-3 → candidate-specific documentary evidence → evidence-context construction → controlled local-LLM explanation → configurability/interface requirements`.

Section 3.5 explains how identifiable documentary evidence is associated with each already fixed candidate without changing ranking. Section 3.6 explains how a traceable context preserves the description/query, fixed candidate and position, available historical support, documentary evidence, and provenance, and then constrains the LLM to explanation only. Section 3.7 explains which resources can be replaced in another instantiation and which interfaces must remain stable.

B02 must explicitly state that explanation context is fed by a compatible versioned documentary/normative corpus, while deferring the concrete experimental corpus, preparation, temporal validity, segmentation, and index to Section 4.3. It must also state the architectural role of the reproducibility repository — preserving/distributing versioned and traceable artifacts required to reconstruct the evaluated instantiation — while deferring the final concrete artifact inventory and restrictions to Section 4.11.

Minimum authorized claims: C02, C03, C15, C17. Prohibited/restricted claims: C12, C13, C16, C18.

B02 must not edit Introduction, Related Work, or 3.1–3.4; draft Section 4 or later sections; introduce experimental results; convert documentary evidence into legal correctness; convert the LLM into a classifier; present diagnostic reranking as the primary architecture; universalize one implementation-specific model, prompt, index, corpus, or BM25; declare novelty, SOTA, empirical generalization, or `FINAL_GAP`; or promote `ARTICLE_MASTER_V009`.

## 10. Mandatory block cycle

```text
Managing AI reconstructs state/evidence
→ Managing AI opens and versions block/prompt
→ Drafting AI executes only that block
→ Drafting AI delivers artifacts and versioned response
→ Managing AI independently audits
→ correction if needed
→ PASS
→ explicit author approval
→ Managing AI performs canonical integration/promotion
→ Managing AI automatically continues until the next genuine gate
```

A Drafting-AI PASS does not replace Managing-AI audit. Author approval does not replace canonical materialization. Canonical materialization does not itself authorize a later block if a separate editorial decision is required; the Managing AI issues that decision without requesting redundant author confirmation.

## 11. Immediate state

```text
CURRENT_GATE = ARCHITECTURE_B02
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ARCHITECTURE_B02_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
BASELINE_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx
BASELINE_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
ARCHITECTURE_B02 = AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
ARTICLE_MASTER_V009 = NOT_AUTHORIZED
```
