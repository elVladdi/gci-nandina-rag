# Prompt28 — Microauditoría aritmética MRR@100 de Gate C / EV04 antes de diseñar v0.4

## 0. Rol y objetivo único

Actúa exclusivamente como **ejecutor forense de una microauditoría aritmética read-only** del MRR@100 histórico de EXP-04 Gate C / EV04.

El objetivo es determinar, con evidencia versionada y reproducción numérica pura, si puede recuperarse el **reductor/acumulador aritmético exacto** que produjo el valor congelado:

- `mrr_at_100_numerator = 44.33224687474574`
- `mrr_at_100 = 0.04198129438896377`

sin ejecutar retrieval, sin reconstruir índices, sin ejecutar EV03/EV04 real, sin ejecutar D1a, sin inferencia del modelo y sin construir todavía v0.4.

Esta microauditoría es necesaria porque el diagnóstico ya integrado de Attempt04 aisló:

`FLOAT_ACCUMULATION_PATH_MISMATCH`

y mostró que el productor v0.3 obtiene:

- `44.33224687474575`
- `0.04198129438896378`

mientras MRR@200 sí es bit-exacto.

No debes convertir una coincidencia numérica accidental en prueba de procedencia histórica.

---

## 1. Baseline Git obligatorio

Trabaja desde el repositorio:

`elVladdi/gci-nandina-rag`

La rama científica base debe ser exactamente:

`main = 6187ca29357c42c43675fb8e5ffdacbb4705ee83`

Crea una rama científica nueva, por ejemplo:

`codex/0b05c-ev04-mrr100-arithmetic-provenance-v03`

El candidato científico debe tener como padre directo exactamente `6187ca29357c42c43675fb8e5ffdacbb4705ee83`.

Antes de cualquier análisis verifica además:

- Plan canónico: `docs/plan-maestro-temporal-2026-08-31 = fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Artículo: `article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`
- Attempt05 sigue `NOT_AUTHORIZED / NOT_EXECUTED`.

Si `main` no coincide exactamente, **detente fail-closed** y no produzcas candidato científico.

---

## 2. Fuentes científicas congeladas que debes verificar

Verifica por Git blob SHA1, no solo por nombre de archivo.

### Diagnóstico ya integrado de Attempt04

`outputs/audits/0b05c_ev04_attempt04_static_diagnosis_v0.3/ev04_metric_mismatch_diagnosis_v0.3.json`

Blob esperado:

`fca5712c615960b41cb2741c2164f19fc00df9dd`

Debe mantener:

- `root_cause_class = FLOAT_ACCUMULATION_PATH_MISMATCH`
- 6 mismatches exactos
- MRR@200 bit-exacto
- Attempt05 no autorizado.

### Fuentes congeladas EV04

`outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/run_metadata.json`

Blob esperado:

`3cbbabd9d9446958e5a0b386f13bd32aec817fa1`

`outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_case_summary.csv`

Blob esperado:

`5421bf1bf2082e2ba66ce045f804f1d02b77fd58`

`outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json`

Blob esperado:

`bc3b34cae7d8832426e6b2b56cb3d2d1541cdd57`

### Gate C histórico

Commit de microcierre:

`ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97`

Padre:

`13d317630bbe59e91bc1058800d4593ba6ace66a`

Commit de outputs iniciales:

`001580944b417e81634dd6d11a9d2facc9ed29be`

Commit del runner histórico recreado:

`ce239059d748a4baf8a2113df5398f50c0e14a58`

Artefacto Gate C:

`outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/gate_c_microaudit_v0.2.json`

Blob esperado actual:

`098bc50f382a54c9dca7025d0e2d4364ac27ad3b`

Artefacto estratificado:

`outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/limitation_stratified_metrics_v0.2.csv`

Blob esperado:

`3e13cd52e8fac58bf4452c1c83a1fb11e233508b`

Test histórico exactamente en el commit Gate C:

`tests/test_normative_bm25_hierarchical_v02.py@ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97`

Blob esperado:

`1d3e45c19b29ce7f1a38a4721f01b7e70d270e3c`

Verifica expresamente que ese test reconstruía `reciprocal_sum_100` con Python `sum(...)` pero lo comparaba mediante `assertAlmostEqual`, no mediante igualdad bit-exacta.

### Productor v0.3 actual

`src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`

Blob esperado:

`3fb1346dcee357d7b1d2d430e3ca98c0bba1d1a0`

No lo modifiques.

---

## 3. Hecho histórico que debes tratar como señal de auditoría, no como conclusión

Existe una discrepancia interna versionada de 1 ULP:

- Gate C / metrics congelados: `mrr_at_100 = 0.04198129438896377`
- `limitation_stratified_metrics_v0.2.csv`, filas `parent_hs4_present` y `not_both_parents_missing` con N=1056: `0.04198129438896378`

Debes documentar esta coexistencia explícitamente.

No presupongas que una de ellas es “correcta” y la otra “incorrecta”. El objetivo es recuperar la ruta aritmética y su procedencia, no normalizar retrospectivamente los resultados.

---

## 4. Microauditoría numérica obligatoria

Usa exclusivamente los artefactos congelados y cálculos puros en memoria.

No ejecutes el runner de evaluación ni ningún retrieval.

N debe ser exactamente 1056.

### 4.1 Dos fuentes de contribución por caso

Evalúa por separado:

1. `1.0 / rank_ref` para `1 <= rank_ref <= 100`;
2. `float(reciprocal_rank)` del CSV, enmascarado por `1 <= rank_ref <= 100`.

Para MRR@200 repite con `<= 200` como control.

### 4.2 Reductores/acumuladores históricamente plausibles

Como mínimo prueba, sin redondear ni introducir tolerancias:

- Python built-in `sum`;
- `math.fsum`;
- `numpy.sum` sobre `float64`;
- `numpy.add.reduce` sobre `float64`;
- `numpy.mean` cuando sea semánticamente equivalente a MRR sobre el vector completo con ceros fuera de cutoff;
- `pandas.Series.sum`;
- `pandas.Series.mean` cuando sea semánticamente equivalente;
- cualquier ruta adicional que esté directamente sugerida por código, tests, artefactos o diff del commit Gate C.

Debes distinguir al menos:

- suma de solo contribuciones no cero y división por 1056;
- vector completo de 1056 contribuciones con cero fuera del cutoff;
- fuente `rank_ref` frente a fuente `reciprocal_rank`.

No pruebes permutaciones arbitrarias ni búsquedas combinatorias de orden para “encontrar” el bit esperado. Solo órdenes que estén documentados o naturalmente inducidos por el CSV/versionado.

### 4.3 Para cada ruta registra

- nombre exacto de la ruta;
- librería y versión ejecutada;
- fuente de contribuciones;
- longitud del vector reducido;
- orden utilizado;
- `repr()` del numerador;
- `float.hex()` del numerador;
- `repr()` del valor /1056;
- `float.hex()` del valor;
- igualdad Python con frozen;
- distancia ULP a frozen;
- delta absoluto.

Hazlo para MRR@100 y MRR@200.

### 4.4 Entorno histórico documentado

El `run_metadata.json` congela:

- Python `3.12.13`
- NumPy `2.3.5`
- pandas `3.0.1`
- Windows 11

Registra el entorno real de la microauditoría.

Si no coincide exactamente con el histórico, no afirmes que una coincidencia de un reductor demuestra por sí sola que ese reductor fue el utilizado históricamente.

No instales paquetes desde Internet ni alteres el entorno para forzar coincidencias.

---

## 5. Arqueología Git/provenance obligatoria

Inspecciona read-only:

- diff completo de `ef9faefbe9ddc0262e6e2e2f5b34feb915a69f97` contra su padre;
- test histórico en ese commit;
- `gate_c_microaudit_v0.2.json`;
- `gate_c_microaudit_v0.2.md`;
- `run_metadata.json`;
- `normative_hierarchical_metrics.json`;
- `limitation_stratified_metrics_v0.2.csv`;
- cualquier fuente versionada que el propio commit Gate C cite como origen del MRR.

Busca evidencia positiva de **cómo** se calculó el valor `.77`, no solo evidencia de que el literal fue escrito en los artefactos.

Debes separar estrictamente:

1. `NUMERIC_MATCH`: una ruta produce los mismos bits;
2. `HISTORICAL_PROVENANCE`: existe evidencia versionada de que esa ruta fue realmente la usada para Gate C.

Una ruta que coincida numéricamente pero carezca de provenance no puede clasificarse como ruta histórica recuperada.

---

## 6. Clasificación causal final obligatoria

Usa exactamente una de estas clases:

### A. `HISTORICAL_ARITHMETIC_PATH_RECOVERED`

Solo si:

- una ruta determinística reproduce bit-exacto MRR@100 congelado;
- MRR@200 se conserva bit-exacto;
- existe evidencia versionada suficiente que vincula esa ruta con Gate C histórico.

### B. `MATCHING_REDUCER_FOUND_BUT_HISTORICAL_PROVENANCE_UNPROVEN`

Si una o más rutas reproducen los bits congelados pero no existe evidencia suficiente de que fueran la ruta histórica real.

### C. `HISTORICAL_ARITHMETIC_PATH_NOT_RECOVERED`

Si ninguna ruta históricamente plausible reproduce bit-exacto el frozen MRR@100.

No inventes una cuarta categoría.

---

## 7. Readiness para v0.4

El artefacto debe incluir:

`v04_recovery_readiness`

con uno de:

- `READY_FOR_NONTAUTOLOGICAL_PROSPECTIVE_GATE_BUILD`
- `NOT_READY_NEEDS_METHODOLOGICAL_DECISION`

Solo usa `READY_FOR_NONTAUTOLOGICAL_PROSPECTIVE_GATE_BUILD` si puede especificarse una regla determinística derivada de evidencia que permita reproducir el control histórico sin:

- copiar/hardcodear los seis escalares congelados;
- sustituir métricas observadas por las esperadas;
- usar tolerancias;
- redondear hasta coincidir;
- debilitar `PASS_EXACT`;
- modificar artefactos históricos.

Incluye una recomendación técnica de máximo 10 líneas sobre el diseño prospectivo, pero **no construyas v0.4**.

---

## 8. Prohibiciones absolutas

No debes:

- modificar `main`;
- integrar el candidato;
- modificar Plan canónico;
- modificar artículo;
- modificar failure record de Attempt04;
- modificar gate/specs/autorización v0.3;
- modificar evaluator v0.3;
- modificar tests históricos;
- construir v0.4;
- crear autorización v0.4;
- autorizar Attempt05;
- ejecutar Attempt05;
- ejecutar retrieval;
- construir índices;
- ejecutar EV03;
- ejecutar EV04 real;
- ejecutar D1a;
- ejecutar EVAL real;
- ejecutar el modelo;
- decidir impacto métrico;
- decidir downstream reexecution;
- cerrar 0B05C;
- tocar EXP11B o EXP12.

Tampoco debes cambiar `PASS_EXACT`, introducir `isclose`, tolerancias, redondeos o comparadores aproximados.

---

## 9. Único cambio científico permitido

El candidato científico debe añadir **exactamente un artefacto de diagnóstico**, por ejemplo:

`outputs/audits/0b05c_ev04_gatec_mrr100_arithmetic_provenance_v0.3/ev04_gatec_mrr100_arithmetic_provenance_v0.3.json`

No modifiques ningún archivo preexistente.

El JSON debe contener como mínimo:

- `artifact_id`;
- `schema_version`;
- `baseline_commit`;
- bindings Git SHA1 de todas las fuentes usadas;
- entorno histórico documentado;
- entorno real ejecutado;
- tabla completa de rutas aritméticas;
- resultados MRR@100 y MRR@200 por ruta;
- frozen values y `float.hex()`;
- coexistencia `.77` / `.78` versionada;
- evidencia de provenance Git;
- `numeric_matching_routes`;
- `historical_provenance_supported_routes`;
- clasificación causal final exacta;
- `v04_recovery_readiness`;
- prohibiciones preservadas;
- `attempt05_authorized = false`;
- `metric_impact = NOT_DETERMINED`;
- `closure = NOT_AUTHORIZED`.

El commit científico candidato debe ser un único commit con un único path añadido.

---

## 10. Tests/cálculos locales y fuerza probatoria

Puedes ejecutar snippets o scripts temporales no versionados para la microauditoría.

No conviertas esos cálculos locales en “CI” ni en evidencia que yo haya ejecutado independientemente.

En tu reporte final distingue:

- hechos Git versionados;
- reproducción aritmética local de CODEX;
- inferencias de provenance.

Si no hay GitHub CI, dilo expresamente.

---

## 11. Persistencia administrativa obligatoria

Al finalizar, persiste tu reporte final en la rama:

`codex/prompts-temporary`

Ruta exacta:

`codex_prompts_tmp/28_RESPUESTA_MICROAUDITORIA_ARITMETICA_MRR100_GATE_C_EV04.md`

Ese commit administrativo debe modificar únicamente ese archivo de respuesta.

No modifiques este Prompt28 ni respuestas anteriores.

No mezcles nunca la rama administrativa con `main`.

---

## 12. Reporte final obligatorio

Responde únicamente con un reporte en español que incluya:

### A. Preflight Git
- heads y bindings.

### B. Evidencia histórica Gate C
- commits, artefactos y test `assertAlmostEqual`.

### C. Inconsistencia `.77` / `.78`
- valores exactos y dónde están versionados.

### D. Matriz de rutas aritméticas
- todas las rutas probadas con `repr`, `float.hex`, ULP y delta.

### E. Provenance
- qué ruta coincide y qué evidencia existe o falta para atribuirla históricamente.

### F. Clasificación final
- exactamente una de las tres clases del §6.

### G. Readiness v0.4
- uno de los dos estados del §7 y recomendación prospectiva breve.

### H. Candidato científico
- rama, commit, padre, tree, path, blob SHA1.

### I. Aislamiento
- confirmar que no hubo ejecución científica ni autorización.

### J. Persistencia administrativa
- rama/path/commit del reporte.

### K. Estado científico
Debe terminar manteniendo, como mínimo:

```text
GROUP_2 = EN_CURSO
0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_INTEGRATED
0B05C_V03_AUTHORIZATION = CONSUMED_BY_ATTEMPT04
EV04_ATTEMPT04_STATIC_DIAGNOSIS = VERSIONED / INTEGRATED
ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED
0B05C_CLOSURE = NOT_AUTHORIZED
```

Detente después de este bloque. No construyas v0.4 y no avances a Attempt05.
