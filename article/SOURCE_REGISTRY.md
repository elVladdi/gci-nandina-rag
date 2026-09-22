# Registro de fuentes / Source Registry

## Español

### Propósito

Este archivo identifica las fuentes primarias y operativas que gobiernan la redacción del artículo y evita ambigüedades entre copias locales, ramas GitHub y versiones documentales.

### Fuentes nucleares actuales

| ID | Fuente | Ubicación vigente | Función | Estado |
|---|---|---|---|---|
| SRC-01 | Proyecto de tesis aprobado | archivo adjunto proporcionado por el autor cuando sea requerido | problema, objetivos, hipótesis, justificación y alcance aprobados | REQUIRED |
| SRC-02 | Anexo metodológico vigente | `Anexo_1_NANDINA_LLM_RAG_v13.docx` o versión posterior expresamente aprobada | arquitectura y metodología operativa vigente | REQUIRED |
| SRC-03 | Plan Maestro experimental | repo `elVladdi/gci-nandina-rag`, rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | estado experimental actual | LIVING_SOURCE_IN_GITHUB |
| SRC-04 | Tesis preliminar vigente | última copia identificada por el autor | síntesis posterior y detección de discrepancias; no sustituye estado experimental ni formulaciones aprobadas | REQUIRED_FOR_COMPARISON |

### SRC-03 — fuente viva y autoridad

`SRC-03` representa un único documento lógico. Solo la IA Experimental tiene autoridad de escritura sobre el Plan Maestro. La IA Gestora y la IA de Redacción lo consultan en modo de solo lectura y no pueden reconciliar divergencias por inferencia.

Ubicación gobernante:

```text
REPOSITORY = elVladdi/gci-nandina-rag
BRANCH = docs/plan-maestro-temporal-2026-08-31
PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

El blob SHA identifica el snapshot efectivamente leído en cada corte editorial y no una identidad permanente de la fuente.

### Snapshots registrados

- 0A-01, 2026-09-02: blob `0a9a82181c6c3840f74f0272e5c225568474058b`.
- 0B-05C final, 2026-09-15: HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`.
- cierre Grupo 3 + G4-F01, 2026-09-20: HEAD `2237ddc46bc1c7bfac203753bdcf2c7d4592f83e`, blob `fb5caa26fc0abca0506fbc7b75bbf15af24a8875`, `main=9f549ebdf940f9d806d5088697394d0c927f9fdc`.
- cierre completo Grupo 4, 2026-09-20: HEAD `3ba3557eb10e741b8f49c420850940dee1df08ef`, blob `5ab0af7af5a2c92a1107e820bee1a6bb65026432`, `main=38e22c19a0eb0d344e7675761a88d7968091eead`.
- cierre completo Grupo 5, 2026-09-21: HEAD `98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e`, blob `9b388fe8cc19fce86ec3c15853e73899cb3e5666`, `main=ca065618d5df0019f76ef5a971e858d91c263e1f`.
- **apertura de Experimental Design B01, 2026-09-22**: HEAD `b74b96d0163807007e4579d86450dd235125b30f`, blob `7b63fdb14b75eace173ac3c94775d39ed7ed7a57`, `main=b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`.

### Último snapshot canónico consumible por el artículo

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
G4_F03_COMPARISON_REGISTRY_COUNT = 11
G4_F03_AUTHORIZED_DISCUSSION_POINT_COUNT = 8
G4_F03_FORBIDDEN_DISCUSSION_POINT_COUNT = 14
GROUP5 = CLOSED / APPROVED
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5_CANONICAL_TABLE_COUNT = 9
GROUP6 = IN_PROGRESS
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01_INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Este estado experimental no bloquea Architecture ni Experimental Design por sí mismo conforme a D-034. No autoriza Results, Discussion ni un freeze científico final.

### Fuentes técnicas congeladas relevantes para Experimental Design B01

En el checkpoint de desarrollo `main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`:

- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`, blob `bcb02c9c3493235a6f80991158c5b24fa7c04510` — identidad, composición y auditorías de H100/DEV/EVAL v0.2;
- `src/configs/data_aduanas_split_clase87_v0.2.json`, blob `059eb81677dad92d6f9241f0b8cbbff9bba332cd` — asignaciones explícitas de DAM y requisitos de split;
- `docs/exp04_bm25_historico_v02_inventory.md`, blob `64e7049ae8fb056a5fcc2173b39bdcb244567a89` — inventario de la evaluación histórica y gates de identidad;
- `src/ingestion/sunat_series_parser.py`, blob `87dafb5f2b5f1febfc588b7b763adc9ab5523339` — parser de series;
- `src/ingestion/prepare_new_historical_multisheet_v0.1.py`, blob `748c7b7ed7d55a1c2f05a76e1b382ee0077f158f` — preparación histórica multisheet.

Las fuentes de desarrollo se consultan para hechos técnicos concretos. No sustituyen `SRC-03` como fuente del estado experimental.

### Material de Grupo 4 para futura Discussion

`docs/analysis/group4/g4_literature_contrast_v0.1.md@main@38e22c19a0eb0d344e7675761a88d7968091eead` contiene 11 registros de contraste, 8 puntos autorizados y 14 prohibidos. No autoriza superioridad numérica cross-study no comparable, SOTA, novelty absoluta, causalidad no sustentada, generalización de EXP11B, uso de EXP12 como evidencia de HE5, ni equivalencia entre evidencia normativa/provenance/rationale y legal correctness.

### Material de Grupo 5 para futura Results

Grupo 5 cerró la organización de evidencia sin introducir nuevas métricas o inferencia. Mantiene nueve tablas canónicas: 2 principales inferenciales, 2 secundarias/descriptivas y 5 de apéndice/suplemento, además de destinos `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON`. Su existencia no abre el gate editorial de Results.

### Regla sobre nombres de adjuntos

Sufijos de plataforma como `(1)`, `(3)`, `(4)` o `(5)` no constituyen versiones científicas. La identidad se determina por contenido, versión interna aprobada, ruta gobernante y SHA cuando corresponda.

### Precedencia por dimensión

1. Estado experimental, resultados, artefactos y campañas: `SRC-03` + artefactos/commits congelados del repositorio de desarrollo.
2. Arquitectura y metodología operativa: `SRC-02`.
3. Problema, objetivos, hipótesis, justificación y alcance aprobados: `SRC-01`.
4. Formulaciones posteriores y tesis preliminar: `SRC-04`.
5. Literatura científica: `BIBLIOGRAPHIC_FRAMEWORK.md` y PDFs verificados.

Una discrepancia entre fuentes no debe resolverse silenciosamente. Debe identificarse, clasificarse y someterse al gate correspondiente.

---

## English

### Purpose

This registry identifies the primary and operational sources governing article drafting and prevents ambiguity among local copies, GitHub branches, and documentary versions.

### Current nuclear sources

| ID | Source | Current location | Function | Status |
|---|---|---|---|---|
| SRC-01 | Approved thesis project | author-provided attachment when required | approved problem, objectives, hypotheses, justification, and scope | REQUIRED |
| SRC-02 | Current methodological Annex | `Anexo_1_NANDINA_LLM_RAG_v13.docx` or later expressly approved version | current operational architecture and methodology | REQUIRED |
| SRC-03 | Experimental Master Plan | `elVladdi/gci-nandina-rag`, branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md` | current experimental state | LIVING_SOURCE_IN_GITHUB |
| SRC-04 | Current preliminary thesis | latest author-identified copy | later synthesis/discrepancy detection; does not replace approved formulations or experimental state | REQUIRED_FOR_COMPARISON |

Only the Experimental AI has write authority over `SRC-03`. The Managing and Drafting AIs read it only. Its current article-consumable snapshot, verified for Experimental Design B01 on 2026-09-22, is HEAD `b74b96d0163807007e4579d86450dd235125b30f`, plan blob `7b63fdb14b75eace173ac3c94775d39ed7ed7a57`, with development `main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`.

```text
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
GROUP5 = CLOSED / APPROVED
GROUP6 = IN_PROGRESS
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01_INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Under D-034, this state does not by itself block Architecture or Experimental-Design drafting and does not authorize Results or a final scientific freeze.

Technical primary sources for Experimental Design B01 at the current development checkpoint are the v0.2 split metadata (`bcb02c9...`), split configuration (`059eb816...`), EXP-04 historical-retrieval inventory (`64e7049a...`), series parser (`87dafb5f...`), and historical multisheet preparation script (`748c7b7e...`). They support concrete technical facts but do not replace `SRC-03` for experimental state.

The Group-4 contrast artifact remains binding for future Discussion; the Group-5 presentation system remains binding for future Results once those editorial gates open. Neither artifact currently opens those sections.

Platform filename suffixes are not scientific versions. Source precedence is: experimental state/results via `SRC-03` plus frozen development artifacts; operational architecture/methodology via `SRC-02`; approved problem/objectives/hypotheses/scope via `SRC-01`; later thesis formulations via `SRC-04`; scientific literature via the bibliographic framework and verified PDFs. Discrepancies must not be silently reconciled.
