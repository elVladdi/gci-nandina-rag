# G5-F02 — Tablas canónicas y control numérico

**Estado:** `PROSPECTIVE / NOT_AUTHORIZED`

## Objetivo

Materializar las tablas científicas desde outputs congelados y verificar que cada cifra reproduce exactamente la fuente aprobada.

## Obligatorio

- generar tablas por script o transformación trazable cuando sea posible;
- ledger `celda/valor → archivo fuente → campo/fórmula`;
- unidades, decimales y N consistentes;
- usar Attempt06 corregido;
- no copiar manualmente números sin trazabilidad.

## Outputs

- tablas canónicas CSV/Markdown según registro G5-F01;
- `outputs/results/group5/g5_numeric_crosscheck_v0.1.json`.

## PASS

Cero discrepancias numéricas no explicadas y cero valores provenientes de outputs supersedidos.

**Siguiente:** G5-F03.
