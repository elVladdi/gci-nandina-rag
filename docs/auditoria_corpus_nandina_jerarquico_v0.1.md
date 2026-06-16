# Auditoria corpus NANDINA jerarquico v0.1

## Objetivo

Auditar si `data/processed/corpus/nandina/nandina_corpus.jsonl` permite construir un corpus NANDINA8 autocontenido con contexto jerarquico 4D/6D/8D, sin modificar el corpus plano ni el indice BM25 vigente.

## Archivo auditado

- Input: `data/processed/corpus/nandina/nandina_corpus.jsonl`.
- SHA256: `4f5f2d33e864ee2d5992e76e68b7a7fa1163f98564b79d2533f5131acb5ace58`.

## Conteos

- Total de registros: 9785.
- `partida_4d`: 1020.
- `hs_6d`: 1117.
- `nandina_8d`: 7648.
- Descripciones vacias: 1.
- Descripciones muy cortas: 3161.

## Problemas detectados

- NANDINA8 sin padre 4D: 407.
- NANDINA8 sin padre HS6 explicito: 4504.
- Padres duplicados conflictivos: 56.
- Saltos de orden detectados: 25 ejemplos muestreados.
- Descripciones con posible encabezado contaminante: 17.
- Descripciones genericas o muy cortas listadas: 3498.

## Evidencia de jerarquia

El corpus trae `section`, `section_title`, `chapter` y `chapter_title` en los registros. La relacion 8D -> 4D se reconstruye por prefijo en la mayoria de los casos. La relacion 8D -> HS6 solo existe cuando hay un registro `hs_6d` con el mismo prefijo de seis digitos; muchos codigos 8D dependen directamente de una partida 4D o de subtitulos que quedaron embebidos en la descripcion 4D.

## Ejemplos positivos

| NANDINA8 | Partida 4D | HS6 | Descripcion 8D | Contexto 4D |
|---|---|---|---|---|
| 01012100 | 0101 |  | Reproductores de raza pura | Caballos, asnos, mulos y burdéganos, vivos. - Caballos: |
| 01012910 | 0101 | 010129 | Para carrera | Caballos, asnos, mulos y burdéganos, vivos. - Caballos: |
| 01012990 | 0101 | 010129 | Los demás | Caballos, asnos, mulos y burdéganos, vivos. - Caballos: |
| 01013000 | 0101 |  | Asnos | Caballos, asnos, mulos y burdéganos, vivos. - Caballos: |
| 01019000 | 0101 |  | Los demás | Caballos, asnos, mulos y burdéganos, vivos. - Caballos: |
| 01022100 | 0102 |  | Reproductores de raza pura | Animales vivos de la especie bovina. |
| 01022910 | 0102 | 010229 | Para lidia | Animales vivos de la especie bovina. |
| 01022990 | 0102 | 010229 | Los demás | Animales vivos de la especie bovina. |
| 01023100 | 0102 |  | Reproductores de raza pura | Animales vivos de la especie bovina. |
| 01023900 | 0102 |  | Los demás | Animales vivos de la especie bovina. |

## Decision metodologica

Si es posible construir una primera version del corpus jerarquico desde este JSONL. La construccion debe conservar advertencias: los padres HS6 faltan con frecuencia y algunas descripciones 4D tienen texto contaminado por encabezados o notas de extraccion. No hace falta volver al PDF/notebook para una v0.1 de ranking inicial, pero si conviene hacerlo despues si se busca una jerarquia HS6 completa y limpia.

## Archivos de auditoria

- `outputs/corpus/auditoria_nandina_jerarquica_v0.1/audit_summary.json`.
- `outputs/corpus/auditoria_nandina_jerarquica_v0.1/missing_parents.csv`.
- `outputs/corpus/auditoria_nandina_jerarquica_v0.1/generic_descriptions.csv`.
- `outputs/corpus/auditoria_nandina_jerarquica_v0.1/hierarchy_examples.csv`.
