# G3-F04 — Decisión HE2/HE5 y cierre de Grupo 3

**Estado:** `PROSPECTIVE / NOT_AUTHORIZED`

## Objetivo

Traducir los resultados inferenciales aprobados en decisiones explícitas sobre HE2/HE5 sin exceder la regla decisional congelada.

## Obligatorio

- usar el texto literal y criterio de G3-F01;
- emitir para cada hipótesis: `SUPPORTED`, `NOT_SUPPORTED`, `INCONCLUSIVE` o la nomenclatura aprobada por el proyecto; no forzar decisión binaria si el protocolo no la soporta;
- separar evidencia primaria, sensibilidad, diagnósticos y limitaciones;
- registrar que EXP12 no aporta estimación de diversidad;
- producir un claim registry para Grupos 4–8.

## Outputs

- `outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json`
- `docs/analysis/group3/g3_claim_registry_v0.1.md`
- `outputs/audits/group3_closure_v0.1.json`

## PASS

Todas las decisiones son trazables a un contraste aprobado, las limitaciones están explícitas y no quedan cálculos inferenciales pendientes.

**Estado terminal:** `GROUP3=CLOSED / APPROVED` tras auditoría externa.

**Siguiente:** G4-F01.
