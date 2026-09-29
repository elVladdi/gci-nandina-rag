# G7-F03 — Auditoría científica del artículo V036 y evaluación pre-FAST v0.1

```text
FICHA = G7-F03
ROLE = IA_EXPERIMENTAL / AUDITORA_METODOLOGICA
DATE = 2026-09-29

STATUS = REVISION_REQUIRED / EXECUTED / NOT_APPROVED
GROUP7 = IN_PROGRESS / NOT_CLOSED
GROUP8 = BLOCKED_BY_GROUP7

ARTICLE_MODIFIED = false
NEW_EXPERIMENT_EXECUTED = false
METRICS_RECOMPUTED = false
NEW_INFERENCE = false
NEW_CI = false
NEW_P_VALUE = false
EXP12_REOPENED = false
```

## 1. Alcance, autorización y baseline

Esta auditoría ejecuta la solicitud inter-rol abierta por D-194 y versionada en:

- `article/prompts/13_G7_F03_EXPERIMENTAL_ARTICLE_REVIEW_REQUEST_V01.md`
- Git blob: `5eabd0bc2ba114008d56028b6beb24c8fdd5ef1e`

Baseline editorial/científico auditado:

- `article/manuscript/ARTICLE_MASTER_V036.md`
- Git blob: `c9dcbcc376cdb121d30dc2408756a6c95b569a90`
- SHA-256 gobernado: `8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8`
- head editorial de solicitud: `952a56bb09c95bc7a93baec9b0a560889d253195`

El head editorial vivo posterior incorporó únicamente gobernanza pre-FAST/D-194 y no alteró el blob del master V036. El artículo no se modifica en esta ficha.

La activación experimental de G7-F03 quedó registrada separadamente en la rama de fichas y el Plan Maestro, reconciliando primero el cierre demostrado de G7-F02.

## 2. Drift check G7-F01 → V036

G7-F01 congeló el artículo en `2aad97aaceec0af6be0edb9ba0dd29170ad35baf`, con `ARTICLE_MASTER_V009` como master, Experimental Design aún en construcción y Results/Discussion/Conclusion no autorizados. El artículo de solicitud se encuentra 583 commits por delante de ese head congelado.

El cambio de SHA no constituye por sí solo drift científico adverso. El contenido incorporado desde G7-F01 materializó Experimental Design, Results, Discussion, Conclusion, Front Matter y parte de End Matter bajo gobernanza editorial propia.

Resultado del drift check:

```text
MATERIAL_SCIENTIFIC_DRIFT_CONTRADICTION = NO
MATERIAL_SCIENTIFIC_OMISSION = YES
OMISSION_SCOPE = DIAGNOSTIC_LLM_RERANKER_METHOD + RESULTS
```

La arquitectura principal se mantiene científicamente alineada con el freeze: ranking histórico → Top-3 fijo → asociación documental por candidato → contexto → explicación local; la evidencia normativa no rerankea y el LLM explicador no cambia candidatos.

## 3. Matriz de auditoría científica de V036

| ID | Sección/localización | Afirmación o dato auditado | Fuente gobernante | Resultado | Severidad | Acción requerida |
|---|---|---|---|---|---|---|
| G7F03-A01 | §3.1, §3.4–3.6, §4.5 | Separación de autoridad: historical ranking fija Top-3; evidencia normativa y explicación no alteran ranking | G7-F01 freeze; G4 guardrails; Phase-F | PASS | — | Ninguna |
| G7F03-A02 | §4.1–4.4, §5.1 | Benchmark interno offline Capítulo 87; SERIE como unidad; DAM como grupo de dependencia; EVAL 1,056 / 67 DAM / 42 NANDINA | G3 analytical contract / population registry | PASS | — | Ninguna |
| G7F03-A03 | §4.6–4.7, §5.2, §5.6 | HE2: 15 contrastes HE2_A con IC 99% y 1 contraste HE2_B con IC 95%; sin p-values | G3-F03/F04; G5-MAIN-01/02 | PASS | — | Ninguna |
| G7F03-A04 | §5.3, §6.1, §6.4, §7 | Asociación documental exacta 3,168/3,168; invariancia Top-3 1,056/1,056; no equivale a corrección normativa/jurídica | Phase-F; G4 guardrails | PASS | — | Ninguna |
| G7F03-A05 | §4.6.3, §5.4, §6.2/6.4/6.6 | HE4: preservación estructural 50/50, auditabilidad 28/50, LLM-as-judge; 0/50 schema como incompatibilidad prompt-schema, no falla sustantiva | Group1 HE4 J/K; G7-F01 freeze | PASS | — | Ninguna |
| G7F03-A06 | §4.7, §5.5, §6.6 | EXP11A no causal; EXP11B descriptivo sin inferencia a superpoblación de seeds; EXP12 cerrado sin retrieval/no estimable; HE5 inconclusa | G3-F04; G4; Group2B | PASS | — | Ninguna |
| G7F03-A07 | §4.8, §6.5–6.6 | Reproducibilidad pública declarada con limitaciones reales; no se afirma one-command fresh-clone reproduction | Group2B + snapshot público auditado | PASS | — | Recheck final antes de submission, como ya declara V036 |
| G7F03-A08 | V036 global | No se inventa disposición formal de HG o HE1 | G7-F01 freeze / Group1 no-assessment marker | PASS | — | Ninguna |
| G7F03-A09 | §3.1/3.4/3.6 y §4.5–4.7 | El artículo solo menciona que puede existir un reranking diagnóstico separado, pero no documenta el protocolo realmente ejecutado de 20 casos | Phase-G reranker run metadata `5daba1ed3f44b2d8906d40588dbe2fcec4bf0e4b` | REVISION_REQUIRED | MAJOR | Incorporar, mediante reapertura editorial controlada, el protocolo ejecutado: muestra diagnóstica de 20 casos, pool cerrado, 19 referencias dentro del pool y 1 fuera, LLM local, una ejecución por input, sin inferencia preespecificada y sin integración al flujo principal |
| G7F03-A10 | §5 Results / síntesis asociada | V036 omite los resultados del reranker diagnóstico ejecutado | `reranker_metrics_v0.2.json` blob `15800df93cf77f4f2c6e83ac6cb692be013bbeb3`; win/tie/loss blob `a4d508070d1ef61abbd09a34a7f0ba76f5013a2a` | REVISION_REQUIRED | MAJOR | Reportar como diagnóstico separado: Top-1 0.50→0.50; Top-3 0.65→0.65; Top-5 0.80→0.80; MRR 0.6326389→0.6326389; `wins/ties/losses = 0/19/0` para los 19 casos con referencia en pool; 1 caso fuera del pool; no afirmar mejora ni degradación ni significancia |
| G7F03-A11 | §6.6 / §7 | Corpus Decision-885-derived y drift respecto de Decision 906 correctamente limitados | G4 limitations + Attempt06 | PASS | — | Ninguna |
| G7F03-A12 | Abstract | Resume únicamente resultados principales y mantiene límites: no overall accuracy, legal correctness, human validation, transfer o deployment readiness | G3/G4/Group1 | PASS | — | No es necesario añadir el reranker al Abstract |

### Dictamen científico de la matriz

Los hallazgos A09 y A10 son dos caras de una misma deuda de sincronización post-tesis: el experimento diagnóstico de reranking fue ejecutado, cerrado y forma parte del estado científico final de HE3, pero V036 lo menciona solo como posibilidad/ruta separada y no documenta su método ni su resultado.

No se detectó necesidad de nuevo experimento, nueva métrica, nuevo intervalo, nuevo p-value ni reapertura de EXP12.

## 4. Disposición científica de las nueve presentaciones G5

La clasificación siguiente determina compatibilidad científica/destino recomendado; IA Gestora conserva la decisión editorial final de maquetación.

| Presentación G5 | Rol congelado | Disposición científica para artículo | Condición |
|---|---|---|---|
| G5-MAIN-01 — HE2_A primary early ranking | PRIMARY_INFERENTIAL | **CUERPO PRINCIPAL** | Mantener separados valores absolutos por brazo de la diferencia pareada y sus IC 99%; no crear IC por brazo |
| G5-MAIN-02 — HE2_B deep coverage | PRIMARY_INFERENTIAL | **CUERPO PRINCIPAL** | Único contraste confirmatorio Recall@200−Recall@100 con IC 95%; Pool@200 solo contexto |
| G5-SECONDARY-01 — Phase E descriptive coverage | DESCRIPTIVE_SUPPLEMENTARY | **SUPPLEMENTARY / APPENDIX** | Descriptivo, sin CI; no promover a evidencia confirmatoria |
| G5-SECONDARY-02 — HE5 descriptive components | DESCRIPTIVE_HE5 | **SUPPLEMENTARY / APPENDIX** | HE5 permanece INCONCLUSIVE; no inventar umbral de concentración/insuficiencia |
| G5-APPENDIX-01 — Top-50 supplementary uncertainty | SUPPLEMENTARY | **SUPPLEMENTARY / APPENDIX** | Fuera de las cinco métricas primarias HE2_A; sin rol decisional |
| G5-APPENDIX-02 — EXP11A size-composition sensitivity | DESCRIPTIVE_SENSITIVITY | **SUPPLEMENTARY / APPENDIX** | Sensibilidad conjunta tamaño-composición; no causal |
| G5-APPENDIX-03 — EXP11B H150/H200 sensitivity | DESCRIPTIVE_SENSITIVITY | **SUPPLEMENTARY / APPENDIX** | Diez pares observados; no inferencia a superpoblación de seeds |
| G5-APPENDIX-04 — Attempt06 corrective sensitivity | DESCRIPTIVE_CORRECTED_STATE | **SUPPLEMENTARY / APPENDIX** | Solo Attempt06 vigente; cambios dependientes del método |
| G5-APPENDIX-05 — Phase E diagnostic-union ceiling | DIAGNOSTIC | **SUPPLEMENTARY / APPENDIX** | Techo diagnóstico; no presentarlo como performance ordinario |

Ninguna de las nueve presentaciones necesita permanecer exclusivamente como soporte interno: todas fueron materializadas por G5-F02 para presentación científica, pero siete deben mantenerse fuera del cuerpo principal para preservar la jerarquía inferencial/descriptiva.

## 5. Disposición científica de las tres figuras G6

| Figura | Rol congelado | Disposición científica | Condición |
|---|---|---|---|
| G6-FIG-01 — HE2 primary evidence | PRIMARY_INFERENTIAL / MAIN | **CUERPO PRINCIPAL** | Mantener caption aprobado, 99% CI solo en diferencias HE2_A y 95% CI en contraste HE2_B; no duplicar la misma evidencia con tablas/prosa de forma que confunda estimandos |
| G6-FIG-02 — Phase E descriptive coverage | DESCRIPTIVE_SUPPLEMENTARY / SECONDARY | **SUPPLEMENTARY / APPENDIX** | No CI/p-values; variante 70/30 solo contexto; diagnostic union excluida del performance ordinario |
| G6-FIG-03 — EXP11A sensitivity | DESCRIPTIVE_SENSITIVITY / APPENDIX | **SUPPLEMENTARY / APPENDIX** | 31 corridas observadas; H100 n=1; tamaño y composición acoplados; no lectura causal/monotónica |

No se autoriza crear nuevas figuras de resultados en esta ficha.

## 6. Figura 1 arquitectónica pendiente

`Figure 1 placeholder — overall architecture and information flow` puede materializarse **sin nueva evidencia experimental** porque sería un esquema editorial de una arquitectura ya congelada, no una nueva visualización de resultados.

Condiciones científicas obligatorias:

1. el flujo principal debe ser exactamente: descripción/normalización → historical retrieval/ranking → Top-3 fijo → asociación documental específica por candidato → construcción de contexto → LLM local de explicación;
2. la etapa normativa no puede aparecer como fuente de reranking del flujo principal;
3. el LLM explicador no puede aparecer como clasificador ni como autoridad para cambiar Top-3;
4. la ruta de reranking diagnóstico, si se dibuja, debe ser lateral/separada y explícitamente `diagnostic only / not feeding main flow`;
5. no incluir métricas, efectos o claims nuevos;
6. la figura debe recibir revisión de fidelidad científica antes de integración editorial.

Cualquier figura adicional que visualice resultados no cubiertos por G6 requiere una nueva decisión científica de alcance y auditoría antes de integrarse. Una figura puramente editorial que reexprese arquitectura ya congelada no requiere nuevo experimento.

## 7. Evaluación científica del FAST_FINALIZATION_MODE

La secuencia propuesta es **científicamente segura con una condición previa obligatoria**:

```text
PRE-FAST SCIENTIFIC CORRECTION GATE
→ FINAL-F01 Scientific Presentation & Visual Structuring
→ FINAL-F02 End Matter & Reference Integrity
→ FINAL-F03 Submission Assembly & Final QA
```

### Corrección obligatoria antes de FINAL-F01

IA Gestora debe abrir una reapertura científica estrecha del artículo para incorporar A09 y A10. La corrección debe:

- añadir el método ejecutado del reranker diagnóstico en Methods/Experimental Design;
- añadir su resultado diagnóstico en Results;
- mantenerlo separado del main flow;
- no reinterpretar `0/19/0` como evidencia inferencial;
- no afirmar mejora, degradación, equivalencia estadística ni generalización;
- conservar HE3 como `SUPPORTED` según el estado experimental congelado;
- modificar Discussion/summary únicamente si es necesario para evitar contradicción con la nueva mención explícita.

Después de esa corrección, IA Experimental debe reauditar únicamente el alcance científico modificado antes del cierre terminal de G7-F03.

### Constraints obligatorios para FINAL-F01

- usar la disposición G5/G6 definida en este informe;
- no recalcular números ni redondeos desde fuentes secundarias;
- no generar CI, p-values, estimandos o summaries nuevos;
- preservar SERIE como unidad y DAM como cluster donde aplica;
- no convertir evidencia descriptiva/sensibilidad en confirmatoria;
- no duplicar tabla + figura + prosa de forma que cambie el rol epistemológico;
- cualquier nueva figura de resultados fuera de G6 requiere gate experimental;
- la Figura 1 arquitectónica es admisible bajo las condiciones de §6.

### Constraints obligatorios para FINAL-F02

- Data Availability y Code/Reproducibility deben describir exactamente el estado material al momento de submission;
- no afirmar reproducibilidad pública completa ni one-command fresh-clone mientras el paquete público siga incompleto;
- distinguir reproducibilidad interna auditada de disponibilidad pública;
- mantener visibles `DECLARED_NOT_RECOVERABLE` y `HASH_BOUND_LOCAL_ONLY` cuando su relevancia llegue al texto de disponibilidad;
- revalidar el HEAD del repositorio público inmediatamente antes de congelar la declaración final;
- las declaraciones CRediT, Funding, Competing interests y Acknowledgements son autor-owned y no pueden inferirse desde evidencia experimental.

### Constraints obligatorios para FINAL-F03

- QA bilingüe EN/ES sin deriva semántica de cifras, denominadores, inferencia o límites;
- cross-references y numeración no deben alterar el rol MAIN/SECONDARY/APPENDIX;
- comprobar que ninguna edición de estilo reintroduzca claims prohibidos: global RAG accuracy, legal correctness, human validation, causal size effect, seed-superpopulation inference, external performance transfer o EXP12 ejecutado;
- freeze final solo después del re-PASS experimental del bloque reranker corregido.

## 8. Estado formal de G7-F03 y condición de cierre

```text
G7_F03_EXECUTION_RESULT =
REVISION_REQUIRED / EXECUTED / NOT_APPROVED

G7_F03_TERMINAL_CLOSED = false
GROUP7_CLOSED = false
G8_F01_ELIGIBLE = false
```

G7-F03 **no está bloqueada por falta de fuentes**. La auditoría pudo completarse. Sin embargo, no puede recibir estado terminal `CLOSED / APPROVED` porque V036 conserva una omisión científica material y reparable: el protocolo y los resultados del reranker diagnóstico ejecutado.

Condición exacta para cierre posterior:

1. IA Gestora abre una corrección científica estrecha A09+A10 bajo gobernanza del artículo;
2. IA de Redacción materializa el candidato sin cambios fuera de alcance;
3. IA Gestora audita integridad editorial/técnica;
4. IA Experimental reaudita el contenido científico modificado contra los artefactos Phase-G congelados;
5. con `PASS`, IA Experimental integra/actualiza el closure record de Grupo 7 a `CLOSED / APPROVED`;
6. solo entonces G8-F01 se vuelve elegible.

## 9. Stop condition

La solicitud D-194 queda respondida con un dictamen G7-F03, matriz científica, disposición G5/G6, decisión sobre la figura arquitectónica y constraints pre-FAST. No se modifica el artículo y no se ejecuta ninguna tarea posterior.

---

## English terminal summary

G7-F03 was executed as an Experimental-AI scientific audit against the frozen evidence and ARTICLE_MASTER_V036. The result is `REVISION_REQUIRED / EXECUTED / NOT_APPROVED`. V036 is broadly consistent with the governed scientific state, but it omits the actually executed 20-case diagnostic LLM reranker protocol and its frozen no-change results. No new experiment or recomputation is required. The article must receive a narrowly governed Methods/Results correction and then a focused Experimental-AI re-audit before G7-F03 and Group 7 can close.
