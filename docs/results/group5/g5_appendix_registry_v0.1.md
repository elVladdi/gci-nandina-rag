# G5-F03 - Registro de anexos y suplementos

## Alcance y gobernanza

Este registro organiza evidencia ya congelada para el cierre documental candidato de Grupo 5. Estado: `CANDIDATE_PENDING_EXTERNAL_AUDIT`. G5-F03 no esta cerrado ni aprobado; Grupo 5 sigue `IN_PROGRESS`. G6-F01 permanece `PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED`. No se derivan metricas, intervalos ni inferencia; no se modifica el articulo ni la tesis.

La unidad de analisis es `SERIE`, con dependencia por `DAM / DECLARACION` cuando corresponde, en el benchmark `CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION`. Se preservan `HE2 = SUPPORTED` y `HE5 = INCONCLUSIVE` sin redecision.

## Fuentes y precedencia

- G5-F01: `docs/results/group5/g5_results_presentation_plan_v0.1.md` (`9eaf780f3a2f6c8579dc80867ed3a86e96683894`) y `outputs/results/group5/g5_table_registry_v0.1.json` (`4fe9318d52fad093066ff9f42d524fc95e436245`). Sus etiquetas historicas de auditoria pendiente no alteran el cierre operacional posterior de G5-F01.
- G5-F02 corregido e integrado: `docs/results/group5/g5_canonical_tables_v0.1.md` (`9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d`) y `outputs/results/group5/g5_numeric_crosscheck_v0.1.json` (`a28af8df10f6d6bb4fdb02458288b41e34e1dc78`) en `e471d4336ab965cd55b7f0e2ca7926445b1f0391`.
- Trazabilidad G3/G4: `outputs/analysis/group3/g3_metric_population_registry_v0.1.json`, `outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json` y `outputs/analysis/group4/g4_limitations_registry_v0.1.json`. Los mapeos congelados de 16 familias y 18 claims se conservan en el registro G5-F01; este documento no los reinterpreta.
- La version G5-F02 v01 (`9a8ca23ef607b5975b46a4336e033fc44ebe9453`) y los Attempts 03/04/05 de 0B-05C no son fuentes numericas vigentes. No se usan fuentes superseded.

## Criterio de inclusion

La ubicacion proviene del contrato G5-F01: hipotesis primaria en `MAIN`, contexto descriptivo en `SECONDARY`, sensibilidad y techo diagnostico en `APPENDIX`, limites no estimables en `TEXT_ONLY`, y guardrails en `NOT_PRESENTED_AS_RESULT_WITH_REASON`. Ninguna pieza se selecciona por favorabilidad. Los resultados negativos, nulos, mixtos, descriptivos y no estimables permanecen visibles con su rol original.

## Sistema completo de nueve tablas

| Presentacion | Destino y rol | CSV canonico congelado |
|---|---|---|
| G5-MAIN-01 | Principal, HE2_A inferencial | `outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv` |
| G5-MAIN-02 | Principal, HE2_B inferencial | `outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv` |
| G5-SECONDARY-01 | Secundaria, Phase E descriptivo | `outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv` |
| G5-SECONDARY-02 | Secundaria, HE5 descriptivo | `outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv` |
| G5-APPENDIX-01 | Anexo, Top-50 suplementario | `outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv` |
| G5-APPENDIX-02 | Anexo, EXP11A sensibilidad descriptiva | `outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv` |
| G5-APPENDIX-03 | Anexo, EXP11B sensibilidad descriptiva | `outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv` |
| G5-APPENDIX-04 | Anexo, 0B-05C Attempt06 correctivo | `outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv` |
| G5-APPENDIX-05 | Anexo, union Phase E diagnostica | `outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv` |

Los nueve CSV y sus conteos/roles estan registrados en el crosscheck G5-F02. Este registro no copia sus celdas ni crea tablas nuevas. G5-MAIN-01 conserva el CI del estimando pareado historico menos comparador, no de cada brazo; G5-MAIN-02 conserva el contraste de cobertura profunda. Phase E no adquiere rol confirmatorio.

## Catalogo de anexos

| ID | Vinculo controlado | Retencion y calificacion obligatoria |
|---|---|---|
| G5-APPENDIX-01 | `G3C-006`; tres familias HE2_A; `G5-MAIN-01` | Top-50 y su incertidumbre congelada son suplementarios, fuera de las cinco metricas primarias; no deciden HE2. Fuente: `outputs/analysis/group3/g3_inferential_results_v0.1.json`. |
| G5-APPENDIX-02 | `G3C-007`; `EXP11A_HISTORICAL_BANK_SENSITIVITY` | H25/H50/H75 y referencia H100 describen sensibilidad conjunta tamano/composicion; no identifican un efecto causal aislado ni monotonico del tamano. Fuentes: `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv` y `exp11_metrics_by_run.csv` del mismo directorio. |
| G5-APPENDIX-03 | `G3C-008`; `EXP11B_H150_H200_PAIRED_SENSITIVITY` | Diez pares de seeds observados H150/H200, descriptivos, sin inferencia a superpoblacion de seeds ni pseudorreplicacion de `10 x 1056` casos. Fuentes: `outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_condition_summary_v0.1.csv` y `exp11b_retrieval_metrics_by_bank_v0.1.csv` del mismo directorio. |
| G5-APPENDIX-04 | `G3C-009`; `0B05C_ATTEMPT06_CORRECTIVE_SENSITIVITY` | Solo Attempt06 corregido: EV03 `ZERO_AGGREGATE_CHANGE`; EV04 `TINY_NONZERO_MRR_DECREASE_ONLY`; D1a `POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT`; conjunto `METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`. Fuentes v0.5 EV03, EV04 y D1a identificadas en el registro JSON. No existe conclusion global de impacto cero. |
| G5-APPENDIX-05 | `HE2_B_PHASE_E_DIAGNOSTIC_UNION`; sin claim positivo | Union diagnostica Phase E como techo descriptivo, separada del rendimiento principal y de evidencia confirmatoria. Fuente: `outputs/evaluation/normative_candidate_pools_data_aduanas_clase87_v0.2/candidate_pool_metrics.json`. |

## Texto, guardrails y evidencia desfavorable

- `G5-TEXT-01` / `G3C-010`: EXP12 cerro sin condiciones oficiales ni retrieval. El efecto de diversidad es `NOT_ESTIMABLE`; no hay fila de rendimiento, comparador medido ni evidencia positiva o negativa para HE5.
- `G5-TEXT-02` / `G3C-011`: la calidad o prevalencia de descripciones ambiguas/incompletas HE5 es `NOT_ESTIMABLE`, no cero.
- `G5-SECONDARY-02` / `G3C-012`, `G3C-013`: proximidad jerarquica y soporte de precedentes historicos son `DESCRIPTIVE_ONLY`. Las filas `SAME_CHAPTER`, `SAME_HS4` y `SAME_HS6` conservan denominador vacio y conteos 147, 284 y 87; no hay umbral congelado de insuficiencia.
- `G5-TEXT-03` / `G3C-014`: validez interna y limites de evidencia/explicacion son limitaciones documentadas, no respaldo inferencial de HE5.
- `G5-TEXT-04` / `G3C-015`: ranking historico, recuperacion de evidencia normativa y explicacion controlada son funciones distintas.
- `G5-NOTRESULT-01..03` / `G3C-016..018`: no convertir superioridad de retrieval historico en exactitud global del RAG, evidencia normativa en correccion juridica vinculante, ni explicacion auditable en correccion clasificatoria o juridica. Son guardrails, no resultados numericos.

Estos destinos completan las 16 familias G3 y 18 claims G4 mediante los mapeos congelados de G5-F01. La evidencia nula EV03 y los cambios pequenos o mixtos EV04/D1a se mantienen juntos; no se oculta un componente por no favorecer una narrativa.

## Limitaciones y separacion de roles

Se conservan las 11 limitaciones no bloqueantes `G2B-L01..G2B-L11` del registro G4: entorno historico incompleto; runner EXP04-C historico irrecuperable; metadata EXP08 v0.1 irrecuperable; evaluacion LLM/AI no reproducible byte a byte; tamano/composicion acoplados en EXP11A; adquisicion NUEVA_02 atestiguada; bancos CSV/rankings EXP11B local-only y sujetos a hash/tamano; alcance del rerun externo de portabilidad EXP11B; pesos D1a local-only sujetos a hash/tamano; planning EXP12 fail-closed sin condiciones; y diagnostico forense EXP12 no gobernante. Tambien rigen el benchmark interno capitulo 87, el rol descriptivo HE5, el limite de inferencia EXP11B y la frontera arquitectonica de G4.

Los CSV G5-MAIN/SECONDARY/APPENDIX son presentaciones de resultados con sus roles congelados. `G5-APPENDIX-05` es diagnostico, no rendimiento confirmatorio. Los registros de auditoria, provenance, hashes, logs y diagnosticos forenses se retienen para trazabilidad, separados de metricas de rendimiento. Ningun status historico `CANDIDATE_PENDING_EXTERNAL_AUDIT` de la generacion G5-F01/F02 sustituye sus cierres operacionales posteriores.

## Handoff

Este es solo un candidato documental de cierre de Grupo 5 sujeto a auditoria externa independiente. No cierra G5-F03 ni Grupo 5. G6-F01 no esta autorizado ni ejecutado; cualquier activacion requiere un paso prospectivo separado.
