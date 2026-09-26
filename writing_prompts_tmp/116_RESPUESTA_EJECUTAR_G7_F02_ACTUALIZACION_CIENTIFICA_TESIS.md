# PROMPT116 — Respuesta de ejecución G7-F02: actualización científica de la tesis

```text
PROMPT116_EXECUTION = COMPLETE
ACTOR = IA_DE_REDACCION_CIENTIFICA
G7_F02_INPUT_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
THESIS_BASELINE_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
APPROVED_PROJECT_SHA256 = 25506900d3110902455458b2291b15d78a7a1bf26e88fa76a2283755b2753421
V13_SHA256 = 8f5a1ec96eec91cee6970f4ec6e1bea3970322160b8d0a759aed5a02fef25067
SOURCE_FREEZE_PATH = docs/writing/group7/g7_writing_source_freeze_v0.1.json
SOURCE_FREEZE_STATUS = APPROVED
CANDIDATE_FILENAME = Molleapasa_gv_G7F02_CANDIDATE_V01.docx
CANDIDATE_SHA256 = e09b93a87378b7158736a3f3a18e72379b52b4cb14eadb445d0e2e0ba91dff8d
CANDIDATE_SIZE_BYTES = 4518781
BASELINE_FINAL_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
TRACEABILITY_FILENAME = g7_thesis_claim_traceability_v0.1.csv
TRACEABILITY_ROW_COUNT = 53
SECTIONS_MODIFIED = 3.1.3; 3.1.4/Table 1; 3.3-3.6; 3.7.4; 3.8.1/Table 9; 3.8.2-3.8.7; 4.1-4.3; CONCLUSIONES; RECOMENDACIONES terminology review; TOC/list-of-tables/list-of-figures synchronization
TABLES_UPDATED = 14 / five methodology tables updated in place + nine G5 canonical table presentations (G5-MAIN-01, G5-MAIN-02, G5-SECONDARY-01, G5-SECONDARY-02, G5-APPENDIX-01..05)
FIGURES_UPDATED = 3 / G6-FIG-01..03 scientific specifications and approved captions; embedded raster renderings reproduce the frozen data/specification, without asserting byte identity with the standalone G6 PNG ledger
NEW_SCIENTIFIC_SOURCES_COUNT = 0
NEW_METRICS_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_P_VALUE_COUNT = 0
EXP12_REOPENED = false
HG_DISPOSITION_INVENTED = false
HE1_DISPOSITION_INVENTED = false
G7_F02_CANDIDATE_STATUS = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

## 1. Gates de identidad

Los tres binarios autoritativos fueron recibidos y verificados antes de editar:

| Rol | SHA-256 esperado | SHA-256 observado | Tamaño observado | Estado |
|---|---|---|---:|---|
| Tesis baseline | `08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed` | mismo | 4,360,620 bytes | PASS |
| Proyecto aprobado | `25506900d3110902455458b2291b15d78a7a1bf26e88fa76a2283755b2753421` | mismo | 1,323,188 bytes | PASS |
| v13 auxiliar | `8f5a1ec96eec91cee6970f4ec6e1bea3970322160b8d0a759aed5a02fef25067` | mismo | 1,573,922 bytes | PASS |

El baseline volvió a verificarse al cierre y conserva exactamente su SHA-256 congelado. No fue sobrescrito.

## 2. Onboarding y fuente científica

Se siguió el onboarding obligatorio de Prompt116 y se aplicó el `g7_writing_source_freeze_v0.1` aprobado. Las formulaciones de problema, objetivos e hipótesis se conservaron conforme al proyecto aprobado. La tesis baseline se trató únicamente como base de corrección y no como ground truth científico.

La redacción científica se sincronizó con los artefactos congelados de G3-G6, Group1/Group2 y las fuentes de HE3/HE4 registradas en el source freeze. No se utilizó búsqueda web y no se incorporó bibliografía científica nueva.

## 3. Actualizaciones científicas materializadas

### Metodología

- Unidad de análisis: `SERIE`.
- Grupo de dependencia cuando corresponde: `DAM / DECLARACION`.
- Partición vigente: H100 = 2,950 series / 28 DAM; DEV = 100 / 6 DAM; EVAL = 1,056 / 67 DAM / 42 NANDINA; separación DAM-disjoint.
- HE2_A: 15 contrastes pareados `Historical - comparator`, CI marginales congelados de 99% con remuestreo por conglomerados DAM.
- HE2_B: un contraste `Recall@200 - Recall@100`, CI congelado de 95%.
- Top-50: incertidumbre suplementaria con CI de 95%, fuera de la familia primaria.
- No se calcularon p-values ni CI por brazo.
- HE4 conserva separados los controles estructurales y la rúbrica cualitativa; no se usa una puntuación normalizada 0-1 ajena al protocolo congelado.
- HE5 conserva descripción `NOT_ESTIMABLE`, proximidad jerárquica y soporte como `DESCRIPTIVE_ONLY`.

### Resultados y contrastación

Se sustituyeron los resultados legacy/provisionales por el estado congelado vigente:

```text
HG = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
```

Se materializaron las nueve fuentes tabulares de G5 en Tablas 10-18 y las tres figuras científicas G6 en Figuras 3-5, con captions aprobados y guardrails de alcance. En las tablas extensas de sensibilidad se emplean las filas canónicas necesarias para la presentación (resúmenes congelados o filas representativas explícitamente identificadas), sin calcular agregados nuevos.

HE3 quedó sincronizada con la invariancia 1,056/1,056 del ranking histórico, la trazabilidad 3,168/3,168 de los slots Top-3 y la evaluación diagnóstica del reranker sobre 20 casos. HE4 quedó sincronizada con 50/50 controles estructurales, 28/50 fichas auditables bajo el protocolo cualitativo y las limitaciones `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `EVALUATOR_MODALITY_DEVIATION`.

EXP11A se presenta como sensibilidad conjunta tamaño-composición no causal; EXP11B como diez pares observados sin inferencia a una superpoblación de semillas; EXP12 se mantiene `CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE`.

## 4. Guardrails verificados

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
EXP11A != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
ATTEMPT06 != GLOBAL_ZERO_IMPACT
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
```

La coherencia final comprobó además que no permanecieran como estado vigente la partición `3,000/100/1,006`, las métricas históricas legacy `0.8628/0.9062`, el score HE4 legacy `0.9520`, la degradación legacy del reranker, ni disposiciones soportada/rechazada fabricadas para HG o HE1.

## 5. QA del candidato Word

```text
DOCX_ZIP_INTEGRITY = PASS
RENDER_PAGE_COUNT = 97
VISUAL_PAGE_REVIEW = PASS
ACCESSIBILITY_AUDIT_HIGH = 0
ACCESSIBILITY_AUDIT_MEDIUM = 0
ACCESSIBILITY_AUDIT_LOW = 0
BASELINE_BYTE_IDENTITY_PRESERVED = true
INTERNAL_CROSS_REFERENCE_AND_LIST_SYNCHRONIZATION = PASS
```

El DOCX fue editado sobre el baseline, no reconstruido desde cero. Se preservaron la portada, estructura institucional, estilos, encabezados/pies, referencias bibliográficas y elementos no afectados. La actualización redujo el documento a 97 páginas renderizadas porque retiró resultados, figuras y tablas superseded de la versión legacy y los sustituyó por el conjunto vigente autorizado.

## 6. Trazabilidad

`g7_thesis_claim_traceability_v0.1.csv` contiene 53 filas, una por claim o cambio científico material trazado. Cada fila incluye sección/localizador, tipo de cambio, resumen baseline/candidato, binding de hipótesis, path y blob de fuente científica, ID de tabla/figura canónica cuando aplica, limitación de alcance, control de interpretación prohibida y estado.

No se añadió el Word candidato a Git. Los dos outputs sustantivos permanecen como entregables externos para auditoría independiente.

## 7. Estado terminal

```text
PROMPT116_EXECUTION = COMPLETE
G7_F02_CANDIDATE_STATUS = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
```

No se modificaron `main`, Plan Maestro, fichas, artículo, proyecto aprobado ni v13.