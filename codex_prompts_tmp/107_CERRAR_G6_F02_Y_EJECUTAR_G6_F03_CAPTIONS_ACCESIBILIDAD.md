# PROMPT107 — CERRAR G6-F02 Y EJECUTAR G6-F03: CAPTIONS, ACCESIBILIDAD Y CIERRE CANDIDATO DE GRUPO 6

## 0. Rol y alcance

Actúa como **Codex ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Este prompt tiene dos etapas secuenciales y obligatorias:

1. **cerrar e integrar G6-F02** usando exclusivamente el candidato corregido ya auditado externamente por la IA Experimental;
2. **activar y ejecutar G6-F03** para producir el paquete candidato de captions, accesibilidad y cierre de Grupo 6.

La segunda etapa solo puede comenzar si la primera termina correctamente.

No eres la IA Experimental auditora. No apruebes tu propio entregable G6-F03. G6-F03 debe terminar como **candidato pendiente de auditoría externa**, no como cierre definitivo autoaprobado.

No modifiques tesis ni artículo. No ejecutes G7. No generes nuevas figuras. No reabras EXP12. No recalcules resultados científicos ni introduzcas métricas, inferencia, CI o p-values nuevos.

---

# 1. Workspace local canónico obligatorio

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier cambio registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git status --porcelain
git worktree list
git fetch origin
```

STOP si:

1. el toplevel no corresponde exactamente al workspace canónico;
2. `origin` no corresponde a `elVladdi/gci-nandina-rag`;
3. estás usando otro clon/worktree como repositorio primario;
4. hay cambios locales no relacionados que no puedan aislarse;
5. alguna referencia congelada de la sección 2 presenta drift material.

Los untracked preexistentes documentados por Prompt106, si continúan existiendo, no deben añadirse ni modificarse.

---

# 2. Binding rector congelado

Verifica exactamente:

```text
MAIN_PRE_G6F02_CLOSE = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_PRE_G6F02_CLOSE = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_POST_PROMPT106 = ea5bc84b8e01f1f7fa0c365a7a83bb69d370d37f
PROMPTS_PRE_PROMPT107 = e71ba7cf70eda8b825af37b1ed418970ff7bebde
G6_F01_INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F02_PREVIOUS_CANDIDATE = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
G6_F02_CORRECTED_CANDIDATE = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F02_CORRECTION_PARENT = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
PROMPT106_SOURCE_COMMIT = 9c1d17db8b0846041c67fb0e7efa265fcb716616
PROMPT106_RESPONSE_COMMIT = e71ba7cf70eda8b825af37b1ed418970ff7bebde
PROMPT106_RESPONSE_BLOB = 782adedc1a15a1c4333b3dd1cab15386e5723c60
FIG007_RESPONSE_COMMIT = b94312c0149a4f5d0cec1680495a0b9731982dca
G6_F01_REGISTRY_PATH = outputs/figures/group6/g6_figure_spec_registry_v0.1.json
G6_F01_REGISTRY_BLOB = 44cc30fc3c38639c6aa4370cb6f317458041f1b1
G6_F02_LEDGER_PATH = outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
G6_F02_LEDGER_BLOB = 10616c7ddac277cc0e788af0b44322a5f93b59d4
```

La auditoría independiente de la IA Experimental sobre Prompt106/G6-F02 queda fijada para este prompt como:

```text
G6_F02_EXTERNAL_AUDIT = PASS
G6_F02_SCIENTIFIC_CORRECTION_REQUIRED = false
G6_F02_RERUN_REQUIRED = false
G6_F02_APPROVED_CANDIDATE = 71b13caf6b97e254b4c701b23318bcb0682714bd
```

La auditoría externa verificó independientemente, entre otros puntos:

```text
corrected candidate direct child of 2a483984... = true
commits ahead vs b6404ca... = 2
commits behind vs b6404ca... = 0
cumulative changed paths vs b6404ca... = 10
C1 canonical-Git ledger semantics = resolved
C2 FIG03 effective minimum font >= 8.5 pt = resolved
C3 FIG03 material point occlusion = resolved
C4 visible internal G6-FIG-0X title prefixes = removed
C5 FIG01 Panel C Hierarchical (Attempt06) = resolved
C6 FIG02 y-axis label outside data field = resolved
scientific source bindings preserved = true
new scientific metric/inference/CI/p-value = 0/0/0/0
```

La imposibilidad del conector de la IA Experimental de recomputar localmente los SHA-256 de bytes PNG binarios se considera una **limitación de herramienta de auditoría, no un defecto del candidato**: se verificaron independientemente identidad Git, paths, tamaños canónicos, scripts, fuentes, geometría SVG y consistencia del ledger; Prompt106 documenta además su chequeo canónico 16/16. No reabras G6-F02 por esta limitación instrumental.

---

# 3. Ground truth científico que no puede alterarse

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
H100 = 2950 series / 28 DAM / 66 NANDINA
DEV = 100 series / 6 DAM
EVAL = 1056 series / 67 DAM / 42 NANDINA
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Guardrails permanentes:

```text
historical retrieval superiority != global RAG accuracy
normative evidence != binding legal correctness
auditable explanation != classification/legal correctness
configurability != empirical generalization
EXP11A != isolated causal size effect
EXP11B != seed-superpopulation inference
Attempt06 != global zero impact
```

Uncertainty/presentation:

```text
HE2_A = 15 primary paired contrasts / frozen 99% CI on paired differences / no arm-level CI
HE2_B = one primary Recall@200 - Recall@100 contrast / frozen 95% CI
Phase E = descriptive only
Top50 = supplementary only
HE5 hierarchy/support = descriptive only
EXP12 = text-only / not estimable
P_VALUES = none
```

---

# 4. Etapa A — cierre e integración formal de G6-F02

## 4.1 Revalidación previa mínima

Antes de integrar, confirma:

```text
origin/main = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
origin/figures/g6-f02-render-v01 = 71b13caf6b97e254b4c701b23318bcb0682714bd
71b13caf parent = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
2a483984 parent = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
candidate vs main = 2 ahead / 0 behind
cumulative changed path count = 10
```

Los diez paths deben ser exactamente:

```text
figures/group6/g6_fig_01_he2.png
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_02_phase_e.png
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_03_exp11a.png
figures/group6/g6_fig_03_exp11a.svg
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
src/figures/group6/render_g6_fig_01_he2.py
src/figures/group6/render_g6_fig_02_phase_e.py
src/figures/group6/render_g6_fig_03_exp11a.py
```

No vuelvas a modificar estos diez paths en esta ejecución. Si detectas drift o una diferencia distinta, STOP.

## 4.2 Integración a main

Integra G6-F02 mediante **fast-forward only**:

```text
MAIN_FROM = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
MAIN_TO = 71b13caf6b97e254b4c701b23318bcb0682714bd
INTEGRATION_METHOD = FAST_FORWARD_ONLY
```

No cherry-pick, no squash, no merge commit, no rebase y no force-push.

Después confirma:

```text
origin/main = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02_INTEGRATION_COMMIT = 71b13caf6b97e254b4c701b23318bcb0682714bd
```

## 4.3 Registrar cierre G6-F02 antes de activar G6-F03

Sobre `docs/fichas-grupos-3-8`, partiendo de:

```text
ea5bc84b8e01f1f7fa0c365a7a83bb69d370d37f
```

actualiza exclusivamente el registro de estado correspondiente para añadir un bloque de cierre G6-F02 con, como mínimo:

```text
FICHA = G6-F02
PROMPT104_CANDIDATE = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
PROMPT106_CORRECTED_CANDIDATE = 71b13caf6b97e254b4c701b23318bcb0682714bd
PROMPT106_RESPONSE_COMMIT = e71ba7cf70eda8b825af37b1ed418970ff7bebde
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false
INTEGRATION_METHOD = FAST_FORWARD_ONLY
INTEGRATION_COMMIT = 71b13caf6b97e254b4c701b23318bcb0682714bd
FINAL_G6_F02_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = IN_PROGRESS
G6_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F03_AUTHORIZED = false
G6_F03_STARTED = false
GROUP7_AUTHORIZED = false
```

Este cierre debe quedar persistido **antes** del bloque de activación G6-F03.

---

# 5. Etapa B — activación formal de G6-F03

La instrucción permanente del usuario autoriza continuidad automática tras un PASS, siempre que la dependencia formal esté satisfecha. Una vez cerrado G6-F02, activa G6-F03.

Registra en fichas:

```text
FICHA = G6-F03
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
AUTHORIZATION_BASIS = STANDING_CONTINUATION_INSTRUCTION + PROMPT107_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
MAIN_AT_ACTIVATION = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = IN_PROGRESS
GROUP7_AUTHORIZED = false
```

No actives G7-F01.

---

# 6. Etapa C — ejecución exclusiva de G6-F03

## 6.1 Ficha rectora

Lee y cumple:

```text
docs/fichas/grupos_3_8/grupo_6/G6_F03_CAPTIONS_ACCESIBILIDAD_Y_CIERRE.md
```

Su objetivo es auditar que cada figura sea científicamente autosuficiente, accesible y consistente con Grupo 5.

## 6.2 Fuentes obligatorias

Trabaja desde `main=71b13caf6b97e254b4c701b23318bcb0682714bd` y consulta directamente:

### Diseño visual/científico

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
```

### Figuras finales G6-F02

```text
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png
figures/group6/g6_fig_03_exp11a.svg
figures/group6/g6_fig_03_exp11a.png
```

### Presentación numérica canónica Grupo 5

```text
outputs/results/group5/g5_table_registry_v0.1.json
docs/results/group5/g5_canonical_tables_v0.1.md
docs/results/group5/g5_appendix_registry_v0.1.md
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
```

### Claims y límites autorizados Grupo 4

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
docs/analysis/group4/g4_literature_contrast_v0.1.md
```

### Inferencia relevante Grupo 3

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
```

No uses tesis ni artículo como fuente de verdad de captions.

---

# 7. Auditoría obligatoria por figura

Audita las tres figuras finales; no diseñes una cuarta.

## G6-FIG-01 — evidencia primaria HE2

Debe mantenerse coherente con:

```text
scientific_role = PRIMARY_INFERENTIAL
destination = MAIN
benchmark = 1056 series / 67 DAM / 42 NANDINA
Panel A = valores observados; NO arm-level CI
Panel B = 15 diferencias pareadas Historical - comparator; frozen 99% CI
Panel C = único contraste Recall@200 - Recall@100; frozen 95% CI
Panel C identity = Hierarchical (Attempt06)
Pool@200 confirmatory estimate count = 0
p-values = none
```

El caption debe distinguir explícitamente valores por brazo, contrastes pareados y niveles 99%/95%. No atribuyas CI a los brazos. No llames a la figura accuracy global del RAG.

## G6-FIG-02 — Phase E

Debe mantenerse:

```text
scientific_role = DESCRIPTIVE_SUPPLEMENTARY
panel_count = 1
mark_count = 15
formal claim variants = 4
context-only variant = hierarchical_70_dual_backfill_30
depths = 50 / 100 / 200
y_range = [0,0.35]
CI = 0
p-values = 0
connecting lines = 0
diagnostic union ordinary-performance marks = 0
```

El caption debe decir claramente que Phase E es descriptivo y que la variante 70/30 es contexto adicional, no evidencia confirmatoria elegida por favorabilidad. La unión diagnóstica no debe presentarse como rendimiento ordinario.

## G6-FIG-03 — EXP11A

Debe mantenerse:

```text
scientific_role = DESCRIPTIVE_SENSITIVITY / APPENDIX
metrics = Top1 / Top3 / Top5 / Top10 / Top50 / MRR
panel_count = 6
observed_run_count = 31
condition counts = 10 / 5 / 5 / 10 / 1
condition order = H25 / H50-D1 / H50-D2 / H75 / H100 ref.
y_range = [0,1]
summary marks = 0
CI = 0
p-values = 0
regression = 0
vertical jitter = 0
H100 = one frozen reference per panel
```

El caption debe afirmar únicamente **sensibilidad conjunta a tamaño/composición**. Debe prohibir explícitamente una lectura causal o monotónica del tamaño. H50-D1 y H50-D2 deben conservarse como composición diferenciada. No conviertas los summaries congelados en CI.

---

# 8. Accesibilidad y autosuficiencia

Verifica para cada figura:

```text
scientific_self_contained
caption_names_population
caption_names_metric_or_evidence_family
caption_names_uncertainty_when_applicable
caption_states_descriptive_vs_inferential_role
caption_states_material_limitations
caption_matches_visible_panels/marks
caption_does_not_depend_on_color_alone
redundant_symbol_encoding_present_when_required
contrast_and_legibility_acceptable
internal_ids_not_visible_as publication titles
no misleading axis truncation or visual exaggeration
```

Para G6-FIG-03 verifica expresamente que ninguna etiqueta efectiva quede por debajo de 8.5 pt y que la multiplicidad de observaciones siga discernible.

Para G6-FIG-02 verifica expresamente que `Exact-NANDINA coverage` permanezca fuera del campo de datos y con tamaño efectivo >= 10 pt.

Si detectas un defecto que requiera **editar una figura o script aprobado de G6-F02**, STOP y produce `REVISION_REQUIRED_G6_F02_ARTIFACT`. No corrijas silenciosamente la figura dentro de G6-F03.

---

# 9. Output 1 — caption registry

Crea únicamente:

```text
docs/figures/group6/g6_caption_registry_v0.1.md
```

Debe contener, para cada `G6-FIG-01`, `G6-FIG-02`, `G6-FIG-03`:

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

Usa como punto de partida los `caption_working` ya congelados en `g6_figure_spec_registry_v0.1.json`. Puedes corregir redacción para hacer el caption autosuficiente o sincronizarlo con el render corregido, pero:

- no agregues claims nuevos;
- no cambies el rol científico;
- no cambies números ni denominadores;
- no conviertas evidencia descriptiva en inferencial;
- no introduzcas resultados no visibles/soportados;
- no traduzcas a otro idioma como tarea adicional;
- no uses la tesis o el artículo como autoridad.

El caption registry es documental; no debe contener una disposición nueva de hipótesis.

---

# 10. Output 2 — cierre candidato de Grupo 6

Crea únicamente:

```text
outputs/audits/group6_closure_v0.1.json
```

Debe ser JSON válido y contener como mínimo:

```text
artifact_id
version
ficha = G6-F03
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
main_source_commit = 71b13caf6b97e254b4c701b23318bcb0682714bd
g6_f01_registry_path/blob
g6_f02_ledger_path/blob
figure_count = 3
caption_count = 3
per_figure_source_bindings
per_figure_caption_checks
per_figure_accessibility_checks
numeric_consistency_with_group5
claim_consistency_with_group4
uncertainty_consistency_with_group3
forbidden_claim_count
new_scientific_metric_count
new_inference_count
new_ci_count
new_p_value_count
exp12_reopened
article_modified
thesis_modified
group6_closure_candidate = true
group6_closed = false
external_audit = PENDING
g7_f01_authorized = false
```

No declares `GROUP6=CLOSED/APPROVED` dentro del candidato antes de la auditoría externa. El eventual cierre definitivo pertenece al paso posterior a la auditoría de la IA Experimental.

---

# 11. Rama y commit candidato de G6-F03

Crea desde:

```text
71b13caf6b97e254b4c701b23318bcb0682714bd
```

la rama:

```text
figures/g6-f03-caption-closure-v01
```

El candidato científico-documental debe modificar **exactamente dos paths**:

```text
docs/figures/group6/g6_caption_registry_v0.1.md
outputs/audits/group6_closure_v0.1.json
```

No modifiques figuras, scripts, ledger, tablas, claims, datos, tesis ni artículo.

Haz un único commit candidato y publícalo sin force-push.

Registra:

```text
G6_F03_CANDIDATE_PARENT = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F03_CHANGED_PATH_COUNT = 2
COMMITS_AHEAD_VS_MAIN = 1
COMMITS_BEHIND_VS_MAIN = 0
```

---

# 12. Gobernanza postejecución

Después de publicar el candidato, actualiza Plan Maestro y fichas **solo para reflejar el estado real**.

## 12.1 Fichas

El estado final de esta ejecución debe quedar:

```text
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
GROUP6_CLOSED = false
G7_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F01_AUTHORIZED = false
GROUP7_AUTHORIZED = false
```

Registra el candidate branch, commit, parent, dos paths, controles principales y `EXTERNAL_AUDIT=PENDING`.

## 12.2 Plan Maestro

Sobre `docs/plan-maestro-temporal-2026-08-31`, partiendo de:

```text
b74b96d0163807007e4579d86450dd235125b30f
```

reconcilia únicamente el estado de Grupo 6 para reflejar:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02_INTEGRATION_COMMIT = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6-F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
G7 = NOT_AUTHORIZED
```

No declares Grupo 6 cerrado todavía.

---

# 13. Validaciones finales

Antes de publicar la respuesta oficial confirma:

```text
MAIN_FINAL = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F02_FINAL = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03_CANDIDATE_PARENT = MAIN_FINAL
G6_F03_CHANGED_PATH_COUNT = 2
FIGURE_FILE_CHANGE_COUNT_IN_G6_F03 = 0
SCRIPT_CHANGE_COUNT_IN_G6_F03 = 0
SCIENTIFIC_DATA_CHANGE_COUNT = 0
CAPTION_COUNT = 3
NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
EXP12_REOPENED = false
GROUP6_CLOSED = false
G7_F01_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING
```

Si falla un control científico, de accesibilidad o de trazabilidad, no fuerces PASS: registra `REVISION_REQUIRED` y conserva G7 bloqueado.

---

# 14. Respuesta oficial

Persiste la respuesta completa en:

```text
codex_prompts_tmp/107_RESPUESTA_CERRAR_G6_F02_Y_EJECUTAR_G6_F03_CAPTIONS_ACCESIBILIDAD.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT107_EXECUTION
WORKSPACE_CONTRACT
G6_F02_EXTERNAL_AUDIT_BINDING
MAIN_PRE_G6F02_CLOSE
G6_F02_CORRECTED_CANDIDATE
G6_F02_INTEGRATION_METHOD
G6_F02_INTEGRATION_COMMIT
G6_F02_FINAL_STATE
G6_F03_ACTIVATION_COMMIT_OR_STATE_RECORD
G6_F03_BRANCH
G6_F03_CANDIDATE_COMMIT
G6_F03_CANDIDATE_PARENT
G6_F03_CHANGED_PATHS
G6_F03_CHANGED_PATH_COUNT
CAPTION_REGISTRY_PATH
GROUP6_CLOSURE_CANDIDATE_PATH
CAPTION_COUNT
FIGURE_AUDIT_SUMMARY
ACCESSIBILITY_AUDIT_SUMMARY
GROUP5_NUMERIC_CROSSCHECK
GROUP4_CLAIM_CROSSCHECK
GROUP3_UNCERTAINTY_CROSSCHECK
NEW_SCIENTIFIC_METRIC_COUNT
NEW_INFERENCE_COUNT
NEW_CI_COUNT
NEW_P_VALUE_COUNT
ARTICLE_MODIFIED
THESIS_MODIFIED
EXP12_REOPENED
MAIN_FINAL
PLAN_FINAL
FICHAS_FINAL
G6_F03_FINAL_STATE
GROUP6_FINAL_STATE
G7_F01_FINAL_STATE
EXTERNAL_AUDIT = PENDING
```

No declares G6-F03 `PASS`, `APPROVED`, `CLOSED` ni `INTEGRATED_TO_MAIN`. No declares `GROUP6=CLOSED` y no activa G7-F01.

Finaliza con:

```text
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
```

---

# 15. Criterios de auditoría externa posterior

La IA Experimental deberá verificar, al menos:

1. G6-F02 fue integrado a `main` por fast-forward exacto a `71b13caf...`;
2. G6-F02 quedó documentalmente `CLOSED / APPROVED / INTEGRATED_TO_MAIN`;
3. G6-F03 parte exactamente de `71b13caf...` y añade solo dos paths;
4. existen exactamente tres captions, uno por figura;
5. cada caption coincide con la población, métrica, rol científico, incertidumbre y limitaciones de G3–G6;
6. FIG01 conserva separación valores por brazo / diferencias pareadas / CI 99% y 95%;
7. FIG02 permanece descriptiva, con cuatro variantes formales y 70/30 solo contextual;
8. FIG03 permanece no causal y explicita tamaño+composición conjunta;
9. no hay claims nuevos ni reinterpretaciones favorables no autorizadas;
10. accesibilidad y autosuficiencia quedan trazadas por figura;
11. ninguna figura/script/dato fue alterado en G6-F03;
12. no hubo nuevas métricas, inferencia, CI o p-values;
13. tesis y artículo permanecieron sin modificación;
14. EXP12 no fue reabierto;
15. Grupo 6 permanece IN_PROGRESS y G7-F01 no autorizado hasta el PASS externo de G6-F03.

Si cualquiera de estos puntos falla, no cierres Grupo 6 y no avances a G7.
