# Mapa maestro de fichas — Grupos 3 a 8

## Regla de secuencia

Ninguna ficha puede ejecutarse antes del cierre auditado de su predecesora. Las fichas son prospectivas y se activan una por una.

| Orden | Ficha | Propósito | Salida principal |
|---|---|---|---|
| 1 | G3-F01 | Freeze analítico, hipótesis y fuentes | contrato analítico congelado |
| 2 | G3-F02 | Registro maestro de métricas/poblaciones | matriz métrica-inferencia |
| 3 | G3-F03 | Inferencia y sensibilidad sobre evidencia válida | resultados inferenciales auditables |
| 4 | G3-F04 | Decisión HE2/HE5 y cierre Grupo 3 | disposition inferencial |
| 5 | G4-F01 | Matriz resultado→claim→evidencia | claim interpretation registry |
| 6 | G4-F02 | Interpretación integrada y límites | síntesis interpretativa |
| 7 | G4-F03 | Discusión comparativa y cierre | cierre Grupo 4 |
| 8 | G5-F01 | Arquitectura de presentación | plan de tablas/resultados |
| 9 | G5-F02 | Tablas canónicas y control numérico | tablas maestras congeladas |
| 10 | G5-F03 | Anexos/suplementos y cierre | paquete de presentación |
| 11 | G6-F01 | Catálogo y especificación de figuras | figure specification registry |
| 12 | G6-F02 | Generación reproducible de figuras | figuras candidatas + fuentes |
| 13 | G6-F03 | Captions, accesibilidad y cierre | paquete gráfico aprobado |
| 14 | G7-F01 | Sincronización editorial y contrato de redacción | writing source freeze |
| 15 | G7-F02 | Redacción/actualización de tesis | candidato de secciones de tesis |
| 16 | G7-F03 | Redacción/actualización del artículo y cierre | candidato editorial aprobado |
| 17 | G8-F01 | Auditoría claim→evidencia y numérica | matriz final de inconsistencias |
| 18 | G8-F02 | Coherencia Métodos–Resultados–Discusión | reconciliación documental |
| 19 | G8-F03 | Auditoría pre-freeze y cierre Grupo 8 | freeze-readiness decision |

Después de G8-F03 aplica `99_POST_G8_FREEZE_HANDOFF.md`.

## Estados permitidos

`PROSPECTIVE`, `READY_FOR_ACTIVATION`, `ACTIVE`, `CANDIDATE_PENDING_EXTERNAL_AUDIT`, `REVISION_REQUIRED`, `APPROVED`, `CLOSED`, `BLOCKED`.
