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
| **2** | Reproducibilidad y trazabilidad experimental | Si otra persona puede reconstruir qué se ejecutó y con qué insumos | **EN CURSO — G2A diagnóstico completado; microclose requerido** |
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
**Hito:** Diagnóstico forense inicial `READ-ONLY` completado y auditado externamente.  
**Gate preliminar:** `REQUIRES_MICROCLOSE`  
**Grupo 1 requiere reapertura:** `false`  
**EXP-11 iniciado:** `false`  
**EXP-12 iniciado:** `false`  
**Grupo 3 iniciado:** `false`

Hallazgos preliminares registrados:

- `G2A-F001`: entorno histórico incompleto y dependencias no fijadas — S2.
- `G2A-F002`: EXP-04 C presenta limitación de repetición exacta porque el runner no quedó versionado en el momento de la ejecución — S2.
- `G2A-F003`: procedencia del entrenamiento D1a requiere cierre forense adicional. La historia Git permite recuperar al menos el último commit que modificó el runner antes de la ejecución; no debe declararse `NOT_RECOVERABLE` sin agotar esa evidencia.
- `G2A-F004`: inferencia LLM/evaluación AI no es reproducible byte-a-byte con la evidencia actual — S2.
- `G2A-F005`: metadata v0.1 utilizada en EXP-08 permanece no recuperable; debe declararse como limitación histórica y no reconstruirse especulativamente — S2.
- `G2A-F006`: contratos ejecutables de EXP-11/EXP-12 aún no implementados — S3.
- `G2A-F007`: banco ampliado H150/H200 aún no existe — S3 y dependencia futura, no defecto del benchmark H100.

**Próximo paso autorizado:** microclose G2A controlado. Debe formalizar inventarios/matrices de reproducibilidad, agotar la procedencia forense recuperable —especialmente D1a— y preparar los contratos prospectivos de EXP-11/EXP-12 sin ejecutar ninguno de los dos experimentos.

## 5. Grupo 2A — auditoría y contratos previos de reproducibilidad

Antes de EXP-11/12 debe cerrar los contratos que deben cumplir las nuevas corridas.

Revisar:

- datasets/corpus y versiones;
- configuraciones;
- seeds o `NOT_APPLICABLE`;
- prompts;
- logs;
- manifests;
- hashes;
- procedencia;
- dependencias;
- entorno computacional;
- matriz input → script → config → output → hash;
- assets versionados/locales/regenerables/runtime-only;
- clean checkout;
- reproducibilidad Windows/Linux.

Pendientes principales:

1. **Freeze del entorno:** Python, OS/plataforma, versiones exactas de paquetes, Torch, sentence-transformers, hnswlib, Ollama, modelo/digest y parámetros.
2. **Matriz end-to-end:** resultado, output, SHA, script, config, seed, inputs, hashes y procedencia.
3. **Auditoría formal de configs/seeds:** A–L, EXP-05–EXP-10 y luego EXP-11/12.
4. **Clasificación de assets:** frozen evidence, reconstructable, restricted/local, runtime-only, optional diagnostic, not required.
5. **Nivel de reproducibilidad alcanzado:** analítica, computacional, fuente administrativa, entrenamiento, inferencia LLM y limitaciones.

Grupo 2A no cambia resultados científicos.

## 6. EXP-11 — Sensibilidad al tamaño del banco histórico

Objetivo principal: medir cómo el tamaño del histórico afecta **Top-3**.

Métricas secundarias: Top-1, Top-5, Top-10, MRR, errores HS6/HS4/capítulo y soporte histórico.

### EXP-11A — H25/H50/H75/H100

- H25 ≈ 25%;
- H50 ≈ 50%;
- H75 ≈ 75%;
- H100 = **2,950 series**.

Reglas:

- DAM completas;
- no muestreo simple por filas;
- preferencia por `H25 ⊂ H50 ⊂ H75 ⊂ H100`;
- varias réplicas cuando corresponda;
- seeds congeladas;
- pipeline/configs fijos;
- evalset v0.2 idéntico.

### Gate de nuevo histórico

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

Evaluar si la curva crece, se satura o empeora por redundancia/confusión.

## 7. EXP-12 — Diversidad con volumen controlado

Pregunta:

**A igual o muy similar volumen histórico, ¿una mayor diversidad efectiva mejora Top-3?**

Condiciones:

- D-LOW;
- D-MID;
- D-HIGH.

Medidas:

- número de DAM;
- HHI;
- número efectivo de DAM;
- descripciones únicas;
- duplicados;
- near-duplicates;
- códigos cubiertos;
- DAM por código;
- soporte independiente por NANDINA;
- diversidad descriptiva/léxica.

Mantener aproximadamente constante el número de series mientras cambia la diversidad.

### Freeze previo de fichas

Antes de correr EXP-11/12 congelar:

- número de réplicas;
- selección de DAM;
- seeds;
- definición de diversidad;
- reglas H150/H200;
- tratamiento de NANDINA nuevas;
- prohibición de cambiar eval;
- métricas;
- análisis estadístico;
- outputs;
- manifests;
- Gates.

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

Revisar:

- precedentes insuficientes;
- ambigüedad/incompletitud;
- confusión jerárquica;
- evidencia normativa débil;
- saturación;
- redundancia;
- diversidad;
- errores persistentes;
- diferencias histórico/normativo;
- límites del LLM;
- alcance Clase 87.

Evitar causalidad no demostrada.

## 11. Grupo 5 — Presentación de resultados

Auditar tablas, denominadores, comparaciones homogéneas, benchmark principal vs diagnósticos, H100 vs H25–H200, diversidad, métricas por componente, variabilidad y resultados principales/secundarios.

## 12. Grupo 6 — Figuras y visualizaciones

Prioridades:

- arquitectura RAG final;
- histórico vs normativo;
- flujo experimental;
- curva H25–H200;
- efecto de diversidad;
- Top-k;
- errores jerárquicos;
- soporte histórico;
- trazabilidad/reproducibilidad;
- retrieval → augmentation → generation;
- revisión humana.

## 13. Grupo 7 — Redacción y argumentación científica

Auditar coherencia evidencia-afirmación, evitar sobreafirmaciones, distinguir respaldada/parcialmente respaldada/demostrada/sugerida, separar resultado de interpretación, declarar limitaciones y describir correctamente el rol del LLM/RAG.

## 14. Grupo 8 — Coherencia metodológica y documental

Verificar:

`Problema → Objetivos → Hipótesis → Variables → Indicadores → Experimentos → Resultados → Discusión → Conclusiones`

Incluye PE↔OE, OE↔HE, HE↔métricas, HE↔EXP, EXP↔resultados, resultados↔conclusiones, anexos, tablas, figuras, repositorio, reproducibilidad y delimitaciones.

## 15. Congelamiento científico final

Solo después de:

1. Grupo 2A;
2. EXP-11A;
3. Gate de datos nuevos;
4. EXP-11B;
5. EXP-12;
6. Grupo 2B;
7. Grupos 3–8.

Congelar:

- commit final;
- datasets/corpus;
- configs;
- prompts;
- seeds;
- modelos/digests;
- manifests;
- hashes;
- outputs;
- métricas;
- figuras;
- tablas;
- veredictos;
- limitaciones;
- conclusiones;
- protocolo.

## 16. Repositorio público independiente de reproducibilidad

Repositorio: `elVladdi/gci-nandina-rag-reproducibility`

Principio: publicar una **especificación reproducible para replicación independiente**, no simplemente copiar la implementación privada.

Debe contener:

- protocolo;
- especificaciones funcionales;
- contratos de datos;
- configs de referencia;
- manifests;
- hashes;
- métricas/resultados verificables;
- pseudocódigo;
- invariantes;
- test vectors;
- ejemplos sintéticos;
- guía de replicación;
- criterios de validez.

Debe permitir otras jurisdicciones, capítulos, HS-6, NANDINA/extensiones nacionales, datos propios y corpus propios.

Completar **después del congelamiento científico final**.

## 17. Artículo científico principal

Revista de referencia actual: **Knowledge-Based Systems (KBS)**, sujeta a reevaluación final.

Alternativas: ESWA, IP&M, DSS, GIQ, AI & Law y World Customs Journal.

Novedad: no limitarla a “RAG/LLM para HS Code”. Ejes:

- independencia por DAM;
- sensibilidad al particionado;
- tamaño/diversidad del histórico;
- memoria documental;
- histórico vs normativo;
- separación ranking/evidencia/generación;
- auditabilidad;
- errores jerárquicos;
- dependencia de precedentes;
- reproducibilidad;
- ejecución local/offline;
- revisión humana.

## 18. Segundo artículo — publicación sectorial aduanera

Orientación principal: **WCO / WCO News**.  
Alternativa: **World Customs Journal**.

Foco: gobernanza, trazabilidad, revisión humana, privacidad, operación local/offline, memoria histórica institucional, evidencia normativa, auditabilidad, replicación en otras jurisdicciones y límites de automatización.

No duplicar el paper científico.

## 19. Cierre de tesis y archivo

- consolidar tesis;
- verificar anexos/referencias;
- congelar tablas/figuras;
- archivar SHA final;
- release si corresponde;
- documentar repositorios;
- documentar datos no redistribuibles;
- documentar replicación.

## 20. Extensiones futuras

Posteriores al trabajo principal:

- validación temporal;
- validación externa;
- otros capítulos;
- universo arancelario completo;
- otras jurisdicciones;
- otros retrieval/reranking;
- evaluación humana externa;
- evaluación operativa real;
- actualización longitudinal del histórico.

## 21. Licencia

`LICENSE_DECISION = PENDING`

No adoptar una licencia nueva sin revisar por separado software, especificaciones, datasets, materiales de terceros y derechos de redistribución.

# 22. Orden maestro definitivo

```text
1. Grupo 1 — Diseño y ejecución experimental
   ✅ CERRADO
        ↓
2. Grupo 2A — Auditoría y contratos de reproducibilidad
        ↓
3. EXP-11A — H25 / H50 / H75 / H100
        ↓
4. Gate de incorporación de nuevo histórico
        ↓
5. EXP-11B — H150 / H200
        ↓
6. EXP-12 — Diversidad con volumen controlado
        ↓
7. Grupo 2B — Reproducibilidad de EXP-11/12 + Gate final
        ↓
8. Grupo 3 — Métricas y análisis estadístico/cuantitativo
        ↓
9. Grupo 4 — Análisis e interpretación
        ↓
10. Grupo 5 — Presentación de resultados
        ↓
11. Grupo 6 — Figuras, diagramas y visualizaciones
        ↓
12. Grupo 7 — Redacción y argumentación científica
        ↓
13. Grupo 8 — Coherencia metodológica y documental
        ↓
14. CONGELAMIENTO CIENTÍFICO FINAL
        ↓
15. Completar repositorio público de reproducibilidad
        ↓
16. Artículo científico principal
    → referencia actual: Knowledge-Based Systems
        ↓
17. Artículo sectorial internacional
    → WCO / WCO News
    → World Customs Journal como alternativa
        ↓
18. Cierre final de tesis / archivo / publicación
        ↓
19. Extensiones futuras
```

## 23. Próximo paso inmediato

**Grupo 2A — microclose correctivo controlado posterior al diagnóstico forense.**

Debe formalizar los inventarios y matrices de reproducibilidad exigidos por G2A, agotar la procedencia histórica recuperable —especialmente D1a— y preparar/fijar los contratos prospectivos de EXP-11/EXP-12. No se autoriza ejecutar EXP-11, EXP-12 ni iniciar Grupo 3 hasta que el Gate G2A sea auditado y aprobado.

---

## Nota de control

Este documento es el **plan maestro acordado**.

Si en el futuro se propone alterar el orden, agregar/quitar experimentos o cambiar la ubicación de EXP-11/EXP-12, debe registrarse explícitamente como una revisión del plan y justificarse antes de ejecutar el cambio.

## 24. Historial de actualización del plan

### 2026-08-31 — Inicio formal de Grupo 2A

- Grupo 1 permanece `CLOSED / APPROVED`.
- Se crearon las fichas `G2-00`, `G2A-01` y `G2B-01`.
- Se completó la primera auditoría forense G2A en modo `READ-ONLY`.
- El Gate preliminar G2A quedó en `REQUIRES_MICROCLOSE`.
- No se modificaron resultados científicos, no se regeneraron artefactos y no se iniciaron EXP-11, EXP-12 ni Grupo 3.
- Se mantiene el orden maestro: cerrar G2A antes de ejecutar EXP-11/EXP-12.
