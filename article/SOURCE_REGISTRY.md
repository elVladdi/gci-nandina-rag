# Registro de fuentes / Source Registry

## Español

### Propósito

Este archivo identifica las fuentes primarias y operativas que gobiernan la redacción del artículo y evita ambigüedades entre copias locales, ramas GitHub y versiones documentales.

### Fuentes nucleares actuales

| ID | Fuente | Ubicación vigente | Función | Estado |
|---|---|---|---|---|
| SRC-01 | Proyecto de tesis aprobado | archivo adjunto proporcionado por el autor cuando sea requerido | problema, objetivos, hipótesis, justificación y alcance aprobados | REQUIRED |
| SRC-02 | Anexo metodológico vigente | `Anexo_1_NANDINA_LLM_RAG_v13.docx` o versión posterior expresamente aprobada, proporcionada por el autor cuando sea requerida | arquitectura y metodología operativa vigente | REQUIRED |
| SRC-03 | Plan Maestro experimental | repositorio `elVladdi/gci-nandina-rag`, rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | estado experimental actual | LIVING_SOURCE_IN_GITHUB |
| SRC-04 | Tesis preliminar vigente | última copia que el autor identifique como tesis preliminar vigente; los sufijos automáticos de adjunto como `(3)` o `(4)` no constituyen por sí solos una versión metodológica | síntesis posterior y detección de discrepancias; no sustituye formulaciones aprobadas ni estado experimental | REQUIRED_FOR_COMPARISON |

### Plan Maestro: documento lógico único y fuente viva

`SRC-03` representa un **único documento lógico** con dos copias operativas sincronizadas:

1. la copia local gestionada dentro del flujo experimental;
2. la copia viva versionada en GitHub, que es la fuente consumida directamente por el flujo del artículo.

La copia GitHub está ubicada en:

- repositorio: `elVladdi/gci-nandina-rag`;
- rama: `docs/plan-maestro-temporal-2026-08-31`;
- ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

La denominación local `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md` identifica la copia iterativa vigente en el corte inicialmente registrado; el nombre local puede evolucionar dentro del flujo experimental sin crear por ello un segundo Plan Maestro vigente.

No se admiten copias divergentes como versiones simultáneamente válidas. La copia local vigente y la copia GitHub deben contener el **mismo contenido textual canónico**: ninguna puede incorporar líneas, secciones, resultados, decisiones o estados ausentes de la otra. La sincronización no se satisface únicamente mediante equivalencia semántica. Las diferencias exclusivamente atribuibles a la representación técnica de fin de línea, por ejemplo CRLF frente a LF, no constituyen divergencia documental cuando el contenido textual canónico es idéntico.

Después de una actualización experimental, ambas copias deben volver a cumplir esta sincronización exacta antes de que el artículo consuma el nuevo estado. Si se detecta divergencia, esta se registra como inconsistencia documental y debe ser corregida exclusivamente por el flujo experimental.

**Autoridad de escritura:** solo la IA experimental puede modificar el Plan Maestro, tanto localmente como en GitHub. La IA editora científica del artículo y la IA de redacción tienen acceso de solo lectura y no pueden modificar, fusionar, elegir entre copias divergentes ni reconciliarlas por inferencia.

`SRC-03` es una **fuente viva** mientras la investigación experimental permanezca abierta. Por ello, el blob SHA no define de forma permanente la identidad de la fuente. En cada corte de análisis o revisión debe registrarse el blob SHA efectivamente leído como **snapshot de ese corte**. Un cambio de blob SHA en la misma rama y ruta no constituye por sí solo un bloqueo; debe comprobarse qué cambió y si el nuevo contenido altera claims, estados, resultados o decisiones ya utilizados por el artículo.

Snapshots registrados:

- revisión de 0A-01, 2026-09-02: blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- reconciliación editorial final de 0B-05C, 2026-09-15: rama HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob SHA leído `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`;
- reconciliación editorial posterior al cierre de Grupo 3 y la integración de G4-F01, 2026-09-20: rama HEAD `2237ddc46bc1c7bfac203753bdcf2c7d4592f83e`, blob SHA leído `fb5caa26fc0abca0506fbc7b75bbf15af24a8875`; checkpoint experimental `main = 9f549ebdf940f9d806d5088697394d0c927f9fdc`.

El último snapshot registra el siguiente estado canónico consumible por el artículo:

```text
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03 = NOT_AUTHORIZED
```

Este snapshot no autoriza por sí mismo la redacción de Results ni Discussion: el gate editorial del artículo continúa siendo independiente. Cuando se abran esas secciones, los claims derivados de Grupo 3 deberán respetar el cierre de G3-F04 y el puente claim–evidencia controlado de G4-F01. EXP11A se interpreta únicamente como sensibilidad conjunta tamaño/composición; EXP11B permanece descriptivo; el efecto de diversidad de EXP12 no es estimable porque el experimento cerró sin retrieval. G4-F02 y G4-F03 no pueden consumirse como evidencia cerrada mientras `SRC-03` no registre el estado requerido.

Los snapshots se registran únicamente como cortes de lectura de la fuente viva. No reemplazan ni reescriben los snapshots históricos utilizados por los experimentos ni convierten el Plan Maestro en una fuente inmutable.

Las IAs del artículo deben consultar directamente la copia GitHub para el estado experimental y **no deben exigir que el autor adjunte la copia local**.

D-011 supersede a D-009 en todo lo relativo a sincronización, coexistencia y divergencia entre las copias local y GitHub. D-009 conserva únicamente la identificación de la fuente operativa y su carácter de fuente viva.

Un cambio de rama, ruta o regla de gobernanza sí requiere actualización explícita de este registro y, cuando corresponda, una nueva decisión en `DECISIONS.md`.

### Regla sobre nombres de archivos adjuntos

Los sufijos generados por la plataforma al adjuntar copias, por ejemplo `(3)`, `(4)` o `(5)`, no se interpretan automáticamente como versiones científicas o metodológicas distintas. La identidad documental se determina por el contenido, la versión interna cuando exista y la indicación expresa del autor sobre cuál copia está vigente.

Cuando dos copias tengan diferencias de contenido reales, deben tratarse como versiones distintas y compararse antes de sustituir una por otra, salvo el Plan Maestro, cuya divergencia se rige específicamente por D-011 y debe resolverse dentro del flujo experimental.

### Precedencia por dimensión

1. Estado experimental: `SRC-03` + artefactos/commits congelados del repositorio de desarrollo.
2. Arquitectura y metodología operativa: `SRC-02`.
3. Problema, objetivos, hipótesis, justificación y alcance aprobados: `SRC-01`.
4. Formulaciones posteriores y borrador de tesis: `SRC-04`.
5. Literatura científica: `BIBLIOGRAPHIC_FRAMEWORK.md` y PDFs verificados.

Una discrepancia entre fuentes no debe resolverse silenciosamente. Debe identificarse, clasificarse y someterse al gate correspondiente.

---

## English

### Purpose

This file identifies the primary and operational sources governing article writing and prevents ambiguity among local copies, GitHub branches, and documentary versions.

### Current nuclear sources

| ID | Source | Current location | Function | Status |
|---|---|---|---|---|
| SRC-01 | Approved thesis project | attachment supplied by the author when required | approved problem, objectives, hypotheses, justification, and scope | REQUIRED |
| SRC-02 | Current methodological Annex | `Anexo_1_NANDINA_LLM_RAG_v13.docx` or a later expressly approved version, supplied by the author when required | current operational architecture and methodology | REQUIRED |
| SRC-03 | Experimental Master Plan | repository `elVladdi/gci-nandina-rag`, branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | current experimental status | LIVING_SOURCE_IN_GITHUB |
| SRC-04 | Current preliminary thesis | latest copy identified by the author as the current preliminary thesis; automatic attachment suffixes such as `(3)` or `(4)` do not by themselves constitute a methodological version | later synthesis and discrepancy detection; does not replace approved formulations or experimental status | REQUIRED_FOR_COMPARISON |

### Master Plan: one logical document and living source

`SRC-03` represents **one logical document** with two synchronized operational copies:

1. the local copy managed within the experimental workflow;
2. the living versioned GitHub copy, which is the source directly consumed by the article workflow.

The GitHub copy is located at:

- repository: `elVladdi/gci-nandina-rag`;
- branch: `docs/plan-maestro-temporal-2026-08-31`;
- path: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

The local name `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md` identifies the current iterative copy at the initially registered cutoff; the local filename may evolve within the experimental workflow without thereby creating a second current Master Plan.

Divergent copies are not allowed as simultaneously valid versions. The current local copy and the GitHub copy must contain the **same canonical textual content**: neither may contain lines, sections, results, decisions, or statuses absent from the other. Synchronization is not satisfied merely by semantic equivalence. Differences attributable exclusively to the technical representation of line endings, such as CRLF versus LF, do not constitute documentary divergence when the canonical textual content is identical.

After an experimental update, both copies must again satisfy this exact synchronization before the article consumes the new state. If divergence is detected, it is recorded as a documentary inconsistency and must be corrected exclusively by the experimental workflow.

**Write authority:** only the experimental AI may modify the Master Plan, both locally and on GitHub. The article scientific-editor AI and drafting AI have read-only access and may not modify, merge, choose between divergent copies, or reconcile them by inference.

`SRC-03` is a **living source** while the experimental research remains open. Therefore, a blob SHA does not permanently define the identity of the source. At each analysis or review cutoff, the blob SHA actually read must be recorded as the **snapshot for that cutoff**. A changed blob SHA at the same branch and path is not by itself a blocker; the changes must be inspected to determine whether they alter claims, statuses, results, or decisions already used by the article.

Recorded snapshots:

- 0A-01 review, 2026-09-02: blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- final 0B-05C editorial reconciliation, 2026-09-15: branch HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, read blob SHA `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`;
- editorial reconciliation after Group 3 closure and G4-F01 integration, 2026-09-20: branch HEAD `2237ddc46bc1c7bfac203753bdcf2c7d4592f83e`, read blob SHA `fb5caa26fc0abca0506fbc7b75bbf15af24a8875`; experimental checkpoint `main = 9f549ebdf940f9d806d5088697394d0c927f9fdc`.

The latest snapshot records the following canonical state consumable by the article:

```text
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = IN_PROGRESS
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G4_F03 = NOT_AUTHORIZED
```

This snapshot does not by itself authorize drafting Results or Discussion: the article editorial gate remains independent. When those sections are opened, Group 3 claims must respect the G3-F04 closure and the controlled G4-F01 claim–evidence bridge. EXP11A is interpreted only as joint size/composition sensitivity; EXP11B remains descriptive; the EXP12 diversity effect is not estimable because that experiment closed without retrieval. G4-F02 and G4-F03 cannot be consumed as closed evidence until `SRC-03` records the required state.

Snapshots are recorded only as reading cutoffs for the living source. They do not replace or rewrite historical snapshots used by the experiments and do not turn the Master Plan into an immutable source.

Article AIs must consult the GitHub copy directly for experimental status and **must not require the author to attach the local copy**.

D-011 supersedes D-009 for all matters concerning synchronization, coexistence, and divergence between the local and GitHub copies. D-009 retains only the identification of the operational source and its living-source character.

A change in branch, path, or governance rule does require an explicit update to this registry and, where applicable, a new decision in `DECISIONS.md`.

### Rule for attachment filenames

Suffixes generated by the platform when attaching copies, such as `(3)`, `(4)`, or `(5)`, are not automatically interpreted as distinct scientific or methodological versions. Documentary identity is determined by content, an internal version where available, and the author's explicit indication of which copy is current.

When two copies contain actual content differences, they must be treated as distinct versions and compared before one replaces another, except for the Master Plan, whose divergence is specifically governed by D-011 and must be resolved within the experimental workflow.

### Precedence by dimension

1. Experimental status: `SRC-03` + frozen artifacts/commits from the development repository.
2. Operational architecture and methodology: `SRC-02`.
3. Approved problem, objectives, hypotheses, justification, and scope: `SRC-01`.
4. Later formulations and preliminary thesis wording: `SRC-04`.
5. Scientific literature: `BIBLIOGRAPHIC_FRAMEWORK.md` and verified PDFs.

A discrepancy between sources must not be resolved silently. It must be identified, classified, and submitted to the applicable gate.