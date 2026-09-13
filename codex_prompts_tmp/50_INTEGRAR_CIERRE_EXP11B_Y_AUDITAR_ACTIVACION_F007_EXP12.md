# PROMPT 50 — INTEGRAR CIERRE EXP11B Y AUDITAR ACTIVACIÓN F007 DE EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque tiene dos fases estrictamente separadas y **NO ejecuta EXP12**:

1. integrar exactamente el candidato ya auditado de reconciliación del Plan Maestro que cierra documentalmente EXP11B;
2. realizar una auditoría prospectiva, read-only y no consumidora para determinar si la dependencia `F007` de EXP12 puede vincularse de forma **documentalmente unívoca** a un universo histórico ampliado ya aprobado, y si dicho universo puede satisfacer las restricciones congeladas antes de cualquier ejecución científica.

No ejecutes retrieval, BM25, Top-k, MRR ni ninguna evaluación EXP12. No modifiques parámetros congelados de EXP12 para hacer viable el diseño.

---

# 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt49 concluyó:

```text
PROMPT49_EXTERNAL_AUDIT = PASS / APPROVED
EXP11B_RETRIEVAL_RESULTS = APPROVED / INTEGRATED
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP11B_EXECUTION_CONFIG_SHA_NOTICE = VERIFIED_EOL_ONLY_WORKTREE_VARIATION
CONFIG_SEMANTIC_DRIFT = false
CANONICAL_PLAN_CANDIDATE = APPROVED_FOR_INTEGRATION
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Estado científico esperado:

```text
origin/main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Candidato de Plan aprobado:

```text
branch = codex/plan-maestro-exp11b-close-v01
commit = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
parent = 6e327d4bcde32a3804e6923015eaa505a0a53374
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Plan canónico esperado antes de integración:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
```

---

# 2. Precondiciones Git exactas

Ejecuta `git fetch` y verifica exactamente:

```text
origin/main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
origin/codex/plan-maestro-exp11b-close-v01 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato del Plan exige:

```text
parent = 6e327d4bcde32a3804e6923015eaa505a0a53374
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
```

Único path:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Si existe cualquier drift: `STOP / PRECONDITION_REF_DRIFT`.

---

# 3. Fase A — integrar exactamente el Plan reconciliado

Sobre `docs/plan-maestro-temporal-2026-08-31`, integra mediante **fast-forward exacto**:

```text
6e327d4bcde32a3804e6923015eaa505a0a53374
→
4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
```

Usa `--ff-only`.

NO hagas merge commit, squash, cherry-pick, rebase, amend ni reconstrucción del Plan.

Después del push exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
```

No modifiques `main` ni Article en esta fase.

Estado documental después de Fase A:

```text
EXP11B = CLOSED / APPROVED / INTEGRATED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
Grupo 2B = NOT_STARTED
Grupo 3 = NOT_STARTED
```

---

# 4. Fase B — objetivo exacto de la auditoría F007 de EXP12

Trabaja desde un checkout limpio de:

```text
origin/main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
```

Debes responder, **sin ejecutar EXP12**, estas dos preguntas en este orden:

1. ¿Cuál es el universo de muestreo histórico ampliado que el contrato versionado de EXP12 permite vincular prospectivamente después de NEW_HISTORICAL_GATE 03?
2. Si ese universo es documentalmente unívoco, ¿puede satisfacer las restricciones congeladas de EXP12 antes de cualquier retrieval?

La respuesta a la pregunta 1 **NO puede decidirse por conveniencia numérica o porque una interpretación sea factible y otra no**. Primero debe resolverse por procedencia documental/versionada.

---

# 5. Fuentes obligatorias y bindings que debes auditar

Lee y registra blob/SHA cuando aplique, como mínimo:

```text
docs/g2a_contract_exp11_exp12_v0.1.md
src/configs/exp12_historical_diversity_control_v0.3.json
src/experiments/plan_historical_bank_conditions_v03.py
src/configs/exp11b_historical_size_extension_v0.1.json

data/interim/new_historical_gate_v0.1/new_historical_eligible.csv
outputs/audits/new_historical_gate_v0.1/new_historical_artifact_hashes.csv
outputs/audits/new_historical_gate_v0.1/new_historical_ingestion_manifest.json
outputs/audits/new_historical_gate_v0.1/exp11b_h150_h200_feasibility_v0.1.json
outputs/audits/new_historical_gate_v0.1/eval_common_clean_masks_v0.1.csv

data/processed/data_aduanas_historico_clase87_v0.2.csv
data/processed/data_aduanas_evalset_clase87_v0.2.csv
```

Bindings congelados que deben permanecer:

```text
H100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
EVAL_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
new_historical_eligible_sha256 = a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4
new_historical_eligible_rows = 6029
new_historical_eligible_dams = 43
```

No uses archivos externos a este repositorio para decidir el binding.

---

# 6. Contrato EXP12 que NO puede modificarse en este bloque

Preserva exactamente el método congelado actual:

```text
target_rows = 2950
max_abs_row_deviation = 148
minimum_rows = 2802
maximum_rows = 3098
preserve_complete_dams = true
number_of_replicates_per_condition = 10
seed_schedule = 20262001..20262010
primary_diversity_variable = DAM_CONCENTRATION_HHI
H100_label_coverage_required = 1.0
maximum_TVD_against_H100 = 0.05
candidate_count_per_seed = 10000
minimum_unique_feasible_candidates = 30
quantiles = D-HIGH:0.10 / D-MID:0.50 / D-LOW:0.90
requires_distinct_dam_sets = true
strict_HHI_order = HHI_DLOW > HHI_DMID > HHI_DHIGH
must_not_fallback_to_h100 = true
no_eval_performance_selection = true
```

No reduzcas cobertura, no relajes TVD, no cambies volumen, seeds, cuantiles, HHI, número de candidatos o mínimo factible.

---

# 7. Protección de EVAL y no contaminación

Para esta auditoría:

- puedes verificar SHA de EVAL;
- puedes leer **únicamente los identificadores DAM** de EVAL para comprobar overlap;
- NO leas ni utilices descripciones comerciales de EVAL;
- NO leas ni utilices etiquetas NANDINA de EVAL;
- NO utilices Top-k, MRR, hits, ranks ni ningún resultado de desempeño para seleccionar o preferir un universo;
- NO ejecutes BM25 ni otro retrieval.

Las NANDINA de H100 sí pueden usarse exclusivamente como distribución/label-set de referencia conforme al contrato ya congelado.

---

# 8. Clasificación documental obligatoria del universo de muestreo

Audita explícitamente, sin materializar bancos científicos, al menos estas interpretaciones potenciales:

```text
A = NEW_ELIGIBLE_ONLY
    data/interim/new_historical_gate_v0.1/new_historical_eligible.csv

B = H100_PLUS_NEW_ELIGIBLE
    unión lógica/prospectiva de H100 congelado + new_historical_eligible

C = EXP11B_H200_DERIVED_BANK_FAMILY
    bancos H200 derivados de EXP11B
```

Para cada una registra:

```text
interpretation_id
documentary_support_paths
explicitly_named_as_exp12_sampling_universe = true/false
compatible_with_must_not_fallback_to_h100 = true/false/ambiguous
requires_new_unversioned_assumption = true/false
status = SUPPORTED / PLAUSIBLE_BUT_NOT_EXPLICIT / CONTRADICTED / NOT_APPLICABLE
reason
```

No elijas una interpretación porque produzca mejores métricas de factibilidad.

Clasifica finalmente:

```text
EXP12_SOURCE_BINDING_STATUS = RESOLVED_UNIQUE | AMBIGUOUS | CONTRADICTED_OR_MISSING
```

`RESOLVED_UNIQUE` solo es válido si una y solo una definición del universo queda determinada por evidencia versionada suficiente y las demás quedan descartadas documentalmente.

Si hay más de una interpretación razonablemente compatible o ninguna está explícitamente sustentada:

```text
EXP12_SOURCE_BINDING_STATUS = AMBIGUOUS
EXP12_EXECUTION = NOT_AUTHORIZED
```

y no debes inventar un source path/hash para la config.

---

# 9. Pre-chequeo estructural de factibilidad

Realiza este bloque para cada interpretación `SUPPORTED` o `PLAUSIBLE_BUT_NOT_EXPLICIT`, pero mantén separada la factibilidad de la decisión documental.

Calcula solo a partir de composición histórica:

```text
rows_total
dam_count
nandina_count
H100_reference_code_count
H100_reference_codes_present
H100_reference_coverage_upper_bound
missing_H100_reference_codes
eval_dam_overlap_count
```

Regla de corte temprano:

Si para un universo la cobertura máxima posible de códigos H100 es `< 1.0`, entonces ningún subconjunto de ese universo puede cumplir el contrato. Clasifica:

```text
STRUCTURAL_FEASIBILITY = IMPOSSIBLE_LABEL_COVERAGE
```

y **NO ejecutes** para ese universo los 10,000 candidatos por seed.

No cambies la regla de cobertura para hacerlo viable.

Si `eval_dam_overlap_count > 0`, clasifica también el incumplimiento correspondiente; no elimines DAM ad hoc salvo que el contrato versionado ya defina esa exclusión.

---

# 10. Planeamiento EXP12 permitido solo bajo binding unívoco

Solo si simultáneamente:

```text
EXP12_SOURCE_BINDING_STATUS = RESOLVED_UNIQUE
H100_reference_coverage_upper_bound = 1.0
eval_dam_overlap_count = 0
```

puedes ejecutar **únicamente la lógica de planeamiento no-retrieval ya versionada** de `plan_historical_bank_conditions_v03.py` sobre el universo resuelto, usando exactamente las 10 seeds y 10,000 candidatos/seed congelados.

Esta fase de planeamiento:

- no materializa outputs de retrieval;
- no abre BM25;
- no consulta desempeño EVAL;
- no crea autorización de ejecución;
- no cambia config v0.3;
- no convierte el resultado en aprobación científica.

Reporta por seed:

```text
seed
unique_feasible_candidate_count
selected_D_HIGH_rows / HHI / effective_DAM / TVD / DAM_count
selected_D_MID_rows  / HHI / effective_DAM / TVD / DAM_count
selected_D_LOW_rows  / HHI / effective_DAM / TVD / DAM_count
strict_hhi_order_pass
distinct_dam_sets_pass
```

Y globalmente:

```text
HHI_q10
HHI_q50
HHI_q90
HHI_span_q90_q10
effective_DAM_q10
effective_DAM_q50
effective_DAM_q90
effective_DAM_ratio_high_low
minimum_feasible_candidates_across_seeds
```

No introduzcas un umbral nuevo de “manipulation strength”. La suficiencia metodológica de la manipulación queda para auditoría externa posterior.

Si alguna seed tiene menos de 30 candidatos factibles o falla la selección estricta, registra el fail-closed; no modifiques reglas ni seeds.

---

# 11. Artefacto candidato de auditoría

Crea desde exacto:

```text
main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
```

una rama nueva:

```text
codex/exp12-f007-source-activation-audit-v01
```

El único commit científico/documental de esta rama debe añadir exclusivamente:

```text
outputs/audits/exp12_source_activation_v0.1/exp12_f007_source_activation_audit_v0.1.json
```

Usa `git add -f` porque `outputs/` está ignorado.

El JSON debe registrar como mínimo:

```text
artifact = EXP12_F007_SOURCE_ACTIVATION_AUDIT
version = v0.1
baseline_main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
retrieval_executed = false
bm25_executed = false
eval_performance_read = false
eval_descriptions_read = false
eval_labels_read = false
exp12_authorized = false
exp12_outputs_created = false

frozen_contract_bindings
historical_gate_bindings
source_interpretations
EXP12_SOURCE_BINDING_STATUS
source_binding_reason
structural_feasibility_by_interpretation
planning_executed = true/false
planning_results si corresponde
blocking_findings
nonblocking_findings
next_required_action
```

No crees todavía una config v0.4, autorización EXP12, bancos EXP12 ni resultados EXP12.

---

# 12. Estados terminales permitidos

### A. Binding ambiguo

```text
EXP12_SOURCE_BINDING_STATUS = AMBIGUOUS
EXP12_F007 = NOT_CLOSED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_REQUIRED_ACTION = EXTERNAL_METHODOLOGICAL_SOURCE_DECISION
```

### B. Binding único pero imposibilidad estructural

```text
EXP12_SOURCE_BINDING_STATUS = RESOLVED_UNIQUE
EXP12_STRUCTURAL_FEASIBILITY = FAIL_CLOSED
EXP12_F007 = SOURCE_RESOLVED_BUT_DESIGN_NOT_EXECUTABLE
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_REQUIRED_ACTION = EXTERNAL_METHODOLOGICAL_REVIEW
```

### C. Binding único y planeamiento factible

```text
EXP12_SOURCE_BINDING_STATUS = RESOLVED_UNIQUE
EXP12_STRUCTURAL_FEASIBILITY = PASS_PRE_RETRIEVAL
EXP12_F007 = CANDIDATE_FOR_CLOSURE_PENDING_EXTERNAL_AUDIT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_REQUIRED_ACTION = EXTERNAL_AUDIT_OF_SOURCE_BINDING_AND_MANIPULATION
```

En todos los casos EXP12 sigue sin autorización al finalizar Prompt50.

---

# 13. Prohibiciones absolutas

NO:

- ejecutar EXP12 retrieval;
- ejecutar BM25/Top-k/MRR para EXP12;
- usar performance EVAL para elegir fuente o condición;
- leer descripciones o etiquetas EVAL;
- modificar `exp12_historical_diversity_control_v0.3.json`;
- relajar cobertura, TVD, volumen, seeds, HHI, cuantiles o mínimo factible;
- usar H100 como fallback silencioso;
- seleccionar entre fuentes por conveniencia de factibilidad;
- materializar bancos EXP12 oficiales;
- crear una autorización EXP12;
- modificar resultados EXP11B;
- ejecutar de nuevo EXP11B;
- modificar Article;
- iniciar Grupo 2B o Grupo 3;
- integrar automáticamente el candidato de auditoría a `main`.

---

# 14. Persistencia administrativa

Después del trabajo:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch`;
3. no hagas rebase/amend/force;
4. crea únicamente:

```text
codex_prompts_tmp/50_RESPUESTA_INTEGRAR_CIERRE_EXP11B_Y_AUDITAR_ACTIVACION_F007_EXP12.md
```

El commit administrativo debe contener solo esa respuesta.

---

# 15. Reporte obligatorio

Reporta al menos:

```text
PROMPT50 = COMPLETED | STOP

plan_initial
plan_final
plan_integration_mode
main_initial/main_final
article_initial/article_final

AUDIT_CANDIDATE_BRANCH
AUDIT_CANDIDATE_COMMIT
AUDIT_CANDIDATE_PARENT
AUDIT_CANDIDATE_CHANGED_PATH_COUNT
AUDIT_ARTIFACT_PATH
AUDIT_ARTIFACT_BLOB
AUDIT_ARTIFACT_SHA256

EXP12_SOURCE_BINDING_STATUS
source_interpretations_summary
structural_feasibility_by_interpretation
planning_executed
minimum_feasible_candidates_across_seeds si aplica
strict_hhi_order_all_seeds si aplica
manipulation_summary si aplica

EXP12_F007
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_RETRIEVAL_EXECUTED = false
EXP11B_REEXECUTED = false
GROUP2B_STARTED = false
GROUP3_STARTED = false
NEXT_REQUIRED_ACTION
```

No declares PASS externo. Solo IA Experimental puede aprobar el cierre de F007 o una futura activación de EXP12.
