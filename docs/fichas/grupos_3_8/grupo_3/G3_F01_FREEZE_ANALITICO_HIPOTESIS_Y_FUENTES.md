# G3-F01 — Freeze analítico, hipótesis y fuentes

**Estado:** `PROSPECTIVE / NOT_AUTHORIZED`

## Objetivo

Congelar el contrato de Grupo 3 antes de calcular inferencia: texto exacto de HE2/HE5, poblaciones, unidades, métricas, comparaciones, dependencias y resultados válidos.

## Obligatorio

- exigir Grupo 2B `CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS` integrado;
- leer el proyecto de tesis aprobado para recuperar HE2/HE5 literalmente; si no está accesible, `BLOCKED`;
- inventariar resultados finales elegibles: Grupo 1, EXP11A, EXP11B, Attempt06 corregido y cierre EXP12;
- fijar SERIE como unidad de análisis y DAM/DECLARACIÓN como agrupamiento cuando haya dependencia;
- registrar para cada contraste: población, estimando, métrica, dirección, unidad inferencial, exclusiones ya congeladas y multiplicidad;
- marcar EXP12 como `NOT_ESTIMABLE` para efecto de diversidad;
- preservar que EXP11A es sensibilidad, no causalidad aislada.

## Prohibido

Calcular p-values, cambiar hipótesis, inventar HE2/HE5, reejecutar retrieval o seleccionar pruebas después de observar un resultado inferencial.

## Outputs

- `outputs/analysis/group3/g3_analytical_contract_v0.1.json`
- `docs/analysis/group3/g3_analytical_contract_v0.1.md`

## PASS

Todas las hipótesis y contrastes están trazados a fuentes primarias, no existe población ambigua y cada familia de resultados tiene status `ELIGIBLE`, `DESCRIPTIVE_ONLY`, `NOT_ESTIMABLE` o `NOT_APPLICABLE`.

**Siguiente:** G3-F02.
