# Plan maestro canónico — Tesis San Marcos

**Proyecto:** Framework RAG explicativo y auditable para recomendación de subpartidas NANDINA  
**Repositorio principal:** `elVladdi/gci-nandina-rag`  
**Repositorio público de reproducibilidad:** `elVladdi/gci-nandina-rag-reproducibility`  
**Fecha de actualización:** 2026-09-15

## 1. Principios congelados

1. **SERIE** es la unidad de análisis.
2. **DAM / DECLARACIÓN** es la unidad de agrupamiento cuando existe dependencia.
3. La recuperación histórica produce el ranking principal de candidatos.
4. La recuperación normativa aporta evidencia documental y no sustituye ni reordena el ranking histórico.
5. El **Top-3 es fijo** antes de la generación.
6. El **LLM local** explica el Top-3 recuperado; no clasifica desde cero.
7. El reranker LLM es únicamente diagnóstico.
8. El piloto permanece restringido experimentalmente a Clase 87.
9. El evalset v0.2 de **1,056 casos** permanece fijo.
10. No se cambian reglas experimentales después de observar resultados.
11. No se reabre Grupo 1 salvo evidencia objetiva nueva de severidad suficiente.
12. EXP-11A no permite inferir un efecto causal aislado del tamaño del banco.
13. Toda nueva data histórica debe seguir el flujo **Excel fuente → Python versionado → dataset derivado → auditoría → hashes → gate**. No se construyen CSV finales manualmente.

## 2. Estado del plan de auditoría

| Grupo | Estado |
|---|---|
| 1. Diseño y ejecución experimental | **CLOSED / APPROVED** |
| 2. Reproducibilidad y trazabilidad | **CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS — GROUP2B_READINESS_V02=AUDITED/APPROVED/INTEGRATED; GROUP2B_CLOSURE_RECORD=INTEGRATED; GROUP2B_CLOSURE_INTEGRATION_COMMIT=a33fc7e10b5bc25a053e982f0ff24ff60eda042f; BLOCKING_GAP_COUNT=0; NONBLOCKING_LIMITATION_COUNT=11; HISTORICAL_ONLY_COUNT=5; ENVIRONMENT_REPRODUCIBILITY=COMPLETE_WITH_DECLARED_LIMITATION; CLEAN_CHECKOUT_REPRODUCIBILITY=COMPLETE_WITH_DECLARED_LIMITATION; SCIENTIFIC_REEXECUTION_REQUIRED=false; RESULTS_RECOMPUTATION_REQUIRED=false. Las limitaciones `DECLARED_NOT_RECOVERABLE` y los assets `HASH_BOUND_LOCAL_ONLY` permanecen explícitos; este cierre no declara reproducibilidad perfecta. EXP12_ORIGINAL_FROZEN_DESIGN=CLOSED; EXP12_DISPOSITION=CLOSED_WITHOUT_RETRIEVAL/PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH; EXP12_DIVERSITY_EFFECT_ESTIMABLE=false; EXP12_RETRIEVAL=NOT_AUTHORIZED/NOT_EXECUTED; EXP12_REDESIGN_IN_CURRENT_EXPERIMENT=NOT_AUTHORIZED.** |
| 3. Métricas e inferencia | **IN_PROGRESS — G3-F01=CLOSED/APPROVED/INTEGRATED_TO_MAIN; NEXT_ELIGIBLE_FICHA=G3-F02; G3-F02=ELIGIBLE/NOT_AUTHORIZED/NOT_EXECUTED** |
| 4. Análisis e interpretación | Pendiente |
| 5. Presentación de resultados | Pendiente |
| 6. Figuras y visualizaciones | Pendiente |
| 7. Redacción científica | Pendiente |
| 8. Coherencia metodológica/documental | Pendiente |

## 3. Benchmark v0.2 congelado

- Histórico H100: **2,950 series / 28 DAM / 66 códigos**.
- Desarrollo: **100 series / 6 DAM**.
- Evaluación: **1,056 series / 67 DAM / 42 códigos**.
- H100 SHA-256: `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- DEV SHA-256: `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`.
- EVAL SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.

H100 histórico: Top-1 0.509470; Top-3 0.671402; Top-5 0.763258; Top-10 0.891098; Top-50 0.991477; MRR 0.629708.

## 4. Grupo 1

**CLOSED / APPROVED.**

## 5. Grupo 2A

**CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS.**

Commit final G2A: `a6140b66cf2975313be327d6d3d4e18e38f1fdf5`.

F001 `PARTIALLY_RESOLVED`; F002 `NOT_RECOVERABLE`; F003 `PARTIALLY_RESOLVED`; F004 `PARTIALLY_RESOLVED`; F005 `NOT_RECOVERABLE`; F006 `VERIFIED_IN_G2`; F007 `OPEN / FUTURE_DEPENDENCY`; F008 `VERIFIED_IN_G2`; F009 `VERIFIED_IN_G2 / DECLARED_LIMITATION`; F010 `VERIFIED_IN_G2`.

## 6. EXP-11A — cierre definitivo

**CLOSED / APPROVED / VERSIONED / INTEGRATED TO MAIN.**

`main = origin/main = 9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.

- H25=10, H50=10, H75=10, H100=1 referencia.
- H50=5 D1 / 5 D2.
- H100 Gate PASS.
- 32,736 filas case-level.
- Sin rerun/resume.
- Freeze de 47 artefactos; 0 hash mismatches.
- Tests finales 13/13 y 270/270.
- HE2/HE5 permanecen pendientes de Grupo 3.

Resultados descriptivos:

| Condición | Top-3 | MRR |
|---|---:|---:|
| H25 | 0.645170 ± 0.051964 | 0.603787 ± 0.047775 |
| H50 | 0.597917 ± 0.066393 | 0.542492 ± 0.060405 |
| H75 | 0.463352 ± 0.132774 | 0.414030 ± 0.126668 |
| H100 | 0.671402 | 0.629708 |

## 7. NEW_HISTORICAL_GATE — Forensic Audit 01

**EXTERNAL AUDIT: APPROVED_WITH_TERMINOLOGY_CORRECTIONS.**

Estado:

- `FORENSIC_EXCEL_PIPELINE_AUDIT_COMPLETED=true`.
- Excel actual: `data/Series - Descripciones.xlsx`.
- SHA actual antes/después: `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`.
- Tamaño: `7,895,186` bytes.
- Hojas: índice 0 `Hoja2` (126,524×9), índice 1 `Hoja1` (41,578×10).
- Hoja activa actual: `Hoja1`.
- Hoja procesada históricamente: `Hoja2`, índice 0, por **default first worksheet**, sin `--sheet`.
- El parser usa `openpyxl.load_workbook(..., read_only=True, data_only=True)`.
- `__sheet_name` del intermedio histórico: únicamente `Hoja2`.
- Intermedio reproducido: 107 DAM / 11,320 series.
- Clase 87: 4,232 filas; 4,106 curadas.
- v0.1: split por fila, estratificado por NANDINA, seed 2026, tamaños 3000/100/1006.
- v0.2: unión de v0.1 y **asignaciones explícitas de DAM** de la configuración T5-safe-159.
- H100/DEV/EVAL v0.2 se reprodujeron byte a byte.
- Clasificación conservadora: `PIPELINE_PARTIALLY_RECONSTRUCTED`.

### Correcciones terminológicas de auditoría externa

1. El workbook histórico completo **no es byte-identificable** con el workbook actual: la metadata histórica registra SHA `cfc85f3d…`, mientras el actual es `db01d1fc…`.
2. La reproducción byte-exacta demuestra **equivalencia funcional del contenido procesado para el parser**, no identidad binaria de la hoja ni del workbook histórico completo.
3. En v0.2, el `seed=2026` queda como atributo de configuración/procedencia; el script materializa el split desde **listas explícitas de DAM** y no usa aleatoriedad para decidir la asignación v0.2.
4. `build_evalset_from_sunat_excel.py` no se reutilizará para la expansión histórica: es un flujo distinto y produce otro esquema, aunque su modo `sunat-block` sea capaz de iterar varias hojas.

### Consecuencia para las nuevas pestañas

El parser histórico actual procesa **una sola hoja por invocación**. Si no se pasa `--sheet`, procesa `workbook.worksheets[0]`. Por tanto, nuevas pestañas no se incorporan automáticamente.

## 8. NEW_HISTORICAL_GATE — Gate 02: freeze fuente + contrato multi-hoja

**CLOSED / APPROVED / INTEGRATED TO MAIN.**

Rama:
`codex/new-historical-gate-source-contract-v01`

Cadena candidata sobre `main=9e8af129...`:

1. `7a7153e6e8bebbc00486bd33e32613209b5febda` — freeze inicial y contrato candidato.
2. `ad4c630a6a4d442776740b59b9552ba72141ea48` — microclose correctivo prospectivo.

El candidato final está exactamente **2 commits delante y 0 detrás** de main y añade cinco artefactos versionados:
- protocolo multi-hoja;
- contrato JSON;
- script prospectivo de ingesta;
- tests Gate 02;
- manifiesto versionado de freeze de fuente.

### Hallazgos Gate 02

- `NHG02-F001 = VERIFIED_RESOLVED`
- `NHG02-F002 = VERIFIED_RESOLVED`
- `NHG02-F003 = VERIFIED_RESOLVED`
- `NHG02-F004 = VERIFIED_RESOLVED`
- `NHG02-F005 = VERIFIED_RESOLVED`

### Contrato prospectivo aprobado

- Fuente clasificada `CURRENT_H100_REPRODUCING_SOURCE`.
- SHA fuente/copia archivada: `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`.
- `preexisting_source_sheets = ["Hoja2", "Hoja1"]`.
- `historically_processed_sheet = "Hoja2"`, índice 0.
- `Hoja1 = PREEXISTING_UNPROCESSED_SOURCE_SHEET`.
- Conjuntos nuevos válidos:
  - `["NUEVA_01"]`;
  - `["NUEVA_01", "NUEVA_02"]`.
- `NUEVA_02` sola falla.
- La selección futura es siempre explícita mediante `--sheet`.
- Pipeline congelado:
  `PARSE → COMBINE → CLASSIFY/CURATE → FROZEN DAM/ID AUDIT → ELIGIBLE → EXACT/NEAR → CAPACITY → OUTPUTS/MANIFEST`.
- `classify_rows(..., scope_class="87")` se reutiliza sobre el conjunto combinado.
- DAM DEV/EVAL e `id_unico` congelado se auditan de forma independiente.
- Near duplicate 0.90/0.95/0.98 = descriptores, no exclusión automática.
- Umbrales de capacidad:
  - H150: 1,475 nuevas filas elegibles netas;
  - H200: 2,950 nuevas filas elegibles netas.
- El modo `--ingest-new-data` no construye H150/H200 y no ejecuta retrieval/BM25.
- Tests Gate 02: 27/27.
- Suite total: 297/297.

### Limitaciones no bloqueantes a vigilar en la ejecución real

1. El path futuro verifica el **orden y nombres** de las hojas preexistentes, pero no calcula por sí mismo una huella semántica de su contenido. Esto no afecta H100 —que nunca se reconstruye desde el workbook ampliado y permanece congelado—, pero la ejecución real debe verificar procedimentalmente que `Hoja2` y `Hoja1` no fueron editadas al añadir nuevas hojas.
2. `execution_commit` se registra desde Git. En la ejecución real se exigirá además working tree limpio y commit conocido antes de observar/procesar la nueva data.

Estas dos limitaciones no cambian la semántica del pipeline prospectivo ni requieren otro cambio de código antes de integrar Gate 02.

### Estado

- `NEW_HISTORICAL_GATE_02_STATUS=CLOSED`.
- `main = origin/main = ad4c630a6a4d442776740b59b9552ba72141ea48`.
- `CURRENT_H100_REPRODUCING_SOURCE_FROZEN=true`.
- `MULTISHEET_CONTRACT_FROZEN=true`.
- `MULTISHEET_CONTRACT_IN_MAIN=true`.
- `NEW_HISTORICAL_DATA_PROCESSED=false`.
- `NEW_SHEETS_ADDED=false`.
- `EXP11B_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.

**Siguiente paso autorizado: el usuario puede agregar `NUEVA_01` al final del workbook actual, preservando sin cambios `Hoja2` y `Hoja1`. `NUEVA_02` solo se añadirá si la cantidad de nueva data requiere una segunda hoja.**

## 9. EXP-11B

Objetivos:

- H150 ≈ 4,425 series.
- H200 ≈ 5,900 series.

H100 debe permanecer exactamente preservado como núcleo del histórico ampliado.

Para capacidad H200 se necesitan al menos **2,950 series nuevas elegibles netas** sobre H100; esta es una condición post-procesamiento, no un número bruto de filas Excel.

## 10. EXP-12

Estado del diseño original congelado: `CLOSED_WITHOUT_RETRIEVAL /
PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH`.

El retrieval EXP12 permanece `NOT_AUTHORIZED / NOT_EXECUTED`; como las
condiciones oficiales D-HIGH/D-MID/D-LOW no fueron materializadas, el efecto
de diversidad histórica previsto por EXP12 no es estimable.

- `EXP12_NEW_HISTORICAL_GATE_EXTENSION_V02=INTEGRATED`.
- `EXP12_SAMPLING_UNIVERSE=SOURCE_BOUND / APPROVED`:
  `data/interim/new_historical_gate_v0.2/new_historical_eligible.csv`, SHA-256
  `f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457`,
  7,190 filas, 101 DAM y 84 códigos NANDINA; cobertura de referencia H100
  `66/66`.
- `EXP12_SOURCE_BINDING_V04=INTEGRATED`,
  `EXP12_PREPLANNING_COMPATIBILITY_AUDIT_V01=INTEGRATED` y
  `EXP12_PREPLANNING_CORRECTION_V01=INTEGRATED`.
- `EXP12_TVD_SUPPORT=FULL_REFERENCE_SUPPORT_PLUS_OTHER`. Se mantiene
  `maximum_tvd=0.05`, cobertura H100 requerida `1.0`, objetivo 2,950 filas,
  rango `[2802,3098]`, 10,000 candidatos por seed, mínimo 30 factibles,
  seeds `20262001..20262010` y cuantiles `0.1 / 0.5 / 0.9`.

```text
EXP12_SAMPLING_UNIVERSE_PATH = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
EXP12_SAMPLING_UNIVERSE_SHA256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
EXP12_SAMPLING_UNIVERSE_ROWS = 7190
EXP12_SAMPLING_UNIVERSE_DAM = 101
EXP12_SAMPLING_UNIVERSE_NANDINA = 84
EXP12_H100_REFERENCE_COVERAGE = 66/66
EXP12_TVD_MAXIMUM = 0.05
EXP12_LABEL_COVERAGE_REQUIRED = 1.0
EXP12_TARGET_ROWS = 2950
EXP12_VOLUME_RANGE = [2802,3098]
EXP12_CANDIDATE_COUNT = 10000
EXP12_MINIMUM_UNIQUE_FEASIBLE = 30
EXP12_SEEDS = 20262001..20262010
EXP12_QUANTILES = 0.1 / 0.5 / 0.9
```

- `EXP12_PLANNING_AUTHORIZATION_V01=INTEGRATED / CONSUMED`.
- `EXP12_PLANNING_ATTEMPT_001=FAILED_ONE_SHOT / AUDITED / INTEGRATED`.
- `EXP12_PLANNING_ATTEMPT_001_FAILURE=Seed 20262001 produced fewer than 30 unique feasible candidates`.
- `EXP12_PLANNING_SUMMARY=NOT_CREATED` y
  `EXP12_PLANNING_OFFICIAL_CONDITIONS=NOT_SELECTED`.
- `EXP12_PLANNING_RETRY=PROHIBITED_UNDER_AUTH_001` y
  `EXP12_PLANNING_GATE=FAILED_UNDER_FROZEN_PLANNING_SEARCH`.
- `EXP12-P61-F001=FAILURE_OBSERVABILITY_GAP / NON_INVALIDATING_FOR_ATTEMPT`:
  la evidencia permite afirmar solo `feasible_count(seed=20262001) < 30`;
  no persiste el conteo exacto ni un breakdown por filtro y no atribuye
  causalidad a TVD, cobertura, volumen o deduplicación.
- `EXP12_FORENSIC_AUTH_001=REJECTED_PREEXECUTION / NOT_INTEGRATED` por la
  colisión entre el padre del marcador y el directorio reservado de salida.
- `EXP12_FORENSIC_AUTH_002=INTEGRATED / CONSUMED` y
  `EXP12_FORENSIC_ATTEMPT_001=COMPLETED_ONE_SHOT / AUDITED / INTEGRATED`.
  El resultado es `NON_GOVERNING_FORENSIC_RESULT`; no reemplaza el Attempt001
  oficial ni autoriza un nuevo planning.
- La reconstrucción forense se limita al seed `20262001`, los 10,000 índices
  congelados y las reglas v0.5. Persistió 10,000 candidatos intentados, cero
  rechazos por duplicación, cero rechazos por overlap EVAL, 10,000 candidatos
  únicos no solapados, 1,617 bajo volumen, 6,821 dentro del rango y 1,562
  sobre el rango. Entre los 6,821 dentro del rango, uno pasó cobertura y
  ninguno pasó TVD; el conteo factible final fue cero frente al mínimo de 30.

```text
EXP12_FORENSIC_CANDIDATE_INDICES_ATTEMPTED = 10000
EXP12_FORENSIC_DUPLICATE_REJECTIONS = 0
EXP12_FORENSIC_EVAL_OVERLAP_REJECTIONS = 0
EXP12_FORENSIC_UNIQUE_NONOVERLAP = 10000
EXP12_FORENSIC_VOLUME_BELOW = 1617
EXP12_FORENSIC_VOLUME_WITHIN = 6821
EXP12_FORENSIC_VOLUME_ABOVE = 1562
EXP12_FORENSIC_COVERAGE_PASS = 1
EXP12_FORENSIC_COVERAGE_FAIL = 6820
EXP12_FORENSIC_TVD_PASS = 0
EXP12_FORENSIC_TVD_FAIL = 6821
EXP12_FORENSIC_FINAL_UNIQUE_FEASIBLE = 0
EXP12_FORENSIC_MINIMUM_REQUIRED = 30
EXP12_FORENSIC_HISTORICAL_FAILURE_REPRODUCED = true
EXP12_FORENSIC_TVD_CHARACTERIZATION = UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
EXP12_FORENSIC_COVERAGE_CHARACTERIZATION = NEAR_UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
EXP12_FORENSIC_GLOBAL_INFEASIBILITY_PROVEN = false
EXP12_FORENSIC_OTHER_SEEDS_CHARACTERIZED = false
```

- `OFFICIAL_FORENSIC_INVOCATION_COUNT=1`. No hubo retry, resume, selección de
  condiciones, otros seeds ni thresholds alternativos. Volumen por sí solo
  no explica el fallo; deduplicación y overlap EVAL no fueron observados como
  cuellos de botella. Esta evidencia no prueba inviabilidad matemática global
  ni prescribe relajar TVD o cobertura.

```text
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_PLANNING_RETRY = PROHIBITED_UNDER_AUTH_001
EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_FORENSIC_FINAL_UNIQUE_FEASIBLE = 0
EXP12_FORENSIC_MINIMUM_REQUIRED = 30
EXP12_PLANNING_OFFICIAL_CONDITIONS = NOT_SELECTED
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_REDESIGN_IN_CURRENT_EXPERIMENT = NOT_AUTHORIZED
EXP12_POST_HOC_PARAMETER_RELAXATION = PROHIBITED
EXP12_SEED_REPLACEMENT_OR_DROPPING = PROHIBITED
EXP12_GLOBAL_MATHEMATICAL_INFEASIBILITY_PROVEN = false
EXP12_OTHER_SEEDS_CHARACTERIZED = false
EXP12_ANALYTICAL_LIMITATION = HISTORICAL_BANK_DIVERSITY_EFFECT_NOT_ESTIMABLE_FROM_EXP12_BECAUSE_OFFICIAL_CONDITIONS_WERE_NOT_MATERIALIZED
```

- El cierre demuestra que una precondición obligatoria del planning falló
  bajo la búsqueda congelada para el seed predeclarado `20262001`. No prueba
  inviabilidad matemática global, no caracteriza otros seeds y no autoriza
  relajar parámetros, sustituir o eliminar el seed, reintentar ni abrir un
  rediseño dentro del experimento original.
- Grupo 3 y la redacción futura no presentarán un efecto EXP12 ni inferirán
  D-HIGH/D-MID/D-LOW como si hubieran sido ejecutados.
- `NEXT_ELIGIBLE_BLOCK=GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE`.

## 11. Grupo 2B

**CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS.**

Readiness v0.2 `fbd321d817d22fef78417064e0d5bc8df37165ca` quedó
`AUDITED / APPROVED / INTEGRATED`. Inventarió 47 artefactos, ejecutó 35
identity checks documentales —31 pass-equivalent y 4
`HASH_BOUND_LOCAL_ONLY`, sin mismatch de contenido— y enlazó 11 cadenas
end-to-end: 1 `COMPLETE` y 10 `COMPLETE_WITH_DECLARED_LIMITATION`.

```text
GROUP2B_READINESS_V02_COMMIT = fbd321d817d22fef78417064e0d5bc8df37165ca
GROUP2B_CLOSURE_RECORD = INTEGRATED
GROUP2B_CLOSURE_INTEGRATION_COMMIT = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
GROUP2B_BLOCKING_GAP_COUNT = 0
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_HISTORICAL_ONLY_COUNT = 5
ENVIRONMENT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
CLEAN_CHECKOUT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
GROUP2B_SCIENTIFIC_REEXECUTION_REQUIRED = false
GROUP2B_RESULTS_RECOMPUTATION_REQUIRED = false
GROUP3 = IN_PROGRESS
NEXT_ELIGIBLE_FICHA = G3-F02
```

Las 11 limitaciones no bloqueantes y los 5 elementos historical-only del
readiness permanecen vigentes. Los activos local-only no fueron versionados y
los elementos `DECLARED_NOT_RECOVERABLE` no fueron recuperados. Este cierre no
equivale a reproducibilidad perfecta ni modifica la disposición final de
EXP12.

## 12. Grupos 3–8

Grupo 3 realizará análisis cuantitativo/inferencia y decisión HE2/HE5. Grupos 4–8: interpretación, presentación, figuras, redacción y coherencia documental.

### Gobernanza prospectiva de Grupos 3–8

El sistema documental de fichas define prospectivamente la secuencia y los
contratos de los Grupos 3–8. Su existencia no activa, autoriza ni ejecuta
ninguna ficha.

```text
FICHAS_G3_G8_BRANCH = docs/fichas-grupos-3-8
FICHAS_G3_G8_SNAPSHOT_COMMIT = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
FICHAS_G3_G8_ROOT = docs/fichas/grupos_3_8/
FICHAS_G3_G8_COUNT = 19
FICHAS_G3_G8_STATUS = G3-F01_CLOSED / REMAINING_FICHAS_NOT_AUTHORIZED
FICHAS_G3_F01_RECONCILIATION_COMMIT = ba9cc595778c4073b3bc20c60ad6a567bf514e9d
GROUP3 = IN_PROGRESS
NEXT_ELIGIBLE_FICHA = G3-F02
G3_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

El cierre aprobado de G3-F01 queda gobernado por:

```text
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F01_MAIN_INTEGRATION_COMMIT = 366bf529c29cb999bfd043db33674a510ba184c7
G3_F01_CORRECTED_EXTERNAL_REAUDIT = PASS
G3_F01_SCIENTIFIC_RERUN_REQUIRED = false
G3_F01_INFERENTIAL_CALCULATION_PERFORMED = false
G3_F01_HE2_DECIDED = false
G3_F01_HE5_DECIDED = false

NEXT_ELIGIBLE_FICHA = G3-F02
G3_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
STATISTICAL_INFERENCE = NOT_YET_AUTHORIZED
HE2_FINAL_DECISION = NOT_AUTHORIZED
HE5_FINAL_DECISION = NOT_AUTHORIZED
```

El snapshot `a42531ad96fc12bea2f2394b0ff8eb49b66a4238` es únicamente
el snapshot documental del sistema de fichas; no es un SHA científico de
ejecución. El mapa y la gobernanza se consultan en la rama, raíz y snapshot
anteriores, sin reproducir el contenido completo de las fichas en este Plan.

La jerarquía de gobierno es:

```text
PLAN MAESTRO
  gobierna estado, orden y autorización
    ↓
MAPA MAESTRO DE FICHAS
  gobierna secuencia y dependencias
    ↓
FICHA ACTIVA
  gobierna el contrato detallado del bloque
    ↓
PROMPT CODEX
  ejecuta solamente el bloque autorizado
    ↓
EVIDENCIA VERSIONADA
    ↓
AUDITORÍA EXTERNA IA EXPERIMENTAL
```

Los estados no son intercambiables ni implican automáticamente el siguiente:

```text
FICHA_CREATED_OR_DEFINED
≠ FICHA_AUTHORIZED
≠ FICHA_EXECUTED
≠ FICHA_VERIFIED
≠ FICHA_APPROVED
≠ FICHA_INTEGRATED
≠ FICHA_CLOSED
```

La ficha siguiente solo puede activarse después del cierre auditado de su
predecesora. Cada activación debe congelar en ese momento, sin reutilizar
automáticamente el snapshot de diseño:

- SHA vigente de `main`;
- SHA vigente del Plan Maestro;
- SHA de `article/main-manuscript` cuando aplique;
- fuentes primarias y artefactos de entrada;
- outputs esperados;
- prohibiciones;
- criterios PASS/FAIL;
- cualquier autorización one-shot o gate requerido.

La secuencia prospectiva oficial es:

```text
G3-F01 → G3-F02 → G3-F03 → G3-F04
→ G4-F01 → G4-F02 → G4-F03
→ G5-F01 → G5-F02 → G5-F03
→ G6-F01 → G6-F02 → G6-F03
→ G7-F01 → G7-F02 → G7-F03
→ G8-F01 → G8-F02 → G8-F03
→ POST-G8 FREEZE HANDOFF
```

Permanecen congeladas las restricciones científicas: EVAL v0.2 contiene
1,056 casos; SERIE es la unidad de análisis; DAM/DECLARACIÓN es la agrupación
cuando existe dependencia; EXP11A es sensibilidad y no un efecto causal
aislado del tamaño; todo análisis futuro de 0B-05C usa los resultados
corregidos de Attempt06; EXP12 está cerrado sin retrieval y su efecto de
diversidad no es estimable. También permanecen las 11 limitaciones no
bloqueantes y los 5 elementos historical-only de Grupo 2B, incluidos
`DECLARED_NOT_RECOVERABLE` y `HASH_BOUND_LOCAL_ONLY`. No se cambian reglas
analíticas después de observar resultados.

`G3-F01` queda únicamente como siguiente ficha elegible para una activación
futura, posterior a la auditoría e integración de este registro. Permanece
`NOT_ACTIVE / NOT_AUTHORIZED / NOT_EXECUTED`; Grupo 3 sigue `NOT_STARTED` y
`NEXT_ELIGIBLE_BLOCK=GROUP3_METRICS_AND_INFERENCE`.

## 13. Orden maestro actual

```text
Grupo 1 ✅
  ↓
Grupo 2A ✅
  ↓
EXP-11A ✅
  ↓
NEW_HISTORICAL_GATE — Forensic Audit 01 ✅
  ↓
Gate 02 ad4c630... ✅ CLOSED / APPROVED / INTEGRATED
  ↓
Real Ingest 01 — NUEVA_01 ✅ COMPLETED / APPROVED
  - eligible pool: 6,029 rows / 43 DAM / 56 NANDINA
  - H150/H200 feasible
  ↓
NEW_HISTORICAL_GATE 03 ✅ CLOSED / APPROVED / INTEGRATED
  ↓
EXP11B Bank Materialization ✅ CLOSED / APPROVED / INTEGRATED
  ↓
EXP11B Retrieval Execution Gate ✅ APPROVED / INTEGRATED
  ↓
0B-05C v0.1 Corrective Numerical Gate and Authorization ✅ HISTORICAL / INTEGRATED / SUPERSEDED FOR NEW EXECUTION
  - D1a training exposure: NO_EFFECTIVE_EXPOSURE_IDENTIFIED
  - D1a Top-200 overlap: NONE_IDENTIFIED
  - frozen original D1a weights
  - D1A_PREEXECUTION=APPROVED / INTEGRATED
  - 0B05C-GATE-F001/F002/F003/F004=CLOSED/PASS
  - D1a execution specification CLOSED_PROSPECTIVELY; D1A_METRIC_IMPACT=NOT_DETERMINED
  - authorization baseline=0e074db638f6b7163d98d34f08f76e1efde07b7f
  - authorization integration=06cc75ec173eb6c4b134a45eeb88fe25999f396e
  - Attempt01 and Attempt02=FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED
  - the historical v0.1 authorization is not operationally valid for a new attempt
  ↓
EV03 Historical Recovery v0.2 ✅ APPROVED / VERSIONED / INTEGRATED
  - candidate=cef8d7ad58d877e933f8c86b9f721cb214d9058d
  - microclose and current main=43291c312c2934aae03f3c087dd0a1ae594341b7
  - LOGICAL_INDEX_IDENTITY=EXACT
  - EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT
  - gate_scope=EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY
  - authorization_readiness=NOT_AUTHORIZATION_READY
  - EV03/EV04/D1a/unified v0.2=NOT_AUTHORIZED / NOT_EXECUTED
  - corrective retrieval and metrics not executed; runtime authorization record v0.2 absent
  ↓
0B-05C v0.2-v0.5 and Attempt06 ✅ CLOSED / APPROVED
  - v0.5=APPROVED / INTEGRATED
  - Attempt06 authorization=AUDITED / INTEGRATED
  - ATTEMPT06=COMPLETED / AUDITED_EXECUTION / INTEGRATED; 19/19 steps PASS
  - PROMPT38_RESULT_INTERPRETATION=REJECTED / SUPERSEDED_BY_PROMPT39
  - EV03_METRIC_IMPACT=ZERO_AGGREGATE_CHANGE
  - EV04_METRIC_IMPACT=TINY_NONZERO_MRR_DECREASE_ONLY
  - D1A_METRIC_IMPACT=POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
  - 0B05C_METRIC_IMPACT=METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
  - DOWNSTREAM_REEXECUTION=NOT_REQUIRED
  - FUTURE_ANALYSES_MUST_USE=ATTEMPT06_CORRECTED_RESULTS
  - 0B05C_CLOSURE=CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
  - prior fail-closed attempts remain preserved as historical evidence
  ↓
EXP11B Portability Replay / Debt Closure ✅ CLOSED / APPROVED / INTEGRATED
  - Prompt41 proof integrated in main=7d7267f8224e56ea5e945625a7e3955ddc15eadb
  - closure record integrated in main=09ff184854659110f7711b3eee65fc18927649da
  - closure of portability debt does not authorize retrieval
  ↓
EXP11B Retrieval H150/H200 ✅ CLOSED / APPROVED / INTEGRATED
  - authorization consumed by the single official execution
  - versionable results and closure integrated; local-only candidates bound by hash and size
  ↓
EXP12 New Historical Gate Extension v0.2 ✅ INTEGRATED
  - source-bound pool: 7,190 rows / 101 DAM / 84 NANDINA
  - H100 reference coverage: 66/66
  ↓
EXP12 Source Binding v0.4 ✅ INTEGRATED
  ↓
EXP12 Pre-planning Compatibility Audit v0.1 ✅ INTEGRATED
  ↓
EXP12 Pre-planning Correction v0.1 ✅ INTEGRATED
  - TVD support: FULL_REFERENCE_SUPPORT_PLUS_OTHER
  - thresholds, seeds, quantiles, volume and candidate_count unchanged
  ↓
EXP12 Planning Attempt 001 ⚠ FAILED_ONE_SHOT / AUDITED / INTEGRATED
  - authorization EXP12_PLANNING_AUTH_001 consumed; retry prohibited
  - seed 20262001 produced fewer than 30 unique feasible candidates
  - summary not created; D-HIGH/D-MID/D-LOW not selected
  - observability gap: exact feasible count and filter breakdown not persisted
  ↓
EXP12 Feasibility Failure Forensic Design ✅ INTEGRATED
  - authorization v0.1 rejected pre-execution and never integrated
  - corrected authorization v0.2 integrated and consumed
  ↓
EXP12 Forensic Attempt 001 ✅ COMPLETED_ONE_SHOT / AUDITED / INTEGRATED
  - 10,000 observed candidates; 6,821 within volume range
  - coverage pass: 1/6,821; TVD pass: 0/6,821
  - final unique feasible: 0; historical failure 0<30 reproduced
  - non-governing result; no global infeasibility claim
  ↓
EXP12 Original Frozen Design ✅ CLOSED_WITHOUT_RETRIEVAL
  - planning precondition failed under frozen search
  - seed 20262001: 0 feasible / minimum 30
  - official D-HIGH/D-MID/D-LOW not selected
  - diversity effect not estimable from EXP12
  - no post-hoc relaxation, seed replacement or retry
  ↓
Grupo 2B — Reproducibilidad y trazabilidad ✅ CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
  ↓
Grupo 3 — Métricas e inferencia ⏳ NEXT / NOT_STARTED
  ↓
Grupos 4–8
  ↓
Freeze científico
  ↓
Repositorio público / artículos / tesis final
```

## 14. Historial reciente

### 2026-09-01 — Forensic Audit 01 aprobado

- Pipeline Excel→Python→v0.1→v0.2 reconstruido parcialmente con reproducción byte-exacta de outputs.
- Workbook histórico completo no recuperado byte a byte.
- `Hoja2` fue la fuente funcional procesada mediante selección predeterminada de primera hoja.
- El workbook actual permanece intacto con SHA `db01d1fc...`.
- Próximo hito: congelar esa fuente actual reproducente y versionar el contrato de expansión multi-hoja antes de editar el Excel.

### 2026-09-01 — Gate 02 candidato auditado externamente

- Rama candidata `codex/new-historical-gate-source-contract-v01` = `7a7153e6e8bebbc00486bd33e32613209b5febda`.
- `main` permanece `9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.
- Commit candidato: 1 commit / 4 archivos añadidos.
- Freeze externo de fuente actual: SHA origen=copia `db01d1fc...`; 7,895,186 bytes; Python `shutil.copy2`.
- 17/17 tests nuevos y 287/287 suite reportados.
- Gate 02 **NO cerrado externamente** por cinco hallazgos prospectivos: manifiesto de freeze no versionado, path de ingesta futura no congelado, `NUEVA_02` aceptada sin `NUEVA_01`, masking de razones de overlap y terminología demasiado amplia sobre “historical_sheets”.
- No se autoriza modificar el Excel ni incorporar nueva data hasta resolver y auditar esos hallazgos.

### 2026-09-01 — Gate 02 microclose aprobado externamente

- Candidato final: `ad4c630a6a4d442776740b59b9552ba72141ea48`.
- Relación con main: 2 commits delante, 0 detrás.
- Cinco archivos versionados en el scope Gate 02.
- F001–F005: `VERIFIED_RESOLVED`.
- Manifiesto de freeze versionado y consistente con SHA `db01d1fc...`.
- Path `--ingest-new-data` congelado y probado sintéticamente.
- 27/27 tests Gate 02; 297/297 suite completa.
- Gate 02: **EXTERNAL APPROVAL = true; INTEGRATION TO MAIN = pending**.
- El Excel sigue intacto; nueva data aún no procesada.

### 2026-09-01 — Gate 02 cerrado e integrado

- `main = origin/main = ad4c630a6a4d442776740b59b9552ba72141ea48`.
- Integración fast-forward desde `9e8af129...`, sin merge commit.
- 27/27 tests Gate 02 y 297/297 suite completa en candidata, main y clean checkout.
- H100/DEV/EVAL hashes preservados.
- Fuente congelada `db01d1fc...` preservada.
- `NEW_HISTORICAL_GATE_02_STATUS=CLOSED`.
- `MULTISHEET_CONTRACT_IN_MAIN=true`.
- Se autoriza al usuario a agregar `NUEVA_01` al workbook actual bajo el contrato congelado.
- `NUEVA_02` es opcional y solo debe agregarse si es necesaria por capacidad física/operativa.
- Antes de la ingesta real se verificará que `Hoja2` y `Hoja1` no hayan cambiado respecto de la copia congelada.
- La nueva data se procesará exclusivamente con Python; no se construyen manualmente H150/H200.

### 2026-09-01 — Real Ingest 01 detenido antes de procesar NUEVA_01

- Workbook ampliado: orden corregido `["Hoja2", "Hoja1", "NUEVA_01"]`.
- `HOJA2_CANONICAL_CONTENT_MATCH=true`.
- `HOJA1_CANONICAL_CONTENT_MATCH=true`.
- Coincidencia en `data_only=True` y `data_only=False`; no existen fórmulas.
- Parser Hoja2: mismas columnas y 11,320 filas, pero la igualdad literal de todos los diccionarios devolvió `false`.
- No se congeló el workbook ampliado.
- No se ejecutó `--validate-new-sheets`.
- No se ejecutaron tests de la pasada.
- No se ejecutó `--ingest-new-data`.
- No se generaron outputs de nueva data.
- Código/config/datasets congelados sin cambios.

#### Diagnóstico externo preliminar

El parser incorpora `__source_file = str(source_file)` en cada fila y `parse_workbook()` pasa el `path` del workbook directamente a `parse_series_block`. Por tanto, comparar literalmente filas obtenidas desde el archivo congelado y desde el workbook ampliado **debe producir una diferencia de procedencia en `__source_file` aunque todo el contenido científico sea idéntico**.

Estado provisional:

`NHG_REAL01-F001 = PARSER_PROVENANCE_PATH_FALSE_MISMATCH / OPEN_FORENSIC_CHECK`.

No se autoriza todavía la ingesta. El siguiente paso es una comparación campo-a-campo READ-ONLY. Solo `__source_file` puede diferir. Si cualquier otro campo, fila, orden, warning o metadato funcional difiere, la ingesta seguirá bloqueada. Si la única diferencia es `__source_file`, el control histórico se considerará PASS y podrá continuar la ejecución real sin modificar código.

### 2026-09-01 — Real Ingest 01: F001 resuelto y F002 de invocación CLI

- `NHG_REAL01-F001=VERIFIED_RESOLVED`.
- Única diferencia parser Hoja2: `__source_file` en 11,320 filas.
- Comparación funcional excluyendo exclusivamente `__source_file`: `true`.
- `SOURCE_PREEXISTING_SHEETS_UNCHANGED=true`.
- Workbook ampliado congelado externamente:
  - `Series - Descripciones_EXPANDED_NUEVA_01_SOURCE_087efd97.xlsx`
  - SHA `087efd97...ee4ba3`
  - 16,060,154 bytes.
- La ejecución se detuvo antes de validar/ingerir NUEVA_01 porque el comando `python -m src.ingestion.prepare_new_historical_multisheet_v0.1` es inválido: el punto en el nombre del archivo hace que Python interprete `v0.1` como segmentos de módulo.
- Nuevo hallazgo:
  `NHG_REAL01-F002 = INVALID_PYTHON_MODULE_INVOCATION_FOR_DOTTED_FILENAME`.
- F002 es procedimental y no científico; no requiere cambio de código.
- Resolución autorizada: ejecutar el mismo archivo congelado mediante ruta directa:
  `python src/ingestion/prepare_new_historical_multisheet_v0.1.py ...`
- No se modifica código/configuración ni se renombra el archivo después de observar nueva data.
- Nueva ingesta real sigue pendiente; no existen outputs científicos nuevos.

### 2026-09-01 — Real Ingest 01 completado con NUEVA_01

**Estado externo:** `APPROVED_FOR_FREEZE_AND_GATE03_DESIGN`.

- `NHG_REAL01-F001=VERIFIED_RESOLVED`.
- `NHG_REAL01-F002=VERIFIED_RESOLVED`.
- Fuente ampliada congelada:
  - `Series - Descripciones_EXPANDED_NUEVA_01_SOURCE_087efd97.xlsx`
  - SHA `087efd97cb17fd166c2e7eb5089690577491e99ab5d415f9e3a8614923ee4ba3`
  - 16,060,154 bytes.
- `SOURCE_PREEXISTING_SHEETS_UNCHANGED=true`.
- `validate-new-sheets=PASS`.
- Tests pre/post: 27/27 Gate 02; 297/297 suite.
- NUEVA_01 parseada: 15,596 series.
- Clase 87: 6,029.
- Quality/duplicate policy: 6,029.
- DEV/EVAL DAM exclusions: 0.
- Frozen `id_unico` overlaps: 0.
- Pool final elegible: **6,029 filas / 43 DAM / 56 NANDINA**.
- Composición nueva:
  - largest DAM = 990 (16.42%);
  - HHI = 0.08755655;
  - effective DAM = 11.4212;
  - 45/66 códigos H100 presentes (68.18%);
  - 11 códigos nuevos respecto de H100.
- Pool potencial `H100 + NEW_ELIGIBLE`:
  - 8,979 filas;
  - 71 DAM;
  - 77 NANDINA;
  - HHI = 0.06496386;
  - effective DAM = 15.3932;
  - largest DAM share = 11.64%.
- Capacidad: `H150_AND_H200_FEASIBLE`.
- Exact/near descriptions permanecen descriptores, no exclusiones:
  - vs H100: exact 1,364; near 0.90/0.95/0.98 = 1,394/1,379/1,367;
  - vs DEV: 0;
  - vs EVAL: exact 23; near = 70/45/32.
- 7/7 artefactos listados por el inventario verificados; 0 mismatches.
- H100/DEV/EVAL hashes preservados.
- Sin retrieval, sin H150/H200 materializados, sin cambios científicos.

### Próximo hito: NEW HISTORICAL GATE 03

Gate 03 debe:

1. congelar/versionar los outputs de Real Ingest 01 y un manifest durable de la fuente ampliada;
2. congelar SHA del `new_historical_eligible.csv`;
3. diseñar H150/H200 **antes de retrieval**, usando únicamente composición del banco;
4. preservar DAM completas;
5. prohibir uso de labels/performance del eval para selección;
6. materializar H150/H200 solo después de aprobar externamente el diseño;
7. definir prospectivamente el análisis complementario de exact/near duplicates contra el máximo banco evaluado, manteniendo 1,056 casos como denominador primario.

`EXP11B_AUTHORIZED=false` hasta cerrar Gate 03.

### 2026-09-01 — Gate 03 candidato `b380619` auditado externamente

**Estado:** `APPROVED_WITH_BLOCKING_MICROCLOSE_BEFORE_MAIN`.

- Rama candidata: `codex/new-historical-gate-expanded-pool-v01`.
- Candidato: `b3806190cb645d35c2a121c0f1d0c07fbfe21605`.
- Relación contra `main=ad4c630...`: 1 commit delante, 0 detrás.
- Real Ingest 01 queda congelado en Git:
  - `new_historical_eligible.csv` SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`;
  - 6,029 filas / 43 DAM / 56 NANDINA;
  - H100/new DAM overlap = 0.
- Diseño de selección EXP-11B:
  - selección únicamente por DAM id + row count + seed + namespace;
  - H100 fijo;
  - DAM completas;
  - H150 estrictamente anidado en H200;
  - tolerancia ±148;
  - 10 pares válidos tras evaluar 24 seeds;
  - accepted seeds exactos:
    `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- No se ejecutó retrieval y H150/H200 no fueron materializados.
- Common-clean:
  - primary N=1056;
  - casos afectados: exact=36, near90=75, near95=54, near98=46;
  - denominadores clean derivados: exact=1020, near90=981, near95=1002, near98=1010.

#### NHG03-F001 — TOTAL_BANK_DESCRIPTORS_MISSING / S2

El planner calcula `descriptor` usando únicamente las DAM incrementales seleccionadas de `NEW_ELIGIBLE`. Esto no representa la composición real de los bancos experimentales futuros, que serán `H100_FROZEN + selected_new_DAMs`.

Antes de integrar Gate 03 se debe agregar, sin cambiar selección/seeds:
- `increment_descriptor` para el subconjunto nuevo;
- `total_bank_descriptor` para H100 + incremento;
- total DAM count;
- HHI/effective DAM del banco total;
- largest DAM share total;
- NANDINA total;
- H100 NANDINA coverage;
- new NANDINA count.

La corrección es descriptiva y no puede alterar ninguna composición aceptada.

#### NHG03-F002 — COMMON_CLEAN_DENOMINATORS_NOT_EXPLICIT / S2

La evidencia conserva los casos afectados pero no congela explícitamente los denominadores clean requeridos. Deben registrarse:
- N_PRIMARY=1056
- N_EXACT_CLEAN=1020
- N_NEAR090_CLEAN=981
- N_NEAR095_CLEAN=1002
- N_NEAR098_CLEAN=1010.

No modifica máscaras ni selección.

**Gate 03 todavía no se integra a main.**

### 2026-09-01 — Gate 03 microclose `ed470d6` aprobado externamente

**Estado:** `APPROVED_FOR_MAIN_INTEGRATION`.

- Candidato corregido: `ed470d67315f505cb3bde471177268db6d16a676`.
- Rama remota `codex/new-historical-gate-expanded-pool-v01` apunta al mismo SHA.
- `main` permanece en `ad4c630a6a4d442776740b59b9552ba72141ea48`.
- El microclose añade únicamente tres cambios: planner, tests y evidencia de factibilidad.
- `NHG03-F001=VERIFIED_RESOLVED`.
- `NHG03-F002=VERIFIED_RESOLVED`.
- Las 10 semillas y las 20 composiciones H150/H200 permanecen idénticas a `b380619`.
- Descriptores separados:
  - `increment_descriptor`;
  - `total_bank_descriptor = H100_FROZEN + incremento seleccionado`.
- Todos los bancos totales preservan cobertura H100 `66/66`.
- Common-clean:
  - primary = 1056;
  - exact clean = 1020;
  - near090 clean = 981;
  - near095 clean = 1002;
  - near098 clean = 1010.
- `eval_common_clean_masks_v0.1.csv` permanece sin cambios.
- `new_historical_eligible.csv` permanece SHA `a78e8c...c083a4`, 6,029 filas y 43 DAM.
- Tests: Gate 02 27/27; Gate 03 29/29; suite completa 326/326.
- No retrieval, no BM25, no materialización H150/H200.

### Próximo paso

Integrar Gate 03 por fast-forward a `main` y validar en clean checkout.

Solo después del cierre post-integración podrá iniciarse el siguiente subgate:

`EXP11B_BANK_MATERIALIZATION_GATE`

para materializar, hash-ear y auditar los 10 H150 + 10 H200 **sin retrieval**. `EXP11B_AUTHORIZED=false` hasta cerrar ese subgate.

### 2026-09-01 — Gate 03 cerrado e integrado a main

**Estado:** `CLOSED / APPROVED / INTEGRATED TO MAIN`.

- `main = origin/main = ed470d67315f505cb3bde471177268db6d16a676`.
- Integración por `git merge --ff-only`, sin merge commit.
- Relación contra base `ad4c630...`: `0 behind / 2 ahead`.
- Real Ingest freeze: 9 artefactos, 0 mismatches.
- Pool elegible congelado:
  - SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`;
  - 6,029 filas;
  - 43 DAM.
- H100/DEV/EVAL permanecen sin cambios.
- EXP-11B:
  - 10 seeds exactas congeladas;
  - 20 composiciones H150/H200 idénticas a baseline;
  - nesting estricto;
  - tolerancia <=148;
  - descriptores incrementales y del banco total congelados.
- Common-clean:
  - primary 1056;
  - exact clean 1020;
  - near090 clean 981;
  - near095 clean 1002;
  - near098 clean 1010.
- Tests en candidata/main/clean checkout:
  - Gate 02 27/27;
  - Gate 03 29/29;
  - suite completa 326/326.
- No retrieval, no BM25, no H150/H200 materializados.
- `EXP11B_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

### Próximo hito obligatorio

`EXP11B_BANK_MATERIALIZATION_GATE`

Objetivo:

1. materializar exactamente los 10 H150 y 10 H200 desde `H100_FROZEN + DAM lists congeladas`;
2. verificar que H100 es núcleo idéntico;
3. verificar DAM exactas, sin faltantes ni extras;
4. verificar row counts y composition SHA;
5. verificar nesting H150⊂H200 por réplica;
6. recalcular descriptores totales;
7. generar manifest e inventario SHA de los 20 bancos;
8. validar en clean checkout;
9. **NO ejecutar retrieval/BM25**.

Solo después de auditoría externa de esta materialización podrá considerarse `EXP11B_RETRIEVAL_AUTHORIZED=true`.

### 2026-09-01 — EXP11B Bank Materialization candidato `7a80b1d` auditado externamente

**Estado:** `APPROVED_WITH_BLOCKING_MICROCLOSE_BEFORE_MAIN`.

- Rama: `codex/exp11b-bank-materialization-v01`.
- Candidato: `7a80b1db657386705d3031559c2861d0a2f88eb2`.
- Padre directo: `ed470d67315f505cb3bde471177268db6d16a676`.
- Relación main→candidate: 0 behind / 1 ahead.
- 20 bancos materializados localmente:
  - 10 H150;
  - 10 H200.
- H100 core: 20/20 PASS.
- Selección Gate03: 20/20 PASS.
- Descriptores: 20/20 PASS.
- Nesting: 10/10 PASS.
- Hashes de bancos: 20 identidades congeladas; clean checkout reprodujo 20/20 byte exacto.
- Bancos CSV no versionados en Git; son derivados regenerables.
- Manifest y hash inventory sí están versionados.
- No retrieval, BM25 ni métricas de evaluación.

#### EXP11B-MAT-F001 — DEV_EVAL_PROVENANCE_NOT_HASH_FROZEN — S2

El materializer usa DEV y EVAL para bloquear overlap de DAM, por lo que ambos son inputs científicos efectivos. Sin embargo:

- `exp11b_bank_materialization_v0.1.json` registra solo sus paths, no SHA;
- `load_inputs()` los lee sin `validate_file_contract`;
- el manifest de materialización no registra DEV/EVAL como inputs observados.

Antes de integrar debe fijarse en config y manifest:

- DEV SHA `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`;
- EVAL SHA `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`;

y el script debe fallar si cambian. Esto no puede modificar ninguno de los 20 bank SHA.

#### EXP11B-MAT-F002 — FROZEN_GATE03_TEST_WEAKENED_OUTSIDE_SCOPE — S2

El commit candidato modificó además `tests/test_exp11b_historical_size_extension_v01.py`, cambiando una aserción de HHI de `assertEqual` a `assertAlmostEqual(..., places=15)`.

Este archivo no formaba parte del scope materializador y Gate03 ya estaba cerrado. La modificación debe revertirse exactamente al contenido de `ed470d6`. Si el test exacto falla, debe detenerse y reportar los dos floats; no se permite debilitar silenciosamente un test congelado.

#### EXP11B-MAT-F003 — HASH_INVENTORY_VERIFY_NOT_FAIL_CLOSED — S2

`verify()` reconstruye y compara correctamente el manifest de bancos, pero al leer `exp11b_bank_hashes_v0.1.csv` solo exige 20 filas y bank_id completos. No compara los valores de cada fila del inventario contra los bancos/manifest.

Debe verificar al menos, por bank_id:

- bank_csv_sha256;
- size_bytes;
- row_count;
- new_row_count;
- total_dam_count;
- new_dam_count;
- composition_sha256;
- H100_core_id_order_sha256;
- increment_id_order_sha256;
- total_bank_id_order_sha256.

La corrección no puede alterar los 20 CSV ni sus hashes.

### Estado

- `EXP11B_BANK_MATERIALIZATION_CANDIDATE_CREATED=true`.
- `BANKS_BYTE_REPRODUCIBLE=20/20`.
- `EXP11B_BANK_MATERIALIZATION_EXTERNAL_APPROVAL=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `RETRIEVAL_EXECUTED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

**No integrar a main hasta cerrar MAT-F001..F003.**

### 2026-09-01 — Microclose materialization detenido por diferencia float de 1 ULP

- HEAD/remoto permanecen `7a80b1db657386705d3031559c2861d0a2f88eb2`.
- `main = origin/main = ed470d67315f505cb3bde471177268db6d16a676`.
- Los 20 bancos canónicos no fueron reescritos.
- MAT-F001 y MAT-F003 no se iniciaron.
- El test Gate03 se restauró exactamente a `ed470d6`.
- Resultado Gate03 con igualdad exacta: 28/29.
- Valor congelado `dam_hhi = 0.13446841032608695`.
- Recomputación Python 3.12.13: `0.13446841032608697`.
- Diferencia binaria real: `2.7755575615628914e-17`, exactamente **1 ULP** en esa magnitud.
- Python 3.12 cambió el algoritmo de `sum()` para floats por uno de mayor precisión; por tanto, igualdad bit-a-bit de un descriptor float recalculado entre runtimes no es un contrato portable.
- El criterio ya usado por el materializer para descriptores es tolerancia absoluta `1e-12`.

#### Re-clasificación externa de MAT-F002

`EXP11B-MAT-F002 = GATE03_FLOAT_SUM_PORTABILITY_DEFECT / S2_PROCEDURAL`.

Resolución autorizada:

- NO cambiar el descriptor congelado Gate03;
- NO recalcular ni reescribir feasibility;
- NO cambiar los 20 bank SHA;
- sustituir el test exacto por una comparación explícita con `abs_tol=1e-12`, `rel_tol=0`, documentando que es una corrección de portabilidad numérica;
- añadir control de que el delta observado está dentro de tolerancia y que el descriptor sigue siendo distinto del descriptor incremental;
- después continuar MAT-F001 y MAT-F003.

Esto no altera selección, composición, resultados ni interpretación científica.

### 2026-09-01 — EXP11B Bank Materialization microclose `95ffec45` aprobado externamente

**Estado:** `APPROVED_FOR_MAIN_INTEGRATION`.

- Rama: `codex/exp11b-bank-materialization-v01`.
- Candidato inicial: `7a80b1db657386705d3031559c2861d0a2f88eb2`.
- Microclose: `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.
- `main = origin/main = ed470d67315f505cb3bde471177268db6d16a676` permanece sin merge.
- Relación `7a80b1d → 95ffec45`: 1 commit, 0 behind.
- Relación `main → 95ffec45`: 2 commits prospectivos del gate de materialización.

#### Findings cerrados

- `EXP11B-MAT-F001=VERIFIED_RESOLVED`.
  - DEV SHA `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`, 100 filas.
  - EVAL SHA `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`, 1,056 filas.
  - Ambos inputs se validan fail-closed y quedan registrados con SHA esperado/observado en el manifest.

- `EXP11B-MAT-F002=VERIFIED_RESOLVED`.
  - Política de portabilidad float: `rel_tol=0`, `abs_tol=1e-12`.
  - Diferencia documentada: `2.7755575615628914e-17` (1 ULP) en Python 3.12.13.
  - Gate03: 30/30 PASS.
  - Planner, feasibility, selección y bank identities no cambiaron.

- `EXP11B-MAT-F003=VERIFIED_RESOLVED`.
  - `--verify` compara campo a campo las 14 columnas del ledger de hashes.
  - Pruebas de corrupción del ledger fallan de forma cerrada.

#### Identidad y reproducibilidad

- 20/20 bank SHA preservados contra `7a80b1d`.
- 20/20 tamaños, filas, composition SHA y hashes de orden de IDs preservados.
- Los CSV canónicos no fueron reescritos.
- Clean checkout: bancos ausentes como corresponde; rematerialización temporal 20/20 byte exacta.
- Tests en Python 3.12.13:
  - base `ed470d6`: 326 tests; único fallo = comparación float exacta documentada;
  - candidato corregido: 368/368;
  - Gate02 27/27;
  - Gate03 30/30;
  - materialización 41/41.
- Formal `--verify`: PASS.
- `retrieval_executed=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.

### Próximo paso

Integrar `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` a `main` por fast-forward, ejecutar verificación post-integración y rematerialización temporal 20/20.

**Solo después de cerrar la integración del Bank Materialization Gate podrá abrirse el gate de ejecución EXP-11B retrieval.**

### 2026-09-01 — EXP11B Bank Materialization Gate cerrado e integrado

**Estado:** `CLOSED / APPROVED / INTEGRATED TO MAIN`.

- `main = origin/main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.
- Cadena de integración:
  - `7a80b1db657386705d3031559c2861d0a2f88eb2` — materialización y freeze de identidades;
  - `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` — microclose de procedencia/fail-closed.
- La relación desde `ed470d6` es 0 behind / 2 ahead.
- Post-push clean checkout:
  - suite completa `368/368`;
  - rematerialización temporal `20/20` byte exacta;
  - 0 discrepancias.
- F001/F002/F003 permanecen `VERIFIED_RESOLVED`.
- Los 20 bancos no están versionados en Git; sus identidades, manifests y hashes sí están congelados.
- `BANK_IDENTITIES_MATCH=20/20`.
- `BANKS_BYTE_REPRODUCIBLE=true`.
- `H100_CORE_MATCH_ALL=true`.
- `SELECTION_MATCH_ALL=true`.
- `DESCRIPTORS_MATCH_ALL=true`.
- `NESTING_MATCH_ALL=true`.
- `RETRIEVAL_EXECUTED=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

#### Limpieza local pendiente

Codex alcanzó a verificar que el worktree post-push estaba limpio y que podía retirarse. Solo quedó pendiente ejecutar:

`git worktree remove "<ruta-del-worktree-post-push>"`

y luego:

`git worktree prune`

sin `--force`.

Esta limpieza es **operativa, no científica** y no bloquea el cierre del Bank Materialization Gate. Si Windows deja metadatos huérfanos por permisos, se registra como limitación local no científica siempre que el worktree ya no aparezca en `git worktree list`.

### Próximo hito científico

`EXP11B RETRIEVAL EXECUTION GATE`

Debe congelar prospectivamente, antes de BM25:
- commit integrado `95ffec45...`;
- SHA del materialization manifest;
- SHA del ledger de los 20 bancos;
- 20 bank SHA;
- EVAL SHA;
- configuración BM25 exacta;
- normalización/tokenización;
- valores k;
- outputs/manifest;
- política de ejecución única y fail-closed;
- denominador primario `N=1056`;
- common-clean solo como sensibilidad complementaria.

No ejecutar retrieval hasta aprobar externamente ese gate.

### 2026-09-06 — EXP-04-D1a / 0B-05C: auditoría pre-ejecución y microclose F001–F003

**Estado:** `CANDIDATE_FOR_EXTERNAL_AUDIT`.

- Conforme a `D-011`, este Markdown es el Plan Maestro canónico SRC-03. El libro
  `docs/plan_fases_proyecto_investigacion_v0.1.xlsx` es un tracker histórico
  secundario y no gobierna la planificación experimental.
- `EXP11B_RETRIEVAL_GATE=APPROVED_AND_INTEGRATED` en
  `main = origin/main = 37eaa712bd12914b97e8fc108b96dc6e68c4e460`.
  `EXP11B_RETRIEVAL_EXECUTION=NOT_AUTHORIZED`, `RETRIEVAL_EXECUTED=false`,
  `EVALUATION_METRICS_COMPUTED=false`, `H150_H200_RESULTS_OBSERVED=false` y
  `EXP12_AUTHORIZED=false`.
- Se abre el microclose `0B-05C` para los hallazgos F001–F003 de la auditoría
  pre-ejecución D1a. No autoriza ni ejecuta una corrida correctiva D1a,
  reconstrucción de índice, retrieval H150/H200, ni cálculo de métricas nuevas.
- El Top-200 original D1a permanece congelado con 1,056 consultas y 200 rangos
  por consulta; no registra ocurrencias de `87044110` ni `87045110`.
- La exposición de entrenamiento se demuestra desde el H100 congelado
  `data/processed/data_aduanas_historico_clase87_v0.2.csv`, SHA-256
  `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`:
  2,950 filas, 66 códigos históricos y ausencia de ambos códigos afectados.
  La fuente de negativos registrada es exclusivamente `historical training codes
  + frozen normative corpus only`. La reconstrucción determinista es
  corroborativa y no identifica el checkout histórico de ejecución.
- `D1A_EXECUTION_SPECIFICATION=CLOSED_PROSPECTIVELY`: se congela una definición
  correctiva de dos códigos basada en la Decisión 906, Gaceta Oficial 5062, con
  pesos D1a originales, reconstrucción atómica de índice y mapping, evaluación
  NANDINA-8 y un root de salida nuevo fail-closed. La métrica correctiva sigue
  `NOT_DETERMINED`, la ejecución numérica no está autorizada, no se justifican
  pasos posteriores y el cierre de 0B-05C no está autorizado.

### 2026-09-07 — Reconciliación canónica posterior a la integración de 0B-05C

**Estado histórico:** `APPROVED / INTEGRATED` en
`main = origin/main = 0e074db638f6b7163d98d34f08f76e1efde07b7f`.

- `D1A_PREEXECUTION=APPROVED / INTEGRATED`.
- `0B05C_CORRECTIVE_NUMERICAL_GATE=APPROVED / INTEGRATED`.
- `0B05C-GATE-F001=CLOSED / PASS`, `F002=CLOSED / PASS`,
  `F003=CLOSED / PASS` y `F004=CLOSED / PASS`.
- `0B05C_NUMERICAL_AUTHORIZATION_GATE=NEXT / NOT_YET_EXECUTED`.
  `EV03_NUMERICAL_EXECUTION=NOT_AUTHORIZED`,
  `EV04_NUMERICAL_EXECUTION=NOT_AUTHORIZED`,
  `D1A_NUMERICAL_EXECUTION=NOT_AUTHORIZED` y
  `UNIFIED_0B05C_NUMERICAL_EXECUTION=NOT_AUTHORIZED`.
- `0B05C_METRIC_IMPACT=NOT_DETERMINED`,
  `DOWNSTREAM_REEXECUTION=NOT_YET_JUSTIFIED` y
  `0B05C_CLOSURE=NOT_AUTHORIZED`.
- `EXP11B_PORTABILITY_DEBT=OPEN`; bloquea D1a=`false` y la autorización de
  retrieval EXP11B=`true`. Esta reconciliación no crea un authorization record,
  no ejecuta sensibilidad numérica y no registra impacto métrico.

### 2026-09-08 — Integración del test harness compatible con autorización

**Registro prospectivo:** `APPROVED / INTEGRATED` en
`main = origin/main = 0ab12515c786e26660d4f7db03fd745887ab83e8`.

- `0B05C_AUTHORIZATION_TEST_HARNESS=APPROVED / INTEGRATED`.
- `0B05C-AUTH-F001=CLOSED / PASS`.
- `D1A_PREEXECUTION=APPROVED / INTEGRATED` y
  `0B05C_CORRECTIVE_NUMERICAL_GATE=APPROVED / INTEGRATED` permanecen sin cambio.
- `0B05C_NUMERICAL_AUTHORIZATION_GATE=NEXT / NOT_YET_EXECUTED`.
  `EV03_NUMERICAL_EXECUTION=NOT_AUTHORIZED`,
  `EV04_NUMERICAL_EXECUTION=NOT_AUTHORIZED`,
  `D1A_NUMERICAL_EXECUTION=NOT_AUTHORIZED` y
  `UNIFIED_0B05C_NUMERICAL_EXECUTION=NOT_AUTHORIZED`.
- `0B05C_METRIC_IMPACT=NOT_DETERMINED`,
  `DOWNSTREAM_REEXECUTION=NOT_YET_JUSTIFIED` y
  `0B05C_CLOSURE=NOT_AUTHORIZED`.
- `EXP11B_PORTABILITY_DEBT=OPEN`. La integración modifica exclusivamente el
  test harness; no cambia el estado científico ni autoriza ejecución.

### 2026-09-08 — Integración de la autorización numérica 0B-05C

**Estado histórico:** `APPROVED / INTEGRATED` en
`main = origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`.

- `0B05C_NUMERICAL_AUTHORIZATION_GATE=APPROVED / INTEGRATED`.
- `EV03_NUMERICAL_EXECUTION=AUTHORIZED / NOT_EXECUTED`,
  `EV04_NUMERICAL_EXECUTION=AUTHORIZED / NOT_EXECUTED`,
  `D1A_NUMERICAL_EXECUTION=AUTHORIZED / NOT_EXECUTED` y
  `UNIFIED_0B05C_NUMERICAL_EXECUTION=AUTHORIZED / NOT_EXECUTED`.
- `authorization_record_present=true` y
  `runtime_authorization_record_present=false`.
- `corrective_retrieval_executed=false` y
  `corrective_metrics_computed=false`.
- `0B05C_AUTHORIZATION_TEST_HARNESS=APPROVED / INTEGRATED` y
  `0B05C-AUTH-F001=CLOSED / PASS` permanecen sin cambio.
- `0B05C_METRIC_IMPACT=NOT_DETERMINED`,
  `DOWNSTREAM_REEXECUTION=NOT_YET_JUSTIFIED` y
  `0B05C_CLOSURE=NOT_AUTHORIZED`.
- `EXP11B_PORTABILITY_DEBT=OPEN`. Esta reconciliación registra únicamente la
  autorización integrada; no registra ejecución numérica ni resultados nuevos.

### 2026-09-08 — Intentos fail-closed y recuperación histórica EV03 v0.2

**Estado consolidado:** `main = origin/main =
43291c312c2934aae03f3c087dd0a1ae594341b7`.

- La autorización v0.1 se conserva como antecedente histórico:
  `authorization_baseline_commit=0e074db638f6b7163d98d34f08f76e1efde07b7f`
  y
  `authorization_integration_commit=06cc75ec173eb6c4b134a45eeb88fe25999f396e`.
  Autorizó prospectivamente EV03, EV04, D1a y unified 0B-05C, pero quedó
  metodológicamente superada para futuros intentos tras detectarse el defecto de
  reproducción EV03.
- `0B05C_NUMERICAL_EXECUTION_ATTEMPT_01=FAIL_CLOSED /
  SCIENTIFIC_STATE_PRESERVED`: authorized preflight PASS; fallo en
  `FAILED_AT_01_UNIFIED_PREFLIGHT`, antes de iniciar EV03, EV04 o D1a, con
  `SANDBOX_WRITE_BOUNDARY_ON_ONEDRIVE_CHECKOUT` y WinError 5 al crear el root
  de runtime. No se calcularon métricas, no hubo decisión downstream y 0B-05C
  no se cerró. La atribución operacional detallada procede de diagnóstico local
  read-only, consistente con GitHub pero no reconstruible íntegramente solo
  desde artefactos remotos.
- `0B05C_NUMERICAL_EXECUTION_ATTEMPT_02=FAIL_CLOSED /
  SCIENTIFIC_STATE_PRESERVED`: authorized preflight PASS; una invocación del
  runner reportada; step 01 alcanzado; fallo en
  `02_EV03_control_reproduction` con `ContractViolation: Mandatory control
  reproduction is not exact`. EV04, D1a y corrected arms no se iniciaron y no
  se calcularon métricas correctivas. El mismatch reportado fue 50,327 filas
  congeladas frente a 79,912 observadas; primer witness
  `DA-EVAL-V02-00001`; top-1 congelado
  `39173210 / 21.311974833146948`; top-1 observado
  `29314600 / 21.825923130489294`. Los outputs locales ignorados del intento no
  son artefactos gobernantes.
- `EV03_REPRODUCTION_ROOT_CAUSE=CURRENT_BUILDER_SEMANTICS_MISMATCH`: el builder
  global/current conserva tokens alfanuméricos de longitud 1; la semántica
  histórica EV03 recuperada aplica `DROP_SINGLE_CHARACTER_TOKENS`.
  `AUTHENTIC_HISTORICAL_SOURCE_PY=NOT_VERSIONED_AT_INDEX_CREATION`: se recuperó
  y validó la semántica funcional relevante, no el código fuente histórico
  auténtico.
- `EV03_HISTORICAL_RECOVERY_V02=APPROVED / VERSIONED / INTEGRATED`: candidate
  `cef8d7ad58d877e933f8c86b9f721cb214d9058d`; microclose
  `43291c312c2934aae03f3c087dd0a1ae594341b7`;
  `LOGICAL_INDEX_IDENTITY=EXACT`;
  `EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT`; 50,327 filas de ranking,
  SHA-256
  `d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015`;
  1,056 filas de case summary, SHA-256
  `f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0`;
  metric table y full metrics exactos; F001–F004 cerrados; reglas LF y bindings
  canónicos incorporados.
  `HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED`.
- El bundle v0.2 integrado tiene
  `gate_scope=EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY` y
  `authorization_readiness=NOT_AUTHORIZATION_READY`.
  `EV03_V02_NUMERICAL_EXECUTION=NOT_AUTHORIZED / NOT_EXECUTED`,
  `EV04_V02_NUMERICAL_EXECUTION=NOT_AUTHORIZED / NOT_EXECUTED`,
  `D1A_V02_NUMERICAL_EXECUTION=NOT_AUTHORIZED / NOT_EXECUTED` y
  `UNIFIED_0B05C_V02_NUMERICAL_EXECUTION=NOT_AUTHORIZED / NOT_EXECUTED`.
  `corrective_retrieval_executed=false`, `corrective_metrics_computed=false`,
  `runtime_authorization_record_v02_present=false`,
  `0B05C_METRIC_IMPACT=NOT_DETERMINED`,
  `DOWNSTREAM_REEXECUTION=NOT_YET_JUSTIFIED` y
  `0B05C_CLOSURE=NOT_AUTHORIZED`.
- El siguiente paso es construir y auditar prospectivamente un gate/runner
  numérico v0.2 separado. La recuperación integrada no constituye autorización
  numérica.

### 2026-09-12 — Integración de Attempt06 y cierre de 0B-05C

**Interpretación numérica y clasificaciones de esta entrada:**
`SUPERSEDED_BY_POST_PROMPT38_EXTERNAL_AUDIT`. Los valores que siguen se
preservan exclusivamente como registro histórico de Prompt38 y no son el estado
canónico. La corrección vinculada a los comparadores versionados se registra en
la entrada cronológica posterior.

**Estado canónico:** `main = origin/main =
6846537602539506c8e90426daad05252cc982b9`.

- El candidato técnico `0B-05C v0.5` quedó `APPROVED / INTEGRATED`; su
  autorización Attempt06 fue auditada y
  `ATTEMPT06=COMPLETED / AUDITED / INTEGRATED`, con `19/19` pasos `PASS`.
- `EV03_METRIC_IMPACT=ZERO_AGGREGATE_CHANGE`: original y corrected son
  exactamente iguales para MRR `0.40223149245938034`, Top-1
  `0.3494318181818182`, Top-3 `0.4431818181818182`, Top-5
  `0.47632575757575757`, Top-10 `0.5208333333333334`, Top-50/Recall@50
  `0.5928030303030303` y Recall@100 `0.6401515151515151`.
- `EV04_METRIC_IMPACT=ZERO_AGGREGATE_CHANGE`: original y corrected son
  exactamente iguales para MRR `0.41801769149469725`, MRR@100
  `0.4209029085295853`, MRR@200 `0.42114657818747986`, contribución 101-200
  `0.00024366965789453498`, Top-1 `0.36742424242424243`, Top-3
  `0.45738636363636365`, Top-5 `0.48295454545454547`, Top-10
  `0.5265151515151515`, Top-50/Recall@50 `0.6742424242424242` y Recall@100
  `0.740530303030303`.
- `D1A_METRIC_IMPACT=POSITIVE_NONZERO_EARLY_RANK_CHANGE`: la corrección
  Decision 906 mejora MRR@10 de `0.06823809523809526` a
  `0.08020006613756614` (delta `+0.011961970899470875`), Top-1 de
  `0.032196969696969696` a `0.038825757575757576` (delta
  `+0.006628787878787879`), Top-3 de `0.06723484848484848` a
  `0.08238636363636363` (delta `+0.015151515151515152`), Top-5 de
  `0.08712121212121213` a `0.10321969696969698` (delta
  `+0.01609848484848485`) y Top-10 de `0.16287878787878787` a
  `0.17897727272727273` (delta `+0.016098484848484862`). En jerarquía,
  partida@10 cambia de `0.42045454545454547` a `0.4393939393939394`,
  sub_partida@10 de `0.3494318181818182` a `0.3683712121212121` y clase@10
  de `0.2774621212121212` a `0.29640151515151514`, con delta común
  `+0.018939393939393923`; partida@50 cambia de `0.7367424242424242` a
  `0.7414772727272727` (delta `+0.004734848484848509`), sub_partida@50 de
  `0.6676136363636364` a `0.6714015151515151` y clase@50 de
  `0.6136363636363636` a `0.6174242424242424`, ambos con delta
  `+0.0037878787878787845`. Las jerarquías @100 y @200 permanecen sin cambio.
  Este resultado no declara significancia estadística, efecto causal ni
  generalización fuera de la sensibilidad determinista.
- `0B05C_METRIC_IMPACT=METHOD_DEPENDENT / NONZERO_ONLY_D1A`: la actualización
  normativa no altera las métricas agregadas de EV03/EV04 y sí mejora las
  posiciones tempranas de D1a; el efecto no es uniforme entre métodos.
- `DOWNSTREAM_REEXECUTION=NOT_REQUIRED` y
  `FUTURE_ANALYSES_MUST_USE=ATTEMPT06_CORRECTED_D1A_RESULTS`. EXP11B Retrieval
  y EXP12 no se ejecutaron; Grupo 3 y Grupos 4-8 permanecen pendientes y pueden
  consumir prospectivamente los resultados D1a corregidos.
- `0B05C_CLOSURE=CLOSED / APPROVED`. No se abre otra remediación 0B-05C. Los
  Attempts fail-closed previos y sus evidencias se conservan sin reescritura.
- `EXP11B_PORTABILITY_DEBT=OPEN`; este cierre no autoriza EXP11B Retrieval ni
  EXP12, que permanecen `NOT_AUTHORIZED / NOT_EXECUTED`.

### 2026-09-12 — Corrección de interpretación Attempt06 posterior a Prompt38

**Estado canónico:** `main = origin/main =
6846537602539506c8e90426daad05252cc982b9`.

- Fuentes contractuales verificadas directamente en `main`:
  `outputs/evaluation/0b05c_corrective_numerical_v0.5/ev03_aggregate_comparison_v0.5.json`
  (blob Git `1fa1aed2584c5612bbc5be16173e93d80c2dd92e`),
  `outputs/evaluation/0b05c_corrective_numerical_v0.5/ev04_aggregate_comparison_v0.5.json`
  (blob Git `3bf28c036b0a0af5dd54d88c3b0050c60365b7f1`) y
  `outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_corrective_vs_original_comparison_v0.5.json`
  (blob Git `6a26777395630722a18bca7826b7df96613ea4ea`).
- `EV03_METRIC_IMPACT=ZERO_AGGREGATE_CHANGE`: original y corrected son
  exactamente iguales para MRR `0.04229731726741296`, Top-1
  `0.027462121212121212`, Top-3 `0.05113636363636364`, Top-5
  `0.061553030303030304`, Top-10 `0.06534090909090909`, Top-50/Recall@50
  `0.07007575757575757` y Recall@100 `0.07102272727272728`.
- `EV04_METRIC_IMPACT=TINY_NONZERO_MRR_DECREASE_ONLY`: MRR@100 cambia de
  `0.04198129438896378` a `0.041971783226435376` y MRR@200 de
  `0.04334161160288281` a `0.043332100440354404`, ambos con delta
  `-9.511162528404171e-06`. La contribución MRR 101-200 permanece en
  `0.0013603172139190346`; Top-1 `0.026515151515151516`, Top-3
  `0.052083333333333336`, Top-5 `0.0625`, Top-10 `0.06534090909090909`,
  Top-50/Recall@50 `0.09090909090909091`, Recall@100
  `0.10132575757575757` y Recall@200 `0.3039772727272727` también permanecen
  iguales. Los demás indicadores discretos y jerárquicos del agregado tienen
  delta cero; el cambio no nulo de MRR ocurre dentro de los primeros 100 rangos.
- `D1A_METRIC_IMPACT=POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT`.
  El comparador contractual no contiene MRR@10. Top@1 cambia de `0.0` a
  `0.000946969696969697` (delta `+0.000946969696969697`), Top@3 de
  `0.003787878787878788` a `0.010416666666666666` (delta
  `+0.006628787878787878`), Top@5 de `0.03409090909090909` a
  `0.05113636363636364` (delta `+0.01704545454545455`), Top@10 de `0.15625`
  a `0.17803030303030304` (delta `+0.02178030303030304`) y Top@50 de
  `0.3058712121212121` a `0.3134469696969697` (delta
  `+0.0075757575757576245`). Recall@100 y Exact@100 permanecen en
  `0.3456439393939394`; Recall@200 y Exact@200 cambian de
  `0.3626893939393939` a `0.36363636363636365` (delta
  `+0.0009469696969697239`). MRR@100 cambia de `0.03242432639034634` a
  `0.038087139731859634` (delta `+0.0056628133415132925`) y MRR@200 de
  `0.03254853477630825` a `0.038217181295822696` (delta
  `+0.005668646519514445`). HS6@100 permanece en `0.36553030303030304` y
  HS6@200 en `0.38825757575757575`; HS4@100 cambia de `0.8731060606060606` a
  `0.8797348484848485` (delta `+0.006628787878787956`), mientras HS4@200
  cambia de `0.9640151515151515` a `0.9630681818181818` (delta
  `-0.0009469696969697239`, equivalente a `1/1056`). Chapter@100 permanece
  en `0.9801136363636364` y Chapter@200 en `1.0`.
- No se declara significancia estadística, efecto causal ni generalización.
  `0B05C_METRIC_IMPACT=METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`: EV03 no
  cambia; EV04 presenta una disminución muy pequeña restringida a MRR@100 y
  MRR@200; D1a mejora predominantemente en ranking exacto y MRR, con un efecto
  jerárquico menor mixto en HS4. El efecto no es uniforme entre métodos.
- `ATTEMPT06=COMPLETED / AUDITED_EXECUTION / INTEGRATED` y
  `PROMPT38_RESULT_INTERPRETATION=REJECTED / SUPERSEDED_BY_PROMPT39`.
- `DOWNSTREAM_REEXECUTION=NOT_REQUIRED` y
  `FUTURE_ANALYSES_MUST_USE=ATTEMPT06_CORRECTED_RESULTS`. No existe resultado
  downstream completado que deba repetirse: EXP11B Retrieval y EXP12 siguen no
  ejecutados, y Grupo 3 y Grupos 4-8 permanecen pendientes.
- `0B05C_CLOSURE=CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`. No se
  abre otra ejecución 0B-05C ni se autoriza otra corrida.
- `EXP11B_PORTABILITY_DEBT=OPEN`; EXP11B Retrieval y EXP12 permanecen
  `NOT_AUTHORIZED / NOT_EXECUTED`.

### 2026-09-12 — Cierre de deuda de portabilidad EXP11B

**Estado canónico:** `main = origin/main =
09ff184854659110f7711b3eee65fc18927649da`.

- El candidato Prompt40 `799156b3c98858fbe081de73f381030426174ce1`
  permanece `REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED`.
- `PROMPT41_EXTERNAL_AUDIT=PASS / APPROVED_FOR_INTEGRATION` y
  `PROMPT41_REPLAY_PROOF=APPROVED / INTEGRATED_IN_MAIN` como
  `7d7267f8224e56ea5e945625a7e3955ddc15eadb`.
- La evidencia runtime de Prompt41 permanece clasificada como
  `CODEX_LOCAL_RUNTIME_EVIDENCE /
  NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR`.
- El `process_return_code=2` fue aceptado como no bloqueante exclusivamente
  para la identidad bancaria gobernada: los 14 campos contractuales y las
  tres comparaciones FROZEN/OFFICIAL/REPLAY pasaron `20/20`, con cero
  mismatches. El campo terminal `total_bank_descriptor` no forma parte de los
  14 campos; el delta máximo `5.329070518200751e-15` quedó dentro de la
  tolerancia histórica `1e-12`, sin afectar el contenido de los CSV.
- `PROMPT42_EXTERNAL_GIT_AUDIT=PASS / APPROVED_FOR_INTEGRATION`. El closure
  record quedó integrado en `main` como
  `09ff184854659110f7711b3eee65fc18927649da` en
  `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_external_closure_v0.1.json`.
- `EXP11B_PORTABILITY_DEBT=CLOSED / APPROVED / INTEGRATED`. El notice
  histórico del retrieval gate permanece inmutable; su condición de bloqueo
  por deuda de portabilidad fue superada prospectivamente por el cierre
  aprobado.
- Cierre de deuda no equivale a autorización de retrieval. EXP11B Retrieval
  H150/H200 requiere un bloque prospectivo separado de autorización y
  permanece `NOT_AUTHORIZED / NOT_EXECUTED`.
- `EXP12=NOT_AUTHORIZED / NOT_EXECUTED`. Grupo 2B y los bloques posteriores no
  fueron abiertos.

### 2026-09-12 — Integración de resultados y cierre de EXP11B Retrieval H150/H200

**Estado vigente reconciliado:** `main = origin/main =
dfd04f0db26383624d54e52bf4fd72f06bbb869c`.

- `PROMPT48_EXTERNAL_AUDIT=PASS / APPROVED_WITH_NONBLOCKING_LIMITATIONS`.
- `EXP11B_RETRIEVAL_AUTHORIZATION=APPROVED / INTEGRATED / CONSUMED`.
- `EXP11B_RETRIEVAL_ATTEMPT_001=EXECUTED_ONCE / COMPLETED / APPROVED`.
- `EXP11B_RETRIEVAL_RESULTS=APPROVED / INTEGRATED`.
- `EXP11B=CLOSED / APPROVED / INTEGRATED`.

Resultados descriptivos oficiales de los diez bancos H150:

- Top-1 `0.512689393939394`; Top-3 `0.6899621212121212`; Top-5
  `0.7833333333333333`; Top-10 `0.8915719696969697`; Top-50
  `0.9895833333333334`; MRR `0.6332675214603809`.

Resultados descriptivos oficiales de los diez bancos H200:

- Top-1 `0.5141098484848485`; Top-3 `0.6894886363636363`; Top-5
  `0.7820075757575757`; Top-10 `0.8952651515151515`; Top-50
  `0.9852272727272726`; MRR `0.6333104425906166`.

Estas cifras son observaciones descriptivas oficiales; esta entrada no añade
interpretación causal ni generaliza fuera del alcance experimental congelado.

**Limitación no bloqueante de persistencia.** El artefacto completo
`exp11b_retrieval_candidates_v0.1.csv` tiene `size_bytes=264935868`, SHA-256
`1dde84b65d8fb060211120ac73a04f1d5a5f7593e6381ed601fbdfb3f4bc9024`
y estado
`LOCAL_OFFICIAL_ARTIFACT_NOT_VERSIONED_DUE_TO_GIT_BLOB_LIMIT_GUARD`. No fue
byte-verificado independientemente por la auditoría Git externa; su identidad
quedó fijada por hash y tamaño en el ledger y en el execution record. Los
outputs primarios versionables —metrics, case-level, summaries, manifest,
environment, failure ledger y hash ledger— sí quedaron versionados. Esta
limitación no invalida los resultados ni bloquea EXP12. Grupo 2B deberá
conservarla en su matriz final de reproducibilidad/trazabilidad y, si
corresponde, definir el mecanismo final de archivo o distribución sin
modificar el resultado científico.

**Limitación no bloqueante de evidencia runtime.** La evidencia conserva la
clasificación `CODEX_LOCAL_OFFICIAL_EXECUTION_EVIDENCE /
NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR`. La auditoría externa
verificó Git, los artefactos versionados, los contratos y la consistencia
matemática disponible; no reejecutó la corrida oficial ni inspeccionó
directamente los bytes del CSV local-only.

**Notice de procedencia del config.** El SHA-256 del config canónico en Git es
`2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af`; el
run manifest registra para los bytes raw del working tree
`0decc631705ae09078bd122b271f25912659574d86166a19e0a431c94af205b9`.
La transformación temporal LF→CRLF del blob canónico reproduce exactamente el
segundo SHA y ambos JSON parsean al mismo objeto. Por tanto,
`EXP11B_EXECUTION_CONFIG_SHA_NOTICE=VERIFIED_EOL_ONLY_WORKTREE_VARIATION` y
`CONFIG_SEMANTIC_DRIFT=false`. No se modificaron retrospectivamente el run
manifest, la autorización ni el config.

- `NEXT_ELIGIBLE_BLOCK=EXP12_PROSPECTIVE_PREPARATION_OR_AUTHORIZATION`.
- `EXP12=NOT_AUTHORIZED / NOT_EXECUTED`.
- `Grupo 2B=NOT_STARTED` y `Grupo 3=NOT_STARTED`.

### 2026-09-12 — Corrección F007 y alcance prospectivo de muestreo EXP12

**Estado vigente reconciliado:** `main = origin/main =
2b9571eee76ecffcaef1abc7fd4a12051f76f906`.

- `PROMPT50_PHASE_A_PLAN_INTEGRATION=PASS / APPROVED`.
- `PROMPT50_PHASE_B_F007_AUDIT=REJECTED`. El candidato
  `ccd10565427a2eb0b938428a68f2b78e538ab144` permanece histórico y no fue
  integrado.
- `PROMPT50_DOCUMENTARY_BINDING_RESULT=AMBIGUOUS_UNDER_STRICT_UNIQUE_RULE`.
  El planeamiento local realizado para la interpretación B se conserva como
  `LOCAL_NONRETRIEVAL_NON_GOVERNING_EVIDENCE_FROM_REJECTED_SOURCE_BINDING` y
  `PROMPT50_INTERPRETATION_B_PLANNING_GOVERNING=false`.
- La decisión metodológica prospectiva específica de EXP12 fija
  `EXP12_SAMPLING_SCOPE=NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY`,
  `H100_ROLE_IN_EXP12=REFERENCE_LABEL_SET_AND_DISTRIBUTION_ONLY` y
  `H100_ROWS_ALLOWED_AS_EXP12_CANDIDATE_SAMPLING_ROWS=false`. Esta decisión no
  modifica ni invalida la construcción H100+incremento ya cerrada de EXP11B.
- La fuente actual es
  `data/interim/new_historical_gate_v0.1/new_historical_eligible.csv`, SHA-256
  `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`:
  6,029 filas, 43 DAM y 56 códigos NANDINA. Contiene 45 de los 66 códigos de
  referencia H100, con cobertura máxima `0.6818181818181818`, y presenta cero
  DAM solapadas con EVAL.
- El contrato conserva `required_label_coverage_fraction=1.0`. Por ello,
  `EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY=FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE`
  y `EXP12_F007=SOURCE_SCOPE_CLARIFIED_CURRENT_GATE_INSUFFICIENT`. La conclusión
  se limita a la insuficiencia de la fuente histórica nueva elegible actualmente
  congelada; no declara que EXP12 sea inviable en términos absolutos.
- Los conteos de composición y cobertura fueron recalculados por Codex sobre
  los artefactos versionados y preservados en el artefacto F007 v0.2. La
  auditoría externa verificó Git, bindings, consistencia metodológica y estado;
  no reivindica haber reejecutado independientemente esa recomputación.
- Permanecen congelados: objetivo 2,950 filas, desviación máxima 148, rango
  2,802–3,098, DAM completas, seeds `20262001..20262010`, HHI primario,
  cobertura H100 1.0, TVD máximo 0.05, 10,000 candidatos por seed, mínimo 30
  factibles, cuantiles 0.10/0.50/0.90, DAM sets distintos, orden estricto
  `HHI_DLOW > HHI_DMID > HHI_DHIGH` y selección sin desempeño EVAL.
- `EXP12=NOT_AUTHORIZED / NOT_EXECUTED`; no se ejecutó planeamiento, retrieval,
  BM25, Top-k ni MRR en Prompt52.
- `NEXT_ELIGIBLE_BLOCK=EXP12_NEW_HISTORICAL_GATE_EXTENSION`. El protocolo
  contempla `NEW_SHEET_SET_2=[NUEVA_01,NUEVA_02]`, pero no se afirma que
  `NUEVA_02` exista, esté disponible, sea válida ni vaya a resolver la brecha
  de cobertura. Una ampliación histórica nueva elegible debe auditarse antes
  de cualquier nuevo planeamiento EXP12.
- `Grupo 2B=NOT_STARTED` y `Grupo 3=NOT_STARTED`.

### 2026-09-13 — Integración de compatibilidad pre-planning EXP12 y fuente v0.2

**Estado vigente reconciliado:** `main = origin/main =
6437a05325bdb01f3cd4964e1b0fae7d3641cc11`.

- `EXP11B=CLOSED / APPROVED / INTEGRATED`.
- `EXP12_NEW_HISTORICAL_GATE_EXTENSION_V02=INTEGRATED` y
  `EXP12_SAMPLING_UNIVERSE=SOURCE_BOUND / APPROVED`.
- Universo EXP12: `data/interim/new_historical_gate_v0.2/new_historical_eligible.csv`,
  SHA-256 `f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457`,
  7,190 filas, 101 DAM, 84 códigos NANDINA y cobertura H100 `66/66`.
- `EXP12_SOURCE_BINDING_V04=INTEGRATED`,
  `EXP12_PREPLANNING_COMPATIBILITY_AUDIT_V01=INTEGRATED` y
  `EXP12_PREPLANNING_CORRECTION_V01=INTEGRATED`.
- La corrección prospectiva fija
  `EXP12_TVD_SUPPORT=FULL_REFERENCE_SUPPORT_PLUS_OTHER`: la masa de códigos
  no presentes en H100 se agrega como `OTHER` con masa de referencia cero y
  sin renormalización condicional sobre los códigos H100.
- Permanecen congelados `EXP12_TVD_MAXIMUM=0.05`,
  `EXP12_LABEL_COVERAGE_REQUIRED=1.0`, `EXP12_TARGET_ROWS=2950`,
  `EXP12_VOLUME_RANGE=[2802,3098]`, `EXP12_CANDIDATE_COUNT=10000`,
  `EXP12_MINIMUM_UNIQUE_FEASIBLE=30`, seeds `20262001..20262010` y cuantiles
  `0.1 / 0.5 / 0.9`.
- Procedencia de NUEVA_02: `NUEVA_02_ACQUISITION_UNIT=COMPLETE_DAM_WITH_ALL_ORIGINAL_SERIES`,
  `NUEVA_02_ACQUISITION_METHOD=SAME_SEARCH_EXTRACTION_COPY_METHOD_AS_INITIAL_DATA_AND_NUEVA_01`,
  `NUEVA_02_SELECTION_BASIS=PREDECLARED_H100_LABEL_COVERAGE_GAP` y
  `NUEVA_02_MODEL_OR_EVAL_PERFORMANCE_SELECTION=NOT_USED`. Esta procedencia
  se clasifica como
  `NUEVA_02_PROVENANCE_EVIDENCE_CLASS=USER_ATTESTED / NOT_INDEPENDENTLY_REPLAYED_AT_ACQUISITION`;
  no constituye verificación independiente de IA Experimental ni Codex.
- El estado anterior de 45/66 códigos del gate v0.1 y
  `EXP12_F007=SOURCE_SCOPE_CLARIFIED_CURRENT_GATE_INSUFFICIENT` se conservan
  como historia `SUPERSEDED_BY_LATER_GATE`. La corrección F007 v0.2, la
  extensión posterior NUEVA_02 y el carácter no gobernante del planeamiento
  local de la interpretación B de Prompt50 permanecen trazables en las
  entradas previas.
- `EXP12_PLANNING=NOT_YET_EXECUTED / NOT_YET_AUTHORIZED`,
  `EXP12_RETRIEVAL=NOT_AUTHORIZED / NOT_EXECUTED` y
  `EXP12=NOT_AUTHORIZED / NOT_EXECUTED`.
- `NEXT_ELIGIBLE_BLOCK=EXP12_PLANNING_EXECUTION_GATE`.
- `Grupo 2B=NOT_STARTED` y `Grupo 3=NOT_STARTED`.

### 2026-09-14 — Attempt001 de planning EXP12 falló en modo one-shot

**Estado vigente reconciliado:** `main = origin/main =
428dfecca5cff313f910032a28a8a3c7ae13c2ef`.

- `EXP12_PLANNING_AUTHORIZATION_V01=INTEGRATED / CONSUMED`.
- `EXP12_PLANNING_ATTEMPT_001=FAILED_ONE_SHOT / AUDITED / INTEGRATED`.
- `EXP12_PLANNING_ATTEMPT_001_FAILURE=Seed 20262001 produced fewer than 30 unique feasible candidates`.
- `EXP12_PLANNING_SUMMARY=NOT_CREATED` y
  `EXP12_PLANNING_OFFICIAL_CONDITIONS=NOT_SELECTED`.
- `EXP12_PLANNING_RETRY=PROHIBITED_UNDER_AUTH_001`.
- `EXP12_PLANNING_GATE=FAILED_UNDER_FROZEN_PLANNING_SEARCH`.
- `EXP12-P61-F001=FAILURE_OBSERVABILITY_GAP / NON_INVALIDATING_FOR_ATTEMPT`.
  El runner lanzó la excepción después del retorno de
  `generate_exp12_candidates(seed=20262001)` y antes de anexar el run al
  summary. No se persistieron el conteo factible exacto ni el breakdown por
  volumen, cobertura, TVD o deduplicación; ninguno es recuperable sin
  recomputación. Por ello no se atribuye causalidad ni se declara que EXP12
  sea definitivamente imposible.
- Se preservan sin cambios source binding v0.4, corrección TVD v0.5,
  autorización one-shot, seeds, thresholds, procedencia de NUEVA_02, estados
  históricos F007 y cierre EXP11B.
- `EXP12_RETRIEVAL=NOT_AUTHORIZED / NOT_EXECUTED` y
  `EXP12=NOT_AUTHORIZED / NOT_EXECUTED`.
- `NEXT_ELIGIBLE_BLOCK=EXP12_FEASIBILITY_FAILURE_FORENSIC_DESIGN`.
- `Grupo 2B=NOT_STARTED` y `Grupo 3=NOT_STARTED`.

### 2026-09-14 — Diagnóstico forense no gobernante de Attempt001 EXP12

**Estado vigente reconciliado:** `main = origin/main =
5787503329afd5ddd5e94d04cdbbdeb000260cda`.

- Prompts61–63 preservaron e integraron el fallo one-shot del planning, su
  evidencia y la fecha canónica, sin retry ni selección de condiciones.
- Prompt64 integró el diseño forense v0.1 sin ejecutar sobre el pool oficial.
- Prompt65 construyó `EXP12_FORENSIC_AUTH_001`; quedó
  `REJECTED_PREEXECUTION / NOT_INTEGRATED` porque la
  auditoría detectó la colisión entre el padre del marcador y el directorio
  reservado de salida antes de cualquier invocación oficial.
- Prompt66 corrigió exclusivamente la orquestación en la autorización v0.2;
  `EXP12_FORENSIC_AUTH_002=INTEGRATED / CONSUMED`.
- Prompt67 ejecutó una sola invocación autorizada:
  `EXP12_FORENSIC_ATTEMPT_001=COMPLETED_ONE_SHOT / AUDITED / INTEGRATED`,
  `OFFICIAL_FORENSIC_INVOCATION_COUNT=1` y
  `EXP12_FORENSIC_RESULT=NON_GOVERNING_FORENSIC_RESULT`.
- Los agregados persistidos son: 10,000 intentados, 0 rechazos por DAM set
  duplicado, 0 rechazos por overlap EVAL, 10,000 únicos no solapados; 1,617
  bajo volumen, 6,821 dentro de rango y 1,562 sobre rango. Entre los 6,821
  dentro de rango, cobertura pasó en 1 y falló en 6,820; TVD pasó en 0 y
  falló en 6,821. El conteo factible final fue `0`, el mínimo requerido `30`
  y el fallo histórico quedó reproducido como `0<30`.
- Para esta búsqueda observada, `TVD<=0.05` fue una restricción vinculante
  universal entre los candidatos que pasaron volumen y cobertura `1.0` fue
  casi universalmente vinculante. Volumen no fue explicación suficiente por
  sí mismo; deduplicación y overlap EVAL no se observaron como cuellos de
  botella.
- La evidencia no demuestra inviabilidad matemática global, no caracteriza
  otros seeds, no valida thresholds alternativos, no prescribe cambios de TVD
  o cobertura y no reemplaza el Attempt001 oficial.
- Se preservan `EXP12_PLANNING_ATTEMPT_001=FAILED_ONE_SHOT / AUDITED /
  INTEGRATED`, `EXP12_PLANNING_RETRY=PROHIBITED_UNDER_AUTH_001` y
  `EXP12_PLANNING_OFFICIAL_CONDITIONS=NOT_SELECTED`.
- `EXP12_RETRIEVAL=NOT_AUTHORIZED / NOT_EXECUTED`,
  `EXP12=NOT_AUTHORIZED / NOT_EXECUTED`, `Grupo 2B=NOT_STARTED` y
  `Grupo 3=NOT_STARTED`.
- `NEXT_ELIGIBLE_BLOCK=EXP12_POST_FAILURE_METHODOLOGICAL_DISPOSITION`.

### 2026-09-14 — Disposición metodológica final EXP12

- `EXP12_ORIGINAL_FROZEN_DESIGN=CLOSED` y
  `EXP12_DISPOSITION=CLOSED_WITHOUT_RETRIEVAL /
  PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH`.
- El contrato exigía los seeds `20262001..20262010`, 10,000 candidatos por
  seed, al menos 30 candidatos factibles únicos por seed y tres condiciones
  D-HIGH/D-MID/D-LOW. El seed obligatorio `20262001` produjo cero candidatos
  factibles frente al mínimo de 30; por tanto, las tres condiciones no podían
  materializarse y el diseño original no podía ejecutarse como fue congelado.
- Se preservan `EXP12_PLANNING_ATTEMPT_001=FAILED_ONE_SHOT / AUDITED /
  INTEGRATED`, `EXP12_PLANNING_RETRY=PROHIBITED_UNDER_AUTH_001`,
  `EXP12_FORENSIC_ATTEMPT_001=COMPLETED_ONE_SHOT / AUDITED / INTEGRATED` y el
  carácter `NON_GOVERNING_FORENSIC_RESULT` del diagnóstico.
- No se probó ningún otro seed. El seed `20262001` no se sustituye ni elimina;
  continuar hasta encontrar seeds viables después del fallo constituiría un
  cambio retrospectivo del protocolo.
- `EXP12_PLANNING_OFFICIAL_CONDITIONS=NOT_SELECTED`,
  `EXP12_DIVERSITY_EFFECT_ESTIMABLE=false` y
  `EXP12_ANALYTICAL_LIMITATION=HISTORICAL_BANK_DIVERSITY_EFFECT_NOT_ESTIMABLE_FROM_EXP12_BECAUSE_OFFICIAL_CONDITIONS_WERE_NOT_MATERIALIZED`.
- `EXP12_RETRIEVAL=NOT_AUTHORIZED / NOT_EXECUTED`. El cierre no equivale a un
  resultado de retrieval ni demuestra un efecto de diversidad histórica.
- `EXP12_REDESIGN_IN_CURRENT_EXPERIMENT=NOT_AUTHORIZED`,
  `EXP12_POST_HOC_PARAMETER_RELAXATION=PROHIBITED` y
  `EXP12_SEED_REPLACEMENT_OR_DROPPING=PROHIBITED`.
- `EXP12_GLOBAL_MATHEMATICAL_INFEASIBILITY_PROVEN=false` y
  `EXP12_OTHER_SEEDS_CHARACTERIZED=false`: la disposición no demuestra
  inviabilidad matemática global ni que TVD `0.05` o cobertura `1.0` sean
  thresholds incorrectos. Un estudio futuro requeriría un protocolo nuevo,
  prospectivo, separado y explícitamente identificado.
- `NEXT_ELIGIBLE_BLOCK=GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE`;
  `Grupo 2B=NOT_STARTED` y `Grupo 3=NOT_STARTED`.

### 2026-09-15 — Cierre de Grupo 2B: reproducibilidad y trazabilidad

- El readiness v0.1 fue rechazado para integración únicamente por los hallazgos
  documentales EXP11A `G2B-RD-F001` y `G2B-RD-F002`; no hubo defecto científico.
- Readiness v0.2 corrigió ambos hallazgos y quedó `AUDITED / APPROVED /
  INTEGRATED` en `main = origin/main =
  fbd321d817d22fef78417064e0d5bc8df37165ca`.
- El registro de cierre de Grupo 2B quedó integrado posteriormente en `main =
  origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f`; el commit del readiness v0.2
  permanece identificado por separado como
  `fbd321d817d22fef78417064e0d5bc8df37165ca`.
- Se inventariaron 47 artefactos. Los 35 identity checks se distribuyen en 31
  pass-equivalent y 4 `HASH_BOUND_LOCAL_ONLY`; estos cuatro no son mismatches.
- Las 11 cadenas end-to-end se clasifican como 1 `COMPLETE` y 10
  `COMPLETE_WITH_DECLARED_LIMITATION`.
- `GROUP2B_BLOCKING_GAP_COUNT=0`,
  `GROUP2B_NONBLOCKING_LIMITATION_COUNT=11` y
  `GROUP2B_HISTORICAL_ONLY_COUNT=5`.
- `ENVIRONMENT_REPRODUCIBILITY=COMPLETE_WITH_DECLARED_LIMITATION` y
  `CLEAN_CHECKOUT_REPRODUCIBILITY=COMPLETE_WITH_DECLARED_LIMITATION`. Las
  limitaciones históricas, los elementos `DECLARED_NOT_RECOVERABLE` y los
  activos `HASH_BOUND_LOCAL_ONLY` permanecen expresamente visibles; no se
  afirma reproducibilidad perfecta.
- `GROUP2B_SCIENTIFIC_REEXECUTION_REQUIRED=false` y
  `GROUP2B_RESULTS_RECOMPUTATION_REQUIRED=false`. No se reabrió EXP12 ni se
  inició Grupo 3.
- `GROUP2B=CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS`, `GROUP3=NOT_STARTED`
  y `NEXT_ELIGIBLE_BLOCK=GROUP3_METRICS_AND_INFERENCE`.

### 2026-09-15 — Gobernanza prospectiva de fichas G3–G8

- Grupo 2B quedó cerrado canónicamente como `CLOSED /
  APPROVED_WITH_NONBLOCKING_LIMITATIONS`.
- Se registró el sistema prospectivo de 19 fichas para los Grupos 3–8,
  referenciado por `docs/fichas-grupos-3-8`, raíz
  `docs/fichas/grupos_3_8/` y snapshot documental
  `a42531ad96fc12bea2f2394b0ff8eb49b66a4238`.
- Ninguna ficha fue activada, autorizada ni ejecutada. `G3-F01` es únicamente
  la siguiente ficha elegible y Grupo 3 permanece `NOT_STARTED`.

### 2026-09-19 — Cierre de G3-F01 tras reauditoría externa

- El contrato analítico corregido de G3-F01 recibió reauditoría externa
  `PASS` y quedó integrado mediante fast-forward puro en `main = origin/main =
  366bf529c29cb999bfd043db33674a510ba184c7`.
- La integración preservó byte-idénticos los artefactos auditados y no ejecutó
  experimentos, métricas ni inferencia.
- El registro de fichas reconcilió post hoc la activación no materializada
  preejecución en `ba9cc595778c4073b3bc20c60ad6a567bf514e9d`.
- Los cierres previos permanecen vigentes:
  `GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS`,
  `EXP12 = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH`,
  `EXP12_DIVERSITY_EFFECT_ESTIMABLE = false`,
  `EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED` y
  `FUTURE_0B05C_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS`.
- `GROUP3 = IN_PROGRESS`; `G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN`.
  `G3_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED` y no ha sido iniciada.
