# EXP-08: sensibilidad v0.1 vs v0.2

## Alcance

Comparacion descriptiva de configuraciones congeladas y globalmente no pareada: v0.1 contiene 1006 casos y v0.2 contiene 1056. No son evalsets equivalentes, no se realizan pruebas inferenciales y no se atribuyen efectos causales exclusivamente a la politica de split. v0.2 permanece como benchmark final.

## Resultados globales

| Metrica | v0.1 | v0.2 | Delta v0.2-v0.1 |
|---|---:|---:|---:|
| Top1 | 0.862823 | 0.509470 | -35.335 pp |
| Top3 | 0.937376 | 0.671402 | -26.597 pp |
| MRR | 0.906239 | 0.629708 | -0.276532 |

## Independencia, duplicados y cobertura

El solapamiento DAM historico-evaluacion cambia de 995/1006 en v0.1 a 0/1056 en v0.2. Los duplicados exactos pasan de 377/1006 (376 misma NANDINA; 358 exactos de misma DAM) a 35/1056 (34 misma NANDINA; 1 diferente). Los near-duplicates v0.2 congelados son umbrales: >=0.90: 55, >=0.95: 44 y >=0.98: 37; no son categorias de etiqueta. La cobertura nominal por NANDINA se reconcilia contra el banco historico de cada version y la sensibilidad por codigo contiene una fila por cada NANDINA de la union de evalsets, sin ocultar denominadores pequenos.

## Estratos y HE

El rendimiento estratificado v0.2 usa banderas congeladas: exactos 35, no exactos 1021, near >=0.95 44 y resto 1012. Las banderas de duplicados por caso no se preservaron en v0.1, por lo que esos estratos se declaran `NOT_AVAILABLE`; el estrato DAM se obtiene por membership de splits congelados. HE2 no se reabre. HE5 conserva cuatro componentes y queda `PARTIALLY_SUPPORTED`: calidad descriptiva no evaluada; proximidad jerarquica apoyada; precedentes con evidencia mixta/no monotona; alcance interno con sensibilidad a configuracion experimental.

## Limitaciones de comparabilidad

La trazabilidad de v0.1 usa `historical_metrics.json`, pero falta `run_metadata.json` (`V01_METADATA_PROVENANCE_LIMITATION`). Ademas, la profundidad de ranking difiere: 200 en v0.1 y 100 en v0.2. Estas limitaciones impiden atribuir los deltas exclusivamente al split.
