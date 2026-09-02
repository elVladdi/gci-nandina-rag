# Registro de fuentes / Source Registry

## Español

### Propósito

Este archivo identifica las fuentes primarias y operativas que gobiernan la redacción del artículo y evita ambigüedades entre copias locales, ramas GitHub y versiones documentales.

### Fuentes nucleares actuales

| ID | Fuente | Ubicación vigente | Función | Estado |
|---|---|---|---|---|
| SRC-01 | Proyecto de tesis aprobado | archivo adjunto proporcionado por el autor cuando sea requerido | problema, objetivos, hipótesis, justificación y alcance aprobados | REQUIRED |
| SRC-02 | Anexo metodológico vigente | `Anexo_1_NANDINA_LLM_RAG_v13.docx` o versión posterior expresamente aprobada, proporcionada por el autor cuando sea requerida | arquitectura y metodología operativa vigente | REQUIRED |
| SRC-03 | Plan Maestro experimental | repositorio `elVladdi/gci-nandina-rag`, rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | estado experimental actual | AVAILABLE_IN_GITHUB |
| SRC-04 | Tesis preliminar vigente | archivo adjunto vigente proporcionado por el autor; para 0A-01: `Molleapasa_gv(3).docx` | síntesis posterior y detección de discrepancias; no sustituye formulaciones aprobadas | REQUIRED_FOR_COMPARISON |

### Equivalencia operativa del Plan Maestro

La copia GitHub de `SRC-03` se considera, para el proceso del artículo, **equivalente operativo** de la copia local iterativa denominada `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md`.

La copia GitHub actualmente verificada está en:

- repositorio: `elVladdi/gci-nandina-rag`;
- rama: `docs/plan-maestro-temporal-2026-08-31`;
- ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- blob SHA verificado: `f90c73fbad9cfba1b2bfc403b05ad929dc4193db`.

Esta equivalencia significa que las IAs del artículo deben consultar directamente la copia GitHub para el estado experimental y **no deben exigir que el autor adjunte la copia local v20** mientras esta equivalencia permanezca vigente.

Si la rama, ruta, contenido o equivalencia cambian, debe registrarse una nueva decisión y actualizar este archivo antes de usar una versión diferente.

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
| SRC-03 | Experimental Master Plan | repository `elVladdi/gci-nandina-rag`, branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | current experimental status | AVAILABLE_IN_GITHUB |
| SRC-04 | Current preliminary thesis | current attachment supplied by the author; for 0A-01: `Molleapasa_gv(3).docx` | later synthesis and discrepancy detection; does not replace approved formulations | REQUIRED_FOR_COMPARISON |

### Operational equivalence of the Master Plan

The GitHub copy of `SRC-03` is considered, for the article workflow, the **operational equivalent** of the iterative local copy named `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md`.

The currently verified GitHub copy is located at:

- repository: `elVladdi/gci-nandina-rag`;
- branch: `docs/plan-maestro-temporal-2026-08-31`;
- path: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`;
- verified blob SHA: `f90c73fbad9cfba1b2bfc403b05ad929dc4193db`.

This equivalence means that article AIs must consult the GitHub copy directly for experimental status and **must not require the author to attach the local v20 copy** while this equivalence remains valid.

If the branch, path, content, or equivalence changes, a new decision must be recorded and this file must be updated before another version is used.

### Precedence by dimension

1. Experimental status: `SRC-03` + frozen artifacts/commits from the development repository.
2. Operational architecture and methodology: `SRC-02`.
3. Approved problem, objectives, hypotheses, justification, and scope: `SRC-01`.
4. Later formulations and preliminary thesis wording: `SRC-04`.
5. Scientific literature: `BIBLIOGRAPHIC_FRAMEWORK.md` and verified PDFs.

A discrepancy between sources must not be resolved silently. It must be identified, classified, and submitted to the applicable gate.
