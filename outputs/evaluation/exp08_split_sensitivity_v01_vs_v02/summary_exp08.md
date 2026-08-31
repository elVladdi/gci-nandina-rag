# Resumen EXP-08

Objetivo: describir la sensibilidad entre el split previo v0.1 por serie y el split final v0.2 agrupado por DAM, sin reejecutar retrieval.

v0.1/v0.2: Top1 0.862823/0.509470 (delta -35.335 pp), Top3 0.937376/0.671402 (delta -26.597 pp), MRR 0.906239/0.629708 (delta -0.276532).

DAM overlap: 995/1006 en v0.1 frente a 0/1056 en v0.2. Duplicados exactos: 377/1006 frente a 35/1056. Near-duplicates v0.2: >=0.90 55, >=0.95 44, >=0.98 37.

Limitaciones: los evalsets no son equivalentes, la comparacion no es pareada, v0.1 carece de run_metadata.json y la profundidad difiere (200 frente a 100). HE5 se mantiene PARTIALLY_SUPPORTED. Gate corrective microclose APPROVED; v0.2 permanece benchmark final interno.
