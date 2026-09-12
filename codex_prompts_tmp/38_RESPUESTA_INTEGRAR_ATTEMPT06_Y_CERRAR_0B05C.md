# RESPUESTA PROMPT 38 - INTEGRAR ATTEMPT06 Y CERRAR 0B-05C

## Estado terminal

```makefile
PROMPT38 = COMPLETED
MAIN = 6846537602539506c8e90426daad05252cc982b9
ATTEMPT06 = COMPLETED / AUDITED / INTEGRATED
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_ONLY_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_D1A_RESULTS
0B05C_CLOSURE = CLOSED / APPROVED
GROUP_2 = EN_CURSO
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

## Verificacion de entrada

```makefile
pre_integration_main = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
pre_integration_origin_main = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
authorization_commit = a9b06b8748316d7f3c403eaa9d55b735e12d96c3
authorization_parent = e7cab327f0ef12b1e8ae21cddd01d215cd42db31
execution_commit = 6846537602539506c8e90426daad05252cc982b9
execution_parent = a9b06b8748316d7f3c403eaa9d55b735e12d96c3
execution_tree = 6114b34bae36d9c7bb92c383509e2f6cb6e903c7
execution_branch = codex/0b05c-v05-attempt06-execution
execution_branch_later_commits = 0
authorization_to_execution_changed_paths = 49
linear_descendant_verification = PASS
protected_paths_modified_by_execution = false
tracked_working_tree_clean_before = true
canonical_plan_previous_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

El diff `a9b06b8... -> 6846537...` contiene exclusivamente los outputs y
el versionado de Attempt06. No modifica el Plan Maestro, `article/`, EXP11B ni
EXP12. La rama remota de ejecucion no contenia ningun commit posterior.

## Integracion cientifica

```makefile
integration_method = FAST_FORWARD_ONLY
merge_commit_created = false
squash_performed = false
rebase_performed = false
amend_performed = false
cherry_pick_performed = false
post_integration_main = 6846537602539506c8e90426daad05252cc982b9
post_integration_origin_main = 6846537602539506c8e90426daad05252cc982b9
integrated_tree = 6114b34bae36d9c7bb92c383509e2f6cb6e903c7
candidate_tree_identity = true
changed_content_beyond_candidate = false
main_push = PASS
```

`main` avanzo por fast-forward desde `e7cab327...` hasta el commit auditado
exacto `6846537602539506c8e90426daad05252cc982b9` y fue publicado en `origin`.

## Interpretacion cientifica congelada

### EV03

```makefile
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
MRR_original = 0.40223149245938034
MRR_corrected = 0.40223149245938034
Top1_original = 0.3494318181818182
Top1_corrected = 0.3494318181818182
Top3_original = 0.4431818181818182
Top3_corrected = 0.4431818181818182
Top5_original = 0.47632575757575757
Top5_corrected = 0.47632575757575757
Top10_original = 0.5208333333333334
Top10_corrected = 0.5208333333333334
Top50_Recall50_original = 0.5928030303030303
Top50_Recall50_corrected = 0.5928030303030303
Recall100_original = 0.6401515151515151
Recall100_corrected = 0.6401515151515151
```

### EV04

```makefile
EV04_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
MRR_original = 0.41801769149469725
MRR_corrected = 0.41801769149469725
MRR100_original = 0.4209029085295853
MRR100_corrected = 0.4209029085295853
MRR200_original = 0.42114657818747986
MRR200_corrected = 0.42114657818747986
MRR_101_200_contribution_original = 0.00024366965789453498
MRR_101_200_contribution_corrected = 0.00024366965789453498
Top1_original = 0.36742424242424243
Top1_corrected = 0.36742424242424243
Top3_original = 0.45738636363636365
Top3_corrected = 0.45738636363636365
Top5_original = 0.48295454545454547
Top5_corrected = 0.48295454545454547
Top10_original = 0.5265151515151515
Top10_corrected = 0.5265151515151515
Top50_Recall50_original = 0.6742424242424242
Top50_Recall50_corrected = 0.6742424242424242
Recall100_original = 0.740530303030303
Recall100_corrected = 0.740530303030303
```

### D1a

```makefile
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EARLY_RANK_CHANGE
MRR10_original = 0.06823809523809526
MRR10_corrected = 0.08020006613756614
MRR10_delta = +0.011961970899470875
Top1_original = 0.032196969696969696
Top1_corrected = 0.038825757575757576
Top1_delta = +0.006628787878787879
Top3_original = 0.06723484848484848
Top3_corrected = 0.08238636363636363
Top3_delta = +0.015151515151515152
Top5_original = 0.08712121212121213
Top5_corrected = 0.10321969696969698
Top5_delta = +0.01609848484848485
Top10_original = 0.16287878787878787
Top10_corrected = 0.17897727272727273
Top10_delta = +0.016098484848484862
partida10_original = 0.42045454545454547
partida10_corrected = 0.4393939393939394
partida10_delta = +0.018939393939393923
sub_partida10_original = 0.3494318181818182
sub_partida10_corrected = 0.3683712121212121
sub_partida10_delta = +0.018939393939393923
clase10_original = 0.2774621212121212
clase10_corrected = 0.29640151515151514
clase10_delta = +0.018939393939393923
partida50_original = 0.7367424242424242
partida50_corrected = 0.7414772727272727
partida50_delta = +0.004734848484848509
sub_partida50_original = 0.6676136363636364
sub_partida50_corrected = 0.6714015151515151
sub_partida50_delta = +0.0037878787878787845
clase50_original = 0.6136363636363636
clase50_corrected = 0.6174242424242424
clase50_delta = +0.0037878787878787845
hierarchy_100_200_change = ZERO
```

La actualizacion normativa no altera las metricas agregadas de los
recuperadores normativos BM25 EV03/EV04 y mejora las posiciones tempranas del
recuperador denso D1a. El drift normativo era material para D1a, pero su efecto
no es uniforme entre metodos. No se declara significancia estadistica, efecto
causal ni generalizacion fuera de este analisis de sensibilidad determinista.

## Decision downstream y cierre

```makefile
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_ONLY_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_D1A_RESULTS
ATTEMPT06 = COMPLETED / AUDITED / INTEGRATED
0B05C_CLOSURE = CLOSED / APPROVED
EXP11B_PORTABILITY_DEBT = OPEN
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
GROUP_3 = PENDING
GROUPS_4_8 = PENDING
```

No se requiere reejecutar trabajo downstream: EXP11B Retrieval y EXP12 no se
han ejecutado, y los grupos posteriores pueden consumir directamente los
resultados D1a corregidos de Attempt06. Esta decision no autoriza EXP11B ni
EXP12 y conserva sus gates y deudas vigentes.

## Reconciliacion del Plan Maestro

```makefile
canonical_plan_branch = docs/plan-maestro-temporal-2026-08-31
canonical_plan_previous_head = fe847f708d4d1ded92b5a50a38d4913bb69ed311
canonical_plan_new_head = 6b1323cc97c1b94119f226768dd4b8cbda273ccb
canonical_plan_parent = fe847f708d4d1ded92b5a50a38d4913bb69ed311
canonical_plan_previous_blob = 9747a1cbf951d92bb63013f2e25e0cb64e905d83
canonical_plan_new_blob = 1cb9711c38d775afb3d4a1fd72fdf8019b9e1183
canonical_plan_changed_paths = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
canonical_plan_changed_path_count = 1
canonical_plan_fast_forward = PASS
canonical_plan_push = PASS
article_head = 254b1e6df736fa9938ac86a515d65b36f4d361c5
article_modified = false
```

El Plan registra cronologicamente la integracion de v0.5, la autorizacion
auditada de Attempt06, la finalizacion 19/19 PASS, los impactos congelados, la
decision downstream y el cierre aprobado de 0B-05C. La historia de los intentos
fail-closed permanece preservada. EXP11B conserva su deuda de portabilidad y
EXP11B/EXP12 permanecen no autorizados y no ejecutados.

## Preservaciones

```makefile
additional_experiments_executed = false
retrieval_executed_again = false
EV03_executed_again = false
EV04_executed_again = false
D1a_executed_again = false
scientific_preflight_executed_again = false
tests_executed = false
new_0B05C_remediation_opened = false
plan_mixed_into_main = false
article_modified = false
exp11b_modified = false
exp12_modified = false
```

El hecho operacional `invocation_count=1 / no retry / no resume` se conserva
como evidencia CODEX-local versionada y coherente; no se reinterpreta como una
observacion independiente del host.

Referencias remotas finales verificadas:

```makefile
origin/main = 6846537602539506c8e90426daad05252cc982b9
origin/codex/0b05c-v05-attempt06-execution = 6846537602539506c8e90426daad05252cc982b9
origin/docs/plan-maestro-temporal-2026-08-31 = 6b1323cc97c1b94119f226768dd4b8cbda273ccb
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```
