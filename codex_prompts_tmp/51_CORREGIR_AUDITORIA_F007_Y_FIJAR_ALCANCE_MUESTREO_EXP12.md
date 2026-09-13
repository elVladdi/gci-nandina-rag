# PROMPT 51 — CORREGIR AUDITORÍA F007 Y FIJAR ALCANCE DE MUESTREO EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque corrige exclusivamente la auditoría prospectiva F007 producida por Prompt50. **NO ejecuta EXP12**, NO ejecuta retrieval/BM25, NO calcula Top-k/MRR, NO modifica los parámetros congelados de EXP12 y NO ingiere datos nuevos.

Debes:

1. preservar como válida la integración del Plan realizada en Prompt50;
2. NO integrar el candidato F007 v0.1 rechazado externamente;
3. materializar un nuevo candidato de auditoría F007 v0.2 desde `main` canónico, incorporando la decisión metodológica prospectiva fijada por IA Experimental sobre el alcance de muestreo de EXP12;
4. realizar únicamente el corte estructural de cobertura del pool nuevo ya congelado;
5. detenerte antes de cualquier planeamiento de 10,000 candidatos, porque dicho planeamiento solo corresponde si el universo fuente cumple primero la cobertura máxima exigida.

---

# 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt50 concluyó:

```text
PROMPT50_EXTERNAL_AUDIT = PARTIAL_PASS / CORRECTION_REQUIRED

PROMPT50_PHASE_A_PLAN_INTEGRATION = PASS / APPROVED
CANONICAL_PLAN = INTEGRATED
EXP11B = CLOSED / APPROVED / INTEGRATED

PROMPT50_PHASE_B_F007_AUDIT = REJECTED
candidate_ccd10565427a2eb0b938428a68f2b78e538ab144 = DO_NOT_INTEGRATE

EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Hallazgos externos que obligan la corrección:

```text
F007-SRC-01 = H100_PLUS_NEW_ELIGIBLE_WAS_NOT_EXPLICITLY_NAMED_AS_EXP12_SAMPLING_UNIVERSE
F007-SRC-02 = COMMON_CLEAN_MAXIMUM_UNIVERSE_WAS_CONFLATED_WITH_SAMPLING_UNIVERSE
F007-SRC-03 = EXP12_SPECIFIC_H100_REFERENCE_ONLY_ROLE_CONFLICTS_WITH_GENERIC_FUTURE_BANK_RULE
F007-SRC-04 = PLANNING_ON_INTERPRETATION_B_IS_NON_GOVERNING_BECAUSE_RESOLVED_UNIQUE_PRECONDITION_WAS_NOT_MET
```

La razón es documental y metodológica:

- `src/configs/exp12_historical_diversity_control_v0.3.json` mantiene `sampling_universe.source=PENDING_NEW_HISTORICAL_GATE`, `path=null`, `sha256=null` y `must_not_fallback_to_h100=true`.
- El mismo contrato define explícitamente `reference_h100.role = reference_label_set_and_distribution_only; never an EXP-12 sampling fallback`.
- `controls.common_clean_policy = defined against the approved maximum historical universe` gobierna la definición del common-clean, no identifica por sí solo el universo de muestreo de EXP12.
- `docs/protocolo_expansion_historico_multisheet_v0.1.md` contiene la regla genérica `Todo futuro banco sera H100_FROZEN + NEW_ELIGIBLE_HISTORICAL_ROWS`, pero ese documento pertenece al gate de expansión y declara que no autoriza EXP12. Esa regla no puede sustituir silenciosamente el rol EXP12-específico de H100 sin una decisión metodológica prospectiva.

Por tanto, bajo las propias reglas de Prompt50, la evidencia documental por sí sola no justificaba `RESOLVED_UNIQUE` para la interpretación B.

---

# 2. Decisión metodológica prospectiva de IA Experimental

Para EXP12 se fija prospectivamente la siguiente interpretación, sin modificar los umbrales ni el objetivo experimental:

```text
EXP12_SAMPLING_SCOPE_DECISION = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
H100_ROLE_IN_EXP12 = REFERENCE_LABEL_SET_AND_DISTRIBUTION_ONLY
H100_ROWS_ALLOWED_AS_EXP12_CANDIDATE_SAMPLING_ROWS = false
```

Justificación:

1. prevalece el contrato específico de EXP12 para el uso de H100;
2. H100 continúa siendo exclusivamente la referencia de conjunto/distribución NANDINA para cobertura y TVD;
3. el universo de muestreo EXP12 debe provenir de las filas históricas nuevas elegibles aprobadas por el gate ampliado;
4. esta aclaración es prospectiva y no modifica, invalida ni reinterpreta los bancos EXP11B H150/H200, cuyo diseño H100+incremento ya está cerrado;
5. no se elige esta interpretación por factibilidad numérica ni por desempeño.

El estado documental histórico de Prompt50 debe conservarse como:

```text
PROMPT50_DOCUMENTARY_BINDING_RESULT = AMBIGUOUS_UNDER_STRICT_UNIQUE_RULE
PROMPT50_B_PLANNING = LOCAL_NONRETRIEVAL_NON_GOVERNING_EVIDENCE
```

No borres ni modifiques el candidato v0.1 rechazado.

---

# 3. Precondiciones Git exactas

Ejecuta `git fetch` y verifica:

```text
origin/main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/exp12-f007-source-activation-audit-v01 = ccd10565427a2eb0b938428a68f2b78e538ab144
```

Exige además:

```text
ccd10565427a2eb0b938428a68f2b78e538ab144 is NOT ancestor of main
main contains no EXP12 execution outputs
EXP12 authorization does not exist
```

Si hay drift: `STOP / PRECONDITION_REF_DRIFT`.

---

# 4. Fuentes obligatorias

Trabaja read-only sobre, como mínimo:

```text
src/configs/exp12_historical_diversity_control_v0.3.json
docs/g2a_contract_exp11_exp12_v0.1.md
docs/protocolo_expansion_historico_multisheet_v0.1.md

data/interim/new_historical_gate_v0.1/new_historical_eligible.csv
outputs/audits/new_historical_gate_v0.1/new_historical_artifact_hashes.csv
outputs/audits/new_historical_gate_v0.1/new_historical_ingestion_manifest.json

data/processed/data_aduanas_historico_clase87_v0.2.csv
data/processed/data_aduanas_evalset_clase87_v0.2.csv
```

Bindings esperados:

```text
new_historical_eligible_sha256 = a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4
new_historical_eligible_rows = 6029
new_historical_eligible_dams = 43
H100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
H100_rows = 2950
H100_nandina_count = 66
EVAL_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

No uses fuentes externas al repositorio.

---

# 5. Corte estructural obligatorio sobre el universo EXP12 decidido

El universo prospectivo actual es exclusivamente:

```text
data/interim/new_historical_gate_v0.1/new_historical_eligible.csv
```

Calcula y registra:

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

Protección EVAL:

- verificar SHA;
- leer únicamente `DECLARACION` para overlap DAM;
- no leer descripciones EVAL;
- no leer NANDINA EVAL;
- no leer desempeño EVAL.

El resultado esperado según la evidencia ya observada es:

```text
rows_total = 6029
dam_count = 43
nandina_count = 56
H100_reference_code_count = 66
H100_reference_codes_present = 45
H100_reference_coverage_upper_bound = 45/66 = 0.6818181818181818
eval_dam_overlap_count = 0
```

Debes recalcularlo desde los artefactos versionados. Si no coincide: `STOP / SOURCE_COMPOSITION_DRIFT`.

Como el contrato congelado exige:

```text
required_label_coverage_fraction = 1.0
```

y la cobertura máxima del universo actual es `<1.0`, clasifica:

```text
EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY = IMPOSSIBLE_LABEL_COVERAGE
```

No ejecutes `generate_exp12_candidates`, no ejecutes 10,000 candidatos por seed y no produzcas HHI quantiles. La imposibilidad se demuestra antes de ese coste.

---

# 6. Estado F007 correcto

Registra inequívocamente:

```text
EXP12_SOURCE_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
EXP12_SOURCE_SCOPE_STATUS = PROSPECTIVELY_CLARIFIED_BY_EXTERNAL_METHODOLOGICAL_DECISION
EXP12_CURRENT_GATE_SOURCE = data/interim/new_historical_gate_v0.1/new_historical_eligible.csv
EXP12_CURRENT_GATE_SOURCE_SHA256 = a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4

EXP12_F007 = SOURCE_SCOPE_CLARIFIED_CURRENT_GATE_INSUFFICIENT
EXP12_STRUCTURAL_FEASIBILITY = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

El hallazgo bloqueante debe ser, como mínimo:

```text
EXP12-F007-SOURCE-COVERAGE-001
classification = CURRENT_NEW_ELIGIBLE_POOL_CANNOT_COVER_ALL_H100_REFERENCE_CODES
observed = 45/66
required = 66/66
```

La planificación B de Prompt50 no es un resultado EXP12 y no gobierna decisiones futuras:

```text
PROMPT50_INTERPRETATION_B_PLANNING_GOVERNING = false
PROMPT50_INTERPRETATION_B_PLANNING_CLASSIFICATION = LOCAL_NONRETRIEVAL_NON_GOVERNING_EVIDENCE_FROM_REJECTED_SOURCE_BINDING
```

---

# 7. Próximo requerimiento, sin ejecutarlo aquí

No cambies la cobertura 1.0, TVD 0.05, volumen, seeds, HHI, cuantiles, candidate_count ni mínimo de 30 factibles.

Registra únicamente:

```text
NEXT_REQUIRED_ACTION = EXP12_NEW_HISTORICAL_GATE_EXTENSION
```

El protocolo ya reconoce prospectivamente:

```text
NEW_SHEET_SET_2 = [NUEVA_01, NUEVA_02]
```

Pero Prompt51 **NO debe**:

- buscar o ingerir NUEVA_02;
- modificar Excel;
- rematerializar `new_historical_eligible.csv`;
- crear un gate nuevo;
- asumir que NUEVA_02 existe;
- afirmar que una futura expansión será suficiente antes de auditarla.

Solo deja documentado que se requiere una ampliación de fuente histórica nueva elegible para intentar cerrar la brecha de cobertura EXP12.

---

# 8. Candidato correctivo F007 v0.2

Crea desde exacto:

```text
main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
```

la rama:

```text
codex/exp12-f007-source-activation-audit-v02
```

Un solo commit; un solo path nuevo:

```text
outputs/audits/exp12_source_activation_v0.1/exp12_f007_source_activation_audit_v0.2.json
```

No modifiques ni elimines el v0.1 rechazado de su rama histórica.

El v0.2 debe incluir como mínimo:

```text
artifact = EXP12_F007_SOURCE_ACTIVATION_EXTERNAL_CORRECTION
version = v0.2
baseline_main
supersedes_rejected_candidate_commit = ccd10565427a2eb0b938428a68f2b78e538ab144
rejected_candidate_integrated = false

retrieval_executed = false
bm25_executed = false
top_k_computed = false
mrr_computed = false
exp12_authorized = false
exp12_outputs_created = false

prompt50_documentary_binding_result
external_methodological_source_scope_decision
source_scope_rationale
frozen_contract_bindings
current_new_eligible_source_binding
current_source_structural_feasibility
missing_H100_reference_codes
blocking_findings
prompt50_b_planning_non_governing_status
next_required_action
```

No crees config v0.4 ni autorización EXP12 en este bloque.

---

# 9. Restricciones

NO:

- integrar `ccd10565427a2eb0b938428a68f2b78e538ab144`;
- ejecutar EXP12;
- ejecutar retrieval/BM25/Top-k/MRR;
- ejecutar 10,000 candidatos/seed;
- leer labels/descripciones EVAL;
- modificar H100, DEV, EVAL o new_historical_eligible;
- modificar config EXP12 v0.3;
- modificar Plan o Article;
- abrir Grupo 2B o Grupo 3;
- volver a ejecutar EXP11B;
- relajar ninguna regla congelada.

---

# 10. Persistencia administrativa

Al finalizar, vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/51_RESPUESTA_CORREGIR_AUDITORIA_F007_Y_FIJAR_ALCANCE_MUESTREO_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No rebase, no amend, no force.

---

# 11. Reporte obligatorio

Reporta al menos:

```text
PROMPT51 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

REJECTED_PROMPT50_CANDIDATE = ccd10565427a2eb0b938428a68f2b78e538ab144
REJECTED_PROMPT50_CANDIDATE_INTEGRATED = false

CORRECTIVE_BRANCH
CORRECTIVE_COMMIT
CORRECTIVE_PARENT
CORRECTIVE_CHANGED_PATH_COUNT
CORRECTIVE_ARTIFACT_PATH
CORRECTIVE_ARTIFACT_BLOB
CORRECTIVE_ARTIFACT_SHA256

EXP12_SOURCE_SCOPE
EXP12_SOURCE_SCOPE_STATUS
current_source_rows
current_source_dams
current_source_nandina
H100_reference_codes_present
H100_reference_code_count
H100_reference_coverage_upper_bound
missing_H100_reference_codes
eval_dam_overlap_count

EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY
EXP12_F007
EXP12
PROMPT50_INTERPRETATION_B_PLANNING_GOVERNING
NEXT_REQUIRED_ACTION

EXP12_RETRIEVAL_EXECUTED = false
EXP12_BM25_EXECUTED = false
EXP12_TOP_K_COMPUTED = false
EXP12_MRR_COMPUTED = false
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT51 = COMPLETED
EXP12_SOURCE_SCOPE = NEW_ELIGIBLE_HISTORICAL_ROWS_ONLY
EXP12_CURRENT_SOURCE_STRUCTURAL_FEASIBILITY = FAIL_CLOSED_IMPOSSIBLE_LABEL_COVERAGE
EXP12_F007 = SOURCE_SCOPE_CLARIFIED_CURRENT_GATE_INSUFFICIENT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_REQUIRED_ACTION = EXP12_NEW_HISTORICAL_GATE_EXTENSION
```
