# FIG001 — REVISIÓN CRÍTICA DEL CATÁLOGO INICIAL DE FIGURAS

## 0. Rol y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto de tesis.

Tu función en FIG001 es exclusivamente **evaluar críticamente el catálogo inicial de figuras propuesto para G6-F01** y dejar una respuesta oficial versionada en GitHub.

Este trabajo es conceptual, científico y visual. No actúes como Codex y no ejecutes instrucciones operativas de Prompt103 relativas a workspace local, branches, activación de fichas, commits de ciencia, generación de figuras o scripts.

Prompt103 queda tratado para este flujo como:

```text
SUPERSEDED / DO_NOT_EXECUTE_AS_CODEX_PROMPT
```

Debe leerse únicamente como fuente histórica de requisitos científicos y visuales.

No autoriza:

- modificar `main`;
- modificar Plan Maestro;
- modificar fichas;
- modificar artículo o tesis;
- generar PNG, SVG, PDF u otra figura final;
- escribir scripts Python de generación;
- recalcular métricas, deltas científicos, inferencia, CI o p-values;
- redecidir HE2 o HE5;
- reabrir EXP12;
- usar resultados superseded.

---

## 1. Fuentes rectoras

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Rama para prompts y respuestas de esta IA:

```text
codex/prompts-temporary
```

Fuente histórica de requisitos de G6-F01:

```text
codex_prompts_tmp/103_ACTIVAR_Y_EJECUTAR_G6_F01_CATALOGO_Y_ESPECIFICACION_FIGURAS.md
commit = 2db3c4d2b6010688b2a4483dc1ac2351610ca336
```

Refs científicas/administrativas vigentes al iniciar FIG001:

```text
main = ca065618d5df0019f76ef5a971e858d91c263e1f
plan = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
fichas = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
article_head_observed = db01f6432464e97d428de7e3d5a5c1e80b34e528
```

Fuentes mínimas que debes consultar directamente en GitHub:

```text
docs/results/group5/g5_results_presentation_plan_v0.1.md
outputs/results/group5/g5_table_registry_v0.1.json
docs/results/group5/g5_canonical_tables_v0.1.md
outputs/results/group5/g5_numeric_crosscheck_v0.1.json
docs/results/group5/g5_appendix_registry_v0.1.md
outputs/audits/group5_closure_v0.1.json
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
outputs/analysis/group4/g4_limitations_registry_v0.1.json
```

Y las nueve tablas canónicas G5-F02:

```text
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
outputs/results/group5/tables/g5_secondary_02_he5_descriptive_components.csv
outputs/results/group5/tables/g5_appendix_01_top50_supplementary.csv
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
outputs/results/group5/tables/g5_appendix_03_exp11b_h150_h200_sensitivity.csv
outputs/results/group5/tables/g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv
outputs/results/group5/tables/g5_appendix_05_phase_e_diagnostic_union.csv
```

Si una fuente no puede verificarse en GitHub, decláralo expresamente y no rellenes el vacío con conocimiento general.

---

## 2. Contrato científico que no puede alterarse

Preserva:

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

Guardrails:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

Semántica vigente de Attempt06:

```text
EV03 = ZERO_AGGREGATE_CHANGE
EV04 = TINY_NONZERO_MRR_DECREASE_ONLY
D1a = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
OVERALL = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

EXP12 no puede convertirse en figura de rendimiento.

---

## 3. Objeto de la revisión

Prompt103 propuso inicialmente seis figuras:

```text
G6-FIG-01 — HE2_A: desempeño absoluto y contrastes pareados primarios
G6-FIG-02 — HE2_B: cobertura profunda
G6-FIG-03 — Phase E descriptivo
G6-FIG-04 — EXP11A sensibilidad tamaño/composición
G6-FIG-05 — EXP11B H150/H200
G6-FIG-06 — HE5 componentes descriptivos
```

No des por correcta esa selección solo porque fue fijada en Prompt103.

Debes evaluar cada figura por:

1. necesidad científica;
2. aporte visual real respecto de la tabla canónica;
3. redundancia con otras figuras/tablas;
4. riesgo de sobreclaim;
5. riesgo de exageración por escala, eje o codificación;
6. coherencia con el rol científico congelado;
7. utilidad para un lector de tesis;
8. costo de complejidad visual;
9. si debe mantenerse, modificarse, fusionarse, dividirse, degradarse a anexo o eliminarse como figura.

La prioridad es que una figura aporte comprensión. No conviertas tablas en gráficos por obligación.

---

## 4. Libertad de diseño permitida

Puedes recomendar:

```text
KEEP
MODIFY
MERGE
SPLIT
MOVE_TO_APPENDIX
TABLE_ONLY
TEXT_ONLY
REMOVE_AS_FIGURE
```

Siempre con justificación apoyada en fuentes congeladas.

Puedes proponer un número final de figuras diferente de seis.

No selecciones u omitas resultados por favorabilidad.

---

## 5. Contenido mínimo de la respuesta

La respuesta oficial debe contener:

### A. Evaluación crítica de las seis figuras iniciales

Para cada una:

```text
figure_id inicial
DICTAMEN
razón científica
razón visual
riesgo principal
fuente(s) relevante(s)
```

### B. Decisión consolidada

Indica cuáles:

```text
mantener
modificar
fusionar
dividir
mover a anexo
mantener solo como tabla
mantener solo como texto
eliminar como figura
```

### C. Catálogo recomendado

Propón el catálogo final preliminar con:

```text
nuevo figure_id
título de trabajo
contenido
rol científico
destino: principal / secundaria / anexo
fuente canónica
claim(s) asociados
justificación de por qué merece ser figura
```

### D. Material que NO debe convertirse en figura

Enumera expresamente qué resultados deben permanecer como tabla o texto y por qué.

### E. Riesgos pendientes

Identifica cualquier ambigüedad que deba resolverse antes de especificar visualmente la primera figura.

---

## 6. Regla de no avance

FIG001 termina con la revisión del catálogo.

No diseñes todavía la composición visual exacta de ninguna figura.
No escribas captions definitivos.
No generes imágenes.
No ejecutes G6-F02.

El siguiente paso será definido mediante FIG002 solo después de auditoría externa de FIG001.

---

## 7. Persistencia obligatoria de la respuesta en GitHub

La respuesta oficial debe almacenarse en:

```text
branch = codex/prompts-temporary
path = figure_prompts_tmp/FIG001_RESPUESTA_REVISION_CRITICA_CATALOGO_INICIAL.md
```

Debes crear únicamente ese archivo en esta rama para la respuesta de FIG001.

No modifiques el propio FIG001 ni ningún otro archivo.

Commit recomendado:

```text
figures: record FIG001 critical catalog review
```

Al terminar, responde en el chat únicamente con:

```text
Rama: codex/prompts-temporary

Archivo de respuesta:
figure_prompts_tmp/FIG001_RESPUESTA_REVISION_CRITICA_CATALOGO_INICIAL.md

Commit:
<SHA>
```

No pegues nuevamente el contenido completo de la respuesta en el chat.
