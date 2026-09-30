# D-213 — FAST-F02 V02 Audit Failure / Narrow V03 Presentation-Consistency Correction Required

## Español

```text
DECISION = D-213
PHASE = FAST_FINALIZATION / FAST_F02_CORRECTIVE_PRESENTATION
PREVIOUS_DECISION = D-212

SOURCE_RESPONSE =
article/responses/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_RESPONSE_V01.md@f2adee6a77ec925f9d2fa413488654e9735ec421
SOURCE_RESPONSE_GIT_BLOB =
17797b884a945b99c9133999f4e631a28f743651

GESTORA_REVIEW =
article/reviews/19_FAST_F02_GLOBAL_TABLE_FIGURE_CORRECTION_INTERNAL_REVIEW_V01.md@d38ec83df8faa2d16a7e01dc1b4547a535b70458
GESTORA_REVIEW_GIT_BLOB =
a7d03575854aa5e528b7118233621e32ca07c40c
GESTORA_REVIEW_RESULT =
FAIL_CORRECTION_REQUIRED

FAST_F02_V02_STATUS = REJECTED_FOR_PRESENTATION_CONSISTENCY
SCIENTIFIC_CONTENT = PASS
NEW_SCIENCE_REQUIRED = NO
EXPERIMENTAL_REAUDIT_REQUIRED = NO

BLOCKING_FINDINGS =
R01_SPANISH_FIGURE2_FIGURE3_IMAGE_OBJECTS_MISSING /
R02_SUPPLEMENTARY_DOCX_READING_NOTE_STALE /
R03_FIGURE2_PNG_HANDOFF_HASH_MISMATCH /
R04_FIGURE2_SVG_PNG_PRESENTATION_VARIANT_MISMATCH

GESTORA_PROMPT_DEFECT =
PROMPT19_DRAWING_COUNT_CONTRACT_UNDERCOUNTED_FOR_BILINGUAL_MASTER

CORRECTION_SCOPE = NARROW_PRESENTATION_CONSISTENCY_ONLY

CANONICAL_MASTER = ARTICLE_MASTER_V038
CANONICAL_PROMOTION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = CLOSED
FAST_F03 = NOT_AUTHORIZED
```

## 1. Dictamen

FAST-F02 V02 no abre gate de aprobación autoral.

La auditoría Gestora confirma que la ciencia, las siete tablas, los valores congelados, las referencias y el alcance inferencial están correctos. La corrección requerida es exclusivamente de consistencia editorial, bilingüe y de trazabilidad de artefactos.

## 2. Defectos bloqueantes

1. La Parte II en español contiene captions para Figuras 2 y 3, pero no contiene sus imágenes en Markdown ni en DOCX.
2. El Supplementary DOCX V02 conserva en la nota inicial el texto obsoleto “Figures S1–S2”, aunque solo Figure S1 permanece.
3. El PNG Figure 2 entregado en el handoff no coincide en SHA con el PNG canónico embebido y declarado en la response.
4. El SVG versionado y el PNG embebido de Figure 2 son dos variantes visuales distintas del mismo conjunto de ocho valores.

## 3. Corrección de gobernanza del contrato anterior

Prompt 19 exigía las mismas cuatro figuras en el espejo español, pero también fijó incorrectamente un conteo esperado de seis drawings.

Para el master bilingüe correcto:

```text
SCIENTIFIC_FIGURE_IDENTITIES = 4
LANGUAGE_INSTANCES_PER_FIGURE = 2
EXPECTED_SCIENTIFIC_DRAWING_INSTANCES = 8
EXPECTED_UNIQUE_SCIENTIFIC_MEDIA = 4
```

La corrección V03 debe usar este contrato.

## 4. Límites

No se autoriza:

- nueva ciencia;
- nuevo análisis;
- nueva métrica;
- nuevos intervalos;
- nuevos p-values;
- nueva hipótesis;
- nueva literatura;
- cambio de referencias;
- cambio semántico en tablas o captions científicos ya auditados.

## 5. Gate

```text
CURRENT_GATE = FAST_F02_V03_PRESENTATION_CONSISTENCY_CORRECTION_PREPARATION
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
NEXT_ACTION = PREPARE_PROMPT_20_AND_EXECUTION_AUTHORIZATION
EXPECTED_EXIT = FAST_F02_V03_CORRECTIVE_EXECUTION_AUTHORIZED
```

---

## English

D-213 rejects FAST-F02 V02 for narrow presentation-consistency defects only. Scientific content passes. A V03 correction is required before any Author approval gate can reopen.
