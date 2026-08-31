# EXP-04 Fase E: candidate pools normativos v0.2

- La unión diagnóstica no es ranking y no reporta MRR.
- D0 excluido: INVALID AS FINAL COMPARATOR - LEGACY VECTOR INDEX NOT REPRODUCIBLE.

## PoolRecall

| Pool | Tipo | N | Exact | HS6 | HS4 | Chapter |
|---|---|---:|---:|---:|---:|---:|
| hierarchical_only | candidate_pool | 50 | 96/1056 (0.090909090909) | 0.100378787879 | 0.181818181818 | 0.377840909091 |
| hierarchical_only | candidate_pool | 100 | 107/1056 (0.101325757576) | 0.111742424242 | 0.250000000000 | 0.509469696970 |
| hierarchical_only | candidate_pool | 200 | 321/1056 (0.303977272727) | 0.343750000000 | 0.500946969697 | 0.767045454545 |
| dual_only | candidate_pool | 50 | 97/1056 (0.091856060606) | 0.100378787879 | 0.181818181818 | 0.391098484848 |
| dual_only | candidate_pool | 100 | 106/1056 (0.100378787879) | 0.114583333333 | 0.256628787879 | 0.547348484848 |
| dual_only | candidate_pool | 200 | 281/1056 (0.266098484848) | 0.321969696970 | 0.485795454545 | 0.783143939394 |
| hierarchical_first_100 | candidate_pool | 50 | 96/1056 (0.090909090909) | 0.100378787879 | 0.181818181818 | 0.377840909091 |
| hierarchical_first_100 | candidate_pool | 100 | 107/1056 (0.101325757576) | 0.111742424242 | 0.250000000000 | 0.509469696970 |
| hierarchical_first_100 | candidate_pool | 200 | 280/1056 (0.265151515152) | 0.317234848485 | 0.482954545455 | 0.782196969697 |
| hierarchical_80_dual_backfill_20 | candidate_pool | 50 | 96/1056 (0.090909090909) | 0.100378787879 | 0.181818181818 | 0.377840909091 |
| hierarchical_80_dual_backfill_20 | candidate_pool | 100 | 107/1056 (0.101325757576) | 0.111742424242 | 0.250000000000 | 0.509469696970 |
| hierarchical_80_dual_backfill_20 | candidate_pool | 200 | 321/1056 (0.303977272727) | 0.343750000000 | 0.500946969697 | 0.767045454545 |
| hierarchical_70_dual_backfill_30 | candidate_pool | 50 | 96/1056 (0.090909090909) | 0.100378787879 | 0.181818181818 | 0.377840909091 |
| hierarchical_70_dual_backfill_30 | candidate_pool | 100 | 108/1056 (0.102272727273) | 0.112689393939 | 0.250946969697 | 0.509469696970 |
| hierarchical_70_dual_backfill_30 | candidate_pool | 200 | 321/1056 (0.303977272727) | 0.343750000000 | 0.500946969697 | 0.767045454545 |
| diagnostic_union_hierarchical_dual | diagnostic_union | 50 | 99/1056 (0.093750000000) | 0.102272727273 | 0.187500000000 | 0.392992424242 |
| diagnostic_union_hierarchical_dual | diagnostic_union | 100 | 113/1056 (0.107007575758) | 0.119318181818 | 0.257575757576 | 0.551136363636 |
| diagnostic_union_hierarchical_dual | diagnostic_union | 200 | 322/1056 (0.304924242424) | 0.348484848485 | 0.514204545455 | 0.783143939394 |

## HE2

- HE2-A ranking temprano: se determina desde la tabla de rankings sin convertir pools en rankings.
- HE2-B cobertura profunda: se determina desde PoolRecall y la unión diagnóstica a 100/200, sin selección posterior de variantes.
