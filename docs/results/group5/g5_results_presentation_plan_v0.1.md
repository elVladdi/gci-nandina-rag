# G5-F01 - Arquitectura de presentacion de resultados

## 1. Alcance y estado de gobernanza

Este documento define la arquitectura de presentacion de resultados. No materializa tablas cientificas finales, no deriva valores, no recalcula metricas o incertidumbre y no redacta Results ni Discussion. El estado es `CANDIDATE_PENDING_EXTERNAL_AUDIT`; Grupo 5 permanece abierto y G5-F02 no esta autorizado.

Estado cientifico preservado: `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`, Grupo 4 `CLOSED / APPROVED`.

## 2. Fuentes congeladas y precedencia de verdad

La verdad operacional procede del Plan Maestro y del registro de fichas posteriores al cierre de Grupo 4. Los artefactos G3 y G4 integrados son fuentes cientificas inmutables; sus estados historicos de generacion no reabren fichas cerradas.

Fuentes rectoras: contrato analitico G3, registro de 548 filas y 16 familias G3, resultados inferenciales G3, disposicion de hipotesis, matriz de 18 claims G4-F01, sintesis y limitaciones G4-F02, y contraste/cierre G4-F03. Los blobs exactos se registran en `outputs/results/group5/g5_table_registry_v0.1.json`.

## 3. Principios de jerarquizacion no oportunista

La jerarquia se decide por hipotesis, objetivo y rol cientifico congelado, nunca por favorabilidad, magnitud, apariencia o conveniencia narrativa. Resultados nulos, mixtos, negativos, descriptivos y no estimables conservan un destino explicito. Las cinco metricas primarias HE2_A y el contraste primario HE2_B tienen prioridad por contrato; sensibilidad, diagnostico y limites se presentan con su rol aprobado.

## 4. Unidad, dependencia y alcance empirico

- Unidad de analisis: `SERIE`.
- Grupo de dependencia: `DAM / DECLARACION` cuando aplica.
- Alcance: `CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION`.
- EVAL: 1,056 series, 67 DAM y 42 NANDINA.

Los denominadores se obtendran de cada fuente congelada. Ninguna repeticion EXP11A ni par de seeds EXP11B se tratara como observacion inferencial independiente.

## 5. Mapa de familias experimentales

| Familia | Rol | Destino |
|---|---|---|
| HE2_A_HISTORICAL_VS_NORMATIVE_FLAT_ATTEMPT06 | Primario HE2_A | G5-MAIN-01 |
| HE2_A_HISTORICAL_VS_NORMATIVE_HIERARCHICAL_ATTEMPT06 | Primario HE2_A | G5-MAIN-01 |
| HE2_A_HISTORICAL_VS_D1A_ATTEMPT06 | Primario HE2_A | G5-MAIN-01 |
| HE2_B_HIERARCHICAL_DEEP_COVERAGE_ATTEMPT06 | Primario HE2_B | G5-MAIN-02 |
| HE2_B_PHASE_E_FROZEN_ROLE_POOLS | Descriptivo/suplementario | G5-SECONDARY-01 |
| HE2_B_PHASE_E_70_30 | Descriptivo/suplementario | G5-SECONDARY-01 |
| HE2_B_PHASE_E_DIAGNOSTIC_UNION | Diagnostico | G5-APPENDIX-05 |
| EXP11A_HISTORICAL_BANK_SENSITIVITY | Sensibilidad descriptiva no causal | G5-APPENDIX-02 |
| EXP11B_H150_H200_PAIRED_SENSITIVITY | Sensibilidad descriptiva | G5-APPENDIX-03 |
| 0B05C_ATTEMPT06_CORRECTIVE_SENSITIVITY | Sensibilidad correctiva | G5-APPENDIX-04 |
| HE5_AMBIGUOUS_INCOMPLETE_DESCRIPTIONS | No estimable | G5-TEXT-02 |
| HE5_HIERARCHICAL_PROXIMITY | Descriptivo HE5 | G5-SECONDARY-02 |
| HE5_INSUFFICIENT_HISTORICAL_PRECEDENTS | Descriptivo HE5 | G5-SECONDARY-02 |
| HE5_INTERNAL_EVALUATION_SCOPE | Limite de validez | G5-TEXT-03 |
| HE5_EXPLANATION_EVIDENCE_LIMITS | Diagnostico/limite | G5-TEXT-03 |
| EXP12_DIVERSITY | No estimable | G5-TEXT-01 |

La cobertura estructurada uno-a-uno, con filas y blobs fuente, esta en el registro JSON.

## 6. Tablas principales propuestas

### G5-MAIN-01 - Rendimiento temprano HE2_A

Estructura para H100 historico y los tres brazos normativos corregidos de Attempt06 en las cinco metricas primarias. Incluir denominador EVAL, unidad SERIE, agrupamiento DAM, estimacion observada y CI ya calculado G3-F03. Top-50 queda fuera de esta tabla por ser suplementario.

### G5-MAIN-02 - Cobertura profunda HE2_B

Estructura para Recall@100 frente a Recall@200 del brazo jerarquico corregido, con CI cluster-bootstrap ya calculado. Pool@200 se identifica como contexto y no como segundo contraste confirmatorio.

## 7. Tablas secundarias propuestas

### G5-SECONDARY-01 - Phase E descriptivo

Estructura para pools de roles congelados y mezcla 70/30 a profundidades 50/100/200. Se etiqueta `DESCRIPTIVE_ONLY`; no incluye CI ni decision inferencial.

### G5-SECONDARY-02 - Componentes descriptivos HE5

Estructura para proximidad jerarquica y buckets literales de soporte historico. No usa umbral de concentracion o insuficiencia que no haya sido congelado.

## 8. Anexos y suplementos propuestos

- `G5-APPENDIX-01`: incertidumbre suplementaria Top-50, sin rol decisorio HE2.
- `G5-APPENDIX-02`: EXP11A H25/H50/H75 y referencia H100, sensibilidad conjunta tamano/composicion no causal.
- `G5-APPENDIX-03`: EXP11B H150/H200 para diez pares de seeds observados, sin superpoblacion de seeds.
- `G5-APPENDIX-04`: sensibilidad correctiva 0B-05C usando exclusivamente Attempt06.
- `G5-APPENDIX-05`: union diagnostica Phase E como techo descriptivo, separada de rendimiento principal.

## 9. Resultados destinados solo a texto

- `G5-TEXT-01`: EXP12 cerrado sin retrieval; efecto de diversidad no estimable.
- `G5-TEXT-02`: calidad de descripcion HE5 no estimable, sin convertirla en cero.
- `G5-TEXT-03`: limite de validez interna y limites de evidencia/explicacion.
- `G5-TEXT-04`: separacion arquitectonica entre ranking, evidencia normativa y explicacion controlada.

## 10. Separacion entre resultados y diagnosticos

Las tablas MAIN y SECONDARY presentan resultados con roles primario o descriptivo aprobados. Los anexos de sensibilidad permanecen separados de la evidencia confirmatoria. La union diagnostica Phase E, auditorias, provenance y controles de trazabilidad no se presentaran como rendimiento. Los guardrails G3C-016, G3C-017 y G3C-018 no son resultados positivos.

## 11. Reglas de denominador, N, incertidumbre y version

Cada tabla materializada por G5-F02 debera declarar unidad, poblacion, denominador, DAM cuando aplique, rol de incertidumbre y blob fuente. Los CI se copiaran solo desde G3-F03; `DESCRIPTIVE_NO_CI_AUTHORIZED` no se convertira en CI; `NOT_ESTIMABLE` no se convertira en cero. Los 10 x 1,056 registros EXP11B no son observaciones independientes.

## 12. Tratamiento de HE2

HE2 permanece `SUPPORTED`. G5-MAIN-01 cubre las cinco metricas primarias HE2_A y G5-MAIN-02 el contraste primario HE2_B. Phase E y Top-50 conservan roles descriptivo/suplementario. La superioridad interna del retrieval historico no implica exactitud global del RAG.

## 13. Tratamiento de HE5

HE5 permanece `INCONCLUSIVE`. Los componentes jerarquico y de precedentes son descriptivos; calidad de descripcion es `NOT_ESTIMABLE`; la validez se limita al benchmark interno. Ninguna tabla transformara estos estados en apoyo o rechazo inferencial.

## 14. Tratamiento de EXP11A

EXP11A se presentara en anexo como sensibilidad conjunta de tamano y composicion. Las repeticiones describen variacion observada y no identifican un efecto causal aislado o monotonico del tamano.

## 15. Tratamiento de EXP11B

EXP11B se presentara en anexo como H150/H200 descriptivo sobre diez pares de seeds observados. Se mostrara la estructura pareada, sin inferencia a una superpoblacion de seeds ni independencia `10 x 1056`.

## 16. Tratamiento de Attempt06

Solo se usara Attempt06: EV03 `ZERO_AGGREGATE_CHANGE`, EV04 `TINY_NONZERO_MRR_DECREASE_ONLY`, D1a `POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT`, conjunto `METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`. Attempts 03/04/05 y lecturas supersedidas quedan prohibidos.

## 17. Tratamiento de EXP12

EXP12 sera `TEXT_ONLY_NOT_ESTIMABLE`: cerrado sin retrieval y efecto de diversidad no estimable. No tendra fila de rendimiento, cero, NA interpretable como medicion ni comparacion con H100/H150/H200.

## 18. Material que G5-F02 debera materializar

G5-F02 podra materializar solo las nueve estructuras con destino `MAIN_TABLE`, `SECONDARY_TABLE` o `APPENDIX_TABLE`, usando columnas, fuentes y cualificaciones congeladas en el JSON. Debera copiar valores ya aprobados sin recomputarlos y verificar blobs antes de llenar celdas.

## 19. Material que G5-F02 no debe materializar

No materializara EXP12 como rendimiento, guardrails como resultados, inferencia para EXP11A/EXP11B/HE5 descriptivo, metricas nuevas, fuentes supersedidas, rankings por conveniencia ni contenido del articulo. Los destinos `TEXT_ONLY` y `NOT_PRESENTED_AS_RESULT_WITH_REASON` no generan tablas numericas.

## 20. Guardrails contra cherry-picking y sobreclaim

- Cobertura obligatoria: 16/16 familias G3 y 18/18 claims G4.
- Seleccion por favorabilidad, efecto grande o conveniencia: prohibida.
- `HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY`.
- `NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS`.
- `AUDITABLE_EXPLANATION != CLASSIFICATION_CORRECTNESS`.
- `AUDITABLE_EXPLANATION != LEGAL_CORRECTNESS`.
- Las 11 limitaciones no bloqueantes de Grupo 2B permanecen vigentes.

Este plan no cierra G5-F01 ni Grupo 5. Su materializacion depende de auditoria externa, integracion posterior y autorizacion separada de G5-F02.
