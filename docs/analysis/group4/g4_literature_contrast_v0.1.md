# G4-F03 - Contraste con literatura y candidato de cierre de Grupo 4

## 1. Alcance y corpus congelado

Este artefacto posiciona los hallazgos aprobados de G4-F01 y la interpretacion controlada de G4-F02 frente al corpus editorial congelado. No recalcula metricas, no ejecuta inferencia, no reabre EXP12 y no modifica las decisiones `HE2 = SUPPORTED` y `HE5 = INCONCLUSIVE`.

Fuentes experimentales rectoras:

- `outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv` (`da0351cb523fc7f3b45a83e072765a07f809b7fe`);
- `outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json` (`cc5d85bad5d0a2610ffb086f99052fd344b6d8ab`);
- `docs/analysis/group4/g4_interpretation_synthesis_v0.1.md` (`129a67b15db429b86af059d61753b1942c8f243f`);
- `outputs/analysis/group4/g4_limitations_registry_v0.1.json` (`ae00b93431e912cb78a58344057d9bf7a51fcd47`).

Gobernanza editorial consultada en modo de solo lectura:

- `article/SOURCE_REGISTRY.md`;
- `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`.

Literatura congelada usada: `0B01`, `0B02`, `0B03A`, `0B03B`, `0B04A`, `0B04B`, `0B05A` y `0B05C`. No se realizo busqueda web, no se admitieron referencias nuevas y no se altero la rama editorial.

## 2. Reglas de comparabilidad

Cada contraste se clasifica como `DIRECTLY_COMPARABLE`, `PARTIALLY_COMPARABLE`, `QUALITATIVE_ONLY` o `NOT_DIRECTLY_COMPARABLE`. La comparacion directa requeriria alineacion de tarea, salida, nivel HS, definicion de metrica, denominador, protocolo, rechazo o fallback, particion y lectura estadistica. El corpus congelado no documenta una alineacion completa para comparar numericamente los resultados del proyecto con un estudio externo; por ello este registro no usa `DIRECTLY_COMPARABLE`.

Se preservan estas fronteras:

- Top-k retrieval no equivale a classification accuracy, weighted F1, MRR ni Hits@k.
- Ranking historico no equivale a deep search regulatorio.
- Precedent retrieval no equivale a normative evidence retrieval.
- RAG classification no equivale a RAG evidence support ni a customs QA RAG.
- Evidencia visible o citas no equivalen a auditabilidad formal ni a correccion juridica.
- Validez de restricciones o paths no equivale a correccion juridica independiente.
- Provenance y reproducibilidad no equivalen a auditabilidad por salida ni a correctness.

## 3. Matriz de contraste

| comparison_id | Hallazgo del proyecto | Literatura congelada | Clase | Frontera interpretativa |
|---|---|---|---|---|
| CMP-001 | HE2: el retrieval historico supera internamente a los tres brazos normativos corregidos en las cinco metricas primarias HE2_A | `0B01`, `0B02`, `0B04A` | `NOT_DIRECTLY_COMPARABLE` | Los trabajos externos usan datasets, tareas, niveles HS, metricas y protocolos heterogeneos; el resultado solo describe el benchmark interno congelado. |
| CMP-002 | El ranking historico produce candidatos y la evidencia normativa se recupera despues para explicar un Top-3 fijo | THE-RAG e ICCA-RAG en `0B03A` | `QUALITATIVE_ONLY` | THE-RAG usa evidencia en la decision del codigo e ICCA-RAG aborda soporte de evidencia en QA; ninguno habilita equivalencia numerica. |
| CMP-003 | El LLM local no clasifica desde cero, no introduce codigos y no reordena candidatos | sistemas agentic, jerarquicos, KG y constraint-aware de `0B03B` | `PARTIALLY_COMPARABLE` | Comparten componentes funcionales, pero difieren el contrato de decision y el rol del modelo. |
| CMP-004 | Separacion entre rendimiento de ranking, evidencia documental y explicacion controlada | Explainable Product Classification, Grainger e ICCA-RAG en `0B02` y `0B03A` | `QUALITATIVE_ONLY` | Explicacion, rationale, citas o faithfulness no prueban auditabilidad formal ni correccion juridica. |
| CMP-005 | Trazabilidad de artefactos y puente resultado-claim-evidencia | provenance, documentacion y reproducibilidad de `0B05A` | `PARTIALLY_COMPARABLE` | La procedencia y la reproducibilidad apoyan inspeccion, pero no certifican calidad, auditabilidad por salida ni correctness. |
| CMP-006 | Evidencia normativa posterior al ranking | autoridad, vigencia y trazabilidad normativa de `0B05C` | `QUALITATIVE_ONLY` | Fuente oficial, asociacion normativa y recuperacion documental no equivalen a suficiencia juridica ni clasificacion correcta. |
| CMP-007 | Particion y control de dependencia por DAM | reportes metodologicos congelados en `0B01` y `0B02` | `QUALITATIVE_ONLY` | La ausencia de un split equivalente documentado no demuestra leakage en antecedentes. |
| CMP-008 | EXP11A: sensibilidad conjunta de tamano y composicion | `0B04A`, `0B05A` | `NOT_DIRECTLY_COMPARABLE` | Es no causal y el corpus no ofrece un diseno alineado que permita aislar el efecto de tamano. |
| CMP-009 | EXP11B: H150/H200 descriptivo sobre diez pares de seeds observados | `0B04A`, `0B05A` | `NOT_DIRECTLY_COMPARABLE` | No existe base para inferencia a una superpoblacion de seeds ni para superioridad externa. |
| CMP-010 | 0B05C Attempt06: impacto dependiente del metodo | `0B05C` | `PARTIALLY_COMPARABLE` | Se comparan estados documentales internos; no se infiere causalidad, significancia ni impacto global cero. |
| CMP-011 | EXP12: cierre sin retrieval y efecto de diversidad no estimable | `0B05A` | `NOT_DIRECTLY_COMPARABLE` | No se encontro un diseno congelado conceptualmente alineado; no se infiere inviabilidad global ni evidencia sobre HE5. |

## 4. Contraste HE2 y retrieval

HE2 permanece `SUPPORTED` porque, dentro del benchmark congelado, el retrieval historico supero a los tres brazos normativos corregidos en las cinco metricas primarias HE2_A. Esta es una comparacion interna con poblaciones, protocolos y definiciones comunes al proyecto.

`0B01`, `0B02` y `0B04A` confirman que la literatura ya incluye clasificacion HS directa, semantic retrieval, sentence retrieval, precedent retrieval y evaluaciones Top-k. Esas familias hacen pertinente el contraste funcional, pero sus accuracies, F1, Top-k, Hits@k o MRR no son intercambiables con las metricas internas. No se formula superioridad numerica entre estudios y ningun componente aislado se presenta como novedad.

## 5. Contraste de arquitectura, RAG, LLM y agentes

`0B03A` y `0B03B` muestran que RAG, reglas, jerarquia, agentes, knowledge graphs, evidencia y rationale ya participan en sistemas relacionados. En THE-RAG y en varios esquemas agentic o constraint-aware, reglas o evidencia intervienen en la decision del codigo. ICCA-RAG se orienta a soporte de evidencia en QA, no al mismo contrato de clasificacion.

El piloto evaluado separa `ranking historico -> evidencia normativa posterior -> explicacion controlada del Top-3 fijo`. El LLM local no clasifica desde cero, no agrega codigos y no altera su orden. Esta es una diferencia funcional del contrato de componentes; no demuestra superioridad, exclusividad ni novedad absoluta.

## 6. Contraste de auditabilidad, trazabilidad y correctness

Los antecedentes congelados permiten hablar de evidencia visible, citas, rationale, faithfulness, provenance, transparency trails y documentacion reproducible. No permiten fusionar esos conceptos. El trabajo conserva por separado: rendimiento de ranking, asociacion documental, trazabilidad de artefactos y explicacion auditable.

Segun `0B02`, `0B03A`, `0B03B`, `0B05A` y `0B05C`, una explicacion visible no valida por si sola la clasificacion; la auditabilidad formal no establece correccion juridica; una fuente oficial no es necesariamente suficiente para un caso; y recuperar evidencia normativa no equivale a un ruling vinculante. El proyecto documenta esas fronteras sin afirmar legal correctness.

## 7. Contraste metodologico de dependencia y particion

El control por DAM responde a la estructura de observaciones relacionadas del proyecto y limita contaminacion entre particiones bajo su propio diseno. El corpus congelado no ofrece evidencia suficiente para atribuir leakage a un antecedente solo porque no documente un group split equivalente. La diferencia se registra como decision metodologica local, no como defecto probado de otros trabajos.

## 8. Sensibilidades y no-estimabilidad

- `EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL`: no identifica un efecto causal del tamano.
- `EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE`: describe diez pares observados y no una poblacion de seeds.
- `0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE`: EV03 tuvo cambio agregado cero, EV04 una disminucion MRR minima no nula y D1a cambio positivo no nulo de ranking exacto con efecto HS4 menor y mixto; el impacto conjunto es dependiente del metodo.
- `EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE`: no prueba inviabilidad matematica global y no aporta evidencia positiva ni negativa para HE5.

## 9. Categorias de contribucion

### TECHNICAL_CONTRIBUTION

Arquitectura funcional que desacopla ranking historico, recuperacion normativa posterior y explicacion controlada de un Top-3 fijo, con un LLM sin capacidad de introducir ni reordenar codigos.

### METHODOLOGICAL_CONTRIBUTION

Evaluacion que separa funciones, controla dependencia por DAM, delimita metricas y claims, conserva sensibilidades no causales y distingue resultados estimables, descriptivos y no estimables.

### TRACEABILITY_CONTRIBUTION

Puente versionado entre resultado, claim y evidencia; registro explicito de limitaciones; identidad de artefactos; y fronteras documentadas entre explicacion auditable, evidencia normativa y correccion juridica.

Estas categorias describen el trabajo dentro del corpus congelado. No constituyen una decision de novelty ni una redecision del gap editorial.

## 10. AUTHORIZED_DISCUSSION_POINTS

| discussion_id | project_claim_ids | literature_source_ids_or_paths | comparison_class | allowed_statement | mandatory_qualification | scientific_role |
|---|---|---|---|---|---|---|
| ADP-001 | HE2; G4-F01 | `0B01`; `0B02`; `0B04A` | `NOT_DIRECTLY_COMPARABLE` | El retrieval historico obtuvo mejor rendimiento interno que los brazos normativos corregidos. | Solo en el benchmark congelado; no comparar porcentajes externos. | METHODOLOGICAL |
| ADP-002 | C01; C02; C03 | `0B03A`; `0B03B`; `0B04B` | `QUALITATIVE_ONLY` | El piloto separa ranking, evidencia normativa y explicacion del Top-3 fijo. | Diferencia funcional, sin superioridad ni exclusividad. | TECHNICAL |
| ADP-003 | G3C-017; G3C-018 | `0B02`; `0B03A`; `0B03B` | `QUALITATIVE_ONLY` | Evidencia, rationale y citas tienen roles distinguibles de la auditabilidad formal. | Ninguno demuestra clasificacion correcta ni legal correctness. | TRACEABILITY |
| ADP-004 | G4-F02 | `0B05A`; `0B05C` | `PARTIALLY_COMPARABLE` | La procedencia y la identidad de artefactos mejoran la inspeccion de la cadena experimental. | No certifican calidad, suficiencia juridica ni correctness. | TRACEABILITY |
| ADP-005 | EXP11A | `0B04A`; `0B05A` | `NOT_DIRECTLY_COMPARABLE` | EXP11A documenta sensibilidad conjunta a tamano y composicion. | Es no causal y no aisla el efecto de tamano. | LIMITATION |
| ADP-006 | EXP11B | `0B04A`; `0B05A` | `NOT_DIRECTLY_COMPARABLE` | EXP11B describe H150/H200 sobre diez pares de seeds observados. | Sin inferencia a superpoblacion de seeds. | LIMITATION |
| ADP-007 | C21; C22; C23; C24; C25 | `0B05C` | `PARTIALLY_COMPARABLE` | El impacto correctivo 0B05C es dependiente del metodo. | No resumir como impacto global cero ni inferir causalidad o significancia. | LIMITATION |
| ADP-008 | EXP12 | `0B05A` | `NOT_DIRECTLY_COMPARABLE` | El efecto de diversidad de EXP12 quedo no estimable bajo su contrato congelado. | No implica inviabilidad global ni informa HE5. | LIMITATION |

## 11. FORBIDDEN_DISCUSSION_POINTS

| discussion_id | forbidden_statement |
|---|---|
| FDP-001 | Afirmar superioridad numerica frente a estudios con datasets, niveles HS, metricas o protocolos no comparables. |
| FDP-002 | Afirmar SOTA, mejor rendimiento de la literatura o equivalentes. |
| FDP-003 | Afirmar novelty absoluta, ser el primero, unicidad o un gap definitivo no gobernado. |
| FDP-004 | Atribuir a EXP11A un efecto causal de tamano. |
| FDP-005 | Generalizar EXP11B a una superpoblacion de seeds. |
| FDP-006 | Describir 0B05C como impacto global cero o sin impacto numerico. |
| FDP-007 | Convertir EXP12 en prueba de inviabilidad matematica global. |
| FDP-008 | Usar EXP12 como evidencia positiva o negativa para HE5. |
| FDP-009 | Derivar exactitud global del RAG desde el rendimiento del retrieval historico. |
| FDP-010 | Derivar correccion juridica desde evidencia normativa u oficialidad de la fuente. |
| FDP-011 | Tratar una explicacion auditable como validacion de la clasificacion. |
| FDP-012 | Atribuir leakage a antecedentes solo por ausencia de group split documentado. |
| FDP-013 | Equiparar path validity, constraints o rationale con correccion legal independiente. |
| FDP-014 | Equiparar provenance o reproducibilidad con auditabilidad por salida o correctness. |

## 12. Handoff a Grupo 5

Este documento y `outputs/audits/group4_closure_v0.1.json` forman un candidato pendiente de auditoria externa. Grupo 4 permanece `IN_PROGRESS`, `group4_closed = false` y G5-F01 permanece `PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED`. El handoff solo delimita material autorizado y prohibido para una etapa posterior; no redacta Discussion, Conclusions, articulo ni tesis, y no activa Grupo 5.
