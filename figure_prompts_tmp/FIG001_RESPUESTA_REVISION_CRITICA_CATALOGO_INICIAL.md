# FIG001 — Respuesta oficial: revisión crítica del catálogo inicial de figuras

## 0. Alcance de esta ejecución

Se ejecutó exclusivamente `FIG001_REVISION_CRITICA_CATALOGO_INICIAL.md` con fuente en el commit `b47fee61a58b345d6ca1e48058f97704b2b2244e`.

Para esta revisión, `Prompt103` se trató únicamente como fuente histórica de requisitos científicos y visuales:

```text
SUPERSEDED / DO_NOT_EXECUTE_AS_CODEX_PROMPT
```

No se ejecutó su flujo operativo. No se modificaron `main`, Plan Maestro, fichas, artículo ni tesis. No se generaron imágenes ni scripts y no se recalcularon métricas, deltas científicos, intervalos, inferencia ni p-values.

Se preserva íntegramente el contrato científico:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42

HE2 = SUPPORTED
HE5 = INCONCLUSIVE

EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
0B05C = ATTEMPT06_CORRECTED_CURRENT_STATE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

También permanecen vigentes los guardrails que impiden equiparar superioridad del retrieval histórico con exactitud global del RAG, evidencia normativa con corrección jurídica vinculante, o explicación auditable con corrección clasificatoria o jurídica.

## 1. Fuentes verificadas

Se consultaron directamente en GitHub las fuentes exigidas por FIG001 y las nueve tablas canónicas de Grupo 5.

### 1.1 Fuentes rectoras

| Fuente | Blob verificado | Uso en FIG001 |
|---|---|---|
| `docs/results/group5/g5_results_presentation_plan_v0.1.md` | `9eaf780f3a2f6c8579dc80867ed3a86e96683894` | Jerarquía científica y destinos de resultados |
| `outputs/results/group5/g5_table_registry_v0.1.json` | `4fe9318d52fad093066ff9f42d524fc95e436245` | Roles, claims, denominadores y restricciones de incertidumbre |
| `docs/results/group5/g5_canonical_tables_v0.1.md` | `9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d` | Lectura consolidada de las tablas canónicas |
| `outputs/results/group5/g5_numeric_crosscheck_v0.1.json` | `a28af8df10f6d6bb4fdb02458288b41e34e1dc78` | Identidad de fuente verificada; el conector no devolvió payload textual utilizable en esta sesión, por lo que no se extrajo de este artefacto ninguna afirmación sustantiva |
| `docs/results/group5/g5_appendix_registry_v0.1.md` | `9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a` | Roles de suplementos, sensibilidad y diagnósticos |
| `outputs/audits/group5_closure_v0.1.json` | `1ba0cf7a4423ca9505d051f4ec54d28ae3ace1cf` | Trazabilidad del cierre candidato y registro de fuentes |
| `outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json` | `cc5d85bad5d0a2610ffb086f99052fd344b6d8ab` | Claims controlados y fuerza permitida |
| `outputs/analysis/group4/g4_limitations_registry_v0.1.json` | `ae00b93431e912cb78a58344057d9bf7a51fcd47` | Límites de interpretación y diseño |

La imposibilidad de obtener contenido textual del `g5_numeric_crosscheck_v0.1.json` no se suplió con conocimiento general. La revisión numérica relevante se apoyó directamente en los nueve CSV canónicos, todos verificables en GitHub.

### 1.2 Tablas canónicas verificadas

| Presentación | Blob |
|---|---|
| `g5_main_01_he2a_primary_early_ranking.csv` | `cb68583ee2260e4455796bac99ad90995ca7ef92` |
| `g5_main_02_he2b_deep_coverage.csv` | `359e4e19b5ef1d44983c03039162209293b2a44c` |
| `g5_secondary_01_phase_e_descriptive.csv` | `fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61` |
| `g5_secondary_02_he5_descriptive_components.csv` | `727076a0d09735a87f45f6522d2a0ecead2cee17` |
| `g5_appendix_01_top50_supplementary.csv` | `c2ded734af9ea340d715483b6e8cc00a7536dfea` |
| `g5_appendix_02_exp11a_size_composition_sensitivity.csv` | `cf3aedab5935d6af9b3ac7be7b51b954fcb9c403` |
| `g5_appendix_03_exp11b_h150_h200_sensitivity.csv` | `76c8c6c588c7e809c6be64f7192f497c491fb692` |
| `g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv` | `490ef570fa1674e2eecad7f0a3cdf34ba96204db` |
| `g5_appendix_05_phase_e_diagnostic_union.csv` | `f43cce08d1d7bc3cef64698dbebf14eae4b26ed5` |

---

# A. Evaluación crítica de las seis figuras iniciales

## A.1 G6-FIG-01 — HE2_A: desempeño absoluto y contrastes pareados primarios

**DICTAMEN:** `MODIFY + MERGE_WITH_G6-FIG-02`

**Razón científica.** Es la visualización con mayor prioridad del catálogo original porque comunica los claims primarios `G3C-001`, `G3C-002` y `G3C-003`. La tabla canónica contiene tres comparaciones por cinco métricas primarias y distingue correctamente entre los valores absolutos observados y el estimando pareado `historical - comparator`. Los CI de 99% pertenecen exclusivamente a ese estimando pareado. Por tanto, existe suficiente densidad científica para justificar una figura principal.

**Razón visual.** La tabla de 15 filas es precisa para lectura numérica, pero no permite reconocer con la misma rapidez la magnitud relativa del desempeño histórico frente a Flat Attempt06, Hierarchical Attempt06 y D1a Attempt06 ni la consistencia de los contrastes pareados entre las cinco métricas. Una figura aporta comprensión real si conserva la separación semántica entre valores absolutos e incertidumbre del contraste.

**Riesgo principal.** El mayor riesgo es vincular visualmente los CI de 99% a los brazos absolutos en vez de al contraste pareado. También debe impedirse que Top-1, Top-3, Top-5, Top-10 y MRR@100 se dibujen como una trayectoria continua de una misma variable: MRR no es una profundidad adicional. Finalmente, la superioridad del retrieval histórico dentro del benchmark no puede presentarse como exactitud global del RAG.

**Fuentes relevantes.** `g5_main_01_he2a_primary_early_ranking.csv`; `g5_table_registry_v0.1.json`; `g4_result_claim_evidence_matrix_v0.1.json`.

**Conclusión.** Debe conservarse como núcleo de la figura principal, pero no necesita quedar aislada de HE2_B si la fusión mantiene explícitamente distintos estimandos y niveles de incertidumbre.

---

## A.2 G6-FIG-02 — HE2_B: cobertura profunda

**DICTAMEN:** `MERGE_WITH_G6-FIG-01`

**Razón científica.** `G3C-004` es evidencia primaria de HE2 y debe permanecer visible. El contraste congelado es Recall@200 menos Recall@100, con un único CI cluster-bootstrap de 95%; `Pool@200 context` no constituye un segundo contraste confirmatorio.

**Razón visual.** Como figura autónoma, la fuente contiene esencialmente dos valores absolutos y un único estimando pareado. La tabla canónica tiene una sola fila. Convertir esa fila en una figura independiente añade poco contenido visual y fragmenta innecesariamente la evidencia primaria de HE2.

**Riesgo principal.** Una figura autónoma puede conferir a un único contraste un peso visual desproporcionado o duplicar `Pool@200` como si fuese una segunda evidencia confirmatoria. También existe riesgo de confundir su CI de 95% con los CI de 99% de HE2_A.

**Fuentes relevantes.** `g5_main_02_he2b_deep_coverage.csv`; `g5_table_registry_v0.1.json`; `g4_result_claim_evidence_matrix_v0.1.json`.

**Conclusión.** Debe conservarse científicamente, pero integrado en la figura principal de HE2 y con separación inequívoca respecto de HE2_A.

---

## A.3 G6-FIG-03 — Phase E: cobertura descriptiva por profundidad

**DICTAMEN:** `KEEP + MODIFY`

**Razón científica.** `G3C-005` es descriptivo y no confirmatorio. La tabla conserva cobertura exact-NANDINA a profundidades 50, 100 y 200 para variantes de Phase E, sin CI autorizado. Su rol complementa HE2_B sin redecidirlo.

**Razón visual.** Aquí existe una relación que una figura transmite mejor que una tabla: la evolución de la cobertura al aumentar la profundidad y las zonas de solapamiento o divergencia entre variantes. En la tabla canónica, las diferencias son muy pequeñas a 50/100 y se vuelven más visibles a 200; esa estructura comparativa sí justifica una visualización secundaria.

**Riesgo principal.** Existe una ambigüedad de trazabilidad que debe resolverse antes del diseño: el claim `G3C-005` refiere específicamente a cuatro variantes `A_historical_defined`, mientras que la tabla canónica materializa cinco variantes, incluyendo `dual_only`. No se debe presentar a las cinco como si todas constituyeran por igual la evidencia formal de `G3C-005`, pero tampoco debe omitirse una variante de la tabla por conveniencia o favorabilidad. También debe evitarse cualquier CI, p-value o interpretación confirmatoria.

**Fuentes relevantes.** `g5_secondary_01_phase_e_descriptive.csv`; `g5_table_registry_v0.1.json`; `g4_result_claim_evidence_matrix_v0.1.json`.

**Conclusión.** Merece una figura secundaria, con la trazabilidad entre las cuatro variantes del claim y la quinta variante descriptiva resuelta explícitamente en la futura especificación.

---

## A.4 G6-FIG-04 — EXP11A: sensibilidad conjunta tamaño/composición

**DICTAMEN:** `KEEP + MODIFY + MOVE_TO_APPENDIX`

**Razón científica.** `G3C-007` define EXP11A como sensibilidad conjunta de tamaño y composición, no como experimento causal de tamaño. La fuente contiene múltiples corridas observadas para H25/H50/H75, referencia H100 y summaries ya congelados. La variabilidad entre corridas forma parte de la evidencia descriptiva que debe permanecer visible.

**Razón visual.** La tabla canónica es extensa y combina condición, corrida/seed, composición del banco y seis métricas. Una figura puede mostrar de manera mucho más eficiente la variación observada dentro y entre condiciones, siempre que no colapse la información composicional ni sugiera una tendencia causal.

**Riesgo principal.** El eje H25-H50-H75-H100 puede inducir una lectura de dosis-respuesta o un efecto monotónico de tamaño que el diseño no identifica. El riesgo aumenta porque H50 contiene corridas con composiciones diferenciadas D1/D2 y las condiciones presentan diferencias en DAM, HHI y cobertura. Ocultar esa heterogeneidad bajo una sola categoría visual H50 sería científicamente empobrecedor. No se autorizan regresiones, bandas, nuevos promedios ni nuevos intervalos.

**Fuentes relevantes.** `g5_appendix_02_exp11a_size_composition_sensitivity.csv`; `g5_appendix_registry_v0.1.md`; `g4_limitations_registry_v0.1.json`; `g4_result_claim_evidence_matrix_v0.1.json`.

**Conclusión.** Es una buena figura de anexo porque aporta comprensión que la tabla no ofrece de forma inmediata, pero la futura especificación debe conservar explícitamente el acoplamiento tamaño/composición.

---

## A.5 G6-FIG-05 — EXP11B: comparación pareada H150/H200 por seeds observados

**DICTAMEN:** `TABLE_ONLY + REMOVE_AS_FIGURE`

**Razón científica.** `G3C-008` limita EXP11B a una sensibilidad descriptiva sobre diez pares de seeds observados, sin inferencia a una superpoblación de seeds y sin tratar `10 × 1056` como observaciones independientes. Los resultados H150/H200 son pequeños y mixtos entre métricas y pares.

**Razón visual.** Con el eje íntegro 0-1 exigible para tasas y MRR absolutos, muchas conexiones H150-H200 resultarían casi horizontales y difíciles de interpretar. Para hacer visualmente prominentes las diferencias sería necesario acortar fuertemente el eje o representar deltas; la primera alternativa magnificaría cambios pequeños y la segunda introduciría transformaciones numéricas no autorizadas como nuevos resultados. La tabla pareada conserva mejor los valores exactos y el identificador de seed sin exagerarlos.

**Riesgo principal.** Magnificación visual de cambios pequeños, inferencia implícita a una población de seeds, o pseudorreplicación de `10 × 1056` casos.

**Fuentes relevantes.** `g5_appendix_03_exp11b_h150_h200_sensitivity.csv`; `g5_appendix_registry_v0.1.md`; `g4_limitations_registry_v0.1.json`; `g4_result_claim_evidence_matrix_v0.1.json`.

**Conclusión.** Debe permanecer como tabla de sensibilidad descriptiva y no convertirse en figura independiente.

---

## A.6 G6-FIG-06 — HE5: componentes descriptivos

**DICTAMEN:** `TABLE_ONLY + REMOVE_AS_FIGURE`

**Razón científica.** HE5 permanece `INCONCLUSIVE`. `G3C-012` establece que las categorías de proximidad jerárquica son descriptivas y no autorizan afirmar concentración de errores; `G3C-013` conserva los buckets literales 1 DAM, 2 DAM, 3-4 DAM y 5+ DAM sin umbral congelado de insuficiencia.

**Razón visual.** El primer componente contiene conteos `SAME_CHAPTER = 147`, `SAME_HS4 = 284` y `SAME_HS6 = 87`, pero la fuente no materializa denominadores. Una gráfica de barras convertiría inevitablemente la diferencia de alturas en el principal mensaje perceptual y favorecería una lectura de “concentración” que el claim prohíbe. En el segundo componente, los denominadores son muy desiguales (`27`, `21`, `425`, `583`) y los valores Top-1/Top-3/MRR no siguen una secuencia monotónica. La tabla permite mantener visibles esos denominadores y valores sin imponer una narrativa visual de umbral o causalidad.

**Riesgo principal.** Sobreinterpretar conteos sin denominador como concentración de errores; sugerir que mayor o menor soporte DAM causa el desempeño; inventar un umbral de insuficiencia; o dar a HE5 un peso perceptual incompatible con su estado `INCONCLUSIVE`.

**Fuentes relevantes.** `g5_secondary_02_he5_descriptive_components.csv`; `g5_table_registry_v0.1.json`; `g4_result_claim_evidence_matrix_v0.1.json`; `g4_limitations_registry_v0.1.json`.

**Conclusión.** Debe mantenerse como tabla descriptiva acompañada de texto de interpretación limitada, no como figura.

---

# B. Decisión consolidada

| Figura inicial | Decisión consolidada | Destino propuesto |
|---|---|---|
| `G6-FIG-01` HE2_A | `MODIFY` + conservar como núcleo | Figura principal |
| `G6-FIG-02` HE2_B | `MERGE` con HE2_A | Integrada en la figura principal |
| `G6-FIG-03` Phase E | `KEEP + MODIFY` | Figura secundaria |
| `G6-FIG-04` EXP11A | `KEEP + MODIFY + MOVE_TO_APPENDIX` | Figura de anexo |
| `G6-FIG-05` EXP11B | `TABLE_ONLY + REMOVE_AS_FIGURE` | Tabla de anexo |
| `G6-FIG-06` HE5 | `TABLE_ONLY + REMOVE_AS_FIGURE` | Tabla secundaria + texto |

No se recomienda dividir ninguna figura en esta etapa. Tampoco se recomienda crear figuras sustitutas para ocupar los espacios dejados por G6-FIG-05 y G6-FIG-06. La reducción de seis a tres figuras se basa en utilidad visual y rol científico, no en favorabilidad de los resultados.

---

# C. Catálogo final preliminar recomendado

## G6-FIG-01 — Evidencia primaria de HE2: ranking temprano y cobertura profunda

- **Contenido:** evidencia primaria HE2_A del retrieval histórico frente a Flat Attempt06, Hierarchical Attempt06 y D1a Attempt06 en las cinco métricas congeladas, junto con el contraste primario HE2_B Recall@100 frente a Recall@200.
- **Rol científico:** `PRIMARY_INFERENTIAL`.
- **Destino:** `principal`.
- **Fuentes canónicas:**
  - `outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv`
  - `outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv`
- **Claims asociados:** `G3C-001`, `G3C-002`, `G3C-003`, `G3C-004`.
- **Justificación de figura:** reúne la evidencia que determina el apoyo a HE2 y permite percibir patrones comparativos que las dos tablas presentan de forma fragmentada. La fusión elimina una figura autónoma de una sola fila sin eliminar evidencia. En FIG002 deberá preservarse la separación entre los estimandos y entre CI 99% de HE2_A y CI 95% de HE2_B.

## G6-FIG-02 — Cobertura exacta NANDINA de Phase E según profundidad y variante

- **Contenido:** cobertura exact-NANDINA a profundidades 50, 100 y 200 para las variantes canónicas de Phase E, con rol estrictamente descriptivo.
- **Rol científico:** `DESCRIPTIVE_SUPPLEMENTARY`.
- **Destino:** `secundaria`.
- **Fuente canónica:** `outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv`.
- **Claim asociado:** `G3C-005`.
- **Justificación de figura:** la relación entre profundidad y cobertura, y los solapamientos/divergencias entre variantes, constituyen una estructura visual genuina que se aprecia peor en una tabla de quince filas. No se autoriza CI ni interpretación confirmatoria.

## G6-FIG-03 — Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A)

- **Contenido:** variación observada de las seis métricas congeladas en H25/H50/H75 y referencia H100, preservando la heterogeneidad de las corridas y la información de composición disponible.
- **Rol científico:** `DESCRIPTIVE_SENSITIVITY / NONCAUSAL`.
- **Destino:** `anexo`.
- **Fuente canónica:** `outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv`.
- **Claim asociado:** `G3C-007`.
- **Justificación de figura:** la cantidad de corridas y la heterogeneidad entre ellas hacen que la dispersión y sensibilidad sean más comprensibles visualmente que mediante la tabla extensa. La figura solo es válida si evita sugerir un efecto causal aislado o monotónico del tamaño.

**Número preliminar recomendado de figuras de resultados: 3.**

Este número no se considera todavía una especificación gráfica final; es el resultado de la auditoría conceptual de necesidad y utilidad visual de FIG001.

---

# D. Material que NO debe convertirse en figura

## D.1 EXP11B H150/H200 — tabla únicamente

**Disposición:** `TABLE_ONLY_DESCRIPTIVE_SENSITIVITY`.

La tabla `g5_appendix_03_exp11b_h150_h200_sensitivity.csv` conserva de forma exacta los diez pares observados, las seis métricas y los summaries congelados. Una figura independiente aporta poco bajo ejes íntegros y aumenta el riesgo de magnificar cambios pequeños o sugerir inferencia entre seeds.

## D.2 Componentes HE5 — tabla + texto únicamente

**Disposición:** `TABLE_ONLY_HE5_DESCRIPTIVE`.

La tabla `g5_secondary_02_he5_descriptive_components.csv` debe conservar los conteos jerárquicos con denominador no materializado y los cuatro buckets literales de soporte con sus denominadores muy desiguales. No debe generarse una figura que sugiera concentración, umbral de insuficiencia, monotonicidad o causalidad. HE5 permanece `INCONCLUSIVE`.

## D.3 Top-50 suplementario — tabla únicamente

**Disposición:** `TABLE_ONLY_SUPPLEMENTARY`.

`g5_appendix_01_top50_supplementary.csv` conserva incertidumbre suplementaria fuera de las cinco métricas primarias de HE2_A. Una figura separada duplicaría la narrativa de la figura principal y elevaría indebidamente el peso de una métrica sin rol en la decisión HE2.

## D.4 0B-05C Attempt06 correctivo — tabla únicamente

**Disposición:** `TABLE_ONLY_CORRECTIVE_SENSITIVITY`.

`g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv` contiene magnitudes de escalas muy distintas y semántica method-dependent: EV03 `ZERO_AGGREGATE_CHANGE`, EV04 `TINY_NONZERO_MRR_DECREASE_ONLY` y D1a `POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT`. Una figura de deltas podría sobrerrepresentar los componentes minúsculos o mezclar escalas incompatibles. Solo Attempt06 es vigente.

## D.5 Phase E diagnostic union — tabla únicamente

**Disposición:** `TABLE_ONLY_DIAGNOSTIC`.

`g5_appendix_05_phase_e_diagnostic_union.csv` representa un techo diagnóstico descriptivo, no rendimiento confirmatorio. No debe incorporarse como una curva adicional de rendimiento a la figura Phase E.

## D.6 EXP12 — texto únicamente

**Disposición:** `TEXT_ONLY_NOT_ESTIMABLE / NO_PERFORMANCE_FIGURE`.

EXP12 cerró sin retrieval para condiciones de diversidad y su efecto es `NOT_ESTIMABLE`. No existe resultado de rendimiento que pueda representarse gráficamente y no debe reabrirse.

## D.7 Otros límites y guardrails — texto, no figuras de resultados

Permanecen fuera del catálogo de figuras de resultados:

- prevalencia de descripciones ambiguas/incompletas: `NOT_ESTIMABLE`;
- límite de validez interna del benchmark;
- límites de evidencia normativa y explicación;
- separación funcional entre ranking histórico, recuperación normativa y explicación controlada;
- guardrails `G3C-016`, `G3C-017` y `G3C-018`.

Su función es limitar la interpretación, no constituir resultados gráficos.

---

# E. Riesgos pendientes antes de especificar visualmente la primera figura

1. **Complejidad de la fusión HE2_A + HE2_B.** La fusión es recomendada a nivel de catálogo, pero FIG002 deberá comprobar que la figura principal no resulte sobrecargada y que HE2_A/HE2_B permanezcan semánticamente separados. En particular, los CI 99% de HE2_A y el CI 95% de HE2_B no pueden presentarse como si compartieran el mismo contrato de incertidumbre.

2. **Trazabilidad de Phase E: cuatro variantes del claim frente a cinco filas de variante en la tabla.** `G3C-005` refiere a cuatro variantes `A_historical_defined`; la tabla canónica contiene además `dual_only`. Antes de diseñar G6-FIG-02 debe fijarse qué variantes constituyen formalmente el claim y cómo se mostrará cualquier variante contextual adicional sin cherry-picking ni ampliación del claim.

3. **Representación de composición en EXP11A.** H25/H50/H75/H100 no son niveles intercambiables de un único factor causal. La futura figura debe preservar de algún modo la composición observada, especialmente la heterogeneidad D1/D2 en H50, sin derivar indicadores nuevos ni introducir una codificación que sugiera causalidad de tamaño.

4. **Deduplicación del historical en HE2_A.** El valor histórico se repite por comparador en la tabla primaria. Cualquier deduplicación futura solo será de presentación y deberá condicionarse a identidad exacta; nunca a promedio o agregación.

5. **Unidades y métricas heterogéneas.** MRR y Top-k comparten rango 0-1 pero no la misma interpretación. FIG002 deberá evitar una codificación que transforme las cinco métricas HE2_A en una secuencia continua artificial.

6. **Incertidumbre no autorizada.** No existen CI por brazo para HE2_A, ni CI para Phase E, EXP11A, EXP11B o HE5 descriptivo. Ninguna fase posterior puede inferir visualmente o calcular barras/bandas de error nuevas a partir de las tablas.

7. **Integridad de ejes.** Las decisiones de FIG001 no autorizan truncamientos para magnificar efectos. El caso más sensible es EXP11B, precisamente una de las razones para conservarlo como tabla.

8. **Ausencia de obligación de completar seis espacios.** La existencia de seis figuras en Prompt103 no constituye evidencia de que deban existir seis figuras finales. No deben inventarse figuras para reemplazar las eliminadas.

---

## Validación terminal de FIG001

```text
FIG001_SCOPE = CRITICAL_CATALOG_REVIEW_ONLY
INITIAL_FIGURE_COUNT = 6
PRELIMINARY_RECOMMENDED_FIGURE_COUNT = 3

KEEP_OR_MODIFY_AS_FIGURE = 3
MERGED_INITIAL_FIGURE_COUNT = 1
REMOVE_AS_FIGURE_COUNT = 2
NEW_REPLACEMENT_FIGURE_COUNT = 0

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
HE2_REDECIDED = false
HE5_REDECIDED = false

EXP11A_CAUSAL_INTERPRETATION_CREATED = false
EXP11B_SEED_SUPERPOPULATION_INFERENCE_CREATED = false
EXP12_REOPENED = false
EXP12_PERFORMANCE_FIGURE_CREATED = false

ATTEMPT06_CURRENT_ONLY = true
SUPERSEDED_RESULT_USED = false
NEW_METRIC_CALCULATED = false
NEW_DELTA_CALCULATED = false
NEW_CI_CALCULATED = false
NEW_P_VALUE_CALCULATED = false
NEW_INFERENCE_PERFORMED = false

FIGURE_FILE_CREATED = false
FIGURE_SCRIPT_CREATED = false
CAPTION_FINAL_WRITTEN = false
G6_F02_EXECUTED = false
```

FIG001 termina aquí. La composición visual exacta de la primera figura queda fuera de alcance hasta la instrucción posterior correspondiente.
