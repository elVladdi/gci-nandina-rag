# Evaluacion BM25 hierarchy ablation devset v0.1

## Objetivo

Ejecutar la Fase 6B-2: ablation de composicion jerarquica y ponderacion del texto indexado NANDINA para BM25, usando solo el devset intermedio de 13 casos.

## Motivacion

El corpus jerarquico v0.1 mejoro recall y Top-10, pero tambien introdujo ruido de padres generales. Esta ablation separa hoja, 4D, HS6, capitulo y repeticion de hoja para ver que composicion conserva las mejoras sin degradar casos sensibles.

## Variantes

- A_leaf_only: solo descripcion NANDINA8.
- B_4d_leaf: partida 4D + NANDINA8.
- C_hs6_leaf: HS6 + NANDINA8; si no hay HS6, solo hoja.
- D_4d_hs6_leaf: 4D + HS6 + NANDINA8.
- E_4d_hs6_leaf_weighted: 4D + HS6 + hoja repetida.
- F_hs6_leaf_weighted: HS6 + hoja repetida.
- G_chapter_4d_hs6_leaf_weighted: capitulo + 4D + HS6 + hoja repetida.

## Metricas

| Metodo | Top-1 | Top-3 | Top-5 | Top-10 | MRR | Recall@50 | Recall@100 | Top-10 HS4 | Top-10 HS2 | NF | Sev vs flat | Sev vs hier |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| BM25_flat_current | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4370 | 0.6154 | 0.6154 | 0.8462 | 0.8462 | 5 | 0 | 2 |
| BM25_hierarchical_v0.1 | 0.3846 | 0.5385 | 0.6154 | 0.6154 | 0.4701 | 0.6923 | 0.6923 | 0.7692 | 0.7692 | 4 | 1 | 0 |
| A_leaf_only | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4370 | 0.6154 | 0.6154 | 0.7692 | 0.7692 | 5 | 0 | 2 |
| B_4d_leaf | 0.3077 | 0.5385 | 0.6154 | 0.6154 | 0.4304 | 0.6154 | 0.6923 | 0.8462 | 0.8462 | 4 | 1 | 1 |
| C_hs6_leaf | 0.4615 | 0.4615 | 0.4615 | 0.5385 | 0.4754 | 0.6154 | 0.6154 | 0.7692 | 0.7692 | 5 | 0 | 2 |
| D_4d_hs6_leaf | 0.3077 | 0.5385 | 0.6154 | 0.6154 | 0.4265 | 0.6154 | 0.6923 | 0.8462 | 0.8462 | 4 | 1 | 1 |
| E_4d_hs6_leaf_weighted | 0.3077 | 0.5385 | 0.5385 | 0.6154 | 0.4126 | 0.6923 | 0.6923 | 0.8462 | 0.8462 | 4 | 1 | 0 |
| F_hs6_leaf_weighted | 0.3846 | 0.4615 | 0.4615 | 0.5385 | 0.4367 | 0.6154 | 0.6154 | 0.7692 | 0.7692 | 5 | 0 | 2 |
| G_chapter_4d_hs6_leaf_weighted | 0.3077 | 0.5385 | 0.5385 | 0.6154 | 0.4256 | 0.6923 | 0.6923 | 0.8462 | 0.8462 | 4 | 1 | 0 |

## Matriz de ranks

| Caso | NANDINA | BM25_flat_current | BM25_hierarchical_v0.1 | A_leaf_only | B_4d_leaf | C_hs6_leaf | D_4d_hs6_leaf | E_4d_hs6_leaf_weighted | F_hs6_leaf_weighted | G_chapter_4d_hs6_leaf_weighted |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dev-01 | 84713000 | 1 | 1 | 1 | 2 | 1 | 2 | 2 | 1 | 2 |
| dev-02 | 10063000 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| dev-03 | 04029110 | 2 | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 |
| dev-04 | 22030000 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| dev-05 | 39012000 | 1 | 36 | 1 | 0 | 1 | 0 | 33 | 1 | 30 |
| dev-06 | 02013000 | 8 | 1 | 8 | 1 | 8 | 1 | 1 | 8 | 1 |
| dev-07 | 84713000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dev-08 | 84717000 | 0 | 0 | 0 | 84 | 0 | 86 | 0 | 0 | 0 |
| dev-09 | 85414100 | 1 | 2 | 1 | 2 | 1 | 2 | 3 | 1 | 2 |
| dev-10 | 63064000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| dev-11 | 95030010 | 18 | 3 | 18 | 4 | 18 | 5 | 6 | 19 | 6 |
| dev-12 | 28151100 | 0 | 4 | 0 | 3 | 0 | 3 | 3 | 0 | 3 |
| dev-13 | 84713000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Casos criticos

Los casos criticos completos quedan en `ablation_critical_cases.csv`. En esta corrida se rastrearon 39012000, 85414100, 28151100, 02013000, 95030010, 84717000, 63064000 y el smoke test de 83022000 para `ruedas`.

## Smoke tests

- `soda caustica solida`: revisar `ablation_smoke_tests.json` para el rank de 28151100 por metodo.
- `ruedas`: revisar `ablation_smoke_tests.json` para el rank de 83022000 por metodo.

## Decision metodologica

Variante candidata para congelar: `ninguna`.
Mejor trade-off exploratorio: `C_hs6_leaf`.
Best trade-off is ordered by Top-1 non-regression, broad metric improvement, severe degradations, Top-10, MRR and Recall. A freeze candidate is declared only if it also preserves the critical flat wins and hierarchical wins.

## Recomendacion

No escalar al evalset todavia. Ninguna variante domina claramente bajo todos los criterios; conviene una siguiente iteracion hibrida o de ponderacion mas fina.

## Limitaciones

- Devset pequeno de 13 casos; no se ejecuto evalset.
- La repeticion de hoja es una ponderacion lexical simple, no un re-ranker.
- No se ejecuto LLM, Text2Trade ni evidencia documental Arancel/RGI/notas.
