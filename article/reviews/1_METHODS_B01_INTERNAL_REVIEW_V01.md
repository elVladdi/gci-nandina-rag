# Methods B01 — Revisión interna V01 / Internal Review V01

## Español

### 1. Objeto

Se revisó exclusivamente la entrega `Methods B01 — Design, scope, and units` del commit `2a0deee3c4b63ae028bbe909d5f44f90a4282086` contra el prompt autorizado, `MWDP_V1.0`, la matriz claim–evidence, la guía de estilo, el ground truth congelado y el `SRC-03` vivo.

Artefactos revisados:

- `article/responses/1_METHODS_B01_DESIGN_SCOPE_UNITS_RESPONSE_V01.md`;
- `article/sections/methods/Methods_B01_V01.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.md`;
- `article/manuscript/ARTICLE_MASTER_CANDIDATE_V01.docx` a nivel estructural y de consistencia con el contenido textual disponible.

El commit añadió únicamente los cuatro artefactos autorizados.

### 2. Dictamen científico/editorial

El núcleo científico del bloque es correcto y conserva las fronteras congeladas: piloto aplicado/offline, alcance restringido al Capítulo 87, apoyo no vinculante, separación funcional historical retrieval → normative evidence → local LLM, Top-3 fijo, SERIE como unidad de análisis y DAM como unidad de agrupamiento cuando la dependencia es relevante. No se introdujeron resultados, métricas, inferencias, novelty, gap final ni literatura externa.

No obstante, V01 requiere correcciones menores obligatorias antes de aprobación.

### 3. Observaciones obligatorias

#### B01-M01 — Lenguaje interno no publicable

La frase inglesa `defined by the governing study artifacts` y su espejo español `definidas por los artefactos gobernantes del estudio` exponen vocabulario de gobernanza interna al lector del artículo. Debe sustituirse por formulación científica autosuficiente orientada al lector, sin referirse a artefactos editoriales internos.

**Estado:** `REVISION_REQUIRED`.

#### B01-M02 — Definición de DAM en inglés

`customs declaration (DAM)` no explica el origen del acrónimo. En la primera aparición inglesa debe conservarse la denominación administrativa de origen y aclararse su significado, por ejemplo mediante una formulación equivalente a `Declaración Aduanera de Mercancías (DAM; customs declaration)`, sin convertir la sección en una explicación normativa extensa.

**Estado:** `REVISION_REQUIRED`.

#### B01-M03 — Uso implícito de C15 fuera del conjunto declarado

La oración `The architecture may be configurable beyond the evaluated setting...` introduce el claim positivo de configurabilidad correspondiente a `C15`. El prompt de B01 autorizó explícitamente `C01`, `C02`, `C03` y `C07`, y el checklist V01 declara únicamente esos cuatro claims. Por tanto, existe una inconsistencia de gobernanza aunque C15 sea un claim globalmente autorizado en la matriz.

Para V02, no ampliar el conjunto de claims del bloque. Eliminar la afirmación positiva de configurabilidad y conservar únicamente el límite de validez: no se evaluó generalización empírica fuera del alcance de Capítulo 87.

**Estado:** `REVISION_REQUIRED`.

#### B01-M04 — Discrepancia real detectada en archivos de control editorial

La IA de Redacción detectó correctamente que `ARTICLE_STATUS.md` y `PHASE_1_METHODS_ENTRY_GATE.md` afirmaban cierres de Grupo 3A/3B, mientras el `SRC-03` vivo en el snapshot `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6` establece `GROUP3=NOT_STARTED` y `Grupo 3 = NEXT / NOT_STARTED`.

La discrepancia es responsabilidad de la IA Gestora y no de la IA de Redacción. Debe corregirse en los archivos editoriales de control antes de aprobar B01. No afecta el contenido científico de V01 porque B01 no utiliza resultados de Grupo 3.

**Estado:** `EDITORIAL_CONTROL_CORRECTION_REQUIRED`.

### 4. Controles que pasan

```text
AUTHORIZED_SCOPE_ONLY = PASS
NO_RESULTS_OR_METRICS = PASS
NO_EXTERNAL_LITERATURE = PASS
CITATION_COMMENT_COVERAGE = 0/0 / PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS_WITH_MINOR_WORDING_CORRECTIONS
WORD_COUNT_264 = VERIFIED
ONLY_AUTHORIZED_ARTIFACTS_CREATED = PASS
B02_OR_LATER_CONTENT = NONE
EXPERIMENTAL_RESULT_INTERPRETATION = NONE
```

El `.docx` existe como paquete OOXML válido y no contiene infraestructura de comentarios, lo cual es consistente con `0/0` citas en este bloque. La aprobación final del Word candidato queda condicionada a que V02 replique exactamente las correcciones de contenido y preserve el layout neutral/editable.

### 5. Dictamen

```text
METHODS_B01_V01_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
MATERIAL_SCIENTIFIC_ERRORS = 0
MINOR_REQUIRED_CORRECTIONS = 3
EDITORIAL_CONTROL_CORRECTION = 1
METHODS_B01 = REVISION_REQUIRED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = NOT_REQUESTED_YET
MASTER_INTEGRATION = NOT_AUTHORIZED
```

---

## English

### 1. Scope

This review covers only the `Methods B01 — Design, scope, and units` delivery at commit `2a0deee3c4b63ae028bbe909d5f44f90a4282086`, checked against the authorized prompt, `MWDP_V1.0`, the claim–evidence matrix, style guide, frozen ground truth, and living `SRC-03`.

The commit added only the four authorized artifacts. The scientific core is sound and preserves the frozen boundaries: applied/offline pilot, Chapter-87 scope, non-binding decision support, functional separation of historical retrieval, normative evidence, and the local LLM, fixed Top-3, SERIES as analysis unit, and DAM as grouping unit when dependence is relevant. No results, metrics, inference, final novelty/gap, or external literature were introduced.

### 2. Required corrections

**B01-M01 — Internal governance wording.** `defined by the governing study artifacts` is internal process language and must be replaced by self-contained manuscript-facing scientific wording. `REVISION_REQUIRED`.

**B01-M02 — DAM definition in English.** `customs declaration (DAM)` does not explain the acronym. At first occurrence, retain the source administrative name and clarify its English meaning, e.g. an equivalent of `Declaración Aduanera de Mercancías (DAM; customs declaration)`. `REVISION_REQUIRED`.

**B01-M03 — Undeclared C15 use.** `The architecture may be configurable beyond the evaluated setting...` is a positive configurability claim corresponding to C15, while the B01 prompt and V01 checklist limit the block to C01/C02/C03/C07. V02 must not broaden the block: remove the positive configurability statement and retain only the validity boundary that empirical generalization beyond Chapter 87 was not evaluated. `REVISION_REQUIRED`.

**B01-M04 — Editorial-control discrepancy.** The Writing AI correctly detected that `ARTICLE_STATUS.md` and the Phase-1 entry gate claimed Group-3A/3B closures while living `SRC-03` at `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6` states `GROUP3=NOT_STARTED` / `NEXT / NOT_STARTED`. This is a Managing-AI control-file error, not a Writing-AI error. It is non-blocking for the scientific content of B01 but must be corrected before approval.

### 3. Passing controls and verdict

```text
AUTHORIZED_SCOPE_ONLY = PASS
NO_RESULTS_OR_METRICS = PASS
NO_EXTERNAL_LITERATURE = PASS
CITATION_COMMENT_COVERAGE = 0/0 / PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS_WITH_MINOR_WORDING_CORRECTIONS
WORD_COUNT_264 = VERIFIED
ONLY_AUTHORIZED_ARTIFACTS_CREATED = PASS
B02_OR_LATER_CONTENT = NONE
EXPERIMENTAL_RESULT_INTERPRETATION = NONE

METHODS_B01_V01_INTERNAL_REVIEW = PASS_WITH_CORRECTIONS
MATERIAL_SCIENTIFIC_ERRORS = 0
MINOR_REQUIRED_CORRECTIONS = 3
EDITORIAL_CONTROL_CORRECTION = 1
METHODS_B01 = REVISION_REQUIRED
B02 = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = NOT_REQUESTED_YET
MASTER_INTEGRATION = NOT_AUTHORIZED
```
