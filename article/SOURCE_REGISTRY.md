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
- apertura de Experimental Design B01, 2026-09-22: HEAD `b74b96d0163807007e4579d86450dd235125b30f`, blob `7b63fdb14b75eace173ac3c94775d39ed7ed7a57`, `main=b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`.
- **sincronización D-052, 2026-09-25**: HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8`, blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`, `main=db0d0ad0d8435921a7838db6720eaea86a263763`.

### Último snapshot consumible por el artículo

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
GROUP6 = CLOSED / APPROVED
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_CLOSURE_COMMIT = e93b44164a9619dad1f527a3b2d4479265858e39
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F01_CLOSURE_COMMIT = db0d0ad0d8435921a7838db6720eaea86a263763
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

Este estado no abre por sí mismo Results, Discussion ni el freeze científico final. Los grupos experimentales permanecen bajo autoridad de la IA Experimental.

### Fuentes técnicas congeladas usadas por Experimental Design B01

El B01 integrado se verificó contra el checkpoint histórico `main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`, incluyendo:

- `data/processed/data_aduanas_splits_clase87_v0.2_metadata.json`, blob `bcb02c9c3493235a6f80991158c5b24fa7c04510`;
- `src/configs/data_aduanas_split_clase87_v0.2.json`, blob `059eb81677dad92d6f9241f0b8cbbff9bba332cd`;
- `docs/exp04_bm25_historico_v02_inventory.md`, blob `64e7049ae8fb056a5fcc2173b39bdcb244567a89`;
- `src/ingestion/sunat_series_parser.py`, blob `87dafb5f2b5f1febfc588b7b763adc9ab5523339`;
- `src/ingestion/prepare_new_historical_multisheet_v0.1.py`, blob `748c7b7ed7d55a1c2f05a76e1b382ee0077f158f`.

Estas identidades documentan el corte técnico consumido por B01; no significan que el desarrollo actual permanezca en ese commit.

### Material de Grupo 4 para futura Discussion

`docs/analysis/group4/g4_literature_contrast_v0.1.md@main@38e22c19a0eb0d344e7675761a88d7968091eead` contiene 11 registros de contraste, 8 puntos autorizados y 14 prohibidos. No autoriza superioridad numérica cross-study no comparable, SOTA, novelty absoluta, causalidad no sustentada, generalización de EXP11B, uso de EXP12 como evidencia de HE5, ni equivalencia entre evidencia normativa/provenance/rationale y legal correctness.

### Material de Grupo 5 para futura Results

Grupo 5 cerró la organización de evidencia sin introducir nuevas métricas o inferencia. Mantiene nueve tablas canónicas: 2 principales inferenciales, 2 secundarias/descriptivas y 5 de apéndice/suplemento, además de destinos `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON`.

### Material de Grupo 6 para futura Results

Grupo 6 cerró y aprobó exactamente tres figuras experimentales y tres captions. Su cierre no introdujo nuevas métricas, inferencias, intervalos de confianza ni p-values y no modificó el artículo. Estas figuras se tratan editorialmente como **recursos visuales ya producidos**, pendientes de inserción cuando se abra el gate de Results o material secundario correspondiente. No sustituyen la futura `Figure 1` arquitectónica de Section 3.1.

Recursos de control relevantes:

- `outputs/figures/group6/g6_figure_spec_registry_v0.1.json`;
- `outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv`.

### Grupo 7 como dependencia externa

G7-F01 cerró el writing source freeze y quedó integrado en `main`. G7-F02 está activo/autorizado bajo el Plan Maestro experimental y G7-F03 permanece prospectivo. La IA Gestora del artículo consume este estado únicamente cuando afecte materialmente un claim o gate editorial; no administra ni ejecuta Grupo 7.

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

Only the Experimental AI has write authority over `SRC-03`. The Managing and Drafting AIs read it only. The latest synchronized snapshot is HEAD `87422102290a4f9a89c51e936cf7274d8e4687d8`, plan blob `cf587b61b7bfbc66dca310a7bb3b4d3f64671eea`, with development `main@db0d0ad0d8435921a7838db6720eaea86a263763`.

```text
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
GROUP5 = CLOSED / APPROVED
GROUP6 = CLOSED / APPROVED
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_CLOSURE_COMMIT = e93b44164a9619dad1f527a3b2d4479265858e39
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

This state does not by itself open Results, Discussion, or final scientific freeze.

The Group-4 contrast artifact remains binding for future Discussion. Group 5 supplies the approved result-presentation system. Group 6 supplies three already approved experimental figures/captions for future editorial insertion; they are not a replacement for the architecture figure planned in Section 3.1. Group 7 remains an external dependency administered by the Experimental AI.

Platform filename suffixes are not scientific versions. Source precedence remains: experimental state/results via `SRC-03` plus frozen development artifacts; operational architecture/methodology via `SRC-02`; approved problem/objectives/hypotheses/scope via `SRC-01`; later thesis formulations via `SRC-04`; scientific literature via the bibliographic framework and verified PDFs. Discrepancies must not be silently reconciled.
