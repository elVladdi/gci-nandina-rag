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
| SRC-04 | Tesis preliminar vigente | última copia que el autor identifique como tesis preliminar vigente | síntesis posterior y detección de discrepancias; no sustituye formulaciones aprobadas ni estado experimental | REQUIRED_FOR_COMPARISON |

### Plan Maestro: documento lógico único y fuente viva

`SRC-03` representa un único documento lógico con dos copias operativas sincronizadas: la copia local gestionada por el flujo experimental y la copia viva versionada en GitHub consumida por el artículo.

Ubicación GitHub gobernante:

- repositorio: `elVladdi/gci-nandina-rag`;
- rama: `docs/plan-maestro-temporal-2026-08-31`;
- ruta: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

No se admiten copias divergentes como simultáneamente válidas. Solo la IA Experimental tiene autoridad de escritura sobre el Plan Maestro. La IA Gestora y la IA de Redacción lo consultan en modo de solo lectura y no pueden reconciliar divergencias por inferencia.

`SRC-03` es una fuente viva. El blob SHA identifica el snapshot efectivamente leído en cada corte editorial, no una identidad permanente de la fuente.

### Snapshots registrados

- revisión de 0A-01, 2026-09-02: blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- reconciliación editorial final de 0B-05C, 2026-09-15: rama HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob SHA `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`;
- reconciliación posterior al cierre de Grupo 3 y G4-F01, 2026-09-20: rama HEAD `2237ddc46bc1c7bfac203753bdcf2c7d4592f83e`, blob SHA `fb5caa26fc0abca0506fbc7b75bbf15af24a8875`, checkpoint `main = 9f549ebdf940f9d806d5088697394d0c927f9fdc`;
- reconciliación posterior al cierre completo de Grupo 4, 2026-09-20: rama HEAD `3ba3557eb10e741b8f49c420850940dee1df08ef`, blob SHA `5ab0af7af5a2c92a1107e820bee1a6bb65026432`, checkpoint experimental `main = 38e22c19a0eb0d344e7675761a88d7968091eead`;
- **reconciliación posterior al cierre completo de Grupo 5, 2026-09-21**: rama HEAD `98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e`, blob SHA `9b388fe8cc19fce86ec3c15853e73899cb3e5666`, checkpoint experimental `main = ca065618d5df0019f76ef5a971e858d91c263e1f`.

### Último snapshot canónico consumible por el artículo

```text
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F04 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03_EXTERNAL_REAUDIT = PASS
G4_F03_COMPARISON_REGISTRY_COUNT = 11
G4_F03_AUTHORIZED_DISCUSSION_POINT_COUNT = 8
G4_F03_FORBIDDEN_DISCUSSION_POINT_COUNT = 14
GROUP5 = CLOSED / APPROVED
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F01_INTEGRATION_COMMIT = d5729887f47c36d8cf42d87090c40f9668e5ae84
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02_INTEGRATION_COMMIT = e471d4336ab965cd55b7f0e2ca7926445b1f0391
G5_F02_EXTERNAL_REAUDIT = PASS
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03_INTEGRATION_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
G5_F03_EXTERNAL_AUDIT = PASS
GROUP5_CANONICAL_TABLE_COUNT = 9
GROUP6 = NOT_STARTED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
```

### Material de Grupo 4 para uso editorial posterior

El cierre G4-F03 integró el artefacto:

`docs/analysis/group4/g4_literature_contrast_v0.1.md`

checkpoint: `main@38e22c19a0eb0d344e7675761a88d7968091eead`.

Este artefacto contiene 11 registros de contraste, 8 puntos de discusión autorizados y 14 puntos de discusión prohibidos. Su uso queda subordinado al gate editorial correspondiente. En particular:

- no autoriza comparar porcentajes o métricas entre estudios no directamente comparables;
- no autoriza SOTA, superioridad frente a la literatura, novelty absoluta, ser el primero o unicidad;
- no convierte EXP11A en efecto causal del tamaño;
- no permite generalizar EXP11B a una superpoblación de seeds;
- no convierte EXP12 en inviabilidad global ni en evidencia a favor o en contra de HE5;
- no convierte rendimiento del retrieval histórico en exactitud global del RAG;
- no convierte evidencia normativa, oficialidad documental, rationale, path validity, provenance o reproducibilidad en corrección jurídica, clasificación correcta o auditabilidad formal por salida.

### Material de Grupo 5 para futura Results

Grupo 5 quedó `CLOSED / APPROVED` después del cierre auditado de G5-F01, G5-F02 y G5-F03. El checkpoint final es `main@ca065618d5df0019f76ef5a971e858d91c263e1f`.

Los artefactos G5 organizan evidencia ya congelada; no introducen nuevas métricas o inferencia. El sistema de presentación contiene nueve tablas canónicas:

- 2 principales con rol inferencial (`G5-MAIN-01`, `G5-MAIN-02`);
- 2 secundarias/descriptivas (`G5-SECONDARY-01`, `G5-SECONDARY-02`);
- 5 de apéndice/suplemento (`G5-APPENDIX-01..05`).

Además, G5-F03 conserva destinos `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON` para evidencia no estimable y guardrails. Estos roles son vinculantes para la futura redacción de Results: Phase E y HE5 descriptivo no pueden promoverse a evidencia confirmatoria; EXP11A sigue siendo sensibilidad conjunta tamaño/composición no causal; EXP11B sigue siendo descriptivo sin inferencia a superpoblación de seeds; EXP12 sigue siendo no estimable.

El cierre de Grupo 5 no abre automáticamente Results, Discussion ni Figuras y no modifica `FINAL_GAP` ni `NOVELTY`. G6-F01 es únicamente elegible y permanece no autorizado/no ejecutado.

### Regla sobre nombres de archivos adjuntos

Los sufijos generados por la plataforma al adjuntar copias, como `(3)`, `(4)` o `(5)`, no se interpretan automáticamente como versiones científicas distintas. La identidad documental se determina por contenido, versión interna cuando exista e indicación expresa del autor.

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
| SRC-02 | Current methodological Annex | `Anexo_1_NANDINA_LLM_RAG_v13.docx` or a later expressly approved version | current operational architecture and methodology | REQUIRED |
| SRC-03 | Experimental Master Plan | repository `elVladdi/gci-nandina-rag`, branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | current experimental status | LIVING_SOURCE_IN_GITHUB |
| SRC-04 | Current preliminary thesis | latest copy identified by the author | later synthesis and discrepancy detection; does not replace approved formulations or experimental status | REQUIRED_FOR_COMPARISON |

### Master Plan: one logical document and living source

`SRC-03` is a living source. Only the Experimental AI has write authority. The article Managing AI and Drafting AI consume the synchronized GitHub copy in read-only mode and may not reconcile divergence by inference.

Governing GitHub location:

- repository: `elVladdi/gci-nandina-rag`;
- branch: `docs/plan-maestro-temporal-2026-08-31`;
- path: `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

Recorded snapshots include the 0A-01 cutoff, the 0B-05C reconciliation, the Group-3/G4-F01 reconciliation, full Group 4 closure, and the latest cutoff after full Group 5 closure.

Latest canonical snapshot, 2026-09-21:

- Master Plan HEAD: `98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e`;
- read blob SHA: `9b388fe8cc19fce86ec3c15853e73899cb3e5666`;
- experimental `main` checkpoint: `ca065618d5df0019f76ef5a971e858d91c263e1f`.

```text
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03_EXTERNAL_REAUDIT = PASS
GROUP5 = CLOSED / APPROVED
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03_EXTERNAL_AUDIT = PASS
GROUP5_CANONICAL_TABLE_COUNT = 9
GROUP6 = NOT_STARTED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

The Group 4 closure artifact `docs/analysis/group4/g4_literature_contrast_v0.1.md` continues to control future literature contrast: 11 comparison records, 8 authorized discussion points, and 14 forbidden discussion points. These controls do not authorize cross-study numerical superiority, SOTA, absolute novelty, empirical generalization, unsupported causality, or legal correctness.

Group 5 closes result presentation without introducing new metrics or inference. Its nine-table system comprises two primary inferential tables, two secondary/descriptive tables, and five appendix/supplementary tables, together with text-only and not-presented-as-result destinations for non-estimable evidence and guardrails. These roles are binding for future Results once its editorial gate opens. Group 5 closure does not itself open Results, Discussion, or figures. Group 6 remains not started; G6-F01 is only eligible and remains unauthorized/unexecuted.

### Precedence by dimension

1. Experimental status: `SRC-03` plus frozen development-repository artifacts/commits.
2. Operational architecture and methodology: `SRC-02`.
3. Approved problem, objectives, hypotheses, justification, and scope: `SRC-01`.
4. Later formulations and preliminary thesis wording: `SRC-04`.
5. Scientific literature: `BIBLIOGRAPHIC_FRAMEWORK.md` and verified PDFs.

A discrepancy between sources must not be resolved silently; it must be identified and submitted to the applicable gate.