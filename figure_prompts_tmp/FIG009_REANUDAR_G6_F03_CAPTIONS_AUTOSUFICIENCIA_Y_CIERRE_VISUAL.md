# FIG009 — Reanudar G6-F03: captions, autosuficiencia y cierre visual

## 0. Rol

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto `elVladdi/gci-nandina-rag`.

Tu tarea es reanudar exclusivamente el contenido científico-visual pendiente de **G6-F03 — Captions, accesibilidad y cierre de Grupo 6** después de que la remediación técnica de accesibilidad fue auditada e integrada a `main`.

No eres CODEX. No modifiques `main`, no regeneres figuras, no edites scripts, no actualices hashes, no cierres formalmente Grupo 6 y no actives G7. Tu salida será una **auditoría científico-visual final y una propuesta congelada de captions/registro de cierre**, para que la IA Experimental la audite antes de cualquier materialización técnica.

---

## 1. Estado vinculante de entrada

Trabaja sobre:

```text
MAIN = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
ACCESSIBILITY_REMEDIATION = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
GROUP6 = IN_PROGRESS / NOT_CLOSED
G7_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

La integración de Prompt109 ya dejó como siguiente actor sustantivo a la IA Diseñadora y Auditora de Figuras.

No reabras la discusión sobre si la remediación debía integrarse. Esa decisión ya fue auditada y ejecutada.

---

## 2. Fuentes obligatorias

Consulta directamente en GitHub y trabaja desde `main=3390878a62ce32ba0e6f4fce69a394c903f5ff11`.

### Ficha rectora

```text
docs/fichas/grupos_3_8/grupo_6/G6_F03_CAPTIONS_ACCESIBILIDAD_Y_CIERRE.md
```

### Registry científico-visual

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
```

### Figuras finales integradas

```text
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png
figures/group6/g6_fig_03_exp11a.svg
figures/group6/g6_fig_03_exp11a.png
```

### Tablas canónicas de Grupo 5

```text
outputs/results/group5/g5_table_registry_v0.1.json
docs/results/group5/g5_canonical_tables_v0.1.md
docs/results/group5/g5_appendix_registry_v0.1.md
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
```

### Claims y límites de Grupo 4

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
docs/analysis/group4/g4_literature_contrast_v0.1.md
```

### Inferencia relevante de Grupo 3

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
```

### Antecedentes de accesibilidad

```text
figure_prompts_tmp/FIG008_RESPUESTA_AUDITORIA_ACCESIBILIDAD_POST_PROMPT107_Y_ESPECIFICACION_CORRECTIVA.md@cbb248ed87836a8c31978344fda08021dc0ea2d2
codex_prompts_tmp/108_RESPUESTA_CORREGIR_ACCESIBILIDAD_FIGURAS_POST_FIG008.md@codex/prompts-temporary
codex_prompts_tmp/109_RESPUESTA_INTEGRAR_REMEDIACION_ACCESIBILIDAD_Y_REANUDAR_G6_F03.md@codex/prompts-temporary
```

No uses tesis ni artículo como fuente de verdad.

---

## 3. Auditoría final obligatoria de las tres figuras

### G6-FIG-01 — HE2

Debe conservar:

```text
scientific_role = PRIMARY_INFERENTIAL
destination = MAIN
benchmark = 1,056 series / 67 DAM / 42 NANDINA
Panel A = observed arm values / no arm-level CI
Panel B = 15 Historical - comparator paired differences / frozen 99% CI
Panel C = one Recall@200 - Recall@100 contrast / frozen 95% CI
Panel C identity = Hierarchical (Attempt06)
Pool@200 confirmatory estimate count = 0
p-values = none
```

Audita que el caption final distinga inequívocamente:

- valores observados por brazo;
- diferencias pareadas;
- 99% CI del Panel B;
- 95% CI del Panel C;
- ausencia de CI por brazo;
- alcance interno/offline/Capítulo 87.

No uses `accuracy global del RAG` ni una formulación equivalente.

### G6-FIG-02 — Phase E

Debe conservar:

```text
scientific_role = DESCRIPTIVE_SUPPLEMENTARY
15 marks = 5 variants × 3 depths
formal variants = 4
context-only variant = hierarchical_70_dual_backfill_30
depths = 50 / 100 / 200
y-range = [0,0.35]
CI = 0
p-values = 0
connecting lines = 0
diagnostic union ordinary-performance marks = 0
```

El caption debe dejar explícito que:

- Phase E es descriptivo;
- 70/30 es contexto descriptivo adicional, no evidencia confirmatoria seleccionada por favorabilidad;
- la unión diagnóstica es un techo/diagnóstico y no rendimiento ordinario;
- la figura no altera la disposición de HE2.

### G6-FIG-03 — EXP11A

Debe conservar:

```text
scientific_role = DESCRIPTIVE_SENSITIVITY / NONCAUSAL
metrics = Top1 / Top3 / Top5 / Top10 / Top50 / MRR
panel_count = 6
observed_run_count = 31
condition counts = 10 / 5 / 5 / 10 / 1
condition order = H25 / H50-D1 / H50-D2 / H75 / H100 ref.
y-range = [0,1]
summary marks = 0
CI = 0
p-values = 0
regression = 0
vertical jitter = 0
H100 = one frozen reference per panel
```

El caption debe decir únicamente **sensibilidad conjunta a tamaño/composición**, sin lectura causal ni monotónica del tamaño. H50-D1 y H50-D2 deben conservarse como composiciones diferenciadas. H100 n=1 no debe tratarse como una distribución de réplicas.

---

## 4. Accesibilidad y autosuficiencia

Confirma, sin reabrir la remediación salvo que detectes un defecto nuevo real:

```text
FIG01 all nonempty text >= 8 pt
FIG01 axis/tick preference ~8.5–9 pt satisfied where applicable
FIG02 both axis titles >= 10 pt
FIG02 ticks/legend target >= 9 pt
FIG03 minimum effective font >= 8.5 pt
FIG03 six panel titles >= 9.5 pt
no material text clipping
no material label overlap
no color-only interpretation where redundant symbol coding is required
no misleading axis truncation
no visible internal IDs as publication titles
```

Si encuentras un defecto que requiera volver a editar SVG/PNG/script, no lo corrijas. Declara:

```text
FIG009_RESULT = REVISION_REQUIRED_TECHNICAL_ARTIFACT
NEXT_ACTOR = CODEX
```

y detente antes de proponer cierre.

---

## 5. Captions finales propuestos

Para cada figura produce un caption final, listo para materializar posteriormente en:

```text
docs/figures/group6/g6_caption_registry_v0.1.md
```

Cada entrada debe contener:

```text
figure_id
working_title
scientific_role
destination
final_caption
population_and_denominator
metric_or_evidence_family
uncertainty_statement
scope_limitation
forbidden_interpretation
source_table_paths
figure_svg_path
figure_png_path
accessibility_checks
status
```

Usa como base los `caption_working` del registry, pero mejora claridad y autosuficiencia cuando sea necesario.

No:

- agregues claims nuevos;
- cambies números;
- cambies denominadores;
- cambies roles científicos;
- conviertas evidencia descriptiva en inferencial;
- introduzcas una nueva disposición de hipótesis;
- traduzcas a otro idioma como tarea adicional.

---

## 6. Propuesta de cierre de Grupo 6

Si las tres figuras y captions pasan, prepara una **propuesta de contenido** para `outputs/audits/group6_closure_v0.1.json`, sin escribir ese archivo.

La propuesta debe incluir al menos:

```text
group = 6
ficha = G6-F03
figure_count = 3
figure_ids = [G6-FIG-01, G6-FIG-02, G6-FIG-03]
scientific_consistency = PASS
accessibility = PASS
caption_self_containment = PASS
canonical_table_consistency = PASS
claim_scope_consistency = PASS
scientific_data_change_count = 0
new_inference_count = 0
new_p_value_count = 0
exp12_reopened = false
g6_f03_candidate_status = READY_FOR_EXTERNAL_AUDIT
recommended_group6_state_after_external_pass = CLOSED / APPROVED
recommended_next_ficha_after_external_pass = G7-F01
```

Tu propuesta no cierra formalmente el grupo. Solo la IA Experimental puede auditar y autorizar el cierre.

---

## 7. Resultado terminal

Usa exactamente una de estas opciones:

```text
FIG009_RESULT = PASS_READY_FOR_EXTERNAL_AUDIT
FIG009_RESULT = REVISION_REQUIRED_CAPTION_OR_VISUAL_SCOPE
FIG009_RESULT = REVISION_REQUIRED_TECHNICAL_ARTIFACT
```

Si es PASS:

```text
NEXT_ACTOR = IA_EXPERIMENTAL
GROUP6_CLOSED = false
G7_F01_AUTHORIZED = false
```

---

## 8. Salida oficial

Publica únicamente tu respuesta en:

```text
figure_prompts_tmp/FIG009_RESPUESTA_REANUDAR_G6_F03_CAPTIONS_AUTOSUFICIENCIA_Y_CIERRE_VISUAL.md
```

sobre la rama:

```text
codex/prompts-temporary
```

Incluye en este orden:

1. `DICTAMEN_TERMINAL`;
2. fuentes exactas revisadas;
3. auditoría de G6-FIG-01;
4. auditoría de G6-FIG-02;
5. auditoría de G6-FIG-03;
6. auditoría transversal de accesibilidad/autosuficiencia;
7. tres captions finales propuestos;
8. propuesta completa de caption registry;
9. propuesta de `group6_closure_v0.1.json`;
10. siguiente actor;
11. declaraciones de no modificación/no cierre.

No modifiques ninguna otra ruta.
