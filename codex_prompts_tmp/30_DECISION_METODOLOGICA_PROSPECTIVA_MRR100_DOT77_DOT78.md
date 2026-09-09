# PROMPT 30 — DECISIÓN METODOLÓGICA PROSPECTIVA MRR@100 (`.77` vs `.78`)

## Rol

Actúa como **ejecutor técnico controlado**. No debes decidir por intuición ni reinterpretar la evidencia. La decisión metodológica ya ha sido fijada externamente por la IA Experimental y este bloque debe **materializarla como artefacto científico candidato**, sin construir todavía v0.4 y sin autorizar Attempt05.

## Repositorio

`elVladdi/gci-nandina-rag`

## Baseline científico obligatorio

Trabaja exclusivamente desde:

`main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`

Verifica antes de cualquier cambio:

- `origin/main` debe ser exactamente el mismo SHA;
- Plan canónico: `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article: `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- working tree tracked limpio.

Si cualquiera de estas condiciones falla: **STOP / FAIL_CLOSED**.

## Evidencia que debes leer íntegramente antes de construir el candidato

Desde `main`:

1. `outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json`
2. `outputs/audits/0b05c_ev04_gatec_mrr100_arithmetic_provenance_v0.3/ev04_gatec_mrr100_arithmetic_provenance_v0.3.json`
3. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json`
4. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json`
5. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv`
6. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/gate_c_microaudit_v0.2.json`
7. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/limitation_stratified_metrics_v0.2.csv`
8. test histórico Gate C en commit `ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97`:
   `tests/test_normative_bm25_hierarchical_v02.py`
9. runner histórico en commit `ce239059d748a4baf8a2113df5398f50c0e14a58`:
   `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`
10. productor correctivo v0.3 actual:
   `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`

No ejecutes retrieval ni evaluación real para leer estas fuentes.

---

# 1. Decisión metodológica externa obligatoria

Debes registrar exactamente esta decisión, sin sustituirla por otra:

## 1.1 Tratamiento del `.77` histórico

El valor Gate C:

- `mrr_at_100_numerator = 44.33224687474574`
- `mrr_at_100 = 0.04198129438896377`

queda **preservado de forma inmutable como literal histórico reportado por Gate C**, pero **NO** será usado como oracle computacional prospectivo para v0.4 porque su ruta aritmética histórica bit-exacta no pudo recuperarse desde la evidencia versionada.

Estado conceptual obligatorio:

`DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE`

No edites ni normalices retrospectivamente ningún artefacto histórico.

## 1.2 Referencia prospectiva

Para v0.4, la referencia prospectiva MRR@K debe ser **case-derived y determinista**, no copiada de escalares históricos.

La referencia prospectiva MRR@100 corresponde al valor case-derived reproducible que en la evidencia auditada se representa como:

- numerator binary64: `44.33224687474575`
- MRR@100 binary64: `0.04198129438896378`

Estado conceptual obligatorio:

`DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE`

Esta selección **no declara que `.78` haya sido el valor histórico “verdadero” de Gate C**. Solo define la referencia computacional prospectiva porque la provenance de `.77` no es recuperable y `.78` deriva del caso congelado bajo una regla reproducible.

## 1.3 Regla canónica prospectiva

La regla metodológica v0.4 debe quedar definida así:

Para cada cutoff `K`:

1. fuente de contribuciones: `rank_ref` entero del case summary;
2. contribución por caso:
   - `1 / rank_ref` si `1 <= rank_ref <= K`;
   - `0` en otro caso;
3. acumulación: suma **racional exacta**, conceptualmente `Fraction(1, rank_ref)`, sin acumulación float intermedia;
4. el orden de filas no debe afectar el resultado matemático;
5. denominador: número exacto de casos (`N`);
6. `numerator_binary64`: una sola conversión final del numerador racional exacto a IEEE-754 binary64;
7. `mrr_binary64`: una sola conversión final de la razón exacta `numerator_rational / N` a IEEE-754 binary64;
8. contribución 101–200: calcular primero racionalmente `S_200 - S_100` y convertir una sola vez; **prohibido derivarla restando dos floats ya redondeados**;
9. no tolerancias;
10. no redondeo decimal de conveniencia;
11. no `nextafter`;
12. no escalars hardcodeados dentro del productor;
13. no corrección manual para “hacer coincidir” `.77` o `.78`.

La implementación futura podrá usar `fractions.Fraction` u otra representación racional exacta equivalente, pero el contrato científico es la regla anterior, no una librería concreta.

## 1.4 PASS_EXACT prospectivo

`PASS_EXACT` se mantiene y **no se debilita**.

Para un futuro control v0.4:

- ranking reproducido debe seguir siendo exacto frente al ranking histórico congelado;
- case summary reproducido debe seguir siendo exacto frente al case summary histórico congelado;
- métricas legacy que tengan productor histórico estable deben conservar su contrato correspondiente;
- los campos enriquecidos MRR@100/MRR@200 y contribución 101–200 deben generarse **determinísticamente con la regla canónica prospectiva**, tanto desde el case summary histórico congelado (expected) como desde el case summary reproducido (actual), y compararse por igualdad exacta;
- el literal histórico `.77` permanece evidencia histórica, no expected computacional del nuevo contrato.

Esto no autoriza a eliminar comprobaciones ni a introducir tolerancias.

---

# 2. Artefacto científico candidato

Crea una rama nueva exacta:

`codex/0b05c-ev04-mrr100-methodological-decision-v04`

partiendo exclusivamente de `main = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`.

Debes crear **exactamente un commit científico** y **exactamente un path nuevo**:

`outputs/audits/0b05c_ev04_mrr100_methodological_decision_v0.4/mrr100_methodological_decision_v0.4.json`

No modifiques ningún otro archivo.

## 2.1 Contenido mínimo obligatorio del JSON

Debe incluir como mínimo:

```text
artifact_id = 0b05c_ev04_mrr100_methodological_decision_v0.4
schema_version = 1
baseline_commit = ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6
decision_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
methodological_decision = ADOPT_CASE_DERIVED_DOT78_AS_PROSPECTIVE_REFERENCE_PRESERVE_DOT77_AS_HISTORICAL_LITERAL
historical_arithmetic_path = NOT_RECOVERED
v04_build_authorized = false
attempt05_authorized = false
metric_impact = NOT_DETERMINED
closure = NOT_AUTHORIZED
```

Debe registrar además:

### A. `historical_literal`

- `.77` y su numerador;
- `float.hex()` de ambos;
- rol exacto: `IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE`;
- provenance: `NOT_RECOVERED`.

### B. `prospective_reference`

- `.78` y su numerador;
- `float.hex()` de ambos;
- rol exacto: `PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE`;
- aclaración expresa de que no se afirma historical provenance para `.78`.

### C. `canonical_reducer_contract`

Representa íntegramente los 13 puntos de la regla canónica prospectiva indicados arriba.

Debe incluir expresamente:

- exact rational accumulation;
- integer `rank_ref` source;
- cutoff semantics;
- exact N;
- one final binary64 conversion;
- rational 101–200 contribution;
- row-order mathematical invariance;
- no tolerance;
- no decimal convenience rounding;
- no nextafter;
- no hardcoded output scalars.

### D. `pass_exact_contract`

Debe dejar explícito que:

- `PASS_EXACT` continúa obligatorio;
- ranking y case summary históricos permanecen frozen controls;
- los enriched MRR expected/actual se derivarán independientemente de frozen/reproduced case summaries bajo la misma regla canónica;
- `.77` no será usado como expected computacional prospectivo;
- no se debilita ningún control para permitir Attempt05.

### E. `source_bindings`

Registra path, ref y Git blob SHA-1 real para al menos:

- diagnosis Attempt04;
- arithmetic provenance Prompt28;
- frozen case summary;
- frozen run metadata;
- frozen metrics artifact;
- Gate C microaudit;
- limitation stratified metrics;
- historical Gate C test;
- historical hierarchical runner;
- current v0.3 producer.

Debes verificar los blobs desde Git; no copies ciegamente los hashes del reporte previo.

### F. `governance`

Debe contener:

```text
historical_artifacts_mutated = false
v03_artifacts_mutated = false
v04_code_built = false
v04_gate_built = false
v04_authorization_created = false
attempt05_authorized = false
attempt05_executed = false
retrieval_executed = false
ev03_executed = false
ev04_real_executed = false
d1a_executed = false
eval_real_executed = false
model_inference_executed = false
canonical_plan_modified = false
article_modified = false
exp11b_or_exp12_touched = false
```

---

# 3. Comprobación aritmética permitida y limitada

Puedes realizar **únicamente una comprobación read-only** de que la regla racional prospectiva aplicada al case summary congelado produce los valores prospectivos declarados.

Si la realizas:

- usa solamente el case summary congelado;
- no ejecutes retrieval;
- no llames al evaluator real;
- no generes índices;
- registra numerador racional exacto, denominador racional exacto, `repr` y `float.hex()` del resultado binary64;
- clasifica esta comprobación como `CODEX_LOCAL_PURE_READ_ONLY_COMPUTATION` salvo que exista CI versionada que la ejecute.

Si la regla racional **no** produce los valores `.78` declarados, **STOP / FAIL_CLOSED** y no construyas el candidato.

---

# 4. Prohibiciones absolutas

No debes:

- modificar `main`;
- integrar el candidato;
- construir v0.4;
- modificar el productor v0.3;
- editar tests existentes;
- editar Gate C histórico;
- editar gate/specs/authorization/failure record v0.3;
- crear una autorización v0.4;
- autorizar Attempt05;
- ejecutar Attempt05;
- ejecutar retrieval;
- ejecutar EV03 o EV04 real;
- ejecutar D1a;
- ejecutar EVAL real;
- ejecutar inferencia del modelo;
- tocar Plan Maestro;
- tocar article;
- tocar EXP11B o EXP12;
- introducir tolerancias, redondeo de conveniencia, `nextafter` o hardcoding de `.77/.78` dentro de código productor.

---

# 5. Validación Git del candidato

Antes de finalizar verifica:

- branch exacta: `codex/0b05c-ev04-mrr100-methodological-decision-v04`;
- parent exacto: `ecb34a8372b4f8f91f0dc2e8329bf68ecb1f1fc6`;
- exactamente `1` commit ahead y `0` behind respecto al baseline;
- merge-base exacto = baseline;
- exactamente `1` changed path;
- ese path es únicamente el JSON de decisión;
- `main` sigue exactamente en el baseline;
- Plan y article no cambian;
- working tree tracked limpio;
- push normal de la rama candidata, sin force.

No declares la decisión **integrada**. El estado máximo permitido del candidato es:

`METHODOLOGICAL_DECISION_CANDIDATE = BUILT / PENDING_EXTERNAL_AUDIT`

Y debe mantenerse:

`V04_BUILD = NOT_AUTHORIZED / NOT_BUILT`

`ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED`

---

# 6. Persistencia administrativa obligatoria

Después de terminar el trabajo científico candidato, vuelve a la rama:

`codex/prompts-temporary`

Haz `git fetch` antes de persistir la respuesta. No rebase, no amend, no force-push.

Crea exclusivamente:

`codex_prompts_tmp/30_RESPUESTA_DECISION_METODOLOGICA_PROSPECTIVA_MRR100_DOT77_DOT78.md`

La respuesta debe contener:

1. baseline exacto;
2. branch/commit/tree/parent candidatos;
3. compare base→candidate;
4. path y blob SHA-1 del artefacto;
5. resumen exacto de la decisión `.77`/`.78`;
6. resultado de la comprobación racional read-only, si fue ejecutada, claramente marcada como CODEX-local;
7. source bindings reales;
8. confirmación de prohibiciones;
9. estado científico final.

El commit administrativo debe modificar exclusivamente ese archivo de respuesta.

## Estado final esperado

```text
GROUP_2 = EN_CURSO
0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED
0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04
EV04_GATEC_MRR100_ARITHMETIC_PROVENANCE_AUDIT = VERSIONED / INTEGRATED
METHODOLOGICAL_DECISION_CANDIDATE = BUILT / PENDING_EXTERNAL_AUDIT
DOT77_ROLE = IMMUTABLE_HISTORICAL_REPORTED_LITERAL / NOT_PROSPECTIVE_COMPUTATIONAL_ORACLE
DOT78_ROLE = PROSPECTIVE_CANONICAL_CASE_DERIVED_REFERENCE
V04_BUILD = NOT_AUTHORIZED / NOT_BUILT
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```
