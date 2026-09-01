# Plan maestro canónico — Tesis San Marcos

**Proyecto:** Framework RAG explicativo y auditable para recomendación de subpartidas NANDINA  
**Repositorio principal:** `elVladdi/gci-nandina-rag`  
**Repositorio público de reproducibilidad:** `elVladdi/gci-nandina-rag-reproducibility`  
**Fecha de actualización:** 2026-09-01

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
12. No se permite interpretar EXP-11A como efecto causal aislado del tamaño del banco.

## 2. Estado del plan de auditoría

| Grupo | Estado |
|---|---|
| 1. Diseño y ejecución experimental | **CLOSED / APPROVED** |
| 2. Reproducibilidad y trazabilidad | **EN CURSO — G2A cerrado; EXP-11A cerrado e integrado; NEW_HISTORICAL_GATE siguiente** |
| 3. Métricas e inferencia | Pendiente |
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
- Eval SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- H100 histórico:
  - Top-1 = 538/1056 = 0.50946969697
  - Top-3 = 709/1056 = 0.67140151515
  - Top-5 = 806/1056 = 0.76325757576
  - Top-10 = 941/1056 = 0.89109848485
  - Top-50 = 1047/1056 = 0.99147727273
  - MRR = `0.6297077493524843`

## 4. Grupo 1

**CLOSED / APPROVED.**

No se reejecuta para mejorar resultados.

## 5. Grupo 2A

**CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS.**

Commit de cierre G2A integrado a main:  
`a6140b66cf2975313be327d6d3d4e18e38f1fdf5`

Estados finales:

- F001 `PARTIALLY_RESOLVED`
- F002 `NOT_RECOVERABLE`
- F003 `PARTIALLY_RESOLVED`
- F004 `PARTIALLY_RESOLVED`
- F005 `NOT_RECOVERABLE`
- F006 `VERIFIED_IN_G2`
- F007 `OPEN / FUTURE_DEPENDENCY`
- F008 `VERIFIED_IN_G2`
- F009 `VERIFIED_IN_G2 / DECLARED_LIMITATION`
- F010 `VERIFIED_IN_G2`

F007 bloquea H150/H200 y EXP-12 hasta aprobar el nuevo histórico, pero no reabre G2A ni Grupo 1.

## 6. EXP-11A — cierre definitivo

**CLOSED / APPROVED / VERSIONED / INTEGRATED TO MAIN.**

`origin/main` actual:  
`9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`

Cadena EXP-11A sobre el cierre G2A:

1. `d44ec215cce639b5bb25a481c944b8ee36a64098` — runner pre-ejecución.
2. `58839ca838772b79df61e7decf62a43ea7df270f` — corrección de precisión del Gate H100.
3. `22b18cdc743b4b0f37b8b345215fb747d614d6eb` — persistencia fail-closed en `--execute`.
4. `9e8af129ca586bd1929e6afe6aa1a1c64d8fe667` — freeze de resultados auditados.

Ejecución válida:

- H25 = 10 corridas.
- H50 = 10 corridas.
- H75 = 10 corridas.
- H100 = 1 referencia.
- H50 = 5 D1 / 5 D2 con seeds pareadas 20261001–20261005.
- Case-level = **32,736 filas = 31 × 1,056**.
- H100 Gate = `PASS`.
- No hubo rerun ni resume.
- Reconciliación del reporte transitorio 25/30: `TRANSIENT_OBSERVATION_WHILE_PROCESS_CONTINUED`.
- `EXP11A_F003_CREATED=false`.
- Freeze: 47 artefactos versionados; 46 hashes directamente verificables; 0 mismatches; 1 autoexclusión del inventario.
- Tests finales: 13/13 EXP-11A y 270/270 suite completa.

### Resultados descriptivos EXP-11A

| Condición | Top-3 | MRR |
|---|---:|---:|
| H25 | 0.645170 ± 0.051964 | 0.603787 ± 0.047775 |
| H50 | 0.597917 ± 0.066393 | 0.542492 ± 0.060405 |
| H75 | 0.463352 ± 0.132774 | 0.414030 ± 0.126668 |
| H100 | 0.671402 | 0.629708 |

Lectura permitida: sensibilidad al tamaño nominal **bajo restricciones naturales de composición**.  
Lectura prohibida: “aumentar el tamaño causa una caída de desempeño”.

H25/H50/H75 difieren también en número de DAM, HHI, cobertura NANDINA y soporte. La inferencia formal y las decisiones HE2/HE5 quedan para Grupo 3.

## 7. NEW_HISTORICAL_GATE

**Trigger alcanzado:** `NEW_HISTORICAL_GATE_TRIGGER_REACHED=true`.  
**Nueva data requerida para la siguiente fase:** `true`.  
**Nueva data procesada:** `false`.  
**Excel modificado:** `false`.  
**EXP-11B autorizado:** `false`.  
**EXP-12 autorizado:** `false`.

### Próximo paso obligatorio

**Auditoría forense READ-ONLY del pipeline original:**

`data/Series - Descripciones.xlsx`  
→ Python de ingesta/normalización  
→ datos v0.1  
→ split por DAM v0.2  
→ H100/dev/eval congelados.

Antes de modificar el Excel se debe establecer con evidencia:

- SHA-256 del libro actual;
- nombres y orden de hojas;
- hoja(s) utilizadas históricamente;
- scripts `.py` exactos y commits;
- argumentos/comandos recuperables;
- reglas de parsing, normalización y filtrado;
- filtro Clase 87;
- construcción de `DECLARACION`, `SERIE`, `NANDINA`, descripción e `id_unico`;
- generación de v0.1;
- transformación v0.1 → v0.2 por DAM;
- reproducción en directorio temporal;
- comparación byte-exacta y, si fuese necesario, comparación canónica fila a fila.

Clasificación final permitida:

- `PIPELINE_EXACTLY_RECONSTRUCTED`
- `PIPELINE_CONTENT_REPRODUCIBLE_NOT_BYTE_EXACT`
- `PIPELINE_PARTIALLY_RECONSTRUCTED`
- `PIPELINE_NOT_RECONSTRUCTIBLE`

### Hallazgo preliminar a verificar

El parser actual `src/ingestion/sunat_series_parser.py` usa por defecto la **primera hoja del workbook** cuando no se proporciona `--sheet`.

Consecuencia: agregar una o dos hojas nuevas al mismo Excel **no implica que el pipeline actual vaya a leerlas**. No se diseñará aún la estrategia multi-hoja; primero se reconstruirá el pipeline histórico.

### Regla para el usuario

**NO modificar todavía `data/Series - Descripciones.xlsx`.**  
No agregar nuevas pestañas hasta aprobar esta auditoría y congelar una copia byte-a-byte de la fuente histórica actual.

## 8. EXP-11B

Objetivos aproximados:

- H150 ≈ **4,425 series**
- H200 ≈ **5,900 series**

Solo se autoriza tras:

1. auditoría forense del pipeline Excel→Python;
2. congelamiento de la fuente histórica actual;
3. definición del contrato para nuevas pestañas;
4. procesamiento Python versionado de la nueva data;
5. aprobación del `NEW_HISTORICAL_GATE`.

## 9. EXP-12

Estado: `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`.

No usar H100 como fallback.

Diseño congelado condicional:

- HHI como variable primaria de diversidad;
- volumen 2,950 ±148;
- cobertura NANDINA H100 = 1.0;
- TVD ≤ 0.05;
- 10,000 candidatos por seed;
- mínimo 30 factibles;
- cuantiles HHI 0.10 / 0.50 / 0.90;
- manipulation check obligatorio.

## 10. Grupo 2B

Después de EXP-11B/EXP-12 cerrar:

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
- clasificación de assets;
- nivel final de reproducibilidad.

## 11. Grupos 3–8

Grupo 3 realizará métricas e inferencia formal, incluida la decisión de HE2/HE5.  
Grupos 4–8 cubrirán interpretación, presentación, figuras, redacción y coherencia documental.

## 12. Orden maestro actual

```text
1. Grupo 1
   ✅ CERRADO
        ↓
2. Grupo 2A
   ✅ CERRADO / APPROVED_WITH_NONBLOCKING_LIMITATIONS
        ↓
3. EXP-11A
   ✅ CLOSED / APPROVED / INTEGRATED TO MAIN
        ↓
4. NEW_HISTORICAL_GATE
   ⏳ AUDITORÍA FORENSE EXCEL → PYTHON → v0.1 → v0.2
        ↓
5. Congelar Excel histórico + contrato para nuevas pestañas
        ↓
6. Incorporar nueva data mediante Python versionado
        ↓
7. EXP-11B H150/H200
        ↓
8. EXP-12
        ↓
9. Grupo 2B
        ↓
10. Grupo 3
        ↓
11. Grupos 4–8
        ↓
12. Freeze científico final
        ↓
13. Repositorio público / artículos / cierre de tesis
```

## 13. Estado de publicación y reproducibilidad

Repositorio público: `elVladdi/gci-nandina-rag-reproducibility`.  
No completar hasta el congelamiento científico final.

Revista científica de referencia actual: **Knowledge-Based Systems**, sujeta a reevaluación.  
Producto sectorial: orientación WCO/WCO News; World Customs Journal como alternativa.

## 14. Historial reciente

### 2026-09-01 — EXP-11A cerrado

- EXP-11A 30/30 auditado, versionado e integrado.
- `main = 9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.
- HE2/HE5 permanecen pendientes.
- Se activa el `NEW_HISTORICAL_GATE`.
- Nueva data es necesaria para la próxima fase, pero todavía no se procesa.
- `data/Series - Descripciones.xlsx` permanece intacto.
- Siguiente hito: reconstrucción forense del pipeline histórico Excel→Python→v0.1→v0.2.
