# PROMPT 30A — CORRECCIÓN DE DECISIÓN METODOLÓGICA MRR v0.4: PRESERVAR CONTRATO LEGACY MRR@200

## Rol

Actúa como **ejecutor técnico controlado**. Este bloque corrige exclusivamente el candidato metodológico generado por Prompt30 después de una auditoría externa independiente.

**No integres a `main`. No construyas código v0.4. No autorices Attempt05.**

La ejecución de Prompt30 fue Git-correcta, pero la auditoría externa detectó un **hallazgo metodológico bloqueante** en el contrato definido: la regla racional aplicada indiscriminadamente a todo cutoff `K` cambia prospectivamente `MRR@200` de `0.04334161160288281` a `0.043341611602882815`, aunque el MRR@200 legacy sí tiene un productor histórico estable y Gate C declara que `mrr` legacy equivale a `mrr_at_200`.

La corrección debe preservar el objetivo original de hacer MRR@100 reproducible sin introducir drift colateral en MRR@200.

---

## 1. Repositorio y baseline científico obligatorio

Repositorio:

`elVladdi/gci-nandina-rag`

Trabaja exclusivamente desde:

`main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`

Verifica antes de cualquier cambio:

- `origin/main` = exactamente `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`;
- Plan canónico = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- working tree tracked limpio.

Si cualquiera falla: **STOP / FAIL_CLOSED**.

El candidato Prompt30 rechazado permanece solo como evidencia de auditoría:

- branch: `codex/0b05c-ev04-mrr100-methodological-decision-v04`
- commit: `0298a6a51181ba992e981063be87a9742ba266ef`
- artifact blob: `60a146e101c77f9c9ffaa679cec5b6eeca94c36c`

**No modifiques, rebasees, amendes ni fuerces esa rama.**

---

## 2. Evidencia obligatoria a leer read-only

Lee íntegramente, sin retrieval ni evaluación real:

Desde `main`:

1. `outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json`
2. `outputs/audits/0b05c_ev04_gatec_mrr100_arithmetic_provenance_v0.3/ev04_gatec_mrr100_arithmetic_provenance_v0.3.json`
3. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv`
4. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json`
5. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json`
6. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/gate_c_microaudit_v0.2.json`
7. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/limitation_stratified_metrics_v0.2.csv`
8. histórico Gate C `ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97`: `tests/test_normative_bm25_hierarchical_v02.py`
9. runner histórico `ce239059d748a4baf8a2113df5398f50c0e14a58`: `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`
10. productor v0.3 actual: `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`
11. candidato rechazado Prompt30 en commit `0298a6a51181ba992e981063be87a9742ba266ef`: `outputs/audits/0b05c_ev04_mrr100_methodological_decision_v0.4/mrr100_methodological_decision_v0.4.json`

Verifica Git blob SHA-1 reales. No copies ciegamente valores del reporte Prompt30.

---

# 3. Hallazgo externo obligatorio que debes corregir

El histórico congelado registra simultáneamente:

```text
legacy mrr = 0.04334161160288281
legacy mrr_numerator = 45.76874185264425
mrr_at_200 = 0.04334161160288281
mrr_at_200_numerator = 45.76874185264425
```

El `mrr_definition` histórico declara que el campo legacy `mrr` **es MRR@200** por depth 200.

Además, el runner histórico versionado contiene un productor estable:

```python
numerator = sum(float(row["reciprocal_rank"]) for row in case_rows)
value = float(numerator / denominator)
```

El candidato Prompt30, en cambio, define para cada `K` una razón racional exacta y una única conversión final. Aplicada a K=200 produce:

```text
0.043341611602882815
```

que está a 1 ULP del histórico `0.04334161160288281`.

Por tanto, el candidato Prompt30 crea una contradicción potencial:

- dice preservar métricas legacy con productor estable;
- pero su regla general para enriched `mrr_at_200` cambia el valor respecto del legacy `mrr` al que debe equivaler.

**Esta contradicción debe desaparecer por completo en el candidato corregido.**

---

# 4. Decisión metodológica corregida obligatoria

## 4.1 MRR@100

Mantén la decisión ya auditada:

```text
historical mrr_at_100 = 0.04198129438896377
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
```

Referencia prospectiva:

```text
mrr_at_100_numerator_binary64 = 44.33224687474575
mrr_at_100_binary64 = 0.04198129438896378
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
```

Para MRR@100:

- fuente = `rank_ref` entero;
- contribución exacta por caso = `1/rank_ref` si `1 <= rank_ref <= 100`, cero si no;
- suma racional exacta;
- N exacto;
- una conversión final a binary64 del numerador racional;
- una conversión final a binary64 de la razón racional/N;
- sin tolerancias, round, nextafter ni hardcoding.

No se reclama historical provenance para `.78`.

## 4.2 MRR@200 / legacy `mrr`

**No aplicar la conversión de la razón racional exacta como output canónico de `mrr_at_200`.**

Debe preservarse el contrato histórico estable de legacy `mrr`:

```text
MRR200_ROLE = STABLE_LEGACY_CONTRACT / ENRICHED_ALIAS_OF_LEGACY_MRR
```

Contrato prospectivo obligatorio para este campo:

1. El productor base legacy conserva la semántica histórica versionada:
   - `sum(float(reciprocal_rank) for row in case_rows)` en el orden del case summary;
   - `float(numerator / N)`.
2. `mrr_at_200_numerator` debe ser alias bit-exacto de `mrr_numerator`.
3. `mrr_at_200_denominator` debe ser alias de `mrr_denominator`.
4. `mrr_at_200` debe ser alias bit-exacto de `mrr`.
5. En el frozen control válido:
   - numerator = `45.76874185264425`;
   - value = `0.04334161160288281`.
6. Está prohibido redefinir `mrr_at_200` como `float(exact_rational_S200/N)` porque eso produciría `.815` y rompería la equivalencia histórica `mrr == mrr_at_200`.

El exact-rational `S200` puede calcularse internamente **solo para definir de forma reproducible la contribución 101–200**, pero no reemplaza el output legacy MRR@200.

## 4.3 Contribución 101–200

Los campos históricos de contribución fueron añadidos en Gate C sin un productor versionado que fije su ruta bit-exacta. Presérvalos como literales históricos, pero no como oracle prospectivo:

```text
historical mrr_101_200_contribution_numerator = 1.436494977898505
historical mrr_101_200_contribution = 0.0013603172139190387
HISTORICAL_101_200_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
```

Para v0.4 define prospectivamente:

- `S100` = suma racional exacta hasta 100;
- `S200` = suma racional exacta hasta 200;
- `C101_200 = S200 - S100` racional exacto;
- `contribution_numerator_binary64 = float(C101_200)` con una única conversión final;
- `contribution_binary64 = float(C101_200 / N)` con una única conversión final;
- prohibido calcular estos campos restando `mrr_at_200` y `mrr_at_100` ya redondeados.

Como control read-only esperado desde el case summary congelado, la regla debe producir:

```text
prospective contribution numerator = 1.4364949778985006
prospective contribution numerator hex = 0x1.6fbe2286f13acp+0
prospective contribution = 0.0013603172139190346
prospective contribution hex = 0x1.649957c8abdbep-10
```

Estos valores deben ser **recomputados** desde los casos; no deben copiarse como escalares de output dentro de ningún futuro productor.

## 4.4 Consistencia semántica obligatoria

El candidato corregido debe declarar expresamente:

```text
mrr_at_200_equals_legacy_mrr_required = true
mrr_at_200_rational_ratio_redefinition_forbidden = true
mrr_at_100_uses_prospective_exact_rational_rule = true
contribution_101_200_uses_prospective_exact_rational_rule = true
```

No debe quedar ninguna afirmación genérica tipo “para cada cutoff K convertir exact-rational/N a binary64” que alcance a `mrr_at_200` output y contradiga el contrato legacy.

---

# 5. PASS_EXACT corregido

`PASS_EXACT` sigue obligatorio y sin tolerancias.

Para un futuro control v0.4:

1. ranking histórico vs reproducido = exacto;
2. case summary histórico vs reproducido = exacto;
3. métricas legacy con productor histórico estable = contrato histórico exacto;
4. `mrr_at_200` = alias exacto de legacy `mrr`;
5. `mrr_at_100` expected y actual = derivados independientemente de frozen/reproduced case summary con la regla racional MRR@100;
6. contribución 101–200 expected y actual = derivada independientemente con diferencia racional exacta y división racional exacta;
7. igualdad expected/actual = exacta;
8. `.77` histórico y contribution histórica no son oracles prospectivos;
9. no se elimina ninguna comprobación para permitir Attempt05.

---

# 6. Comprobaciones read-only permitidas

Puedes realizar únicamente cálculos puros sobre el case summary congelado para verificar la decisión.

Debes comprobar, como mínimo:

- MRR@100 prospectivo = `.78` y hex esperado;
- legacy MRR@200 bajo el productor histórico = `.81` y hex `0x1.630df28c7d779p-5`;
- exact-rational ratio MRR@200 = `.815` y hex `0x1.630df28c7d77ap-5` **solo como control negativo**, confirmando que está a 1 ULP y que no será usado como output `mrr_at_200`;
- contribución racional prospectiva normalizada = `0.0013603172139190346`, hex `0x1.649957c8abdbep-10`;
- diferencia ULP entre legacy MRR@200 y rational-ratio MRR@200 = `1`.

Clasifica cualquier cálculo como:

`CODEX_LOCAL_PURE_READ_ONLY_COMPUTATION`

salvo evidencia CI versionada real.

No ejecutes retrieval ni evaluator real.

---

# 7. Nuevo candidato científico limpio

Crea **una nueva rama desde el baseline `main`**, sin heredar el commit rechazado:

`codex/0b05c-ev04-mrr-methodological-decision-v04-corrected`

Crea exactamente **1 commit científico** y exactamente **1 path nuevo**:

`outputs/audits/0b05c_ev04_mrr_methodological_decision_v0.4/mrr_methodological_decision_v0.4.json`

Contenido mínimo:

```text
artifact_id = 0b05c_ev04_mrr_methodological_decision_v0.4
schema_version = 1
baseline_commit = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
decision_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
corrects_rejected_candidate_commit = 0298a6a51181ba992e981063be87a9742ba266ef
external_audit_finding = MRR200_CONTRACT_COLLATERAL_DRIFT
historical_arithmetic_path_mrr100 = NOT_RECOVERED
v04_build_authorized = false
attempt05_authorized = false
metric_impact = NOT_DETERMINED
closure = NOT_AUTHORIZED
```

Debe contener secciones estructuradas para:

- `mrr_at_100_decision`;
- `mrr_at_200_legacy_contract`;
- `contribution_101_200_decision`;
- `pass_exact_contract`;
- `source_bindings`;
- `read_only_checks`;
- `governance`;
- `scientific_state`.

Incluye `repr` y `float.hex()` para los valores históricos y prospectivos relevantes.

No hardcodees esos valores en código productor: este bloque no crea código.

---

# 8. Git contract

Antes de finalizar verifica:

- nueva branch exacta indicada;
- parent exacto = `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`;
- merge-base exacto = baseline;
- 1 ahead / 0 behind;
- exactamente 1 commit;
- exactamente 1 changed path;
- el único path es el JSON corregido;
- `main` sigue en baseline;
- branch Prompt30 rechazada sigue intacta en `0298a6a...`;
- Plan y article intactos;
- push normal, sin force/rebase/amend.

---

# 9. Prohibiciones absolutas

No debes:

- integrar a `main`;
- modificar el candidato rechazado Prompt30;
- construir v0.4;
- crear gate/specs v0.4;
- crear autorización v0.4;
- autorizar o ejecutar Attempt05;
- modificar productor v0.3;
- modificar tests históricos;
- modificar artefactos históricos;
- ejecutar retrieval;
- ejecutar EV03/EV04 real;
- ejecutar D1a;
- ejecutar EVAL real;
- ejecutar modelo;
- tocar Plan, article, EXP11B o EXP12;
- introducir tolerancias, round, nextafter o hardcoding en código.

---

# 10. Persistencia administrativa

Al terminar, vuelve a:

`codex/prompts-temporary`

Haz fetch. No rebase, amend ni force.

Crea exclusivamente:

`codex_prompts_tmp/30A_RESPUESTA_CORREGIR_DECISION_METODOLOGICA_MRR_V04_CONTRATO_MRR200.md`

El reporte debe incluir:

1. baseline y refs;
2. verificación del hallazgo MRR@200;
3. resultado de los cálculos read-only, claramente CODEX-local;
4. branch/commit/tree/parent del candidato corregido;
5. compare exacto;
6. path/blob del nuevo artefacto;
7. source bindings;
8. prohibiciones;
9. estado científico final.

El commit administrativo debe modificar exclusivamente el archivo de respuesta.

## Estado final máximo permitido

```text
GROUP_2 = EN_CURSO
PROMPT30_CANDIDATE = REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED
PROMPT30_BLOCKING_FINDING = MRR200_CONTRACT_COLLATERAL_DRIFT
CORRECTED_METHODOLOGICAL_DECISION_CANDIDATE = BUILT / PENDING_EXTERNAL_AUDIT
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
MRR200_ROLE = STABLE_LEGACY_CONTRACT / ENRICHED_ALIAS_OF_LEGACY_MRR
V04_BUILD = NOT_AUTHORIZED / NOT_BUILT
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```
