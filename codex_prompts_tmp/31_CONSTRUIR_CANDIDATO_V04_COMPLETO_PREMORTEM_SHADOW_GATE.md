# PROMPT 31 — CONSTRUIR CANDIDATO v0.4 COMPLETO: PRE-MORTEM + IMPLEMENTACIÓN + TESTS + GATE/SPECS + SHADOW VALIDATION

## Rol

Actúa como **ejecutor técnico controlado**. Este bloque consolida en una sola rama científica todo lo necesario para que la IA Experimental pueda auditar integralmente la recuperación v0.4 antes de cualquier autorización numérica.

Este prompt **AUTORIZA ÚNICAMENTE LA CONSTRUCCIÓN DEL CANDIDATO TÉCNICO v0.4**. No autoriza ejecución numérica, Attempt05, retrieval, EV03 real, EV04 real, D1a, EVAL ni inferencia del modelo.

La prioridad es reducir ciclos sin reducir garantías: primero pre-mortem de invariantes y blast radius; después implementación; después pruebas y shadow validation exhaustiva sobre artefactos congelados; finalmente un único candidato científico auditable.

---

# 1. Repositorio y baseline obligatorio

Repositorio:

`elVladdi/gci-nandina-rag`

Trabaja exclusivamente desde:

`main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

Antes de cualquier cambio ejecuta `git fetch --all --prune` y verifica:

- `origin/main` = exactamente `ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`;
- Plan canónico = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- working tree tracked limpio;
- candidato Prompt30 rechazado sigue en `0298a6a51181ba992e981063be87a9742ba266ef`;
- autorización v0.3 permanece consumida por Attempt04 y no puede reutilizarse.

Si cualquiera falla: **STOP / FAIL_CLOSED**.

La decisión metodológica corregida ya está integrada en `main`:

`outputs/audits/0b05c_ev04_mrr_methodological_decision_v0.4/mrr_methodological_decision_v0.4.json`

Git blob esperado en el baseline:

`26b4310979e042bc7bb4fa0594d1ef450bf0032e`

Verifica el blob desde Git. No interpretes el campo interno `decision_status = CANDIDATE_PENDING_EXTERNAL_AUDIT` como estado de autorización: ese JSON fue integrado bit a bit después de auditoría externa. La evidencia de gobernanza para este bloque es **identidad Git + integración a main + este Prompt31**. El campo interno no autoriza ejecución.

---

# 2. Evidencia obligatoria a leer antes de diseñar

Lee íntegramente, como mínimo:

## 2.1 Decisión y diagnósticos

1. `outputs/audits/0b05c_ev04_mrr_methodological_decision_v0.4/mrr_methodological_decision_v0.4.json`
2. `outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json`
3. `outputs/audits/0b05c_ev04_gatec_mrr100_arithmetic_provenance_v0.3/ev04_gatec_mrr100_arithmetic_provenance_v0.3.json`
4. `outputs/audits/0b05c_attempt04_failclosed_v0.3/attempt04_failure_record_v0.3.json`

## 2.2 Artefactos frozen EV04

5. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv`
6. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_results.csv`
7. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json`
8. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json`
9. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/gate_c_microaudit_v0.2.json`
10. `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/limitation_stratified_metrics_v0.2.csv`

## 2.3 Código/contratos existentes

11. `src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py`
12. `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`
13. `src/experiments/build_bm25_corrective_0b05c_v03.py`
14. `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
15. `src/experiments/run_0b05c_corrective_numerical_v03.py`
16. `src/experiments/run_d1a_corrective_0b05c_v03.py`
17. `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`
18. `tests/test_0b05c_corrective_numerical_gate_v03.py`
19. `tests/test_0b05c_ev03_historical_builder_recovery_v02.py`

## 2.4 Gate/specs v0.3 consumidos — solo como antecedente

20. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
21. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json`
22. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json`
23. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json`
24. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_manifest_v0.3.json`
25. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_gate_hash_ledger_v0.3.json`
26. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_numerical_authorization_record_v0.3.json`

No copies ciegamente hashes o estados del reporte previo. Verifica objetos Git reales.

---

# 3. PRE-MORTEM OBLIGATORIO ANTES DE CODIFICAR

Antes de crear código, construye en memoria/working tree temporal una **matriz de invariantes y blast radius**. Si detectas una contradicción metodológica no resuelta por la decisión integrada, detente antes de crear el candidato y reporta `FAIL_CLOSED / NEW_BLOCKING_INVARIANT`.

La matriz debe cubrir al menos:

1. **MRR@100**: `.77` histórico es literal inmutable/no-oracle; expected prospectivo se deriva desde case summary por suma racional exacta y produce `.78`.
2. **MRR@200**: conserva productor legacy; `mrr_at_200`, numerador y denominador son aliases exactos de `mrr` legacy; no aplicar ratio racional como output.
3. **Contribución 101–200**: se deriva racionalmente como `S200-S100`; no resta de floats ya redondeados; literal histórico no es oracle.
4. **Metric dict completo**: definir exactamente key-set, tipos, `metric_table`, orden de filas y semántica de expected/actual; no comparar ciegamente contra el dict histórico que contiene `.77`.
5. **No drift legacy**: todos los campos legacy con productor histórico estable deben conservar identidad exacta cuando se aplican al frozen case summary.
6. **Ranking y case summary**: siguen siendo controles históricos frozen exactos; la recuperación v0.4 no los debilita.
7. **Comparator**: expected y actual deben derivarse independientemente; igualdad exacta; detectar key/schema/value drift.
8. **EV03**: comportamiento y recuperación histórica previamente resuelta deben permanecer sin cambio científico.
9. **D1a**: no retraining, no cambios de modelo/corpus/config; reutilizar componentes v0.3 si son científicamente invariantes, evitando wrappers innecesarios.
10. **19-step orchestration**: conservar orden y fail-closed semántico salvo cambios estrictamente necesarios por v0.4.
11. **Authorization boundary**: v0.4 nace UNAUTHORIZED; ninguna autorización v0.3 consumida puede reutilizarse; `Attempt05` debe seguir `NOT_AUTHORIZED / NOT_EXECUTED`.
12. **Side-effect boundary**: `preflight_authorized()` v0.4 debe fallar antes de cualquier escritura si v0.4 no está autorizado.
13. **Future roots**: todos los roots prospectivos v0.4 deben ser nuevos/no colisionar con v0.3 ni outputs históricos; ausencia debe poder verificarse antes de ejecución.
14. **Historical immutability**: no editar artefactos Gate C, outputs v0.2, v0.3, Attempt04, tests históricos ni autorización v0.3.
15. **No oracle leakage**: el productor v0.4 no puede contener hardcoded los escalares `.77`, `.78`, `.81`, `.815` ni contribuciones para forzar coincidencia. Los valores pueden aparecer en tests/audits como expectativas, no como lógica productora.
16. **No tolerance**: prohibidos `isclose`, tolerancias, redondeo de conveniencia, `nextafter` o normalización que haga tautológico PASS_EXACT.
17. **Cross-field aliases**: `mrr_at_200 == mrr`, `mrr_at_200_numerator == mrr_numerator`, `mrr_at_200_denominator == mrr_denominator` bit/tipo exactos donde aplique.
18. **Row-order sensitivity split**: MRR@100 y contribución racional deben ser matemáticamente invariantes al orden; MRR@200 legacy conserva explícitamente el orden del case summary como parte de su contrato.
19. **Schema blast radius**: revisar cualquier consumidor downstream de `metrics`, `metric_table`, summary, manifest, ledger y comparadores para impedir incompatibilidades silenciosas.
20. **Governance blast radius**: Plan, article, EXP11B y EXP12 no se tocan; 0B05C metric impact sigue `NOT_DETERMINED`.

La matriz y su resultado deben quedar persistidos en el artefacto shadow/preexecution descrito más adelante.

---

# 4. RAMA Y ALCANCE DEL CANDIDATO v0.4

Crea una nueva rama exacta desde el baseline:

`codex/0b05c-v04-complete-preexecution-candidate`

Parent científico obligatorio:

`ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

Construye **un único bundle científico coherente**. Preferencia: **1 commit científico** que contenga implementación + tests + gate/specs + shadow audit, para que la auditoría externa pueda revisar un único diff.

No modifiques ningún archivo v0.3 ni histórico. Crea archivos v0.4 nuevos.

### Paths de código esperados

Crea, si resultan necesarios tras el pre-mortem:

- `src/experiments/evaluate_normative_bm25_corrective_0b05c_v04.py`
- `src/experiments/prepare_0b05c_corrective_numerical_gate_v04.py`
- `src/experiments/run_0b05c_corrective_numerical_v04.py`

**No crees un wrapper D1a v0.4 si `run_d1a_corrective_0b05c_v03.py` puede reutilizarse sin alterar su contrato científico.** Si concluyes que un wrapper v0.4 es imprescindible, debes justificarlo en el pre-mortem y mantener cero cambios de modelo/corpus/config.

### Tests nuevos esperados

Crea como mínimo:

- `tests/test_0b05c_ev04_mrr_contract_v04.py`
- `tests/test_0b05c_corrective_numerical_gate_v04.py`

Puedes crear un tercer test solo si cubre una frontera claramente distinta y reduce riesgo real. No copies suites enteras sin necesidad.

### Gate/specs candidatos v0.4

Crea un directorio nuevo:

`outputs/audits/0b05c_corrective_numerical_gate_v0.4/`

Debe contener, como mínimo:

- `0b05c_corrective_numerical_execution_gate_v0.4.json`
- `ev03_numerical_execution_spec_v0.4.json`
- `ev04_numerical_execution_spec_v0.4.json`
- `d1a_numerical_execution_spec_v0.4.json`
- `0b05c_corrective_numerical_gate_manifest_v0.4.json`
- `0b05c_corrective_numerical_gate_hash_ledger_v0.4.json`

**NO** crees authorization record v0.4 en este bloque.

Todos esos artefactos deben estar en estado inequívocamente no autorizado. Usa estados claros equivalentes a:

- `gate_status = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED`
- `authorization_readiness = NOT_AUTHORIZED`
- D1A/EV03/EV04/UNIFIED = `NOT_AUTHORIZED`
- `attempt05 = NOT_AUTHORIZED / NOT_EXECUTED`

No uses palabras `AUTHORIZED`, `APPROVED_FOR_EXECUTION` ni equivalentes como estado positivo actual.

### Artefacto consolidado de pre-mortem/shadow

Crea:

`outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json`

Debe registrar:

- baseline y source bindings reales;
- matriz completa de 20 invariantes con `PASS/FAIL` y evidencia;
- key-set/schema esperado de métricas v0.4;
- diferencias conocidas entre métricas históricas Gate C y referencia prospectiva;
- resultados de shadow validation;
- pruebas de fail-closed;
- test commands/results;
- clasificación probatoria correcta de ejecuciones locales;
- estado final `V04_CANDIDATE = BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT` solo si todo pasa.

---

# 5. IMPLEMENTACIÓN v0.4 — CONTRATO MRR OBLIGATORIO

## 5.1 MRR@100

Implementa una función pura que, desde `case_rows`, derive `mrr_at_100` según la decisión integrada:

- fuente: `rank_ref` entero;
- contribución `Fraction(1, rank_ref)` si `1 <= rank_ref <= 100`, cero de otro modo;
- suma racional exacta;
- `N = len(case_rows)` exacto;
- una sola conversión final del numerador racional a binary64;
- una sola conversión final de la razón racional/N a binary64.

No uses acumulación float intermedia.

## 5.2 MRR@200

Conserva el productor legacy estable:

- `mrr_numerator = sum(float(row["reciprocal_rank"]) for row in case_rows)` en el orden del case summary;
- `mrr = float(mrr_numerator / N)`;
- `mrr_at_200_numerator = mrr_numerator`;
- `mrr_at_200_denominator = mrr_denominator`;
- `mrr_at_200 = mrr`.

No redefinas `mrr_at_200` usando `float(exact_rational_S200/N)`.

## 5.3 Contribución 101–200

Deriva:

- `S100` racional exacto desde `rank_ref`;
- `S200` racional exacto desde `rank_ref`;
- `C101_200 = S200 - S100` racional;
- numerador output = una sola conversión `float(C101_200)`;
- valor output = una sola conversión `float(C101_200/N)`.

No uses `mrr_at_200 - mrr_at_100` ni resta de numeradores float.

## 5.4 Canonical metrics builder

Crea una función explícita y auditable que construya el **dict completo de métricas canónicas v0.4** desde un case summary.

Requisitos:

- partir de los productores legacy estables para campos legacy;
- aplicar solo las redefiniciones prospectivas aprobadas a MRR@100 y contribución 101–200;
- `mrr_at_200` como alias legacy;
- preservar key-set, tipos y orden de `metric_table` acordados;
- ningún scalar de resultado hardcoded en lógica productora;
- expected y actual deben poder llamarse separadamente sobre frozen/reproduced case summaries;
- no usar el dict histórico enriquecido como oracle para los campos prospectivos.

Debe existir una validación interna fuerte del schema/key-set antes del compare.

---

# 6. COMPARATOR v0.4 Y SHADOW EXECUTION ESTÁTICA

El control EV04 v0.4 no debe volver a ejecutar el error de v0.3 de comparar `run_metadata["metrics"]` histórico enriquecido contra actual sin normalización metodológica.

Define el control así:

1. ranking histórico frozen vs ranking reproducido: exacto;
2. case summary histórico frozen vs reproducido: exacto;
3. `expected_metrics_v04 = canonical_metrics_v04(frozen_case_summary)`;
4. `actual_metrics_v04 = canonical_metrics_v04(reproduced_case_summary)`;
5. verificar además que **todo campo legacy estable** del expected derivado coincide exactamente con su contrato histórico frozen;
6. comparar expected vs actual por igualdad exacta del dict completo;
7. schema/key-set/metric-table order exactos;
8. sin tolerancias.

## 6.1 Shadow validation obligatoria — sin retrieval

Antes de publicar el candidato, ejecuta una shadow validation **solo con artefactos frozen versionados**. No llames a retrieval/evaluator real.

Como mínimo:

### Shadow A — derivación frozen

Carga el frozen EV04 case summary y deriva el dict canónico v0.4.

Debe verificarse:

- N = 1056;
- MRR@100 prospectivo = `0.04198129438896378` y hex `0x1.57e927ce3818cp-5`;
- MRR@100 numerator = `44.33224687474575`;
- legacy MRR/MRR@200 = `0.04334161160288281` y hex `0x1.630df28c7d779p-5`;
- MRR@200 numerator = `45.76874185264425`;
- contribution 101–200 = `0.0013603172139190346` y hex `0x1.649957c8abdbep-10`;
- contribution numerator = `1.4364949778985006`;
- `mrr_at_200 == mrr` exacto;
- numerador/denominador aliases exactos;
- todos los legacy fields restantes coinciden con frozen contract;
- no hay drift inesperado de keys/types/metric_table.

### Shadow B — independencia expected/actual

Vuelve a cargar el mismo frozen case summary por una ruta/objeto independiente y deriva `actual_shadow_metrics_v04` por segunda llamada, sin reutilizar el dict expected.

Debe cumplirse:

`expected_shadow_metrics_v04 == actual_shadow_metrics_v04`

por igualdad Python exacta del dict completo.

### Shadow C — comparator completo

Usa ranking frozen y case summary frozen como ambos lados de un control shadow y demuestra que el comparator v0.4 produce exactamente `PASS_EXACT`.

Esto no es una ejecución EV04 real porque no se construye índice ni se recupera nada; solo prueba el contrato de comparación con archivos frozen.

### Shadow D — negative controls

Demuestra fail-closed al menos para:

- `mrr_at_100` alterado 1 ULP;
- `mrr_at_200 != mrr`;
- contribution alterada 1 ULP;
- key faltante;
- key extra;
- orden/schema `metric_table` alterado;
- ranking alterado;
- case summary alterado.

Cada caso debe fallar explícitamente, no “pasar con warning”.

### Shadow E — no historical-oracle leakage

Comprueba estáticamente que el productor v0.4 no contiene como lógica de output los literales históricos/prospectivos conocidos. Puedes tenerlos en tests y artefactos de auditoría, pero no en funciones productoras.

### Shadow F — row-order semantics

Con una permutación sintética/derivada de case rows:

- MRR@100 racional debe ser idéntico;
- contribution racional debe ser idéntica;
- documenta que MRR@200 legacy **no se redefine** como row-order invariant: preserva el orden del case summary bajo su productor histórico.

No uses la permutación para alterar el control histórico real; es solo una prueba de función pura.

---

# 7. TESTS Y REGRESIÓN

Ejecuta localmente, como mínimo:

1. los tests v0.4 nuevos;
2. `tests/test_0b05c_corrective_numerical_gate_v03.py` como regresión de versión anterior;
3. `tests/test_0b05c_ev03_historical_builder_recovery_v02.py`;
4. los tests v0.1/v0.2 de gate que sean razonablemente rápidos y no ejecuten retrieval pesado;
5. cualquier test directamente afectado por imports/contratos modificados.

No es necesario ejecutar toda la suite si contiene pruebas costosas o experimentos reales; documenta exactamente qué ejecutaste y por qué.

Toda ejecución local debe clasificarse:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`

salvo que exista CI versionada real para ese commit.

No conviertas un PASS local en verificación externa.

---

# 8. GATE/SPECS v0.4 — FRESH, UNAUTHORIZED, FAIL-CLOSED

El gate v0.4 debe ser nuevo y no puede heredar autorización consumida v0.3.

Requisitos:

- bind de decisión metodológica integrada por path + Git blob + baseline commit;
- bind de código v0.4 candidato;
- bind de artefactos frozen relevantes;
- bind de D1a/model/config/corpus sin cambios;
- Attempt04 registrado solo como antecedente fail-closed;
- Attempt05 explícitamente `NOT_AUTHORIZED / NOT_EXECUTED`;
- todas las autorizaciones v0.4 = `NOT_AUTHORIZED`;
- no authorization record v0.4;
- roots v0.4 nuevos;
- no overwrite/resume silencioso;
- futuras transiciones de autorización deberán ocurrir en un bloque separado posterior a integración y auditoría externa.

El runner v0.4 debe tener una frontera inequívoca:

- inspección/preflight de candidato permitida read-only;
- ejecución numérica imposible con el gate candidato actual;
- `preflight_authorized()` debe rechazar el estado no autorizado **antes de cualquier side effect**;
- la futura ejecución, cuando exista autorización separada, debe conservar el orden formal de 19 pasos salvo justificación explícita y auditada.

Crea tests que demuestren mecánicamente el rechazo pre-side-effect.

---

# 9. FUTURE ROOTS Y AISLAMIENTO DE ATTEMPT05

No reutilices roots de Attempt04/v0.3.

Define roots nuevos y explícitos para un eventual Attempt05/v0.4. Deben permanecer ausentes después de este Prompt31, excepto los artefactos estáticos del gate/audit que sí son parte del candidato.

El shadow audit debe listar:

- todos los future roots v0.4;
- existencia antes/después del build estático;
- `runtime_output_roots_created = false`;
- `authorization_record_v0.4_present = false`;
- `attempt05_executed = false`.

---

# 10. PROHIBICIONES ABSOLUTAS

No debes:

- modificar `main`;
- integrar el candidato;
- crear autorización v0.4;
- marcar ningún componente como AUTHORIZED;
- autorizar Attempt05;
- ejecutar Attempt05;
- ejecutar retrieval;
- construir índices reales de control/correctivos;
- ejecutar EV03 real;
- ejecutar EV04 real;
- ejecutar D1a;
- ejecutar EVAL real;
- ejecutar inferencia de modelo;
- retrain;
- modificar modelo/config/corpus D1a;
- modificar archivos v0.3 existentes;
- modificar outputs históricos v0.2/Gate C;
- modificar failure record Attempt04;
- modificar candidato Prompt30 rechazado;
- modificar Plan Maestro;
- modificar article;
- tocar EXP11B o EXP12;
- introducir tolerancias, `isclose`, redondeo de conveniencia, `nextafter`, hardcoding de escalares output o bypass de comparator;
- crear outputs numéricos correctivos que puedan confundirse con resultados de Attempt05.

Si un test requiere archivos temporales, usa un tempdir fuera de paths científicos futuros y elimínalo al terminar.

---

# 11. VALIDACIÓN GIT FINAL DEL CANDIDATO

Antes de publicar verifica:

- branch exacta `codex/0b05c-v04-complete-preexecution-candidate`;
- parent/merge-base exacto `ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`;
- `main` sigue exactamente en el baseline;
- Plan/article intactos;
- Prompt30 rechazado intacto;
- no archivos v0.3/históricos modificados;
- solo paths nuevos v0.4 y artefactos preexecution/shadow autorizados por este prompt;
- no authorization record v0.4;
- no runtime outputs;
- working tree tracked limpio;
- push normal de la rama candidata, sin force/rebase/amend del historial protegido.

Si necesitaste más de 1 commit científico, justifica por qué. Preferencia fuerte: 1 commit coherente.

Estado máximo permitido:

```text
V04_CANDIDATE = BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
V04_GATE = DEFINED / UNAUTHORIZED
V04_AUTHORIZATION = NOT_CREATED
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

---

# 12. REPORTE FINAL OBLIGATORIO

Tu respuesta debe incluir, de forma compacta pero completa:

1. baseline y refs protegidas;
2. resultado del pre-mortem de 20 invariantes;
3. branch/commit/tree/parent/compare del candidato;
4. lista exacta de changed paths con Git blob SHA-1;
5. arquitectura de implementación v0.4 y qué componentes v0.3 se reutilizan;
6. definición exacta del canonical metrics dict v0.4;
7. shadow A–F con resultados;
8. negative controls y fail-closed;
9. gate/spec states y future roots;
10. comandos de tests locales y resultados, clasificados correctamente como CODEX-local;
11. confirmación de no retrieval/no numerical execution/no Attempt05;
12. estado científico final.

Si algo no pasa exactamente, reporta `FAIL_CLOSED` y no presentes el candidato como ready.

---

# 13. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Después de terminar el trabajo científico candidato, vuelve a:

`codex/prompts-temporary`

Haz `git fetch` antes de persistir la respuesta. No rebase, no amend, no force-push.

Crea exclusivamente:

`codex_prompts_tmp/31_RESPUESTA_CONSTRUIR_CANDIDATO_V04_COMPLETO_PREMORTEM_SHADOW_GATE.md`

El commit administrativo debe modificar únicamente ese archivo de respuesta.

No mezcles el historial administrativo con `main` ni con la rama científica.
