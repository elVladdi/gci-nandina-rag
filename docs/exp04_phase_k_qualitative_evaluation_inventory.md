# EXP-04 Fase K: inventario de evaluacion cualitativa HE4 v0.2

## Modalidad auditada

La modalidad historica es **A. revision humana/manual**. `docs/revision_cualitativa_fichas_auditables_v0.1.md` contiene revision narrativa por ficha y la rubrica fuente describe calidad para auditoria humana. No se identifico una operacionalizacion deterministica 0-2 por las ocho dimensiones ni un LLM-as-judge preespecificado.

Por ello esta fase prepara el paquete ciego y no asigna puntuaciones. El scoring queda a cargo de un revisor humano no asignado.

## Contrato congelado

- Rubrica: `src/configs/he4_rubric_v0.2.json`.
- Ocho dimensiones, escala 0-2, total maximo 16.
- Una ficha es auditable solo con >=12/16 y sin hard violation.
- Los labels, ranks de referencia y buckets se excluyen del paquete humano.
- `advertencias_globales` se excluye del scoring por `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`.

## Estado

`GATE K = PENDING HUMAN SCORING`. No se aplico la rubrica, no se llamo modelo, no hubo retrieval ni evidencia externa, y Fase L permanece bloqueada.
