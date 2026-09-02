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

### Equivalencia operativa del Plan Maestro

La copia GitHub de `SRC-03` se considera, para el proceso del artículo, **equivalente operativo** de la copia local iterativa denominada `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md` mientras el autor no indique lo contrario.

La fuente operativa se identifica por:

- repositorio: `elVladdi/gci-nandina-rag`;
- rama: `docs/plan-maestro-temporal-2026-08-31`;
- ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

`SRC-03` es una **fuente viva** mientras la investigación experimental permanezca abierta. Por ello, el blob SHA no define de forma permanente la identidad de la fuente. En cada corte de análisis o revisión debe registrarse el blob SHA efectivamente leído como **snapshot de ese corte**. Un cambio de blob SHA en la misma rama y ruta no constituye por sí solo un bloqueo; debe comprobarse qué cambió y si el nuevo contenido altera claims, estados, resultados o decisiones ya utilizados por el artículo.

Snapshot verificado durante la revisión de 0A-01 del 2026-09-02:

- blob SHA: `0a9a82181c6c3840f74f0272e5c225568474058b`.

La equivalencia significa que las IAs del artículo deben consultar directamente la copia GitHub para el estado experimental y **no deben exigir que el autor adjunte la copia local v20**.

Un cambio de rama, ruta o decisión de equivalencia sí requiere actualización explícita de este registro y, cuando corresponda, una nueva decisión en `DECISIONS.md`.

### Regla sobre nombres de archivos adjuntos

Los sufijos generados por la plataforma al adjuntar copias, por ejemplo `(3)`, `(4)` o `(5)`, no se interpretan automáticamente como versiones científicas o metodológicas distintas. La identidad documental se determina por el contenido, la versión interna cuando exista y la indicación expresa del autor sobre cuál copia está vigente.

Cuando dos copias tengan diferencias de contenido reales, deben tratarse como versiones distintas y compararse antes de sustituir una por otra.

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

### Operational equivalence of the Master Plan

The GitHub copy of `SRC-03` is considered, for the article workflow, the **operational equivalent** of the iterative local copy named `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md` unless the author states otherwise.

The operational source is identified by:

- repository: `elVladdi/gci-nandina-rag`;
- branch: `docs/plan-maestro-temporal-2026-08-31`;
- path: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

`SRC-03` is a **living source** while the experimental research remains open. Therefore, a blob SHA does not permanently define the identity of the source. At each analysis or review cutoff, the blob SHA actually read must be recorded as the **snapshot for that cutoff**. A changed blob SHA at the same branch and path is not by itself a blocker; the changes must be inspected to determine whether they alter claims, statuses, results, or decisions already used by the article.

Snapshot verified during the 0A-01 review on 2026-09-02:

- blob SHA: `0a9a82181c6c3840f74f0272e5c225568474058b`.

This equivalence means that article AIs must consult the GitHub copy directly for experimental status and **must not require the author to attach the local v20 copy**.

A change in branch, path, or equivalence decision does require an explicit update to this registry and, where applicable, a new decision in `DECISIONS.md`.

### Rule for attachment filenames

Suffixes generated by the platform when attaching copies, such as `(3)`, `(4)`, or `(5)`, are not automatically interpreted as distinct scientific or methodological versions. Documentary identity is determined by content, an internal version where available, and the author's explicit indication of which copy is current.

When two copies contain actual content differences, they must be treated as distinct versions and compared before one replaces the other.

### Precedence by dimension

1. Experimental status: `SRC-03` + frozen artifacts/commits from the development repository.
2. Operational architecture and methodology: `SRC-02`.
3. Approved problem, objectives, hypotheses, justification, and scope: `SRC-01`.
4. Later formulations and preliminary thesis wording: `SRC-04`.
5. Scientific literature: `BIBLIOGRAPHIC_FRAMEWORK.md` and verified PDFs.

A discrepancy between sources must not be resolved silently. It must be identified, classified, and submitted to the applicable gate.
