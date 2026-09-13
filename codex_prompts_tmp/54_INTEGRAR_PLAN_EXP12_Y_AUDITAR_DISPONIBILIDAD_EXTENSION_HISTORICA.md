# PROMPT 54 — INTEGRAR PLAN EXP12 F007 Y AUDITAR DISPONIBILIDAD DE EXTENSIÓN HISTÓRICA

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el candidato del Plan Maestro ya auditado externamente;
2. realizar una **auditoría local, estrictamente de solo lectura, de disponibilidad de una fuente ampliada** para el próximo bloque `EXP12_NEW_HISTORICAL_GATE_EXTENSION`.

Este bloque **NO ingiere datos**, NO rematerializa el pool histórico, NO modifica XLSX, NO ejecuta EXP12, NO genera los 10,000 candidatos por seed, NO ejecuta retrieval/BM25/Top-k/MRR y NO abre Grupo 2B ni Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de Prompt53 concluyó que el candidato del Plan publicado sin cambios es apto para integración:

```text
PLAN_RECONCILIATION_CANDIDATE = APPROVED_FOR_INTEGRATION
candidate_branch = codex/plan-maestro-exp12-f007-v01
candidate_commit = 00adb8f6fc668609500be913203be50a5d402554
candidate_parent = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
candidate_tree = 56e221039aee8d064173dbffb6b2a9e7a8088a4e
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_ELIGIBLE_BLOCK = EXP12_NEW_HISTORICAL_GATE_EXTENSION
```

Estado canónico esperado al inicio:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/plan-maestro-exp12-f007-v01 = 00adb8f6fc668609500be913203be50a5d402554
```

Si existe drift: `STOP / PRECONDITION_REF_DRIFT`.

---

## 2. Fase A — integración exacta del Plan

Verifica antes de integrar:

```text
parent = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
commits_ahead = 1
commits_behind = 0
tree = 56e221039aee8d064173dbffb6b2a9e7a8088a4e
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Integra exclusivamente:

```text
4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
→
00adb8f6fc668609500be913203be50a5d402554
```

mediante fast-forward exacto en `docs/plan-maestro-temporal-2026-08-31`.

Prohibidos: merge commit, squash, cherry-pick, rebase, amend o reconstrucción del markdown.

Después del push exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
```

`main` y Article no deben moverse.

---

## 3. Fase B — auditoría read-only de disponibilidad de extensión histórica

### 3.1 Contrato que debes leer

Lee y respeta íntegramente:

```text
docs/protocolo_expansion_historico_multisheet_v0.1.md
src/configs/new_historical_multisheet_contract_v0.1.json
outputs/audits/new_historical_gate_v0.1/new_historical_ingestion_manifest.json
src/ingestion/prepare_new_historical_multisheet_v0.1.py
```

Hechos que no puedes reinterpretar:

```text
CURRENT_EXP12_SOURCE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
CURRENT_ELIGIBLE_ROWS = 6029
CURRENT_H100_REFERENCE_COVERAGE = 45/66
CURRENT_SOURCE_STATUS = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
VALID_FUTURE_NEW_SHEET_SET_2 = [NUEVA_01, NUEVA_02]
EXPECTED_FUTURE_WORKBOOK_SHEET_ORDER = [Hoja2, Hoja1, NUEVA_01, NUEVA_02]
```

La ampliación futura no puede sustituir, modificar ni reconstruir H100, DEV o EVAL.

### 3.2 Ámbito permitido de búsqueda local

No hagas una búsqueda global del equipo ni del perfil del usuario.

Puedes inspeccionar únicamente:

1. el workbook `NUEVA_01` ya congelado cuya ruta está registrada en `new_historical_ingestion_manifest.json`;
2. el **directorio padre exacto** de ese workbook archivado;
3. el directorio `data/` del repositorio, solo para archivos `.xlsx` situados directamente allí.

No recorras recursivamente OneDrive, Documentos, Downloads, Desktop ni otros árboles ajenos a estos ámbitos.

Ignora:

- archivos temporales `~$*.xlsx`;
- copias sin extensión `.xlsx`;
- cualquier archivo fuera del ámbito permitido.

### 3.3 Inventario read-only

Para cada `.xlsx` candidato dentro del ámbito permitido, registra sin modificarlo:

```text
absolute_path
filename
size_bytes
sha256
sheet_order
```

Clasifica cada archivo como una de estas categorías:

```text
CURRENT_NUEVA01_BASELINE
VALID_NUEVA01_NUEVA02_EXTENSION_CANDIDATE
INVALID_SHEET_SET_OR_ORDER
UNRELATED_XLSX
```

Un candidato válido de extensión debe tener **exactamente**:

```text
[Hoja2, Hoja1, NUEVA_01, NUEVA_02]
```

No aceptes:

- `NUEVA_02` sola;
- orden inverso;
- hojas adicionales;
- ausencia de `NUEVA_01`;
- un workbook con solo `[Hoja2, Hoja1, NUEVA_01]` como si fuera extensión nueva.

### 3.4 Validación no ingerente

Si existe exactamente **un** candidato válido, ejecuta sobre ese archivo, una sola vez:

```powershell
python src/ingestion/prepare_new_historical_multisheet_v0.1.py \
  --validate-new-sheets \
  --future-workbook <CANDIDATO> \
  --new-sheet NUEVA_01 \
  --new-sheet NUEVA_02
```

Este modo es de validación únicamente. Debe terminar `RESULT: PASS` y no crear datasets.

No uses:

```text
--ingest-new-data
--overwrite
--freeze-source
```

en esta fase.

Si la validación falla, conserva el error y clasifica el candidato como inválido. No lo repares ni edites.

### 3.5 Estado de salida

Determina exactamente uno:

```text
A) EXP12_EXTENSION_SOURCE_AVAILABILITY = READY_SINGLE_CANDIDATE
```

solo si existe exactamente un workbook válido y `--validate-new-sheets` pasa.

```text
B) EXP12_EXTENSION_SOURCE_AVAILABILITY = BLOCKED_NO_VALID_CANDIDATE
```

si no existe ninguno.

```text
C) EXP12_EXTENSION_SOURCE_AVAILABILITY = BLOCKED_AMBIGUOUS_MULTIPLE_CANDIDATES
```

si existen dos o más candidatos válidos.

No elijas arbitrariamente entre múltiples candidatos.

La evidencia de esta Fase B debe clasificarse como:

```text
CODEX_LOCAL_SOURCE_AVAILABILITY_AUDIT / NOT_INDEPENDENT_GITHUB_FILE_OBSERVATION
```

No declares que IA Experimental inspeccionó los bytes XLSX locales.

---

## 4. Prohibiciones absolutas

Durante Prompt54 NO:

- modifiques ningún XLSX;
- copies o reconstruyas un workbook;
- agregues `NUEVA_02` a ningún workbook;
- ejecutes `--ingest-new-data`;
- rematerialices `new_historical_eligible.csv`;
- reemplaces outputs de `new_historical_gate_v0.1`;
- modifiques H100, DEV o EVAL;
- leas desempeño EVAL;
- ejecutes EXP12;
- ejecutes candidate generation / 10,000 candidatos por seed;
- ejecutes retrieval/BM25/Top-k/MRR;
- modifiques `src/configs/exp12_historical_diversity_control_v0.3.json`;
- crees autorización EXP12;
- modifiques `main`;
- modifiques Article;
- abras Grupo 2B o Grupo 3.

---

## 5. Verificaciones finales

Exige:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/docs/plan-maestro-temporal-2026-08-31 = 00adb8f6fc668609500be913203be50a5d402554
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
NEW_HISTORICAL_INGESTION_EXECUTED = false
XLSX_WRITE_COUNT = 0
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

---

## 6. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/54_RESPUESTA_INTEGRAR_PLAN_EXP12_Y_AUDITAR_DISPONIBILIDAD_EXTENSION_HISTORICA.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 7. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT54 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

PLAN_CANDIDATE_INTEGRATED = true/false
PLAN_INTEGRATION_MODE

SEARCH_SCOPE
XLSX_FILES_INSPECTED_COUNT
VALID_EXTENSION_CANDIDATE_COUNT

Para cada candidato válido:
- path
- filename
- size_bytes
- sha256
- sheet_order
- validate_new_sheets_return_code
- validate_new_sheets_result

EXP12_EXTENSION_SOURCE_AVAILABILITY = READY_SINGLE_CANDIDATE | BLOCKED_NO_VALID_CANDIDATE | BLOCKED_AMBIGUOUS_MULTIPLE_CANDIDATES
SOURCE_AVAILABILITY_EVIDENCE_CLASS = CODEX_LOCAL_SOURCE_AVAILABILITY_AUDIT / NOT_INDEPENDENT_GITHUB_FILE_OBSERVATION

NEW_HISTORICAL_INGESTION_EXECUTED = false
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT54 = COMPLETED
PLAN_RECONCILIATION = INTEGRATED
EXP12_EXTENSION_SOURCE_AVAILABILITY = <A|B|C>
NEW_HISTORICAL_INGESTION_EXECUTED = false
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
