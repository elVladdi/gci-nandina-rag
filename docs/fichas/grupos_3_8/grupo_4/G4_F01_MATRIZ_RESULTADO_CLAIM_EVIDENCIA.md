# G4-F01 — Matriz resultado → claim → evidencia

**Estado:** `PROSPECTIVE / NOT_AUTHORIZED`

## Objetivo

Convertir el cierre inferencial de Grupo 3 en un conjunto controlado de afirmaciones interpretables.

## Obligatorio

Para cada resultado relevante registrar: fuente, cifra, incertidumbre, claim permitido, fuerza del claim, causalidad/no causalidad, limitación y sección candidata de tesis/artículo.

Deben aparecer como límites explícitos: EXP11A no causal, EXP12 no estimable, retrieval histórico ≠ exactitud global del RAG, evidencia normativa ≠ corrección jurídica, explicación auditable ≠ clasificación legalmente correcta.

## Output

`outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv` y versión JSON.

## PASS

Cero claims sin evidencia y cero claims más fuertes que el resultado que los soporta.

**Siguiente:** G4-F02.
