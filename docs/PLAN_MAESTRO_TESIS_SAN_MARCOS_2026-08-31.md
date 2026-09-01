# Plan maestro acordado — Tesis San Marcos

**Proyecto:** Framework RAG explicativo y auditable para recomendación de subpartidas NANDINA  
**Repositorio principal de investigación:** `elVladdi/gci-nandina-rag`  
**Repositorio público de reproducibilidad:** `elVladdi/gci-nandina-rag-reproducibility`  
**Fecha de consolidación:** 2026-08-31

## 1. Propósito

Este archivo conserva el **plan maestro canónico acordado** para continuar la tesis, la auditoría científica, los experimentos complementarios, el congelamiento final, el repositorio de reproducibilidad y los dos productos editoriales previstos.

Debe evitar reabrir trabajo cerrado sin evidencia objetiva, mezclar auditoría con nuevos experimentos, cambiar retrospectivamente reglas después de observar resultados o confundir el repositorio de implementación con el repositorio público de reproducibilidad.

## 2. Principios congelados

1. **SERIE** es la unidad de análisis.
2. **DAM / DECLARACIÓN** es la unidad de agrupamiento cuando existe dependencia.
3. El **ranking histórico** es el mecanismo principal de candidatos.
4. La **recuperación normativa** aporta evidencia documental y no sustituye el ranking histórico.
5. El **Top-3 es fijo** antes de la explicación.
6. El **LLM local** explica el contexto recuperado; no clasifica desde cero.
7. El **reranker LLM** es diagnóstico.
8. El piloto experimental actual se mantiene en **Clase 87**.
9. Benchmark v0.2:
   - histórico: **2,950 series / 28 DAM**;
   - desarrollo: **100 series / 6 DAM**;
   - evaluación: **1,056 series / 67 DAM**.
10. El **evalset v0.2 de 1,056 casos permanece fijo** para EXP-11 y EXP-12.
11. H100 actual:
   - Top-1 = **50.95%**
   - Top-3 = **67.14%**
   - Top-5 = **76.33%**
   - Top-10 = **89.11%**
   - MRR = **0.6297**
12. El Grupo 1 solo se reabre ante un defecto objetivo nuevo.
13. EXP-11/EXP-12 deben ejecutarse con reglas predefinidas antes de observar sus resultados.

## 3. Plan de auditoría científica — 8 grupos

| Grupo | Nombre | Qué se revisa | Estado |
|---|---|---|---|
| **1** | Diseño y ejecución experimental | Si los experimentos permiten contrastar objetivos e hipótesis | **CERRADO / APPROVED** |
| **2** | Reproducibilidad y trazabilidad experimental | Si otra persona puede reconstruir qué se ejecutó y con qué insumos | **EN CURSO — G2A cerrado; EXP-11A filesystem confirma 30/30 corridas variables y outputs finales; auditoría externa de resultados pendiente** |
| **3** | Métricas y análisis estadístico/cuantitativo | Si se extrae toda la evidencia válida de los resultados | Pendiente |
| **4** | Análisis e interpretación de resultados | Si los resultados permiten explicar el comportamiento observado | Pendiente |
| **5** | Presentación de resultados | Si tablas y resultados comunican claramente la evidencia | Pendiente |
| **6** | Figuras, diagramas y visualizaciones | Si las figuras aportan información y representan fielmente método/resultados | Pendiente |
| **7** | Redacción y argumentación científica | Coherencia entre afirmaciones y evidencia | Pendiente |
| **8** | Coherencia metodológica y documental de la tesis | Correspondencia completa proyecto → tesis | Pendiente |

## 4. Grupo 1 — estado

**CERRADO / APPROVED.**

Incluye EXP-01 a EXP-10; EXP-04 A–L; split v0.2 por DAM; controles de duplicados y near-duplicates; recuperación histórica y normativa; D1a MNRL; integración histórico-normativa; reranker diagnóstico; HE4; HE5; EXP-08; EXP-05/07; cierre consolidado; procedencia; SHA/EOL; clean checkout; integración final en `main`.

No se reejecuta para mejorar resultados.

## 4.1 Registro de avance — Grupo 2A

**Fecha:** 2026-08-31  
**Hito:** G2A cerrado tras diagnóstico forense, microcierres metodológicos, versionamiento, clean checkout e integración a `main`.  
**Gate final:** `APPROVED_WITH_NONBLOCKING_LIMITATIONS`  
**Commit final G2A / main:** `a6140b66cf2975313be327d6d3d4e18e38f1fdf5`  
**Grupo 1 requiere reapertura:** `false`  
**EXP-11 retrieval iniciado durante G2A:** `false`  
**EXP-12 iniciado:** `false`  
**Grupo 3 iniciado:** `false`

Estados finales G2A:

- `G2A-F001`: `PARTIALLY_RESOLVED` — entorno histórico incompleto pero explícitamente delimitado.
- `G2A-F002`: `NOT_RECOVERABLE` — runner histórico EXP-04 C no versionado al ejecutar; R1/R2 preservados, R3 exacta limitada.
- `G2A-F003`: `PARTIALLY_RESOLVED` — procedencia script/config D1a recuperada; `execution_repository_head=UNKNOWN`.
- `G2A-F004`: `PARTIALLY_RESOLVED` — inferencia LLM/evaluación AI no reproducible byte a byte.
- `G2A-F005`: `NOT_RECOVERABLE` — metadata v0.1 de EXP-08 no recuperable; no reconstrucción retrospectiva.
- `G2A-F006`: `VERIFIED_IN_G2` — contratos EXP-11/EXP-12 implementados y testeados.
- `G2A-F007`: `OPEN / FUTURE_DEPENDENCY` — bloquea H150/H200 y toda ejecución EXP-12; no bloquea G2A ni EXP-11A.
- `G2A-F008`: `VERIFIED_IN_G2` — nesting EXP-11 demostrado estructuralmente inviable y corregido antes de retrieval.
- `G2A-F009`: `VERIFIED_IN_G2` — limitación declarada: tamaño y composición DAM están acoplados en H100; no se permite reclamar efecto causal aislado del tamaño.
- `G2A-F010`: `VERIFIED_IN_G2` — H50 corregido prospectivamente a 5 D1 / 5 D2 mediante seeds pareados.

Validación final:

- tests G2A y suite completa aprobados;
- suite completa final reportada: **257 tests, 0 fallos, 0 errores, 0 skips**;
- clean checkout final limpio;
- 11 artefactos G2A versionados con SHA coincidente;
- `origin/codex/g2a-reproducibility-v01` = `a6140b66cf2975313be327d6d3d4e18e38f1fdf5`;
- `origin/main` = `a6140b66cf2975313be327d6d3d4e18e38f1fdf5` tras fast-forward sin merge commit;
- relación base `e8a5aa7218df54b2cc309424e85914b7d914df15...main` = `0 2`.

## 5. Grupo 2A — auditoría y contratos previos de reproducibilidad

**CERRADO / APPROVED_WITH_NONBLOCKING_LIMITATIONS.**

G2A no cambió resultados científicos. Congeló contratos, seeds, configuraciones, evidencia mínima, procedencia disponible, limitaciones históricas y reglas fail-closed para EXP-11/EXP-12.

## 6. EXP-11 — Sensibilidad al tamaño del banco histórico

Objetivo principal: medir cómo el tamaño del histórico afecta **Top-3**.

Métricas secundarias: Top-1, Top-5, Top-10, MRR, errores HS6/HS4/capítulo y soporte histórico.

### EXP-11A — H25/H50/H75/H100

- H25 ≈ 25%;
- H50 ≈ 50%;
- H75 ≈ 75%;
- H100 = **2,950 series**.

Reglas congeladas:

- DAM completas;
- no muestreo simple por filas;
- nesting no requerido: `H25 ⊂ H50 ⊂ H75` fue descartado por `G2A-F008` como estructuralmente inviable;
- H25/H50/H75 se construyen como subconjuntos independientes por condición;
- H25: 10 composiciones congeladas;
- H50: 10 composiciones estratificadas **5 D1 / 5 D2** mediante cinco seeds pareados;
- H75: 10 composiciones congeladas;
- H100: una referencia única congelada;
- tolerancia máxima de volumen ±148 filas;
- selección sin NANDINA, eval, Top-k ni MRR;
- análisis principal H50 `POOLED_EQUAL_WEIGHT_5_D1_5_D2`;
- comparación D1/D2 solo diagnóstica;
- no se permite afirmar efecto causal aislado del tamaño;
- evalset v0.2 idéntico.

Interpretación obligatoria:

> Sensibilidad del desempeño de recuperación histórica al tamaño nominal del banco bajo muestreo por DAM completas y las restricciones de composición del H100 congelado.

### Gate de nuevo histórico

**Nueva data todavía no necesaria.**

El `NEW_HISTORICAL_GATE` se activa **después de cerrar y auditar EXP-11A**, antes de iniciar EXP-11B H150/H200 y antes de cualquier ejecución real de EXP-12.

Antes de H150/H200 revisar:

- procedencia;
- integridad;
- SERIE;
- DAM;
- NANDINA;
- duplicados exactos;
- near-duplicates;
- calidad básica;
- cobertura;
- ausencia de contaminación del eval;
- versionamiento;
- hashes;
- distribución/concentración;
- cobertura por código.

### EXP-11B — H150/H200

Objetivos aproximados:

- H150 ≈ **4,425 series**;
- H200 ≈ **5,900 series**.

Solo se ejecuta después de aprobar el `NEW_HISTORICAL_GATE`.

Evaluar si la curva crece, se satura o empeora por redundancia/confusión.

## 7. EXP-12 — Diversidad con volumen controlado

Estado contractual: **`CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`**.

`EXP12_EXECUTION_AUTHORIZED = false` hasta aprobar el histórico ampliado.

Pregunta:

**A igual o muy similar volumen histórico, ¿una mayor diversidad efectiva mejora Top-3?**

Diseño congelado condicionalmente:

- variable primaria: DAM HHI;
- volumen objetivo: 2,950 ±148;
- cobertura NANDINA H100 = 1.0;
- TVD ≤ 0.05 contra distribución H100;
- 10,000 candidatos por seed;
- mínimo 30 candidatos factibles;
- D-HIGH/D-MID/D-LOW por cuantiles HHI 0.10/0.50/0.90;
- `must_not_fallback_to_h100 = true`;
- manipulation check obligatorio antes de retrieval real;
- duplicados y near-duplicates son descriptores secundarios, no criterios de selección.

## 8. Grupo 2B — cierre de reproducibilidad

Después de EXP-11/12 incorporar:

- manifests;
- hashes;
- configs;
- seeds;
- scripts;
- logs;
- outputs por caso;
- matriz end-to-end;
- entorno;
- clean checkout;
- pruebas de reproducibilidad;
- clasificación de assets;
- nivel final de reproducibilidad.

Gate final:

> ¿Puede un tercero reconstruir documentalmente qué se ejecutó, con qué insumos, configuración y artefactos para cada resultado?

## 9. Grupo 3 — Métricas y análisis cuantitativo

Ejecutar después de EXP-11/12.

Revisar Top-k, MRR, Pool@N, soporte histórico, análisis pareado, estratificación, distancia jerárquica, duplicados, near-duplicates, H25–H200, variabilidad entre réplicas, intervalos/dispersiones, diversidad, tamaño, interacción tamaño×diversidad, análisis por código/DAM y limitaciones estadísticas.

## 10. Grupo 4 — Análisis e interpretación

Revisar precedentes insuficientes, ambigüedad/incompletitud, confusión jerárquica, evidencia normativa débil, saturación, redundancia, diversidad, errores persistentes, diferencias histórico/normativo, límites del LLM y alcance Clase 87. Evitar causalidad no demostrada.

## 11. Grupo 5 — Presentación de resultados

Auditar tablas, denominadores, comparaciones homogéneas, benchmark principal vs diagnósticos, H100 vs H25–H200, diversidad, métricas por componente, variabilidad y resultados principales/secundarios.

## 12. Grupo 6 — Figuras y visualizaciones

Prioridades: arquitectura RAG final, histórico vs normativo, flujo experimental, curva H25–H200, efecto de diversidad, Top-k, errores jerárquicos, soporte histórico, trazabilidad/reproducibilidad, retrieval → augmentation → generation y revisión humana.

## 13. Grupo 7 — Redacción y argumentación científica

Auditar coherencia evidencia-afirmación, evitar sobreafirmaciones, distinguir respaldada/parcialmente respaldada/demostrada/sugerida, separar resultado de interpretación, declarar limitaciones y describir correctamente el rol del LLM/RAG.

## 14. Grupo 8 — Coherencia metodológica y documental

Verificar:

`Problema → Objetivos → Hipótesis → Variables → Indicadores → Experimentos → Resultados → Discusión → Conclusiones`

## 15. Congelamiento científico final

Solo después de Grupo 2A, EXP-11A, Gate de datos nuevos, EXP-11B, EXP-12, Grupo 2B y Grupos 3–8.

## 16. Repositorio público independiente de reproducibilidad

Repositorio: `elVladdi/gci-nandina-rag-reproducibility`.

Completar después del congelamiento científico final.

## 17. Artículo científico principal

Revista de referencia actual: **Knowledge-Based Systems (KBS)**, sujeta a reevaluación final.

## 18. Artículo sectorial / WCO

Producto diferenciado orientado a gobernanza, trazabilidad, revisión humana, privacidad y despliegue offline/local.

## 19. Licencia

Estado: `LICENSE_DECISION = PENDING`.

## 20. Orden maestro actualizado

1. Grupo 1 — cerrado.
2. Grupo 2A — **cerrado con limitaciones no bloqueantes e integrado a main**.
3. **EXP-11A — ejecución completada 30/30 en filesystem; auditoría externa de resultados pendiente.**
4. Auditar resultados EXP-11A.
5. Activar `NEW_HISTORICAL_GATE` y solicitar nueva data.
6. EXP-11B H150/H200.
7. EXP-12.
8. Grupo 2B.
9. Grupo 3.
10. Grupo 4.
11. Grupo 5.
12. Grupo 6.
13. Grupo 7.
14. Grupo 8.
15. Freeze científico.
16. Repositorio público de reproducibilidad.
17. Artículo científico.
18. Artículo sectorial/WCO.
19. Tesis final/archive.
20. Extensiones futuras.

## 21. Registro de decisiones y hallazgos clave

### 2026-08-31 — G2A Microclose 1C y 1D

- **Microclose 1C:** se sustituyó el nesting inviable por subconjuntos independientes por condición con DAM completas y volumen controlado. Se preservaron H25/H75 y se registró `G2A-F009 = STRUCTURAL_SIZE_COMPOSITION_COUPLING` como limitación de interpretación.
- La evidencia pre-ejecución confirmó 10 composiciones factibles H25, 10 H50 y 10 H75 sin ejecutar BM25 ni usar desempeño del evalset.
- Se detectó `G2A-F010 = H50_DOMINANT_STRATUM_IMBALANCE` porque la primera composición H50 contenía D1 en 2/10 réplicas y D2 en 8/10; el hallazgo ocurrió antes de retrieval.
- **Microclose 1D:** H50 se corrigió prospectivamente mediante cinco seeds pareados que generan **5 H50-D1 y 5 H50-D2**. El análisis principal será `POOLED_EQUAL_WEIGHT_5_D1_5_D2`; D1/D2 queda como diagnóstico secundario sin interpretación causal.
- H25 y H75 conservaron sus diez composiciones y SHA previamente auditados.
- EXP-12 v3 queda `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`, con HHI como variable primaria y manipulation check obligatorio antes de retrieval real.
- Tests reportados: **26/26 G2A** y **255/255 suite completa**, sin fallos ni errores.
- No se ejecutó retrieval EXP-11, EXP-12 permanece sin ejecución, no cambiaron resultados científicos y Grupo 1 no se reabre.
- **Pendiente antes del Gate G2A:** normalizar estados F001–F010, cerrar F010 como corrección verificada, versionar la evidencia mínima G2A y validar clean checkout post-commit.

### 2026-08-31 — Cierre de G2A

- Rama auditada: `codex/g2a-reproducibility-v01`.
- Commit candidato remoto: `c9751f67165b0bf6e06b54e4e979e7258481ded6`.
- Comparación contra `main`/base `e8a5aa7218df54b2cc309424e85914b7d914df15`: **ahead_by=1, behind_by=0**, 18 archivos cambiados; 17 añadidos y una modificación autorizada del test HE4.
- Tests pre-commit: **28 G2A / 257 suite completa**, sin fallos, errores ni skips.
- Clean checkout post-commit reportado limpio y reproducible; 11 artefactos G2A versionados con SHA coincidente.
- Estados finales: F001/F003/F004 `PARTIALLY_RESOLVED`; F002/F005 `NOT_RECOVERABLE`; F006/F008/F009/F010 `VERIFIED_IN_G2`; F007 `OPEN / FUTURE_DEPENDENCY`.
- Gate final G2A: **`APPROVED_WITH_NONBLOCKING_LIMITATIONS`**.
- Grupo 1 permanece cerrado y no se reabre.
- EXP-11 y EXP-12 no fueron ejecutados durante G2A.
- Siguiente paso autorizado: **EXP-11A H25/H50/H75/H100**.
- La nueva data no se requiere aún; se activa después de EXP-11A, para el Gate de histórico ampliado previo a H150/H200 y EXP-12.

### 2026-08-31 — Cierre operativo final e integración de G2A a main

- Gate final confirmado en repositorio: `APPROVED_WITH_NONBLOCKING_LIMITATIONS`; `G2A_CLOSED=true`.
- Commit final G2A: `a6140b66cf2975313be327d6d3d4e18e38f1fdf5`.
- `origin/codex/g2a-reproducibility-v01` y `origin/main` apuntan al mismo commit final.
- Integración a `main` realizada por **fast-forward**, sin merge commit; relación `e8a5aa...main = 0 2`.
- Suite final reportada sobre rama, clean checkout y `main`: **257 tests, 0 failures, 0 errors, 0 skips**.
- EXP-11A queda contractualmente autorizado solo para `H25/H50/H75/H100`.
- EXP-11B permanece bloqueado; H150/H200 siguen `PENDING_NEW_HISTORICAL_GATE`.
- EXP-12 permanece `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE` y no autorizado.
- `NEW_HISTORICAL_DATA_REQUIRED_NOW=false`; trigger de nueva data: `AFTER_EXP11A_EXTERNAL_AUDIT`.
- Próximo paso: **primer prompt de ejecución científica EXP-11A**.

### 2026-08-31 — EXP-11A iniciado y detenido por Gate H100

- Rama experimental: `codex/exp11a-size-sensitivity-v01`.
- Commit pre-ejecución: `d44ec215cce639b5bb25a481c944b8ee36a64098`.
- Preflight: `PASS`.
- `EXP11_RETRIEVAL_STARTED=true`.
- H100 reejecutado; Gate `EXP11A_VALIDITY_GATE=FAILED`.
- Corridas variables ejecutadas: **0/30**; no existen resultados H25/H50/H75.
- Suite previa al retrieval: **262 tests, 0 failures, 0 errors**.
- Código/config sin cambios después del inicio.
- Auditoría externa del defecto: el runner usa MRR congelado truncado `0.62970774935`, mientras el artefacto histórico versionado contiene `0.6297077493524843`; con `abs_tol=1e-12`, la diferencia de ~`2.484e-12` produce un falso negativo posible del Gate.
- Estado: **EXP-11A PAUSADO — CORRECCIÓN DEL GATE H100 REQUERIDA; NO REABRIR DISEÑO NI RESELECCIONAR COMPOSICIONES**.
- Nueva data: todavía no requerida.

### 2026-08-31 — H100 revalidado y Gate EXP-11A aprobado

- Attempt 01 preservado con SHA `46f4d2af67505fdc308ee6a1a8de1048fe17ee146aa6d97342cdc32f675eb13c` y 3,462,859 bytes.
- Hallazgos `EXP11A-F001` y `EXP11A-F002` confirmados como defectos de Gate/persistencia sin afectación científica.
- Commit correctivo congelado: `58839ca838772b79df61e7decf62a43ea7df270f`.
- La rama remota `codex/exp11a-size-sensitivity-v01` coincide con ese commit.
- Corrección limitada a runner EXP-11A y sus tests.
- Tests EXP-11A: **11 PASS**; suite completa: **268 tests, 0 failures, 0 errors**; clean checkout también aprobado.
- `H100_ATTEMPT_02`: Top1 538/538, Top3 709/709, Top5 806/806, Top10 941/941, Top50 1047/1047, MRR `0.6297077493524843 / 0.6297077493524843`, delta `0.0`.
- `H100_REVALIDATION=PASS`; `EXP11A_VALIDITY_GATE=PASS` tras auditoría externa.
- Corridas variables ejecutadas hasta este hito: **0/30**.
- Siguiente paso autorizado: ejecutar las 30 corridas H25/H50/H75 sin cambiar código, configuración, seeds ni composiciones.
- Nueva data: todavía no requerida.

### 2026-08-31 — H100 PASS con hallazgo residual de persistencia en `--execute`

- Attempt 02 persistió correctamente inicio y diagnóstico.
- Top1/Top3/Top5/Top10/Top50 y MRR coinciden exactamente con H100 congelado; delta MRR `0.0`.
- Commit correctivo auditado: `58839ca838772b79df61e7decf62a43ea7df270f`; rama remota coincide.
- Diff respecto a `d44ec215...`: solo runner EXP-11A y tests.
- Tests: **11 EXP-11A PASS**; suite completa **268/268**, clean checkout aprobado.
- Auditoría externa del código detectó que la persistencia fail-closed corregida existe en `run_h100_check_only`, pero el path productivo `execute()` todavía puede lanzar el H100 Gate antes de serializar el diagnóstico.
- `EXP11A-F001` queda resuelto.
- `EXP11A-F002` queda **PARTIALLY_RESOLVED** hasta unificar la persistencia en `--execute`.
- Corridas variables ejecutadas: **0/30**.
- Próximo paso: microclose correctivo 02; todavía no ejecutar H25/H50/H75.

### 2026-08-31 — Execution path EXP-11A congelado

- HEAD inicial del microclose: `58839ca838772b79df61e7decf62a43ea7df270f`.
- Commit final de ejecución: `22b18cdc743b4b0f37b8b345215fb747d614d6eb`.
- Diff limitado al runner EXP-11A y sus tests.
- `EXP11A-F001=VERIFIED_RESOLVED`.
- `EXP11A-F002=VERIFIED_RESOLVED`.
- Tests EXP-11A: **13/13 PASS**.
- Suite completa: **270/270 PASS**, 0 fallos, 0 errores, 0 skips.
- Clean checkout reportado limpio con config, referencia H100 y evidencia v0.2 tracked.
- La prueba productiva verifica que un fallo H100 se persiste antes del raise y deja `variable_runs_completed=0`.
- Corridas variables ejecutadas hasta este hito: **0/30**.
- Siguiente paso autorizado: preservar Attempt 02 y ejecutar `--execute` bajo `22b18cdc...`.
- Nueva data: todavía no requerida.

### 2026-08-31 — EXP-11A ejecución completa interrumpida tras 25/30 variables

- Commit de ejecución congelado: `22b18cdc743b4b0f37b8b345215fb747d614d6eb`; rama remota verificada idéntica.
- Corridas variables completas reportadas inicialmente: **25/30**.
- H25: **10/10** completas.
- H50: **10/10** completas.
- H75: **5/10** completas.
- `H75-R06`: inicialmente se reportó CSV de condición materializado, sin run JSON.
- No se reintentó ninguna corrida ni se modificó código/configuración.
- La escritura de metadata administrativa posterior fue bloqueada por límite de herramientas de la plataforma.
- Este estado quedó posteriormente contradicho por el filesystem completo; se conserva como registro de una observación transitoria/no reconciliada, no como estado científico final.

### 2026-08-31 — Reconciliación: filesystem confirma EXP-11A 30/30

- El microcierre forense se detuvo sin escribir metadata ni renombrar outputs al detectar una contradicción objetiva con el reporte previo de 25/30.
- Filesystem actual: **31 run JSON** = 1 H100 + **30 variables completas**.
- H25: **10/10**.
- H50: **10/10**.
- H75: **10/10**, incluidos `H75-R06` a `H75-R10`.
- Existen los **11 outputs finales**, incluido `exp11_run_manifest.json`.
- Los 30 run JSON variables validaron: execution commit, composition SHA, subset SHA, eval SHA, `n_eval=1056`, BM25 y overlap.
- `EXP11A-F003` **NO se crea** en este estado; la hipótesis de interrupción parcial queda descartada por evidencia posterior del filesystem.
- Pendiente: reconciliar timestamps/logs para determinar si el reporte 25/30 fue una observación transitoria mientras el proceso seguía activo o un reporte stale; auditar hashes, manifest y resultados descriptivos completos.
- No rerun, no resume, no cambio de código/config, no commit de resultados.
- Nueva data: todavía no requerida.
