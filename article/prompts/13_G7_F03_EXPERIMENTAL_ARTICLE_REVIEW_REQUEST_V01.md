# 13 — Solicitud a IA Experimental: revisión científica G7-F03 del artículo finalizado V036 y evaluación pre-FAST

## Naturaleza de esta solicitud

Esta es una **solicitud inter-rol de revisión científica** emitida por IA Gestora del Artículo al rol **IA Experimental**. No es un prompt de IA de Redacción y no autoriza modificación del manuscrito por IA Experimental.

El Autor solicita que IA Experimental revise el artículo ahora que existe una versión canónica sustancialmente finalizada, con dos objetivos:

1. permitir que IA Experimental resuelva, conforme a su propio Plan Maestro, la ficha **G7-F03**;
2. obtener un dictamen científico antes de que IA Gestora organice el `FAST_FINALIZATION_MODE`.

Si el Plan Maestro Experimental vigente requiere una activación, autorización o artefacto previo adicional para ejecutar G7-F03, IA Experimental debe detenerse y declarar exactamente el blocker en lugar de eludir su propia gobernanza.

## Repositorios y estados que deben verificarse

### Repositorio experimental principal

`elVladdi/gci-nandina-rag`, rama `main`.

Head observado por IA Gestora al emitir esta solicitud:

`db0d0ad0d8435921a7838db6720eaea86a263763`

G7-F01 ya está cerrado/aprobado e integrado y su contrato se encuentra en:

- `docs/writing/group7/g7_writing_source_freeze_v0.1.md`
- Git blob: `feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430`
- companion JSON:
  `docs/writing/group7/g7_writing_source_freeze_v0.1.json`
- Git blob JSON: `776fcb52e8ada9967504001b897c75b4108bfb63`

Ese contrato establece expresamente para G7-F03:

- `g7_f03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED` en el freeze original;
- antes de cualquier G7-F03 debe compararse el artículo vigente contra el artículo congelado en G7-F01 y reconciliar drift científico material;
- el head editorial congelado entonces era
  `2aad97aaceec0af6be0edb9ba0dd29170ad35baf`;
- los controles editoriales no sustituyen las fuentes experimentales primarias.

### Repositorio/rama editorial a auditar

`elVladdi/gci-nandina-rag`, rama:

`article/main-manuscript`

Head de solicitud:

`952a56bb09c95bc7a93baec9b0a560889d253195`

Master Markdown canónico:

`article/manuscript/ARTICLE_MASTER_V036.md`

Git blob:

`c9dcbcc376cdb121d30dc2408756a6c95b569a90`

SHA-256 gobernado:

`8b37aeda893759a4b48d4a346561b030d3611bc474cefb9f7d73d900e345e4f8`

Word canónico acumulativo bajo custodia local del Autor:

`ARTICLE_MASTER_CANDIDATE_AI_DISCLOSURE_B02_V02_CORRECTED.docx`

SHA-256 gobernado:

`d7f59b60ec6a261d94d2c81b146b99fae36de0bca886392340ac42daf1392e3d`

Comentarios: 48. Tracked changes: 0. Páginas auditadas: 72.

La auditoría científica G7-F03 debe basarse primariamente en el Markdown versionado y en las fuentes experimentales congeladas. La falta del binario DOCX en Git no autoriza a declarar un problema científico inexistente.

## Fuentes experimentales mínimas obligatorias

IA Experimental debe usar su propia precedencia vigente y, como mínimo, reconciliar V036 contra las fuentes ya congeladas por G7-F01:

- G3: contrato analítico, poblaciones métricas, inferencia y disposición de hipótesis;
- G4: matriz claim-evidence, síntesis interpretativa, limitaciones y contraste de literatura;
- G5: registro y materialización de tablas canónicas;
- G6: figuras y captions aprobados;
- cierres de Grupo 1 / Grupo 2 cuando correspondan a HE3, HE4, reproducibilidad y trazabilidad.

En particular:

### G5 — tablas científicas congeladas

`outputs/results/group5/g5_table_registry_v0.1.json`
Git blob `4fe9318d52fad093066ff9f42d524fc95e436245`

`docs/results/group5/g5_canonical_tables_v0.1.md`
Git blob `9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d`

El registro cubre nueve presentaciones canónicas:

- G5-MAIN-01 — HE2_A primary early ranking;
- G5-MAIN-02 — HE2_B deep coverage;
- G5-SECONDARY-01 — Phase E descriptive coverage;
- G5-SECONDARY-02 — HE5 descriptive components;
- G5-APPENDIX-01 — Top-50 supplementary uncertainty;
- G5-APPENDIX-02 — EXP11A size-composition sensitivity;
- G5-APPENDIX-03 — EXP11B H150/H200 sensitivity;
- G5-APPENDIX-04 — Attempt06 corrective sensitivity;
- G5-APPENDIX-05 — Phase E diagnostic-union ceiling.

### G6 — figuras científicas aprobadas

`outputs/figures/group6/g6_figure_spec_registry_v0.1.json`
Git blob `44cc30fc3c38639c6aa4370cb6f317458041f1b1`

`docs/figures/group6/g6_caption_registry_v0.1.md`
Git blob `0dcb43cfa56dfce2e6955f960184069beb36ba76`

`outputs/audits/group6_closure_v0.1.json`
Git blob `a5d698ccda4e7a540e2f8b54533720ad59b02e73`

G6 está CLOSED / APPROVED y contiene:

- G6-FIG-01 — evidencia primaria HE2, MAIN;
- G6-FIG-02 — Phase E descriptive coverage, SECONDARY;
- G6-FIG-03 — EXP11A joint size-composition sensitivity, APPENDIX.

No crear nuevas métricas, CIs, p-values ni inferencias para esta revisión.

## Alcance de G7-F03 solicitado

### A. Drift check obligatorio

Comparar el estado científico del artículo que G7-F01 congeló en
`2aad97aaceec0af6be0edb9ba0dd29170ad35baf`
con el artículo actual
`952a56bb09c95bc7a93baec9b0a560889d253195`,
poniendo el foco en el contenido científico incorporado desde entonces.

No tratar un cambio de SHA por sí solo como contradicción. Identificar exclusivamente drift científico material.

### B. Auditoría científica integral de V036

Revisar el contenido científico de:

- Introduction cuando haga afirmaciones sobre contribución o alcance experimental;
- Architecture §3 en cuanto a roles/autoridad de componentes;
- Experimental design §4;
- Results §5;
- Discussion §6;
- Conclusion §7;
- Abstract cuando resuma resultados;
- cualquier declaración de reproducibilidad o disponibilidad vinculada al experimento.

Comprobar, como mínimo:

- cifras y denominadores;
- unidad de análisis SERIE y dependencia/grupo DAM cuando aplica;
- benchmark interno offline de Capítulo 87;
- separación historical ranking → fixed Top-3 → candidate-specific normative evidence → context → local LLM explanation;
- normative evidence no reranks;
- diagnostic reranker no se presenta como main flow;
- HE2, HE3, HE4 y HE5 conforme a fuentes vigentes;
- ausencia de disposición formal inventada para HG/HE1 cuando corresponda;
- EXP11A no causal;
- EXP11B descriptivo sin superpopulation inference;
- EXP12 CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE;
- auditabilidad distinta de classification/legal correctness;
- configurabilidad distinta de empirical generalization;
- reproduccibilidad declarada con sus limitaciones reales;
- ningún resultado superseded utilizado como vigente.

### C. Dictamen sobre tablas y figuras para el artículo

IA Gestora realizó una revisión editorial del corpus KBS-34 y detectó que V036 está demasiado apoyado en prosa numérica. Esta observación es editorial; IA Experimental debe decidir únicamente la compatibilidad científica con los artefactos congelados.

Se solicita:

1. indicar cuáles de las nueve presentaciones G5 deben:
   - incorporarse al cuerpo principal del artículo;
   - ir a Supplementary/Appendix;
   - permanecer solo como soporte interno;
2. indicar cuáles de las tres figuras G6 deben:
   - incorporarse al cuerpo principal;
   - ir a Supplementary/Appendix;
   - no incorporarse;
3. revisar si la actual `Figure 1 placeholder — overall architecture and information flow` puede materializarse editorialmente sin nueva evidencia experimental;
4. señalar si cualquier figura adicional propuesta requeriría una nueva decisión/acción experimental;
5. evitar duplicación tabla-figura-prosa que pueda distorsionar roles inferenciales o descriptivos.

No se pide crear ni rediseñar las figuras en esta ficha; se pide **disposición científica**.

### D. Evaluación de la propuesta `FAST_FINALIZATION_MODE`

La siguiente propuesta es **PROVISIONAL / NOT AUTHORIZED** y se entrega solo para revisión:

- `FINAL-F01 — Scientific Presentation & Visual Structuring`: optimización de tablas/figuras y reducción de prosa redundante, sin cambiar resultados ni claims.
- `FINAL-F02 — End Matter & Reference Integrity`: metadatos de autor, declaraciones, data/reproducibility, referencias y supplementary.
- `FINAL-F03 — Submission Assembly & Final QA`: cleanup, cross-references, numeración, Word final y QA.

IA Experimental debe indicar:

- si este orden es científicamente seguro;
- qué correcciones científicas derivadas de G7-F03 deben ocurrir **antes** de FINAL-F01;
- qué verificaciones experimentales deben convertirse en constraints de FINAL-F01/F02/F03;
- si alguna tarea propuesta invadiría competencias de IA Experimental;
- si puede cerrarse G7-F03 antes de la finalización editorial o si exige una reauditoría posterior a FINAL-F01.

## Entregables requeridos

IA Experimental debe emitir, conforme a su propio Plan Maestro vigente:

1. **estado formal de G7-F03**: PASS / PASS_WITH_REQUIRED_CORRECTIONS / BLOCKED, o la taxonomía exacta que gobierne su Plan;
2. matriz de discrepancias científicas de V036:
   - sección/localización;
   - afirmación o dato auditado;
   - fuente gobernante;
   - resultado;
   - severidad;
   - acción requerida;
3. disposición de las 9 tablas G5 para el artículo;
4. disposición de las 3 figuras G6 para el artículo;
5. dictamen sobre la figura arquitectónica pendiente;
6. evaluación científica del `FAST_FINALIZATION_MODE`;
7. lista exacta de condiciones que IA Gestora debe incorporar al plan final;
8. indicación explícita de si G7-F03 queda resuelta/cerrada con esta revisión o qué falta para cerrarla.

Si el Plan Experimental establece rutas y formatos canónicos para los artefactos de G7-F03, usar esos. Si no los establece, materializar un informe versionado bajo `docs/writing/group7/` y un companion JSON cuando sea útil para trazabilidad.

## Prohibiciones

- No modificar `article/main-manuscript`.
- No reescribir el artículo.
- No generar nuevos resultados experimentales.
- No reabrir EXP12.
- No recalcular métricas o inferencias salvo que el propio Plan Experimental lo autorice expresamente por un blocker demostrado.
- No aprobar el `FAST_FINALIZATION_MODE` en nombre del Autor o de IA Gestora.
- No convertir decisiones editoriales en evidencia científica.
- No usar ARTICLE_STATUS como sustituto de las fuentes experimentales primarias.

## Stop condition

La ejecución termina cuando IA Experimental entrega su dictamen G7-F03 y la evaluación científica de la propuesta pre-FAST.

Después de ese dictamen, **IA Gestora** reorganizará el `FAST_FINALIZATION_MODE` y lo someterá al Autor antes de cualquier nueva edición del manuscrito.
