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
| **2** | Reproducibilidad y trazabilidad experimental | Si otra persona puede reconstruir qué se ejecutó y con qué insumos | **EN CURSO — G2A CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS e integrado a main; siguiente: EXP-11A** |
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
3. **EXP-11A — siguiente paso.**
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

## 21. Próximo paso inmediato

**EXP-11A — ejecución de sensibilidad H25/H50/H75/H100 bajo el contrato congelado.**

G2A queda `CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS` e integrado a `main` en `a6140b66cf2975313be327d6d3d4e18e38f1fdf5`.

Se autoriza avanzar a EXP-11A únicamente con las composiciones, seeds, tolerancias, controles y outputs ya congelados. H100 permanece como referencia única. No se autoriza EXP-11B ni EXP-12 todavía.

**Nueva data:** todavía no es necesaria. El punto de activación será después de cerrar y auditar EXP-11A, antes de EXP-11B H150/H200 y antes de cualquier ejecución real de EXP-12. En ese momento debe ejecutarse el `NEW_HISTORICAL_GATE` sobre el banco ampliado.

---

## 22. Historial de actualización del plan

### 2026-08-31 — Inicio formal de Grupo 2A

- Grupo 1 permanece `CLOSED / APPROVED`.
- Se crearon las fichas `G2-00`, `G2A-01` y `G2B-01`.
- Se completó la primera auditoría forense G2A en modo `READ-ONLY`.
- El Gate preliminar G2A quedó en `REQUIRES_MICROCLOSE`.

### 2026-08-31 — Microcierres G2A

- Se completaron los microcierres 1A–1E.
- Se corrigió la dependencia de rama del test HE4 sin alterar evidencia científica.
- Se formalizó la procedencia D1a disponible.
- Se demostró la inviabilidad estructural del nesting EXP-11.
- Se rediseñó EXP-11 con subconjuntos independientes por condición.
- Se declaró la limitación tamaño–composición DAM.
- Se corrigió H50 a 5 D1 / 5 D2 antes de retrieval.
- Se congeló EXP-12 condicionalmente y fail-closed.

### 2026-08-31 — Cierre operativo final e integración de G2A a main

- Gate final: `APPROVED_WITH_NONBLOCKING_LIMITATIONS`.
- Commit final G2A: `a6140b66cf2975313be327d6d3d4e18e38f1fdf5`.
- `origin/codex/g2a-reproducibility-v01` y `origin/main` apuntan al mismo commit final.
- Integración a `main` por fast-forward, sin merge commit.
- Suite final reportada sobre rama, clean checkout y `main`: **257 tests, 0 failures, 0 errors, 0 skips**.
- EXP-11A autorizado únicamente para H25/H50/H75/H100.
- EXP-11B y EXP-12 continúan bloqueados.
- `NEW_HISTORICAL_DATA_REQUIRED_NOW=false`.
- Trigger de nueva data: `AFTER_EXP11A_EXTERNAL_AUDIT`.
- Próximo paso: **ejecución científica EXP-11A**.
